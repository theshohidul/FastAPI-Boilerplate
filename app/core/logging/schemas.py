from typing import Any, Optional
from pydantic import BaseModel, Field, validator


class ExtraLogData(BaseModel):
    request_id: Optional[str]
    channel_request_id: Optional[str]
    user: Optional[str]
    user_host: Optional[str]
    user_agent: Optional[str]
    path: Optional[str]
    method: Optional[str]
    path_params: Optional[dict]
    query_params: Optional[dict]
    payload: Optional[dict]
    request_data: Optional[str]
    response_data: Optional[str]
    response_code: Optional[int]
    response_time: Optional[float]

    @validator("request_data", always=True)
    def prepare_request_data(cls, v, values):
        res = {}
        if "path_params" in values and values["path_params"]:
            res["path_params"] = values["path_params"]
        if "query_params" in values and values["query_params"]:
            res["query_params"] = values["query_params"]
        if "payload" in values and values["payload"]:
            res["payload"] = values["payload"]
        return res or None

    class Config:
        validate_assignment = True
        use_enum_values = True
        arbitrary_types_allowed = True
