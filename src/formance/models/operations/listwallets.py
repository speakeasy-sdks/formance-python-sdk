"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import listwalletsresponse as shared_listwalletsresponse
from typing import Optional



@dataclasses.dataclass
class ListWalletsMetadata:
    r"""Filter wallets by metadata key value pairs. Nested objects can be used as seen in the example below."""
    pass



@dataclasses.dataclass
class ListWalletsRequest:
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Parameter used in pagination requests.
    Set to the value of next for the next page of results.
    Set to the value of previous for the previous page of results.
    No other parameters can be set when the pagination token is set.
    """
    metadata: Optional[ListWalletsMetadata] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    r"""Filter wallets by metadata key value pairs. Nested objects can be used as seen in the example below."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'name', 'style': 'form', 'explode': True }})
    r"""Filter on wallet name"""
    page_size: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'pageSize', 'style': 'form', 'explode': True }})
    r"""The maximum number of results to return per page"""
    




@dataclasses.dataclass
class ListWalletsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_wallets_response: Optional[shared_listwalletsresponse.ListWalletsResponse] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

