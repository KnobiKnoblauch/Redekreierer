import streamlit as st
import chatgpt_benutzen
import time

from DatabaseConnector import DatabaseConnector
from DatabaseService import DatabaseService

db = DatabaseConnector()
database_service = DatabaseService(db)

def inputSpeakType(database_service):
    """
    Lässt den Nutzer seinen gewünschten Redentyp (speak_type) angeben

    :param db: Database to save data to
    :return: speak_type
    """

    speak_type = {
        "topic": st.session_state.speak_type['topic'],
        "goal": st.session_state.speak_type['goal'],
        "address": st.session_state.speak_type['addresant'],
        "speaker": st.session_state.speak_type['speaker'],
        "points": st.session_state.speak_type['points']
    }

    database_service.create_table("prompt","(id INTEGER PRIMARY KEY AUTOINCREMENT, topics TEXT, addresses TEXT, goals TEXT, speakers TEXT)")
    database_service.insert_prompt(speak_type)

    print("Save speech_type in database")

    return speak_type


if 'speak_type' not in st.session_state:
    st.session_state.speak_type = {
        "topic": "",
        "goal": "",
        "addresant": "",
        "speaker": "",
        "points": ""
    }


def setup():
    st.title("*Der Redekreierer* **von** :blue[Knobi] **und** :blue[TayozZ]")
    st.subheader("Lasse dir mit einfachen Schritten deine _eigene_, _personalisierte_ und _qualitativ hochwertige_ :blue[Rede] kreieren!", divider="blue")

    with st.form("speech_form"):
        st.session_state.speak_type["topic"] = st.text_input("What is your speech about?")
        st.session_state.speak_type["goal"] = st.text_input("What are you trying to achieve with your speech?")
        st.session_state.speak_type["addresant"] = st.text_input("Who listens to your speech?")
        st.session_state.speak_type["speaker"] = st.text_input("Who is performing your speech?")
        st.session_state.speak_type["points"] = st.text_input("How many points should your speech score on a scale of 1-100?")

        submit_button = st.form_submit_button("Submit")

    if submit_button:
        display_speech_info()

def display_speech_info():
    with st.sidebar:
        st.write("### Your Speech Details")
        st.write(f"- **Topic**: *{st.session_state.speak_type['topic']}*")
        st.write(f"- **Goal**: *{st.session_state.speak_type['goal']}*")
        st.write(f"- **Audience**: *{st.session_state.speak_type['addresant']}*")
        st.write(f"- **Speaker**: *{st.session_state.speak_type['speaker']}*")
        st.write(f"- **Score**: *{st.session_state.speak_type['points']}*")
    st.success("Your speech has been submitted!")

    min_score = st.session_state.speak_type['points']

    with st.spinner("Generating Speech"):
        speak_type = inputSpeakType(database_service)
        output = chatgpt_benutzen.gptbenutzen_infos(speak_type, min_score, database_service)

    st.success("speech generated")
    time.sleep(2)
    speech_output(output)

def speech_output(output):
    st.markdown(output)

setup()

