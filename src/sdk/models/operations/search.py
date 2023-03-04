from __future__ import annotations
import dataclasses
import requests
from ..shared import query as shared_query
from ..shared import response as shared_response
from typing import Optional


@dataclasses.dataclass
class SearchRequest:
    request: shared_query.Query = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class SearchResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests.Response] = dataclasses.field(default=None)
    response: Optional[shared_response.Response] = dataclasses.field(default=None)
    