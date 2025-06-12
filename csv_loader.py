from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(r"C:\Users\kanha\Desktop\GenAI\Langchain_document_loaders\Social_Network_Ads.csv")

docs = loader.load()

print ((docs[5:9]))