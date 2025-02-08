# ##Data ingestion steps
#txt file read
# from langchain_community.document_loaders import TextLoader
# loader= TextLoader("speech.txt")
# text_documents = loader.load()
# print(text_documents)

# #KEYS
# import os
# from dotenv import load_dotenv
# load_dotenv()

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# #one more data ingestion technique
# #webbasedloader
# from langchain_community.document_loaders import WebBaseLoader
# import bs4
# #load,chunk and index the contents of the html page
# loader= WebBaseLoader(web_path=("https://lilianweng.github.io/posts/2023-06-23-agent/"),
#                        bs_kwargs=dict(parse_only=bs4.SoupStrainer(
#                            class_=("post-title","post-content","post-header")
                           
#                        )))

# text_documents=loader.load()
# print(text_documents)

#pdf reader..load
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('K21sw036_Proposal.pdf')
docs = loader.load()


#Transform...into chunks
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
documents = text_splitter.split_documents(docs)


#vector embedding and vector store
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
db = Chroma.from_documents(documents[:20],OpenAIEmbeddings())

#Vector database
query = "Who is the supervisor?"
results = db.similarity_search(query)
print(results)
