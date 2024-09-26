import sqlite3
import streamlit as st

# Set up the Streamlit page
st.set_page_config(page_title="Sign Up", layout="centered", initial_sidebar_state="collapsed")
st.markdown('<h1 class="title">Sign Up</h1>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Create an Account to continue.</div>', unsafe_allow_html=True)
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
    username = st.session_state.username
    password = st.session_state.password
    password_confirmed = st.session_state.password_confirmed
    cursor.execute("SELECT COUNT(*) FROM Users WHERE username = ?", (username,))
    count = cursor.fetchone()[0]
    if count > 0:
        print("Username is already taken")
        st.session_state.c.markdown('<div class="message">Username is already taken</div>', unsafe_allow_html=True)
        connection.close()
    elif username == "" or password == "" or password_confirmed == "":
        print("It looks like some fields are empty")
        st.session_state.c.markdown('<div class="message">It looks like some fields are empty</div>', unsafe_allow_html=True)
        connection.close()
    elif len(password) < 5:
        print("Password must have at least 5 tokens")
        st.session_state.c.markdown('<div class="message">Password must have at least 5 tokens</div>', unsafe_allow_html=True)
        connection.close()
    elif password == password_confirmed:
        CreateAccount(username, password)
        print("Account created")
        st.session_state.c.markdown('<div class="message">Account created</div>', unsafe_allow_html=True)
        connection.close()
        switch_page()
    elif password != password_confirmed:
        print("Passwords doesnt match")
        st.session_state.c.markdown('<div class="message">Passwords doesnt match</div>', unsafe_allow_html=True)
        connection.close()

    

def setup():
    st.session_state.c = st.container(height=20, border=False)
    st.session_state.username = st.text_input("Username", placeholder="Enter your username")
    st.session_state.password = st.text_input("Password", type="password", placeholder="Enter your password")
    st.session_state.password_confirmed = st.text_input("Confirm password", type="password", placeholder="Confirm your password")
    col1, col2, col3 = st.columns([1, 1, 1])
    col2.html("<div style='text-align:center'><a href=/Login style='color:blue'>Already have an Account?</a></div>")
    st.button("Continue", on_click=clicked, use_container_width=True)    

def CreateAccount(username, password):
    cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
    connection.commit()

def switch_page():
    st.components.v1.html(f"""
        <script>
            window.open("{"Login"}");
        </script>
    """)


setup()
st.markdown('<div class="footer">Lasse dir mit einfachen Schritten deine eigene, personalisierte und qualitativ hochwertige Rede kreieren!</div>', unsafe_allow_html=True)


