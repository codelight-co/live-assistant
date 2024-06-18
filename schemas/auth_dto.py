from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    email: str = Field(..., example="admin@gmail.com")
    password: str = Field(..., example="12345678") 

    class Config:
        orm_mode = True