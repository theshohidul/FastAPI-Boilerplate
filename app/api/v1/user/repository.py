from typing import Optional

from sqlalchemy import select, insert
from sqlalchemy.orm import joinedload, lazyload, contains_eager

from core.db.db import database
from .models import UserModel, RoleModel, user_roles_table
from .schemas.requests import UserCreateSchema


class UserRepository:
    def __init__(self, db=database):
        self.db = db

    async def create_user(self, user: UserCreateSchema):
        await self.db.rollback()

        user_dict = user.dict()
        role_name = user.role
        del user_dict["role"]

        query = insert(UserModel).values(**user_dict)
        user = await self.db.execute(query)

        query = select(RoleModel).where(RoleModel.role == role_name)
        role = await self.db.execute(query)
        role = role.scalars().first()
        if role:
            query = insert(user_roles_table).values({'role_id': role.id, 'user_id': user.inserted_primary_key[0]})
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
