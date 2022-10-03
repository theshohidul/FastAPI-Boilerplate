from api.v1.auth.service import AuthService
from .schemas.requests import LoginRequest, RefreshTokenRequest
from .schemas.responses import TokenData, TokenResponse
from core.utils import make_response_from_model


class AuthView:
    def __init__(self, auth_service: AuthService = AuthService()):
        self.auth_service = auth_service

    async def access(self, login_request: LoginRequest):
        token_data: TokenData = await self.auth_service.access(login_request)
        return make_response_from_model(
            TokenResponse(
                data=token_data
            )
        )

    async def refresh(self, refresh_token_request: RefreshTokenRequest):
        token_data: TokenData = await self.auth_service.refresh(refresh_token_request)
        return make_response_from_model(
            TokenResponse(
                data=token_data
            )
        )
