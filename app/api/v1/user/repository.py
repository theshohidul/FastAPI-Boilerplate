from typing import Optional

from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload, lazyload, contains_eager

from core.db.db import database
from .models import UserModel
from .schemas.requests import UserCreateSchema


class UserRepository:
    def __init__(self, db=database):
        self.db = db

    async def create_user(self, user: UserCreateSchema):
        query = insert(UserModel).values(**user.dict())
        await self.db.execute(query)
        return await self.db.commit()

    async def get_user_by_email(self, email: str):
        await self.db.rollback()
        query = select(UserModel).where(UserModel.email == email).options(joinedload(UserModel.roles))
        user = await self.db.execute(query)
        user = user.scalars().first()
        return user

    async def get_user_by_id(self, user_id: int):
        await self.db.rollback()
        query = select(UserModel).where(UserModel.id == user_id).options(joinedload(UserModel.roles))
        user = await self.db.execute(query)
        user: UserModel = user.scalars().first()
        return user

    async def get_user_list(
            self,
            limit: int = 12,
            prev: Optional[int] = None,
    ):
        query = select(UserModel)

        if prev:
            query = query.where(UserModel.id < prev)

        query = query.options(joinedload(UserModel.roles)).limit(limit)

        users = await self.db.execute(query)
        users = users.scalars().unique().all()
        return users
