from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class Security:
    authorization: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2', 'field_name': 'Authorization' }})
    