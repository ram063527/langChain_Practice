from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

chatModel = ChatOpenAI(model="openai/gpt-oss-120b:free", temperature=0.8,
                       openai_api_key=os.getenv("OPENAI_API_KEY"),
                        openai_api_base="https://openrouter.ai/api/v1"
                       )


messages = [
    (
        "system",
        "You are a helful assistant that translates English to Marathi. Translate the user sentence"
    ),
    ("user", "I love India and I am proud to be an Indian.")
]

result = chatModel.invoke(messages)
print(result.content)
