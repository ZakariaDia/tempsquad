import streamlit as st
import subprocess
import sys
import psutil

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

def script_is_running(scriptName):
    for p in psutil.process_iter(["cmdline"]):
        try:
            if p.info["cmdline"] and scriptName in p.info["cmdline"]:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False


if "sender_started" not in st.session_state:
    if not script_is_running("sender.py"):
        DETACHED_PROCESS = 0x00000008
        subprocess.Popen(
            [sys.executable, "sender.py"],
            creationflags=DETACHED_PROCESS
        )
        st.session_state["sender_started"] = True

if "connector_started" not in st.session_state:
    if not script_is_running("connector.py"):
        DETACHED_PROCESS = 0x00000008  # Windows
        subprocess.Popen(
            [sys.executable, "connector.py"],
            creationflags=DETACHED_PROCESS
        )
        st.session_state["connector_started"] = True

