class PromptCreationService:

    def __int__(self):
        pass

    def create_speech_prompt(self, prompt_param, eval_param, answer):
        """
            Kreiert die Speech Type Parameter

            :param prompt_param:
            :param eval_param:
            :param answer:
            :return:
        """

        return f"Bewerte diese Rede hinsichtlich {eval_param} " \
               f"mit beachten dem Thema: {prompt_param['topic']} " \
               f"mit dem Ziel {prompt_param['goal']} " \
               f"an wen die Rede gerichtet ist {prompt_param['adresse']} " \
               f"und von wem sie gehalten wird {prompt_param['speaker']} " \
               f"auf einer Skala von 1-33 und gebe als Ausgabe nur " \
               f"eine einzige Zahl (kein Leerzeichen etc.) aus {answer}"

    def create_openai_request(self, prompt_param, eval_param, answer, model="gpt-4o-mini"):
        """
            Erstellt die Request parameter für den open AI Aufruf (Request)

            :param prompt:
            :param eval_param:
            :param model:
            :return:
        """
        system_content = "du bist ein Bewerter"
        user_content = self.create_speech_prompt(prompt_param, eval_param, answer)

        return {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": system_content
                },
                {
                    "role": "user",
                    "content": user_content
                }
            ]
        }

    def create_task_prompt(self, speak_type):
            return "Schreibe eine Rede über das Thema " + \
                     speak_type["topic"] + " und richte sie an " + \
                     speak_type["address"] + " mit dem Ziel: " + \
                     speak_type["goal"]
