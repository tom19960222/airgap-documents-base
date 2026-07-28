---
collection: ansible
version: "8"
title: "google.cloud.gcp_kms_key_ring module – Creates a GCP KeyRing"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_kms_key_ring_module.html
fetched_at: 2026-07-28T02:33:16+00:00
---
# google.cloud.gcp_kms_key_ring module – Creates a GCP KeyRing

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
> see [Requirements](gcp_kms_key_ring_module.md#ansible-collections-google-cloud-gcp-kms-key-ring-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_kms_key_ring`.

- [Synopsis](gcp_kms_key_ring_module.md#synopsis)
- [Requirements](gcp_kms_key_ring_module.md#requirements)
- [Parameters](gcp_kms_key_ring_module.md#parameters)
- [Notes](gcp_kms_key_ring_module.md#notes)
- [Examples](gcp_kms_key_ring_module.md#examples)
- [Return Values](gcp_kms_key_ring_module.md#return-values)

## [Synopsis](gcp_kms_key_ring_module.md#id1)

- A `KeyRing` is a toplevel logical grouping of `CryptoKeys`.

## [Requirements](gcp_kms_key_ring_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_kms_key_ring_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **location**  string / required | The location for the KeyRing.  A full list of valid locations can be found by running `gcloud kms locations list`. |
| **name**  string / required | The resource name for the KeyRing. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](gcp_kms_key_ring_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings>
> - Creating a key ring: <https://cloud.google.com/kms/docs/creating-keys#create_a_key_ring>
> - for authentication, you can set service_account_file using the `GCP_SERVICE_ACCOUNT_FILE` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set access_token using the `GCP_ACCESS_TOKEN` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_kms_key_ring_module.md#id5)

```yaml+jinja
- name: create a key ring
  google.cloud.gcp_kms_key_ring:
    name: test_object
    location: us-central1
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_kms_key_ring_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **createTime**  string | The time that this resource was created on the server.  This is in RFC3339 text format.  **Returned:** success |
| **location**  string | The location for the KeyRing.  A full list of valid locations can be found by running `gcloud kms locations list`.  **Returned:** success |
| **name**  string | The resource name for the KeyRing.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
