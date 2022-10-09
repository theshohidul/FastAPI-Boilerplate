from api.v1.auth.service import AuthService
from core.utils import base_response_to_json_response
from .schemas.requests import LoginRequest, RefreshTokenRequest
from .schemas.responses import TokenData, TokenResponse


class AuthView:
    def __init__(self, auth_service: AuthService = AuthService()):
        self.auth_service = auth_service

    async def access(self, login_request: LoginRequest):
        token_data: TokenData = await self.auth_service.access(login_request)
        return base_response_to_json_response(TokenResponse(
                data=token_data
            ))

    async def refresh(self, refresh_token_request: RefreshTokenRequest):
        token_data: TokenData = await self.auth_service.refresh(refresh_token_request)
        return base_response_to_json_response(TokenResponse(
                data=token_data
            ))

