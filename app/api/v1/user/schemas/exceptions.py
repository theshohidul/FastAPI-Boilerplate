from core.exceptions.base import CustomException
from core.enums.exception_status import ExceptionStatus
from core.enums.status_type import StatusType


class DuplicateEmailException(CustomException):
    status = StatusType.ERROR.value
    status_type = ExceptionStatus.DUPLICATE_EMAIL.name
    message = ExceptionStatus.DUPLICATE_EMAIL.message
    _status_code = ExceptionStatus.DUPLICATE_EMAIL.status_code


class UserNotFoundException(CustomException):
    status = StatusType.ERROR.value
    status_type = ExceptionStatus.USER_NOT_FOUND.name
    message = ExceptionStatus.USER_NOT_FOUND.message
    _status_code = ExceptionStatus.USER_NOT_FOUND.status_code
