from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

chatModel = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview",
                                      temperature=0.8)

messages = [
    (
        "system",
        "You are a helful assistant that translates English to Marathi. Translate the user sentence"
    ),  
    ("user", "I love India and I am proud to be an Indian.")
]

result = chatModel.invoke(messages)
print(result.content)
