"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createclientresponse as shared_createclientresponse
from typing import Optional


@dataclasses.dataclass
class CreateClientResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    create_client_response: Optional[shared_createclientresponse.CreateClientResponse] = dataclasses.field(default=None)

    r"""Client created"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    