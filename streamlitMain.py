import streamlit as st
import subprocess
import psutil
import os

st.logo("david.png",icon_image="david.png",size="large")

hideLogo = """
<style>
[data-testid="stSidebarLogo"]{
        height: 5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
[data-testid="stSidebarHeader"]{
    height: 6.5rem;
}
[data-testid="stHeaderLogo"]{
    height: 5rem;
    margin-top: 3rem;
}
    
</style>
"""
st.markdown(hideLogo,unsafe_allow_html=True)

login = st.Page("login.py")
signup = st.Page("signup.py")
home = st.Page("01_Home.py",title="Tableau de bord")
measurements = st.Page("02_Données brutes.py",title="Données complètes")
notifications = st.Page("03_Seuils.py",title="Paramètres")
david = st.Page("david.py",title="")

pages = [login,
         home,
         measurements,
         notifications,
         david,
         signup]

# sidebar hiding login page
st.sidebar.page_link(home,label="Tableau de bord")
st.sidebar.page_link(measurements,label="Données complètes")
st.sidebar.page_link(notifications,label="Paramètres")
st.sidebar.page_link(david,label="⠀")

pg = st.navigation(pages)
pg.run()


