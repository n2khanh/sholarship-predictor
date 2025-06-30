# 🎓 Scholarship Predictor

A machine learning web application that predicts the probability of receiving a scholarship based on academic and extracurricular profile.

## 📌 Features

- 💡 Predicts scholarship probability (0%–100%) using regression model
- 🧠 Trained with RandomForestRegressor (with GridSearchCV tuning)
- 📈 Provides evaluation metrics (R², RMSE) and visualizations
- 🌐 User-friendly Streamlit web interface

---

## 📊 Input Features

| Feature              | Description                                |
|----------------------|--------------------------------------------|
| GRE Score            | Graduate Record Exam (out of 340)          |
| TOEFL Score          | TOEFL English Test Score (out of 120)      |
| University Rating    | Rating of target university (1–5)          |
| SOP Score            | Statement of Purpose score (1.0–5.0)       |
| LOR Score            | Letter of Recommendation score (1.0–5.0)   |
| CGPA                 | Undergraduate GPA (0.0–10.0)               |
| Research             | 1 if has research experience, else 0       |
| Publications         | Number of research publications            |

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/scholarship-predictor.git
cd scholarship-predictor
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Prepare Data
Place your dataset in the data/ folder. Use a CSV file with appropriate columns.

Example:

bash
Copy
Edit
data/admission_data.csv
4. Train the Model
bash
Copy
Edit
python main.py
This will:

Preprocess data

Train the model

Save the model & scaler to models/

5. Run the Web App
bash
Copy
Edit
streamlit run app/app.py
Then visit: http://localhost:8501