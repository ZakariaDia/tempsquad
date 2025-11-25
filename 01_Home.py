import streamlit as st
import pandas as pd
import plotly.express as pl

# Page setting

st.set_page_config(layout="wide")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if "username" not in st.session_state or "password" not in st.session_state:
    st.switch_page("login.py")

st.title(f"Bienvenue, {''.join(st.session_state['username'])}!")

st.subheader("Données principales")

col1,col2,col3 = st.columns(3,border=True)

@st.fragment(run_every="3s")
def createTemp():
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    chart = pl.line(data, x="date", y="tempMoy",height=350, labels={
                     "date": "Temps (En HH:MM)",
                     "tempMoy": "Température (°C)",
                 })
    chart.update_layout(paper_bgcolor="#21499f",plot_bgcolor="#21499f")
    chart.update_traces(line_color="#DF3A40")
    st.plotly_chart(chart,width="stretch",key="tempChart")

@st.fragment(run_every="3s")
def createHum():
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    chart = pl.line(data, x="date", y="humMoy",height=350, labels={
                     "date": "Temps (En HH:MM)",
                     "humMoy": "Humidité (%)",
                 })
    chart.update_layout(paper_bgcolor="#21499f",plot_bgcolor="#21499f")
    st.plotly_chart(chart,key="humChart")

@st.fragment(run_every="3s")
def createMetric():
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    temp = float(data.iloc[-1,21])
    hum = float(data.iloc[-1,22])
    tempDelta = round((temp - float(data.iloc[-2,21])),2)
    humDelta = round((hum - float(data.iloc[-2,22])),2)

    #Calcul du risque d'incendie
    InfTemp = 0.7 #influence de la température sur le % de risque d'incendie
    InfHum = 0.3 #influence d'humidité sur le % de risque d'incendie

    RiskIncendie = round((InfTemp*temp + InfHum*hum),2)
    if "riskLast" not in st.session_state:
        st.session_state["riskLast"] = 0

    st.session_state["riskNow"] = RiskIncendie

    deltaIncendie = round((st.session_state["riskNow"] - st.session_state["riskLast"]),2)

    st.session_state["riskLast"] = RiskIncendie

    st.metric("Risque d'incendie",f"{RiskIncendie} %",f"{deltaIncendie} %")
    st.metric("Température moyenne",f"{temp} °C", f"{tempDelta} °C")
    st.metric("Pourcentage d'humidité moyenne",f"{hum} %", f"{humDelta} %")

with col1:
    createMetric()
    
with col2:
    st.markdown("### Diagramme de température")
    createTemp()
    
with col3:
    st.markdown("### Diagramme  d'humidité")
    createHum()



#pg = st.navigation([Accueil,"Données brutes.py","page3.py","page4.py"],expanded=False)
#pg.run()


        
