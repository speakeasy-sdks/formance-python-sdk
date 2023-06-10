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
        authorization="",
    ),
)

req = operations.GetMappingRequest(
    ledger='ledger001',
)

res = s.mapping.get_mapping(req)

if res.mapping_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetMappingRequest](../../models/operations/getmappingrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetMappingResponse](../../models/operations/getmappingresponse.md)**


## update_mapping

Update the mapping of a ledger

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.UpdateMappingRequest(
    mapping=shared.Mapping(
        contracts=[
            shared.Contract(
                account='users:001',
                expr=shared.ContractExpr(),
            ),
            shared.Contract(
                account='users:001',
                expr=shared.ContractExpr(),
            ),
        ],
    ),
    ledger='ledger001',
)

res = s.mapping.update_mapping(req)

if res.mapping_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateMappingRequest](../../models/operations/updatemappingrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateMappingResponse](../../models/operations/updatemappingresponse.md)**
