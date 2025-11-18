import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image


st.logo("david.png",icon_image="david-logo.png",size="large")

seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])

# Page setting

st.set_page_config(layout="wide")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



st.title("Bienvenue, <nom> !")
# Row A

st.subheader("Mesures principales")

col1,col2,col3 = st.columns(3,border=True)


with col1:
    st.metric("Risque d'incendie","XX%","-X %")
    st.metric("Température X", "22.0 °C", "1.2 °C")
    st.metric("Humidité 1", "54%", "1.2 %")

with col2:
    graphs = st.container
    st.markdown('### Histogramme de température')
    plost.line_chart(
    data=seattle_weather,
    color = "#f73939",
    x='date',
    y='temp_max')
with col3:
    st.markdown('### Histogramme humidité')
    plost.line_chart(
    data=seattle_weather,
    x='date',
    y='temp_max',
    color = "#1088e9",)



#pg = st.navigation([Accueil,"Données brutes.py","page3.py","page4.py"],expanded=False)
#pg.run()


        
