import streamlit as st
import pandas as pd
import numpy as np
import plost
import time
from PIL import Image


st.logo("david.png",icon_image="david-logo.png",size="large")


# Page setting

st.set_page_config(layout="wide")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



st.title("Bienvenue, <nom> !")
# Row A

st.subheader("Mesures principales")

contMain = st.container(border=True)

with contMain:
    st.metric("Risque d'incendie","XX%","-X %")
    st.metric("Température X", "22.0 °C", "1.2 °C")
    st.metric("Humidité 1", "54%", "1.2 %")






#pg = st.navigation([Accueil,"Données brutes.py","page3.py","page4.py"],expanded=False)
#pg.run()


        