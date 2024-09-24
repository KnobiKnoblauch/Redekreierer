import streamlit as st
import time
 
st.title('Chat')
 
if "messages" not in st.session_state:
    st.session_state.messages = []
if "selected_index" not in st.session_state:
    st.session_state.selected_index = 0
 
for messages in st.session_state.messages:
    with st.chat_message(messages["role"]):
        st.markdown(messages["content"])
 
if prompt := st.chat_input("Do Input"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user", "content":prompt})
 
def enumerate(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1
 
def response_generator():
    for counter, question in enumerate(
    [
        "Question 1",
        "Question 2",
        "Question 3"
    ]):
        if counter == st.session_state.selected_index:
            for word in question.split():
                yield word + " "
                time.sleep(0.05)
    st.session_state.selected_index += 1
    if st.session_state.selected_index > 2:
        st.session_state.selected_index = 0
    print(st.session_state.selected_index)

    
 
with st.chat_message("assistent"):
    response = st.write_stream(response_generator())
    st.session_state.messages.append({"role":"assistent", "content":response})