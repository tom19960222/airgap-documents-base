---
collection: ansible
version: "6"
title: "ansible.posix.profile_tasks callback – adds time information to tasks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/posix/profile_tasks_callback.html
fetched_at: 2026-07-27T16:44:46+00:00
---
# ansible.posix.profile_tasks callback – adds time information to tasks

> **Note:**
>
> This callback plugin is part of the [ansible.posix collection](https://galaxy.ansible.com/ansible/posix) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](profile_tasks_callback.md#ansible-collections-ansible-posix-profile-tasks-callback-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.profile_tasks`.

- [Callback plugin](profile_tasks_callback.md#callback-plugin)
- [Synopsis](profile_tasks_callback.md#synopsis)
- [Requirements](profile_tasks_callback.md#requirements)
- [Parameters](profile_tasks_callback.md#parameters)
- [Examples](profile_tasks_callback.md#examples)

## [Callback plugin](profile_tasks_callback.md#id1)

This plugin is an **aggregate callback**. It adds additional console output next to the configured stdout callback.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](profile_tasks_callback.md#id2)

- Ansible callback plugin for timing individual tasks and overall execution time.
- Mashup of 2 excellent original works: <https://github.com/jlafon/ansible-profile>, <https://github.com/junaid18183/ansible_home/blob/master/ansible_plugins/callback_plugins/timestamp.py.old>
- Format: `<task start timestamp> (<length of previous task>` <current elapsed playbook execution time>)
- It also lists the top/bottom time consuming tasks in the summary (configurable)
- Before 2.4 only the environment variables were available for configuration.

## [Requirements](profile_tasks_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelisting in configuration - see examples section below for details.

## [Parameters](profile_tasks_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **output_limit**  string | Number of tasks to display in the summary  Default: `20`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_profile_tasks]   task_output_limit = 20   ``` - Environment variable: [`PROFILE_TASKS_TASK_OUTPUT_LIMIT`](../../environment_variables.md#envvar-PROFILE_TASKS_TASK_OUTPUT_LIMIT) |
| **sort_order**  string | Adjust the sorting output of summary tasks  Choices:   - `"descending"` ← (default) - `"ascending"` - `"none"`   Configuration:   - INI entry:  ```YAML+Jinja   [callback_profile_tasks]   sort_order = descending   ``` - Environment variable: [`PROFILE_TASKS_SORT_ORDER`](../../environment_variables.md#envvar-PROFILE_TASKS_SORT_ORDER) |

## [Examples](profile_tasks_callback.md#id5)

```yaml+jinja
example: >
  To enable, add this to your ansible.cfg file in the defaults block
    [defaults]
    callback_whitelist = ansible.posix.profile_tasks
sample output: >
#
#    TASK: [ensure messaging security group exists] ********************************
#    Thursday 11 June 2017  22:50:53 +0100 (0:00:00.721)       0:00:05.322 *********
#    ok: [localhost]
#
#    TASK: [ensure db security group exists] ***************************************
#    Thursday 11 June 2017  22:50:54 +0100 (0:00:00.558)       0:00:05.880 *********
#    changed: [localhost]
#
```

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.posix)
[Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
