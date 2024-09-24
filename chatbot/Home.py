import streamlit as st



st.sidebar.title("Navigation")


pages_dict = {
    "Authentication": {
        "Login": "pages.Account.login",
        "Signup": "pages.auth.signup"
    },
    "Standalone Pages": {
        "About": "pages.about",
        "Contact": "pages.contact"
    }
}