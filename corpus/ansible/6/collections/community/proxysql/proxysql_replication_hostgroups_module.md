---
collection: ansible
version: "6"
title: "community.proxysql.proxysql_replication_hostgroups module – Manages replication hostgroups using the proxysql admin interface"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/proxysql/proxysql_replication_hostgroups_module.html
fetched_at: 2026-07-27T17:20:38+00:00
---
# community.proxysql.proxysql_replication_hostgroups module – Manages replication hostgroups using the proxysql admin interface

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
> see [Requirements](proxysql_replication_hostgroups_module.md#ansible-collections-community-proxysql-proxysql-replication-hostgroups-module-requirements) for details.
>
> To use it in a playbook, specify: `community.proxysql.proxysql_replication_hostgroups`.

- [Synopsis](proxysql_replication_hostgroups_module.md#synopsis)
- [Requirements](proxysql_replication_hostgroups_module.md#requirements)
- [Parameters](proxysql_replication_hostgroups_module.md#parameters)
- [Notes](proxysql_replication_hostgroups_module.md#notes)
- [Examples](proxysql_replication_hostgroups_module.md#examples)
- [Return Values](proxysql_replication_hostgroups_module.md#return-values)

## [Synopsis](proxysql_replication_hostgroups_module.md#id1)

- Each row in mysql_replication_hostgroups represent a pair of writer_hostgroup and reader_hostgroup. ProxySQL will monitor the value of read_only for all the servers in specified hostgroups, and based on the value of read_only will assign the server to the writer or reader hostgroups.

## [Requirements](proxysql_replication_hostgroups_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyMySQL
- mysqlclient

## [Parameters](proxysql_replication_hostgroups_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **check_type**  string  added in community.proxysql 1.3.0 | Which check type to use when detecting that the node is a standby.  Requires proxysql >= 2.0.1. Otherwise it has no effect.  `read_only|innodb_read_only` and `read_only&innodb_read_only` requires proxysql >= 2.0.8.  Choices:   - `"read_only"` ← (default) - `"innodb_read_only"` - `"super_read_only"` - `"read_only|innodb_read_only"` - `"read_only&innodb_read_only"` |
| **comment**  string | Text field that can be used for any purposes defined by the user.  Default: `""` |
| **config_file**  path | Specify a config file from which *login_user* and *login_password* are to be read.  Default: `""` |
| **load_to_runtime**  boolean | Dynamically load config to runtime memory.  Choices:   - `false` - `true` ← (default) |
| **login_host**  string | The host used to connect to ProxySQL admin interface.  Default: `"127.0.0.1"` |
| **login_password**  string | The password used to authenticate to ProxySQL admin interface. |
| **login_port**  integer | The port used to connect to ProxySQL admin interface.  Default: `6032` |
| **login_unix_socket**  string | The socket used to connect to ProxySQL admin interface. |
| **login_user**  string | The username used to authenticate to ProxySQL admin interface. |
| **reader_hostgroup**  integer / required | Id of the reader hostgroup. |
| **save_to_disk**  boolean | Save config to sqlite db on disk to persist the configuration.  Choices:   - `false` - `true` ← (default) |
| **state**  string | When `present` - adds the replication hostgroup, when `absent` - removes the replication hostgroup.  Choices:   - `"present"` ← (default) - `"absent"` |
| **writer_hostgroup**  integer / required | Id of the writer hostgroup. |

## [Notes](proxysql_replication_hostgroups_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](proxysql_replication_hostgroups_module.md#id5)

```yaml+jinja
---
# This example adds a replication hostgroup, it saves the mysql server config
# to disk, but avoids loading the mysql server config to runtime (this might be
# because several replication hostgroup are being added and the user wants to
# push the config to runtime in a single batch using the
# community.general.proxysql_manage_config module).  It uses supplied credentials
# to connect to the proxysql admin interface.

- name: Add a replication hostgroup
  community.proxysql.proxysql_replication_hostgroups:
    login_user: 'admin'
    login_password: 'admin'
    writer_hostgroup: 1
    reader_hostgroup: 2
    state: present
    load_to_runtime: False

- name: Change check_type
  community.proxysql.proxysql_replication_hostgroups:
    login_user: 'admin'
    login_password: 'admin'
    writer_hostgroup: 1
    reader_hostgroup: 2
    check_type: innodb_read_only
    state: present
    load_to_runtime: False

# This example removes a replication hostgroup, saves the mysql server config
# to disk, and dynamically loads the mysql server config to runtime.  It uses
# credentials in a supplied config file to connect to the proxysql admin
# interface.

- name: Remove a replication hostgroup
  community.proxysql.proxysql_replication_hostgroups:
    config_file: '~/proxysql.cnf'
    writer_hostgroup: 3
    reader_hostgroup: 4
    state: absent
```

## [Return Values](proxysql_replication_hostgroups_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stdout**  dictionary | The replication hostgroup modified or removed from proxysql.  Returned: On create/update will return the newly modified group, on delete it will return the deleted record.  Sample: `{"changed": true, "msg": "Added server to mysql_hosts", "repl_group": {"check_type": "read_only", "comment": "", "reader_hostgroup": "1", "writer_hostgroup": "2"}, "state": "present"}` |

### Authors

- Ben Mildren (@bmildren)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.proxysql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.proxysql)
