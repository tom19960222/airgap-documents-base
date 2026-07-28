---
collection: ansible
version: "8"
title: "community.rabbitmq.rabbitmq_plugin module – Manage RabbitMQ plugins"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/rabbitmq/rabbitmq_plugin_module.html
fetched_at: 2026-07-28T01:58:51+00:00
---
# community.rabbitmq.rabbitmq_plugin module – Manage RabbitMQ plugins

> **Note:**
>
> This module is part of the [community.rabbitmq collection](https://galaxy.ansible.com/ui/repo/published/community/rabbitmq/) (version 1.2.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.rabbitmq`.
>
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_plugin`.

- [Synopsis](rabbitmq_plugin_module.md#synopsis)
- [Parameters](rabbitmq_plugin_module.md#parameters)
- [Examples](rabbitmq_plugin_module.md#examples)
- [Return Values](rabbitmq_plugin_module.md#return-values)

## [Synopsis](rabbitmq_plugin_module.md#id1)

- This module can be used to enable or disable RabbitMQ plugins.

## [Parameters](rabbitmq_plugin_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **broker_state**  string | Specify whether the broker should be online or offline for the plugin change.  **Choices:**   - `"online"` ← (default) - `"offline"` |
| **names**  aliases: name  string / required | Comma-separated list of plugin names. Also, accepts plugin name. |
| **new_only**  boolean | Only enable missing plugins.  Does not disable plugins that are not in the names list.  **Choices:**   - `false` ← (default) - `true` |
| **prefix**  string | Specify a custom install prefix to a Rabbit. |
| **state**  string | Specify if plugins are to be enabled or disabled.  **Choices:**   - `"enabled"` ← (default) - `"disabled"` |

## [Examples](rabbitmq_plugin_module.md#id3)

```yaml+jinja
- name: Enables the rabbitmq_management plugin
  community.rabbitmq.rabbitmq_plugin:
    names: rabbitmq_management
    state: enabled

- name: Enable multiple rabbitmq plugins
  community.rabbitmq.rabbitmq_plugin:
    names: rabbitmq_management,rabbitmq_management_visualiser
    state: enabled

- name: Disable plugin
  community.rabbitmq.rabbitmq_plugin:
    names: rabbitmq_management
    state: disabled

- name: Enable every plugin in list with existing plugins
  community.rabbitmq.rabbitmq_plugin:
    names: rabbitmq_management,rabbitmq_management_visualiser,rabbitmq_shovel,rabbitmq_shovel_management
    state: enabled
    new_only: true

- name: Enables the rabbitmq_peer_discovery_aws plugin without requiring a broker connection.
  community.rabbitmq.rabbitmq_plugin:
    names: rabbitmq_peer_discovery_aws_plugin
    state: enabled
    broker_state: offline
```

## [Return Values](rabbitmq_plugin_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **disabled**  list / elements=string | list of plugins disabled during task run  **Returned:** always  **Sample:** `["rabbitmq_management"]` |
| **enabled**  list / elements=string | list of plugins enabled during task run  **Returned:** always  **Sample:** `["rabbitmq_management"]` |

### Authors

- Chris Hoffman (@chrishoffman)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
