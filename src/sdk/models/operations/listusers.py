from __future__ import annotations
import dataclasses
from ..shared import listusersresponse as shared_listusersresponse
from typing import Optional


@dataclasses.dataclass
class ListUsersResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    list_users_response: Optional[shared_listusersresponse.ListUsersResponse] = dataclasses.field(default=None)
    