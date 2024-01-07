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
st.write("DisPred uygulamasına Hosgeldiniz!")