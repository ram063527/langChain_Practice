# Structured Output Parser is now removed from Lanchain and Lanchain_core also.
# It might be available in langchain_classic 


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
                            task="text-generation")

model = ChatHuggingFace(llm=llm)
