import os
import chromadb
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

### Load ASU Library text files
documents = SimpleDirectoryReader("asu_data").load_data()

### Create embedding model (API key via env var)
embed_model = OpenAIEmbedding(api_key=os.getenv("OPENAI_API_KEY"))

### Create Chroma client (same path as the app)
client = chromadb.PersistentClient(path="./llamachromadb")

### Create or get ASU collection
collection = client.get_or_create_collection(name="asulib")

### Wrap Chroma with LlamaIndex
vector_store = ChromaVectorStore(chroma_collection=collection)

### Build index from documents
index = VectorStoreIndex.from_documents(
    documents,
    vector_store=vector_store,
    embed_model=embed_model,
)

print("ASU Library vector index built successfully.")
