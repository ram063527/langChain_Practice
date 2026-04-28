from langchain_community.document_loaders import  WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")
parser =  StrOutputParser()

prompt = PromptTemplate(
    template="Anwer the question based on the following text: {text} \n Question: {question}",
    input_variables=["text", "question"]
)

url = "https://en.wikipedia.org/wiki/Cricket#Laws_and_gameplay"

loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | chatModel | parser
result = chain.invoke({
    'question': "What does LBW mean in cricket?",
    'text': docs[0].page_content
}
)

print(result)