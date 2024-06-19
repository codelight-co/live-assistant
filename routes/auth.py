from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.auth_dto import LoginRequest
from services.auth_service import login_service, user_create_service
from database.connection import get_db
from database.models import Users
from schemas.models import UserDto
from utils.security import  validate_token, get_current_user
from typing import Annotated
from sqlalchemy.orm import Session

router = APIRouter(tags=["auth"])

@router.post("/login", status_code = status.HTTP_200_OK )
def login(request_data: LoginRequest):
    return login_service(request_data.email, request_data.password)


@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(dto: UserDto, db: Session = Depends(get_db)):
    return user_create_service(db=db, dto=dto)

@router.get("/users/me")
async def read_users_me(current_user: Annotated[Users, Depends(get_current_user)]):
    print(current_user)
    return current_user