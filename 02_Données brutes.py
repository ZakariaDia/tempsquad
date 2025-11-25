import streamlit as st
import plotly_express as pl
import pandas as pd

# Data

@st.fragment(run_every="10s")
def createTemp():
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    chart = pl.line(data, x="date", y="temp1",height=350)
    chart.update_layout(paper_bgcolor="#21499f",plot_bgcolor="#21499f")
    chart.update_traces(line_color="#DF3A40")
    st.plotly_chart(chart,key="tempChart")

@st.fragment(run_every="10s")
def createHum():
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    chart = pl.line(data, x="date", y="hum1",height=350)
    chart.update_layout(paper_bgcolor="#21499f",plot_bgcolor="#21499f")
    st.plotly_chart(chart,key="humChart")

@st.fragment(run_every="10s")
def createMetric(num,type,index):
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    if type == "temp":
        var = data.iloc[-1,index]
        varDelta = round((float(var) - float(data.iloc[-2,index])),2)
        st.metric(f"Température {num}", f"{var} °C", varDelta)
    else:
        var = data.iloc[-1,index]
        varDelta = round((float(var) - float(data.iloc[-2,index])),2)
        st.metric(f"Humidité {num}", f"{var} %", varDelta)




st.set_page_config(layout="wide")

with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("Données brutes")

col1,col2,col3 = st.columns([3,3,5],border=True,gap="small")

with col1:
    st.header("Température",anchor=False)
    st.subheader("Capteurs réels", anchor=False)
    colTempR1, colTempR2 = st.columns(2)
    with colTempR1:
        createMetric(1,"temp",1)
    with colTempR2:
        createMetric(2,"temp",2)
    col1.space("small")
    st.subheader("Capteurs simulés", anchor=False)
    colT1, colT2 = st.columns(2)
    with colT1:
        createMetric(1,"temp",5)
        createMetric(3,"temp",7)
        createMetric(5,"temp",9)
        createMetric(7,"temp",11)
    with colT2:
        createMetric(2,"temp",6)
        createMetric(4,"temp",8)
        createMetric(6,"temp",10)
        createMetric(8,"temp",12)

with col2:
    st.header("Humidité",anchor=False)
    st.subheader("Capteurs réels", anchor=False)
    colHumR1, colHumR2 = st.columns(2)
    with colHumR1:
        createMetric(1,"hum",3)
    with colHumR2:
        createMetric(2,"hum",4)
    col2.space("small")
    st.subheader("Capteurs simulés", anchor=False)
    colH1, colH2 = st.columns(2)
    with colH1:
        createMetric(1,"hum",13)
        createMetric(3,"hum",15)
        createMetric(5,"hum",17)
        createMetric(7,"hum",19)
    with colH2:
        createMetric(2,"hum",14)
        createMetric(4,"hum",16)
        createMetric(6,"hum",18)
        createMetric(8,"hum",20)

with col3:
    st.markdown("### Histogramme de température")
    createTemp()
    st.markdown("### Histogramme d'humidité")
    createHum()
    






    




