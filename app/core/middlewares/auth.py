from fastapi.responses import JSONResponse
from starlette.middleware.authentication import (
    AuthenticationMiddleware as BaseAuthenticationMiddleware,
)
from starlette.requests import HTTPConnection

from core.schemas.base import BaseAuthenticationError


class AuthenticationMiddleware(BaseAuthenticationMiddleware):

    @staticmethod
    def default_on_error(conn: HTTPConnection, exc: BaseAuthenticationError) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content={
                'status': exc.status,
                'status_type': exc.status_type,
                'message': exc.message
            }
        )
