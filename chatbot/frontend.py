import streamlit as st
import chatgpt_benutzen
import time

from DatabaseConnector import DatabaseConnector
from DatabaseService import DatabaseService
import show_speech_page

db = DatabaseConnector()
database_service = DatabaseService(db)


st.markdown(
    """
    <style>
    .custom-divider {
        border: 0;
        height: 2px; /* Höhe der Linie */
        background-color: #0099FF; /* Ändere die Farbe hier */
        margin: 20px 0; /* Abstand oben und unten */
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'show_speech' not in st.session_state:
    st.session_state.show_speech = False


def input_speak_type(database_service):
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

    database_service.create_table("prompt", "(id INTEGER PRIMARY KEY AUTOINCREMENT, topics TEXT, addresses TEXT, goals TEXT, speakers TEXT)")
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
    if not st.session_state.show_speech:
        st.title("*Der Redekreierer* **von** :blue[Knobi] **und** :blue[TayozZ]")
        st.subheader("Lasse dir mit einfachen Schritten deine _eigene_, _personalisierte_ und _qualitativ hochwertige_ :blue[Rede] kreieren!", divider="blue")

        with st.form("speech_form"):
            st.session_state.speak_type["topic"] = st.text_input("What is your speech about?")
            st.session_state.speak_type["goal"] = st.text_input("What are you trying to achieve with your speech?")
            st.session_state.speak_type["addresant"] = st.text_input("Who listens to your speech?")
            st.session_state.speak_type["speaker"] = st.text_input("Who is performing your speech?")
            st.session_state.speak_type["points"] = st.text_input("How many points should your speech score on a scale of 1-100?")

            submit_button = st.form_submit_button("Submit")

            with st.sidebar:
                st.write("### Your Speech Details")
                st.write(f"- **Topic**: *{st.session_state.speak_type['topic']}*")
                st.write(f"- **Goal**: *{st.session_state.speak_type['goal']}*")
                st.write(f"- **Audience**: *{st.session_state.speak_type['addresant']}*")
                st.write(f"- **Speaker**: *{st.session_state.speak_type['speaker']}*")

                st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

                st.write("### Your Saved Speeches ")

                saved_speeches = database_service.select_table("saved_speeches", "name")


                for speech in saved_speeches:
                    with st.popover(speech):
                        id = database_service.select_table_id("saved_speeches", "id", speech)

                        st.button("Delete Speech", on_click=delete_speech, key=f"delete_{id}", args=id)
                        st.button("Show Speech", on_click=show_speech, key=f"show_{id}", args=id)

        if submit_button:
            display_speech_info()


def speech_saved(speech):
    with st.spinner("Saving Speech"):
        database_service.create_table("saved_speeches", "(id INTEGER PRIMARY KEY AUTOINCREMENT, speech, name)")
        st.success("Tabelle erstellt")
        database_service.insert_speech(speech, chatgpt_benutzen.speech_name(speech))
        time.sleep(5)
    st.success("Speech saved")


def display_speech_info():

    st.success("Your speech has been submitted!")

    min_score = st.session_state.speak_type['points']

    with st.spinner("Generating Speech"):
        speak_type = input_speak_type(database_service)
        st.session_state.output = chatgpt_benutzen.gptbenutzen_infos(speak_type, min_score, database_service)
    output = st.session_state.output
    st.success("speech generated")
    time.sleep(2)
    speech_output(output)

    if 'speech_saved' not in st.session_state:
        st.session_state.speech_saved = False

    st.button("Save for later", on_click=uebergang)


def uebergang():
    output = st.session_state.output
    speech_saved(output)


def speech_output(speech):
    st.markdown(speech)


def delete_speech(id):

    database_service.delete_speech(id)

    with st.spinner("deleting Speech"):
        time.sleep(2)

    st.success("Speech deleted")


def show_speech(id):
    st.session_state.show_speech = True
    st.session_state.speech_id = id
    show_speech_page.setup_show_speech(id)


def return_home():
    st.session_state.show_speech = False


setup()
