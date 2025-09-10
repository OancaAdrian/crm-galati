import streamlit as st
import pandas as pd
import requests
from datetime import date

# 🔗 URL-ul public al backendului FastAPI
API_URL = "https://crm-api-galati.onrender.com"

st.set_page_config(page_title="CRM Galați", layout="wide")
st.title("CRM Galați — Motor de căutare și agendă")

# 🔍 Căutare firmă
st.subheader("Căutare firmă")
cui_or_name = st.text_input("Introduceți CUI sau fragment de denumire")

if st.button("Caută"):
    try:
        response = requests.get(f"{API_URL}/firme?q={cui_or_name}")
        if response.status_code == 200:
            results = response.json()
            if results:
                st.session_state.selected_firm = results[0]
            else:
                st.warning("⚠️ Firma nu a fost găsită în baza de date.")
        elif response.status_code == 404:
            st.warning("⚠️ Firma nu există în baza de date.")
        else:
            st.error(f"❌ Eroare API: {response.status_code}")
    except Exception as e:
        st.error(f"❌ Eroare la interogarea API: {e}")

# ✅ Afișare firmă selectată
if "selected_firm" in st.session_state:
    firm = st.session_state.selected_firm
    st.markdown(f"**Firmă selectată:** {firm['denumire']}")
    st.markdown(f"- CUI: `{firm['cui']}`")
    st.markdown(f"- Județ: `{firm['adr_judet']}`")
    st.markdown(f"- Cifra afaceri: `{firm['cifra_afaceri']}` RON")

# 📅 Agenda zilnică
st.subheader("Agenda zilnică")
selected_date = st.date_input("Selectați o dată", value=date.today())

if st.button("Încarcă agenda"):
    if "selected_firm" not in st.session_state:
        st.warning("⚠️ Selectați mai întâi o firmă.")
    else:
        cui = st.session_state.selected_firm["cui"]
        try:
            response = requests.get(f"{API_URL}/agenda?cui={cui}&data={selected_date}")
            if response.status_code == 200:
                activitati = response.json()
                if activitati:
                    st.success(f"✅ {len(activitati)} activități pentru {selected_date}")
                    for act in activitati:
                        st.markdown(f"- {act['comentariu']} (Scor: {act['scor']})")
                else:
                    st.info("ℹ️ Nicio activitate pentru data aleasă.")
            elif response.status_code == 404:
                st.info("ℹ️ Agenda nu conține activități pentru această firmă și dată.")
            else:
                st.error(f"❌ Eroare API: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Eroare la interogarea agendei: {e}")

# 📝 Formular activitate
if "selected_firm" in st.session_state and selected_date:
    st.subheader("Adaugă activitate")

    scor = st.slider("Scor activitate", 0, 10, 5)
    comentariu = st.text_area("Comentariu")
    salveaza = st.button("Salvează activitatea")

    if salveaza:
        payload = {
            "cui": st.session_state.selected_firm["cui"],
            "data": str(selected_date),
            "scor": scor,
            "comentariu": comentariu
        }
        try:
            response = requests.post(f"{API_URL}/agenda", json=payload)
            if response.status_code == 200:
                st.success("✅ Activitate salvată cu succes.")
            else:
                st.error(f"❌ Eroare la salvare: {response.status_code}")
        except Exception as e:
            st.error(f"❌ Eroare la salvarea activității: {e}")
