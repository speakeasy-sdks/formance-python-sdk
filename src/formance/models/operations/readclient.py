from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import readclientresponse as shared_readclientresponse
from typing import Optional


@dataclasses.dataclass
class ReadClientPathParams:
    client_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ReadClientRequest:
    path_params: ReadClientPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ReadClientResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    read_client_response: Optional[shared_readclientresponse.ReadClientResponse] = dataclasses.field(default=None)
    