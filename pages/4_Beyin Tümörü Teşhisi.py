import streamlit as st
from PIL import Image
import numpy as np
import tensorflow
import os
from tensorflow.keras.models import load_model

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


model = load_model("models/model.h5")
# Sınıf etiketlerini tanımla
labels = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']


def preprocess_image(image):
    # Giriş resmi boyutunu ve şeklini ayarla (224x224 piksel olarak)
    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = img_array.reshape(1, 224, 224, 3)
    return img_array

def predict_tumor(image):
    # Modeli kullanarak tahmin yap
    prediction = model.predict(image)

    # Tahmin edilen sınıf indeksi
    predicted_class_index = np.argmax(prediction)

    # Tahmin edilen sınıf etiketi
    predicted_class_label = labels[predicted_class_index]

    return predicted_class_label

st.image(Image.open("brain.png"))
st.title("Beyin Tümörü Tahmini")
uploaded_file = st.file_uploader("Teşhis etmek istediğiniz beyin MR dosyasını yükleyin", type=["jpg", "jpeg"])

if uploaded_file is not None:
    # Yüklenen dosyayı oku
    image = Image.open(uploaded_file)

    # Görüntüyü model için uygun formata getir
    img_array = preprocess_image(image)

    # Tahmin yap
    predicted_class = predict_tumor(img_array)

    # Sonucu göster
    st.image(image, use_column_width=True)
    if predicted_class == 'no_tumor':
        st.write("Tahmin edilen sınıf: no_tumor")
    elif predicted_class == 'meningioma_tumor':
        st.write("Tahmin edilen sınıf: meningioma_tumor")
    elif predicted_class == 'glioma_tumor':
        st.write("Tahmin edilen sınıf: glioma_tumor")
    else predicted_class == 'pituitary_tumor':
        st.write("Tahmin edilen sınıf: pituitary_tumor")


else:
    st.write("Lütfen bir resim dosyası yükleyin.")
