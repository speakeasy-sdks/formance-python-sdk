from __future__ import annotations
import dataclasses
from ..shared import listclientsresponse as shared_listclientsresponse
from typing import Optional


@dataclasses.dataclass
class ListClientsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_clients_response: Optional[shared_listclientsresponse.ListClientsResponse] = dataclasses.field(default=None)
    