import streamlit as st
import time

st.title("_Der Redekreirer_ :blue[von Knobi]")
st.subheader("Lalalalaalalala", divider="gray")
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

    with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button("Rerun")