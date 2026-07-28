---
collection: ansible
version: "6"
title: "community.general.counter_enabled callback – adds counters to the output items (tasks and hosts/task)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/counter_enabled_callback.html
fetched_at: 2026-07-27T17:14:25+00:00
---
# community.general.counter_enabled callback – adds counters to the output items (tasks and hosts/task)

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
> see [Requirements](counter_enabled_callback.md#ansible-collections-community-general-counter-enabled-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.counter_enabled`.

- [Callback plugin](counter_enabled_callback.md#callback-plugin)
- [Synopsis](counter_enabled_callback.md#synopsis)
- [Requirements](counter_enabled_callback.md#requirements)
- [Parameters](counter_enabled_callback.md#parameters)

## [Callback plugin](counter_enabled_callback.md#id1)

This plugin is a **stdout callback**. You can use only use one stdout callback at a time. Additional aggregate or notification callbacks can be enabled though.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](counter_enabled_callback.md#id2)

- Use this callback when you need a kind of progress bar on a large environments.
- You will know how many tasks has the playbook to run, and which one is actually running.
- You will know how many hosts may run a task, and which of them is actually running.

## [Requirements](counter_enabled_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- set as stdout callback in ansible.cfg (stdout_callback = counter_enabled)

## [Parameters](counter_enabled_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **check_mode_markers**  boolean  added in Ansible 2.9 | Toggle to control displaying markers when running in check mode.  The markers are `DRY RUN` at the beginning and ending of playbook execution (when calling `ansible-playbook --check`) and `CHECK MODE` as a suffix at every play and task that is run in check mode.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   check_mode_markers = false   ``` - Environment variable: [`ANSIBLE_CHECK_MODE_MARKERS`](../../environment_variables.md#envvar-ANSIBLE_CHECK_MODE_MARKERS) |
| **display_failed_stderr**  boolean  added in Ansible 2.7 | Toggle to control whether failed and unreachable tasks are displayed to STDERR (vs. STDOUT)  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   display_failed_stderr = false   ``` - Environment variable: [`ANSIBLE_DISPLAY_FAILED_STDERR`](../../environment_variables.md#envvar-ANSIBLE_DISPLAY_FAILED_STDERR) |
| **display_ok_hosts**  boolean  added in Ansible 2.7 | Toggle to control displaying ‘ok’ task/host results in a task  Choices:   - `false` - `true` ← (default)   Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   display_ok_hosts = true   ``` - Environment variable: [`ANSIBLE_DISPLAY_OK_HOSTS`](../../environment_variables.md#envvar-ANSIBLE_DISPLAY_OK_HOSTS) |
| **display_skipped_hosts**  boolean | Toggle to control displaying skipped task/host results in a task  Choices:   - `false` - `true` ← (default)   Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   display_skipped_hosts = true   ``` - Environment variable: [`DISPLAY_SKIPPED_HOSTS`](../../../reference_appendices/config.md#envvar-DISPLAY_SKIPPED_HOSTS)  Removed in: version 2.12 of ansible.builtin  Why: environment variables without `ANSIBLE_` prefix are deprecated  Alternative: the `ANSIBLE_DISPLAY_SKIPPED_HOSTS` environment variable - Environment variable: [`ANSIBLE_DISPLAY_SKIPPED_HOSTS`](../../../reference_appendices/config.md#envvar-ANSIBLE_DISPLAY_SKIPPED_HOSTS) |
| **show_custom_stats**  boolean | This adds the custom stats set via the set_stats plugin to the play recap  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   show_custom_stats = false   ``` - Environment variable: [`ANSIBLE_SHOW_CUSTOM_STATS`](../../../reference_appendices/config.md#envvar-ANSIBLE_SHOW_CUSTOM_STATS) |
| **show_per_host_start**  boolean  added in Ansible 2.9 | This adds output that shows when a task is started to execute for each host  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   show_per_host_start = false   ``` - Environment variable: [`ANSIBLE_SHOW_PER_HOST_START`](../../environment_variables.md#envvar-ANSIBLE_SHOW_PER_HOST_START) |
| **show_task_path_on_failure**  boolean  added in ansible-core 2.11 | When a task fails, display the path to the file containing the failed task and the line number. This information is displayed automatically for every task when running with `-vv` or greater verbosity.  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   show_task_path_on_failure = false   ``` - Environment variable: [`ANSIBLE_SHOW_TASK_PATH_ON_FAILURE`](../../environment_variables.md#envvar-ANSIBLE_SHOW_TASK_PATH_ON_FAILURE) |

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
