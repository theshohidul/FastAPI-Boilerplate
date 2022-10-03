from fastapi import APIRouter
from fastapi import Depends, status

from .view import UserView
from ..shared.role_checker import CheckRole

user_views = UserView()

user_router = APIRouter(
    responses={404: {"description": "Not found"}},
)

user_router.add_api_route(
    path="",
    endpoint=user_views.list,
    methods=["GET"],
    description="User",
    name="Get All Users",
    response_model_by_alias=False,
    dependencies=[Depends(CheckRole(['Admin']))],
)
