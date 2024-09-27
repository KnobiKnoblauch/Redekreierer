import streamlit as st
import time

from DatabaseConnector import DatabaseConnector
from DatabaseService import DatabaseService

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
        .stSubheader{
            
            text-align: center;
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

def setup_show_speech(id):

    speech = database_service.select_table_name("saved_speeches", "name", id)

    st.markdown("""
                <div style="text-align: center;">
                    <h1 class="title"style="line-height: 1.2;">Der Redekreierer</h1>
                </div>
            """, unsafe_allow_html=True)
    
    st.subheader(speech)

    show_speech(id)

    st.button("Return back to Home", on_click=return_home)


def return_home():
    st.session_state.show_speech = False


def show_speech(id):
    speech = database_service.select_table_spalte("saved_speeches", "speech", id)
    st.write(speech)