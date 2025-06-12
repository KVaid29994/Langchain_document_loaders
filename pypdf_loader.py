from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\kanha\Desktop\GenAI\Langchain_document_loaders\dl-curriculum.pdf')

docs = loader.load()
# print (docs)
print(len(docs))
print(docs[0].page_content)
print(docs[1].metadata)

