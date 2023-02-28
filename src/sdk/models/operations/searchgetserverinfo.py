from __future__ import annotations
import dataclasses
from ..shared import serverinfo as shared_serverinfo
from typing import Optional


@dataclasses.dataclass
class SearchgetServerInfoResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    server_info: Optional[shared_serverinfo.ServerInfo] = dataclasses.field(default=None)
    