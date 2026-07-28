---
collection: ansible
version: "8"
title: "google.cloud.gcp_iam_service_account_key module – Creates a GCP ServiceAccountKey"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_iam_service_account_key_module.html
fetched_at: 2026-07-28T02:33:14+00:00
---
# google.cloud.gcp_iam_service_account_key module – Creates a GCP ServiceAccountKey

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
> see [Requirements](gcp_iam_service_account_key_module.md#ansible-collections-google-cloud-gcp-iam-service-account-key-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_iam_service_account_key`.

- [Synopsis](gcp_iam_service_account_key_module.md#synopsis)
- [Requirements](gcp_iam_service_account_key_module.md#requirements)
- [Parameters](gcp_iam_service_account_key_module.md#parameters)
- [Examples](gcp_iam_service_account_key_module.md#examples)
- [Return Values](gcp_iam_service_account_key_module.md#return-values)

## [Synopsis](gcp_iam_service_account_key_module.md#id1)

- A service account in the Identity and Access Management API.

## [Requirements](gcp_iam_service_account_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_iam_service_account_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **key_algorithm**  string | Specifies the algorithm for the key.  Some valid choices include: “KEY_ALG_UNSPECIFIED”, “KEY_ALG_RSA_1024”, “KEY_ALG_RSA_2048” |
| **path**  path | The full name of the file that will hold the service account private key.  If the file already exists, it will attempt to be read. Ensure the file does not exist or is alreay a valid key.  File path must be absolute. |
| **private_key_type**  string | Output format for the service account key.  Some valid choices include: “TYPE_UNSPECIFIED”, “TYPE_PKCS12_FILE”, “TYPE_GOOGLE_CREDENTIALS_FILE” |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account**  dictionary | The name of the serviceAccount.  This field represents a link to a ServiceAccount resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘name’ and value of your resource’s name Alternatively, you can add `register: name-of-resource` to a gcp_iam_service_account task and then set this service_account field to “{{ name-of-resource }}” |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Examples](gcp_iam_service_account_key_module.md#id4)

```yaml+jinja
- name: create a service account
  google.cloud.gcp_iam_service_account:
    name: test-ansible@graphite-playground.google.com.iam.gserviceaccount.com
    display_name: My Ansible test key
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: serviceaccount

- name: create a service account key
  google.cloud.gcp_iam_service_account_key:
    service_account: "{{ serviceaccount }}"
    private_key_type: TYPE_GOOGLE_CREDENTIALS_FILE
    path: "~/test_account.json"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_iam_service_account_key_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **keyAlgorithm**  string | Specifies the algorithm for the key.  **Returned:** success |
| **keyType**  string | Specifies the type of the key. Possible values include KEY_TYPE_UNSPECIFIED, USER_MANAGED and SYSTEM_MANAGED .  **Returned:** success |
| **name**  string | The name of the key.  **Returned:** success |
| **path**  string | The full name of the file that will hold the service account private key.  If the file already exists, it will attempt to be read. Ensure the file does not exist or is alreay a valid key.  File path must be absolute.  **Returned:** success |
| **privateKeyData**  string | Private key data. Base-64 encoded.  **Returned:** success |
| **privateKeyType**  string | Output format for the service account key.  **Returned:** success |
| **publicKeyData**  string | Public key data. Base-64 encoded.  **Returned:** success |
| **serviceAccount**  dictionary | The name of the serviceAccount.  **Returned:** success |
| **validAfterTime**  string | Key can only be used after this time.  **Returned:** success |
| **validBeforeTime**  string | Key can only be used before this time.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
