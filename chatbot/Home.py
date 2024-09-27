import streamlit as st
import importlib
from streamlit_extras.switch_page_button import switch_page



st.set_page_config(page_title="Get Started", layout="centered", initial_sidebar_state="collapsed")



    

st.markdown("""
    <style>
        .super-title {
            font-size: 93px;
            color: #4F8BF9;
            font-weight: bold;
            text-align: center;
        }
        .title {
            font-size: 36px;
            color: #4F8BF9;
            font-weight: bold;
            text-align: center;
        }
        .subtitle {
            font-size: 18px;
            color: #555;
            text-align: center;
            margin-bottom: 20px;
        }
        .super-subtitle {
            font-size: 30px;
            color: #555;
            text-align: center;
            margin-bottom: 20px;
        }
        .message {
            font-size: 15px;
            color: #555;
            text-align: center;
            margin-bottom: 0px;    
        }
        .footer {
            text-align: center;
            font-size: 15px;
            color: #555;
            margin-top: 50px;
        }
        .stButton > button {
            background-color: #4F8BF9; 
            color: white; 
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            #margin-top: 50px;
        }
        .stButton > button:hover {
            background-color: #3a7cd3;
            color: white; 
            outline: none; 
        }
        .stButton > button:focus {
            outline: none !important; 
            box-shadow: none !important; 
            color: white !important; 
            border: none !important;
        }
        .stButton > button:active {
            background-color: #4F8BF9 !important;
            color: white !important;
            outline: none !important; 
            box-shadow: none !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">Der Redekreierer</h1>', unsafe_allow_html=True)
st.container(height=50, border=False)
st.write("---")
st.markdown('<div class="super-subtitle">Lasse dir mit einfachen Schritten deine eigene, personalisierte und qualitativ hochwertige Rede kreieren!</div>', unsafe_allow_html=True)
st.write("---")
st.container(height=50, border=False)
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col3:
    login_button = st.button("Login", use_container_width=True)
    if login_button:
        switch_page("login")

with col4:
    sign_up_button = st.button("Sign Up", use_container_width=True)
    if sign_up_button:
        switch_page("sign up")

st.container(height=10, border=False)

col1, col2, col3 = st.columns(3)

with col2:
    continue_button = st.button("Skip", use_container_width=True)
    if continue_button:
        switch_page("bot")

st.markdown('<div class="footer">Erstellt von Knobi und TayoZz 😎</div>', unsafe_allow_html=True)
