import streamlit as st
import sqlite3



st.title("Login")
st.session_state.c = st.empty()

connection = sqlite3.connect("LoginData1.sqlite", check_same_thread=False)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Users (username TEXT UNIQUE, password TEXT)")
cursor.execute("INSERT OR IGNORE INTO Users VALUES ('Knobi', '1234')")
cursor.execute("INSERT OR IGNORE INTO Users VALUES ('Theo', '1234')")
connection.commit()


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
        print("Login succesfull")
        st.session_state.c.container(height=50, border=True)
        st.session_state.c.text("Login succesfull")
        connection.close()
    else:
        print("Incorrect Username or Password")
        st.session_state.c.container(height=50, border=True)
        st.session_state.c.text("Incorrect Username or Password")
        connection.close()

def setup():
    st.session_state.username = st.text_input("Username")
    st.session_state.password = st.text_input("Password", type = "password")
    st.button("continue", type="secondary", on_click = clicked)

def get_login_data():
    rows = cursor.execute("SELECT username, password FROM Users").fetchall()
    return rows


setup()
