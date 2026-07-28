---
collection: ansible
version: "6"
title: "google.cloud.gcp_pubsub_topic module – Creates a GCP Topic"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_pubsub_topic_module.html
fetched_at: 2026-07-27T17:49:15+00:00
---
# google.cloud.gcp_pubsub_topic module – Creates a GCP Topic

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/google/cloud) (version 1.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_pubsub_topic_module.md#ansible-collections-google-cloud-gcp-pubsub-topic-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_pubsub_topic`.

- [Synopsis](gcp_pubsub_topic_module.md#synopsis)
- [Requirements](gcp_pubsub_topic_module.md#requirements)
- [Parameters](gcp_pubsub_topic_module.md#parameters)
- [Notes](gcp_pubsub_topic_module.md#notes)
- [Examples](gcp_pubsub_topic_module.md#examples)
- [Return Values](gcp_pubsub_topic_module.md#return-values)

## [Synopsis](gcp_pubsub_topic_module.md#id1)

- A named resource to which messages are sent by publishers.

## [Requirements](gcp_pubsub_topic_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_pubsub_topic_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **kms_key_name**  string | The resource name of the Cloud KMS CryptoKey to be used to protect access to messages published on this topic. Your project’s PubSub service account ([`service-{{PROJECT_NUMBER}}@gcp-sa-pubsub.iam.gserviceaccount.com](mailto:`service-{{PROJECT_NUMBER}}%40gcp-sa-pubsub.iam.gserviceaccount.com)`) must have `roles/cloudkms.cryptoKeyEncrypterDecrypter` to use this feature.  The expected format is `projects/\*/locations/\*/keyRings/\*/cryptoKeys/\*` . |
| **labels**  dictionary | A set of key/value label pairs to assign to this Topic. |
| **message_storage_policy**  dictionary | Policy constraining the set of Google Cloud Platform regions where messages published to the topic may be stored. If not present, then no constraints are in effect. |
| **allowed_persistence_regions**  list / elements=string / required | A list of IDs of GCP regions where messages that are published to the topic may be persisted in storage. Messages published by publishers running in non-allowed GCP regions (or running outside of GCP altogether) will be routed for storage in one of the allowed regions. An empty list means that no regions are allowed, and is not a valid configuration. |
| **name**  string / required | Name of the topic. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](gcp_pubsub_topic_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics>
> - Managing Topics: <https://cloud.google.com/pubsub/docs/admin#managing_topics>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_pubsub_topic_module.md#id5)

```yaml+jinja
- name: create a topic
  google.cloud.gcp_pubsub_topic:
    name: test-topic1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_pubsub_topic_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **kmsKeyName**  string | The resource name of the Cloud KMS CryptoKey to be used to protect access to messages published on this topic. Your project’s PubSub service account ([`service-{{PROJECT_NUMBER}}@gcp-sa-pubsub.iam.gserviceaccount.com](mailto:`service-{{PROJECT_NUMBER}}%40gcp-sa-pubsub.iam.gserviceaccount.com)`) must have `roles/cloudkms.cryptoKeyEncrypterDecrypter` to use this feature.  The expected format is `projects/\*/locations/\*/keyRings/\*/cryptoKeys/\*` .  Returned: success |
| **labels**  dictionary | A set of key/value label pairs to assign to this Topic.  Returned: success |
| **messageStoragePolicy**  complex | Policy constraining the set of Google Cloud Platform regions where messages published to the topic may be stored. If not present, then no constraints are in effect.  Returned: success |
| **allowedPersistenceRegions**  list / elements=string | A list of IDs of GCP regions where messages that are published to the topic may be persisted in storage. Messages published by publishers running in non-allowed GCP regions (or running outside of GCP altogether) will be routed for storage in one of the allowed regions. An empty list means that no regions are allowed, and is not a valid configuration.  Returned: success |
| **name**  string | Name of the topic.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
