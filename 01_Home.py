import streamlit as st
import pandas as pd
import numpy as np
import plost
import plotly.express as pl
from PIL import Image




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
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    chart = pl.line(data, x="date", y="temp1",height=350)
    chart.update_layout(paper_bgcolor="#21499f",plot_bgcolor="#21499f")
    chart.update_traces(line_color="#DF3A40")
    st.plotly_chart(chart,key="tempChart")

@st.fragment(run_every="3s")
def createHum():
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    chart = pl.line(data, x="date", y="hum1",height=350)
    chart.update_layout(paper_bgcolor="#21499f",plot_bgcolor="#21499f")
    st.plotly_chart(chart,key="humChart")


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


        
