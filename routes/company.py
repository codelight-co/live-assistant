from fastapi import APIRouter, Depends, HTTPException, status
from fastapi import FastAPI, UploadFile, File
from fastapi import Request
from sqlalchemy.orm import Session
from database.models import Users
from schemas.models import UserDto
from typing import Annotated
from pathlib import Path
from utils.security import  validate_token, get_current_user
from database.connection import get_db
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from ai_models.app import pdfPost as ai_pdf_post

router = APIRouter(tags=["company"])

@router.post('/upload-data')
async def build_knowledge(current_user: Annotated[Users, Depends(get_current_user)],request: Request, file: UploadFile = File(...)):
    id = current_user.id
    file_name = file.filename
    print(file_name)    
    save_dir = Path("ai_models/data") / id
    save_dir.mkdir(parents=True, exist_ok=True)
    save_file = save_dir / file_name
    with save_file.open("wb") as buffer:
        buffer.write(await file.read())
    print(f"filename: {file_name}")
    # documents = SimpleDirectoryReader("./ai_models/data/").load_data()
    # return ai_pdf_post(documents)


# Endpoint to authenticate a company user
@router.post('/login')
def company_login():
    # Authentication logic here
    # ...
    return {'message': 'Company user authentication successful'}

# Endpoint to retrieve a list of all AI agents for the company
@router.get('/agents')
def get_company_agents():
    # Logic to retrieve all AI agents for the company
    # ...
    agents = []
    # Populate the agents list with retrieved data
    # ...
    return agents

# Endpoint to create a new AI agent for the company
@router.post('/agents')
def create_agent():
    # Logic to create a new AI agent for the company using request data
    # ...
    # Retrieve the agent data from the request
    agent_data = request.json()
    # Process and create the agent
    # ...
    return {'message': 'AI agent created successfully'}

# Endpoint to update an AI agent for the company
@router.put('/agents/{agentId}')
def update_agent(agentId: int):
    # Logic to update the specified AI agent for the company using request data
    # ...
    # Retrieve the agent data from the request
    agent_data = request.json()
    # Process and update the agent
    # ...
    return {'message': 'AI agent updated successfully'}

# Endpoint to delete an AI agent for the company
@router.delete('/agents/{agentId}')
def delete_agent(agentId: int):
    # Logic to delete the specified AI agent for the company
    # ...
    return {'message': 'AI agent deleted successfully'}

# Endpoint to update the knowledge base for an AI agent
@router.post('/agents/{agentId}/knowledge')
def update_agent_knowledge(agentId: int):
    # Logic to update the knowledge base for the specified AI agent using request data
    # ...
    # Retrieve the knowledge data from the request
    knowledge_data = request.json()
    # Process and update the knowledge base
    # ...
    return {'message': 'Knowledge base updated successfully'}

# Endpoint to retrieve a list of all end-users for a specific AI agent
@router.get('/agents/{agentId}/users')
def get_agent_users(agentId: int):
    # Logic to retrieve all end-users for the specified AI agent
    # ...
    users = []
    # Populate the users list with retrieved data
    # ...
    return users

# Endpoint to retrieve analytics for the company's agents
@router.get('/analytics')
def get_company_analytics():
    # Logic to retrieve analytics for the company's agents
    # ...
    analytics = {}
    # Populate the analytics data
    # ...
    return analytics