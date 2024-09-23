import streamlit as st
import time

# Use session state to store the speak_type dictionary
if 'speak_type' not in st.session_state:
    st.session_state.speak_type = {
        "topic": "",
        "goal": "",
        "addresant": "",
        "speaker": ""
    }


def setup():
    st.title("_Der Redekreierer_ :blue[von Tobi]")
    st.subheader("Lasse dir mit einfachen Schritten deine _eigene_, _personalisierte_ und _qualitativ hochwertige_ :blue[Rede] kreieren!", divider="gray")

    # Input form for the speech information
    with st.form("speech_form"):
        st.session_state.speak_type["topic"] = st.text_input("What is your speech about?")
        st.session_state.speak_type["goal"] = st.text_input("What are you trying to achieve with your speech?")
        st.session_state.speak_type["addresant"] = st.text_input("Who listens to your speech?")
        st.session_state.speak_type["speaker"] = st.text_input("Who is performing your speech?")

        # Submit button for the form
        submit_button = st.form_submit_button("Submit")

    # After submission, show the results
    if submit_button:
        display_speech_info()


# Function to display the gathered speech information
def display_speech_info():
    with st.sidebar:
        st.write("### Your Speech Details")
        st.write(f"- **Topic**: {st.session_state.speak_type['topic']}")
        st.write(f"- **Goal**: {st.session_state.speak_type['goal']}")
        st.write(f"- **Audience**: {st.session_state.speak_type['addresant']}")
        st.write(f"- **Speaker**: {st.session_state.speak_type['speaker']}")
    st.success("Your speech has been submitted!")
    with st.spinner("Generating Speech..."):
        time.sleep(5)
    st.succes("Speech Generated")
    time.sleep(2)
    st.markdown("Rede")


# Main setup function to run the app
setup()

