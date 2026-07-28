---
collection: ansible
version: "8"
title: "community.general.mssql_db module – Add or remove MSSQL databases from a remote host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/mssql_db_module.html
fetched_at: 2026-07-28T01:48:03+00:00
---
# community.general.mssql_db module – Add or remove MSSQL databases from a remote host

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
> see [Requirements](mssql_db_module.md#ansible-collections-community-general-mssql-db-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.mssql_db`.

- [Synopsis](mssql_db_module.md#synopsis)
- [Requirements](mssql_db_module.md#requirements)
- [Parameters](mssql_db_module.md#parameters)
- [Attributes](mssql_db_module.md#attributes)
- [Notes](mssql_db_module.md#notes)
- [Examples](mssql_db_module.md#examples)

## [Synopsis](mssql_db_module.md#id1)

- Add or remove MSSQL databases from a remote host.

Aliases: database.mssql.mssql_db

## [Requirements](mssql_db_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- pymssql

## [Parameters](mssql_db_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **autocommit**  boolean | Automatically commit the change only if the import succeed. Sometimes it is necessary to use autocommit=true, since some content can’t be changed within a transaction.  **Choices:**   - `false` ← (default) - `true` |
| **login_host**  string / required | Host running the database |
| **login_password**  string | The password used to authenticate with  **Default:** `""` |
| **login_port**  string | Port of the MSSQL server. Requires login_host be defined as other than localhost if login_port is used  **Default:** `"1433"` |
| **login_user**  string | The username used to authenticate with  **Default:** `""` |
| **name**  aliases: db  string / required | name of the database to add or remove |
| **state**  string | The database state  **Choices:**   - `"present"` ← (default) - `"absent"` - `"import"` |
| **target**  string | Location, on the remote host, of the dump file to read from or write to. Uncompressed SQL files (`.sql`) files are supported. |

## [Attributes](mssql_db_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](mssql_db_module.md#id5)

> **Note:**
>
> - Requires the pymssql Python package on the remote host. For Ubuntu, this is as easy as pip install pymssql (See [ansible.builtin.pip](../../ansible/builtin/pip_module.md#ansible-collections-ansible-builtin-pip-module).)

## [Examples](mssql_db_module.md#id6)

```yaml+jinja
- name: Create a new database with name 'jackdata'
  community.general.mssql_db:
    name: jackdata
    state: present

# Copy database dump file to remote host and restore it to database 'my_db'
- name: Copy database dump file to remote host
  ansible.builtin.copy:
    src: dump.sql
    dest: /tmp

- name: Restore the dump file to database 'my_db'
  community.general.mssql_db:
    name: my_db
    state: import
    target: /tmp/dump.sql
```

### Authors

- Vedit Firat Arig (@vedit)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
