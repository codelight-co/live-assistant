

from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.storage.index_store.redis import RedisIndexStore
from llama_index.storage.docstore.redis import RedisDocumentStore
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.chat_engine import CondensePlusContextChatEngine
from llama_index.storage.chat_store.redis import RedisChatStore
from fastapi import APIRouter, Depends, HTTPException, status, Request, File, UploadFile
from database.models import Users
from typing import Annotated
from utils.security import  validate_token, get_current_user
import os


llm = Ollama(model="llama3", request_timeout=120.0)
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

Settings.llm = llm
Settings.embed_model = embed_model


# define embedding function
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")





router = APIRouter(tags=["ai"])

@router.post("/assistant/{agent_id}", status_code = status.HTTP_200_OK )
async def ask_ai_data(agent_id:str,user_unique_str:str, request: Request):
    # Save the uploaded file
    base_directory = f"./ai_models/data/{agent_id}"
    
    index_store = RedisIndexStore.from_host_and_port(
        host="127.0.0.1", port="6379", namespace=f"llama_index/{agent_id}"
    )

    # load documents
    documents = SimpleDirectoryReader(base_directory).load_data()

    storage_context = StorageContext.from_defaults(index_store=index_store)
    index = VectorStoreIndex.from_documents(
        documents, storage_context=storage_context, embed_model=embed_model
    )
    
    chat_store = RedisChatStore(redis_url="redis://localhost:6379", ttl=300)
    memory = ChatMemoryBuffer.from_defaults(
        token_limit=3900,
        chat_store=chat_store,
        chat_store_key=f"{agent_id}/{user_unique_str}",
    )
    
    
    chat_engine = CondensePlusContextChatEngine.from_defaults(
        index.as_retriever(),
        memory=memory,
        llm=llm,
        context_prompt=(
            "You are a chatbot, able to have normal interactions"
            "Here are the relevant documents for the context:\n"
            "{context_str}"
            "\nInstruction: Use the previous chat history, or the context above, to interact and help the user."
        ),
        verbose=True,
    )
    json_content = await request.json()
    query = json_content.get("query")
    print(query)
    response = chat_engine.chat(query)
    print(str(response))
    return str(response)


@router.post("/data", status_code = status.HTTP_200_OK )
async def data_post(current_user: Annotated[Users, Depends(get_current_user)], file: UploadFile = File(...)):
    id = current_user.id
    # Save the uploaded file
    base_directory = f"./ai_models/data/{id}"
    file_location = os.path.join(base_directory, file.filename)
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    print(f"filename: {file.filename}")
    
    response = {
        "status": "Successfully Uploaded",
        "filename": file.filename,
    }
    return response
    



