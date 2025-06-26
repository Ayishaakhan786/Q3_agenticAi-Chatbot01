import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# Load .env from root
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

models = [
    "mistralai/mistral-7b-instruct",
    "meta-llama/llama-3-8b-instruct",
    "undi95/toppy-m-7b",
    "mistralai/mistral-small-3.2-24b-instruct"
]

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
            text = f" Error: {e}"
        responses.append((model, text))
    return responses