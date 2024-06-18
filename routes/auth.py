from fastapi import APIRouter, Depends, HTTPException, status
from schemas.auth_dto import LoginRequest
from services.auth_service import login

router = APIRouter(tags=["auth"])

@router.post("/login", status_code = status.HTTP_200_OK )
def login(request_data: LoginRequest):
    return login(request_data.email, request_data.password)
