from __future__ import annotations
import dataclasses
from ..shared import errorresponse as shared_errorresponse
from ..shared import mapping as shared_mapping
from ..shared import mappingresponse as shared_mappingresponse
from typing import Optional


@dataclasses.dataclass
class UpdateMappingPathParams:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpdateMappingRequest:
    path_params: UpdateMappingPathParams = dataclasses.field()
    request: shared_mapping.Mapping = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateMappingResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    mapping_response: Optional[shared_mappingresponse.MappingResponse] = dataclasses.field(default=None)
    