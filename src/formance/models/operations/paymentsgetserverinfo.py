from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import serverinfo as shared_serverinfo
from typing import Optional


@dataclasses.dataclass
class PaymentsgetServerInfoResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    server_info: Optional[shared_serverinfo.ServerInfo] = dataclasses.field(default=None)
    