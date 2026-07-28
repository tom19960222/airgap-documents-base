---
collection: ansible
version: "8"
title: "ansible.posix.skippy callback – Ansible screen output that ignores skipped status"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/skippy_callback.html
fetched_at: 2026-07-28T01:09:38+00:00
---
# ansible.posix.skippy callback – Ansible screen output that ignores skipped status

> **Note:**
>
> This callback plugin is part of the [ansible.posix collection](https://galaxy.ansible.com/ui/repo/published/ansible/posix/) (version 1.5.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](skippy_callback.md#ansible-collections-ansible-posix-skippy-callback-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.skippy`.

- [DEPRECATED](skippy_callback.md#deprecated)
- [Callback plugin](skippy_callback.md#callback-plugin)
- [Synopsis](skippy_callback.md#synopsis)
- [Requirements](skippy_callback.md#requirements)
- [Parameters](skippy_callback.md#parameters)
- [Status](skippy_callback.md#status)

## [DEPRECATED](skippy_callback.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   The ‘default’ callback plugin now supports this functionality

Alternative:
:   ‘default’ callback plugin with ‘display_skipped_hosts = no’ option

## [Callback plugin](skippy_callback.md#id2)

This plugin is a **stdout callback**. You can use only use one stdout callback at a time. Additional aggregate or notification callbacks can be enabled though.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](skippy_callback.md#id3)

- This callback does the same as the default except it does not output skipped host/task/item status

## [Requirements](skippy_callback.md#id4)

The below requirements are needed on the local controller node that executes this callback.

- set as main display callback

## [Parameters](skippy_callback.md#id5)

| Parameter | Comments |
| --- | --- |
| **check_mode_markers**  boolean  *added in Ansible 2.9* | Toggle to control displaying markers when running in check mode.  The markers are `DRY RUN` at the beginning and ending of playbook execution (when calling `ansible-playbook --check`) and `CHECK MODE` as a suffix at every play and task that is run in check mode.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   check_mode_markers = false   ``` - Environment variable: [`ANSIBLE_CHECK_MODE_MARKERS`](../../environment_variables.md#envvar-ANSIBLE_CHECK_MODE_MARKERS) |
| **display_failed_stderr**  boolean  *added in Ansible 2.7* | Toggle to control whether failed and unreachable tasks are displayed to STDERR (vs. STDOUT)  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   display_failed_stderr = false   ``` - Environment variable: [`ANSIBLE_DISPLAY_FAILED_STDERR`](../../environment_variables.md#envvar-ANSIBLE_DISPLAY_FAILED_STDERR) |
| **display_ok_hosts**  boolean  *added in Ansible 2.7* | Toggle to control displaying ‘ok’ task/host results in a task  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   display_ok_hosts = true   ``` - Environment variable: [`ANSIBLE_DISPLAY_OK_HOSTS`](../../environment_variables.md#envvar-ANSIBLE_DISPLAY_OK_HOSTS) |
| **display_skipped_hosts**  boolean | Toggle to control displaying skipped task/host results in a task  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   display_skipped_hosts = true   ``` - Environment variable: [`ANSIBLE_DISPLAY_SKIPPED_HOSTS`](../../../reference_appendices/config.md#envvar-ANSIBLE_DISPLAY_SKIPPED_HOSTS) |
| **show_custom_stats**  boolean | This adds the custom stats set via the set_stats plugin to the play recap  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   show_custom_stats = false   ``` - Environment variable: [`ANSIBLE_SHOW_CUSTOM_STATS`](../../../reference_appendices/config.md#envvar-ANSIBLE_SHOW_CUSTOM_STATS) |
| **show_per_host_start**  boolean  *added in Ansible 2.9* | This adds output that shows when a task is started to execute for each host  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   show_per_host_start = false   ``` - Environment variable: [`ANSIBLE_SHOW_PER_HOST_START`](../../environment_variables.md#envvar-ANSIBLE_SHOW_PER_HOST_START) |
| **show_task_path_on_failure**  boolean  *added in ansible-core 2.11* | When a task fails, display the path to the file containing the failed task and the line number. This information is displayed automatically for every task when running with `-vv` or greater verbosity.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   show_task_path_on_failure = false   ``` - Environment variable: [`ANSIBLE_SHOW_TASK_PATH_ON_FAILURE`](../../environment_variables.md#envvar-ANSIBLE_SHOW_TASK_PATH_ON_FAILURE) |

## [Status](skippy_callback.md#id6)

- This callback will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](skippy_callback.md#deprecated).

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
