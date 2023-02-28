from __future__ import annotations
import dataclasses
from ..shared import createsecretrequest as shared_createsecretrequest
from ..shared import createsecretresponse as shared_createsecretresponse
from typing import Optional


@dataclasses.dataclass
class CreateSecretPathParams:
    client_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CreateSecretRequest:
    path_params: CreateSecretPathParams = dataclasses.field()
    request: Optional[shared_createsecretrequest.CreateSecretRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateSecretResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_secret_response: Optional[shared_createsecretresponse.CreateSecretResponse] = dataclasses.field(default=None)
    