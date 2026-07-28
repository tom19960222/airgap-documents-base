---
collection: ansible
version: "8"
title: "community.general.vertica_configuration module – Updates Vertica configuration parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/vertica_configuration_module.html
fetched_at: 2026-07-28T01:51:16+00:00
---
# community.general.vertica_configuration module – Updates Vertica configuration parameters

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](vertica_configuration_module.md#ansible-collections-community-general-vertica-configuration-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.vertica_configuration`.

- [Synopsis](vertica_configuration_module.md#synopsis)
- [Requirements](vertica_configuration_module.md#requirements)
- [Parameters](vertica_configuration_module.md#parameters)
- [Attributes](vertica_configuration_module.md#attributes)
- [Notes](vertica_configuration_module.md#notes)
- [Examples](vertica_configuration_module.md#examples)

## [Synopsis](vertica_configuration_module.md#id1)

- Updates Vertica configuration parameters.

Aliases: database.vertica.vertica_configuration

## [Requirements](vertica_configuration_module.md#id2)

The below requirements are needed on the host that executes this module.

- unixODBC
- pyodbc

## [Parameters](vertica_configuration_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | Name of the Vertica cluster.  **Default:** `"localhost"` |
| **db**  string | Name of the Vertica database. |
| **login_password**  string | The password used to authenticate with. |
| **login_user**  string | The username used to authenticate with.  **Default:** `"dbadmin"` |
| **parameter**  aliases: name  string / required | Name of the parameter to update. |
| **port**  string | Vertica cluster port to connect to.  **Default:** `"5433"` |
| **value**  string | Value of the parameter to be set. |

## [Attributes](vertica_configuration_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](vertica_configuration_module.md#id5)

> **Note:**
>
> - The default authentication assumes that you are either logging in as or sudo’ing to the `dbadmin` account on the host.
> - This module uses `pyodbc`, a Python ODBC database adapter. You must ensure that `unixODBC` and `pyodbc` is installed on the host and properly configured.
> - Configuring `unixODBC` for Vertica requires `Driver = /opt/vertica/lib64/libverticaodbc.so` to be added to the `Vertica` section of either `/etc/odbcinst.ini` or `$HOME/.odbcinst.ini` and both `ErrorMessagesPath = /opt/vertica/lib64` and `DriverManagerEncoding = UTF-16` to be added to the `Driver` section of either `/etc/vertica.ini` or `$HOME/.vertica.ini`.

## [Examples](vertica_configuration_module.md#id6)

```yaml+jinja
- name: Updating load_balance_policy
  community.general.vertica_configuration: name=failovertostandbyafter value='8 hours'
```

### Authors

- Dariusz Owczarek (@dareko)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
