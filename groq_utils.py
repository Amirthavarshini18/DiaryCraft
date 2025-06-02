# # diary_app/groq_utils.py
# import openai

# # Replace this with your GROQ-compatible OpenAI API key
# openai.api_key = "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"

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the OpenAI client with Groq API
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def format_diary(hints):
    prompt = f"""You are an assistant that writes diary entries by expanding only on the user-provided hints. Do not add any extra events, facts, or people. Only elaborate on what is already mentioned, adding natural language, emotions, and structure to turn the hints into a coherent first-person diary entry around 150 to 300words:\n\nHints:\n{hints}\n\nDiary Entry:"""

    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Groq-supported LLaMA3 model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=800
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Fallback in case of API issues
        return f"Error generating diary entry: {str(e)}. Original hints: {hints}"