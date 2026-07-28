---
collection: ansible
version: "8"
title: "community.rabbitmq.rabbitmq_upgrade module – Execute rabbitmq-upgrade commands"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/rabbitmq/rabbitmq_upgrade_module.html
fetched_at: 2026-07-28T01:58:54+00:00
---
# community.rabbitmq.rabbitmq_upgrade module – Execute rabbitmq-upgrade commands

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
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_upgrade`.

New in community.rabbitmq 1.1.0

- [Synopsis](rabbitmq_upgrade_module.md#synopsis)
- [Parameters](rabbitmq_upgrade_module.md#parameters)
- [Examples](rabbitmq_upgrade_module.md#examples)

## [Synopsis](rabbitmq_upgrade_module.md#id1)

- Allows to execute rabbitmq-upgrade commands

## [Parameters](rabbitmq_upgrade_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string / required | Specify action to be executed.  **Choices:**   - `"await_online_quorum_plus_one"` - `"await_online_synchronized_mirror"` - `"post_upgrade"` - `"drain"` - `"revive"` |
| **node**  string | Erlang node name of the target rabbit node.  **Default:** `"rabbit"` |

## [Examples](rabbitmq_upgrade_module.md#id3)

```yaml+jinja
- name: Drain 'rabbit@node-1' node (in other words, put it into maintenance mode)
  community.rabbitmq.rabbitmq_upgrade:
    action: drain
    node: rabbit@node-1
```

### Authors

- Damian Dabrowski (@damiandabrowski5)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
