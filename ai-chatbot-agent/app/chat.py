import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from transformers import pipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

DB_PATH = "db"

def chat_with_bot():
    print("🔍 Loading vector store from disk...")

    # Load embeddings and vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    retriever = vectorstore.as_retriever()

    print("🧠 Loading Falcon-1B-Instruct model (optimized for CPU)...")
    model_name = "tiiuae/falcon-1b-instruct"

    # Load the lightweight Falcon model
    llm_pipeline = pipeline(
    "text-generation",
    model="tiiuae/falcon-rw-1b",
    torch_dtype="auto",
    trust_remote_code=True
)


    print("💬 Chatbot ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("🧑 You: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        # Retrieve relevant documents from your knowledge base
        docs = retriever.get_relevant_documents(user_input)

        context = "\n".join([doc.page_content for doc in docs])
        prompt = f"Context:\n{context}\n\nQuestion: {user_input}\nAnswer:"

        # Generate response
        response = llm_pipeline(prompt)[0]["generated_text"]
        answer = response.split("Answer:")[-1].strip()
        print(f"🤖 Bot: {answer}\n")


if __name__ == "__main__":
    chat_with_bot()
