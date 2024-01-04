import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler

ensemble_model = joblib.load('./DisPred_App/ensemble_model.joblib')
rs = joblib.load("rs_diabetes.joblib")

# Web uygulamasını oluşturma
st.title("Diyabet Tahmin Uygulaması")

# Kullanıcıdan giriş alalım
Cholesterol = st.number_input("Cholesterol", min_value=0, max_value=500, value=150)
Glucose = st.number_input("Glucose", min_value=0, max_value=500, value=100)
HDL_Chol = st.number_input("HDL_Chol", min_value=0, max_value=400, value=50)
Chol_HDL_ratio = Cholesterol / HDL_Chol
Age = st.number_input("Age", min_value=0, max_value=120, value=30)
Gender_mapping = {"Male": 1, "Female": 0}
Gender = st.selectbox("Gender", ["Male", "Female"])
Gender_encoded = Gender_mapping[Gender]
Height = st.number_input("Height", min_value=50, max_value=300, value=170)
Weight = st.number_input("Weight", min_value=10, max_value=300, value=70)
BMI = (Weight / (Height / 100) ** 2)
Systolic_BP = st.number_input("Systolic_BP", min_value=0, max_value=400, value=120)
Diastolic_BP = st.number_input("Diastolic_BP", min_value=0, max_value=400, value=80)
waist = st.number_input("waist", min_value=0, max_value=300, value=80)
hip = st.number_input("hip", min_value=0, max_value=300, value=90)
Waist_hip_ratio = waist / hip
insert_index=5
# Kullanıcının girdiği verileri bir veri çerçevesine yerleştirelim
input_data=([[Cholesterol,Glucose,HDL_Chol,Chol_HDL_ratio,Age,Height,Weight,BMI,Systolic_BP,Diastolic_BP,waist,hip,Waist_hip_ratio]])

input_data_scaled = rs.transform(input_data)
input_data_scaled=np.insert(input_data_scaled, insert_index, Gender_encoded, axis=1)
# Tahmin butonu
if st.button("Tahmin Et"):
    # Kullanıcının girdiği veri üzerinde tahmin yapalım
    prediction = ensemble_model.predict(input_data_scaled)
    st.subheader("Giriş Verileri")
    st.write(input_data_scaled)
    # Tahmini ekrana yazdıralım
    st.subheader("Tahmin Sonucu")
    if prediction[0] == 1:
        st.write("Diyabet olma olasılığı yüksek.")
    else:
        st.write("Diyabet olma olasılığı düşük.")