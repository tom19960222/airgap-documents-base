---
collection: ansible
version: "6"
title: "community.rabbitmq.rabbitmq_policy module – Manage the state of policies in RabbitMQ"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/rabbitmq/rabbitmq_policy_module.html
fetched_at: 2026-07-27T17:20:43+00:00
---
# community.rabbitmq.rabbitmq_policy module – Manage the state of policies in RabbitMQ

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
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_policy`.

- [Synopsis](rabbitmq_policy_module.md#synopsis)
- [Parameters](rabbitmq_policy_module.md#parameters)
- [Examples](rabbitmq_policy_module.md#examples)

## [Synopsis](rabbitmq_policy_module.md#id1)

- Manage the state of a policy in RabbitMQ.

## [Parameters](rabbitmq_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **apply_to**  string | What the policy applies to. Requires RabbitMQ 3.2.0 or later.  Choices:   - `"all"` ← (default) - `"exchanges"` - `"queues"` |
| **name**  string / required | The name of the policy to manage. |
| **node**  string | Erlang node name of the rabbit we wish to configure.  Default: `"rabbit"` |
| **pattern**  string | A regex of queues to apply the policy to. Required when `state=present`. This option is no longer required as of Ansible 2.9. |
| **priority**  string | The priority of the policy.  Default: `"0"` |
| **state**  string | The state of the policy.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | A dict or string describing the policy. Required when `state=present`. This option is no longer required as of Ansible 2.9. |
| **vhost**  string | The name of the vhost to apply to.  Default: `"/"` |

## [Examples](rabbitmq_policy_module.md#id3)

```yaml+jinja
- name: ensure the default vhost contains the HA policy via a dict
  community.rabbitmq.rabbitmq_policy:
    name: HA
    pattern: .*
  args:
    tags:
      ha-mode: all

- name: ensure the default vhost contains the HA policy
  community.rabbitmq.rabbitmq_policy:
    name: HA
    pattern: .*
    tags:
      ha-mode: all
```

### Authors

- John Dewey (@retr0h)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
