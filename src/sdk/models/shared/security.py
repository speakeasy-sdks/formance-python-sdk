from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class SchemeAuthorization:
    authorization: str = dataclasses.field(metadata={'security': { 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class Security:
    authorization: SchemeAuthorization = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    