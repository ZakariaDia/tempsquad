import streamlit as st
import pandas as pd
import numpy as np
import plost
from PIL import Image


st.logo("david.png",icon_image="david-logo.png",size="large")


# Page setting

st.set_page_config(layout="wide")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



st.title("Bienvenue, <nom> !")
# Row A

st.subheader("Mesures principales")

col1,col2,col3 = st.columns(3,border=True)

@st.fragment(run_every="3s")
def createTemp():
    plost.line_chart(
    data = pd.read_csv('measurements.csv', parse_dates=['date']),
    color = "#f73939",
    x='date',
    y='temp1')

@st.fragment(run_every="3s")
def createHum():
    plost.line_chart(
    data = pd.read_csv('measurements.csv', parse_dates=['date']),
    x='date',
    y='hum1',
    color = "#1088e9",)


with col1:
    st.metric("Risque d'incendie","XX%","-X %")
    st.metric("Température X", "22.0 °C", "1.2 °C")
    st.metric("Humidité 1", "54%", "1.2 %")
    
with col2:
    st.markdown('### Histogramme de température')
    createTemp()
    
with col3:
    st.markdown('### Histogramme humidité')
    createHum()



#pg = st.navigation([Accueil,"Données brutes.py","page3.py","page4.py"],expanded=False)
#pg.run()


        
