from typing import Any, List

from pydantic import BaseModel
from starlette.authentication import AuthenticationError
from fastapi.exceptions import RequestValidationError


class BaseResponse(BaseModel):
    status: str
    status_type: str
    message: str
    _status_code: int

    class Config:
        arbitrary_types_allowed = True
        underscore_attrs_are_private = True

    @property
    def status_code(self):
        return self._status_code


class BaseAuthenticationError(AuthenticationError):
    status: str
    status_type: str
    message: str

    class Config:
        arbitrary_types_allowed = True
        underscore_attrs_are_private = True

    @property
    def status_code(self):
        return self._status_code


class BaseValidationError(RequestValidationError):
    status: str
    status_type: str
    message: str
    errors: List[Any]

    class Config:
        arbitrary_types_allowed = True
        underscore_attrs_are_private = True
