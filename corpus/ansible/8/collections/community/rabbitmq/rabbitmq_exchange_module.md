---
collection: ansible
version: "8"
title: "community.rabbitmq.rabbitmq_exchange module – Manage rabbitMQ exchange"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/rabbitmq/rabbitmq_exchange_module.html
fetched_at: 2026-07-28T01:58:49+00:00
---
# community.rabbitmq.rabbitmq_exchange module – Manage rabbitMQ exchange

> **Note:**
>
> This module is part of the [community.rabbitmq collection](https://galaxy.ansible.com/ui/repo/published/community/rabbitmq/) (version 1.2.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.rabbitmq`.
> You need further requirements to be able to use this module,
> see [Requirements](rabbitmq_exchange_module.md#ansible-collections-community-rabbitmq-rabbitmq-exchange-module-requirements) for details.
>
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_exchange`.

- [Synopsis](rabbitmq_exchange_module.md#synopsis)
- [Requirements](rabbitmq_exchange_module.md#requirements)
- [Parameters](rabbitmq_exchange_module.md#parameters)
- [Examples](rabbitmq_exchange_module.md#examples)

## [Synopsis](rabbitmq_exchange_module.md#id1)

- This module uses rabbitMQ Rest API to create/delete exchanges

## [Requirements](rabbitmq_exchange_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 1.0.0

## [Parameters](rabbitmq_exchange_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **arguments**  dictionary | Extra arguments for exchange. If defined this argument is a key/value dictionary.  **Default:** `{}` |
| **auto_delete**  boolean | If the exchange should delete itself after all queues/exchanges unbound from it.  **Choices:**   - `false` ← (default) - `true` |
| **ca_cert**  aliases: cacert  path | CA certificate to verify SSL connection to management API. |
| **client_cert**  aliases: cert  path | Client certificate to send on SSL connections to management API. |
| **client_key**  aliases: key  path | Private key matching the client certificate. |
| **durable**  boolean | Whether exchange is durable or not.  **Choices:**   - `false` - `true` ← (default) |
| **exchange_type**  aliases: type  string | Type for the exchange.  If using *x-delayed-message*, *x-random*, *x-consistent-hash* or *x-recent-history* the respective plugin on  the RabbitMQ server must be enabled.  **Choices:**   - `"fanout"` - `"direct"` ← (default) - `"headers"` - `"topic"` - `"x-delayed-message"` - `"x-random"` - `"x-consistent-hash"` - `"x-recent-history"` |
| **internal**  boolean | Exchange is available only for other exchanges.  **Choices:**   - `false` ← (default) - `true` |
| **login_host**  string | RabbitMQ host for connection.  **Default:** `"localhost"` |
| **login_password**  string | RabbitMQ password for connection.  **Default:** `"guest"` |
| **login_port**  string | RabbitMQ management API port.  **Default:** `"15672"` |
| **login_protocol**  string | RabbitMQ management API protocol.  **Choices:**   - `"http"` ← (default) - `"https"` |
| **login_user**  string | RabbitMQ user for connection.  **Default:** `"guest"` |
| **name**  string / required | Name of the exchange to create. |
| **state**  string | Whether the exchange should be present or absent.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vhost**  string | RabbitMQ virtual host.  **Default:** `"/"` |

## [Examples](rabbitmq_exchange_module.md#id4)

```yaml+jinja
- name: Create direct exchange
  community.rabbitmq.rabbitmq_exchange:
    name: directExchange

- name: Create topic exchange on vhost
  community.rabbitmq.rabbitmq_exchange:
    name: topicExchange
    type: topic
    vhost: myVhost
```

### Authors

- Manuel Sousa (@manuel-sousa)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
