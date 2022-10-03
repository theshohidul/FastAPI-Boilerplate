from fastapi import APIRouter

from api.v1.register.schemas.responses import UserRegisteredSuccessfully
from api.v1.register.view import RegisterView

register_view = RegisterView()

register_router = APIRouter(
    responses={
        404: {"description": "Not found"},
    },
)

register_router.add_api_route(
    "",
    register_view.register,
    methods=["POST"],
    description="User Register",
    name="Registration",
    response_model=UserRegisteredSuccessfully,
)
