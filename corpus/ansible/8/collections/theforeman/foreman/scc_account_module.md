---
collection: ansible
version: "8"
title: "theforeman.foreman.scc_account module – Manage SUSE Customer Center Accounts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/scc_account_module.html
fetched_at: 2026-07-28T02:56:34+00:00
---
# theforeman.foreman.scc_account module – Manage SUSE Customer Center Accounts

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](scc_account_module.md#ansible-collections-theforeman-foreman-scc-account-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.scc_account`.

New in theforeman.foreman 1.0.0

- [Synopsis](scc_account_module.md#synopsis)
- [Requirements](scc_account_module.md#requirements)
- [Parameters](scc_account_module.md#parameters)
- [Attributes](scc_account_module.md#attributes)
- [Examples](scc_account_module.md#examples)
- [Return Values](scc_account_module.md#return-values)

## [Synopsis](scc_account_module.md#id1)

- Manage SUSE Customer Center Accounts
- This module requires the foreman_scc_manager plugin set up in the server
- See <https://github.com/ATIX-AG/foreman_scc_manager>

Aliases: foreman_scc_account

## [Requirements](scc_account_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](scc_account_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **base_url**  string | URL of SUSE for suse customer center account |
| **interval**  string | Interval for syncing suse customer center account  **Choices:**   - `"never"` - `"daily"` - `"weekly"` - `"monthly"` |
| **login**  string | Login id of suse customer center account |
| **name**  string / required | Name of the suse customer center account |
| **organization**  string / required | Name of related organization |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **scc_account_password**  string | Password of suse customer center account |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the suse customer center account  **Choices:**   - `"present"` ← (default) - `"absent"` - `"synced"` |
| **sync_date**  string | Last Sync time of suse customer center account |
| **test_connection**  boolean | Test suse customer center account credentials that connects to the server  **Choices:**   - `false` ← (default) - `true` |
| **updated_name**  string | Name to be updated of suse customer center account |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](scc_account_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](scc_account_module.md#id5)

```yaml+jinja
- name: "Create a suse customer center account"
  theforeman.foreman.scc_account:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "Test"
    login: "abcde"
    scc_account_password: "12345"
    base_url: "https://scc.suse.com"
    state: present

- name: "Update a suse customer center account"
  theforeman.foreman.scc_account:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "Test1"
    state: present

- name: "Delete a suse customer center account"
  theforeman.foreman.scc_account:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "Test"
    state: absent
```

## [Return Values](scc_account_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **scc_accounts**  list / elements=dictionary | List of scc accounts.  **Returned:** success |

### Authors

- Manisha Singhal (@manisha15) ATIX AG

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
