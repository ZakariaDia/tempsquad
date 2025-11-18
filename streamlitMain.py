import streamlit as st

st.logo("david.png",icon_image="david-logo.png",size="large")

login = st.Page("login.py")
home = st.Page("01_Home.py",title="Accueil")
measurements = st.Page("02_Données brutes.py",title="Données brutes")
notifications = st.Page("03_Seuils.py",title="Seuils configurables")
account = st.Page("04_Account.py",title="Paramètres de compte")

pages = [login,
         home,
         measurements,
         notifications,
         account]

# sidebar hiding login page
st.sidebar.page_link(home,label="Accueil")
st.sidebar.page_link(measurements,label="Données brutes")
st.sidebar.page_link(notifications,label="Seuils")
st.sidebar.page_link(account,label="Gestion de compte")

pg = st.navigation(pages)
pg.run()