import streamlit as st

st.set_page_config(
    page_title="DisPred",
    page_icon="👋",
)

st.title("DİSPRED")
st.write("DİSPRED uygulamasına hoşgeldiniz.")

intro_markdown = read_markdown_file("about.md")
st.markdown(intro_markdown, unsafe_allow_html=True)