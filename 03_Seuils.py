import streamlit as st

st.set_page_config(layout="wide")


st.title("Seuils programmables")

st.subheader("Température")

tempContainer = st.container(horizontal="true", horizontal_alignment="right")

with tempContainer:
    tempContainer.selectbox("Choisir une donnée :", ("T1", "T2", "T3", "T4"), key=1)
    tempContainer.selectbox("Choisir une condition :",(">", "<", "=", "=/="),key=2)
    tempContainer.number_input("Entrez un nombre :",key=5)

tempContainer.text_area("Message à envoyer : ", width=425)

st.subheader("Humidité")

humContainer = st.container(horizontal="true", horizontal_alignment="right")

with humContainer:
    humContainer.selectbox("Choisir une donnée :", ("H1", "H2", "H3", "H4"),key=3)
    humContainer.selectbox("Choisir une condition :",(">", "<", "=", "=/="),key=4)
    humContainer.number_input("Entrez un nombre :",key=6)
humContainer.text_area("Message à envoyer : ", width=425,key=8)
    
