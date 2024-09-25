from DatabaseConnector import DatabaseConnector
from DatabaseService import DatabaseService
from chatbot import frontend

db_connector = DatabaseConnector()

def inputSpeakType():
    """
    Lässt den Nutzer seinen gewünschten Redentyp (speak_type) angeben

    :param db: Database to save data to
    :return: speak_type
    """

    speak_type = {
        "topic": frontend.st.session_state.speak_type['topic'],
        "goal": frontend.st.session_state.speak_type['goal'],
        "address": frontend.st.session_state.speak_type['addresant'],
        "speaker": frontend.st.session_state.speak_type['speaker']
    }

    prompt = DatabaseService(db_connector)
    prompt.create_table("prompt","(id INTEGER PRIMARY KEY AUTOINCREMENT, topics TEXT, addresses TEXT, goals TEXT, speakers TEXT)")
    prompt.insert_prompt(speak_type)

    return speak_type
