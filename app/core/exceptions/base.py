from http import HTTPStatus
from core.enums.status_type import StatusType


class CustomException(Exception):
    status: str
    status_code: int
    status_type: str
    message: str


class BadRequestException(CustomException):
    status = StatusType.ERROR.value
    status_code = HTTPStatus.BAD_REQUEST.value
    status_type = HTTPStatus.BAD_REQUEST.name
    message = HTTPStatus.BAD_REQUEST.phrase


class NotFoundException(CustomException):
    status = StatusType.ERROR.value
    status_code = HTTPStatus.BAD_REQUEST.value
    status_type = HTTPStatus.NOT_FOUND.name
    message = HTTPStatus.NOT_FOUND.phrase


class ForbiddenException(CustomException):
    status = StatusType.ERROR.value
    status_code = HTTPStatus.BAD_REQUEST.value
    status_type = HTTPStatus.FORBIDDEN.name
    message = HTTPStatus.FORBIDDEN.phrase


class UnauthorizedException(CustomException):
    status = StatusType.ERROR.value
    status_code = HTTPStatus.BAD_REQUEST.value
    status_type = HTTPStatus.UNAUTHORIZED.name
    message = HTTPStatus.UNAUTHORIZED.phrase


class UnprocessableEntity(CustomException):
    status = StatusType.ERROR.value
    status_code = HTTPStatus.UNPROCESSABLE_ENTITY.value
    status_type = HTTPStatus.UNPROCESSABLE_ENTITY.name
    message = HTTPStatus.UNPROCESSABLE_ENTITY.phrase


class DuplicateValueException(CustomException):
    status = StatusType.ERROR.value
    status_code = HTTPStatus.BAD_REQUEST.value
    status_type = HTTPStatus.UNPROCESSABLE_ENTITY.name
    message = HTTPStatus.UNPROCESSABLE_ENTITY.phrase
