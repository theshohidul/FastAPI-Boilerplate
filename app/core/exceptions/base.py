from http import HTTPStatus

from core.enums.status_type import StatusType


class CustomException(Exception):
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


class BadRequestException(CustomException):
    status = StatusType.ERROR.value
    status_type = HTTPStatus.BAD_REQUEST.name
    message = HTTPStatus.BAD_REQUEST.phrase
    _status_code = HTTPStatus.BAD_REQUEST.value


class NotFoundException(CustomException):
    status = StatusType.ERROR.value
    status_type = HTTPStatus.NOT_FOUND.name
    message = HTTPStatus.NOT_FOUND.phrase
    _status_code = HTTPStatus.NOT_FOUND.value


class ForbiddenException(CustomException):
    status = StatusType.ERROR.value
    status_type = HTTPStatus.FORBIDDEN.name
    message = HTTPStatus.FORBIDDEN.phrase
    _status_code = HTTPStatus.FORBIDDEN.value


class UnauthorizedException(CustomException):
    status = StatusType.ERROR.value
    status_type = HTTPStatus.UNAUTHORIZED.name
    message = HTTPStatus.UNAUTHORIZED.phrase
    _status_code = HTTPStatus.UNAUTHORIZED.value


class UnprocessableEntity(CustomException):
    status = StatusType.ERROR.value
    status_type = HTTPStatus.UNPROCESSABLE_ENTITY.name
    message = HTTPStatus.UNPROCESSABLE_ENTITY.phrase
    _status_code = HTTPStatus.UNPROCESSABLE_ENTITY.value


class DuplicateValueException(CustomException):
    status = StatusType.ERROR.value
    status_type = HTTPStatus.UNPROCESSABLE_ENTITY.name
    message = HTTPStatus.UNPROCESSABLE_ENTITY.phrase
    _status_code = HTTPStatus.UNPROCESSABLE_ENTITY.value
