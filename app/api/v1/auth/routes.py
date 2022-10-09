from fastapi import APIRouter

from api.v1.auth.schemas.responses import TokenResponse
from api.v1.auth.view import AuthView
from api.v1.register.schemas.responses import UserNotFound
from api.v1.shared.schemas.responses import ValidationErrorResponse

auth_views = AuthView()

auth_router = APIRouter(
    responses={
        404: {"description": "Not found", "model": UserNotFound},
        422: {"description": "Validation Error", "model": ValidationErrorResponse},
    },

)

auth_router.add_api_route(
    "/token",
    auth_views.access,
    methods=["POST"],
    description="User Authentication and create access token",
    name="Authentication-AccessToken",
    response_model_by_alias=False,
    response_model=TokenResponse,
)

auth_router.add_api_route(
    "/token/refresh",
    auth_views.refresh,
    methods=["POST"],
    description="Create access token from refresh token",
    name="Authentication-AccessToken-From-RefreshToken",
    response_model_by_alias=False,
    response_model=TokenResponse,
)
