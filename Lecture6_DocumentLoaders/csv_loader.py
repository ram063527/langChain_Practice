from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="cricketStats.csv")

docs = loader.load()
# docs = loader.lazy_load()

print(len(docs)) # expected output: 10

# for first row
# print(docs[0].page_content)
# print(docs[0].metadata) 

# # TYpe of docs[0]
# print(type(docs[0]))    



print(docs)