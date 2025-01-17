import streamlit as st

st.title("OKX Streamlit Demo")

api_key = st.secrets["OKX"]["API_KEY"]
secret_key = st.secrets["OKX"]["SECRET_KEY"]
passphrase = st.secrets["OKX"]["PASSPHRASE"]

st.write("API Key:", api_key)
st.write("Secret Key:", secret_key)
st.write("Passphrase:", passphrase)
