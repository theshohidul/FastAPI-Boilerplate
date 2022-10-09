from pydantic import BaseModel, EmailStr, validator


class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str
    role: str
