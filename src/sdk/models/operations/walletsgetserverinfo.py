from __future__ import annotations
import dataclasses
from ..shared import serverinfo as shared_serverinfo
from ..shared import walletserrorresponse as shared_walletserrorresponse
from typing import Optional


@dataclasses.dataclass
class WalletsgetServerInfoResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    server_info: Optional[shared_serverinfo.ServerInfo] = dataclasses.field(default=None)
    wallets_error_response: Optional[shared_walletserrorresponse.WalletsErrorResponse] = dataclasses.field(default=None)
    