from __future__ import annotations
import dataclasses
from ..shared import attemptresponse as shared_attemptresponse
from typing import Optional


@dataclasses.dataclass
class TestConfigPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TestConfigRequest:
    path_params: TestConfigPathParams = dataclasses.field()
    

@dataclasses.dataclass
class TestConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    attempt_response: Optional[shared_attemptresponse.AttemptResponse] = dataclasses.field(default=None)
    