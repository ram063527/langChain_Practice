from langchain_core.prompts import ChatPromptTemplate

chat_template  = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert"),
    ('human', "Explain the concept of {concept} in simple terms.")
])

prompt = chat_template.invoke({"domain": "Politics Indian", "concept": "democracy"})

print(prompt)