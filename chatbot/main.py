import chatgpt_benutzen
from UserInteraction import inputSpeakType

if __name__ == '__main__':


    while True:
        speak_type = inputSpeakType()
        chatgpt_benutzen.gptbenutzen_infos(speak_type)
