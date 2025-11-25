import streamlit as st
import pandas as pd
import csv

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
try:
    with open("users.csv","a+") as file:
        pd.read_csv("users.csv")
except:
    st.error("Aucun compte dans le système. Veuillez créer un compte.")



st.markdown(divColour,unsafe_allow_html=True)
st.markdown(hide_sidebar, unsafe_allow_html=True,width="content")
st.set_page_config(layout="centered")


col1, col2, col3 = st.columns([11,20,10])
with col1:
    pass
with col2:
    st.image("david.png")
with col3:
    pass


st.title("Connexion")

contLogin = st.container(border=True,key="container=login")

incorrect = False

with contLogin:
    username = [contLogin.text_input("Nom d'utilisateur")]
    passw = [contLogin.text_input("Mot de passe",type="password")]
    if contLogin.button(label="Connecter"):
        with open("users.csv","r") as file:
            reader = csv.reader(file)
            for row in reader:
                if tuple(row) == tuple(username+passw):
                    if "username" not in st.session_state:
                        st.session_state["username"] = username
                    if "password" not in st.session_state:
                        st.session_state["password"] = passw
                    st.switch_page("01_Home.py")
                else:
                    incorrect = True 
            if incorrect == True:
                st.error("Nom d'utilisateur ou mot de passe invalide. Vérifier vos entrées.")
    if contLogin.button(label="Créer un compte"):
        st.switch_page("signup.py")
    