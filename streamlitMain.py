import streamlit as st
import subprocess
import sys
import psutil

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

