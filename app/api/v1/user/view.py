from typing import List

from fastapi import Depends, status
from fastapi.requests import Request
from fastapi.responses import StreamingResponse

from .service import UserService


class UserView:
    def __init__(self, user_service: UserService = UserService()):
        self.user_service = user_service
    
    async def list(self):
        return await self.user_service.get_user_list()
