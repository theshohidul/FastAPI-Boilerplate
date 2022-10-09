from core.schemas.base import BaseResponse
from core.enums.response_status import ResponseStatus
from core.enums.status_type import StatusType


class UserRegisteredSuccessfully(BaseResponse):
    status: str = StatusType.SUCCESS.value
    status_type: str = ResponseStatus.USER_REGISTERED.name
    message: str = ResponseStatus.USER_REGISTERED.message
    _status_code: int = ResponseStatus.USER_REGISTERED.status_code


class UserNotFound(BaseResponse):
    status: str = StatusType.ERROR.value
    status_type: str = ResponseStatus.USER_NOT_FOUND.name
    message: str = ResponseStatus.USER_NOT_FOUND.message
    _status_code: int = ResponseStatus.USER_NOT_FOUND.status_code


class DuplicateEmail(BaseResponse):
    status = StatusType.ERROR.value
    status_type = ResponseStatus.DUPLICATE_EMAIL.name
    message = ResponseStatus.DUPLICATE_EMAIL.message
    _status_code = ResponseStatus.DUPLICATE_EMAIL.status_code
