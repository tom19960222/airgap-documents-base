---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.resource_governor module – Configures the resource governor on a SQL Server instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/resource_governor_module.html
fetched_at: 2026-07-28T02:40:36+00:00
---
# lowlydba.sqlserver.resource_governor module – Configures the resource governor on a SQL Server instance

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
> see [Requirements](resource_governor_module.md#ansible-collections-lowlydba-sqlserver-resource-governor-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.resource_governor`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](resource_governor_module.md#synopsis)
- [Requirements](resource_governor_module.md#requirements)
- [Parameters](resource_governor_module.md#parameters)
- [Attributes](resource_governor_module.md#attributes)
- [Examples](resource_governor_module.md#examples)
- [Return Values](resource_governor_module.md#return-values)

## [Synopsis](resource_governor_module.md#id1)

- Enables or disables and optionally sets the classifier function for the resource governor feature.

## [Requirements](resource_governor_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](resource_governor_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **classifier_function**  string | The name of the classifier function that resource governor will use. To clear the function, use the string `NULL`. |
| **enabled**  boolean | Whether to enable or disable resource governor.  **Choices:**   - `false` - `true` ← (default) |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |

## [Attributes](resource_governor_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](resource_governor_module.md#id5)

```yaml+jinja
- name: Enable resource governor
  lowlydba.sqlserver.resource_governor:
    sql_instance: sql-01.myco.io
    enabled: true
```

## [Return Values](resource_governor_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `Set-DbaResourceGovernor` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
