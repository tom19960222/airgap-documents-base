---
collection: ansible
version: "6"
title: "google.cloud.gcp_runtimeconfig_config module – Creates a GCP Config"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_runtimeconfig_config_module.html
fetched_at: 2026-07-27T17:49:19+00:00
---
# google.cloud.gcp_runtimeconfig_config module – Creates a GCP Config

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
> see [Requirements](gcp_runtimeconfig_config_module.md#ansible-collections-google-cloud-gcp-runtimeconfig-config-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_runtimeconfig_config`.

- [Synopsis](gcp_runtimeconfig_config_module.md#synopsis)
- [Requirements](gcp_runtimeconfig_config_module.md#requirements)
- [Parameters](gcp_runtimeconfig_config_module.md#parameters)
- [Examples](gcp_runtimeconfig_config_module.md#examples)
- [Return Values](gcp_runtimeconfig_config_module.md#return-values)

## [Synopsis](gcp_runtimeconfig_config_module.md#id1)

- A RuntimeConfig resource is the primary resource in the Cloud RuntimeConfig service.
- A RuntimeConfig resource consists of metadata and a hierarchy of variables.

## [Requirements](gcp_runtimeconfig_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_runtimeconfig_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **description**  string | The description to associate with the runtime config. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **name**  string / required | The name of the runtime config. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](gcp_runtimeconfig_config_module.md#id4)

```yaml+jinja
- name: create a config
  google.cloud.gcp_runtimeconfig_config:
    name: test_object
    description: My config
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_runtimeconfig_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The description to associate with the runtime config.  Returned: success |
| **name**  string | The name of the runtime config.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
