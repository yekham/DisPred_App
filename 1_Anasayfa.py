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
st.image(Image.open("dispred.jpg"),use_column_width=True)
st.write(
    "Merhaba! Yapay Zeka ile Hastalık Tahmini Uygulamamıza hoş geldiniz. Bu uygulama, belirli semptomlara dayanarak "
    "bir hastalığın olası olup olmadığını tahmin etmeye yardımcı olur. Formu doldurduktan sonra uygulamayı kullanmak için sol taraftaki "
    "paneli kullanabilirsiniz."
)

user_data = {}

# Sayfa ortalamak için CSS kullanımı
st.markdown("""
    <style>
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
    </style>
""", unsafe_allow_html=True)

# Kullanıcı Girişi Formu
with st.form("login_form"):
    st.header("Kullanıcı Girişi")
    username = st.text_input("Kullanıcı Adı")
    st.write("<style>div.Widget.row-widget.stButton {margin-top: 25px;}</style>", unsafe_allow_html=True)  # Form elemanları arasında boşluk bırakmak için
    submitted = st.form_submit_button("Giriş Yap")

    # Kullanıcı Girişi Kontrolü
    if submitted:
        # Giriş işlemleri burada yapılabilir
        user_data["username"] = username
        st.success(f"Başarıyla giriş yaptınız, {username}!")

# Diğer sayfalarda kullanıcı adını gösterme örneği
if "username" in user_data:
    st.write(f"Kullanıcı adı: {user_data['username']}")
    # Burada diğer sayfa içeriğini gösterebilirsiniz