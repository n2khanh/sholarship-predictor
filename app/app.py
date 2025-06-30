import streamlit as st
import joblib
import numpy as np
import os

# Load model và scaler
MODEL_PATH = "models/best_model.pkl"
SCALER_PATH = "models/scaler.pkl"

if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
    st.error("Model hoặc scaler chưa được tạo. Hãy chạy main.py trước.")
    st.stop()

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Giao diện
st.title("🎓 Scholarship Prediction App")
st.markdown("Dự đoán khả năng nhận học bổng dựa trên thông tin học tập.")

# Nhập thông tin
gre = st.slider("GRE Score", 290, 340, 320)
toefl = st.slider("TOEFL Score", 60, 120, 100)
univ_rating = st.slider("University Rating (1–5)", 1, 5, 3)
sop = st.slider("SOP Score", 1.0, 5.0, 3.0)
lor = st.slider("LOR Score", 1.0, 5.0, 3.0)
cgpa = st.slider("CGPA (0.0–10.0)", 6.0, 10.0, 8.5)
research = st.selectbox("Research (0 = No, 1 = Yes)", [0, 1])


if st.button("🔮 Dự đoán"):
    input_data = np.array([[gre, toefl, univ_rating, sop, lor, cgpa, research]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    st.success(f"🎯 Xác suất nhận học bổng: {prediction * 100:.2f}%")
