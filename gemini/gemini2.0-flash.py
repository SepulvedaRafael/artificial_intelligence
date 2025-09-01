import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()

gemini_key = os.getenv("GEMINI_KEY")

client = genai.Client(api_key=gemini_key)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=types.Content(
        role='user',
        parts=[types.Part.from_text(text="Escreva uma história sobre o desenvolvimento do campo da Inteligência Artificial até a invenção dos LLMs.")]
    ),
    config=types.GenerateContentConfig(
        temperature=0.9
    )
)

print(response.text)