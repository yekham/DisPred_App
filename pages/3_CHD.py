import streamlit as st
import pandas as pd
from sklearn.preprocessing import RobustScaler
import joblib
import numpy as np



xgb_model = joblib.load("DisPred_App\xgb_model.joblib")
rs = joblib.load("DisPred_App\pages\rs_CHD.joblib")


# Streamlit uygulama başlığı
st.title("Koroner Kalp Hastalığı Tahmin Uygulaması")

# Kullanıcıdan giriş verilerini al
Gender_mapping = {"Erkek": 1, "Kadın": 0}
Gender = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])
Gender_encoded = Gender_mapping[Gender]
age = st.number_input("Yaş", min_value=0, max_value=120, value=30)
Yn_mapping = {"Evet": 1, "Hayır": 0}
currentSmoker = st.selectbox("Şu an sigara içiyor mu?", ["Evet", "Hayır"])
smoker_encoded = Yn_mapping[currentSmoker]
cigsPerDay = st.number_input("Günde içilen sigara adedi", min_value=0, max_value=50, value=0)
BPMeds = st.selectbox("Tansiyon ilacı kullanıyor mu?", ["Evet", "Hayır"])
bpMeds_encoded = Yn_mapping[BPMeds]
prevalentStroke = st.selectbox("Daha önce felç geçirdi mi?", ["Evet", "Hayır"])
stroke_encoded = Yn_mapping[prevalentStroke]
prevalentHyp = st.selectbox("Yüksek tansiyonu var mı?", ["Evet", "Hayır"])
hyp_encoded = Yn_mapping[prevalentHyp]
diabetes = st.selectbox("Diyabet hastalığı var mı?", ["Evet", "Hayır"])
diabetes_encoded = Yn_mapping[diabetes]
totChol = st.number_input("Toplam Kolesterol", min_value=0, max_value=600, value=200)
sysBP = st.number_input("Sistolik Kan Basıncı", min_value=0, max_value=300, value=120)
diaBP = st.number_input("Diyastolik Kan Basıncı", min_value=0, max_value=200, value=80)
BMI = st.number_input("Vücut Kitle İndeksi (BMI)", min_value=10, max_value=50, value=25)
heartRate = st.number_input("Kalp Atış Hızı", min_value=0, max_value=200, value=70)
glucose = st.number_input("Kan Şeker Seviyesi", min_value=0, max_value=500, value=100)
insert_age=0
insert_currentSmoker=2
insert_bpMeds=4
insert_prevalentStroke=5
insert_prevalentHyp=6
insert_diabetes=7

input_data=([[age,cigsPerDay,totChol,sysBP,diaBP,BMI,heartRate,glucose]])
input_data_scaled = rs.transform(input_data)
input_data_scaled=np.insert(input_data_scaled, insert_age, Gender_encoded, axis=1)
input_data_scaled=np.insert(input_data_scaled, insert_currentSmoker, smoker_encoded, axis=1)
input_data_scaled=np.insert(input_data_scaled, insert_bpMeds, bpMeds_encoded, axis=1)
input_data_scaled=np.insert(input_data_scaled, insert_prevalentStroke, stroke_encoded, axis=1)
input_data_scaled=np.insert(input_data_scaled, insert_prevalentHyp, hyp_encoded, axis=1)
input_data_scaled=np.insert(input_data_scaled, insert_diabetes, diabetes_encoded, axis=1)

# Tahmin işlemi
if st.button("Tahmin Et"):
    prediction = xgb_model.predict(input_data_scaled)
    st.subheader("Giriş Verileri")
    st.write(input_data_scaled)
    st.subheader("Tahmin Sonucu")
    if prediction[0] == 1:
        st.write("Diyabet olma olasılığı yüksek.")
    else:
        st.write("Diyabet olma olasılığı düşük.")
