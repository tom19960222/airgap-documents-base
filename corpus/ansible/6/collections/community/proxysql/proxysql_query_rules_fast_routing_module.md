---
collection: ansible
version: "6"
title: "community.proxysql.proxysql_query_rules_fast_routing module – Modifies query rules for fast routing policies using the proxysql admin interface"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/proxysql/proxysql_query_rules_fast_routing_module.html
fetched_at: 2026-07-27T17:20:37+00:00
---
# community.proxysql.proxysql_query_rules_fast_routing module – Modifies query rules for fast routing policies using the proxysql admin interface

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
> see [Requirements](proxysql_query_rules_fast_routing_module.md#ansible-collections-community-proxysql-proxysql-query-rules-fast-routing-module-requirements) for details.
>
> To use it in a playbook, specify: `community.proxysql.proxysql_query_rules_fast_routing`.

New in community.proxysql 1.1.0

- [Synopsis](proxysql_query_rules_fast_routing_module.md#synopsis)
- [Requirements](proxysql_query_rules_fast_routing_module.md#requirements)
- [Parameters](proxysql_query_rules_fast_routing_module.md#parameters)
- [Notes](proxysql_query_rules_fast_routing_module.md#notes)
- [Examples](proxysql_query_rules_fast_routing_module.md#examples)
- [Return Values](proxysql_query_rules_fast_routing_module.md#return-values)

## [Synopsis](proxysql_query_rules_fast_routing_module.md#id1)

- The [community.proxysql.proxysql_query_rules_fast_routing](proxysql_query_rules_fast_routing_module.md#ansible-collections-community-proxysql-proxysql-query-rules-fast-routing-module) module modifies query rules for fast routing policies and attributes using the proxysql admin interface.

## [Requirements](proxysql_query_rules_fast_routing_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyMySQL
- mysqlclient

## [Parameters](proxysql_query_rules_fast_routing_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comment**  string | Free form text field, usable for a descriptive comment of the query rule.  Default: `""` |
| **config_file**  path | Specify a config file from which *login_user* and *login_password* are to be read.  Default: `""` |
| **destination_hostgroup**  integer / required | Route matched queries to this hostgroup. This happens unless there is a started transaction and the logged in user has *transaction_persistent* set to `True` (refer to [community.proxysql.proxysql_mysql_users](proxysql_mysql_users_module.md#ansible-collections-community-proxysql-proxysql-mysql-users-module)). |
| **flagIN**  integer | Evaluated in the same way as *flagIN* is in **mysql_query_rules** and correlates to the *flagOUT/apply* specified in the **mysql_query_rules** table. (see [community.proxysql.proxysql_query_rules](proxysql_query_rules_module.md#ansible-collections-community-proxysql-proxysql-query-rules-module)).  Default: `0` |
| **force_delete**  boolean | By default, we avoid deleting more than one schedule in a single batch; however, if you need this behaviour and you are not concerned about the schedules deleted, you can set *force_delete* to `True`.  Choices:   - `false` ← (default) - `true` |
| **load_to_runtime**  boolean | Dynamically load config to runtime memory.  Choices:   - `false` - `true` ← (default) |
| **login_host**  string | The host used to connect to ProxySQL admin interface.  Default: `"127.0.0.1"` |
| **login_password**  string | The password used to authenticate to ProxySQL admin interface. |
| **login_port**  integer | The port used to connect to ProxySQL admin interface.  Default: `6032` |
| **login_unix_socket**  string | The socket used to connect to ProxySQL admin interface. |
| **login_user**  string | The username used to authenticate to ProxySQL admin interface. |
| **save_to_disk**  boolean | Save config to sqlite db on disk to persist the configuration.  Choices:   - `false` - `true` ← (default) |
| **schemaname**  string / required | Filtering criteria matching schemaname, a query will match only if the connection uses schemaname as its default schema. |
| **state**  string | When `present`, adds the rule. When `absent`, removes the rule.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Filtering criteria matching username, a query will match only if the connection is made with the correct username. |

## [Notes](proxysql_query_rules_fast_routing_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](proxysql_query_rules_fast_routing_module.md#id5)

```yaml+jinja
---
# This example adds a rule for fast routing
- name: Add a rule
  community.proxysql.proxysql_query_rules_fast_routing:
    login_user: admin
    login_password: admin
    username: 'user_ro'
    schemaname: 'default'
    destination_hostgroup: 1
    comment: 'fast route user_ro to default schema'
    state: present
    save_to_disk: yes
    load_to_runtime: yes
```

## [Return Values](proxysql_query_rules_fast_routing_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stdout**  dictionary | The mysql user modified or removed from proxysql.  Returned: On create/update will return the newly modified rule, in all other cases will return a list of rules that match the supplied criteria.  Sample: `{"changed": true, "msg": "Added rule to mysql_query_rules_fast_routing", "rules": [{"comment": "", "destination_hostgroup": 1, "flagIN": "0", "schemaname": "default", "username": "user_ro"}], "state": "present"}` |

### Authors

- Akim Lindberg (@akimrx)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.proxysql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.proxysql)
