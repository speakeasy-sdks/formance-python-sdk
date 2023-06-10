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
        authorization="",
    ),
)

req = shared.Query(
    after=[
        'users:002',
        'users:002',
    ],
    cursor='YXVsdCBhbmQgYSBtYXhpbXVtIG1heF9yZXN1bHRzLol=',
    ledgers=[
        'quickstart',
    ],
    page_size=688661,
    policy='OR',
    sort='txid:asc',
    target='enim',
    terms=[
        'destination=central_bank1',
        'destination=central_bank1',
        'destination=central_bank1',
        'destination=central_bank1',
    ],
)

res = s.search.search(req)

if res.response is not None:
    # handle response
```

### Parameters

| Parameter                                    | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `request`                                    | [shared.Query](../../models/shared/query.md) | :heavy_check_mark:                           | The request object to use for the request.   |


### Response

**[operations.SearchResponse](../../models/operations/searchresponse.md)**

