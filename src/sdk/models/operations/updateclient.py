from __future__ import annotations
import dataclasses
from ..shared import updateclientrequest as shared_updateclientrequest
from ..shared import updateclientresponse as shared_updateclientresponse
from typing import Optional


@dataclasses.dataclass
class UpdateClientPathParams:
    client_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateClientRequest:
    path_params: UpdateClientPathParams = dataclasses.field()
    request: Optional[shared_updateclientrequest.UpdateClientRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateClientResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    update_client_response: Optional[shared_updateclientresponse.UpdateClientResponse] = dataclasses.field(default=None)
    