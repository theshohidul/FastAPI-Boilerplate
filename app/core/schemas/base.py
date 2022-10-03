from typing import Any, List

from pydantic import BaseModel
from starlette.authentication import AuthenticationError
from fastapi.exceptions import RequestValidationError


class BaseResponse(BaseModel):
    status: int
    status_type: str
    message: str


class BaseAuthenticationError(AuthenticationError):
    status: int
    status_type: str
    message: str


class BaseValidationError(RequestValidationError):
    status: int
    status_type: str
    message: str
    errors: List[Any]
