---
collection: ansible
version: "8"
title: "google.cloud.gcp_iam_service_account module – Creates a GCP ServiceAccount"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_iam_service_account_module.html
fetched_at: 2026-07-28T02:33:13+00:00
---
# google.cloud.gcp_iam_service_account module – Creates a GCP ServiceAccount

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
> see [Requirements](gcp_iam_service_account_module.md#ansible-collections-google-cloud-gcp-iam-service-account-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_iam_service_account`.

- [Synopsis](gcp_iam_service_account_module.md#synopsis)
- [Requirements](gcp_iam_service_account_module.md#requirements)
- [Parameters](gcp_iam_service_account_module.md#parameters)
- [Examples](gcp_iam_service_account_module.md#examples)
- [Return Values](gcp_iam_service_account_module.md#return-values)

## [Synopsis](gcp_iam_service_account_module.md#id1)

- A service account in the Identity and Access Management API.

## [Requirements](gcp_iam_service_account_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_iam_service_account_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **display_name**  string | User specified description of service account. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **name**  string | The name of the service account. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Examples](gcp_iam_service_account_module.md#id4)

```yaml+jinja
- name: create a service account
  google.cloud.gcp_iam_service_account:
    name: sa-{{ resource_name.split("-")[-1] }}@graphite-playground.google.com.iam.gserviceaccount.com
    display_name: My Ansible test key
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_iam_service_account_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **displayName**  string | User specified description of service account.  **Returned:** success |
| **email**  string | Email address of the service account.  **Returned:** success |
| **name**  string | The name of the service account.  **Returned:** success |
| **oauth2ClientId**  string | OAuth2 client id for the service account.  **Returned:** success |
| **projectId**  string | Id of the project that owns the service account.  **Returned:** success |
| **uniqueId**  string | Unique and stable id of the service account.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
