from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")
parser = StrOutputParser()

# Idea : Take a topic from the user and generate a detailed report on a topic and then send back that response to the LLM and generate a 5 line summary.

# Step 1: Create a prompt template for generating a detailed report about a topic
prompt1 = PromptTemplate(
    template="Generate a detailed report about the following topic: {topic}",
    input_variables=["topic"]
)

# Step 2 : Create a prompt template for generating a summary of the report

prompt2 = PromptTemplate(
    template="Summarize the following report in 5 lines: {report}",
    input_variables=["report"]
)

# Step 3 : Create a chain using LCEL
chain = prompt1 | model | parser | prompt2 | model | parser

# Step 4 : Run the chain with a user input
result = chain.invoke({"topic": "Office Chair"})
print(result)
chain.get_graph().print_ascii()
