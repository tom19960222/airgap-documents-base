---
collection: ansible
version: "6"
title: "ansible.posix.cgroup_perf_recap callback – Profiles system activity of tasks and full execution using cgroups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/posix/cgroup_perf_recap_callback.html
fetched_at: 2026-07-27T16:44:45+00:00
---
# ansible.posix.cgroup_perf_recap callback – Profiles system activity of tasks and full execution using cgroups

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
> see [Requirements](cgroup_perf_recap_callback.md#ansible-collections-ansible-posix-cgroup-perf-recap-callback-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.cgroup_perf_recap`.

- [Callback plugin](cgroup_perf_recap_callback.md#callback-plugin)
- [Synopsis](cgroup_perf_recap_callback.md#synopsis)
- [Requirements](cgroup_perf_recap_callback.md#requirements)
- [Parameters](cgroup_perf_recap_callback.md#parameters)
- [Notes](cgroup_perf_recap_callback.md#notes)

## [Callback plugin](cgroup_perf_recap_callback.md#id1)

This plugin is an **aggregate callback**. It adds additional console output next to the configured stdout callback.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](cgroup_perf_recap_callback.md#id2)

- This is an ansible callback plugin utilizes cgroups to profile system activity of ansible and individual tasks, and display a recap at the end of the playbook execution

## [Requirements](cgroup_perf_recap_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelist in configuration
- cgroups

## [Parameters](cgroup_perf_recap_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **control_group**  string / required | Name of cgroups control group  Configuration:   - INI entry:  ```YAML+Jinja   [callback_cgroup_perf_recap]   control_group = VALUE   ``` - Environment variable: [`CGROUP_CONTROL_GROUP`](../../environment_variables.md#envvar-CGROUP_CONTROL_GROUP) |
| **cpu_poll_interval**  float | Interval between CPU polling for determining CPU usage. A lower value may produce inaccurate results, a higher value may not be short enough to collect results for short tasks.  Default: `0.25`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_cgroup_perf_recap]   cpu_poll_interval = 0.25   ``` - Environment variable: [`CGROUP_CPU_POLL_INTERVAL`](../../environment_variables.md#envvar-CGROUP_CPU_POLL_INTERVAL) |
| **display_recap**  boolean | Controls whether the recap is printed at the end, useful if you will automatically process the output files  Choices:   - `false` - `true` ← (default)   Configuration:   - INI entry:  ```YAML+Jinja   [callback_cgroup_perf_recap]   display_recap = true   ``` - Environment variable: [`CGROUP_DISPLAY_RECAP`](../../environment_variables.md#envvar-CGROUP_DISPLAY_RECAP) |
| **file_name_format**  string | Format of filename. Accepts `%(counter`s), `%(task_uuid`s), `%(feature`s), `%(ext`s). Defaults to `%(feature`s.%(ext)s) when `file_per_task` is `False` and `%(counter`s-%(task_uuid)s-%(feature)s.%(ext)s) when `True`  Default: `"%(feature)s.%(ext)s"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_cgroup_perf_recap]   file_name_format = %(feature)s.%(ext)s   ``` - Environment variable: [`CGROUP_FILE_NAME_FORMAT`](../../environment_variables.md#envvar-CGROUP_FILE_NAME_FORMAT) |
| **file_per_task**  boolean | When set as `True` along with `write_files`, this callback will write 1 file per task instead of 1 file for the entire playbook run  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [callback_cgroup_perf_recap]   file_per_task = false   ``` - Environment variable: [`CGROUP_FILE_PER_TASK`](../../environment_variables.md#envvar-CGROUP_FILE_PER_TASK) |
| **memory_poll_interval**  float | Interval between memory polling for determining memory usage. A lower value may produce inaccurate results, a higher value may not be short enough to collect results for short tasks.  Default: `0.25`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_cgroup_perf_recap]   memory_poll_interval = 0.25   ``` - Environment variable: [`CGROUP_MEMORY_POLL_INTERVAL`](../../environment_variables.md#envvar-CGROUP_MEMORY_POLL_INTERVAL) |
| **output_dir**  path | Output directory for files containing recorded performance readings. If the value contains a single %s, the start time of the playbook run will be inserted in that space. Only the deepest level directory will be created if it does not exist, parent directories will not be created.  Default: `"/tmp/ansible-perf-%s"`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_cgroup_perf_recap]   output_dir = /tmp/ansible-perf-%s   ``` - Environment variable: [`CGROUP_OUTPUT_DIR`](../../environment_variables.md#envvar-CGROUP_OUTPUT_DIR) |
| **output_format**  string | Output format, either CSV or JSON-seq  Choices:   - `"csv"` ← (default) - `"json"`   Configuration:   - INI entry:  ```YAML+Jinja   [callback_cgroup_perf_recap]   output_format = csv   ``` - Environment variable: [`CGROUP_OUTPUT_FORMAT`](../../environment_variables.md#envvar-CGROUP_OUTPUT_FORMAT) |
| **pid_poll_interval**  float | Interval between PID polling for determining PID count. A lower value may produce inaccurate results, a higher value may not be short enough to collect results for short tasks.  Default: `0.25`  Configuration:   - INI entry:  ```YAML+Jinja   [callback_cgroup_perf_recap]   pid_poll_interval = 0.25   ``` - Environment variable: [`CGROUP_PID_POLL_INTERVAL`](../../environment_variables.md#envvar-CGROUP_PID_POLL_INTERVAL) |
| **write_files**  boolean | Dictates whether files will be written containing performance readings  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [callback_cgroup_perf_recap]   write_files = false   ``` - Environment variable: [`CGROUP_WRITE_FILES`](../../environment_variables.md#envvar-CGROUP_WRITE_FILES) |

## [Notes](cgroup_perf_recap_callback.md#id5)

> **Note:**
>
> - Requires ansible to be run from within a cgroup, such as with `cgexec -g cpuacct,memory,pids:ansible_profile ansible-playbook ...`
> - This cgroup should only be used by ansible to get accurate results
> - To create the cgroup, first use a command such as `sudo cgcreate -a ec2-user:ec2-user -t ec2-user:ec2-user -g cpuacct,memory,pids:ansible_profile`

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.posix)
[Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
