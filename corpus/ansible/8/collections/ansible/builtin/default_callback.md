---
collection: ansible
version: "8"
title: "ansible.builtin.default callback – default Ansible screen output"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/default_callback.html
fetched_at: 2026-07-28T01:07:53+00:00
---
# ansible.builtin.default callback – default Ansible screen output

> **Note:**
>
> This callback plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `default`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.default` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same callback plugin name.

- [Callback plugin](default_callback.md#callback-plugin)
- [Synopsis](default_callback.md#synopsis)
- [Requirements](default_callback.md#requirements)
- [Parameters](default_callback.md#parameters)

## [Callback plugin](default_callback.md#id1)

This plugin is a **stdout callback**. You can use only use one stdout callback at a time. Additional aggregate or notification callbacks can be enabled though.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](default_callback.md#id2)

- This is the default output callback for ansible-playbook.

## [Requirements](default_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- set as stdout in configuration

## [Parameters](default_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **check_mode_markers**  boolean  *added in Ansible 2.9* | Toggle to control displaying markers when running in check mode.  The markers are `DRY RUN` at the beginning and ending of playbook execution (when calling `ansible-playbook --check`) and `CHECK MODE` as a suffix at every play and task that is run in check mode.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   check_mode_markers = false   ``` - Environment variable: [`ANSIBLE_CHECK_MODE_MARKERS`](../../environment_variables.md#envvar-ANSIBLE_CHECK_MODE_MARKERS) |
| **display_failed_stderr**  boolean  *added in Ansible 2.7* | Toggle to control whether failed and unreachable tasks are displayed to STDERR (vs. STDOUT)  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   display_failed_stderr = false   ``` - Environment variable: [`ANSIBLE_DISPLAY_FAILED_STDERR`](../../environment_variables.md#envvar-ANSIBLE_DISPLAY_FAILED_STDERR) |
| **display_ok_hosts**  boolean  *added in Ansible 2.7* | Toggle to control displaying ‘ok’ task/host results in a task  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   display_ok_hosts = true   ``` - Environment variable: [`ANSIBLE_DISPLAY_OK_HOSTS`](../../environment_variables.md#envvar-ANSIBLE_DISPLAY_OK_HOSTS) |
| **display_skipped_hosts**  boolean | Toggle to control displaying skipped task/host results in a task  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   display_skipped_hosts = true   ``` - Environment variable: [`ANSIBLE_DISPLAY_SKIPPED_HOSTS`](../../../reference_appendices/config.md#envvar-ANSIBLE_DISPLAY_SKIPPED_HOSTS) |
| **pretty_results**  boolean  *added in ansible-core 2.13* | Configure the result format to be more readable  When the result format is set to `yaml` this option defaults to `True`, and defaults to `False` when configured to `json`.  Setting this option to `True` will force `json` and `yaml` results to always be pretty printed regardless of verbosity.  When set to `True` and used with the `yaml` result format, this option will modify module responses in an attempt to produce a more human friendly output at the expense of correctness, and should not be relied upon to aid in writing variable manipulations or conditionals. For correctness, set this option to `False` or set the result format to `json`.  **Choices:**   - `false` - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   callback_format_pretty = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_FORMAT_PRETTY`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_FORMAT_PRETTY) |
| **result_format**  string  *added in ansible-core 2.13* | Define the task result format used in the callback output.  These formats do not cause the callback to emit valid JSON or YAML formats.  The output contains these formats interspersed with other non-machine parsable data.  **Choices:**   - `"json"` ← (default) - `"yaml"`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   callback_result_format = json   ``` - Environment variable: [`ANSIBLE_CALLBACK_RESULT_FORMAT`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_RESULT_FORMAT) |
| **show_custom_stats**  boolean | This adds the custom stats set via the set_stats plugin to the play recap  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   show_custom_stats = false   ``` - Environment variable: [`ANSIBLE_SHOW_CUSTOM_STATS`](../../../reference_appendices/config.md#envvar-ANSIBLE_SHOW_CUSTOM_STATS) |
| **show_per_host_start**  boolean  *added in Ansible 2.9* | This adds output that shows when a task is started to execute for each host  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   show_per_host_start = false   ``` - Environment variable: [`ANSIBLE_SHOW_PER_HOST_START`](../../environment_variables.md#envvar-ANSIBLE_SHOW_PER_HOST_START) |
| **show_task_path_on_failure**  boolean  *added in ansible-core 2.11* | When a task fails, display the path to the file containing the failed task and the line number. This information is displayed automatically for every task when running with `-vv` or greater verbosity.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   show_task_path_on_failure = false   ``` - Environment variable: [`ANSIBLE_SHOW_TASK_PATH_ON_FAILURE`](../../environment_variables.md#envvar-ANSIBLE_SHOW_TASK_PATH_ON_FAILURE) |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
