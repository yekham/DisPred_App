import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="DisPred",
    page_icon="👋",
)

st.title("DİSPRED")
st.write("DİSPRED uygulamasına hoşgeldiniz.")
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

intro_markdown = read_markdown_file("about.md")
st.markdown(intro_markdown, unsafe_allow_html=True)