# document upload


from langchain_community.document_loaders import TextLoader

loader = TextLoader("notes.txt", encoding="utf-8")

documents = loader.load()

print(documents[0].page_content)

print("------------done upload--------------------------------")





#  splitting (chunking)

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=30
)

chunks = text_splitter.split_documents(documents)

for chunk in chunks:
    print(chunk.page_content)
    print("-----------------")


print("Total chunks:", len(chunks))

print("\n first chunk:")
print(chunks[0].page_content)

print("\n chunk metadata:")
print(chunks[0].metadata)



# Embeddings(numerical representation)

from langchain_huggingface import HuggingFaceEmbeddings


# creating embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# chunks into vectors

vectors = embeddings.embed_documents(
    [chunk.page_content for chunk in chunks]
) 

print("total embeddings", len(vectors))
print("first embeddings", vectors[0])
print("vectors dimensions", len(vectors[0]))



# store the  embeddings in vectorDB

from langchain_community.vectorstores import FAISS

vector_store = FAISS.from_documents(
    chunks,
    embeddings
)

print("FAISS vector store created sucessfully")
print("Total vectors stored", vector_store.index.ntotal)

print("------------------------------------------------Data  stored in sucessfully----------------------------------------")

# similarity_search

query = "what is Machine Learning?"

results = vector_store.similarity_search(query, k=2)

for result in results:
    print(result.page_content)
    print("--------------------------------------")