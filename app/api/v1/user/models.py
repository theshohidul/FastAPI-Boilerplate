from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey, Table, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base, relationship

from core.db.base import Base


user_roles_table = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("role_id", ForeignKey("roles.id")),
    PrimaryKeyConstraint('user_id', 'role_id'),
)


class RoleModel(Base):
    def __init__(self):
        pass

    __tablename__ = "roles"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    role: str = Column(String(255), nullable=False)
    __mapper_args__ = {"eager_defaults": True}

    users = relationship(
        "UserModel", secondary=user_roles_table, back_populates="roles"
    )


class UserModel(Base):
    def __init__(self):
        pass

    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(255), nullable=False)
    email: str = Column(String(255), nullable=False, unique=True)
    password: str = Column(String(255), nullable=False)
    phone: str = Column(String(255), nullable=False)
    __mapper_args__ = {"eager_defaults": True}

    roles: List[RoleModel] = relationship(
        "RoleModel",
        secondary=user_roles_table,
        back_populates="users",
    )
