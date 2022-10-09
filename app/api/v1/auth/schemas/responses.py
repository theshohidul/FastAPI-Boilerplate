from typing import Optional

from pydantic import BaseModel, EmailStr, validator
from core.schemas.base import BaseResponse
from core.enums.status_type import StatusType
from core.enums.response_status import ResponseStatus


class TokenData(BaseModel):
    access_token: str
    refresh_token: Optional[str]
    access_expires: int
    refresh_expires: Optional[int]
    token_type: str = "Bearer"


class TokenPayload(BaseModel):
    sub: int
    name: str


class TokenResponse(BaseResponse):
    status: int = StatusType.SUCCESS.value
    status_type: str = ResponseStatus.USER_LOGGED_IN.name
    message: str = ResponseStatus.USER_LOGGED_IN.message
    data: TokenData
    _status_code: str = ResponseStatus.USER_LOGGED_IN.status_code
