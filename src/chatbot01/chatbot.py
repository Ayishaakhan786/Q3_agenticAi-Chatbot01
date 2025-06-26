import os
from openai import OpenAI
from dotenv import load_dotenv

# ✅ Load environment variables from .env or Streamlit Secrets
load_dotenv()

# ✅ Get API Key from env (whether local or streamlit secret)
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Create OpenAI client with OpenRouter base URL
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# ✅ List of working models
models = [
    "mistralai/mistral-7b-instruct",
    "meta-llama/llama-3-8b-instruct",
    "undi95/toppy-m-7b",
    "mistralai/mistral-small-3.2-24b-instruct"
]

# ✅ Core function to get responses from each model
def get_model_responses(prompt: str):
    responses = []
    for model in models:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            text = response.choices[0].message.content
        except Exception as e:
            text = f"❌ Error from `{model}`: {e}"
        responses.append((model, text))
    return responses