from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")

parser = StrOutputParser()

# Create a prompt template that takes in the content of a document and asks the model to summarize it.

summarization_prompt = PromptTemplate(
    template="Summarize the following document:\n\n{text}\n\nSummary:",
    input_variables=["text"]
)

# Create a TextLoader object, specifying the path to the text file, and various other options like : encoding, chunk size, and chunk overlap as well as the metadata fields to include in the loaded documents.

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

# print(type(docs))
# print(len(docs))
# print(docs)

# print(docs[0].page_content) 
# print("******************************")
# print(docs[0].metadata)

# print(type(docs[0]))



# Create a chain 

chain = summarization_prompt | model | parser 
result = chain.invoke({
    "text": docs[0].page_content
})  
print(result)