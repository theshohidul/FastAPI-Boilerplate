from core.enums.exception_status import ExceptionStatus
from core.enums.status_type import StatusType
from core.schemas.base import BaseAuthenticationError


class CustomUnauthorizedError(BaseAuthenticationError):
    status = StatusType.ERROR.value
    status_code = ExceptionStatus.UNAUTHORIZED.status_code
    status_type = ExceptionStatus.UNAUTHORIZED.name
    message = ExceptionStatus.UNAUTHORIZED.message


class CustomInvalidTokenError(BaseAuthenticationError):
    status = StatusType.ERROR.value
    status_code = ExceptionStatus.INVALID_TOKEN.status_code
    status_type = ExceptionStatus.INVALID_TOKEN.name
    message = ExceptionStatus.INVALID_TOKEN.message


class CustomDecodeTokenError(BaseAuthenticationError):
    status = StatusType.ERROR.value
    status_code = ExceptionStatus.UNPROCESSABLE_TOKEN.status_code
    status_type = ExceptionStatus.UNPROCESSABLE_TOKEN.name
    message = ExceptionStatus.UNPROCESSABLE_TOKEN.message


class CustomExpiredTokenError(BaseAuthenticationError):
    status = StatusType.ERROR.value
    status_code = ExceptionStatus.TOKEN_EXPIRED.status_code
    status_type = ExceptionStatus.TOKEN_EXPIRED.name
    message = ExceptionStatus.TOKEN_EXPIRED.message
