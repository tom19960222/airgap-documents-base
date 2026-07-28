---
collection: ansible
version: "8"
title: "community.general.selective callback – only print certain tasks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/selective_callback.html
fetched_at: 2026-07-28T01:52:04+00:00
---
# community.general.selective callback – only print certain tasks

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
> see [Requirements](selective_callback.md#ansible-collections-community-general-selective-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.selective`.

- [Callback plugin](selective_callback.md#callback-plugin)
- [Synopsis](selective_callback.md#synopsis)
- [Requirements](selective_callback.md#requirements)
- [Parameters](selective_callback.md#parameters)
- [Examples](selective_callback.md#examples)

## [Callback plugin](selective_callback.md#id1)

This plugin is a **stdout callback**. You can use only use one stdout callback at a time. Additional aggregate or notification callbacks can be enabled though.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](selective_callback.md#id2)

- This callback only prints tasks that have been tagged with `print_action` or that have failed. This allows operators to focus on the tasks that provide value only.
- Tasks that are not printed are placed with a `.`.
- If you increase verbosity all tasks are printed.

## [Requirements](selective_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- set as main display callback

## [Parameters](selective_callback.md#id4)

| Parameter | Comments |
| --- | --- |
| **nocolor**  boolean | This setting allows suppressing colorizing output.  **Choices:**   - `false` ← (default) - `true`   **Configuration:**   - INI entry:  ```YAML+Jinja   [defaults]   nocolor = false   ``` - Environment variable: [`ANSIBLE_NOCOLOR`](../../../reference_appendices/config.md#envvar-ANSIBLE_NOCOLOR) - Environment variable: [`ANSIBLE_SELECTIVE_DONT_COLORIZE`](../../environment_variables.md#envvar-ANSIBLE_SELECTIVE_DONT_COLORIZE) |

## [Examples](selective_callback.md#id5)

```yaml+jinja
- ansible.builtin.debug: msg="This will not be printed"
- ansible.builtin.debug: msg="But this will"
  tags: [print_action]
```

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
