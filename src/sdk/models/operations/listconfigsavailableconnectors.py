from __future__ import annotations
import dataclasses
from ..shared import connectorsconfigsresponse as shared_connectorsconfigsresponse
from typing import Optional


@dataclasses.dataclass
class ListConfigsAvailableConnectorsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connectors_configs_response: Optional[shared_connectorsconfigsresponse.ConnectorsConfigsResponse] = dataclasses.field(default=None)
    