import streamlit as st
import time
from PIL import Image

st.set_page_config(layout="wide")

st.logo("david.png",icon_image="david-logo.png",size="large")


with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Page de connexion")

contAccount = st.container()
with contAccount:
    st.image(Image.open("david.png"))
    st.text("Nom d'utilisateur : zdia054")
    st.text("Mot de passe : *******")
    if st.button("Déconnecter"):
        st.balloons()
        time.sleep(0.5)
        message = st.write("bro thought it would work")

        
