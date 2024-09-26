import sqlite3
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_keyup import st_keyup

# Set up the Streamlit page
st.session_state.logged_in = False
st.set_page_config(page_title="Login", layout="centered", initial_sidebar_state="collapsed")
st.markdown('<h1 class="title">Login</h1>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Please enter your credentials to continue.</div>', unsafe_allow_html=True)
st.write("---")
st.session_state.c = st.empty()

# Set up SQLite connection and user table
connection = sqlite3.connect("LoginData.sqlite", check_same_thread=False)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Users (username TEXT UNIQUE, password TEXT)")
connection.commit()

# CSS styling for the app
st.markdown("""
    <style>
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

def clicked():
    correct = False
    username = st.session_state.username
    password = st.session_state.password
    login_data = get_login_data()
    user_inputs = "('" + username + "', '" + password + "')"
    i = 0
    while i < len(login_data):
        if user_inputs == str(login_data[i]):
            correct = True
            break
        i += 1
    if correct:
        print("Login successful")
        st.session_state.c.markdown('<div class="message">Login successful.</div>', unsafe_allow_html=True)
        connection.close()
        st.session_state.logged_in = True
        return st.session_state.logged_in
    elif username == "" or password == "":
        st.session_state.c.markdown('<div class="message">It looks like some fields are empty</div>', unsafe_allow_html=True)
    else:
        print("Incorrect Username or Password")
        st.session_state.c.markdown('<div class="message">Incorrect username or password</div>', unsafe_allow_html=True)
        st.session_state.c.markdown('<div class="message">Please try again</div>', unsafe_allow_html=True)
        connection.close()
    return False

def setup():
    st.session_state.c = st.container(height=20, border=False)
    st.session_state.username = st.text_input("Username", placeholder="Enter your username")
    st.session_state.password = st.text_input("Password", type="password", placeholder="Enter your password")
    col1, col2, col3 = st.columns([1, 1, 1])
    col2.html("<div style='text-align:center'><a href=/Sign_Up style='color:blue'>Don't have an Account?</a></div>")
    continue_button = st.button("Continue", use_container_width=True)    
    if continue_button:
        login_success = clicked()
        if login_success:
            switch_page("bot")


def get_login_data():
    rows = cursor.execute("SELECT username, password FROM Users").fetchall()
    return rows


def GoToSignUp():
    st.session_state.page == "SignUp"


setup()
st.markdown('<div class="footer">Lasse dir mit einfachen Schritten deine eigene, personalisierte und qualitativ hochwertige Rede kreieren!</div>', unsafe_allow_html=True)