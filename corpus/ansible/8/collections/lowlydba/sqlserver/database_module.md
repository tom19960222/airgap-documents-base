---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.database module – Creates and configures a database"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/database_module.html
fetched_at: 2026-07-28T02:40:29+00:00
---
# lowlydba.sqlserver.database module – Creates and configures a database

> **Note:**
>
> This module is part of the [lowlydba.sqlserver collection](https://galaxy.ansible.com/ui/repo/published/lowlydba/sqlserver/) (version 2.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install lowlydba.sqlserver`.
> You need further requirements to be able to use this module,
> see [Requirements](database_module.md#ansible-collections-lowlydba-sqlserver-database-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.database`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](database_module.md#synopsis)
- [Requirements](database_module.md#requirements)
- [Parameters](database_module.md#parameters)
- [Attributes](database_module.md#attributes)
- [Examples](database_module.md#examples)
- [Return Values](database_module.md#return-values)

## [Synopsis](database_module.md#id1)

- Adds a new database to an existing SQL Server instance.

## [Requirements](database_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](database_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **compatibility**  string | Compatibility mode for the database. Follows the format of `Version90`, `Version100`, and so on.  String is validated by `Set-DbaDbCompatibility`. |
| **data_file_path**  string | Directory where the data files should be placed. Uses SQL Server’s default if not supplied.  Only used if database is being created. |
| **database**  string / required | Name of the target database. |
| **log_file_path**  string | Directory where the log files should be placed. Uses SQL Server’s default if not supplied.  Only used if database is being created. |
| **maxdop**  integer | MAXDOP value for the database. |
| **only_accessible**  boolean  *added in lowlydba.sqlserver 2.2.0* | Whether or not to enable Read Committed Snapshot Isolation.  **Choices:**   - `false` - `true` ← (default) |
| **owner**  string | Database owner login. |
| **rcsi**  boolean | Whether or not to enable Read Committed Snapshot Isolation.  **Choices:**   - `false` - `true` |
| **recovery_model**  string | Choose the recovery model for the database.  **Choices:**   - `"Full"` - `"Simple"` - `"BulkLogged"` |
| **secondary_maxdop**  integer | MAXDOP value for the database when it is a non-primary replica in an availability group. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **state**  string | Whether or not the object should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Attributes](database_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](database_module.md#id5)

```yaml+jinja
- name: Create database
  lowlydba.sqlserver.database:
    sql_instance: sql-01.myco.io
    database: LowlyDB

- name: Create database with customizations
  lowlydba.sqlserver.database:
    sql_instance: sql-01.myco.io
    database: LowlyDB
    owner: sa
    maxdop: 2
    recovery_model: Simple
```

## [Return Values](database_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Modified output from the `New-DbaDatabase`, `Set-DbaDatabase`, or `Remove-DbaDatabase` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
