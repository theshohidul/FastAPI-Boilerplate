from typing import Optional

from .repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository = UserRepository()):
        self.user_repository = user_repository

    async def get_user_list(
            self,
            limit: int = 12,
            prev: Optional[int] = None,
    ):
        return await self.user_repository.get_user_list(limit, prev)

    async def get_user_by_email(self, email: str):
        return await self.user_repository.get_user_by_email(email)
