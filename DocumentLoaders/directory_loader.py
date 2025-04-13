#helps u load multiple documents from a directory(folder) of files

from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

loader = DirectoryLoader(
    path = 'books',
    glob = '*.pdf',#pattern u want to load that pattern files
    loader_cls=PyPDFLoader
)
docs = loader.lazy_load() 

for document in docs:
    print(document.metadata)

