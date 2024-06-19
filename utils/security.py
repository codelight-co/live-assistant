
import time
import jwt
from typing import Annotated, Union
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import ValidationError
from database.models import Users
from sqlalchemy.orm import Session

SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'

reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)


def validate_token(http_authorization_credentials=Depends(reusable_oauth2)) -> str:
    """
    Decode JWT token to get username => return username
    """
    try:
        payload = jwt.decode(http_authorization_credentials.credentials, SECRET_KEY, algorithms=[SECURITY_ALGORITHM])

        if payload.get('exp') < time.time():
            raise HTTPException(status_code=403, detail="Token expired")

        print(payload)

        return payload.get('email')

    except(jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=403,
            detail=f"Could not validate credentials",
        )

def fake_user(email:str):
    if email == "admin@gmail.com":
        return Users(id="dabfc06b-b4c4-4493-a740-60545cb4ccf5",email="admin@gmail.com", password="12345678", role="admin", name="Thanh ADMIN")
    if email == "company1@gmail.com":
        return Users(id="d83c8f4f-ca91-4150-bcbe-28f06999ff9e",email="company1@gmail.com", password="12345678", role="company", name="John HR")
    if email == "company2@gmail.com":
        return Users(id="0e6b0050-199e-4a75-bec5-3afc9e80afac",email="company2@gmail.com", password="12345678", role="company", name="Adam HR")


async def get_current_user(token: Annotated[str, Depends(validate_token)]):
    user = fake_user(token)
    return user

