---
collection: ansible
version: "8"
title: "community.proxysql.proxysql_mysql_users module – Adds or removes mysql users from proxysql admin interface"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/proxysql/proxysql_mysql_users_module.html
fetched_at: 2026-07-28T01:58:44+00:00
---
# community.proxysql.proxysql_mysql_users module – Adds or removes mysql users from proxysql admin interface

> **Note:**
>
> This module is part of the [community.proxysql collection](https://galaxy.ansible.com/ui/repo/published/community/proxysql/) (version 1.5.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.proxysql`.
> You need further requirements to be able to use this module,
> see [Requirements](proxysql_mysql_users_module.md#ansible-collections-community-proxysql-proxysql-mysql-users-module-requirements) for details.
>
> To use it in a playbook, specify: `community.proxysql.proxysql_mysql_users`.

- [Synopsis](proxysql_mysql_users_module.md#synopsis)
- [Requirements](proxysql_mysql_users_module.md#requirements)
- [Parameters](proxysql_mysql_users_module.md#parameters)
- [Notes](proxysql_mysql_users_module.md#notes)
- [Examples](proxysql_mysql_users_module.md#examples)
- [Return Values](proxysql_mysql_users_module.md#return-values)

## [Synopsis](proxysql_mysql_users_module.md#id1)

- The [community.proxysql.proxysql_mysql_users](proxysql_mysql_users_module.md#ansible-collections-community-proxysql-proxysql-mysql-users-module) module adds or removes mysql users using the proxysql admin interface.

## [Requirements](proxysql_mysql_users_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyMySQL
- mysqlclient

## [Parameters](proxysql_mysql_users_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | A user with *active* set to `False` will be tracked in the database, but will be never loaded in the in-memory data structures. If omitted the proxysql database default for *active* is `True`.  **Choices:**   - `false` - `true` |
| **backend**  boolean | If *backend* is set to `True`, this (username, password) pair is used for authenticating to the ProxySQL instance.  **Choices:**   - `false` - `true` ← (default) |
| **config_file**  path | Specify a config file from which *login_user* and *login_password* are to be read.  **Default:** `""` |
| **default_hostgroup**  integer | If there is no matching rule for the queries sent by this user, the traffic it generates is sent to the specified hostgroup. If omitted the proxysql database default for *use_ssl* is 0. |
| **default_schema**  string | The schema to which the connection should change to by default. |
| **encrypt_password**  boolean | Encrypt a cleartext password passed in the *password* option, using the method defined in *encryption_method*.  **Choices:**   - `false` ← (default) - `true` |
| **encryption_method**  string | Encryption method used when *encrypt_password* is set to `True`.  **Choices:**   - `"mysql_native_password"` ← (default) |
| **fast_forward**  boolean | If *fast_forward* is set to `True`, *fast_forward* will bypass the query processing layer (rewriting, caching) and pass through the query directly as is to the backend server. If omitted the proxysql database default for *fast_forward* is `False`.  **Choices:**   - `false` - `true` |
| **frontend**  boolean | If *frontend* is set to `True`, this (username, password) pair is used for authenticating to the mysqld servers against any hostgroup.  **Choices:**   - `false` - `true` ← (default) |
| **load_to_runtime**  boolean | Dynamically load config to runtime memory.  **Choices:**   - `false` - `true` ← (default) |
| **login_host**  string | The host used to connect to ProxySQL admin interface.  **Default:** `"127.0.0.1"` |
| **login_password**  string | The password used to authenticate to ProxySQL admin interface. |
| **login_port**  integer | The port used to connect to ProxySQL admin interface.  **Default:** `6032` |
| **login_unix_socket**  string | The socket used to connect to ProxySQL admin interface. |
| **login_user**  string | The username used to authenticate to ProxySQL admin interface. |
| **max_connections**  integer | The maximum number of connections ProxySQL will open to the backend for this user. If omitted the proxysql database default for *max_connections* is 10000. |
| **password**  string | Password of the user connecting to the mysqld or ProxySQL instance. |
| **save_to_disk**  boolean | Save config to sqlite db on disk to persist the configuration.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | When `present` - adds the user, when `absent` - removes the user.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **transaction_persistent**  boolean | If this is set for the user with which the MySQL client is connecting to ProxySQL (thus a “frontend” user), transactions started within a hostgroup will remain within that hostgroup regardless of any other rules. If omitted the proxysql database default for *transaction_persistent* is `False`.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If *use_ssl* is set to `True`, connections by this user will be made using SSL connections. If omitted the proxysql database default for *use_ssl* is `False`.  **Choices:**   - `false` - `true` |
| **username**  string / required | Name of the user connecting to the mysqld or ProxySQL instance. |

## [Notes](proxysql_mysql_users_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](proxysql_mysql_users_module.md#id5)

```yaml+jinja
---
# This example adds a user, it saves the mysql user config to disk, but
# avoids loading the mysql user config to runtime (this might be because
# several users are being added and the user wants to push the config to
# runtime in a single batch using the community.general.proxysql_manage_config
# module).  It uses supplied credentials to connect to the proxysql admin
# interface.

- name: Add a user
  community.proxysql.proxysql_mysql_users:
    login_user: 'admin'
    login_password: 'admin'
    username: 'productiondba'
    state: present
    load_to_runtime: false

# This example removes a user, saves the mysql user config to disk, and
# dynamically loads the mysql user config to runtime.  It uses credentials
# in a supplied config file to connect to the proxysql admin interface.

- name: Remove a user
  community.proxysql.proxysql_mysql_users:
    config_file: '~/proxysql.cnf'
    username: 'mysqlboy'
    state: absent
```

## [Return Values](proxysql_mysql_users_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stdout**  dictionary | The mysql user modified or removed from proxysql.  **Returned:** On create/update will return the newly modified user, on delete it will return the deleted record.  **Sample:** `{"changed": true, "msg": "Added user to mysql_users", "state": "present", "user": {"active": 1, "backend": 1, "default_hostgroup": 1, "default_schema": null, "fast_forward": 0, "frontend": 1, "max_connections": 10000, "password": "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER", "schema_locked": 0, "transaction_persistent": 0, "use_ssl": 0, "username": "guest_ro"}, "username": "guest_ro"}` |

### Authors

- Ben Mildren (@bmildren)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.proxysql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.proxysql)
