import time

from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from core.logging.logger import logger
from core.logging.schemas import ExtraLogData

from core.utils import get_matching_route_path, get_path_params


class LoggingMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app: ASGIApp,
    ):
        super().__init__(app)

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        method = request.method
        path = get_matching_route_path(request)
        path_params: dict = get_path_params(request)
        try:
            _user = getattr(request, "user", None)
        except AssertionError:
            _user = None

        log_data = ExtraLogData(
            request_id=request.state.request_id,
            user=getattr(_user, "email", None),
            user_host=request.client.host,
            user_agent=request.headers.get("User-Agent", ""),
            path=path,
            method=method,
            path_params=path_params,
            query_params=request.query_params.__dict__["_dict"],
            payload=dict(),
        )
        request.state.log_data = log_data
        logger.info("Request Received", **log_data.dict())
        start_time = time.time()

        try:
            response: Response = await call_next(request)
            log_data.response_code = response.status_code
        except Exception as exc:
            log_data.response_code = 500
            print(exc)
            print(type(exc))
            raise
        finally:
            end_time = time.time()
            process_time = (end_time - start_time) * 1000
            log_data.response_time = '{0:.2f}'.format(process_time)
            logger.info("Response Sent", **log_data.dict())

        return response
