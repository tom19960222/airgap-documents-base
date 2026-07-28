---
collection: ansible
version: "8"
title: "community.general.odbc module – Execute SQL via ODBC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/odbc_module.html
fetched_at: 2026-07-28T01:48:16+00:00
---
# community.general.odbc module – Execute SQL via ODBC

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](odbc_module.md#ansible-collections-community-general-odbc-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.odbc`.

New in community.general 1.0.0

- [Synopsis](odbc_module.md#synopsis)
- [Requirements](odbc_module.md#requirements)
- [Parameters](odbc_module.md#parameters)
- [Attributes](odbc_module.md#attributes)
- [Notes](odbc_module.md#notes)
- [Examples](odbc_module.md#examples)
- [Return Values](odbc_module.md#return-values)

## [Synopsis](odbc_module.md#id1)

- Read/Write info via ODBC drivers.

Aliases: database.misc.odbc

## [Requirements](odbc_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- pyodbc

## [Parameters](odbc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **commit**  boolean  *added in community.general 1.3.0* | Perform a commit after the execution of the SQL query.  Some databases allow a commit after a select whereas others raise an exception.  Default is `true` to support legacy module behavior.  **Choices:**   - `false` - `true` ← (default) |
| **dsn**  string / required | The connection string passed into ODBC. |
| **params**  list / elements=string | Parameters to pass to the SQL query. |
| **query**  string / required | The SQL query to perform. |

## [Attributes](odbc_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](odbc_module.md#id5)

> **Note:**
>
> - Like the command module, this module always returns changed = yes whether or not the query would change the database.
> - To alter this behavior you can use `changed_when`: [yes or no].
> - For details about return values (description and row_count) see <https://github.com/mkleehammer/pyodbc/wiki/Cursor>.

## [Examples](odbc_module.md#id6)

```yaml+jinja
- name: Set some values in the test db
  community.general.odbc:
    dsn: "DRIVER={ODBC Driver 13 for SQL Server};Server=db.ansible.com;Database=my_db;UID=admin;PWD=password;"
    query: "Select * from table_a where column1 = ?"
    params:
      - "value1"
    commit: false
  changed_when: false
```

## [Return Values](odbc_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  list / elements=dictionary | List of dicts about the columns selected from the cursors, likely empty for DDL statements. See notes.  **Returned:** success |
| **results**  list / elements=list | List of lists of strings containing selected rows, likely empty for DDL statements.  **Returned:** success |
| **row_count**  string | The number of rows selected or modified according to the cursor defaults to -1. See notes.  **Returned:** success |

### Authors

- John Westcott IV (@john-westcott-iv)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
