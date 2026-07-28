---
collection: ansible
version: "8"
title: "community.rabbitmq.rabbitmq lookup – Retrieve messages from an AMQP/AMQPS RabbitMQ queue."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/rabbitmq/rabbitmq_lookup.html
fetched_at: 2026-07-28T01:58:58+00:00
---
# community.rabbitmq.rabbitmq lookup – Retrieve messages from an AMQP/AMQPS RabbitMQ queue.

> **Note:**
>
> This lookup plugin is part of the [community.rabbitmq collection](https://galaxy.ansible.com/ui/repo/published/community/rabbitmq/) (version 1.2.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.rabbitmq`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](rabbitmq_lookup.md#ansible-collections-community-rabbitmq-rabbitmq-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq`.

- [Synopsis](rabbitmq_lookup.md#synopsis)
- [Requirements](rabbitmq_lookup.md#requirements)
- [Keyword parameters](rabbitmq_lookup.md#keyword-parameters)
- [Notes](rabbitmq_lookup.md#notes)
- [Examples](rabbitmq_lookup.md#examples)
- [Return Value](rabbitmq_lookup.md#return-value)

## [Synopsis](rabbitmq_lookup.md#id1)

- This lookup uses a basic get to retrieve all, or a limited number `count`, messages from a RabbitMQ queue.

## [Requirements](rabbitmq_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- The python pika package <https://pypi.org/project/pika/>.

## [Keyword parameters](rabbitmq_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.rabbitmq.rabbitmq', key1=value1, key2=value2, ...)` and `query('community.rabbitmq.rabbitmq', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **count**  string | How many messages to collect from the queue.  If not set, defaults to retrieving all the messages from the queue. |
| **queue**  string / required | The queue to get messages from. |
| **url**  string / required | An URI connection string to connect to the AMQP/AMQPS RabbitMQ server.  For more information refer to the URI spec <https://www.rabbitmq.com/uri-spec.html>. |

## [Notes](rabbitmq_lookup.md#id4)

> **Note:**
>
> - This lookup implements BlockingChannel.basic_get to get messages from a RabbitMQ server.
> - After retrieving a message from the server, receipt of the message is acknowledged and the message on the server is deleted.
> - Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that tries to stay fairly independent of the underlying network support library.
> - More information about pika can be found at <https://pika.readthedocs.io/en/stable/>.
> - This plugin is tested against RabbitMQ. Other AMQP 0.9.1 protocol based servers may work but not tested/guaranteed.
> - Assigning the return messages to a variable under `vars` may result in unexpected results as the lookup is evaluated every time the variable is referenced.
> - Currently this plugin only handles text based messages from a queue. Unexpected results may occur when retrieving binary data.

## [Examples](rabbitmq_lookup.md#id5)

```yaml+jinja
- name: Get all messages off a queue
  debug:
    msg: "{{ lookup('community.rabbitmq.rabbitmq', url='amqp://guest:guest@192.168.0.10:5672/%2F', queue='hello') }}"

# If you are intending on using the returned messages as a variable in more than
# one task (eg. debug, template), it is recommended to set_fact.

- name: Get 2 messages off a queue and set a fact for re-use
  set_fact:
    messages: "{{ lookup('community.rabbitmq.rabbiotmq', url='amqp://guest:guest@192.168.0.10:5672/%2F', queue='hello', count=2) }}"

- name: Dump out contents of the messages
  debug:
    var: messages
```

## [Return Value](rabbitmq_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A list of dictionaries with keys and value from the queue.  **Returned:** success |
| **content_type**  string | The content_type on the message in the queue.  **Returned:** success |
| **delivery_mode**  string | The delivery_mode on the message in the queue.  **Returned:** success |
| **delivery_tag**  string | The delivery_tag on the message in the queue.  **Returned:** success |
| **exchange**  string | The exchange the message came from.  **Returned:** success |
| **headers**  dictionary | The headers for the message returned from the queue.  **Returned:** success |
| **json**  dictionary | If application/json is specified in content_type, json will be loaded into variables.  **Returned:** success |
| **message_count**  string | The message_count for the message on the queue.  **Returned:** success |
| **msg**  string | The content of the message.  **Returned:** success |
| **redelivered**  boolean | The redelivered flag. True if the message has been delivered before.  **Returned:** success |
| **routing_key**  string | The routing_key on the message in the queue.  **Returned:** success |

### Authors

- John Imison (@Im0)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
