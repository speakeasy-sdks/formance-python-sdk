from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createsecretrequest as shared_createsecretrequest
from ..shared import createsecretresponse as shared_createsecretresponse
from typing import Optional


@dataclasses.dataclass
class CreateSecretRequest:
    client_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientId', 'style': 'simple', 'explode': False }})
    create_secret_request: Optional[shared_createsecretrequest.CreateSecretRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateSecretResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    create_secret_response: Optional[shared_createsecretresponse.CreateSecretResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    