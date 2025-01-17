import streamlit as st

st.title("OKX Streamlit Demo")

api_key = st.secrets["OKX"]["API684TL"]
secret_key = st.secrets["OKX"]["SECRET684TL"]
passphrase = st.secrets["OKX"]["PASSPHRASE684TL"]

st.write("API Key:", api_key)
st.write("Secret Key:", secret_key)
st.write("Passphrase:", passphrase)
