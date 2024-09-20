import re

from openai import OpenAI

from DatabaseConnector import DatabaseConnector
from DatabaseService import DatabaseService

client = OpenAI(
    api_key="your own api key"
)

db = DatabaseConnector()
database_service = DatabaseService(db)

erste_frage = ""
answer = ""
differenz = ""


def aufgabe(speak_type):
    prompt = "Schreibe eine Rede über das Thema " + speak_type["topic"] + "und richte sie an " + speak_type[
        "address"] + " mit dem Ziel: " + speak_type["goal"]

    return prompt

def punktzahl_quality():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "du bist ein Bewerter"},
            {"role": "user",
             "content": "Bewerte diese Rede hinsichtlich der Qualität mit beachten dem Thema: " + database_service.select_last_row_but_id("prompt", 1)
                        + "dem Ziel: " + database_service.select_last_row_but_id("prompt", 3)
                        + "an wen die Rede gerichtet ist: " + database_service.select_last_row_but_id("prompt", 2)
                        + "und von wem sie gehalten wird: " + database_service.select_last_row_but_id("prompt", 4)
                        + "auf einer Skala von 1-33 und gebe als ausgabe nur eine einzige Zahl(keine leerzeichen etc.)"
                        + answer}
        ]
    )

    chat_gpt_response = response.choices[0].message.content
    return chat_gpt_response


def punktzahl_content():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "du bist ein Bewerter"},
            {"role": "user",
             "content": "Bewerte diese Rede hinsichtlich des Inhalts mit beachten dem Thema: " + database_service.select_last_row_but_id("prompt", 1)
                        + "dem Ziel: " + database_service.select_last_row_but_id("prompt", 3)
                        + "an wen die Rede gerichtet ist: " + database_service.select_last_row_but_id("prompt", 2)
                        + "und von wem sie gehalten wird: " + database_service.select_last_row_but_id("prompt", 4)
                        + "auf einer Skala von 1-33 und gebe als ausgabe nur eine einzige Zahl(keine leerzeichen etc.)"
                        + answer}
        ]
    )
    return response.choices[0].message.content


def punktzahl_laenge():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "du bist ein Bewerter"},
            {"role": "user",
             "content": "Bewerte diese Rede hinsichtlich der Länge mit beachten dem Thema: " + database_service.select_last_row_but_id("prompt", 1)
                        + "dem Ziel: " + database_service.select_last_row_but_id("prompt", 3)
                        + "an wen die Rede gerichtet ist: " + database_service.select_last_row_but_id("prompt", 2)
                        + "und von wem sie gehalten wird: " + database_service.select_last_row_but_id("prompt", 4)
                        + "auf einer Skala von 1-33 und gebe als ausgabe nur eine einzige Zahl(keine leerzeichen etc.)"
                        + answer}
        ]
    )
    return response.choices[0].message.content


def gptbenutzen_infos(speak_type):
    mindest_score = int(input("Wie gut soll die Rede auf einer Skala von 1-100 sein: "))

    if mindest_score > 85:
        mindest_score = 85

    frage = aufgabe(speak_type)
    global erste_frage
    erste_frage = frage
    global wichtig
    wichtig = antwort(frage, speak_type)

    score_type = {
        "quality": int(punktzahl_quality()),
        "content": int(punktzahl_content()),
        "length": int(punktzahl_laenge())
    }

    score = score_type["quality"] + score_type["content"] + score_type["length"]
    print(score)

    score_db = DatabaseService(db)
    score_db.create_table("score", "(id INTEGER PRIMARY KEY AUTOINCREMENT, quality, word_count, content)")
    score_db.insert_score_points(score_type)

    count = 1
    while mindest_score > score:
        print(f"Starte {count}. iteration")
        frage = erste_frage + wichtig + "verbessere das vorherige Ergebnis hinsichtlich Qualität, Länge und Inhalt"
        antwort(frage, speak_type)

        quality_punktzahl = int(punktzahl_quality())
        content_punktzahl = int(punktzahl_content())
        length_punktzahl = int(punktzahl_laenge())

        diff = quality_punktzahl + content_punktzahl + length_punktzahl - score

        score_later = {
            "quality": quality_punktzahl,
            "content": content_punktzahl,
            "length": length_punktzahl,
            "differenz": diff
        }

        improvement = DatabaseService(db)
        improvement.create_table("improvement", "(id INTEGER PRIMARY KEY AUTOINCREMENT, quality, word_count, content, how_much_more)")
        improvement.insert_improvement_points(score_later)

        score = score_later["quality"] + score_later["content"] + score_later["length"]

        print(f"{count}. Verbesserung auf score: {score}")

        count += 1
    else:
        print(antwort(frage, speak_type))


def antwort(frage, speak_type):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "du bist " + speak_type["speaker"]},
            {"role": "user", "content": frage}
        ]
    )
    global answer
    answer = response.choices[0].message.content
    return answer

# change