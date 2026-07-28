---
collection: ansible
version: "8"
title: "community.general.diy callback – Customize the output"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/diy_callback.html
fetched_at: 2026-07-28T01:51:54+00:00
---
# community.general.diy callback – Customize the output

> **Note:**
>
> This callback plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](diy_callback.md#ansible-collections-community-general-diy-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.diy`.

New in community.general 0.2.0

- [Callback plugin](diy_callback.md#callback-plugin)
- [Synopsis](diy_callback.md#synopsis)
- [Requirements](diy_callback.md#requirements)
- [Parameters](diy_callback.md#parameters)
- [Notes](diy_callback.md#notes)
- [See Also](diy_callback.md#see-also)
- [Examples](diy_callback.md#examples)

## [Callback plugin](diy_callback.md#id1)

This plugin is a **stdout callback**. You can use only use one stdout callback at a time. Additional aggregate or notification callbacks can be enabled though.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](diy_callback.md#id2)

- Callback plugin that allows you to supply your own custom callback templates to be output.

## [Requirements](diy_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- set as stdout_callback in configuration

## [Parameters](diy_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **check_mode_markers**  boolean  *added in Ansible 2.9* | Toggle to control displaying markers when running in check mode.  The markers are `DRY RUN` at the beginning and ending of playbook execution (when calling `ansible-playbook --check`) and `CHECK MODE` as a suffix at every play and task that is run in check mode.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   check_mode_markers = false   ``` - Environment variable: [`ANSIBLE_CHECK_MODE_MARKERS`](../../environment_variables.md#envvar-ANSIBLE_CHECK_MODE_MARKERS) |
| **display_failed_stderr**  boolean  *added in Ansible 2.7* | Toggle to control whether failed and unreachable tasks are displayed to STDERR (vs. STDOUT)  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   display_failed_stderr = false   ``` - Environment variable: [`ANSIBLE_DISPLAY_FAILED_STDERR`](../../environment_variables.md#envvar-ANSIBLE_DISPLAY_FAILED_STDERR) |
| **display_ok_hosts**  boolean  *added in Ansible 2.7* | Toggle to control displaying ‘ok’ task/host results in a task  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   display_ok_hosts = true   ``` - Environment variable: [`ANSIBLE_DISPLAY_OK_HOSTS`](../../environment_variables.md#envvar-ANSIBLE_DISPLAY_OK_HOSTS) |
| **display_skipped_hosts**  boolean | Toggle to control displaying skipped task/host results in a task  **Choices:**   - `false` - `true` ← (default)   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   display_skipped_hosts = true   ``` - Environment variable: [`ANSIBLE_DISPLAY_SKIPPED_HOSTS`](../../../reference_appendices/config.md#envvar-ANSIBLE_DISPLAY_SKIPPED_HOSTS) |
| **on_any_msg**  string | Output to be used for callback on_any.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   on_any_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_ON_ANY_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_ON_ANY_MSG) - Variable: ansible_callback_diy_on_any_msg |
| **on_any_msg_color**  string | Output color to be used for `on_any_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   on_any_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_ON_ANY_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_ON_ANY_MSG_COLOR) - Variable: ansible_callback_diy_on_any_msg_color |
| **on_file_diff_msg**  string | Output to be used for callback on_file_diff.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   on_file_diff_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_ON_FILE_DIFF_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_ON_FILE_DIFF_MSG) - Variable: ansible_callback_diy_on_file_diff_msg |
| **on_file_diff_msg_color**  string | Output color to be used for `on_file_diff_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   on_file_diff_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_ON_FILE_DIFF_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_ON_FILE_DIFF_MSG_COLOR) - Variable: ansible_callback_diy_on_file_diff_msg_color |
| **playbook_on_handler_task_start_msg**  string | Output to be used for callback playbook_on_handler_task_start.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_handler_task_start_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_HANDLER_TASK_START_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_HANDLER_TASK_START_MSG) - Variable: ansible_callback_diy_playbook_on_handler_task_start_msg |
| **playbook_on_handler_task_start_msg_color**  string | Output color to be used for `playbook_on_handler_task_start_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_handler_task_start_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_HANDLER_TASK_START_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_HANDLER_TASK_START_MSG_COLOR) - Variable: ansible_callback_diy_playbook_on_handler_task_start_msg_color |
| **playbook_on_include_msg**  string | Output to be used for callback playbook_on_include.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_include_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_INCLUDE_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_INCLUDE_MSG) - Variable: ansible_callback_diy_playbook_on_include_msg |
| **playbook_on_include_msg_color**  string | Output color to be used for `playbook_on_include_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_include_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_INCLUDE_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_INCLUDE_MSG_COLOR) - Variable: ansible_callback_diy_playbook_on_include_msg_color |
| **playbook_on_no_hosts_matched_msg**  string | Output to be used for callback playbook_on_no_hosts_matched.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_no_hosts_matched_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NO_HOSTS_MATCHED_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NO_HOSTS_MATCHED_MSG) - Variable: ansible_callback_diy_playbook_on_no_hosts_matched_msg |
| **playbook_on_no_hosts_matched_msg_color**  string | Output color to be used for `playbook_on_no_hosts_matched_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_no_hosts_matched_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NO_HOSTS_MATCHED_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NO_HOSTS_MATCHED_MSG_COLOR) - Variable: ansible_callback_diy_playbook_on_no_hosts_matched_msg_color |
| **playbook_on_no_hosts_remaining_msg**  string | Output to be used for callback playbook_on_no_hosts_remaining.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_no_hosts_remaining_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NO_HOSTS_REMAINING_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NO_HOSTS_REMAINING_MSG) - Variable: ansible_callback_diy_playbook_on_no_hosts_remaining_msg |
| **playbook_on_no_hosts_remaining_msg_color**  string | Output color to be used for `playbook_on_no_hosts_remaining_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_no_hosts_remaining_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NO_HOSTS_REMAINING_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NO_HOSTS_REMAINING_MSG_COLOR) - Variable: ansible_callback_diy_playbook_on_no_hosts_remaining_msg_color |
| **playbook_on_notify_msg**  string | Output to be used for callback playbook_on_notify.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_notify_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NOTIFY_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NOTIFY_MSG) - Variable: ansible_callback_diy_playbook_on_notify_msg |
| **playbook_on_notify_msg_color**  string | Output color to be used for `playbook_on_notify_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_notify_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NOTIFY_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_NOTIFY_MSG_COLOR) - Variable: ansible_callback_diy_playbook_on_notify_msg_color |
| **playbook_on_play_start_msg**  string | Output to be used for callback playbook_on_play_start.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_play_start_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_PLAY_START_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_PLAY_START_MSG) - Variable: ansible_callback_diy_playbook_on_play_start_msg |
| **playbook_on_play_start_msg_color**  string | Output color to be used for `playbook_on_play_start_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_play_start_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_PLAY_START_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_PLAY_START_MSG_COLOR) - Variable: ansible_callback_diy_playbook_on_play_start_msg_color |
| **playbook_on_setup_msg**  string | Output to be used for callback playbook_on_setup.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_setup_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_SETUP_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_SETUP_MSG) - Variable: ansible_callback_diy_playbook_on_setup_msg |
| **playbook_on_setup_msg_color**  string | Output color to be used for `playbook_on_setup_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_setup_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_SETUP_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_SETUP_MSG_COLOR) - Variable: ansible_callback_diy_playbook_on_setup_msg_color |
| **playbook_on_start_msg**  string | Output to be used for callback playbook_on_start.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_start_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_START_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_START_MSG) - Variable: ansible_callback_diy_playbook_on_start_msg |
| **playbook_on_start_msg_color**  string | Output color to be used for `playbook_on_start_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_start_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_START_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_START_MSG_COLOR) - Variable: ansible_callback_diy_playbook_on_start_msg_color |
| **playbook_on_stats_msg**  string | Output to be used for callback playbook_on_stats.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_stats_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_STATS_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_STATS_MSG) - Variable: ansible_callback_diy_playbook_on_stats_msg |
| **playbook_on_stats_msg_color**  string | Output color to be used for `playbook_on_stats_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_stats_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_STATS_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_STATS_MSG_COLOR) - Variable: ansible_callback_diy_playbook_on_stats_msg_color |
| **playbook_on_task_start_msg**  string | Output to be used for callback playbook_on_task_start.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_task_start_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_TASK_START_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_TASK_START_MSG) - Variable: ansible_callback_diy_playbook_on_task_start_msg |
| **playbook_on_task_start_msg_color**  string | Output color to be used for `playbook_on_task_start_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_task_start_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_TASK_START_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_TASK_START_MSG_COLOR) - Variable: ansible_callback_diy_playbook_on_task_start_msg_color |
| **playbook_on_vars_prompt_msg**  string | Output to be used for callback playbook_on_vars_prompt.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_vars_prompt_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_VARS_PROMPT_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_VARS_PROMPT_MSG) - Variable: ansible_callback_diy_playbook_on_vars_prompt_msg |
| **playbook_on_vars_prompt_msg_color**  string | Output color to be used for `playbook_on_vars_prompt_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   playbook_on_vars_prompt_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_VARS_PROMPT_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_PLAYBOOK_ON_VARS_PROMPT_MSG_COLOR) - Variable: ansible_callback_diy_playbook_on_vars_prompt_msg_color |
| **runner_item_on_failed_msg**  string | Output to be used for callback runner_item_on_failed.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_item_on_failed_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_FAILED_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_FAILED_MSG) - Variable: ansible_callback_diy_runner_item_on_failed_msg |
| **runner_item_on_failed_msg_color**  string | Output color to be used for `runner_item_on_failed_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_item_on_failed_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_FAILED_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_FAILED_MSG_COLOR) - Variable: ansible_callback_diy_runner_item_on_failed_msg_color |
| **runner_item_on_ok_msg**  string | Output to be used for callback runner_item_on_ok.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_item_on_ok_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_OK_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_OK_MSG) - Variable: ansible_callback_diy_runner_item_on_ok_msg |
| **runner_item_on_ok_msg_color**  string | Output color to be used for `runner_item_on_ok_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_item_on_ok_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_OK_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_OK_MSG_COLOR) - Variable: ansible_callback_diy_runner_item_on_ok_msg_color |
| **runner_item_on_skipped_msg**  string | Output to be used for callback runner_item_on_skipped.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_item_on_skipped_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_SKIPPED_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_SKIPPED_MSG) - Variable: ansible_callback_diy_runner_item_on_skipped_msg |
| **runner_item_on_skipped_msg_color**  string | Output color to be used for `runner_item_on_skipped_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_item_on_skipped_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_SKIPPED_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ITEM_ON_SKIPPED_MSG_COLOR) - Variable: ansible_callback_diy_runner_item_on_skipped_msg_color |
| **runner_on_failed_msg**  string | Output to be used for callback runner_on_failed.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_on_failed_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ON_FAILED_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ON_FAILED_MSG) - Variable: ansible_callback_diy_runner_on_failed_msg |
| **runner_on_failed_msg_color**  string | Output color to be used for `runner_on_failed_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_on_failed_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ON_FAILED_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ON_FAILED_MSG_COLOR) - Variable: ansible_callback_diy_runner_on_failed_msg_color |
| **runner_on_no_hosts_msg**  string | Output to be used for callback runner_on_no_hosts.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_on_no_hosts_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ON_NO_HOSTS_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ON_NO_HOSTS_MSG) - Variable: ansible_callback_diy_runner_on_no_hosts_msg |
| **runner_on_no_hosts_msg_color**  string | Output color to be used for `runner_on_no_hosts_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_on_no_hosts_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ON_NO_HOSTS_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ON_NO_HOSTS_MSG_COLOR) - Variable: ansible_callback_diy_runner_on_no_hosts_msg_color |
| **runner_on_ok_msg**  string | Output to be used for callback runner_on_ok.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_on_ok_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ON_OK_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ON_OK_MSG) - Variable: ansible_callback_diy_runner_on_ok_msg |
| **runner_on_ok_msg_color**  string | Output color to be used for `runner_on_ok_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_on_ok_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ON_OK_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ON_OK_MSG_COLOR) - Variable: ansible_callback_diy_runner_on_ok_msg_color |
| **runner_on_skipped_msg**  string | Output to be used for callback runner_on_skipped.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_on_skipped_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ON_SKIPPED_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ON_SKIPPED_MSG) - Variable: ansible_callback_diy_runner_on_skipped_msg |
| **runner_on_skipped_msg_color**  string | Output color to be used for `runner_on_skipped_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_on_skipped_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ON_SKIPPED_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ON_SKIPPED_MSG_COLOR) - Variable: ansible_callback_diy_runner_on_skipped_msg_color |
| **runner_on_start_msg**  string | Output to be used for callback runner_on_start.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_on_start_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ON_START_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ON_START_MSG) - Variable: ansible_callback_diy_runner_on_start_msg |
| **runner_on_start_msg_color**  string | Output color to be used for `runner_on_start_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_on_start_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ON_START_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ON_START_MSG_COLOR) - Variable: ansible_callback_diy_runner_on_start_msg_color |
| **runner_on_unreachable_msg**  string | Output to be used for callback runner_on_unreachable.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_on_unreachable_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ON_UNREACHABLE_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ON_UNREACHABLE_MSG) - Variable: ansible_callback_diy_runner_on_unreachable_msg |
| **runner_on_unreachable_msg_color**  string | Output color to be used for `runner_on_unreachable_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_on_unreachable_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_ON_UNREACHABLE_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_ON_UNREACHABLE_MSG_COLOR) - Variable: ansible_callback_diy_runner_on_unreachable_msg_color |
| **runner_retry_msg**  string | Output to be used for callback runner_retry.  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_retry_msg = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_RETRY_MSG`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_RETRY_MSG) - Variable: ansible_callback_diy_runner_retry_msg |
| **runner_retry_msg_color**  string | Output color to be used for `runner_retry_msg`.  Template should render a [valid color value](diy_callback.md#notes).  **Configuration:**   - INI entry:  ```YAML+Jinja   [callback_diy]   runner_retry_msg_color = VALUE   ``` - Environment variable: [`ANSIBLE_CALLBACK_DIY_RUNNER_RETRY_MSG_COLOR`](../../environment_variables.md#envvar-ANSIBLE_CALLBACK_DIY_RUNNER_RETRY_MSG_COLOR) - Variable: ansible_callback_diy_runner_retry_msg_color |
| **show_custom_stats**  boolean | This adds the custom stats set via the set_stats plugin to the play recap  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   show_custom_stats = false   ``` - Environment variable: [`ANSIBLE_SHOW_CUSTOM_STATS`](../../../reference_appendices/config.md#envvar-ANSIBLE_SHOW_CUSTOM_STATS) |
| **show_per_host_start**  boolean  *added in Ansible 2.9* | This adds output that shows when a task is started to execute for each host  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   show_per_host_start = false   ``` - Environment variable: [`ANSIBLE_SHOW_PER_HOST_START`](../../environment_variables.md#envvar-ANSIBLE_SHOW_PER_HOST_START) |
| **show_task_path_on_failure**  boolean  *added in ansible-core 2.11* | When a task fails, display the path to the file containing the failed task and the line number. This information is displayed automatically for every task when running with `-vv` or greater verbosity.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   show_task_path_on_failure = false   ``` - Environment variable: [`ANSIBLE_SHOW_TASK_PATH_ON_FAILURE`](../../environment_variables.md#envvar-ANSIBLE_SHOW_TASK_PATH_ON_FAILURE) |

## [Notes](diy_callback.md#id5)

> **Note:**
>
> - Uses the [ansible.builtin.default](../../ansible/builtin/default_callback.md#ansible-collections-ansible-builtin-default-callback) callback plugin output when a custom callback `message(msg)` is not provided.
> - Makes the callback event data available via the `ansible_callback_diy` dictionary, which can be used in the templating context for the options. The dictionary is only available in the templating context for the options. It is not a variable that is available via the other various execution contexts, such as playbook, play, task etc.
> - Options being set by their respective variable input can only be set using the variable if the variable was set in a context that is available to the respective callback. Use the `ansible_callback_diy` dictionary to see what is available to a callback. Additionally, `ansible_callback_diy.top_level_var_names` will output the top level variable names available to the callback.
> - Each option value is rendered as a template before being evaluated. This allows for the dynamic usage of an option. For example, `"{{ 'yellow' if ansible_callback_diy.result.is_changed else 'bright green' }}"`
> - \*\*Condition\*\* for all `msg` options: if value `is None or omit`, then the option is not being used. \*\*Effect\*\*: use of the `default` callback plugin for output
> - \*\*Condition\*\* for all `msg` options: if value `is not None and not omit and length is not greater than 0`, then the option is being used without output. \*\*Effect\*\*: suppress output
> - \*\*Condition\*\* for all `msg` options: if value `is not None and not omit and length is greater than 0`, then the option is being used with output. \*\*Effect\*\*: render value as template and output
> - Valid color values: `black`, `bright gray`, `blue`, `white`, `green`, `bright blue`, `cyan`, `bright green`, `red`, `bright cyan`, `purple`, `bright red`, `yellow`, `bright purple`, `dark gray`, `bright yellow`, `magenta`, `bright magenta`, `normal`

## [See Also](diy_callback.md#id6)

> **See also:**
>
> [default – default Ansible screen output](https://docs.ansible.com/ansible/latest/plugins/callback/default.html)
> :   The official documentation on the **default** callback plugin.

## [Examples](diy_callback.md#id7)

```yaml+jinja
ansible.cfg: >
  # Enable plugin
  [defaults]
  stdout_callback=community.general.diy

  [callback_diy]
  # Output when playbook starts
  playbook_on_start_msg="DIY output(via ansible.cfg): playbook example: {{ ansible_callback_diy.playbook.file_name }}"
  playbook_on_start_msg_color=yellow

  # Comment out to allow default plugin output
  # playbook_on_play_start_msg="PLAY: starting play {{ ansible_callback_diy.play.name }}"

  # Accept on_skipped_msg or ansible_callback_diy_runner_on_skipped_msg as input vars
  # If neither are supplied, omit the option
  runner_on_skipped_msg="{{ on_skipped_msg | default(ansible_callback_diy_runner_on_skipped_msg) | default(omit) }}"

  # Newline after every callback
  # on_any_msg='{{ " " | join("\n") }}'

playbook.yml: >
  ---
  - name: "Default plugin output: play example"
    hosts: localhost
    gather_facts: false
    tasks:
      - name:  Default plugin output
        ansible.builtin.debug:
          msg: default plugin output

  - name: Override from play vars
    hosts: localhost
    gather_facts: false
    vars:
      ansible_connection: local
      green: "\e[0m\e[38;5;82m"
      yellow: "\e[0m\e[38;5;11m"
      bright_purple: "\e[0m\e[38;5;105m"
      cyan: "\e[0m\e[38;5;51m"
      green_bg_black_fg: "\e[0m\e[48;5;40m\e[38;5;232m"
      yellow_bg_black_fg: "\e[0m\e[48;5;226m\e[38;5;232m"
      purple_bg_white_fg: "\e[0m\e[48;5;57m\e[38;5;255m"
      cyan_bg_black_fg: "\e[0m\e[48;5;87m\e[38;5;232m"
      magenta: "\e[38;5;198m"
      white: "\e[0m\e[38;5;255m"
      ansible_callback_diy_playbook_on_play_start_msg: "\n{{green}}DIY output(via play vars): play example: {{magenta}}{{ansible_callback_diy.play.name}}\n\n"
      ansible_callback_diy_playbook_on_task_start_msg: "DIY output(via play vars): task example: {{ ansible_callback_diy.task.name }}"
      ansible_callback_diy_playbook_on_task_start_msg_color: cyan
      ansible_callback_diy_playbook_on_stats_msg: |+2
                CUSTOM STATS
        ==============================
        {% for key in ansible_callback_diy.stats | sort %}
        {% if ansible_callback_diy.stats[key] %}
        {% if key == 'ok' %}
        {% set color_one = lookup('vars','green_bg_black_fg') %}
        {% set prefix = '      ' %}
        {% set suffix = '     ' %}
        {% set color_two = lookup('vars','green') %}
        {% elif key == 'changed' %}
        {% set color_one = lookup('vars','yellow_bg_black_fg') %}
        {% set prefix = '   ' %}
        {% set suffix = '   ' %}
        {% set color_two = lookup('vars','yellow') %}
        {% elif key == 'processed' %}
        {% set color_one = lookup('vars','purple_bg_white_fg') %}
        {% set prefix = '  ' %}
        {% set suffix = '  ' %}
        {% set color_two = lookup('vars','bright_purple') %}
        {% elif key == 'skipped' %}
        {% set color_one = lookup('vars','cyan_bg_black_fg') %}
        {% set prefix = '   ' %}
        {% set suffix = '   ' %}
        {% set color_two = lookup('vars','cyan') %}
        {% else %}
        {% set color_one = "" %}
        {% set prefix = "" %}
        {% set suffix = "" %}
        {% set color_two = "" %}
        {% endif %}
        {{ color_one }}{{ "%s%s%s" | format(prefix,key,suffix) }}{{ color_two }}: {{ ansible_callback_diy.stats[key] | to_nice_yaml }}
        {% endif %}
        {% endfor %}

    tasks:
      - name: Custom banner with default plugin result output
        ansible.builtin.debug:
          msg: "default plugin output: result example"

      - name: Override from task vars
        ansible.builtin.debug:
          msg: "example {{ two }}"
        changed_when: true
        vars:
          white_fg_red_bg: "\e[0m\e[48;5;1m"
          two: "{{ white_fg_red_bg }}    2    "
          ansible_callback_diy_playbook_on_task_start_msg: "\nDIY output(via task vars): task example: {{ ansible_callback_diy.task.name }}"
          ansible_callback_diy_playbook_on_task_start_msg_color: bright magenta
          ansible_callback_diy_runner_on_ok_msg: "DIY output(via task vars): result example: \n{{ ansible_callback_diy.result.output.msg }}\n"
          ansible_callback_diy_runner_on_ok_msg_color: "{{ 'yellow' if ansible_callback_diy.result.is_changed else 'bright green' }}"

      - name: Suppress output
        ansible.builtin.debug:
          msg: i should not be displayed
        vars:
          ansible_callback_diy_playbook_on_task_start_msg: ""
          ansible_callback_diy_runner_on_ok_msg: ""

      - name: Using alias vars (see ansible.cfg)
        ansible.builtin.debug:
          msg:
        when: false
        vars:
          ansible_callback_diy_playbook_on_task_start_msg: ""
          on_skipped_msg: "DIY output(via task vars): skipped example:\n\e[0m\e[38;5;4m\u25b6\u25b6 {{ ansible_callback_diy.result.task.name }}\n"
          on_skipped_msg_color: white

      - name: Just stdout
        ansible.builtin.command: echo some stdout
        vars:
          ansible_callback_diy_playbook_on_task_start_msg: "\n"
          ansible_callback_diy_runner_on_ok_msg: "{{ ansible_callback_diy.result.output.stdout }}\n"

      - name: Multiline output
        ansible.builtin.debug:
          msg: "{{ multiline }}"
        vars:
          ansible_callback_diy_playbook_on_task_start_msg: "\nDIY output(via task vars): task example: {{ ansible_callback_diy.task.name }}"
          multiline: "line\nline\nline"
          ansible_callback_diy_runner_on_ok_msg: |+2
            some
            {{ ansible_callback_diy.result.output.msg }}
            output

          ansible_callback_diy_playbook_on_task_start_msg_color: bright blue

      - name: Indentation
        ansible.builtin.debug:
          msg: "{{ item.msg }}"
        with_items:
          - { indent: 1, msg: one., color: red }
          - { indent: 2, msg: two.., color: yellow }
          - { indent: 3, msg: three..., color: bright yellow }
        vars:
          ansible_callback_diy_runner_item_on_ok_msg: "{{ ansible_callback_diy.result.output.msg | indent(item.indent, True) }}"
          ansible_callback_diy_runner_item_on_ok_msg_color: "{{ item.color }}"
          ansible_callback_diy_runner_on_ok_msg: "GO!!!"
          ansible_callback_diy_runner_on_ok_msg_color: bright green

      - name: Using lookup and template as file
        ansible.builtin.shell: "echo {% raw %}'output from {{ file_name }}'{% endraw %} > {{ file_name }}"
        vars:
          ansible_callback_diy_playbook_on_task_start_msg: "\nDIY output(via task vars): task example: {{ ansible_callback_diy.task.name }}"
          file_name: diy_file_template_example
          ansible_callback_diy_runner_on_ok_msg: "{{ lookup('template', file_name) }}"

      - name: 'Look at top level vars available to the "runner_on_ok" callback'
        ansible.builtin.debug:
          msg: ''
        vars:
          ansible_callback_diy_playbook_on_task_start_msg: "\nDIY output(via task vars): task example: {{ ansible_callback_diy.task.name }}"
          ansible_callback_diy_runner_on_ok_msg: |+2
            {% for var in (ansible_callback_diy.top_level_var_names|reject('match','vars|ansible_callback_diy.*')) | sort %}
            {{ green }}{{ var }}:
              {{ white }}{{ lookup('vars', var) }}

            {% endfor %}
          ansible_callback_diy_runner_on_ok_msg_color: white

      - name: 'Look at event data available to the "runner_on_ok" callback'
        ansible.builtin.debug:
          msg: ''
        vars:
          ansible_callback_diy_playbook_on_task_start_msg: "\nDIY output(via task vars): task example: {{ ansible_callback_diy.task.name }}"
          ansible_callback_diy_runner_on_ok_msg: |+2
            {% for key in ansible_callback_diy | sort %}
            {{ green }}{{ key }}:
              {{ white }}{{ ansible_callback_diy[key] }}

            {% endfor %}
```

### Authors

- Trevor Highfill (@theque5t)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
