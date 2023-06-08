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
                    "delectus": 'eum',
                    "non": 'eligendi',
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
                timestamp=dateutil.parser.isoparse('2022-05-29T21:42:45.399Z'),
            ),
            shared.TransactionData(
                metadata={
                    "sint": 'officia',
                    "dolor": 'debitis',
                    "a": 'dolorum',
                    "in": 'in',
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
                    shared.Posting(
                        amount=100,
                        asset='COIN',
                        destination='users:002',
                        source='users:001',
                    ),
                ],
                reference='ref:001',
                timestamp=dateutil.parser.isoparse('2020-11-26T01:41:04.216Z'),
            ),
            shared.TransactionData(
                metadata={
                    "magnam": 'cumque',
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
                    shared.Posting(
                        amount=100,
                        asset='COIN',
                        destination='users:002',
                        source='users:001',
                    ),
                ],
                reference='ref:001',
                timestamp=dateutil.parser.isoparse('2022-08-09T06:36:34.417Z'),
            ),
        ],
    ),
    ledger='ledger001',
)

res = s.transactions.create_transactions(req)

if res.transactions_response is not None:
    # handle response
```

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
        "accusamus": 'non',
        "occaecati": 'enim',
        "accusamus": 'delectus',
    },
    ledger='ledger001',
    txid=1234,
)

res = s.transactions.add_metadata_on_transaction(req)

if res.status_code == 200:
    # handle response
```

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
    end_time=dateutil.parser.isoparse('2021-10-28T10:05:29.849Z'),
    end_time_deprecated=dateutil.parser.isoparse('2021-09-06T10:36:33.442Z'),
    ledger='ledger001',
    metadata={
        "deleniti": 'sapiente',
        "amet": 'deserunt',
        "nisi": 'vel',
    },
    reference='ref:001',
    source='users:001',
    start_time=dateutil.parser.isoparse('2021-10-15T07:59:26.631Z'),
    start_time_deprecated=dateutil.parser.isoparse('2022-12-24T23:52:02.245Z'),
)

res = s.transactions.count_transactions(req)

if res.status_code == 200:
    # handle response
```

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
            "magnam": 'distinctio',
            "id": 'labore',
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
            vars={
                "natus": 'nobis',
                "eum": 'vero',
            },
        ),
        timestamp=dateutil.parser.isoparse('2022-11-24T10:55:00.183Z'),
    ),
    ledger='ledger001',
    preview=True,
)

res = s.transactions.create_transaction(req)

if res.transactions_response is not None:
    # handle response
```

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
    end_time=dateutil.parser.isoparse('2022-11-28T06:48:16.205Z'),
    end_time_deprecated=dateutil.parser.isoparse('2022-04-17T13:06:08.135Z'),
    ledger='ledger001',
    metadata={
        "quos": 'sint',
        "accusantium": 'mollitia',
        "reiciendis": 'mollitia',
    },
    page_size=320997,
    page_size_deprecated=431418,
    pagination_token='aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==',
    reference='ref:001',
    source='users:001',
    start_time=dateutil.parser.isoparse('2022-02-07T18:15:06.372Z'),
    start_time_deprecated=dateutil.parser.isoparse('2022-08-19T20:09:28.183Z'),
)

res = s.transactions.list_transactions(req)

if res.transactions_cursor_response is not None:
    # handle response
```

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
