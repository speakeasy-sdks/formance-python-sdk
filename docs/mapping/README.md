# mapping

## Overview

Everything related to Mapping

### Available Operations

* [get_mapping](#get_mapping) - Get the mapping of a ledger
* [update_mapping](#update_mapping) - Update the mapping of a ledger

## get_mapping

Get the mapping of a ledger

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.GetMappingRequest(
    ledger="ledger001",
)

res = s.mapping.get_mapping(req)

if res.mapping_response is not None:
    # handle response
```

## update_mapping

Update the mapping of a ledger

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.UpdateMappingRequest(
    mapping=shared.Mapping(
        contracts=[
            shared.Contract(
                account="users:001",
                expr={
                    "nobis": "enim",
                },
            ),
            shared.Contract(
                account="users:001",
                expr={
                    "nemo": "minima",
                    "excepturi": "accusantium",
                    "iure": "culpa",
                },
            ),
        ],
    ),
    ledger="ledger001",
)

res = s.mapping.update_mapping(req)

if res.mapping_response is not None:
    # handle response
```
