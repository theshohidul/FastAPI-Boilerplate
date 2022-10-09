from fastapi import APIRouter

from api.v1.register.schemas.responses import UserRegisteredSuccessfully, DuplicateEmail
from api.v1.register.view import RegisterView
from api.v1.shared.schemas.responses import ValidationErrorResponse

register_view = RegisterView()

register_router = APIRouter(
    responses={
        209: {"description": "User Already Exists", "model": DuplicateEmail},
        422: {"description": "Validation Error", "model": ValidationErrorResponse},
    },
)

register_router.add_api_route(
    "",
    register_view.register,
    methods=["POST"],
    description="New user registration",
    name="New user registration",
    response_model=UserRegisteredSuccessfully,
    status_code=UserRegisteredSuccessfully().status_code,
)
