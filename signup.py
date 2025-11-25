import streamlit as st

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

st.image("david-logo.png")

st.title("Création d'un compte")

contLogin = st.container(border=True,key="container=login")

with contLogin:
    contLogin.text_input("Nom d'utilisateur")
    contLogin.text_input("Mot de passe")
    if contLogin.button(label="Créer un compte"):
        st.switch_page("login.py")
