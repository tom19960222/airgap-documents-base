---
collection: ansible
version: "8"
title: "community.rabbitmq.rabbitmq_vhost module – Manage the state of a virtual host in RabbitMQ"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/rabbitmq/rabbitmq_vhost_module.html
fetched_at: 2026-07-28T01:58:56+00:00
---
# community.rabbitmq.rabbitmq_vhost module – Manage the state of a virtual host in RabbitMQ

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
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_vhost`.

- [Synopsis](rabbitmq_vhost_module.md#synopsis)
- [Parameters](rabbitmq_vhost_module.md#parameters)
- [Examples](rabbitmq_vhost_module.md#examples)

## [Synopsis](rabbitmq_vhost_module.md#id1)

- Manage the state of a virtual host in RabbitMQ

## [Parameters](rabbitmq_vhost_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: vhost  string / required | The name of the vhost to manage |
| **node**  string | erlang node name of the rabbit we wish to configure  **Default:** `"rabbit"` |
| **state**  string | The state of vhost  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tracing**  aliases: trace  boolean | Enable/disable tracing for a vhost  **Choices:**   - `false` ← (default) - `true` |

## [Examples](rabbitmq_vhost_module.md#id3)

```yaml+jinja
- name: Ensure that the vhost /test exists.
  community.rabbitmq.rabbitmq_vhost:
    name: /test
    state: present
```

### Authors

- Chris Hoffman (@chrishoffman)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
