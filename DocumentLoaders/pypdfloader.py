#works on simple text pdfs not work well on scanned pdfs
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(len(docs))
print (docs[0].page_content)
print(docs[1].metadata)

#usecases
# pdfs with labels/columns ---> PDFPlumberLoader
# scanned/image pdfs ---> UnstructuredPDFLoader or AmazonTextractPDFLoader
# need layout and image data ---> PyMuPDFLoader
# want best structure extraction ---> UnstructuredPDFLoader