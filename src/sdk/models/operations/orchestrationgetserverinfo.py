from __future__ import annotations
import dataclasses
from ..shared import error as shared_error
from ..shared import serverinfo as shared_serverinfo
from typing import Optional


@dataclasses.dataclass
class OrchestrationgetServerInfoResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    server_info: Optional[shared_serverinfo.ServerInfo] = dataclasses.field(default=None)
    