---
collection: ansible
version: "8"
title: "community.rabbitmq.rabbitmq_parameter module – Manage RabbitMQ parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/rabbitmq/rabbitmq_parameter_module.html
fetched_at: 2026-07-28T01:58:51+00:00
---
# community.rabbitmq.rabbitmq_parameter module – Manage RabbitMQ parameters

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
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_parameter`.

- [Synopsis](rabbitmq_parameter_module.md#synopsis)
- [Parameters](rabbitmq_parameter_module.md#parameters)
- [Examples](rabbitmq_parameter_module.md#examples)

## [Synopsis](rabbitmq_parameter_module.md#id1)

- Manage dynamic, cluster-wide parameters for RabbitMQ

## [Parameters](rabbitmq_parameter_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **component**  string / required | Name of the component of which the parameter is being set |
| **name**  string / required | Name of the parameter being set |
| **node**  string | erlang node name of the rabbit we wish to configure  **Default:** `"rabbit"` |
| **state**  string | Specify if parameter is to be added or removed  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **value**  string | Value of the parameter, as a JSON term |
| **vhost**  string | vhost to apply access privileges.  **Default:** `"/"` |

## [Examples](rabbitmq_parameter_module.md#id3)

```yaml+jinja
- name: Set the federation parameter 'local_username' to a value of 'guest' (in quotes)
  community.rabbitmq.rabbitmq_parameter:
    component: federation
    name: local-username
    value: '"guest"'
    state: present
```

### Authors

- Chris Hoffman (@chrishoffman)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
