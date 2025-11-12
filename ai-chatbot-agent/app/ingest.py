import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def create_knowledge_base():
    data_folder = "data"
    persist_directory = "db"

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        print(f"📂 Created empty data folder at: {data_folder}")
        print("⚠️ Please add your .txt or .md files inside the 'data' folder.")
        return

    loader = DirectoryLoader(data_folder, glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()

    print(f"📄 Loaded {len(documents)} document(s).")
    if not documents:
        print("⚠️ No text files found in 'data' folder.")
        return

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    print(f"🧩 Split into {len(texts)} chunks.")

    print("🔍 Loading embedding model (this may take a few seconds)...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("⚙️ Generating embeddings...")
    sample = embeddings.embed_query("test embedding")
    print(f"✅ Sample embedding generated with length {len(sample)}.")

    print("💾 Creating and saving Chroma vector store...")
    Chroma.from_documents(texts, embeddings, persist_directory=persist_directory)

    print(f"✅ Knowledge base created and saved in '{persist_directory}'")

if __name__ == "__main__":
    create_knowledge_base()
