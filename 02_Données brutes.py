import streamlit as st
import plost
import pandas as pd

# Data
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

st.set_page_config(layout="wide")

with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Données brutes")

st.header("Capteurs réels")

contTemp = st.container(horizontal=True)

with contTemp:  
    st.metric("Température 1", "22.0 °C", "1.2 °C")
    st.metric("Température 2", "22.0 °C", "1.2 °C")

contHum = st.container(horizontal=True)

with contHum:
    st.metric("Humidité 1", "54%", "1.2 %")
    st.metric("Humidité 2", "54%", "1.2 %")

st.divider()

st.header("Capteurs simulés")

contSimTemp = st.container(horizontal=True)

with contSimTemp:
    st.metric("Température 1", "22.0 °C", "1.2 °C")
    st.metric("Température 2", "22.0 °C", "1.2 °C")
    st.metric("Température 3", "22.0 °C", "1.2 °C")
    st.metric("Température 4", "22.0 °C", "1.2 °C")
    st.metric("Température 5", "22.0 °C", "1.2 °C")
    st.metric("Température 6", "22.0 °C", "1.2 °C")
    st.metric("Température 7", "22.0 °C", "1.2 °C")
    st.metric("Température 8", "22.0 °C", "1.2 °C")

contSimHum = st.container(horizontal=True)

with contSimHum:
    st.metric("Humidité 1", "22.0 °C", "1.2 °C")
    st.metric("Humidité 2", "22.0 °C", "1.2 °C")
    st.metric("Humidité 3", "22.0 °C", "1.2 °C")
    st.metric("Humidité 4", "22.0 °C", "1.2 °C")
    st.metric("Humidité 5", "22.0 °C", "1.2 °C")
    st.metric("Humidité 6", "22.0 °C", "1.2 °C")
    st.metric("Humidité 7", "22.0 °C", "1.2 °C")
    st.metric("Humidité 8", "22.0 °C", "1.2 °C")

st.divider()

st.header("Graphiques")

a1, a2 = st.columns(2)
with a1:
    st.markdown('### Histogramme de température')
    plost.line_chart(
    data=seattle_weather,
    color = "#f73939",
    x='date',
    y='temp_max')
with a2:
    st.markdown('### Histogramme humidité')
    plost.line_chart(
    data=seattle_weather,
    x='date',
    y='temp_max',
    color = "#1088e9",)