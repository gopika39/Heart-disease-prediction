from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import pickle
import numpy as np
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secretkey"

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ------------------------- DATABASE -------------------------
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    patient_name TEXT,
                    age INTEGER,
                    risk_level TEXT,
                    probability REAL,
                    date TEXT,
                    time TEXT
                )''')
    conn.commit()
    conn.close()

init_db()

# ------------------------- ROUTES -------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            flash("Please enter username and password")
            return redirect(url_for("register"))

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        if c.fetchone():
            flash("Username already exists! Please login.")
            conn.close()
            return redirect(url_for("register"))

        hashed_pw = generate_password_hash(password)
        c.execute("INSERT INTO users (username, password) VALUES (?,?)", (username, hashed_pw))
        conn.commit()
        conn.close()
        flash("Registered successfully! Please login.")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            flash("Please enter username and password")
            return redirect(url_for("login"))

        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session["user"] = username
            flash("Logged in successfully")
            return redirect(url_for("prediction"))
        else:
            flash("Invalid username or password")
            return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out")
    return redirect(url_for("home"))

@app.route("/prediction")
def prediction():
    if "user" not in session:
        flash("Please login first")
        return redirect(url_for("login"))
    return render_template("prediction.html", username=session["user"])

@app.route("/patient")
def patient():
    if "user" not in session:
        flash("Please login first")
        return redirect(url_for("login"))
    return render_template("patient.html")

@app.route("/history")
def history():
    if "user" not in session:
        flash("Please login first")
        return redirect(url_for("login"))
    
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT patient_name, age, risk_level, date, time FROM history WHERE user_id=? ORDER BY id DESC", (session["user"],))
    records = c.fetchall()
    conn.close()
    
    return render_template("history.html", history=records)

@app.route("/predict", methods=["POST"])
def predict():
    if "user" not in session:
        return {"error": "Unauthorized"}, 401
        
    data = request.json
    try:
        # Mandatory fields check
        features_list = [
            float(data["age"]),
            float(data["gender"]),
            float(data["bmi"]),
            float(data["systolic_bp"]),
            float(data["diastolic_bp"]),
            float(data["max_heart_rate"]),
            float(data["cholesterol"]),
            float(data["ldl"]),
            float(data["hdl"]),
            float(data["triglycerides"]),
            float(data["blood_sugar"]),
            float(data["fever"]),
            float(data["chest_pain"]),
            float(data["shortness_of_breath"]),
            float(data["ecg_abnormality"]),
            float(data["troponin_level"]),
            float(data["smoking"]),
            float(data["diabetes"]),
            float(data["hypertension"]),
            float(data["heart_history"])
        ]
    except KeyError as e:
        return {"error": f"Missing field: {str(e)}"}, 400
    except ValueError:
        return {"error": "Invalid input values"}, 400

    features = np.array([features_list])
    features = scaler.transform(features)
    probability = model.predict_proba(features)[0][1]

    if probability > 0.7:
        risk = "High Risk"
    elif probability > 0.4:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    # Save to History
    from datetime import datetime
    now = datetime.now()
    
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''INSERT INTO history (user_id, patient_name, age, risk_level, probability, date, time)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
              (session["user"], data.get("patient_name", "Unknown"), int(data["age"]), 
               risk, round(probability * 100, 2), now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")))
    conn.commit()
    conn.close()

    return {
        "risk": risk,
        "probability": round(probability * 100, 2)
    }

if __name__ == "__main__":
    app.run(debug=True)
