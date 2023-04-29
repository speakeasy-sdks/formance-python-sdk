"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import configchangesecret as shared_configchangesecret
from ..shared import configresponse as shared_configresponse
from typing import Optional


@dataclasses.dataclass
class ChangeConfigSecretRequest:
    
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""Config ID"""
    config_change_secret: Optional[shared_configchangesecret.ConfigChangeSecret] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ChangeConfigSecretResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    config_response: Optional[shared_configresponse.ConfigResponse] = dataclasses.field(default=None)
    r"""Secret successfully changed."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    