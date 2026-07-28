---
collection: ansible
version: "6"
title: "community.general.cgroup_memory_recap callback – Profiles maximum memory usage of tasks and full execution using cgroups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/cgroup_memory_recap_callback.html
fetched_at: 2026-07-27T17:14:24+00:00
---
# community.general.cgroup_memory_recap callback – Profiles maximum memory usage of tasks and full execution using cgroups

> **Note:**
>
> This callback plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](cgroup_memory_recap_callback.md#ansible-collections-community-general-cgroup-memory-recap-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.cgroup_memory_recap`.

- [Callback plugin](cgroup_memory_recap_callback.md#callback-plugin)
- [Synopsis](cgroup_memory_recap_callback.md#synopsis)
- [Requirements](cgroup_memory_recap_callback.md#requirements)
- [Parameters](cgroup_memory_recap_callback.md#parameters)
- [Notes](cgroup_memory_recap_callback.md#notes)

## [Callback plugin](cgroup_memory_recap_callback.md#id1)

This plugin is an **aggregate callback**. It adds additional console output next to the configured stdout callback.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](cgroup_memory_recap_callback.md#id2)

- This is an ansible callback plugin that profiles maximum memory usage of ansible and individual tasks, and displays a recap at the end using cgroups

## [Requirements](cgroup_memory_recap_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelist in configuration
- cgroups

## [Parameters](cgroup_memory_recap_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **cur_mem_file**  string / required | Path to `memory.usage_in_bytes` file. Example `/sys/fs/cgroup/memory/ansible_profile/memory.usage_in_bytes`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_cgroupmemrecap]   cur_mem_file = VALUE   ``` - Environment variable: [`CGROUP_CUR_MEM_FILE`](../../environment_variables.md#envvar-CGROUP_CUR_MEM_FILE) |
| **max_mem_file**  string / required | Path to cgroups `memory.max_usage_in_bytes` file. Example `/sys/fs/cgroup/memory/ansible_profile/memory.max_usage_in_bytes`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_cgroupmemrecap]   max_mem_file = VALUE   ``` - Environment variable: [`CGROUP_MAX_MEM_FILE`](../../environment_variables.md#envvar-CGROUP_MAX_MEM_FILE) |

## [Notes](cgroup_memory_recap_callback.md#id5)

> **Note:**
>
> - Requires ansible to be run from within a cgroup, such as with `cgexec -g memory:ansible_profile ansible-playbook ...`
> - This cgroup should only be used by ansible to get accurate results
> - To create the cgroup, first use a command such as `sudo cgcreate -a ec2-user:ec2-user -t ec2-user:ec2-user -g memory:ansible_profile`

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
