from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import configresponse as shared_configresponse
from typing import Optional


@dataclasses.dataclass
class InsertConfigResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    config_response: Optional[shared_configresponse.ConfigResponse] = dataclasses.field(default=None)
    insert_config_400_text_plain_string: Optional[str] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    