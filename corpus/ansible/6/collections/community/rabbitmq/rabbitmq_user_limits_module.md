---
collection: ansible
version: "6"
title: "community.rabbitmq.rabbitmq_user_limits module – Manage RabbitMQ user limits"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/rabbitmq/rabbitmq_user_limits_module.html
fetched_at: 2026-07-27T17:20:47+00:00
---
# community.rabbitmq.rabbitmq_user_limits module – Manage RabbitMQ user limits

> **Note:**
>
> This module is part of the [community.rabbitmq collection](https://galaxy.ansible.com/community/rabbitmq) (version 1.2.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.rabbitmq`.
>
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_user_limits`.

New in community.rabbitmq 1.1.0

- [Synopsis](rabbitmq_user_limits_module.md#synopsis)
- [Parameters](rabbitmq_user_limits_module.md#parameters)
- [Notes](rabbitmq_user_limits_module.md#notes)
- [Examples](rabbitmq_user_limits_module.md#examples)

## [Synopsis](rabbitmq_user_limits_module.md#id1)

- Manage the state of user limits in RabbitMQ. Supported since RabbitMQ version 3.8.10.

## [Parameters](rabbitmq_user_limits_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **max_channels**  integer | Max number of channels.  Negative value means “no limit”.  Ignored when the *state* is `absent`.  Default: `-1` |
| **max_connections**  integer | Max number of concurrent client connections.  Negative value means “no limit”.  Ignored when the *state* is `absent`.  Default: `-1` |
| **node**  string | Name of the RabbitMQ Erlang node to manage. |
| **state**  string | Specify whether the limits are to be set or cleared.  If set to `absent`, the limits of both *max_connections* and *max_channels* will be cleared.  Choices:   - `"present"` ← (default) - `"absent"` |
| **user**  aliases: username, name  string / required | Name of user to manage limits for. |

## [Notes](rabbitmq_user_limits_module.md#id3)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](rabbitmq_user_limits_module.md#id4)

```yaml+jinja
- name: Limit both of the max number of connections and channels on the user 'guest'.
  community.rabbitmq.rabbitmq_user_limits:
    user: guest
    max_connections: 64
    max_channels: 256
    state: present

# This task implicitly clears the max number of channels limit using default value: -1.
- name: Limit the max number of connections on the user 'guest'.
  community.rabbitmq.rabbitmq_user_limits:
    user: guest
    max_connections: 64
    state: present

- name: Clear the limits on the user 'guest'.
  community.rabbitmq.rabbitmq_user_limits:
    user: guest
    state: absent
```

### Authors

- Aitor Pazos (@aitorpazos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
