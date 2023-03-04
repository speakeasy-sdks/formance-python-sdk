from __future__ import annotations
import dataclasses
import requests
from ..shared import serverinfo as shared_serverinfo
from typing import Optional


@dataclasses.dataclass
class GetServerInfoResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    server_info: Optional[shared_serverinfo.ServerInfo] = dataclasses.field(default=None)
    