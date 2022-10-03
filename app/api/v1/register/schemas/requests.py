from pydantic import BaseModel, EmailStr, validator, Field


class RegisterRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: str = Field(..., min_length=1, max_length=32)
    password: str = Field(..., min_length=1, max_length=32)
