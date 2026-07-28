---
collection: ansible
version: "8"
title: "community.windows.win_rabbitmq_plugin module – Manage RabbitMQ plugins"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_rabbitmq_plugin_module.html
fetched_at: 2026-07-28T02:02:19+00:00
---
# community.windows.win_rabbitmq_plugin module – Manage RabbitMQ plugins

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_rabbitmq_plugin`.

- [Synopsis](win_rabbitmq_plugin_module.md#synopsis)
- [Parameters](win_rabbitmq_plugin_module.md#parameters)
- [Examples](win_rabbitmq_plugin_module.md#examples)
- [Return Values](win_rabbitmq_plugin_module.md#return-values)

## [Synopsis](win_rabbitmq_plugin_module.md#id1)

- Manage RabbitMQ plugins.

## [Parameters](win_rabbitmq_plugin_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **names**  aliases: name  string / required | Comma-separated list of plugin names. |
| **new_only**  boolean | Only enable missing plugins.  Does not disable plugins that are not in the names list.  **Choices:**   - `false` ← (default) - `true` |
| **prefix**  string | Specify a custom install prefix to a Rabbit. |
| **state**  string | Specify if plugins are to be enabled or disabled.  **Choices:**   - `"disabled"` - `"enabled"` ← (default) |

## [Examples](win_rabbitmq_plugin_module.md#id3)

```yaml+jinja
- name: Enables the rabbitmq_management plugin
  community.windows.win_rabbitmq_plugin:
    names: rabbitmq_management
    state: enabled
```

## [Return Values](win_rabbitmq_plugin_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **disabled**  list / elements=string | List of plugins disabled during task run.  **Returned:** always  **Sample:** `["rabbitmq_management"]` |
| **enabled**  list / elements=string | List of plugins enabled during task run.  **Returned:** always  **Sample:** `["rabbitmq_management"]` |

### Authors

- Artem Zinenko (@ar7z1)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
