# ledger

## Overview

Everything related to Ledger

### Available Operations

* [get_ledger_info](#get_ledger_info) - Get information about a ledger

## get_ledger_info

Get information about a ledger

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.GetLedgerInfoRequest(
    ledger='ledger001',
)

res = s.ledger.get_ledger_info(req)

if res.ledger_info_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetLedgerInfoRequest](../../models/operations/getledgerinforequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetLedgerInfoResponse](../../models/operations/getledgerinforesponse.md)**
