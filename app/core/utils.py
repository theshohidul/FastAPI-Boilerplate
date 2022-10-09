import bcrypt
from fastapi.responses import JSONResponse
from starlette.requests import Request
from starlette.routing import Match

from core.configs import get_settings
from core.schemas.base import BaseResponse


def get_matching_route_path(request: Request) -> str:
    for route in request.app.routes:
        match, child_scope = route.matches(request.scope)
        if match == Match.FULL:
            return route.path
    return request.url.path


def get_path_params(request: Request) -> dict:
    for route in request.app.routes:
        match, child_scope = route.matches(request.scope)
        if match == Match.FULL:
            return child_scope["path_params"]
    return {}


def remove_empty_from_dict(d):
    if type(d) is dict:
        return dict((k, remove_empty_from_dict(v)) for k, v in d.items() if v and remove_empty_from_dict(v))
    elif type(d) is list:
        return [remove_empty_from_dict(v) for v in d if v and remove_empty_from_dict(v)]
    else:
        return d


def verify_password(password, hashed_password) -> bool:
    settings = get_settings()
    return bcrypt.checkpw(
        password.encode(settings.ENCODING),
        hashed_password.encode(settings.ENCODING)
    )


def hash_password(password):
    settings = get_settings()
    return bcrypt.hashpw(
        password=password.encode(settings.ENCODING),
        salt=bcrypt.gensalt()
    )


def base_response_to_json_response(model: BaseResponse):
    try:
        status_code = model.status_code
        content = model.dict()

        return JSONResponse(
            status_code=status_code,
            content=remove_empty_from_dict(content)
        )
    except AttributeError:
        return model
