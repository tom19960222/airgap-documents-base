---
collection: ansible
version: "6"
title: "lowlydba.sqlserver.rg_resource_pool module – Configures a resource pool for use by the Resource Governor"
source_url: https://docs.ansible.com/projects/ansible/6/collections/lowlydba/sqlserver/rg_resource_pool_module.html
fetched_at: 2026-07-27T17:55:15+00:00
---
# lowlydba.sqlserver.rg_resource_pool module – Configures a resource pool for use by the Resource Governor

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
> see [Requirements](rg_resource_pool_module.md#ansible-collections-lowlydba-sqlserver-rg-resource-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.rg_resource_pool`.

New in lowlydba.sqlserver 0.1.0

- [Synopsis](rg_resource_pool_module.md#synopsis)
- [Requirements](rg_resource_pool_module.md#requirements)
- [Parameters](rg_resource_pool_module.md#parameters)
- [Attributes](rg_resource_pool_module.md#attributes)
- [Examples](rg_resource_pool_module.md#examples)
- [Return Values](rg_resource_pool_module.md#return-values)

## [Synopsis](rg_resource_pool_module.md#id1)

- Creates or modifies a resource pool to be used by the Resource Governor. Default values are handled by the Powershell functions themselves.

## [Requirements](rg_resource_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](rg_resource_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cap_cpu_perc**  integer | Cap CPU Percentage able to be used by queries in this resource pool. |
| **max_cpu_perc**  integer | Maximum CPU Percentage able to be used by queries in this resource pool. |
| **max_iops_per_vol**  integer | Maximum IOPS/volume able to be used by queries in this resource pool. |
| **max_mem_perc**  integer | Maximum Memory Percentage able to be used by queries in this resource pool. |
| **min_cpu_perc**  integer | Minimum CPU Percentage able to be used by queries in this resource pool. |
| **min_iops_per_vol**  integer | Minimum IOPS/volume able to be used by queries in this resource pool. |
| **min_mem_perc**  integer | Minimum Memory Percentage able to be used by queries in this resource pool. |
| **resource_pool**  string / required | Name of the target resource pool. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **state**  string | Whether or not the object should be `present` or `absent`.  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string | Specify the type of resource pool.  Choices:   - `"Internal"` ← (default) - `"External"` |

## [Attributes](rg_resource_pool_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | Platforms: all | Target OS/families that can be operated against. |

## [Examples](rg_resource_pool_module.md#id5)

```yaml+jinja
- name: Enable resource governor
  lowlydba.sqlserver.resource_governor:
    sql_instance: sql-01.myco.io
    enabled: true

- name: Create rg resource pool
  lowlydba.sqlserver.rg_resource_pool:
    sql_instance: sql-01.myco.io
    resource_pool: "rpLittle"
    max_cpu_perc: 5
```

## [Return Values](rg_resource_pool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `Set-DbaRgResourcePool`, `New-DbaRgResourcePool`, or `Remove-DbaRgResourcePool` function.  Returned: success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

[Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
[Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
