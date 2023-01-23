from functools import lru_cache
from typing import List

from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    ENV: str = "dev"
    PROJECT_NAME: str = "Boilerplate"
    PROJECT_TITLE: str = "FastAPI Boilerplate"
    PROJECT_DESCRIPTION: str = "FastAPI Boilerplate"
    PROJECT_VERSION: str = "1.0.0"

    ENCODING: str = 'utf-8'

    API_V1_PREFIX: str = "/api/v1"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_SECRET_KEY: str = "MySuperSecret"
    JWT_REFRESH_SECRET_KEY: str = "MySuperSecretRefresh"
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 1
    REFRESH_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 30
    BACKEND_CORS_ORIGINS: List[str] = ['*']

    AUTH_EXCLUDE_PATHS: List[str] = [
        "/docs",
        "/redoc",
        "/openapi",
        "/auth/token",
        "/auth/token/refresh",
        "/register",
    ]

    LOG_LEVEL: str = "DEBUG"
    LOG_FORMAT: str = (
        "time: {time:YYYY-MM-DD HH:mm:ss Z} | "
        "level: {level} | "
        "request_id: {extra[request_id]} | "
        "user: {extra[user]} | "
        "user_host: {extra[user_host]} | "
        "user_agent: {extra[user_agent]} | "
        "url: {extra[path]} | "
        "method: {extra[method]} | "
        "request_data: {extra[request_data]} | "
        "response_data: {extra[response_data]} | "
        "response_time: {extra[response_time]} | "
        "response_code: {extra[response_code]} | "
        "message: {message} | "
        "exception: {exception}"
    )

    DB_ECHO_LOG: bool = True
    DB_CONNECTION: str
    DB_HOST: str
    DB_PORT: str
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_URL: str = ''

    @validator("DB_URL", always=True)
    def prepare_db_url(cls, value, values):
        return '{0}+aiomysql://{1}:{2}@{3}:{4}/{5}'.format(
            values.get('DB_CONNECTION'),
            values.get('DB_USERNAME'),
            values.get('DB_PASSWORD'),
            values.get('DB_HOST'),
            values.get('DB_PORT'),
            values.get('DB_DATABASE')
        )

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()


@lru_cache()
def get_settings():
    return Settings()
