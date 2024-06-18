from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.models import User
from schemas.admin_dto import LoginRequest
from database.connection import get_db
from services.admin_service import login
from utils.security import reusable_oauth2, validate_token


router = APIRouter(tags=["admin"])

# Endpoint to retrieve a list of all companies
@router.get('/companies', dependencies=[Depends(validate_token)])
def get_all_companies():
    # Logic to retrieve all companies
    companies = []
    return companies
# Endpoint to create a new company
@router.post('/companies')
def create_company():
    # Logic to create a new company using request data
    # ...
    # Retrieve the company data from the request
    company_data = request.json()
    return {'message': 'Company created successfully'}

# Endpoint to delete a company
@router.delete('/admin/companies/{companyId}')
def delete_company(companyId: int):
    # Logic to delete the specified company
    # ...
    return {'message': 'Company deleted successfully'}

@router.get('/agents')
def get_all_agents():
    # Logic to retrieve all AI agents
    # ...
    agents = []
    # Populate the agents list with retrieved data
    # ...
    return agents

# Endpoint to retrieve a list of all end-users for a specific AI agent
@router.get('/agents/{agentId}/users')
def get_agent_users(agentId: int):
    # Logic to retrieve all end-users for the specified AI agent
    # ...
    users = []
    # Populate the users list with retrieved data
    # ...
    return users

# Endpoint to retrieve platform-wide analytics
@router.get('/analytics')
def get_platform_analytics():
    # Logic to retrieve platform-wide analytics
    # ...
    analytics = {}
    # Populate the analytics data
    # ...
    return analytics

# @router.post("/create", status_code=status.HTTP_201_CREATED, response_model=User)
# def create_company(user: User, db: Session = Depends(get_db)):
#     return company_create(db=db, user=user)