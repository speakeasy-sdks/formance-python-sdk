from __future__ import annotations
import dataclasses
from ..shared import connectorsresponse as shared_connectorsresponse
from typing import Optional


@dataclasses.dataclass
class ListAllConnectorsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connectors_response: Optional[shared_connectorsresponse.ConnectorsResponse] = dataclasses.field(default=None)
    