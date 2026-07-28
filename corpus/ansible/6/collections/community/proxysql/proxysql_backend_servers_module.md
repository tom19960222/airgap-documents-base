---
collection: ansible
version: "6"
title: "community.proxysql.proxysql_backend_servers module – Adds or removes mysql hosts from proxysql admin interface"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/proxysql/proxysql_backend_servers_module.html
fetched_at: 2026-07-27T17:20:33+00:00
---
# community.proxysql.proxysql_backend_servers module – Adds or removes mysql hosts from proxysql admin interface

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
> see [Requirements](proxysql_backend_servers_module.md#ansible-collections-community-proxysql-proxysql-backend-servers-module-requirements) for details.
>
> To use it in a playbook, specify: `community.proxysql.proxysql_backend_servers`.

- [Synopsis](proxysql_backend_servers_module.md#synopsis)
- [Requirements](proxysql_backend_servers_module.md#requirements)
- [Parameters](proxysql_backend_servers_module.md#parameters)
- [Notes](proxysql_backend_servers_module.md#notes)
- [Examples](proxysql_backend_servers_module.md#examples)
- [Return Values](proxysql_backend_servers_module.md#return-values)

## [Synopsis](proxysql_backend_servers_module.md#id1)

- The [community.proxysql.proxysql_backend_servers](proxysql_backend_servers_module.md#ansible-collections-community-proxysql-proxysql-backend-servers-module) module adds or removes mysql hosts using the proxysql admin interface.

## [Requirements](proxysql_backend_servers_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyMySQL
- mysqlclient

## [Parameters](proxysql_backend_servers_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comment**  string | Text field that can be used for any purposed defined by the user. Could be a description of what the host stores, a reminder of when the host was added or disabled, or a JSON processed by some checker script.  Default: `""` |
| **compression**  integer | If the value of *compression* is greater than 0, new connections to that server will use compression. If omitted the proxysql database default for *compression* is 0. |
| **config_file**  path | Specify a config file from which *login_user* and *login_password* are to be read.  Default: `""` |
| **hostgroup_id**  integer | The hostgroup in which this mysqld instance is included. An instance can be part of one or more hostgroups.  Default: `0` |
| **hostname**  string / required | The ip address at which the mysqld instance can be contacted. |
| **load_to_runtime**  boolean | Dynamically load config to runtime memory.  Choices:   - `false` - `true` ← (default) |
| **login_host**  string | The host used to connect to ProxySQL admin interface.  Default: `"127.0.0.1"` |
| **login_password**  string | The password used to authenticate to ProxySQL admin interface. |
| **login_port**  integer | The port used to connect to ProxySQL admin interface.  Default: `6032` |
| **login_unix_socket**  string | The socket used to connect to ProxySQL admin interface. |
| **login_user**  string | The username used to authenticate to ProxySQL admin interface. |
| **max_connections**  integer | The maximum number of connections ProxySQL will open to this backend server. If omitted the proxysql database default for *max_connections* is 1000. |
| **max_latency_ms**  integer | Ping time is monitored regularly. If a host has a ping time greater than *max_latency_ms* it is excluded from the connection pool (although the server stays ONLINE). If omitted the proxysql database default for *max_latency_ms* is 0. |
| **max_replication_lag**  integer | If greater than 0, ProxySQL will regularly monitor replication lag. If replication lag goes above *max_replication_lag*, proxysql will temporarily shun the server until replication catches up. If omitted the proxysql database default for *max_replication_lag* is 0. |
| **port**  integer | The port at which the mysqld instance can be contacted.  Default: `3306` |
| **save_to_disk**  boolean | Save config to sqlite db on disk to persist the configuration.  Choices:   - `false` - `true` ← (default) |
| **state**  string | When `present` - adds the host, when `absent` - removes the host.  Choices:   - `"present"` ← (default) - `"absent"` |
| **status**  string | ONLINE - Backend server is fully operational. OFFLINE_SOFT - When a server is put into `OFFLINE_SOFT` mode, connections are kept in use until the current transaction is completed. This allows to gracefully detach a backend. OFFLINE_HARD - When a server is put into `OFFLINE_HARD` mode, the existing connections are dropped, while new incoming connections aren’t accepted either.  If omitted the proxysql database default for *status* is `ONLINE`.  Choices:   - `"ONLINE"` - `"OFFLINE_SOFT"` - `"OFFLINE_HARD"` |
| **use_ssl**  boolean | If *use_ssl* is set to `True`, connections to this server will be made using SSL connections. If omitted the proxysql database default for *use_ssl* is `False`.  Choices:   - `false` - `true` |
| **weight**  integer | The bigger the weight of a server relative to other weights, the higher the probability of the server being chosen from the hostgroup. If omitted the proxysql database default for *weight* is 1. |

## [Notes](proxysql_backend_servers_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](proxysql_backend_servers_module.md#id5)

```yaml+jinja
---
# This example adds a server, it saves the mysql server config to disk, but
# avoids loading the mysql server config to runtime (this might be because
# several servers are being added and the user wants to push the config to
# runtime in a single batch using the community.general.proxysql_manage_config
# module).  It uses supplied credentials to connect to the proxysql admin
# interface.

- name: Add a server
  community.proxysql.proxysql_backend_servers:
    login_user: 'admin'
    login_password: 'admin'
    hostname: 'mysql01'
    state: present
    load_to_runtime: False

# This example removes a server, saves the mysql server config to disk, and
# dynamically loads the mysql server config to runtime.  It uses credentials
# in a supplied config file to connect to the proxysql admin interface.

- name: Remove a server
  community.proxysql.proxysql_backend_servers:
    config_file: '~/proxysql.cnf'
    hostname: 'mysql02'
    state: absent
```

## [Return Values](proxysql_backend_servers_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stdout**  dictionary | The mysql host modified or removed from proxysql  Returned: On create/update will return the newly modified host, on delete it will return the deleted record.  Sample: `{"changed": true, "hostname": "192.168.52.1", "msg": "Added server to mysql_hosts", "server": {"comment": "", "compression": "0", "hostgroup_id": "1", "hostname": "192.168.52.1", "max_connections": "1000", "max_latency_ms": "0", "max_replication_lag": "0", "port": "3306", "status": "ONLINE", "use_ssl": "0", "weight": "1"}, "state": "present"}` |

### Authors

- Ben Mildren (@bmildren)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.proxysql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.proxysql)
