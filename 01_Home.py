import streamlit as st
import pandas as pd
import plotly.express as pl

# Page setting

st.set_page_config(layout="wide")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Bienvenue, <nom> !")

st.subheader("Mesures principales")

col1,col2,col3 = st.columns(3,border=True)

@st.fragment(run_every="3s")
def createTemp():
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    chart = pl.line(data, x="date", y="temp1",height=350)
    chart.update_layout(paper_bgcolor="#21499f",plot_bgcolor="#21499f")
    chart.update_traces(line_color="#DF3A40")
    st.plotly_chart(chart,width="stretch",key="tempChart")

@st.fragment(run_every="3s")
def createHum():
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    chart = pl.line(data, x="date", y="hum1",height=350)
    chart.update_layout(paper_bgcolor="#21499f",plot_bgcolor="#21499f")
    st.plotly_chart(chart,key="humChart")

@st.fragment(run_every="3s")
def createMetric():
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    temp = data.iloc[-1,21]
    hum = data.iloc[-1,22]
    tempDelta = round((float(temp) - float(data.iloc[-2,21])),2)
    humDelta = round((float(hum) - float(data.iloc[-2,22])),2)
    st.metric("Risque d'incendie","XX%","-X %")
    st.metric("Température", temp, tempDelta)
    st.metric("Humidité", hum, humDelta)

with col1:
    createMetric()
    
with col2:
    st.markdown('### Histogramme de température')
    createTemp()
    
with col3:
    st.markdown('### Histogramme humidité')
    createHum()



#pg = st.navigation([Accueil,"Données brutes.py","page3.py","page4.py"],expanded=False)
#pg.run()


        
