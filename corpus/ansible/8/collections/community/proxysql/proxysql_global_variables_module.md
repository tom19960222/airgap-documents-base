---
collection: ansible
version: "8"
title: "community.proxysql.proxysql_global_variables module – Gets or sets the proxysql global variables"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/proxysql/proxysql_global_variables_module.html
fetched_at: 2026-07-28T01:58:42+00:00
---
# community.proxysql.proxysql_global_variables module – Gets or sets the proxysql global variables

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
> see [Requirements](proxysql_global_variables_module.md#ansible-collections-community-proxysql-proxysql-global-variables-module-requirements) for details.
>
> To use it in a playbook, specify: `community.proxysql.proxysql_global_variables`.

- [Synopsis](proxysql_global_variables_module.md#synopsis)
- [Requirements](proxysql_global_variables_module.md#requirements)
- [Parameters](proxysql_global_variables_module.md#parameters)
- [Notes](proxysql_global_variables_module.md#notes)
- [Examples](proxysql_global_variables_module.md#examples)
- [Return Values](proxysql_global_variables_module.md#return-values)

## [Synopsis](proxysql_global_variables_module.md#id1)

- The [community.proxysql.proxysql_global_variables](proxysql_global_variables_module.md#ansible-collections-community-proxysql-proxysql-global-variables-module) module gets or sets the proxysql global variables.

## [Requirements](proxysql_global_variables_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyMySQL
- mysqlclient

## [Parameters](proxysql_global_variables_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config_file**  path | Specify a config file from which *login_user* and *login_password* are to be read.  **Default:** `""` |
| **load_to_runtime**  boolean | Dynamically load config to runtime memory.  **Choices:**   - `false` - `true` ← (default) |
| **login_host**  string | The host used to connect to ProxySQL admin interface.  **Default:** `"127.0.0.1"` |
| **login_password**  string | The password used to authenticate to ProxySQL admin interface. |
| **login_port**  integer | The port used to connect to ProxySQL admin interface.  **Default:** `6032` |
| **login_unix_socket**  string | The socket used to connect to ProxySQL admin interface. |
| **login_user**  string | The username used to authenticate to ProxySQL admin interface. |
| **save_to_disk**  boolean | Save config to sqlite db on disk to persist the configuration.  **Choices:**   - `false` - `true` ← (default) |
| **value**  string | Defines a value the variable specified using *variable* should be set to. |
| **variable**  string / required | Defines which variable should be returned, or if *value* is specified which variable should be updated. |

## [Notes](proxysql_global_variables_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](proxysql_global_variables_module.md#id5)

```yaml+jinja
---
# This example sets the value of a variable, saves the mysql admin variables
# config to disk, and dynamically loads the mysql admin variables config to
# runtime. It uses supplied credentials to connect to the proxysql admin
# interface.

- name: Set the value of a variable
  community.proxysql.proxysql_global_variables:
    login_user: 'admin'
    login_password: 'admin'
    variable: 'mysql-max_connections'
    value: 4096

# This example gets the value of a variable.  It uses credentials in a
# supplied config file to connect to the proxysql admin interface.

- name: Get the value of a variable
  community.proxysql.proxysql_global_variables:
    config_file: '~/proxysql.cnf'
    variable: 'mysql-default_query_delay'
```

## [Return Values](proxysql_global_variables_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stdout**  dictionary | Returns the mysql variable supplied with it’s associated value.  **Returned:** Returns the current variable and value, or the newly set value for the variable supplied..  **Sample:** `{"changed": false, "msg": "The variable is already been set to the supplied value", "var": {"variable_name": "mysql-poll_timeout", "variable_value": "3000"}}` |

### Authors

- Ben Mildren (@bmildren)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.proxysql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.proxysql)
