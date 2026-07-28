---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.ag_listener module – Configures an availability group listener"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/ag_listener_module.html
fetched_at: 2026-07-28T02:40:21+00:00
---
# lowlydba.sqlserver.ag_listener module – Configures an availability group listener

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
> see [Requirements](ag_listener_module.md#ansible-collections-lowlydba-sqlserver-ag-listener-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.ag_listener`.

New in lowlydba.sqlserver 0.5.0

- [Synopsis](ag_listener_module.md#synopsis)
- [Requirements](ag_listener_module.md#requirements)
- [Parameters](ag_listener_module.md#parameters)
- [Attributes](ag_listener_module.md#attributes)
- [Examples](ag_listener_module.md#examples)
- [Return Values](ag_listener_module.md#return-values)

## [Synopsis](ag_listener_module.md#id1)

- Creates an Availability Group Listener for an existing availability group.

## [Requirements](ag_listener_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](ag_listener_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ag_name**  string / required | Name of the target availability group. |
| **dhcp**  boolean | Indicates whether the listener uses DHCP.  **Choices:**   - `false` ← (default) - `true` |
| **ip_address**  string | IP address(es) of the listener. Comma separated if multiple. |
| **listener_name**  string / required | Name of the Listener to be configured. |
| **port**  integer | Sets the port number used to communicate with the availability group.  **Default:** `1433` |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **state**  string | Whether or not the object should be `present` or `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet_ip**  string | Subnet IP address(es) of the listener. Comma separated if multiple. |
| **subnet_mask**  string | Sets the subnet IP mask(s) of the availability group listener. Comma separated if multiple.  **Default:** `"255.255.255.0"` |

## [Attributes](ag_listener_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against. |

## [Examples](ag_listener_module.md#id5)

```yaml+jinja
- name: Create Availability Group
  lowlydba.sqlserver.availability_group:
    sql_instance: sql-01.myco.io
    ag_name: AG_MyDatabase

- name: Create AG Listener
  lowlydba.sqlserver.ag_listener:
    sql_instance_primary: sql-01.myco.io
    ag_name: AG_MyDatabase
    listener_name: aglMyDatabase
    ip_address: 10.0.20.20,10.1.77.77
    subnet_ip: 255.255.252.0
    subnet_mask: 255.255.255.0
```

## [Return Values](ag_listener_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `Add-DbaAgListener` or `Set-DbaAgListener` function.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
