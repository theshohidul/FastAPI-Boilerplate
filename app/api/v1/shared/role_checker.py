from typing import List

from starlette.requests import Request
from api.v1.user.models import RoleModel
from core.exceptions.base import ForbiddenException, UnauthorizedException


class CheckRole:
    def __init__(self, allowed_roles: List[str] = None, match_any: bool = True):
        if allowed_roles is None:
            allowed_roles = []
        self.allowed_roles = allowed_roles
        self.match_any = match_any

    async def __call__(self, request: Request):
        user = request.user
        if not user:
            raise UnauthorizedException

        if self.allowed_roles is None:
            raise ForbiddenException

        roles: List[RoleModel] = user.roles
        if not roles:
            raise ForbiddenException

        role_names = [role.role for role in roles]
        print(role_names)

        if self.match_any:
            if len(list(set(role_names) & set(self.allowed_roles))) > 0:
                return True
        else:
            if set(role_names) >= set(self.allowed_roles):
                return True

        raise ForbiddenException
