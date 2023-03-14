from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import mappingresponse as shared_mappingresponse
from typing import Optional


@dataclasses.dataclass
class GetMappingRequest:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetMappingResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    mapping_response: Optional[shared_mappingresponse.MappingResponse] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    