---
collection: ansible
version: "8"
title: "lowlydba.sqlserver.tcp_port module – Sets the TCP port for the instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/lowlydba/sqlserver/tcp_port_module.html
fetched_at: 2026-07-28T02:40:42+00:00
---
# lowlydba.sqlserver.tcp_port module – Sets the TCP port for the instance

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
> see [Requirements](tcp_port_module.md#ansible-collections-lowlydba-sqlserver-tcp-port-module-requirements) for details.
>
> To use it in a playbook, specify: `lowlydba.sqlserver.tcp_port`.

New in lowlydba.sqlserver 0.10.0

- [Synopsis](tcp_port_module.md#synopsis)
- [Requirements](tcp_port_module.md#requirements)
- [Parameters](tcp_port_module.md#parameters)
- [Attributes](tcp_port_module.md#attributes)
- [Examples](tcp_port_module.md#examples)
- [Return Values](tcp_port_module.md#return-values)

## [Synopsis](tcp_port_module.md#id1)

- Sets the TCP port for a SQL Server instance.

## [Requirements](tcp_port_module.md#id2)

The below requirements are needed on the host that executes this module.

- [dbatools](https://www.powershellgallery.com/packages/dbatools/) PowerShell module

## [Parameters](tcp_port_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **force**  boolean  *added in lowlydba.sqlserver 1.2.0* | Restart SQL Server and SQL Agent services automatically.  **Choices:**   - `false` ← (default) - `true` |
| **ip_address**  string | IPv4 address. |
| **password**  string | Password for alternative credential to authenticate with Windows. |
| **port**  integer / required | Port for SQL Server to listen on. |
| **sql_instance**  string / required | The SQL Server instance to modify. |
| **sql_password**  string | Password for SQL Authentication. |
| **sql_username**  string | Username for SQL Authentication. |
| **username**  string | Username for alternative credential to authenticate with Windows. |

## [Attributes](tcp_port_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target. |
| **platform** | **Platform:** **Windows** | Target OS/families that can be operated against. |

## [Examples](tcp_port_module.md#id5)

```yaml+jinja
- name: Set the default port
  lowlydba.sqlserver.tcp_port:
    sql_instance: sql-01.myco.io
    port: 1433

- name: Set a non-standard default port
  lowlydba.sqlserver.tcp_port:
    sql_instance: sql-01.myco.io
    port: 1933
```

## [Return Values](tcp_port_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | Output from the `Set-DbaTcpPort` function.  RestartRequired returned if the change requires a service restart to take effect.  **Returned:** success, but not in check_mode. |

### Authors

- John McCall (@lowlydba)

### Collection links

- [Issue Tracker](https://github.com/LowlyDBA/lowlydba.sqlserver/issues)
- [Repository (Sources)](https://github.com/LowlyDBA/lowlydba.sqlserver)
