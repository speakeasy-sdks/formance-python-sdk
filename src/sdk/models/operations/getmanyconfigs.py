from __future__ import annotations
import dataclasses
from ..shared import configsresponse as shared_configsresponse
from typing import Optional


@dataclasses.dataclass
class GetManyConfigsQueryParams:
    endpoint: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'endpoint', 'style': 'form', 'explode': True }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'id', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GetManyConfigsRequest:
    query_params: GetManyConfigsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetManyConfigsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    configs_response: Optional[shared_configsresponse.ConfigsResponse] = dataclasses.field(default=None)
    