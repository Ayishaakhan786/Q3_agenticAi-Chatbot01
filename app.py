import streamlit as st
from dotenv import load_dotenv
from src.chatbot01.chatbot import get_model_responses

load_dotenv()

st.set_page_config(page_title="Multi-Model AI Chatbot", layout="centered")
st.title("Multi-Model Chatbot (OpenRouter via Streamlit)")

prompt = st.text_area("Enter your prompt:", placeholder="Ask me anything...")

if st.button("Generate Responses") and prompt:
    with st.spinner("Generating responses..."):
        results = get_model_responses(prompt)
    
    for model, text in results:
        st.subheader(f" Model: `{model}`")
        st.write(text)