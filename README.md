# ✈️ AI-Enabled Visa Processing Time Predictor

This project uses **Machine Learning** to estimate how long a visa application might take to be processed based on applicant and application details.

It aims to reduce uncertainty for applicants by providing **data-driven predictions** of visa processing times.

---

## 📌 Project Objective

Visa applicants often face long waiting times and uncertainty.  
This project builds a predictive system that:

✔ Estimates visa processing time  
✔ Analyzes trends across visa types and countries  
✔ Provides a future-ready foundation for a web-based estimator tool  

---

## 📊 Dataset

Due to privacy restrictions, real applicant-level visa records are not publicly available.  
Therefore, this project uses a **synthetic dataset** designed based on realistic immigration trends.

The dataset contains:

- Application Date  
- Decision Date  
- Applicant Country  
- Visa Type (Student, Tourist, Work)  
- Processing Office  

From this, we calculate:

**Processing Time (in days)** = Decision Date − Application Date

---

## 🧹 Milestone 1 — Data Collection & Preprocessing

✔ Created a structured visa application dataset  
✔ Converted date columns into datetime format  
✔ Calculated visa processing time in days  
✔ Removed missing values  
✔ Saved cleaned dataset for modeling  

Files:
- `data/visa_data.csv` → Raw dataset  
- `data/visa_data_cleaned.csv` → Preprocessed dataset  
- `src/preprocessing.py` → Data cleaning script  

---

## 🧠 Upcoming Milestones

🔹 **Milestone 2:** Exploratory Data Analysis (EDA)  
🔹 **Milestone 3:** Machine Learning Model Training  
🔹 **Milestone 4:** Web Application for Visa Time Prediction  

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib / Seaborn (for visualization)  
- Flask (for web app in later stages)

---

## 🚀 How to Run Preprocessing

```bash
python src/preprocessing.py
