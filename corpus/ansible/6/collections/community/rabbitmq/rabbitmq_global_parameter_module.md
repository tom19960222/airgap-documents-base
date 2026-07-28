---
collection: ansible
version: "6"
title: "community.rabbitmq.rabbitmq_global_parameter module – Manage RabbitMQ global parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/rabbitmq/rabbitmq_global_parameter_module.html
fetched_at: 2026-07-27T17:20:41+00:00
---
# community.rabbitmq.rabbitmq_global_parameter module – Manage RabbitMQ global parameters

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
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_global_parameter`.

- [Synopsis](rabbitmq_global_parameter_module.md#synopsis)
- [Parameters](rabbitmq_global_parameter_module.md#parameters)
- [Examples](rabbitmq_global_parameter_module.md#examples)
- [Return Values](rabbitmq_global_parameter_module.md#return-values)

## [Synopsis](rabbitmq_global_parameter_module.md#id1)

- Manage dynamic, cluster-wide global parameters for RabbitMQ

## [Parameters](rabbitmq_global_parameter_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name of the global parameter being set |
| **node**  string | erlang node name of the rabbit we wish to configure  Default: `"rabbit"` |
| **state**  string | Specify if global parameter is to be added or removed  Choices:   - `"present"` ← (default) - `"absent"` |
| **value**  string | Value of the global parameter, as a JSON term |

## [Examples](rabbitmq_global_parameter_module.md#id3)

```yaml+jinja
- name: Set the global parameter 'cluster_name' to a value of 'mq-cluster' (in quotes)
  community.rabbitmq.rabbitmq_global_parameter:
    name: cluster_name
    value: "{{ 'mq-cluster' | to_json }}"
    state: present
```

## [Return Values](rabbitmq_global_parameter_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **name**  string | name of the global parameter being set  Returned: success  Sample: `"cluster_name"` |
| **value**  string | value of the global parameter, as a JSON term  Returned: changed  Sample: `"the-cluster-name"` |

### Authors

- Juergen Kirschbaum (@jgkirschbaum)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
