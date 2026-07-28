---
collection: ansible
version: "8"
title: "community.google.gcpubsub_info module – List Topics/Subscriptions and Messages from Google PubSub."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/google/gcpubsub_info_module.html
fetched_at: 2026-07-28T01:53:11+00:00
---
# community.google.gcpubsub_info module – List Topics/Subscriptions and Messages from Google PubSub.

> **Note:**
>
> This module is part of the [community.google collection](https://galaxy.ansible.com/ui/repo/published/community/google/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.google`.
> You need further requirements to be able to use this module,
> see [Requirements](gcpubsub_info_module.md#ansible-collections-community-google-gcpubsub-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.google.gcpubsub_info`.

- [Synopsis](gcpubsub_info_module.md#synopsis)
- [Requirements](gcpubsub_info_module.md#requirements)
- [Parameters](gcpubsub_info_module.md#parameters)
- [Notes](gcpubsub_info_module.md#notes)
- [Examples](gcpubsub_info_module.md#examples)
- [Return Values](gcpubsub_info_module.md#return-values)

## [Synopsis](gcpubsub_info_module.md#id1)

- List Topics/Subscriptions from Google PubSub. Use the gcpubsub module for topic/subscription management. See <https://cloud.google.com/pubsub/docs> for an overview.
- This module was called `gcpubsub_facts` before Ansible 2.9. The usage did not change.

Aliases: gcpubsub_facts

## [Requirements](gcpubsub_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- google-auth >= 0.5.0
- google-cloud-pubsub >= 0.22.0

## [Parameters](gcpubsub_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **credentials_file**  string | path to the JSON file associated with the service account email |
| **project_id**  string | your GCE project ID |
| **service_account_email**  string | service account email |
| **state**  string | list is the only valid option.  **Choices:**   - `"list"` ← (default) |
| **topic**  string | GCP pubsub topic name. Only the name, not the full path, is required. |
| **view**  string | Choices are ‘topics’ or ‘subscriptions’  **Choices:**   - `"topics"` ← (default) - `"subscriptions"` |

## [Notes](gcpubsub_info_module.md#id4)

> **Note:**
>
> - list state enables user to list topics or subscriptions in the project. See examples for details.

## [Examples](gcpubsub_info_module.md#id5)

```yaml+jinja
- name: List all Topics in a project
  community.google.gcpubsub_info:
    view: topics
    state: list

- name: List all Subscriptions in a project
  community.google.gcpubsub_info:
    view: subscriptions
    state: list

- name: List all Subscriptions for a Topic in a project
  community.google.gcpubsub_info:
    view: subscriptions
    topic: my-topic
    state: list
```

## [Return Values](gcpubsub_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **subscriptions**  list / elements=string | List of subscriptions.  **Returned:** When view is set to subscriptions.  **Sample:** `["mysubscription", "mysubscription2"]` |
| **topic**  string | Name of topic. Used to filter subscriptions.  **Returned:** Always  **Sample:** `"mytopic"` |
| **topics**  list / elements=string | List of topics.  **Returned:** When view is set to topics.  **Sample:** `["mytopic", "mytopic2"]` |

### Authors

- Tom Melendez (@supertom)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.google/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.google)
