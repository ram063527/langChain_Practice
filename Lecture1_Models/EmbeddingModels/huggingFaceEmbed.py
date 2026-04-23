from langchain_huggingface.embeddings import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

text = "I love India and I am proud to be an Indian."

document = [
    "I love India and I am proud to be an Indian.",
    "India is a country in South Asia. It is the seventh-largest country by land area and the second-most populous country in the world. India has a rich history and diverse culture, with many languages, religions, and traditions. The capital of India is New Delhi, and the largest city is Mumbai. India is known for its contributions to art, science, and technology, as well as its vibrant film industry, Bollywood.",
    "Diverse culture, rich history, and vibrant film industry make India a unique and fascinating country."
]

queryResult = embeddings.embed_query(text)
print("Query Result: ", queryResult)

documentResult = embeddings.embed_documents(document)
print("----------------------------------------"*20)
print("Document Result: ", documentResult)
