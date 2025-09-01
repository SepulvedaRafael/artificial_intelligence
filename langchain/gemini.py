import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.9,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=os.getenv("GEMINI_KEY")
)

# Mensagem direto
'''messages = [
    SystemMessage("Traduza o seguinte texto de Inglês para Português."),
    HumanMessage("Hi!")
]

print(llm.invoke(messages))'''

# Mensagem via template
system_template = "Traduza o seguinte texto em inglês para {idioma}"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

prompt = prompt_template.invoke({
    "idioma": "Italian",
    "text": "hi!"
})

print(llm.invoke(prompt))