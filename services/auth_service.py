from uuid import UUID
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Union, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from schemas.models import UserDto
from database.models import Users
import jwt


SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'


def generate_token(email: Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds=60 * 60 * 24 * 3  # Expired after 3 days
    )
    to_encode = {
        "exp": expire, "email": email
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    return encoded_jwt

def verify_user(email, password):
    ## hard code
    if (email == "admin@gmail.com" and password == "12345678"):
        return True
    if (email == "company1@gmail.com" and password == "12345678"):
        return True

    return False

def login_service(email, password):
    if verify_user(email, password):
        token = generate_token(email)
        return {
            'token': token,
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")


def user_create_service(db: Session, dto: UserDto):
    db_post = Users(email=dto.email, password=dto.password, role=dto.role)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# def get_current_user(db: Session, email:str):
#     db.query(Users).filter_by(email=email).one()

def get_current_user(email:str):
    if email == "admin@gmail.com":
        return Users(id="dabfc06b-b4c4-4493-a740-60545cb4ccf5",email="admin@gmail.com", password="12345678", role="admin", name="Thanh ADMIN")
    if email == "company1@gmail.com":
        return Users(id="d83c8f4f-ca91-4150-bcbe-28f06999ff9e",email="company1@gmail.com", password="12345678", role="company", name="John HR")