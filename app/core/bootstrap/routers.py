from fastapi import FastAPI
from api.v1 import router as api_v1_router


def init_routers(app_: FastAPI) -> None:
    app_.include_router(api_v1_router)
