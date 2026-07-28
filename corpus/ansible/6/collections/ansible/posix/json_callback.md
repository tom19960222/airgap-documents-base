---
collection: ansible
version: "6"
title: "ansible.posix.json callback – Ansible screen output as JSON"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/posix/json_callback.html
fetched_at: 2026-07-27T16:44:46+00:00
---
# ansible.posix.json callback – Ansible screen output as JSON

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
> see [Requirements](json_callback.md#ansible-collections-ansible-posix-json-callback-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.json`.

- [Callback plugin](json_callback.md#callback-plugin)
- [Synopsis](json_callback.md#synopsis)
- [Requirements](json_callback.md#requirements)
- [Parameters](json_callback.md#parameters)
- [Notes](json_callback.md#notes)

## [Callback plugin](json_callback.md#id1)

This plugin is a **stdout callback**. You can use only use one stdout callback at a time. Additional aggregate or notification callbacks can be enabled though.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](json_callback.md#id2)

- This callback converts all events into JSON output to stdout

## [Requirements](json_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- Set as stdout in config

## [Parameters](json_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **show_custom_stats**  boolean | This adds the custom stats set via the set_stats plugin to the play recap  Choices:   - `false` ← (default) - `true`   Configuration:   - INI entry:  ```YAML+Jinja   [defaults]   show_custom_stats = false   ``` - Environment variable: [`ANSIBLE_SHOW_CUSTOM_STATS`](../../../reference_appendices/config.md#envvar-ANSIBLE_SHOW_CUSTOM_STATS) |

## [Notes](json_callback.md#id5)

> **Note:**
>
> - When using a strategy such as free, host_pinned, or a custom strategy, host results will be added to new task results in ``.plays[].tasks[]``. As such, there will exist duplicate task objects indicated by duplicate task IDs at ``.plays[].tasks[].task.id``, each with an individual host result for the task.

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.posix)
[Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
