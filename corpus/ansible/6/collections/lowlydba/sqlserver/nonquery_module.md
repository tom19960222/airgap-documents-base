---
collection: ansible
version: "6"
title: "lowlydba.sqlserver.nonquery module – Executes a generic nonquery"
source_url: https://docs.ansible.com/projects/ansible/6/collections/lowlydba/sqlserver/nonquery_module.html
fetched_at: 2026-07-27T17:55:13+00:00
---
# lowlydba.sqlserver.nonquery module – Executes a generic nonquery

> **Note:**
>
> This module is part of the [lowlydba.sqlserver collection](https://galaxy.ansible.com/lowlydba/sqlserver) (version 1.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install lowlydba.sqlserver`.
> You need further requirements to be able to use this module,
> see [Requirements](nonquery_module.md#ansible-collections-lowlydba-sqlserver-nonquery-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.nonquery`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](nonquery_module.md#synopsis)
- [Requirements](nonquery_module.md#requirements)
- [Parameters](nonquery_module.md#parameters)
- [Attributes](nonquery_module.md#attributes)
- [Examples](nonquery_module.md#examples)

## [Synopsis](nonquery_module.md#id1)

- Execute a nonquery against a database. Does not return a resultset. Ideal for ad-hoc configurations or DML queries.

## [Requirements](nonquery_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](nonquery_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **database**  string / required | Name of the database to execute the nonquery in. |
| **nonquery**  string / required | The nonquery to be executed. |
| **query_timeout**  integer | Number of seconds to wait before timing out the nonquery execution.  Default: `60` |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |

## [Attributes](nonquery_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | Platforms: all | Target OS/families that can be operated against. |

## [Examples](nonquery_module.md#id5)

```yaml+jinja
- name: Update a table value
  lowlydba.sqlserver.nonquery:
    sql_instance: sql-01-myco.io
    database: userdb
    nonquery: "UPDATE dbo.User set IsActive = 1;"
```

### Authors

- John McCall (@lowlydba)

### Collection links

[Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
[Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
