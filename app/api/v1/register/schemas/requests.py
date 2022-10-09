from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class RolesEnum(str, Enum):
    renter = 'renter'
    landlord = 'landlord'


class RegisterRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="User full name")
    email: EmailStr
    phone: str = Field(..., min_length=4, max_length=32)
    password: str = Field(..., min_length=8, max_length=32)
    role: RolesEnum
