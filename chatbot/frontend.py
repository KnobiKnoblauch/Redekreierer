import streamlit as st
import time
#import chatgpt_benutzen



# funktioniert noch nicht



speak_type = {
    "topic" : "",
    "goal" : "",
    "addresant" : "",
    "speaker" : ""

}


def setup():
    st.title("_Der Redekreirer_ :blue[von Knobi]")
    st.subheader("Lalalalaalalala", divider="gray")
    input_loop()

def input_loop():
    speak_type["topic"] = get_topic()
    if speak_type["topic"] != "" and speak_type["topic"] != None:
        speak_type["goal"] = get_goal()
        if speak_type["goal"] != "" and speak_type["goal"] != None:
            speak_type["addresant"] = get_addresant()
            if speak_type["addresant"] != "" and speak_type["goal"] != None:
                speak_type["speaker"] = get_speaker()
                #if speak_type["speaker"] != "":
                    # alle inputs
    
    

def get_topic():
    prompt = st.chat_input("What is your speech about?")
    if prompt:
         return prompt

def get_goal():
    prompt = st.chat_input("What are you trying to achieve with your speech?")
    if prompt:
         return prompt

def get_addresant():
    prompt = st.chat_input("Who listens to your speech?")
    if prompt:
         return prompt

def get_speaker():
    prompt = st.chat_input("Who is performing your speech?")
    if prompt:
         return prompt

setup()


st.button("Rerun")
