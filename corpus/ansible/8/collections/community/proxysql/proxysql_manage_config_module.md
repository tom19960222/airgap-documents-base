---
collection: ansible
version: "8"
title: "community.proxysql.proxysql_manage_config module – Writes the proxysql configuration settings between layers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/proxysql/proxysql_manage_config_module.html
fetched_at: 2026-07-28T01:58:44+00:00
---
# community.proxysql.proxysql_manage_config module – Writes the proxysql configuration settings between layers

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
> see [Requirements](proxysql_manage_config_module.md#ansible-collections-community-proxysql-proxysql-manage-config-module-requirements) for details.
>
> To use it in a playbook, specify: `community.proxysql.proxysql_manage_config`.

- [Synopsis](proxysql_manage_config_module.md#synopsis)
- [Requirements](proxysql_manage_config_module.md#requirements)
- [Parameters](proxysql_manage_config_module.md#parameters)
- [Notes](proxysql_manage_config_module.md#notes)
- [Examples](proxysql_manage_config_module.md#examples)
- [Return Values](proxysql_manage_config_module.md#return-values)

## [Synopsis](proxysql_manage_config_module.md#id1)

- The [community.proxysql.proxysql_global_variables](proxysql_global_variables_module.md#ansible-collections-community-proxysql-proxysql-global-variables-module) module writes the proxysql configuration settings between layers. Currently this module will always report a changed state, so should typically be used with WHEN however this will change in a future version when the CHECKSUM table commands are available for all tables in proxysql.

## [Requirements](proxysql_manage_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyMySQL
- mysqlclient

## [Parameters](proxysql_manage_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string / required | The supplied *action* combines with the supplied *direction* to provide the semantics of how we want to move the *config_settings* between the *config_layers*.  **Choices:**   - `"LOAD"` - `"SAVE"` |
| **config_file**  path | Specify a config file from which *login_user* and *login_password* are to be read.  **Default:** `""` |
| **config_layer**  string / required | RUNTIME - represents the in-memory data structures of ProxySQL used by the threads that are handling the requests. MEMORY - (sometimes also referred as main) represents the in-memory SQLite3 database. DISK - represents the on-disk SQLite3 database. CONFIG - is the classical config file. You can only LOAD FROM the config file.  **Choices:**   - `"MEMORY"` - `"DISK"` - `"RUNTIME"` - `"CONFIG"` |
| **config_settings**  string / required | The *config_settings* specifies which configuration we’re writing.  **Choices:**   - `"MYSQL USERS"` - `"MYSQL SERVERS"` - `"MYSQL QUERY RULES"` - `"MYSQL VARIABLES"` - `"ADMIN VARIABLES"` - `"SCHEDULER"` |
| **direction**  string / required | FROM - denotes we’re reading values FROM the supplied *config_layer* and writing to the next layer. TO - denotes we’re reading from the previous layer and writing TO the supplied *config_layer*.”  **Choices:**   - `"FROM"` - `"TO"` |
| **login_host**  string | The host used to connect to ProxySQL admin interface.  **Default:** `"127.0.0.1"` |
| **login_password**  string | The password used to authenticate to ProxySQL admin interface. |
| **login_port**  integer | The port used to connect to ProxySQL admin interface.  **Default:** `6032` |
| **login_unix_socket**  string | The socket used to connect to ProxySQL admin interface. |
| **login_user**  string | The username used to authenticate to ProxySQL admin interface. |

## [Notes](proxysql_manage_config_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](proxysql_manage_config_module.md#id5)

```yaml+jinja
---
# This example saves the mysql users config from memory to disk. It uses
# supplied credentials to connect to the proxysql admin interface.

- name: Save the mysql users config from memory to disk
  community.proxysql.proxysql_manage_config:
    login_user: 'admin'
    login_password: 'admin'
    action: "SAVE"
    config_settings: "MYSQL USERS"
    direction: "FROM"
    config_layer: "MEMORY"

# This example loads the mysql query rules config from memory to runtime. It
# uses supplied credentials to connect to the proxysql admin interface.

- name: Load the mysql query rules config from memory to runtime
  community.proxysql.proxysql_manage_config:
    config_file: '~/proxysql.cnf'
    action: "LOAD"
    config_settings: "MYSQL QUERY RULES"
    direction: "TO"
    config_layer: "RUNTIME"
```

## [Return Values](proxysql_manage_config_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stdout**  dictionary | Simply reports whether the action reported a change.  **Returned:** Currently the returned value with always be changed=True.  **Sample:** `{"changed": true}` |

### Authors

- Ben Mildren (@bmildren)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.proxysql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.proxysql)
