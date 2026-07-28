---
collection: ansible
version: "8"
title: "community.rabbitmq.rabbitmq_vhost_limits module – Manage the state of virtual host limits in RabbitMQ"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/rabbitmq/rabbitmq_vhost_limits_module.html
fetched_at: 2026-07-28T01:58:57+00:00
---
# community.rabbitmq.rabbitmq_vhost_limits module – Manage the state of virtual host limits in RabbitMQ

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
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_vhost_limits`.

- [Synopsis](rabbitmq_vhost_limits_module.md#synopsis)
- [Parameters](rabbitmq_vhost_limits_module.md#parameters)
- [Examples](rabbitmq_vhost_limits_module.md#examples)

## [Synopsis](rabbitmq_vhost_limits_module.md#id1)

- This module sets/clears certain limits on a virtual host.
- The configurable limits are *max_connections* and *max-queues*.

## [Parameters](rabbitmq_vhost_limits_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **max_connections**  integer | Max number of concurrent client connections.  Negative value means “no limit”.  Ignored when the *state* is `absent`.  **Default:** `-1` |
| **max_queues**  integer | Max number of queues.  Negative value means “no limit”.  Ignored when the *state* is `absent`.  **Default:** `-1` |
| **node**  string | Name of the RabbitMQ Erlang node to manage. |
| **state**  string | Specify whether the limits are to be set or cleared.  If set to `absent`, the limits of both *max_connections* and *max-queues* will be cleared.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vhost**  string | Name of the virtual host to manage.  **Default:** `"/"` |

## [Examples](rabbitmq_vhost_limits_module.md#id3)

```yaml+jinja
- name: Limit both of the max number of connections and queues on the vhost '/'.
  community.rabbitmq.rabbitmq_vhost_limits:
    vhost: /
    max_connections: 64
    max_queues: 256
    state: present

- name: |-
    Limit the max number of connections on the vhost '/'.
    This task implicitly clears the max number of queues limit using default value: -1.
  community.rabbitmq.rabbitmq_vhost_limits:
    vhost: /
    max_connections: 64
    state: present

- name: Clear the limits on the vhost '/'.
  community.rabbitmq.rabbitmq_vhost_limits:
    vhost: /
    state: absent
```

### Authors

- Hiroyuki Matsuo (@h-matsuo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
