from __future__ import annotations
import dataclasses
from ..shared import createclientrequest as shared_createclientrequest
from ..shared import createclientresponse as shared_createclientresponse
from typing import Optional


@dataclasses.dataclass
class CreateClientRequest:
    request: Optional[shared_createclientrequest.CreateClientRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateClientResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_client_response: Optional[shared_createclientresponse.CreateClientResponse] = dataclasses.field(default=None)
    