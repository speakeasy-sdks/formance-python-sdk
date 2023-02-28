from __future__ import annotations
import dataclasses
from ..shared import configinforesponse as shared_configinforesponse
from ..shared import errorresponse as shared_errorresponse
from typing import Optional


@dataclasses.dataclass
class GetInfoResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    config_info_response: Optional[shared_configinforesponse.ConfigInfoResponse] = dataclasses.field(default=None)
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    