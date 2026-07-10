import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

st.title("Chatbot using Streamlit")
prompt = st.text_input("Enter the Prompt",placeholder = "Ask anything 😊")

if st.button("Ask AI"):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt,
    )

    st.write(f"Bot : {response.text}")