---
collection: ansible
version: "8"
title: "google.cloud.gcp_pubsub_topic_info module – Gather info for GCP Topic"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_pubsub_topic_info_module.html
fetched_at: 2026-07-28T02:33:24+00:00
---
# google.cloud.gcp_pubsub_topic_info module – Gather info for GCP Topic

> **Note:**
>
> This module is part of the [google.cloud collection](https://galaxy.ansible.com/ui/repo/published/google/cloud/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install google.cloud`.
> You need further requirements to be able to use this module,
> see [Requirements](gcp_pubsub_topic_info_module.md#ansible-collections-google-cloud-gcp-pubsub-topic-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_pubsub_topic_info`.

- [Synopsis](gcp_pubsub_topic_info_module.md#synopsis)
- [Requirements](gcp_pubsub_topic_info_module.md#requirements)
- [Parameters](gcp_pubsub_topic_info_module.md#parameters)
- [Notes](gcp_pubsub_topic_info_module.md#notes)
- [Examples](gcp_pubsub_topic_info_module.md#examples)
- [Return Values](gcp_pubsub_topic_info_module.md#return-values)

## [Synopsis](gcp_pubsub_topic_info_module.md#id1)

- Gather info for GCP Topic

## [Requirements](gcp_pubsub_topic_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_pubsub_topic_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |

## [Notes](gcp_pubsub_topic_info_module.md#id4)

> **Note:**
>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_pubsub_topic_info_module.md#id5)

```yaml+jinja
- name: get info on a topic
  gcp_pubsub_topic_info:
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_pubsub_topic_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  **Returned:** always |
| **kmsKeyName**  string | The resource name of the Cloud KMS CryptoKey to be used to protect access to messages published on this topic. Your project’s PubSub service account ([`service-{{PROJECT_NUMBER}}@gcp-sa-pubsub.iam.gserviceaccount.com](mailto:`service-{{PROJECT_NUMBER}}%40gcp-sa-pubsub.iam.gserviceaccount.com)`) must have `roles/cloudkms.cryptoKeyEncrypterDecrypter` to use this feature.  The expected format is `projects/\*/locations/\*/keyRings/\*/cryptoKeys/\*` .  **Returned:** success |
| **labels**  dictionary | A set of key/value label pairs to assign to this Topic.  **Returned:** success |
| **messageStoragePolicy**  complex | Policy constraining the set of Google Cloud Platform regions where messages published to the topic may be stored. If not present, then no constraints are in effect.  **Returned:** success |
| **allowedPersistenceRegions**  list / elements=string | A list of IDs of GCP regions where messages that are published to the topic may be persisted in storage. Messages published by publishers running in non-allowed GCP regions (or running outside of GCP altogether) will be routed for storage in one of the allowed regions. An empty list means that no regions are allowed, and is not a valid configuration.  **Returned:** success |
| **name**  string | Name of the topic.  **Returned:** success |
| **schemaSettings**  complex | Settings for validating messages published against a schema.  **Returned:** success |
| **encoding**  string | The encoding of messages validated against schema.  **Returned:** success |
| **schema**  string | The name of the schema that messages published should be validated against. Format is projects/{project}/schemas/{schema}.  The value of this field will be _deleted-schema_ if the schema has been deleted.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
