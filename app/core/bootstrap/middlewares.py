from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.auth.auth_backend import AuthBackend
from core.configs import Settings, get_settings
from core.middlewares.logging import LoggingMiddleware
from core.middlewares.auth import AuthenticationMiddleware
from core.middlewares.request_id import RequestIdMiddleware


def init_middlewares(app_: FastAPI) -> None:
    settings: Settings = get_settings()

    app_.add_middleware(LoggingMiddleware)
    app_.add_middleware(AuthenticationMiddleware, backend=AuthBackend(
        prefix=f"{settings.API_V1_PREFIX}",
        exclude_paths=settings.AUTH_EXCLUDE_PATHS if settings.AUTH_EXCLUDE_PATHS else [],
    ))
    app_.add_middleware(RequestIdMiddleware)

    # CORSMiddleware
    app_.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )