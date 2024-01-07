import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="DisPred",
    page_icon="🩺",
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: red;'>DisPred</h1>", unsafe_allow_html=True)
st.image(Image.open("dispred.jpg"))
st.write(
    "Merhaba! Yapay Zeka ile Hastalık Tahmini Uygulamamıza hoş geldiniz. Bu uygulama, belirli semptomlara dayanarak "
    "bir hastalığın olası olup olmadığını tahmin etmeye yardımcı olur. Hemen başlamak için sol taraftaki "
    "paneli kullanabilirsiniz."
)