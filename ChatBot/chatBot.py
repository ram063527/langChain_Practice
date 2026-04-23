from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")


chat_history = [
    SystemMessage(content="You are a helpful assistant and expert in Politics Indian"),
]


while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.text))
    print('Bot:', result.text)

print('Chat ended.')
print('Chat History:')
for message in chat_history:
    print(message)  