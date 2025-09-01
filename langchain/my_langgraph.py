import os
import uuid
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.9,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=os.getenv("GEMINI_KEY")
)

# Definição do Grafo de Estado para Coordenarmos as mensagens
workflow = StateGraph(state_schema=MessagesState)

# Chamando o modelo com as mensagens
def call_model(state: MessagesState):
    response = llm.invoke(state["messages"])
    return {"messages": response}

# Definindo os estados da conversa
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# O armazenamento da memória da conversa
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# Definindo o ID da conversa pela thread
thread_id = str(uuid.uuid4())
config = {"configurable": {"thread_id": thread_id}}

query = "Olá, eu sou o Felipe!"
input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()

query = "Como eu me chamo?"
input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()
