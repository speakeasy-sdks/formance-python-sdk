from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import script as shared_script
from ..shared import scriptresponse as shared_scriptresponse
from typing import Optional


@dataclasses.dataclass
class RunScriptPathParams:
    ledger: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ledger', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RunScriptQueryParams:
    preview: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'preview', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class RunScriptRequest:
    path_params: RunScriptPathParams = dataclasses.field()
    query_params: RunScriptQueryParams = dataclasses.field()
    request: shared_script.Script = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class RunScriptResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    script_response: Optional[shared_scriptresponse.ScriptResponse] = dataclasses.field(default=None)
    