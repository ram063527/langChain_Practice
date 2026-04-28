from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('UpdatedCAS.pdf')


docs = loader.load()

# print(docs)
# print(len(docs))


# print(docs[0].page_content)
# print("-----------------------------"*10)
# print(docs[0].metadata)


