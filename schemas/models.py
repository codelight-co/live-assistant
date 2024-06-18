import enum
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class UserRole(enum.Enum):
    admin = "admin"
    company = "company"

class HealthResponse(BaseModel):
    status: str


class Post(BaseModel):
    id: Optional[UUID]
    title: str
    description: str

    class Config:
        orm_mode = True

class User(BaseModel):
    id: Optional[UUID]
    username: str
    password: str
    model_id: Optional[UUID]

    class Config:
        orm_mode = True
