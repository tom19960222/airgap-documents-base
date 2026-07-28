---
collection: ansible
version: "6"
title: "community.general.hana_query module – Execute SQL on HANA"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/hana_query_module.html
fetched_at: 2026-07-27T17:09:15+00:00
---
# community.general.hana_query module – Execute SQL on HANA

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.hana_query`.

New in community.general 3.2.0

- [Synopsis](hana_query_module.md#synopsis)
- [Parameters](hana_query_module.md#parameters)
- [Notes](hana_query_module.md#notes)
- [Examples](hana_query_module.md#examples)
- [Return Values](hana_query_module.md#return-values)

## [Synopsis](hana_query_module.md#id1)

- This module executes SQL statements on HANA with hdbsql.

## [Parameters](hana_query_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **autocommit**  boolean | Autocommit the statement.  Choices:   - `false` - `true` ← (default) |
| **database**  string | Define the database on which to connect. |
| **encrypted**  boolean | Use encrypted connection. Defaults to `false`.  Choices:   - `false` ← (default) - `true` |
| **filepath**  list / elements=path | One or more files each containing one SQL query to run.  Must be a string or list containing strings. |
| **host**  string | The Host IP address. The port can be defined as well. |
| **instance**  string / required | The instance number. |
| **password**  string | The password to connect to the database.  **Note:** Since the passwords have to be passed as command line arguments, *userstore=true* should be used whenever possible, as command line arguments can be seen by other users on the same machine. |
| **query**  list / elements=string | SQL query to run.  Must be a string or list containing strings. Please note that if you supply a string, it will be split by commas (`,`) to a list. It is better to supply a one-element list instead to avoid mangled input. |
| **sid**  string / required | The system ID. |
| **user**  string | A dedicated username. The user could be also in hdbuserstore. Defaults to `SYSTEM`.  Default: `"SYSTEM"` |
| **userstore**  boolean  added in community.general 3.5.0 | If `true` the user must be in hdbuserstore.  Choices:   - `false` ← (default) - `true` |

## [Notes](hana_query_module.md#id3)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](hana_query_module.md#id4)

```yaml+jinja
- name: Simple select query
  community.general.hana_query:
    sid: "hdb"
    instance: "01"
    password: "Test123"
    query: "select user_name from users"

- name: Run several queries
  community.general.hana_query:
    sid: "hdb"
    instance: "01"
    password: "Test123"
    query:
    - "select user_name from users;"
    - select * from SYSTEM;
    host: "localhost"
    autocommit: false

- name: Run several queries from file
  community.general.hana_query:
    sid: "hdb"
    instance: "01"
    password: "Test123"
    filepath:
    - /tmp/HANA_CPU_UtilizationPerCore_2.00.020+.txt
    - /tmp/HANA.txt
    host: "localhost"

- name: Run several queries from user store
  community.general.hana_query:
    sid: "hdb"
    instance: "01"
    user: hdbstoreuser
    userstore: true
    query:
    - "select user_name from users;"
    - select * from users;
    autocommit: false
```

## [Return Values](hana_query_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **query_result**  list / elements=list | List containing results of all queries executed (one sublist for every query).  Returned: on success  Sample: `[[{"Column": "Value1"}, {"Column": "Value2"}], [{"Column": "Value1"}, {"Column": "Value2"}]]` |

### Authors

- Rainer Leber (@rainerleber)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
