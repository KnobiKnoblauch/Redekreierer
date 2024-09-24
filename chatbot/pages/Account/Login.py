import sqlite3
import streamlit as st

# Set up the Streamlit page
st.set_page_config(page_title="Login", layout="centered")
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
        .login-container {
            background-color: #f0f2f6;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
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
            margin-top: 30px;
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
    else:
        print("Incorrect Username or Password")
        st.session_state.c.markdown('<div class="message">Incorrect username or password</div>', unsafe_allow_html=True)
        st.session_state.c.markdown('<div class="message">Please try again</div>', unsafe_allow_html=True)
        connection.close()

def setup():
    st.session_state.username = st.text_input("Username", placeholder="Enter your username")
    st.session_state.password = st.text_input("Password", type="password", placeholder="Enter your password")
    st.button("Continue", on_click=clicked)
    st.session_state.c = st.container(height=100, border=False)

def get_login_data():
    rows = cursor.execute("SELECT username, password FROM Users").fetchall()
    return rows

setup()
st.markdown('<div class="footer">Lasse dir mit einfachen Schritten deine eigene, personalisierte und qualitativ hochwertige Rede kreieren!</div>', unsafe_allow_html=True)

