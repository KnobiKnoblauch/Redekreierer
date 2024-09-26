import os
from openai import OpenAI
#from dotenv import load_dotenv

from prompt_creator import PromptCreationService

#load_dotenv()

api_key = "sk-UjackFxt9Fq7ya8FF-YEOrEweg812-RCLWunJ--GAsT3BlbkFJwEEmTIZNu01wlgUip5ICwzKlYQ8wmK-Jncq1dNqJEA"

client = OpenAI(api_key=api_key)

prompt_creation_service = PromptCreationService()

erste_frage = ""
answer = ""
differenz = ""


def punktzahl_quality(database_service):
    speech_type_params = database_service.select_speech_type_params("prompt")
    request = prompt_creation_service.create_openai_request(speech_type_params, "der Qualität", answer)
    response = client.chat.completions.create(**request)
    chat_gpt_response = response.choices[0].message.content

    print("Qualität: " + chat_gpt_response)

    return chat_gpt_response


def punktzahl_content(database_service):
    speech_type_params = database_service.select_speech_type_params("prompt")
    request = prompt_creation_service.create_openai_request(speech_type_params, "des Inhalts", answer)
    response = client.chat.completions.create(**request)
    chat_gpt_response = response.choices[0].message.content
    print("Inhalt: " + chat_gpt_response)
    return chat_gpt_response


def punktzahl_laenge(database_service):
    speech_type_params = database_service.select_speech_type_params("prompt")
    request = prompt_creation_service.create_openai_request(speech_type_params, "der Länge", answer)
    response = client.chat.completions.create(**request)
    chat_gpt_response = response.choices[0].message.content
    print("Länge: " + chat_gpt_response)
    return chat_gpt_response


def gptbenutzen_infos(speak_type, score, database_service):
    min_score = int(score)

    if min_score > 85:
        min_score = 85

    frage = prompt_creation_service.create_task_prompt(speak_type)

    global erste_frage
    erste_frage = frage
    global wichtig
    wichtig = antwort(frage, speak_type)

    score_type = {
        "quality": int(punktzahl_quality(database_service)),
        "content": int(punktzahl_content(database_service)),
        "length": int(punktzahl_laenge(database_service))
    }

    score = score_type["quality"] + score_type["content"] + score_type["length"]
    print(score)

    database_service.create_table("score", "(id INTEGER PRIMARY KEY AUTOINCREMENT, quality, word_count, content)")
    database_service.insert_score_points(score_type)

    count = 1
    while min_score > score:
        print(f"Starte {count}. iteration")
        frage = erste_frage + wichtig + "verbessere das vorherige Ergebnis hinsichtlich Qualität, Länge und Inhalt"
        antwort(frage, speak_type)

        quality_punktzahl = int(punktzahl_quality(database_service))
        content_punktzahl = int(punktzahl_content(database_service))
        length_punktzahl = int(punktzahl_laenge(database_service))

        diff = quality_punktzahl + content_punktzahl + length_punktzahl - score

        score_later = {
            "quality": quality_punktzahl,
            "content": content_punktzahl,
            "length": length_punktzahl,
            "differenz": diff
        }

        database_service.create_table("improvement", "(id INTEGER PRIMARY KEY AUTOINCREMENT, quality, word_count, content, how_much_more)")
        database_service.insert_improvement_points(score_later)

        score = score_later["quality"] + score_later["content"] + score_later["length"]

        print(f"{count}. Verbesserung auf score: {score}")

        count += 1
    else:
        return antwort(frage, speak_type)


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


def speech_name(speech):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "du bist ein Mensch"},
            {"role": "user", "content": "Gib dieser Rede einen Namen: " + speech}
        ]
    )
    return response.choices[0].message.content