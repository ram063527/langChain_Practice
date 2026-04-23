from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")

messages = [
    SystemMessage(content="You are a helpful assistant and expert in Politics Indian"),
    HumanMessage(content="Tell me whether india is truely democratic country or not?")
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.text))
print(messages)