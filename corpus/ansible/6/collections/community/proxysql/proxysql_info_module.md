---
collection: ansible
version: "6"
title: "community.proxysql.proxysql_info module – Gathers information about proxysql server"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/proxysql/proxysql_info_module.html
fetched_at: 2026-07-27T17:20:34+00:00
---
# community.proxysql.proxysql_info module – Gathers information about proxysql server

> **Note:**
>
> This module is part of the [community.proxysql collection](https://galaxy.ansible.com/community/proxysql) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.proxysql`.
> You need further requirements to be able to use this module,
> see [Requirements](proxysql_info_module.md#ansible-collections-community-proxysql-proxysql-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.proxysql.proxysql_info`.

New in community.proxysql 1.2.0

- [Synopsis](proxysql_info_module.md#synopsis)
- [Requirements](proxysql_info_module.md#requirements)
- [Parameters](proxysql_info_module.md#parameters)
- [Notes](proxysql_info_module.md#notes)
- [Examples](proxysql_info_module.md#examples)
- [Return Values](proxysql_info_module.md#return-values)

## [Synopsis](proxysql_info_module.md#id1)

- Gathers information about proxysql server.
- Caution. The number of tables that returns, depends on the underlying proyxsql server version.

## [Requirements](proxysql_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyMySQL
- mysqlclient

## [Parameters](proxysql_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config_file**  path | Specify a config file from which *login_user* and *login_password* are to be read.  Default: `""` |
| **login_host**  string | The host used to connect to ProxySQL admin interface.  Default: `"127.0.0.1"` |
| **login_password**  string | The password used to authenticate to ProxySQL admin interface. |
| **login_port**  integer | The port used to connect to ProxySQL admin interface.  Default: `6032` |
| **login_unix_socket**  string | The socket used to connect to ProxySQL admin interface. |
| **login_user**  string | The username used to authenticate to ProxySQL admin interface. |

## [Notes](proxysql_info_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](proxysql_info_module.md#id5)

```yaml+jinja
- name: Receive information about proxysql setup
  community.proxysql.proxysql_info:
    login_user: admin
    login_password: admin
```

## [Return Values](proxysql_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stdout**  dictionary | The number of tables that returns, depends on the underlying proyxsql server version.  Returned: Always  Sample: `{"changed": false, "failed": false, "global_variables": {"description": "Global variables of requested proxysql.", "returned": "Always", "type": "dict"}, "tables": {"description": "List of tables that exist in the requested proxysql version.", "returned": "Always", "sample": ["global_variables", "mysql_aws_aurora_hostgroups", "mysql_collations", "mysql_firewall_whitelist_rules", "mysql_firewall_whitelist_sqli_fingerprints", "mysql_firewall_whitelist_users", "mysql_galera_hostgroups", "mysql_group_replication_hostgroups", "mysql_query_rules", "mysql_query_rules_fast_routing", "mysql_replication_hostgroups", "mysql_servers", "mysql_users", "proxysql_servers", "restapi_routes", "runtime_checksums_values", "runtime_global_variables", "runtime_mysql_aws_aurora_hostgroups", "runtime_mysql_firewall_whitelist_rules", "runtime_mysql_firewall_whitelist_sqli_fingerprints", "runtime_mysql_firewall_whitelist_users", "runtime_mysql_galera_hostgroups", "runtime_mysql_group_replication_hostgroups", "runtime_mysql_query_rules", "runtime_mysql_query_rules_fast_routing", "runtime_mysql_replication_hostgroups", "runtime_mysql_servers", "runtime_mysql_users", "runtime_proxysql_servers", "runtime_restapi_routes", "runtime_scheduler", "scheduler"], "type": "list"}, "version": {"description": "Version of proxysql.", "returned": "Always", "sample": {"full": "2.1.1-40-g1c2b7e4", "major": 2, "minor": 1, "release": 1, "suffix": 40}, "type": "dict"}}` |

### Authors

- Markus Bergholz (@markuman)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.proxysql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.proxysql)
