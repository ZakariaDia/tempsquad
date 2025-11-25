import streamlit as st
import pandas as pd
import csv
import time

hide_sidebar = """
<style>
/* Hide sidebar container entirely */
[data-testid="stSidebar"] {
    display: none !important;
}
[data-testid="stExpandSidebarButton"]{
    display: none;
}
</style>
"""
divColour = """
<style>
    .st-key-container-login{
        background-color: #21499f;
        }
<style>
"""


st.markdown(divColour,unsafe_allow_html=True)
st.markdown(hide_sidebar, unsafe_allow_html=True,width="content")

col1, col2, col3 = st.columns([11,20,10])
with col1:
    pass
with col2:
    st.image("david.png")
with col3:
    pass


st.title("Création d'un compte")

contLogin = st.container(border=True,key="container=login")

with contLogin:
    username = contLogin.text_input("Nom d'utilisateur")
    passw = contLogin.text_input("Mot de passe",type="password")
    if contLogin.button(label="Créer un compte"):
        exists = False
        with open("users.csv","r") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row or len(row) < 2:
                    continue

                if row[0] == username:
                    st.error("Cette compte existe déjà!")
                    st.info("Redirection vers la page de connexion...")
                    exists = True
                    time.sleep(1)
                    break
                    
        if exists == False:
            with open("users.csv","a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow([username,passw])
        
        st.switch_page("login.py")
    if contLogin.button(label="Connecter à nouveau"):
        st.switch_page("login.py")
        
