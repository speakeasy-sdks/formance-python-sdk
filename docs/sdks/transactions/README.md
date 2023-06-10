# transactions

## Overview

Everything related to Transactions

### Available Operations

* [create_transactions](#create_transactions) - Create a new batch of transactions to a ledger
* [add_metadata_on_transaction](#add_metadata_on_transaction) - Set the metadata of a transaction by its ID
* [count_transactions](#count_transactions) - Count the transactions from a ledger
* [create_transaction](#create_transaction) - Create a new transaction to a ledger
* [get_transaction](#get_transaction) - Get transaction from a ledger by its ID
* [list_transactions](#list_transactions) - List transactions from a ledger
* [revert_transaction](#revert_transaction) - Revert a ledger transaction by its ID

## create_transactions

Create a new batch of transactions to a ledger

### Example Usage

```python
import formance
import dateutil.parser
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.CreateTransactionsRequest(
    transactions=shared.Transactions(
        transactions=[
            shared.TransactionData(
                metadata={
                    "quae": 'ipsum',
                    "quidem": 'molestias',
                    "excepturi": 'pariatur',
                    "modi": 'praesentium',
                },
                postings=[
                    shared.Posting(
                        amount=100,
                        asset='COIN',
                        destination='users:002',
                        source='users:001',
                    ),
                    shared.Posting(
                        amount=100,
                        asset='COIN',
                        destination='users:002',
                        source='users:001',
                    ),
                    shared.Posting(
                        amount=100,
                        asset='COIN',
                        destination='users:002',
                        source='users:001',
                    ),
                ],
                reference='ref:001',
                timestamp=dateutil.parser.isoparse('2022-09-20T03:14:35.704Z'),
            ),
            shared.TransactionData(
                metadata={
                    "sint": 'veritatis',
                    "itaque": 'incidunt',
                    "enim": 'consequatur',
                    "est": 'quibusdam',
                },
                postings=[
                    shared.Posting(
                        amount=100,
                        asset='COIN',
                        destination='users:002',
                        source='users:001',
                    ),
                ],
                reference='ref:001',
                timestamp=dateutil.parser.isoparse('2021-07-27T01:56:50.693Z'),
            ),
        ],
    ),
    ledger='ledger001',
)

res = s.transactions.create_transactions(req)

if res.transactions_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateTransactionsRequest](../../models/operations/createtransactionsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateTransactionsResponse](../../models/operations/createtransactionsresponse.md)**


## add_metadata_on_transaction

Set the metadata of a transaction by its ID

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.AddMetadataOnTransactionRequest(
    request_body={
        "labore": 'modi',
        "qui": 'aliquid',
        "cupiditate": 'quos',
        "perferendis": 'magni',
    },
    ledger='ledger001',
    txid=1234,
)

res = s.transactions.add_metadata_on_transaction(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.AddMetadataOnTransactionRequest](../../models/operations/addmetadataontransactionrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.AddMetadataOnTransactionResponse](../../models/operations/addmetadataontransactionresponse.md)**


## count_transactions

Count the transactions from a ledger

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

req = operations.CountTransactionsRequest(
    account='users:001',
    destination='users:001',
    end_time=dateutil.parser.isoparse('2021-11-22T01:26:35.048Z'),
    end_time_deprecated=dateutil.parser.isoparse('2022-11-08T13:10:11.700Z'),
    ledger='ledger001',
    metadata=operations.CountTransactionsMetadata(),
    reference='ref:001',
    source='users:001',
    start_time=dateutil.parser.isoparse('2021-11-11T04:17:07.569Z'),
    start_time_deprecated=dateutil.parser.isoparse('2022-04-19T03:15:40.816Z'),
)

res = s.transactions.count_transactions(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CountTransactionsRequest](../../models/operations/counttransactionsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CountTransactionsResponse](../../models/operations/counttransactionsresponse.md)**


## create_transaction

Create a new transaction to a ledger

### Example Usage

```python
import formance
import dateutil.parser
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.CreateTransactionRequest(
    post_transaction=shared.PostTransaction(
        metadata={
            "labore": 'delectus',
            "eum": 'non',
            "eligendi": 'sint',
        },
        postings=[
            shared.Posting(
                amount=100,
                asset='COIN',
                destination='users:002',
                source='users:001',
            ),
            shared.Posting(
                amount=100,
                asset='COIN',
                destination='users:002',
                source='users:001',
            ),
        ],
        reference='ref:001',
        script=shared.PostTransactionScript(
            plain='vars {
        account $user
        }
        send [COIN 10] (
        	source = @world
        	destination = $user
        )
        ',
            vars=shared.PostTransactionScriptVars(),
        ),
        timestamp=dateutil.parser.isoparse('2021-03-17T21:24:26.606Z'),
    ),
    ledger='ledger001',
    preview=True,
)

res = s.transactions.create_transaction(req)

if res.transactions_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateTransactionRequest](../../models/operations/createtransactionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateTransactionResponse](../../models/operations/createtransactionresponse.md)**


## get_transaction

Get transaction from a ledger by its ID

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.GetTransactionRequest(
    ledger='ledger001',
    txid=1234,
)

res = s.transactions.get_transaction(req)

if res.transaction_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetTransactionRequest](../../models/operations/gettransactionrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetTransactionResponse](../../models/operations/gettransactionresponse.md)**


## list_transactions

List transactions from a ledger, sorted by txid in descending order.

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

req = operations.ListTransactionsRequest(
    account='users:001',
    after='1234',
    cursor='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    destination='users:001',
    end_time=dateutil.parser.isoparse('2021-09-21T14:06:09.271Z'),
    end_time_deprecated=dateutil.parser.isoparse('2022-02-09T13:58:59.361Z'),
    ledger='ledger001',
    metadata=operations.ListTransactionsMetadata(),
    page_size=952749,
    page_size_deprecated=680056,
    pagination_token='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    reference='ref:001',
    source='users:001',
    start_time=dateutil.parser.isoparse('2022-07-21T01:01:39.776Z'),
    start_time_deprecated=dateutil.parser.isoparse('2020-01-25T11:09:22.009Z'),
)

res = s.transactions.list_transactions(req)

if res.transactions_cursor_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.ListTransactionsRequest](../../models/operations/listtransactionsrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ListTransactionsResponse](../../models/operations/listtransactionsresponse.md)**


## revert_transaction

Revert a ledger transaction by its ID

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="",
    ),
)

req = operations.RevertTransactionRequest(
    ledger='ledger001',
    txid=1234,
)

res = s.transactions.revert_transaction(req)

if res.transaction_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RevertTransactionRequest](../../models/operations/reverttransactionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.RevertTransactionResponse](../../models/operations/reverttransactionresponse.md)**

