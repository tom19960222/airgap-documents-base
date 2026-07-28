---
collection: ansible
version: "8"
title: "google.cloud.gcp_runtimeconfig_variable module – Creates a GCP Variable"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_runtimeconfig_variable_module.html
fetched_at: 2026-07-28T02:33:29+00:00
---
# google.cloud.gcp_runtimeconfig_variable module – Creates a GCP Variable

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
> see [Requirements](gcp_runtimeconfig_variable_module.md#ansible-collections-google-cloud-gcp-runtimeconfig-variable-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_runtimeconfig_variable`.

- [Synopsis](gcp_runtimeconfig_variable_module.md#synopsis)
- [Requirements](gcp_runtimeconfig_variable_module.md#requirements)
- [Parameters](gcp_runtimeconfig_variable_module.md#parameters)
- [Examples](gcp_runtimeconfig_variable_module.md#examples)
- [Return Values](gcp_runtimeconfig_variable_module.md#return-values)

## [Synopsis](gcp_runtimeconfig_variable_module.md#id1)

- Describes a single variable within a runtime config resource.

## [Requirements](gcp_runtimeconfig_variable_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_runtimeconfig_variable_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **config**  string / required | The name of the runtime config that this variable belongs to. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **name**  string / required | The name of the variable resource. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **text**  string | The string value of the variable. Either this or `value` can be set. |
| **value**  string | The binary value of the variable. Either this or `text` can be set. |

## [Examples](gcp_runtimeconfig_variable_module.md#id4)

```yaml+jinja
- name: create a config
  google.cloud.gcp_runtimeconfig_config:
    name: my-config
    description: My config
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: config

- name: create a variable
  google.cloud.gcp_runtimeconfig_variable:
    name: prod-variables/hostname
    config: my-config
    text: example.com
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_runtimeconfig_variable_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **config**  string | The name of the runtime config that this variable belongs to.  **Returned:** success |
| **name**  string | The name of the variable resource.  **Returned:** success |
| **text**  string | The string value of the variable. Either this or `value` can be set.  **Returned:** success |
| **value**  string | The binary value of the variable. Either this or `text` can be set.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
