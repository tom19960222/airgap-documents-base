---
collection: ansible
version: "6"
title: "community.rabbitmq.rabbitmq_binding module – Manage rabbitMQ bindings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/rabbitmq/rabbitmq_binding_module.html
fetched_at: 2026-07-27T17:20:39+00:00
---
# community.rabbitmq.rabbitmq_binding module – Manage rabbitMQ bindings

> **Note:**
>
> This module is part of the [community.rabbitmq collection](https://galaxy.ansible.com/community/rabbitmq) (version 1.2.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.rabbitmq`.
> You need further requirements to be able to use this module,
> see [Requirements](rabbitmq_binding_module.md#ansible-collections-community-rabbitmq-rabbitmq-binding-module-requirements) for details.
>
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_binding`.

- [Synopsis](rabbitmq_binding_module.md#synopsis)
- [Requirements](rabbitmq_binding_module.md#requirements)
- [Parameters](rabbitmq_binding_module.md#parameters)
- [Examples](rabbitmq_binding_module.md#examples)

## [Synopsis](rabbitmq_binding_module.md#id1)

- This module uses rabbitMQ REST APIs to create / delete bindings.

## [Requirements](rabbitmq_binding_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 1.0.0

## [Parameters](rabbitmq_binding_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **arguments**  dictionary | extra arguments for exchange. If defined this argument is a key/value dictionary  Default: `{}` |
| **ca_cert**  aliases: cacert  path | CA certificate to verify SSL connection to management API. |
| **client_cert**  aliases: cert  path | Client certificate to send on SSL connections to management API. |
| **client_key**  aliases: key  path | Private key matching the client certificate. |
| **destination**  aliases: dst, dest  string / required | destination exchange or queue for the binding. |
| **destination_type**  aliases: type, dest_type  string / required | Either queue or exchange.  Choices:   - `"queue"` - `"exchange"` |
| **login_host**  string | RabbitMQ host for connection.  Default: `"localhost"` |
| **login_password**  string | RabbitMQ password for connection.  Default: `"guest"` |
| **login_port**  string | RabbitMQ management API port.  Default: `"15672"` |
| **login_protocol**  string | RabbitMQ management API protocol.  Choices:   - `"http"` ← (default) - `"https"` |
| **login_user**  string | RabbitMQ user for connection.  Default: `"guest"` |
| **name**  aliases: src, source  string / required | source exchange to create binding on. |
| **routing_key**  string | routing key for the binding.  Default: `"#"` |
| **state**  string | Whether the bindings should be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vhost**  string | RabbitMQ virtual host.  Default: `"/"` |

## [Examples](rabbitmq_binding_module.md#id4)

```yaml+jinja
- name: Bind myQueue to directExchange with routing key info
  community.rabbitmq.rabbitmq_binding:
    name: directExchange
    destination: myQueue
    type: queue
    routing_key: info

- name: Bind directExchange to topicExchange with routing key *.info
  community.rabbitmq.rabbitmq_binding:
    name: topicExchange
    destination: topicExchange
    type: exchange
    routing_key: '*.info'
```

### Authors

- Manuel Sousa (@manuel-sousa)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
