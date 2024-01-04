import streamlit as st
import cv2
import numpy as np
from keras.models import load_model


# Modeli yükle


model = load_model("model.h5")

# Sınıf etiketlerini tanımla
labels = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']

def predict_tumor(image):
    # Giriş resmi boyutunu ve şeklini ayarla (150x150 piksel olarak)
    img = cv2.resize(image, (224, 224))
    img_array = np.array(img)
    img_array = img_array.reshape(1, 224, 224, 3)

    # Modeli kullanarak tahmin yap
    prediction = model.predict(img_array)

    # Tahmin edilen sınıf indeksi
    predicted_class_index = np.argmax(prediction)

    # Tahmin edilen sınıf etiketi
    predicted_class_label = labels[predicted_class_index]

    return predicted_class_label

# Streamlit uygulaması
st.title("Brain Tumor Classification")
uploaded_file = st.file_uploader("Choose a brain MRI image...", type=["jpg", "jpeg"])

if uploaded_file is not None:
    # Yüklenen dosyayı oku
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Tahmin yap
    predicted_class = predict_tumor(image)

    # Sonucu göster
    st.image(image, caption='Uploaded MRI Image.', use_column_width=True)
    st.write("Prediction:", predicted_class)
else:
    st.write("Please upload an image.")
