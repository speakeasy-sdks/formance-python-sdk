from __future__ import annotations
import dataclasses
import requests
from typing import Optional


@dataclasses.dataclass
class DeleteSecretPathParams:
    client_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'clientId', 'style': 'simple', 'explode': False }})
    secret_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'secretId', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteSecretRequest:
    path_params: DeleteSecretPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteSecretResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    