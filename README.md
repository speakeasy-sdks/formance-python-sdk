<div align="center">
    <picture>
        <source srcset="https://user-images.githubusercontent.com/6267663/221572723-e77f55a3-5d19-4a13-94f8-e7b0b340d71e.svg" media="(prefers-color-scheme: dark)">
        <img src="https://user-images.githubusercontent.com/6267663/221572726-6982541c-d1cf-4d9f-9bbf-cd774a2713e6.svg">
    </picture>
   <h1>Formance Python SDK</h1>
   <p><strong>Open Source Ledger for money-moving platforms</strong></p>
   <p>Build and track custom fit money flows on a scalable financial infrastructure.</p>
   <a href="https://docs.formance.com/api/stack/v1.0#section/Introduction"><img src="https://img.shields.io/static/v1?label=Docs&message=Docs&color=000&style=for-the-badge" /></a>
   <a href="https://github.com/speakeasy-sdks/formance-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/formance-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://join.slack.com/t/formance-community/shared_invite/zt-1of48xmgy-Jc6RH8gzcWf5D0qD2HBPQA"><img src="https://img.shields.io/static/v1?label=Slack&message=Join&color=7289da&style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
</div>

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install formance
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import formance
from formance.models import operations, shared

s = formance.Formance()
s.config_security(
    security=shared.Security(
        authorization="Bearer YOUR_ACCESS_TOKEN_HERE",
    )
)
    
res = s.get_server_info()

if res.server_info is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations

### Formance SDK

* `get_server_info` - Get server info
* `paymentsget_server_info` - Get server info
* `searchget_server_info` - Get server info

### accounts

* `add_metadata_to_account` - Add metadata to an account
* `count_accounts` - Count the accounts from a ledger
* `get_account` - Get account by its address
* `list_accounts` - List accounts from a ledger

### balances

* `get_balances` - Get the balances from a ledger's account
* `get_balances_aggregated` - Get the aggregated balances from selected accounts

### clients

* `add_scope_to_client` - Add scope to client
* `create_client` - Create client
* `create_secret` - Add a secret to a client
* `delete_client` - Delete client
* `delete_scope_from_client` - Delete scope from client
* `delete_secret` - Delete a secret from a client
* `list_clients` - List clients
* `read_client` - Read client
* `update_client` - Update client

### ledger

* `get_ledger_info` - Get information about a ledger

### logs

* `list_logs` - List the logs from a ledger

### mapping

* `get_mapping` - Get the mapping of a ledger
* `update_mapping` - Update the mapping of a ledger

### orchestration

* `create_workflow` - Create workflow
* `get_flow` - Get a flow by id
* `get_workflow_occurrence` - Get a workflow occurrence by id
* `list_flows` - List registered flows
* `list_runs` - List occurrences of a workflow
* `orchestrationget_server_info` - Get server info
* `run_workflow` - Run workflow

### payments

* `connectors_stripe_transfer` - Transfer funds between Stripe accounts
* `get_connector_task` - Read a specific task of the connector
* `get_payment` - Get a payment
* `install_connector` - Install a connector
* `list_all_connectors` - List all installed connectors
* `list_configs_available_connectors` - List the configs of each available connector
* `list_connector_tasks` - List tasks from a connector
* `list_payments` - List payments
* `paymentslist_accounts` - List accounts
* `read_connector_config` - Read the config of a connector
* `reset_connector` - Reset a connector
* `uninstall_connector` - Uninstall a connector

### scopes

* `add_transient_scope` - Add a transient scope to a scope
* `create_scope` - Create scope
* `delete_scope` - Delete scope
* `delete_transient_scope` - Delete a transient scope from a scope
* `list_scopes` - List scopes
* `read_scope` - Read scope
* `update_scope` - Update scope

### script

* `run_script` - Execute a Numscript

### search

* `search` - Search

### server

* `get_info` - Show server information

### stats

* `read_stats` - Get statistics from a ledger

### transactions

* `create_transactions` - Create a new batch of transactions to a ledger
* `add_metadata_on_transaction` - Set the metadata of a transaction by its ID
* `count_transactions` - Count the transactions from a ledger
* `create_transaction` - Create a new transaction to a ledger
* `get_transaction` - Get transaction from a ledger by its ID
* `list_transactions` - List transactions from a ledger
* `revert_transaction` - Revert a ledger transaction by its ID

### users

* `list_users` - List users
* `read_user` - Read user

### wallets

* `confirm_hold` - Confirm a hold
* `create_balance` - Create a balance
* `create_wallet` - Create a new wallet
* `credit_wallet` - Credit a wallet
* `debit_wallet` - Debit a wallet
* `get_balance` - Get detailed balance
* `get_hold` - Get a hold
* `get_holds` - Get all holds for a wallet
* `get_transactions`
* `get_wallet` - Get a wallet
* `list_balances` - List balances of a wallet
* `list_wallets` - List all wallets
* `update_wallet` - Update a wallet
* `void_hold` - Cancel a hold
* `walletsget_server_info` - Get server info

### webhooks

* `activate_config` - Activate one config
* `change_config_secret` - Change the signing secret of a config
* `deactivate_config` - Deactivate one config
* `delete_config` - Delete one config
* `get_many_configs` - Get many configs
* `insert_config` - Insert a new config
* `test_config` - Test one config
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
