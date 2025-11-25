import streamlit as st
import plotly_express as pl
import pandas as pd

# Data

def plotly_preserve_zoom(fig, key):
    """
    Preserve zoom/pan for a Plotly chart rendered with st.plotly_chart().
    """

    # Restore zoom if saved earlier
    if key in st.session_state:
        zoom = st.session_state[key]
        fig.update_xaxes(range=zoom.get("x"))
        fig.update_yaxes(range=zoom.get("y"))

    # Display chart with event capture
    event = st.plotly_chart(
        fig,
        key=key,
        on_event="relayout",
        use_container_width=True
    )

    # The event is a dict of axis ranges if the user zoomed
    if isinstance(event, dict):
        x0 = event.get("xaxis.range[0]")
        x1 = event.get("xaxis.range[1]")
        y0 = event.get("yaxis.range[0]")
        y1 = event.get("yaxis.range[1]")

        # update session storage only if zoom is valid
        if x0 is not None and x1 is not None:
            st.session_state.setdefault(key, {})["x"] = [x0, x1]
        if y0 is not None and y1 is not None:
            st.session_state.setdefault(key, {})["y"] = [y0, y1]

@st.fragment(run_every="10s")
def createTemp():
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    chart = pl.line(data, x="date", y="temp1",height=350)
    chart.update_layout(paper_bgcolor="#21499f",plot_bgcolor="#21499f")
    chart.update_traces(line_color="#DF3A40")
    plotly_preserve_zoom(chart, "tempChart")

@st.fragment(run_every="10s")
def createHum():
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    chart = pl.line(data, x="date", y="hum1",height=350)
    chart.update_layout(paper_bgcolor="#21499f",plot_bgcolor="#21499f")
    plotly_preserve_zoom(chart, "humChart")

@st.fragment(run_every="10s")
def createMetric(num,type,index):
    data = pd.read_csv('measurements.csv', parse_dates=['date'])
    lastRow = data.tail(1)
    if type == "temp":
        var = lastRow.iloc[0,index]
        st.metric(f"Température {num}", f"{var} °C", "1.2 °C")
    else:
        var = lastRow.iloc[0,index]
        st.metric(f"Humidité {num}", f"{var} %", "1.2 °C")


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
    






    




