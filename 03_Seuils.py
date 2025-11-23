import streamlit as st

st.set_page_config(layout="wide")

divColour = """
<style>
    [data-testid="stColumn"]{
        background-color: #21499f;
        }
    .st-key-container-email{
        background-color: #21499f;
        }
    .st-key-container-user{
        background-color: #21499f;
        }
<style>
"""

st.markdown(divColour,unsafe_allow_html=True)
st.title("Paramètres des seuils")

colT, colH = st.columns(2,border=True)

with colT:
    st.subheader("Température")
    contT = st.container(horizontal="true")
    with contT:
        varTemp = st.selectbox("Choisir une donnée :", ("T1", "T2", "T3", "T4"), key=1)
        choiceTemp = st.selectbox("Choisir une condition :",(">", "<", "=", "=/="),key=2)
    st.text_area("Message à envoyer : ",key=5)

with colH:
    st.subheader("Humidité")
    contH = st.container(horizontal="true")
    with contH:
        varTemp = st.selectbox("Choisir une donnée :", ("H1", "H2", "H3", "H4"), key=3)
        choiceTemp = st.selectbox("Choisir une condition :",(">", "<", "=", "=/="),key=4)
    st.text_area("Message à envoyer : ",key=6)
    
contEmail = st.container(border=True,key="container-email")
with contEmail:
    st.text_input("Destinataire",placeholder="example@gmail.com")
    
st.divider()

st.title("Paramètres de compte")

contUser = st.container(border=True,key="container-user",width=400)
with contUser:
    col1,col2= st.columns([5,2])
    with col1:
        st.write("Nom d'utilisateur : zdia054")
        st.write("Mot de passe : censored ")
        contSpace = st.container(horizontal=True)
        with contSpace:
            contSpace.space()
            st.button("Déconnecter")
        
    with col2:
        col2.space(27)
        st.toggle("Afficher")

