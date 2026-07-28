---
collection: ansible
version: "6"
title: "lowlydba.sqlserver.sp_whoisactive module – Install/update sp_whoisactive by Adam Mechanic"
source_url: https://docs.ansible.com/projects/ansible/6/collections/lowlydba/sqlserver/sp_whoisactive_module.html
fetched_at: 2026-07-27T17:55:18+00:00
---
# lowlydba.sqlserver.sp_whoisactive module – Install/update `sp_whoisactive` by Adam Mechanic

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
> see [Requirements](sp_whoisactive_module.md#ansible-collections-lowlydba-sqlserver-sp-whoisactive-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.sp_whoisactive`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](sp_whoisactive_module.md#synopsis)
- [Requirements](sp_whoisactive_module.md#requirements)
- [Parameters](sp_whoisactive_module.md#parameters)
- [Attributes](sp_whoisactive_module.md#attributes)
- [Examples](sp_whoisactive_module.md#examples)
- [Return Values](sp_whoisactive_module.md#return-values)

## [Synopsis](sp_whoisactive_module.md#id1)

- A wrapper for `Install-DbaWhoIsActive` to fetch the latest version of the script, or install from a local cached version.

## [Requirements](sp_whoisactive_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](sp_whoisactive_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **database**  string / required | Name of the target database. |
| **force**  boolean | If this switch is enabled, then `sp_WhoisActive` will be downloaded from the internet even if previously cached.  Choices:   - `false` ← (default) - `true` |
| **local_file**  string | Specifies the path to a local file to install sp_WhoisActive from.  This can be either the zip file as distributed by the website or the expanded SQL script.  If this option is not specified, the latest version will be downloaded and installed from <https://github.com/amachanic/sp_whoisactive/releases> |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |

## [Attributes](sp_whoisactive_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | Platforms: all | Target OS/families that can be operated against. |

## [Examples](sp_whoisactive_module.md#id5)

```yaml+jinja
- name: Install/Update sp_whoisactive
  lowlydba.sqlserver.sp_whoisactive:
    sql_instance: sql-01.myco.io
    database: lowlydb
```

## [Return Values](sp_whoisactive_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `Install-DbaWhoIsActive` function.  Returned: success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

[Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
[Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
