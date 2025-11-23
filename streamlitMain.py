import streamlit as st

st.logo("david.png",icon_image="david.png",size="large")

login = st.Page("login.py")
home = st.Page("01_Home.py",title="Accueil")
measurements = st.Page("02_Données brutes.py",title="Données brutes")
notifications = st.Page("03_Seuils.py",title="Paramètres")

pages = [login,
         home,
         measurements,
         notifications,]

# sidebar hiding login page
st.sidebar.page_link(home,label="Accueil")
st.sidebar.page_link(measurements,label="Données brutes")
st.sidebar.page_link(notifications,label="Paramètres")


pg = st.navigation(pages)
pg.run()