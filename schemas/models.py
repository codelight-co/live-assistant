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

class UserDto(BaseModel):
    id: Optional[UUID]
    email: str
    password: str
    role: UserRole

    class Config:
        orm_mode = True
