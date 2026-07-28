---
collection: ansible
version: "8"
title: "community.rabbitmq.rabbitmq_publish module – Publish a message to a RabbitMQ queue."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/rabbitmq/rabbitmq_publish_module.html
fetched_at: 2026-07-28T01:58:53+00:00
---
# community.rabbitmq.rabbitmq_publish module – Publish a message to a RabbitMQ queue.

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
> see [Requirements](rabbitmq_publish_module.md#ansible-collections-community-rabbitmq-rabbitmq-publish-module-requirements) for details.
>
> To use it in a playbook, specify: `community.rabbitmq.rabbitmq_publish`.

- [Synopsis](rabbitmq_publish_module.md#synopsis)
- [Requirements](rabbitmq_publish_module.md#requirements)
- [Parameters](rabbitmq_publish_module.md#parameters)
- [Notes](rabbitmq_publish_module.md#notes)
- [Examples](rabbitmq_publish_module.md#examples)
- [Return Values](rabbitmq_publish_module.md#return-values)

## [Synopsis](rabbitmq_publish_module.md#id1)

- Publish a message on a RabbitMQ queue using a blocking connection.

## [Requirements](rabbitmq_publish_module.md#id2)

The below requirements are needed on the host that executes this module.

- pika

## [Parameters](rabbitmq_publish_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_delete**  boolean | Set the queue to auto delete.  **Choices:**   - `false` ← (default) - `true` |
| **body**  string | The body of the message.  A `body` cannot be provided if a `src` is specified. |
| **cafile**  string | CA file used during connection to the RabbitMQ server over SSL.  If this option is specified, also *certfile* and *keyfile* must be specified. |
| **certfile**  string | Client certificate to establish SSL connection.  If this option is specified, also *cafile* and *keyfile* must be specified. |
| **content_type**  string | The content type of the body.  **Default:** `"text/plain"` |
| **durable**  boolean | Set the queue to be durable.  **Choices:**   - `false` ← (default) - `true` |
| **exchange**  string | The exchange to publish a message to.  An `exchange` cannot be provided if a `queue` is specified. |
| **exclusive**  boolean | Set the queue to be exclusive.  **Choices:**   - `false` ← (default) - `true` |
| **headers**  dictionary | A dictionary of headers to post with the message.  **Default:** `{}` |
| **host**  string | The RabbitMQ server hostname or IP. |
| **keyfile**  string | Client key to establish SSL connection.  If this option is specified, also *cafile* and *certfile* must be specified. |
| **password**  string | The RabbitMQ password. |
| **port**  integer | The RabbitMQ server port. |
| **proto**  string | The protocol to use.  **Choices:**   - `"amqps"` - `"amqp"` |
| **queue**  string | The queue to publish a message to. If no queue is specified, RabbitMQ will return a random queue name.  A `queue` cannot be provided if an `exchange` is specified. |
| **routing_key**  string | The routing key. |
| **src**  aliases: file  path | A file to upload to the queue. Automatic mime type detection is attempted if content_type is not defined (left as default).  A `src` cannot be provided if a `body` is specified.  The filename is added to the headers of the posted message to RabbitMQ. Key being the `filename`, value is the filename. |
| **url**  string | An URL connection string to connect to the RabbitMQ server.  *url* and *host*/*port*/*user*/*pass*/*vhost* are mutually exclusive, use either or but not both. |
| **username**  string | The RabbitMQ username. |
| **vhost**  string | The virtual host to target.  If default vhost is required, use `'%2F'`. |

## [Notes](rabbitmq_publish_module.md#id4)

> **Note:**
>
> - This module requires the pika python library <https://pika.readthedocs.io/>.
> - Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that tries to stay fairly independent of the underlying network support library.
> - This module is tested against RabbitMQ. Other AMQP 0.9.1 protocol based servers may work but not tested/guaranteed.
> - The certificate authentication was tested with certificates created via <https://www.rabbitmq.com/ssl.html#automated-certificate-generation> and RabbitMQ configuration variables `ssl_options.verify = verify_peer` & `ssl_options.fail_if_no_peer_cert = true`.

## [Examples](rabbitmq_publish_module.md#id5)

```yaml+jinja
- name: Publish to an exchange
  community.rabbitmq.rabbitmq_publish:
    exchange: exchange1
    url: "amqp://guest:guest@192.168.0.32:5672/%2F"
    body: "Hello exchange from ansible module rabbitmq_publish"
    content_type: "text/plain"

- name: Publish to an exchange with routing_key
  community.rabbitmq.rabbitmq_publish:
    exchange: exchange1
    routing_key: queue1
    url: "amqp://guest:guest@192.168.0.32:5672/%2F"
    body: "Hello queue via exchange routing_key from ansible module rabbitmq_publish"
    content_type: "text/plain"

- name: Publish a message to a queue with headers
  community.rabbitmq.rabbitmq_publish:
    url: "amqp://guest:guest@192.168.0.32:5672/%2F"
    queue: 'test'
    body: "Hello world from ansible module rabbitmq_publish"
    content_type: "text/plain"
    headers:
      myHeader: myHeaderValue

- name: Publish a file to a queue
  community.rabbitmq.rabbitmq_publish:
    url: "amqp://guest:guest@192.168.0.32:5672/%2F"
    queue: 'images'
    file: 'path/to/logo.gif'

- name: RabbitMQ auto generated queue
  community.rabbitmq.rabbitmq_publish:
    url: "amqp://guest:guest@192.168.0.32:5672/%2F"
    body: "Hello world random queue from ansible module rabbitmq_publish"
    content_type: "text/plain"

- name: Publish with certs
  community.rabbitmq.rabbitmq_publish:
    url: "amqps://guest:guest@192.168.0.32:5671/%2F"
    body: "Hello test queue from ansible module rabbitmq_publish via SSL certs"
    queue: 'test'
    content_type: "text/plain"
    cafile: 'ca_certificate.pem'
    certfile: 'client_certificate.pem'
    keyfile: 'client_key.pem'
```

## [Return Values](rabbitmq_publish_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | If posted to an exchange, the result contains the status *msg*, content type *content_type* the exchange name *exchange*  and the routing key *routing_key*.  If posted to a queue, the result contains the status *msg*, content type *content_type* and the queue name *queue*.  **Returned:** success  **Sample:** `"'result': { 'content_type': 'text/plain', 'msg': 'Successfully published to queue test', 'queue': 'test' }\n"` |

### Authors

- John Imison (@Im0)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.rabbitmq/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.rabbitmq)
