---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.hadr module – Enable or disable HADR"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/hadr_module.html
fetched_at: 2026-07-28T02:40:31+00:00
---
# lowlydba.sqlserver.hadr module – Enable or disable HADR

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
> see [Requirements](hadr_module.md#ansible-collections-lowlydba-sqlserver-hadr-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.hadr`.

New in lowlydba.sqlserver 0.4.0

- [Synopsis](hadr_module.md#synopsis)
- [Requirements](hadr_module.md#requirements)
- [Parameters](hadr_module.md#parameters)
- [Attributes](hadr_module.md#attributes)
- [Examples](hadr_module.md#examples)
- [Return Values](hadr_module.md#return-values)

## [Synopsis](hadr_module.md#id1)

- Enable or disable the High Availability Disaster Recovery (HADR) feature.

## [Requirements](hadr_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](hadr_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean | Flag to enable or disable the feature.  **Choices:**   - `false` - `true` ← (default) |
| **force**  boolean | Restart SQL Server and SQL Agent services automatically.  **Choices:**   - `false` ← (default) - `true` |
| **password**  string | Password for alternative credential to authenticate with Windows. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **username**  string | Username for alternative credential to authenticate with Windows. |

## [Attributes](hadr_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platform:** **Windows** | Target OS/families that can be operated against. |

## [Examples](hadr_module.md#id5)

```yaml+jinja
- name: Enable hadr with service restart
  lowlydba.sqlserver.hadr:
    sql_instance: sql-01.myco.io
    enabled: true
    force: true
```

## [Return Values](hadr_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `Enable-DbaAgHadr` or `Disable-DbaAgHadr` function.  RestartRequired returned if the setting requires a service restart to take effect.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
