import streamlit as st
import time

from DatabaseConnector import DatabaseConnector
from DatabaseService import DatabaseService

db = DatabaseConnector()
database_service = DatabaseService(db)


def setup_show_speech(id):

    speech = database_service.select_table_name("saved_speeches", "name", id)

    st.title("Der Redekreierer")
    st.subheader(speech)

    show_speech(id)

    st.button("Return back to Home", on_click=return_home)


def return_home():
    st.session_state.show_speech = False


def show_speech(id):
    speech = database_service.select_table_spalte("saved_speeches", "speech", id)

    with st.spinner("loading Speech"):
        time.sleep(2)

    st.markdown('<div class="stSuccess">Speech loaded</div>', unsafe_allow_html=True)

    st.write(speech)