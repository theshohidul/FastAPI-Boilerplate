from http import HTTPStatus
from enum import Enum


class ExceptionStatus(Enum):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    DUPLICATE_EMAIL = (HTTPStatus.CONFLICT, "User already exists")
    USER_NOT_FOUND = (HTTPStatus.NOT_FOUND, "User not found")
    PASSWORD_NOT_MATCHED = (HTTPStatus.BAD_REQUEST, "Password doesn't match")

    UNPROCESSABLE_TOKEN = (HTTPStatus.UNPROCESSABLE_ENTITY, "Couldn't decode the token")
    INVALID_TOKEN = (HTTPStatus.UNPROCESSABLE_ENTITY, "Token is invalid")
    TOKEN_EXPIRED = (HTTPStatus.UNAUTHORIZED, "Token expired")
    UNAUTHORIZED = (HTTPStatus.UNAUTHORIZED, "Unauthorized")