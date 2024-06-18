from uuid import UUID
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import Union, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt


SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'


def generate_token(username: Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds=60 * 60 * 24 * 3  # Expired after 3 days
    )
    to_encode = {
        "exp": expire, "username": username
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
    return encoded_jwt

def verify_user(email, password):
    if username == 'admin@gmail.com' and password == '12345678':
        return True
    return False

def login(email, password):
    if verify_user(email, password):
        token = generate_token(username)
        return {
            'token': token,
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")


