---
collection: ansible
version: "6"
title: "community.rabbitmq.rabbitmq_queue module – Manage rabbitMQ queues"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/rabbitmq/rabbitmq_queue_module.html
fetched_at: 2026-07-27T17:20:45+00:00
---
# community.rabbitmq.rabbitmq_queue module – Manage rabbitMQ queues

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
> see [Requirements](rabbitmq_queue_module.md#ansible-collections-community-rabbitmq-rabbitmq-queue-module-requirements) for details.
>
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_queue`.

- [Synopsis](rabbitmq_queue_module.md#synopsis)
- [Requirements](rabbitmq_queue_module.md#requirements)
- [Parameters](rabbitmq_queue_module.md#parameters)
- [Examples](rabbitmq_queue_module.md#examples)

## [Synopsis](rabbitmq_queue_module.md#id1)

- This module uses rabbitMQ Rest API to create/delete queues.
- Due to limitations in the API, it cannot modify existing queues.

## [Requirements](rabbitmq_queue_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests >= 1.0.0

## [Parameters](rabbitmq_queue_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **arguments**  dictionary | extra arguments for queue. If defined this argument is a key/value dictionary  Arguments here take precedence over parameters. If both are defined, the argument will be used.  Default: `{}` |
| **auto_delete**  boolean | if the queue should delete itself after all queues/queues unbound from it.  Choices:   - `false` ← (default) - `true` |
| **auto_expires**  integer | How long a queue can be unused before it is automatically deleted (milliseconds). |
| **ca_cert**  aliases: cacert  path | CA certificate to verify SSL connection to management API. |
| **client_cert**  aliases: cert  path | Client certificate to send on SSL connections to management API. |
| **client_key**  aliases: key  path | Private key matching the client certificate. |
| **dead_letter_exchange**  string | Optional name of an exchange to which messages will be republished if they  are rejected or expire. |
| **dead_letter_routing_key**  string | Optional replacement routing key to use when a message is dead-lettered.  Original routing key will be used if unset. |
| **durable**  boolean | whether queue is durable or not.  Choices:   - `false` - `true` ← (default) |
| **login_host**  string | RabbitMQ host for connection.  Default: `"localhost"` |
| **login_password**  string | RabbitMQ password for connection.  Default: `"guest"` |
| **login_port**  string | RabbitMQ management API port.  Default: `"15672"` |
| **login_protocol**  string | RabbitMQ management API protocol.  Choices:   - `"http"` ← (default) - `"https"` |
| **login_user**  string | RabbitMQ user for connection.  Default: `"guest"` |
| **max_length**  integer | How many messages can the queue contain before it starts rejecting. |
| **max_priority**  integer | Maximum number of priority levels for the queue to support.  If not set, the queue will not support message priorities.  Larger numbers indicate higher priority. |
| **message_ttl**  integer | How long a message can live in queue before it is discarded (milliseconds). |
| **name**  string / required | Name of the queue. |
| **state**  string | Whether the queue should be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vhost**  string | RabbitMQ virtual host.  Default: `"/"` |

## [Examples](rabbitmq_queue_module.md#id4)

```yaml+jinja
- name: Create a queue
  community.rabbitmq.rabbitmq_queue:
    name: myQueue

- name: Create a queue on remote host
  community.rabbitmq.rabbitmq_queue:
    name: myRemoteQueue
    login_user: user
    login_password: secret
    login_host: remote.example.org

# You may specify different types of queues using the arguments parameter.
- name: Create RabbitMQ stream
  become: yes
  community.rabbitmq.rabbitmq_queue:
    name: test-x
    arguments:
      x-queue-type: stream
      x-max-age: 24h
```

### Authors

- Manuel Sousa (@manuel-sousa)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
