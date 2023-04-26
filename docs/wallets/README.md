# wallets

## Overview

Everything related to Wallets

### Available Operations

* [confirm_hold](#confirm_hold) - Confirm a hold
* [create_balance](#create_balance) - Create a balance
* [create_wallet](#create_wallet) - Create a new wallet
* [credit_wallet](#credit_wallet) - Credit a wallet
* [debit_wallet](#debit_wallet) - Debit a wallet
* [get_balance](#get_balance) - Get detailed balance
* [get_hold](#get_hold) - Get a hold
* [get_holds](#get_holds) - Get all holds for a wallet
* [get_transactions](#get_transactions)
* [get_wallet](#get_wallet) - Get a wallet
* [list_balances](#list_balances) - List balances of a wallet
* [list_wallets](#list_wallets) - List all wallets
* [update_wallet](#update_wallet) - Update a wallet
* [void_hold](#void_hold) - Cancel a hold
* [walletsget_server_info](#walletsget_server_info) - Get server info

## confirm_hold

Confirm a hold

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.ConfirmHoldRequest(
    confirm_hold_request=shared.ConfirmHoldRequest(
        amount=100,
        final=True,
    ),
    hold_id="iure",
)

res = s.wallets.confirm_hold(req)

if res.status_code == 200:
    # handle response
```

## create_balance

Create a balance

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.CreateBalanceRequest(
    create_balance_request=shared.CreateBalanceRequest(
        name="Doyle Gibson",
    ),
    id="b711e5b7-fd2e-4d02-8921-cddc692601fb",
)

res = s.wallets.create_balance(req)

if res.create_balance_response is not None:
    # handle response
```

## create_wallet

Create a new wallet

### Example Usage

```python
import formance
from formance.models import shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = shared.CreateWalletRequest(
    metadata={
        "voluptate": "autem",
        "nam": "eaque",
    },
    name="Dr. Herman Wolf",
)

res = s.wallets.create_wallet(req)

if res.create_wallet_response is not None:
    # handle response
```

## credit_wallet

Credit a wallet

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.CreditWalletRequest(
    credit_wallet_request=shared.CreditWalletRequest(
        amount=shared.Monetary(
            amount=11714,
            asset="cumque",
        ),
        balance="corporis",
        metadata={
            "libero": "nobis",
            "dolores": "quis",
            "totam": "dignissimos",
            "eaque": "quis",
        },
        reference="nesciunt",
        sources=[
            shared.LedgerAccountSubject(
                identifier="dolores",
                type="minus",
            ),
        ],
    ),
    id="73d5fe9b-90c2-4890-9b3f-e49a8d9cbf48",
)

res = s.wallets.credit_wallet(req)

if res.status_code == 200:
    # handle response
```

## debit_wallet

Debit a wallet

### Example Usage

```python
import formance
from formance.models import operations, shared

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.DebitWalletRequest(
    debit_wallet_request=shared.DebitWalletRequest(
        amount=shared.Monetary(
            amount=398221,
            asset="dolorem",
        ),
        balances=[
            "dolor",
        ],
        description="qui",
        destination=shared.LedgerAccountSubject(
            identifier="hic",
            type="excepturi",
        ),
        metadata={
            "voluptate": "dignissimos",
            "reiciendis": "amet",
            "dolorum": "numquam",
        },
        pending=False,
    ),
    id="100674eb-f692-480d-9ba7-7a89ebf737ae",
)

res = s.wallets.debit_wallet(req)

if res.debit_wallet_response is not None:
    # handle response
```

## get_balance

Get detailed balance

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.GetBalanceRequest(
    balance_name="eius",
    id="203ce5e6-a95d-48a0-9446-ce2af7a73cf3",
)

res = s.wallets.get_balance(req)

if res.get_balance_response is not None:
    # handle response
```

## get_hold

Get a hold

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.GetHoldRequest(
    hold_id="tempore",
)

res = s.wallets.get_hold(req)

if res.get_hold_response is not None:
    # handle response
```

## get_holds

Get all holds for a wallet

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.GetHoldsRequest(
    cursor="aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
    metadata={
        "numquam": "enim",
        "dolorem": "sapiente",
        "totam": "nihil",
        "sit": "expedita",
    },
    page_size=207470,
    wallet_id="sed",
)

res = s.wallets.get_holds(req)

if res.get_holds_response is not None:
    # handle response
```

## get_transactions

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.GetTransactionsRequest(
    cursor="aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
    page_size=424685,
    wallet_id="libero",
)

res = s.wallets.get_transactions(req)

if res.get_transactions_response is not None:
    # handle response
```

## get_wallet

Get a wallet

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.GetWalletRequest(
    id="5a73429c-db1a-4842-abb6-79d2322715bf",
)

res = s.wallets.get_wallet(req)

if res.get_wallet_response is not None:
    # handle response
```

## list_balances

List balances of a wallet

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.ListBalancesRequest(
    id="0cbb1e31-b8b9-40f3-843a-1108e0adcf4b",
)

res = s.wallets.list_balances(req)

if res.list_balances_response is not None:
    # handle response
```

## list_wallets

List all wallets

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.ListWalletsRequest(
    cursor="aHR0cHM6Ly9nLnBhZ2UvTmVrby1SYW1lbj9zaGFyZQ==",
    metadata={
        "qui": "quae",
        "laudantium": "odio",
        "occaecati": "voluptatibus",
    },
    name="Ignacio Moen",
    page_size=961571,
)

res = s.wallets.list_wallets(req)

if res.list_wallets_response is not None:
    # handle response
```

## update_wallet

Update a wallet

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.UpdateWalletRequest(
    request_body=operations.UpdateWalletRequestBody(
        metadata={
            "consectetur": "vero",
            "tenetur": "dignissimos",
        },
    ),
    id="fbc7abd7-4dd3-49c0-b5d2-cff7c70a4562",
)

res = s.wallets.update_wallet(req)

if res.status_code == 200:
    # handle response
```

## void_hold

Cancel a hold

### Example Usage

```python
import formance
from formance.models import operations

s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


req = operations.VoidHoldRequest(
    hold_id="vel",
)

res = s.wallets.void_hold(req)

if res.status_code == 200:
    # handle response
```

## walletsget_server_info

Get server info

### Example Usage

```python
import formance


s = formance.Formance(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    ),
)


res = s.wallets.walletsget_server_info()

if res.server_info is not None:
    # handle response
```
