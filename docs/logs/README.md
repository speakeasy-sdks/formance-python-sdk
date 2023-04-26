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
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.ListLogsRequest(
    after="1234",
    cursor="aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
    end_time=dateutil.parser.isoparse('2020-11-28T02:15:07.561Z'),
    end_time_deprecated=dateutil.parser.isoparse('2022-12-10T00:25:28.749Z'),
    ledger="ledger001",
    page_size=969810,
    page_size_deprecated=666767,
    pagination_token="aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
    start_time=dateutil.parser.isoparse('2021-08-29T10:25:27.700Z'),
    start_time_deprecated=dateutil.parser.isoparse('2022-10-16T05:02:54.746Z'),
)

res = s.logs.list_logs(req)

if res.logs_cursor_response is not None:
    # handle response
```
