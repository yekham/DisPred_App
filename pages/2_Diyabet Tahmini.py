import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler
from PIL import Image
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


with open('models/ensemble_model.joblib', 'rb') as file:
    ensemble_model = joblib.load(file)

with open('models/rs_diabetes.joblib', 'rb') as file:
    rs = joblib.load(file)



st.image(Image.open("diabetes.png",use_column_width=True))
st.title("Diyabet Tahmini")

# Kullanıcıdan giriş alalım
Cholesterol = st.number_input("Toplam Kolesterol", min_value=0, max_value=500, value=150)
Glucose = st.number_input("Kan Şeker Seviyesi", min_value=0, max_value=500, value=100)
HDL_Chol = st.number_input("HDL Kolesterol", min_value=0, max_value=400, value=50)
Chol_HDL_ratio = Cholesterol / HDL_Chol
Age = st.number_input("Yaş", min_value=0, max_value=120, value=30)
Gender_mapping = {"Erkek": 1, "Kadın": 0}
Gender = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])
Gender_encoded = Gender_mapping[Gender]
Height = st.number_input("Boy", min_value=50, max_value=300, value=170)
Weight = st.number_input("Kilo", min_value=10, max_value=300, value=70)
BMI = (Weight / (Height / 100) ** 2)
Systolic_BP = st.number_input("Sistolik Kan Basıncı", min_value=0, max_value=400, value=120)
Diastolic_BP = st.number_input("Diyastolik Kan Basıncı", min_value=0, max_value=400, value=80)
waist = st.number_input("Bel çevre uzunluğu", min_value=0, max_value=300, value=80)
hip = st.number_input("Kalça çevre uzunluğu", min_value=0, max_value=300, value=90)
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
        diabetes_dig = "Tahminlerimize göre Diyabet hastalığı riski taşıyor."
        image = Image.open('positive.jpg')
        st.image(image, caption='')
    else:
        diabetes_dig = 'Harika. Diyabet hastalığı riski yok.'
        image = Image.open('negative.jpg')
        st.image(image, caption='')
    st.success(diabetes_dig)