from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader(file_path='dl-curriculum.pdf')
# docs = loader.load()

text = """I am writing to formally tender my resignation from my role as a Microsoft Learn Student Ambassador (MLSA), effective immediately. This decision follows deeply disturbing revelations—brought to light by a Microsoft employee during the company's 50th anniversary—regarding Microsoft’s involvement in the development and deployment of artificial intelligence technologies that are reportedly being used to enable and support human rights violations.

As a Muslim, I am morally and spiritually compelled to take a firm stand against injustice and oppression in all its forms. I cannot support or promote technologies that are implicated in the surveillance, targeting, and systemic harm of marginalized communities—especially when such tools are used in the context of ongoing genocides and the suppression of fundamental human rights."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 0,
)

# result = splitter.split_text(docs)
chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)