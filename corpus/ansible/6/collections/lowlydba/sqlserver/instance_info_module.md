---
collection: ansible
version: "6"
title: "lowlydba.sqlserver.instance_info module – Returns basic information for a SQL Server instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/lowlydba/sqlserver/instance_info_module.html
fetched_at: 2026-07-27T17:55:10+00:00
---
# lowlydba.sqlserver.instance_info module – Returns basic information for a SQL Server instance

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
> see [Requirements](instance_info_module.md#ansible-collections-lowlydba-sqlserver-instance-info-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.instance_info`.

New in lowlydba.sqlserver 0.2.0

- [Synopsis](instance_info_module.md#synopsis)
- [Requirements](instance_info_module.md#requirements)
- [Parameters](instance_info_module.md#parameters)
- [Attributes](instance_info_module.md#attributes)
- [Examples](instance_info_module.md#examples)
- [Return Values](instance_info_module.md#return-values)

## [Synopsis](instance_info_module.md#id1)

- Returns basic information for a SQL Server instance.

## [Requirements](instance_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](instance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |

## [Attributes](instance_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | This module is “read only” and operates the same regardless of check mode. |
| **platform** | Platforms: all | Target OS/families that can be operated against. |

## [Examples](instance_info_module.md#id5)

```yaml+jinja
- name: Get basic info for an instance
  lowlydba.sqlserver.instance_info:
    sql_instance: sql-01.myco.io
```

## [Return Values](instance_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Instance level properties of the SQL Server instance.  Returned: always |

### Authors

- John McCall (@lowlydba)

### Collection links

[Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
[Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
