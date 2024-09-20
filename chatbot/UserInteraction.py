from DatabaseConnector import DatabaseConnector
from DatabaseService import DatabaseService

db_connector = DatabaseConnector()

def inputSpeakType():
    """
    Lässt den Nutzer seinen gewünschten Redentyp (speak_type) angeben

    :param db: Database to save data to
    :return: speak_type
    """

    speak_type = {
        "topic": input("Was ist das Thema deiner Rede: "),
        "goal": input("Was ist das Ziel deiner Rede: "),
        "address": input("An wen ist deine Rede gerichtet: "),
        "speaker": input("Wer hält deine Rede: ")
    }



    prompt = DatabaseService(db_connector)
    prompt.create_table("prompt","(id INTEGER PRIMARY KEY AUTOINCREMENT, topics TEXT, addresses TEXT, goals TEXT, speakers TEXT)")
    prompt.insert_prompt(speak_type)

    return speak_type
