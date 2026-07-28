---
collection: ansible
version: "6"
title: "community.rabbitmq.rabbitmq_feature_flag module – Enables feature flag"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/rabbitmq/rabbitmq_feature_flag_module.html
fetched_at: 2026-07-27T17:20:40+00:00
---
# community.rabbitmq.rabbitmq_feature_flag module – Enables feature flag

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
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_feature_flag`.

New in community.rabbitmq 1.1.0

- [Synopsis](rabbitmq_feature_flag_module.md#synopsis)
- [Parameters](rabbitmq_feature_flag_module.md#parameters)
- [Examples](rabbitmq_feature_flag_module.md#examples)

## [Synopsis](rabbitmq_feature_flag_module.md#id1)

- Allows to enable specified feature flag.

## [Parameters](rabbitmq_feature_flag_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Feature flag name. |
| **node**  string | Erlang node name of the target rabbit node.  Default: `"rabbit"` |

## [Examples](rabbitmq_feature_flag_module.md#id3)

```yaml+jinja
- name: Enable the 'maintenance_mode_status' feature flag on 'rabbit@node-1'
  community.rabbitmq.rabbitmq_feature_flag:
    name: maintenance_mode_status
    node: rabbit@node-1
```

### Authors

- Damian Dabrowski (@damiandabrowski5)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
