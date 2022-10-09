from fastapi import APIRouter
from fastapi import Depends, status

from .view import UserView
from ..shared.role_checker import CheckRole
from ..shared.schemas.responses import ValidationErrorResponse

user_views = UserView()

user_router = APIRouter(
    responses={
        404: {"description": "Not found"},
        422: {"description": "Validation Error", "model": ValidationErrorResponse},
    },
)

user_router.add_api_route(
    path="",
    endpoint=user_views.list,
    methods=["GET"],
    description="User",
    name="Get All Users",
    response_model_by_alias=False,
    dependencies=[Depends(CheckRole(['landlord']))],
)
