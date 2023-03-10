from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import readuserresponse as shared_readuserresponse
from typing import Optional


@dataclasses.dataclass
class ReadUserPathParams:
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'userId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ReadUserRequest:
    path_params: ReadUserPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ReadUserResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    read_user_response: Optional[shared_readuserresponse.ReadUserResponse] = dataclasses.field(default=None)
    