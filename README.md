# ❤️ Heart Disease Prediction System 

 # 🧠 Problem Description
One of the main causes of death in the world is heart disease. Taking preventative action and saving lives can be facilitated by early prediction and risk assessment.
--
The goal of this project is to create a web application that uses machine learning to determine a person's risk of heart disease based on medical parameters
--
### 📌 Overview of the Project
Flask was used to create this full-stack machine learning web application. 
The system predicts the probability of heart disease by processing user-provided medical data using a trained machine learning model.

Prediction history tracking and user authentication are also features of the application.
---
## 🚀 Features
- 🔐 User Login System

- ❤️ Heart Disease Risk Prediction
- 📊 Prediction History Page

- 💾 Model and Scaler Integration using Pickle
- 🎨 Clean and Responsive UI
- ⚡ Fast and Lightweight Flask Backend

## 🛠 Technologies Used

### 🔹 Backend
- Python
- Flask

### 🔹 Frontend
- HTML
- CSS
- JavaScript

### 🔹 Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Pickle (Model Serialization)

---

## ⚙ Backend Architecture

The backend is developed using Flask and handles:

- Routing between pages (`/`, `/login`, `/prediction`, `/history`)
- User authentication
- Receiving and validating user input
- Loading trained ML model (`model.pkl`)
- Applying feature scaling using saved scaler (`scaler.pkl`)
- Performing prediction
- Displaying prediction results
- Maintaining prediction history

---

## 🔄 Application Flow

1. User logs into the system.
2. User enters medical details (age, cholesterol, blood pressure, etc.).
3. Backend processes and scales the input data.
4. Trained ML model predicts heart disease risk.
5. Result is displayed to the user.
6. Prediction is stored and can be viewed in the history page.

---

## 📊 Machine Learning Model

The model was trained using a heart disease dataset with the following steps:

- Data Cleaning
- Feature Selection
- Feature Scaling (StandardScaler)
- Model Training
- Model Evaluation
- Model Serialization using Pickle

The trained model is saved as:
- `model.pkl`
- `scaler.pkl`

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository
```
git clone https://github.com/your-username/Heart-disease-prediction.git
```

### 2️⃣ Navigate to Project Folder
```
cd Heart-disease-prediction
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

(If no requirements file:)
```
pip install flask numpy pandas scikit-learn
```

### 4️⃣ Run the Application
```
python app.py
```

### 5️⃣ Open in Browser
```
http://127.0.0.1:5000/
```

---

## 📂 Project Structure

```
Heart-disease-prediction/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── prediction.html
│   └── history.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

## 🎯 Future Improvements
- Add user registration system
- Deploy the application using Render/Heroku
- Connect with a real database (MySQL / MongoDB)
- Improve UI with advanced styling
- Add more evaluation metrics visualization

---

## 👩‍💻 Author
**Gopika**

---

## ⭐ If you found this project useful
Please consider giving it a star on GitHub!
