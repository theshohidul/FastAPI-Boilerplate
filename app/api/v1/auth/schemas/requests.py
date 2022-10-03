from pydantic import BaseModel, EmailStr, validator, Field


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1, max_length=32)


class RefreshTokenRequest(BaseModel):
    refresh_token: str
