"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import createscoperesponse as shared_createscoperesponse
from typing import Optional


@dataclasses.dataclass
class CreateScopeResponse:
    
    content_type: str = dataclasses.field()

    status_code: int = dataclasses.field()

    create_scope_response: Optional[shared_createscoperesponse.CreateScopeResponse] = dataclasses.field(default=None)

    r"""Created scope"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)

    