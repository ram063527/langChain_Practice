from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
                            task="text-generation")

chatModel = ChatHuggingFace(llm=llm, temperature=0.8)

messages = [
    (
        "system",
        "You are a helful assistant that translates English to Marathi. Translate the user sentence"
    ),
    ("user", "I love India and I am proud to be an Indian.")
]

result = chatModel.invoke(messages)
print(result.content)
