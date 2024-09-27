import streamlit as st
import chatgpt_benutzen
import time
import Login

from DatabaseConnector import DatabaseConnector
from DatabaseService import DatabaseService
import show_speech_page

db = DatabaseConnector()
database_service = DatabaseService(db)

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
        .stButton > button, .stForm div > button {
            background-color: #4F8BF9;  /* Deine Hintergrundfarbe */
            color: white;  /* Textfarbe */
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            margin-top: 10px;
            font-size: 16px;
            font-weight: bold;
        }

        .stButton > button:hover, .stForm div > button:hover {
            background-color: #3a7cd3;  
            color: white;
            outline: none;
        }

        .stButton > button:focus, .stForm div > button:focus {
            outline: none !important;
            box-shadow: none !important;
            color: white !important;
            border: none !important;
        }

        .stButton > button:active, .stForm div > button:active {
            background-color: #4F8BF9 !important;
            color: white !important;
            outline: none !important;
            box-shadow: none !important;
        }
        
         .stSuccess {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            background-color: #4F8BF9; /* Deine gewünschte Hintergrundfarbe */
            color: white; /* Textfarbe */
            border-radius: 5px; /* Abgerundete Ecken */
            padding: 10px; /* Innenabstand */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Optionaler Schatten */
            border: 2px solid white;
        }
        
        .custom-divider {
            border: 0;
            height: 2px; /* Höhe der Linie */
            background-color: #4F8BF9; /* Ändere die Farbe hier */
            margin: 20px 0; /* Abstand oben und unten */
        
        }
    
        /* Expander Container */
        .stExpander {
            border-radius: 5px;
            overflow: hidden;
        }
        
        .st-emotion-cache-p5msec.eqpbllx1:hover {
            color: white !important;
        }
        
        .st-emotion-cache-p5msec.eqpbllx1:hover {
            color: white !important;
        }
        
        svg:hover {
            color: white !important;
        }

        /* Hintergrundfarbe und Textfarbe beim Hover */
        .stExpander:hover {
            background-color: #3e74d8;
            color: white !important;
        }

        /* Standardfarbe des Expanders */
        .stExpander h2, .stExpander .stExpanderHeader {
            color: black !important; /* Standard Schriftfarbe */
        }

        /* Toggle-Button/ Header des Expanders, wenn man über ihn fährt */
        .stExpanderHeader:hover {
            background-color: #3e74d8; /* Gleiche Hintergrundfarbe beim Hover */
            color: white !important; /* Schriftfarbe wird weiß beim Hover */
        }

        /* Speziell der Text und Pfeil-Symbol im geöffneten Zustand */
        .stExpander:focus-within .stExpanderHeader {
            background-color: #3e74d8; /* Hintergrund bleibt im geöffneten Zustand blau */
            color: white !important; /* Schrift und Pfeil bleibt weiß */
        }

        /* Speziell für das Pfeil-Symbol und den Header-Text */
        .stExpanderHeader:hover div {
            color: white !important;
        }

        /* Auch im geöffneten Zustand die Farben beibehalten */
        .stExpanderHeader:focus-within {
            background-color: #3e74d8; 
            color: white !important;
        }
   
    </style>
""", unsafe_allow_html=True)


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
        st.markdown('<h1 class="title">Der Redekreierer</h1>', unsafe_allow_html=True)
        st.container(height=30, border=False)
        st.markdown('<div class="subtitle">Lasse dir mit einfachen Schritten deine eigene, personalisierte und qualitativ hochwertige Rede kreieren!</div>', unsafe_allow_html=True)
        st.container(height=30, border=False)
        st.session_state.speak_type["topic"] = st.text_input("What is your speech about?")
        st.session_state.speak_type["goal"] = st.text_input("What are you trying to achieve with your speech?")
        st.session_state.speak_type["addresant"] = st.text_input("Who listens to your speech?")
        st.session_state.speak_type["speaker"] = st.text_input("Who is performing your speech?")
        st.session_state.speak_type["points"] = st.text_input("How many points should your speech score on a scale of 1-100?")

        submit_button = st.button("Submit", use_container_width=True)

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



                with st.expander(speech):
                    col1, col2 = st.columns(2)
                    id = database_service.select_table_id("saved_speeches", "id", speech)
                    with col1:
                        st.button("Delete Speech", on_click=delete_speech, key=f"delete_{id}", args=id)
                    with col2:
                        st.button("Show Speech", on_click=show_speech, key=f"show_{id}", args=id)

        if submit_button:
           if st.session_state.speak_type["topic"] == "" or st.session_state.speak_type["goal"] == "" or st.session_state.speak_type["addresant"] == "" or st.session_state.speak_type["speaker"] == "" or st.session_state.speak_type["points"] == "":
               st.markdown('<div class="message">Some fields are empty</div>', unsafe_allow_html=True)
           display_speech_info()


def speech_saved(speech):
    with st.spinner("Saving Speech"):
        username = Login.st.session_state.username
        cursor.execute("INSERT INTO Users WHERE username == {username} (speech) VALUES (?)", (speech))
        time.sleep(5)
    st.markdown('<div class="stSuccess">Speech saved</div>', unsafe_allow_html=True)


def display_speech_info():
    st.markdown('<div class="stSuccess">Your Speech has been submitted</div>', unsafe_allow_html=True)

    min_score = st.session_state.speak_type['points']

    with st.spinner("Generating Speech"):
        speak_type = input_speak_type(database_service)
        st.session_state.output = chatgpt_benutzen.gptbenutzen_infos(speak_type, min_score, database_service)
    output = st.session_state.output
    st.markdown('<div class="stSuccess">speech generated</div>', unsafe_allow_html=True)
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

    st.markdown('<div class="stSuccess">Speech deleted</div>', unsafe_allow_html=True)


def show_speech(id):
    st.session_state.show_speech = True
    st.session_state.speech_id = id
    show_speech_page.setup_show_speech(id)


def return_home():
    st.session_state.show_speech = False


setup()
