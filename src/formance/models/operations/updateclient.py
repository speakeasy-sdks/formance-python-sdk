from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import updateclientrequest as shared_updateclientrequest
from ..shared import updateclientresponse as shared_updateclientresponse
from typing import Optional


@dataclasses.dataclass
class UpdateClientRequest:
    client_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientId', 'style': 'simple', 'explode': False }})
    update_client_request: Optional[shared_updateclientrequest.UpdateClientRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateClientResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    update_client_response: Optional[shared_updateclientresponse.UpdateClientResponse] = dataclasses.field(default=None)
    