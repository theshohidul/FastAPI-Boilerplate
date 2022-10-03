from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from core.configs import settings
from sqlalchemy import inspect

from .base import Base


def use_inspector(conn):
    inspector = inspect(conn)
    return inspector.get_table_names()


class AsyncDatabaseSession:
    def __init__(self):
        self._session = None
        self._engine = None

    def __getattr__(self, name):
        return getattr(self._session, name)

    async def init(self):
        self._engine = create_async_engine(
            settings.DB_URL,
            future=True,
            echo=settings.DB_ECHO_LOG,
            pool_pre_ping=True,
            pool_size=20,
            max_overflow=10,
            echo_pool='debug',
            pool_recycle=499,
            isolation_level="READ UNCOMMITTED"
        )
        self._session = sessionmaker(
            bind=self._engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )()

    async def create_all(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            tables = await conn.run_sync(use_inspector)
            print(tables)

    async def disconnect(self) -> None:
        if self._engine:
            await self._engine.dispose()


database = AsyncDatabaseSession()
