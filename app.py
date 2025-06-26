import streamlit as st
from dotenv import load_dotenv
from src.chatbot01.chatbot import get_model_responses
import os

# ✅ First Streamlit command — must be at the top
st.set_page_config(page_title="Multi-Model AI Chatbot", layout="centered")

# ✅ Optional debug
st.write("🔑 API Key loaded:", os.getenv("OPENAI_API_KEY") is not None)

load_dotenv()

st.title("Multi-Model Chatbot (OpenRouter via Streamlit)")
st.markdown("#### Compare responses from 4 different models")

prompt = st.text_area("Enter your prompt:", placeholder="Ask me anything...")

if st.button("Generate Responses") and prompt:
    with st.spinner("Generating responses..."):
        results = get_model_responses(prompt)
    
    for model, text in results:
        st.subheader(f"🧠 Model: `{model}`")
        st.write(text)