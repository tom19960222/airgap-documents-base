---
collection: ansible
version: "8"
title: "google.cloud.gcp_sql_user module – Creates a GCP User"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_sql_user_module.html
fetched_at: 2026-07-28T02:33:41+00:00
---
# google.cloud.gcp_sql_user module – Creates a GCP User

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
> see [Requirements](gcp_sql_user_module.md#ansible-collections-google-cloud-gcp-sql-user-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_sql_user`.

- [Synopsis](gcp_sql_user_module.md#synopsis)
- [Requirements](gcp_sql_user_module.md#requirements)
- [Parameters](gcp_sql_user_module.md#parameters)
- [Examples](gcp_sql_user_module.md#examples)
- [Return Values](gcp_sql_user_module.md#return-values)

## [Synopsis](gcp_sql_user_module.md#id1)

- The Users resource represents a database user in a Cloud SQL instance.

## [Requirements](gcp_sql_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_sql_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **host**  string / required | The host name from which the user can connect. For insert operations, host defaults to an empty string. For update operations, host is specified as part of the request URL. The host name cannot be updated after insertion. |
| **instance**  dictionary / required | The name of the Cloud SQL instance. This does not include the project ID.  This field represents a link to a Instance resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘name’ and value of your resource’s name Alternatively, you can add `register: name-of-resource` to a gcp_sql_instance task and then set this instance field to “{{ name-of-resource }}” |
| **name**  string / required | The name of the user in the Cloud SQL instance. |
| **password**  string | The password for the user. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Examples](gcp_sql_user_module.md#id4)

```yaml+jinja
- name: create a instance
  google.cloud.gcp_sql_instance:
    name: "{{resource_name}}-1"
    settings:
      ip_configuration:
        authorized_networks:
        - name: google dns server
          value: 8.8.8.8/32
      tier: db-n1-standard-1
    region: us-central1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: instance

- name: create a user
  google.cloud.gcp_sql_user:
    name: test-user
    host: 10.1.2.3
    password: secret-password
    instance: "{{ instance }}"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_sql_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **host**  string | The host name from which the user can connect. For insert operations, host defaults to an empty string. For update operations, host is specified as part of the request URL. The host name cannot be updated after insertion.  **Returned:** success |
| **instance**  dictionary | The name of the Cloud SQL instance. This does not include the project ID.  **Returned:** success |
| **name**  string | The name of the user in the Cloud SQL instance.  **Returned:** success |
| **password**  string | The password for the user.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
