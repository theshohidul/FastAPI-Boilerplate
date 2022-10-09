from http import HTTPStatus
from enum import Enum


class ResponseStatus(Enum):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    USER_REGISTERED = (HTTPStatus.CREATED, 'User registered successfully')
    USER_LOGGED_IN = (HTTPStatus.OK, 'User logged in successfully')
    USER_NOT_FOUND = (HTTPStatus.NOT_FOUND, 'User not found')
    DUPLICATE_EMAIL = (HTTPStatus.CONFLICT, "User already exists")
