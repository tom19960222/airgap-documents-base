---
collection: ansible
version: "8"
title: "ansible.posix.jsonl callback – Ansible screen output as JSONL (lines in json format)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/jsonl_callback.html
fetched_at: 2026-07-28T01:09:36+00:00
---
# ansible.posix.jsonl callback – Ansible screen output as JSONL (lines in json format)

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
> see [Requirements](jsonl_callback.md#ansible-collections-ansible-posix-jsonl-callback-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.jsonl`.

- [Callback plugin](jsonl_callback.md#callback-plugin)
- [Synopsis](jsonl_callback.md#synopsis)
- [Requirements](jsonl_callback.md#requirements)
- [Parameters](jsonl_callback.md#parameters)
- [Notes](jsonl_callback.md#notes)

## [Callback plugin](jsonl_callback.md#id1)

This plugin is a **stdout callback**. You can use only use one stdout callback at a time. Additional aggregate or notification callbacks can be enabled though.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](jsonl_callback.md#id2)

- This callback converts all events into JSON output to stdout
- This callback in contrast with ansible.posix.json uses less memory, because it doesn’t store results.

## [Requirements](jsonl_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- Set as stdout in config

## [Parameters](jsonl_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **json_indent**  integer | If specified, use this many spaces for indenting in the JSON output. If not specified or <= 0, write to a single line.  **Default:** `0`  **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   json_indent = 0   ``` - Environment variable: [`ANSIBLE_JSON_INDENT`](../../environment_variables.md#envvar-ANSIBLE_JSON_INDENT) |
| **show_custom_stats**  boolean | This adds the custom stats set via the set_stats plugin to the play recap  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   show_custom_stats = false   ``` - Environment variable: [`ANSIBLE_SHOW_CUSTOM_STATS`](../../../reference_appendices/config.md#envvar-ANSIBLE_SHOW_CUSTOM_STATS) |

## [Notes](jsonl_callback.md#id5)

> **Note:**
>
> - When using a strategy such as free, host_pinned, or a custom strategy, host results will be added to new task results in ``.plays[].tasks[]``. As such, there will exist duplicate task objects indicated by duplicate task IDs at ``.plays[].tasks[].task.id``, each with an individual host result for the task.

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
