from core.configs import get_settings
from core.utils import hash_password
from api.v1.user.repository import UserRepository
from api.v1.user.schemas.exceptions import DuplicateEmailException
from api.v1.user.schemas.requests import UserCreateSchema
from api.v1.user.models import UserModel
from .schemas.requests import RegisterRequest


class RegisterService:
    def __init__(self, user_repository: UserRepository = UserRepository()):
        self.user_repository = user_repository
        self.settings = get_settings()

    async def register(self, register_request: RegisterRequest):
        user: UserModel = await self.user_repository.get_user_by_email(register_request.email)
        if user:
            raise DuplicateEmailException

        register_request.password = hash_password(register_request.password)
        return await self.user_repository.create_user(UserCreateSchema(
            **register_request.dict(),
        ))
