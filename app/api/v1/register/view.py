from api.v1.register.service import RegisterService
from core.utils import base_response_to_json_response
from .schemas.requests import RegisterRequest
from .schemas.responses import UserRegisteredSuccessfully


class RegisterView:
    def __init__(self, register_service: RegisterService = RegisterService()):
        self.register_service = register_service

    async def register(self, register_request: RegisterRequest):
        try:
            await self.register_service.register(register_request)
        except Exception as exc:
            print(exc)
            raise
        return base_response_to_json_response(UserRegisteredSuccessfully())
