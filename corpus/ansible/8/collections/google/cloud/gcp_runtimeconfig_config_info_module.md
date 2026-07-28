---
collection: ansible
version: "8"
title: "google.cloud.gcp_runtimeconfig_config_info module – Gather info for GCP Config"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_runtimeconfig_config_info_module.html
fetched_at: 2026-07-28T02:33:29+00:00
---
# google.cloud.gcp_runtimeconfig_config_info module – Gather info for GCP Config

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
> see [Requirements](gcp_runtimeconfig_config_info_module.md#ansible-collections-google-cloud-gcp-runtimeconfig-config-info-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_runtimeconfig_config_info`.

- [Synopsis](gcp_runtimeconfig_config_info_module.md#synopsis)
- [Requirements](gcp_runtimeconfig_config_info_module.md#requirements)
- [Parameters](gcp_runtimeconfig_config_info_module.md#parameters)
- [Notes](gcp_runtimeconfig_config_info_module.md#notes)
- [Examples](gcp_runtimeconfig_config_info_module.md#examples)
- [Return Values](gcp_runtimeconfig_config_info_module.md#return-values)

## [Synopsis](gcp_runtimeconfig_config_info_module.md#id1)

- Gather info for GCP Config

## [Requirements](gcp_runtimeconfig_config_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_runtimeconfig_config_info_module.md#id3)

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

## [Notes](gcp_runtimeconfig_config_info_module.md#id4)

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

## [Examples](gcp_runtimeconfig_config_info_module.md#id5)

```yaml+jinja
- name: get info on a config
  gcp_runtimeconfig_config_info:
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
```

## [Return Values](gcp_runtimeconfig_config_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resources**  complex | List of resources  **Returned:** always |
| **description**  string | The description to associate with the runtime config.  **Returned:** success |
| **name**  string | The name of the runtime config.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
