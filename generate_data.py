import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

def generate_heart_data(n=1000):
    data = []
    
    for i in range(1, n + 1):
        age = np.random.randint(20, 90)
        gender = np.random.choice([0, 1])  # 0: Female, 1: Male
        bmi = np.random.uniform(18, 40)
        systolic_bp = np.random.randint(90, 200)
        diastolic_bp = np.random.randint(60, 130)
        max_heart_rate = np.random.randint(100, 210)
        cholesterol = np.random.randint(150, 300)
        ldl = np.random.randint(70, 190)
        hdl = np.random.randint(30, 80)
        triglycerides = np.random.randint(100, 250)
        blood_sugar = np.random.randint(70, 200)
        fever = np.random.choice([0, 1], p=[0.9, 0.1])
        chest_pain = np.random.choice([0, 1, 2, 3])
        shortness_of_breath = np.random.choice([0, 1])
        ecg_abnormality = np.random.choice([0, 1])
        troponin_level = np.random.uniform(0.0, 0.5)
        smoking = np.random.choice([0, 1])
        diabetes = np.random.choice([0, 1])
        hypertension = 1 if systolic_bp > 140 else 0
        heart_history = np.random.choice([0, 1])
        
        # Simple rule-based target generation for a correlated dataset
        risk_score = (
            (age > 60) * 0.2 +
            (bmi > 30) * 0.15 +
            (systolic_bp > 150) * 0.2 +
            (cholesterol > 240) * 0.1 +
            (smoking == 1) * 0.1 +
            (diabetes == 1) * 0.1 +
            (heart_history == 1) * 0.15 +
            (troponin_level > 0.1) * 0.2
        )
        
        target = 1 if risk_score + np.random.normal(0, 0.1) > 0.5 else 0
        
        data.append([
            i, age, gender, bmi, systolic_bp, diastolic_bp, max_heart_rate,
            cholesterol, ldl, hdl, triglycerides, blood_sugar, fever,
            chest_pain, shortness_of_breath, ecg_abnormality, troponin_level,
            smoking, diabetes, hypertension, heart_history, target
        ])

    columns = [
        "PatientID", "Age", "Gender", "BMI", "SystolicBP", "DiastolicBP", 
        "MaxHeartRate", "Cholesterol", "LDL", "HDL", "Triglycerides", 
        "BloodSugar", "Fever", "ChestPain", "ShortnessOfBreath", 
        "ECG_Abnormality", "TroponinLevel", "Smoking", "Diabetes", 
        "Hypertension", "HistoryHeart", "target"
    ]
    
    df = pd.DataFrame(data, columns=columns)
    df.to_csv("heart_v2.csv", index=False)
    print(f"Generated {n} rows in heart_v2.csv")

if __name__ == "__main__":
    generate_heart_data()
