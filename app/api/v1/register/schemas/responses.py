from core.schemas.base import BaseResponse
from core.enums.response_status import ResponseStatus
from core.enums.status_type import StatusType


class UserRegisteredSuccessfully(BaseResponse):
    status: int = StatusType.SUCCESS.value
    status_code: str = ResponseStatus.USER_REGISTERED.status_code
    status_type: str = ResponseStatus.USER_REGISTERED.name
    message: str = ResponseStatus.USER_REGISTERED.message