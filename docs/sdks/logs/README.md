# logs

## Overview

Everything related to Logs

### Available Operations

* [list_logs](#list_logs) - List the logs from a ledger

## list_logs

List the logs from a ledger, sorted by ID in descending order.

### Example Usage

```python
import formance
import dateutil.parser
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.ListLogsRequest(
    after='1234',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    end_time=dateutil.parser.isoparse('2022-09-13T17:41:46.141Z'),
    end_time_deprecated=dateutil.parser.isoparse('2022-07-22T16:55:44.795Z'),
    ledger='ledger001',
    page_size=616934,
    page_size_deprecated=386489,
    pagination_token='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    start_time=dateutil.parser.isoparse('2020-04-17T15:42:43.722Z'),
    start_time_deprecated=dateutil.parser.isoparse('2022-02-06T12:52:33.708Z'),
)

res = s.logs.list_logs(req)

if res.logs_cursor_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.ListLogsRequest](../../models/operations/listlogsrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.ListLogsResponse](../../models/operations/listlogsresponse.md)**

