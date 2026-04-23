from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

document = [
    "Virat Kohli is an Indian cricketer and former captain of the Indian national team.",
    "Sachin Tendulkar is a former Indian cricketer and one of the greatest batsmen in the history of cricket.",
    "M.S. Dhoni is a former Indian cricketer and captain of the Indian national team.",
    "Rohit Sharma is an Indian cricketer and the current captain of the Indian national team."
]

query = "Tell me about Rohit Sharma."

# Embed the documents and the query
document_embeddings = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

# Compute cosine similarity between the query and each document

scores = cosine_similarity([query_embedding], document_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]
print(f"Most similar document: {document[index]} with a similarity score of {score:.4f}")

