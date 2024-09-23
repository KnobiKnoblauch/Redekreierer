import streamlit as st
user_input = {}
speak_type_placeholders = {
    "topic": "What is your speech about?",
    "goal": "What is the goal of your speech?",
    "addresant": "Who is your addressee?",
    "speaker": "Who is delivering the speech?"
}

if 'speak_type' not in st.session_state:
    st.session_state.speak_type = {
        "topic": "",
        "goal": "",
        "addresant": "",
        "speaker": ""
    }

if 'current_step' not in st.session_state:
    st.session_state.current_step = 1

def setup():
    st.title("_Der Redekreierer_ :blue[von Knobi]")
    st.subheader("Lalalalaalalala")
    st.write("---") 

def input_loop():
    if 'worked' not in st.session_state:
        st.session_state.worked = False
    else:
        print("tedt")
    
    if st.session_state.worked == False:
        keys = list(st.session_state.speak_type.keys())
        current_key = keys[st.session_state.current_step - 1]
        placeholder = speak_type_placeholders[current_key]
        #print(st.session_state.current_step)
        if st.session_state.current_step < len(keys):
            user_input = st.chat_input(placeholder)
            print(f"user input: {user_input}")
            if user_input is not None:
                st.session_state.speak_type[current_key] = user_input
                st.session_state.current_step += 1
                st.session_state.worked = True
            else:
                st.session_state.worked = False
            #print(st.session_state.current_step)
            
        print(f"CurrentStep: {st.session_state.current_step}")

        if st.session_state.current_step >= len(st.session_state.speak_type):
            st.write("### Here's the speech information you provided:")
            st.write(st.session_state.speak_type)
    else:
        st.session_state.worked = False
    print(st.session_state.worked)


'''
if st.button('Submit'):
  if user_input:
      st.write(f"Chatbot:{user_input}")
      '''

setup()
input_loop()
print("finished")
