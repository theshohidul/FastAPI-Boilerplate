from typing import Sequence, Tuple, Union

from starlette.requests import HTTPConnection
from fastapi.security.utils import get_authorization_scheme_param
from starlette.authentication import (
    AuthenticationBackend,
    AuthenticationError,
    UnauthenticatedUser,
)

from api.v1.auth.schemas.errors import (
    CustomUnauthorizedError,
    CustomDecodeTokenError,
    CustomInvalidTokenError,
    CustomExpiredTokenError,
)
from api.v1.auth.schemas.exceptions import DecodeTokenException, ExpiredTokenException
from api.v1.auth.service import AuthService
from api.v1.user.schemas.responses import SystemUser


class AuthBackend(AuthenticationBackend):
    def __init__(
            self, prefix: str,
            exclude_paths: Sequence[str],
            auth_service: AuthService = AuthService()
    ):
        self.prefix = prefix
        self.exclude_paths = exclude_paths if exclude_paths else []
        self.auth_service = auth_service

    async def authenticate(
            self,
            conn: HTTPConnection,
    ) -> Tuple[bool, Union[SystemUser, UnauthenticatedUser]]:
        current_path = conn.url.path.removeprefix(self.prefix)


        for path in self.exclude_paths:
            if current_path.startswith(path):
                return False, UnauthenticatedUser()

        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            raise CustomUnauthorizedError

        scheme, token = get_authorization_scheme_param(authorization)
        if not (authorization and scheme and token):
            raise CustomUnauthorizedError
        if scheme.lower() != "bearer":
            raise CustomUnauthorizedError

        try:
            user = await self.auth_service.get_user_from_access_token(token)
            conn.scope["user"] = user
        except DecodeTokenException:
            raise CustomDecodeTokenError
        except ExpiredTokenException:
            raise CustomExpiredTokenError
        except Exception:
            raise CustomInvalidTokenError

        return True, user
