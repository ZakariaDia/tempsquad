import streamlit as st


st.logo("david.png",icon_image="david-logo.png",size="large")

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
st.markdown(hide_sidebar, unsafe_allow_html=True,width="content")

st.image("david-logo.png")

st.title("Connexion")

contLogin = st.container(border=True)

with contLogin:
    contLogin.text_input("Nom d'utilisateur")
    contLogin.text_input("Mot de passe")
    contLogin.page_link("01_Home.py",label="Connecter")
    