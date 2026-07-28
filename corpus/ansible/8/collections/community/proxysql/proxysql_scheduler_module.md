---
collection: ansible
version: "8"
title: "community.proxysql.proxysql_scheduler module – Adds or removes schedules from proxysql admin interface"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/proxysql/proxysql_scheduler_module.html
fetched_at: 2026-07-28T01:58:47+00:00
---
# community.proxysql.proxysql_scheduler module – Adds or removes schedules from proxysql admin interface

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
> see [Requirements](proxysql_scheduler_module.md#ansible-collections-community-proxysql-proxysql-scheduler-module-requirements) for details.
>
> To use it in a playbook, specify: `community.proxysql.proxysql_scheduler`.

- [Synopsis](proxysql_scheduler_module.md#synopsis)
- [Requirements](proxysql_scheduler_module.md#requirements)
- [Parameters](proxysql_scheduler_module.md#parameters)
- [Notes](proxysql_scheduler_module.md#notes)
- [Examples](proxysql_scheduler_module.md#examples)
- [Return Values](proxysql_scheduler_module.md#return-values)

## [Synopsis](proxysql_scheduler_module.md#id1)

- The [community.proxysql.proxysql_scheduler](proxysql_scheduler_module.md#ansible-collections-community-proxysql-proxysql-scheduler-module) module adds or removes schedules using the proxysql admin interface.

## [Requirements](proxysql_scheduler_module.md#id2)

The below requirements are needed on the host that executes this module.

- PyMySQL
- mysqlclient

## [Parameters](proxysql_scheduler_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | A schedule with *active* set to `False` will be tracked in the database, but will be never loaded in the in-memory data structures.  **Choices:**   - `false` - `true` ← (default) |
| **arg1**  string | Argument that can be passed to the job. |
| **arg2**  string | Argument that can be passed to the job. |
| **arg3**  string | Argument that can be passed to the job. |
| **arg4**  string | Argument that can be passed to the job. |
| **arg5**  string | Argument that can be passed to the job. |
| **comment**  string | Text field that can be used for any purposed defined by the user. |
| **config_file**  path | Specify a config file from which *login_user* and *login_password* are to be read.  **Default:** `""` |
| **filename**  string / required | Full path of the executable to be executed. |
| **force_delete**  boolean | By default we avoid deleting more than one schedule in a single batch, however if you need this behaviour and you are not concerned about the schedules deleted, you can set *force_delete* to `True`.  **Choices:**   - `false` ← (default) - `true` |
| **interval_ms**  integer | How often (in millisecond) the job will be started. The minimum value for *interval_ms* is 100 milliseconds.  **Default:** `10000` |
| **load_to_runtime**  boolean | Dynamically load config to runtime memory.  **Choices:**   - `false` - `true` ← (default) |
| **login_host**  string | The host used to connect to ProxySQL admin interface.  **Default:** `"127.0.0.1"` |
| **login_password**  string | The password used to authenticate to ProxySQL admin interface. |
| **login_port**  integer | The port used to connect to ProxySQL admin interface.  **Default:** `6032` |
| **login_unix_socket**  string | The socket used to connect to ProxySQL admin interface. |
| **login_user**  string | The username used to authenticate to ProxySQL admin interface. |
| **save_to_disk**  boolean | Save config to sqlite db on disk to persist the configuration.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | When `present` - adds the schedule, when `absent` - removes the schedule.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](proxysql_scheduler_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](proxysql_scheduler_module.md#id5)

```yaml+jinja
---
# This example adds a schedule, it saves the scheduler config to disk, but
# avoids loading the scheduler config to runtime (this might be because
# several servers are being added and the user wants to push the config to
# runtime in a single batch using the community.general.proxysql_manage_config
# module).  It uses supplied credentials to connect to the proxysql admin
# interface.

- name: Add a schedule
  community.proxysql.proxysql_scheduler:
    login_user: 'admin'
    login_password: 'admin'
    interval_ms: 1000
    filename: "/opt/maintenance.py"
    state: present
    load_to_runtime: false

# This example removes a schedule, saves the scheduler config to disk, and
# dynamically loads the scheduler config to runtime.  It uses credentials
# in a supplied config file to connect to the proxysql admin interface.

- name: Remove a schedule
  community.proxysql.proxysql_scheduler:
    config_file: '~/proxysql.cnf'
    filename: "/opt/old_script.py"
    state: absent
```

## [Return Values](proxysql_scheduler_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stdout**  dictionary | The schedule modified or removed from proxysql.  **Returned:** On create/update will return the newly modified schedule, on delete it will return the deleted record.  **Sample:** `{"changed": true, "filename": "/opt/test.py", "msg": "Added schedule to scheduler", "schedules": [{"active": "1", "arg1": null, "arg2": null, "arg3": null, "arg4": null, "arg5": null, "comment": "", "filename": "/opt/test.py", "id": "1", "interval_ms": "10000"}], "state": "present"}` |

### Authors

- Ben Mildren (@bmildren)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.proxysql/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.proxysql)
