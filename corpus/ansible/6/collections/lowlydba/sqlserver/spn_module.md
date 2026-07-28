---
collection: ansible
version: "6"
title: "lowlydba.sqlserver.spn module – Configures SPNs for SQL Server"
source_url: https://docs.ansible.com/projects/ansible/6/collections/lowlydba/sqlserver/spn_module.html
fetched_at: 2026-07-27T17:55:19+00:00
---
# lowlydba.sqlserver.spn module – Configures SPNs for SQL Server

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
> see [Requirements](spn_module.md#ansible-collections-lowlydba-sqlserver-spn-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.spn`.

New in lowlydba.sqlserver 0.6.0

- [Synopsis](spn_module.md#synopsis)
- [Requirements](spn_module.md#requirements)
- [Parameters](spn_module.md#parameters)
- [Attributes](spn_module.md#attributes)
- [Examples](spn_module.md#examples)
- [Return Values](spn_module.md#return-values)

## [Synopsis](spn_module.md#id1)

- Configures SPNs for SQL Server.

## [Requirements](spn_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](spn_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **computer**  string / required | The host or alias to configure the SPN for. Can include the port in the format `host:port`. |
| **computer_password**  string | Password of a credential to connect to Active Directory with. |
| **computer_username**  string | Username of a credential to connect to Active Directory with. |
| **service_account**  string / required | The account you want the SPN added to. Will be looked up if not provided. |
| **state**  string | Whether or not the object should be `present` or `absent`.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Attributes](spn_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | Platform: Windows | Target OS/families that can be operated against. |

## [Examples](spn_module.md#id5)

```yaml+jinja
- name: Add server SPN
  lowlydba.sqlserver.spn:
    computer: sql-01.myco.io
    service_account: myco\sql-svc

- name: Create an AG Listener
  lowlydba.sqlserver.ag_listener:
    sql_instance_primary: sql-01.myco.io
    ag_name: AG_MyDatabase
    listener_name: aglMyDatabase
    ip_address: 10.0.20.20,10.1.77.77
    subnet_ip: 255.255.252.0
    subnet_mask: 255.255.255.0

- name: Add SPN for new AG listener on port 1433
  lowlydba.sqlserver.spn:
    computer: aglMyDatabase.myco.io:1433
    service_account: myco\sql-svc
```

## [Return Values](spn_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `Set-DbaSpn` or `Remove-DbaSpn` function.  Returned: success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

[Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
[Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
