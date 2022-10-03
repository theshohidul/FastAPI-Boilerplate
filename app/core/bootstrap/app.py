from fastapi import FastAPI

from core.configs import Settings, get_settings

from .middlewares import init_middlewares
from .routers import init_routers
from .listeners import init_listeners
from .handlers import init_handlers


def create_app() -> FastAPI:
    settings: Settings = get_settings()

    app_ = FastAPI(
        title=settings.PROJECT_TITLE,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        docs_url=None if settings.ENV == "prod" else "/docs",
        redoc_url=None if settings.ENV == "prod" else "/redoc",
    )

    # Initializing required dependencies
    init_listeners(app_=app_)
    init_handlers(app_=app_)
    init_middlewares(app_=app_)
    init_routers(app_=app_)

    return app_
