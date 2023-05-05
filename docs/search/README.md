# search

## Overview

Everything related to Search

### Available Operations

* [search](#search) - Search

## search

ElasticSearch query engine

### Example Usage

```python
import formance
from formance.models import shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)

req = shared.Query(
    after=[
        'users:002',
    ],
    cursor='YXVsdCBhbmQgYSBtYXhpbXVtIG1heF9yZXN1bHRzLol=',
    ledgers=[
        'quickstart',
        'quickstart',
        'quickstart',
    ],
    page_size=569618,
    policy='OR',
    sort='txid:asc',
    target='tempora',
    terms=[
        'destination=central_bank1',
        'destination=central_bank1',
        'destination=central_bank1',
    ],
)

res = s.search.search(req)

if res.response is not None:
    # handle response
```
