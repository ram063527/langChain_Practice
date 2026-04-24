from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")
parser = StrOutputParser()


# Idea : Take a topic from the user and generate five interesting facts about it.

# Step 1: Create a prompt template for generating facts about a topic

prompt = PromptTemplate(
    template="Generate five interesting facts about the following topic: {topic}",
    input_variables=["topic"]
)

# Step 2 : Create a chain using LCEL 

chain = prompt | model | parser

# Step 3 : Run the chain with a user input
result = chain.invoke({"topic": "Office Chair"})
print(result)

chain.get_graph().print_ascii()







