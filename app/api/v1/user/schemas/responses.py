from pydantic import BaseModel, EmailStr, validator


class SystemUser(BaseModel):
    name: str
    email: EmailStr
    phone: str