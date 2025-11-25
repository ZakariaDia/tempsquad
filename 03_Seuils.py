import streamlit as st
import pandas as pd
import yaml


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

@st.fragment(run_every="10s")
def yamlWriter(varT,thresholdT,msgT,email,varH,thresholdH,msgH):
    options = {
        "tempVar" : varT,
        "humVar" : varH,
        "thresholdTemp" : thresholdT,
        "thresholdHum" : thresholdH,
        "msgTemp" : msgT,
        "msgHum" : msgH,
        "email" : email,
        "cooldown" : 10
    }
    with open("options.yaml","w") as file:
        yaml.dump(options,file)


try:
    with open("options.yaml","r") as file:
        options = yaml.safe_load(file)
except:
    varTemp="temp1"
    thresholdTemp=25
    msgTemp=""
    email=""
    varHum="hum1"
    thresholdHum=50
    msgHum=""
    yamlWriter(varTemp,thresholdTemp,msgTemp,email,varHum,thresholdHum,msgHum)
    with open("options.yaml","r") as file:
        options = yaml.safe_load(file)


data = pd.read_csv('measurements.csv', parse_dates=['date'])
indexes = data.columns
tempIndexes = indexes[21:22].union(indexes[1:3].union(indexes[5:13]))
humIndexes = indexes[22:23].union(indexes[3:5].union(indexes[14:21]))

### notification settings
st.markdown(divColour,unsafe_allow_html=True)
st.title("Paramètres des seuils")


colT, colH = st.columns(2,border=True)

with colT:
    st.subheader("Température")
    contT = st.container(horizontal="true")
    with contT:
        varTemp = st.selectbox("Choisir un capteur :", tempIndexes,index=tempIndexes.get_loc(options["tempVar"]) , key=1)
        choiceTemp = st.selectbox("Choisir une condition :",(">", "<", "=") , key=2)
    thresholdTemp = st.slider("Température à dépasser :",0,55,options["thresholdTemp"])
    msgTemp = st.text_area(label="Message à envoyer : ", value=options["msgTemp"], key=5)
    

with colH:
    st.subheader("Humidité")
    contH = st.container(horizontal="true")
    with contH:
        varHum = st.selectbox("Choisir un capteur :", humIndexes,index=humIndexes.get_loc(options["humVar"]), key=3)
        choiceHum = st.selectbox("Choisir une condition :",(">", "<", "=", "=/="),key=4)
    thresholdHum = st.slider("Pourcentage d'humidité à dépasser :",0,100,options["thresholdHum"])
    msgHum = st.text_area("Message à envoyer : ",value=options["msgHum"],key=6)
    
contEmail = st.container(border=True,key="container-email")
with contEmail:
    email = st.text_input("Destinataire",placeholder="example@gmail.com",value=options["email"])

yamlWriter(varTemp,thresholdTemp,msgTemp,email,varHum,thresholdHum,msgHum)

st.divider()


### account settings

st.title("Paramètres de compte")

contUser = st.container(border=True,key="container-user",width=400)
with contUser:
    st.text_input(label="Nom d'utilisateur",value=f"{''.join(st.session_state['username'])}",disabled=True)
    st.text_input(label="Mot de passe",value=f"{''.join((st.session_state['password']))}",disabled=True,type="password")
    contSpace = st.container(horizontal=True)
    with contSpace:
        contSpace.space("large")
        contSpace.space("medium")
        if st.button("Déconnecter"):
            del st.session_state["username"]
            del st.session_state["password"]
            st.switch_page("login.py")
        
<<<<<<< Updated upstream
    with col2:
        col2.space(27)
        st.toggle("Afficher")
=======





>>>>>>> Stashed changes
