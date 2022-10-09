import jwt
from datetime import datetime, timedelta

from core.configs import get_settings
from core.utils import verify_password

from .schemas.requests import LoginRequest, RefreshTokenRequest
from .schemas.exceptions import (
    PasswordDoesNotMatchException,
    DecodeTokenException,
    ExpiredTokenException,
    InvalidTokenException
)
from .schemas.responses import TokenData, TokenPayload

from api.v1.user.repository import UserRepository
from api.v1.user.schemas.exceptions import UserNotFoundException
from api.v1.user.models import UserModel


class AuthService:
    def __init__(self, user_repository: UserRepository = UserRepository()):
        self.user_repository = user_repository
        self.settings = get_settings()

    async def access(self, login_request: LoginRequest):
        user: UserModel = await self.user_repository.get_user_by_email(login_request.email)
        if not user:
            raise UserNotFoundException

        if not verify_password(login_request.password, user.password):
            raise PasswordDoesNotMatchException

        return await self.create_token_data_from_user(user)

    async def refresh(self, refresh_token_request: RefreshTokenRequest) -> TokenData:
        user: UserModel = await self.get_user_from_refresh_token(refresh_token_request.refresh_token)
        return await self.create_token_data_from_user(user)

    async def create_access_token(self, payload: TokenPayload):
        return jwt.encode(
            payload={
                **payload.dict(),
                "exp": datetime.utcnow() + timedelta(seconds=self.settings.ACCESS_TOKEN_EXPIRE_SECONDS),
            },
            key=self.settings.JWT_ACCESS_SECRET_KEY,
            algorithm=self.settings.JWT_ALGORITHM,
        )

    async def create_refresh_token(self, payload: TokenPayload):
        return jwt.encode(
            payload={
                **payload.dict(),
                "exp": datetime.utcnow() + timedelta(seconds=self.settings.REFRESH_TOKEN_EXPIRE_SECONDS),
            },
            key=self.settings.JWT_REFRESH_SECRET_KEY,
            algorithm=self.settings.JWT_ALGORITHM,
        )

    async def create_token_data_from_user(self, user: UserModel) -> TokenData:
        payload = TokenPayload(
            sub=user.id,
            name=user.name
        )

        return TokenData(
            access_token=await self.create_access_token(payload=payload),
            refresh_token=await self.create_refresh_token(payload=payload),
            access_expires=datetime.timestamp(
                datetime.now() + timedelta(seconds=self.settings.ACCESS_TOKEN_EXPIRE_SECONDS)),
            refresh_expires=datetime.timestamp(
                datetime.now() + timedelta(seconds=self.settings.REFRESH_TOKEN_EXPIRE_SECONDS)),
        )

    async def get_user_from_access_token(self, token) -> UserModel:
        decoded_token = await self.decode_access_token(token=token)
        user = await self.user_repository.get_user_by_id(decoded_token['sub'])
        if not user:
            raise InvalidTokenException

        return user

    async def get_user_from_refresh_token(self, token) -> UserModel:
        decoded_token = await self.decode_refresh_token(token=token)
        user = await self.user_repository.get_user_by_id(decoded_token['sub'])
        if not user:
            raise InvalidTokenException

        return user

    async def decode_access_token(self, token) -> dict:
        try:
            return jwt.decode(
                token,
                key=self.settings.JWT_ACCESS_SECRET_KEY,
                algorithms=[self.settings.JWT_ALGORITHM],
            )
        except jwt.exceptions.DecodeError:
            raise DecodeTokenException
        except jwt.exceptions.ExpiredSignatureError:
            raise ExpiredTokenException

    async def decode_refresh_token(self, token) -> dict:
        try:
            return jwt.decode(
                token,
                key=self.settings.JWT_REFRESH_SECRET_KEY,
                algorithms=[self.settings.JWT_ALGORITHM],
            )
        except jwt.exceptions.DecodeError:
            raise DecodeTokenException
        except jwt.exceptions.ExpiredSignatureError:
            raise ExpiredTokenException


