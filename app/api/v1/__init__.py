from fastapi import APIRouter
from core.configs import get_settings

from .register.routes import register_router as register_v1_router
from .auth.routes import auth_router as auth_v1_router
from .user.routes import user_router as user_v1_router

settings = get_settings()

router = APIRouter()
router.include_router(register_v1_router, prefix=settings.API_V1_PREFIX + "/register", tags=["Registration"])
router.include_router(auth_v1_router, prefix=settings.API_V1_PREFIX + "/auth", tags=["Authentication"])
router.include_router(user_v1_router, prefix=settings.API_V1_PREFIX + "/users", tags=["Users"])

__all__ = ["router"]