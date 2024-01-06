import streamlit as st

st.set_page_config(
    page_title="DisPred",
    page_icon="👋",
)

st.title("DİSPRED")
st.write("DİSPRED uygulamasına hoşgeldiniz.")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)