from fastapi import FastAPI
from core.db.db import database


def init_listeners(app_: FastAPI) -> None:
    @app_.on_event("startup")
    async def startup():
        await database.init()
        print("Database connected")

    @app_.on_event("shutdown")
    async def shutdown():
        await database.close()
        print("Database disconnected")