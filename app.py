import nest_asyncio

nest_asyncio.apply()

from llama_index.llms.ollama import Ollama

llm = Ollama(model="llama3", request_timeout=120.0)

from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

from llama_index.core import Settings

Settings.llm = llm
Settings.embed_model = embed_model


# import
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# from IPython.display import Markdown, display
import chromadb

chroma_client = chromadb.EphemeralClient()
chroma_collection = chroma_client.create_collection("quickstart")

# define embedding function
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# load documents
documents = SimpleDirectoryReader("./data/").load_data()

# set up ChromaVectorStore and load in data
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, embed_model=embed_model
)

# query_engine = index.as_query_engine(similarity_top_k=3)
# response = query_engine.query("Tell me about family matters")
# print(str(response))

from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.chat_engine import CondensePlusContextChatEngine

memory = ChatMemoryBuffer.from_defaults(token_limit=3900)

chat_engine = CondensePlusContextChatEngine.from_defaults(
    index.as_retriever(),
    memory=memory,
    llm=llm,
    context_prompt=(
        "You are a ai assistant, able to have normal interactions, as well as talk"
        " about Codelight."
        "Here are the relevant documents for the context:\n"
        "{context_str}"
        "\nInstruction: Use the previous chat history, or the context above, to interact and help the user."
    ),
    verbose=True,
)
# print(1)
# response = chat_engine.chat(
#     "Tell me about codelight."
# )
# print(str(response))

from flask import Flask, request

app = Flask(__name__)

@app.route("/assistant", methods=["POST"])
def askPDFPost():
    json_content = request.json
    query = json_content.get("query")
    global chat_engine
    response = chat_engine.chat(
        query
    )
    print(str(response))
    return str(response)


@app.route("/data", methods=["POST"])
def pdfPost():
    file = request.files["file"]
    file_name = file.filename
    save_file = "data/" + file_name
    file.save(save_file)
    print(f"filename: {file_name}")
    documents = SimpleDirectoryReader("./data/").load_data()

# set up ChromaVectorStore and load in data
    global index
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, embed_model=embed_model
    )
    global chat_engine
    chat_engine = CondensePlusContextChatEngine.from_defaults(
        index.as_retriever(),
        memory=memory,
        llm=llm,
        context_prompt=(
            "You are a chatbot, able to have normal interactions, as well as talk"
            " about Codelight."
            "Here are the relevant documents for the context:\n"
            "{context_str}"
            "\nInstruction: Use the previous chat history, or the context above, to interact and help the user."
        ),
        verbose=True,
    )
    
    response = {
        "status": "Successfully Uploaded",
        "filename": file_name,
    }
    return response
    


def start_app():
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == "__main__":
    start_app()




