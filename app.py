import streamlit as st
import requests

st.title("Banana Appender")

user_input = st.text_input("Enter a text string:")

if st.button("Append Bananas"):
    if user_input:
        response = requests.post("http://127.0.0.1:8000/append", json={"text": user_input})
        if response.status_code == 200:
            result = response.json().get("result")
            st.success(f"Result: {result}")
        else:
            st.error("Failed to get response from FastAPI server.")
    else:
        st.warning("Please enter a text string.")

