from core.exceptions.base import CustomException
from core.enums.status_type import StatusType
from core.enums.exception_status import ExceptionStatus


class PasswordDoesNotMatchException(CustomException):
    status = StatusType.ERROR.value
    status_type = ExceptionStatus.PASSWORD_NOT_MATCHED.name
    message = ExceptionStatus.PASSWORD_NOT_MATCHED.message
    _status_code = ExceptionStatus.PASSWORD_NOT_MATCHED.status_code


class InvalidTokenException(CustomException):
    status = StatusType.ERROR.value
    status_type = ExceptionStatus.INVALID_TOKEN.name
    message = ExceptionStatus.INVALID_TOKEN.message
    _status_code = ExceptionStatus.INVALID_TOKEN.status_code


class DecodeTokenException(CustomException):
    status = StatusType.ERROR.value
    status_type = ExceptionStatus.UNPROCESSABLE_TOKEN.name
    message = ExceptionStatus.UNPROCESSABLE_TOKEN.message
    _status_code = ExceptionStatus.UNPROCESSABLE_TOKEN.status_code


class ExpiredTokenException(CustomException):
    status = StatusType.ERROR.value
    status_type = ExceptionStatus.TOKEN_EXPIRED.name
    message = ExceptionStatus.TOKEN_EXPIRED.message
    _status_code = ExceptionStatus.TOKEN_EXPIRED.status_code
