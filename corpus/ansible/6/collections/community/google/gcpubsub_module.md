---
collection: ansible
version: "6"
title: "community.google.gcpubsub module – Create and Delete Topics/Subscriptions, Publish and pull messages on PubSub"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/google/gcpubsub_module.html
fetched_at: 2026-07-27T17:15:23+00:00
---
# community.google.gcpubsub module – Create and Delete Topics/Subscriptions, Publish and pull messages on PubSub

> **Note:**
>
> This module is part of the [community.google collection](https://galaxy.ansible.com/community/google) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.google`.
> You need further requirements to be able to use this module,
> see [Requirements](gcpubsub_module.md#ansible-collections-community-google-gcpubsub-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gcpubsub`.

- [Synopsis](gcpubsub_module.md#synopsis)
- [Requirements](gcpubsub_module.md#requirements)
- [Parameters](gcpubsub_module.md#parameters)
- [Notes](gcpubsub_module.md#notes)
- [Examples](gcpubsub_module.md#examples)
- [Return Values](gcpubsub_module.md#return-values)

## [Synopsis](gcpubsub_module.md#id1)

- Create and Delete Topics/Subscriptions, Publish and pull messages on PubSub. See <https://cloud.google.com/pubsub/docs> for an overview.

## [Requirements](gcpubsub_module.md#id2)

The below requirements are needed on the host that executes this module.

- google-auth >= 0.5.0
- google-cloud-pubsub >= 0.22.0

## [Parameters](gcpubsub_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **credentials_file**  string | path to the JSON file associated with the service account email |
| **project_id**  string | your GCE project ID |
| **publish**  list / elements=string | List of dictionaries describing messages and attributes to be published. Dictionary is in message(str):attributes(dict) format. Only message is required. |
| **service_account_email**  string | service account email |
| **state**  string | State of the topic or queue.  Applies to the most granular resource.  If subscription isspecified we remove it.  If only topic is specified, that is what is removed.  NOTE - A topic can be removed without first removing the subscription.  Choices:   - `"absent"` - `"present"` ← (default) |
| **subscription**  dictionary | Dictionary containing a subscription name associated with a topic (required), along with optional ack_deadline, push_endpoint and pull. For pulling from a subscription, message_ack (bool), max_messages (int) and return_immediate are available as subfields. See subfields name, push_endpoint and ack_deadline for more information. |
| **ack_deadline**  string | Subfield of subscription. Not required. Default deadline for subscriptions to ACK the message before it is resent. See examples. |
| **name**  string | Subfield of subscription. Required if subscription is specified. See examples. |
| **pull**  string | Subfield of subscription. Not required. If specified, messages will be retrieved from topic via the provided subscription name. max_messages (int; default None; max number of messages to pull), message_ack (bool; default False; acknowledge the message) and return_immediately (bool; default True, don’t wait for messages to appear). If the messages are acknowledged, changed is set to True, otherwise, changed is False. |
| **push_endpoint**  string | Subfield of subscription. Not required. If specified, message will be sent to an endpoint. See <https://cloud.google.com/pubsub/docs/advanced#push_endpoints> for more information. |
| **topic**  string / required | GCP pubsub topic name.  Only the name, not the full path, is required. |

## [Notes](gcpubsub_module.md#id4)

> **Note:**
>
> - Subscription pull happens before publish. You cannot publish and pull in the same task.

## [Examples](gcpubsub_module.md#id5)

```yaml+jinja
# (Message will be pushed; there is no check to see if the message was pushed before
- name: Create a topic and publish a message to it
  community.google.gcpubsub:
    topic: ansible-topic-example
    state: present

# Subscriptions associated with topic are not deleted.
- name: Delete Topic
  community.google.gcpubsub:
    topic: ansible-topic-example
    state: absent

# Setting absent will keep the messages from being sent
- name: Publish multiple messages, with attributes (key:value available with the message)
  community.google.gcpubsub:
    topic: '{{ topic_name }}'
    state: present
    publish:
      - message: this is message 1
        attributes:
          mykey1: myvalue
          mykey2: myvalu2
          mykey3: myvalue3
      - message: this is message 2
        attributes:
          server: prod
          sla: "99.9999"
          owner: fred

- name: Create Subscription (pull)
  community.google.gcpubsub:
    topic: ansible-topic-example
    subscription:
    - name: mysub
    state: present

# pull is default, ack_deadline is not required
- name: Create Subscription with ack_deadline and push endpoint
  community.google.gcpubsub:
    topic: ansible-topic-example
    subscription:
    - name: mysub
      ack_deadline: "60"
      push_endpoint: http://pushendpoint.example.com
    state: present

# Setting push_endpoint to "None" converts subscription to pull.
- name: Subscription change from push to pull
  community.google.gcpubsub:
    topic: ansible-topic-example
    subscription:
      name: mysub
      push_endpoint: "None"

### Topic will not be deleted
- name: Delete subscription
  community.google.gcpubsub:
    topic: ansible-topic-example
    subscription:
    - name: mysub
    state: absent

# only pull keyword is required.
- name: Pull messages from subscription
  community.google.gcpubsub:
    topic: ansible-topic-example
    subscription:
      name: ansible-topic-example-sub
      pull:
        message_ack: yes
        max_messages: "100"
```

## [Return Values](gcpubsub_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **publish**  list / elements=string | List of dictionaries describing messages and attributes to be published. Dictionary is in message(str):attributes(dict) format. Only message is required.  Returned: Only when specified  Sample: `["publish: ['message': 'my message'", " attributes: {'key1': 'value1'}]"]` |
| **pulled_messages**  list / elements=string | list of dictionaries containing message info. Fields are ack_id, attributes, data, message_id.  Returned: Only when subscription.pull is specified  Sample: `[{"ack_id": "XkASTCcYREl...", "attributes": {"...": null, "key1": "val1"}, "data": "this is message 1", "message_id": "49107464153705"}, ".."]` |
| **state**  string | The state of the topic or subscription. Value will be either ‘absent’ or ‘present’.  Returned: Always  Sample: `"present"` |
| **subscription**  string | Name of subscription.  Returned: When subscription fields are specified  Sample: `"mysubscription"` |
| **topic**  string | Name of topic.  Returned: Always  Sample: `"mytopic"` |

### Authors

- Tom Melendez (@supertom)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.google/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.google)
