import streamlit as st
import importlib

st.set_page_config(page_title="Get Started", layout="centered", initial_sidebar_state="collapsed")

if "page" not in st.session_state:
    st.session_state.page = "Home"

def GoLogin():
    st.session_state.page = "Login"

def GoSignUp():
    st.session_state.page = "SignUp"

def newPage():
    if st.session_state.page == "Bot":
        st.switch_page("pages/Bot.py")
    if st.session_state.page == "SignUp":
        st.switch_page("pages/Sign_Up.py")
    if st.session_state.page == "Login":
        st.switch_page("pages/Login.py")
    

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
st.markdown('<div class="super-subtitle">Lasse dir mit einfachen Schritten deine eigene, personalisierte und qualitativ hochwertige Rede kreieren!</div>', unsafe_allow_html=True)
st.container(height=50, border=False)
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col3:
    st.button("Login", on_click=GoLogin)
    newPage()
with col4:
    st.button("Sign Up", on_click=GoSignUp)
    newPage()
#st.switch_page("pages/Login.py")

