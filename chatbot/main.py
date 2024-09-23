import chatgpt_benutzen
from UserInteraction import inputSpeakType



def frontend_output():
    while True:
        speak_type = inputSpeakType()
        chatgpt_benutzen.gptbenutzen_infos(speak_type)