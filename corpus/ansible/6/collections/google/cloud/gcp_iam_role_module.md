---
collection: ansible
version: "6"
title: "google.cloud.gcp_iam_role module – Creates a GCP Role"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_iam_role_module.html
fetched_at: 2026-07-27T17:49:02+00:00
---
# google.cloud.gcp_iam_role module – Creates a GCP Role

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
> see [Requirements](gcp_iam_role_module.md#ansible-collections-google-cloud-gcp-iam-role-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_iam_role`.

- [Synopsis](gcp_iam_role_module.md#synopsis)
- [Requirements](gcp_iam_role_module.md#requirements)
- [Parameters](gcp_iam_role_module.md#parameters)
- [Examples](gcp_iam_role_module.md#examples)
- [Return Values](gcp_iam_role_module.md#return-values)

## [Synopsis](gcp_iam_role_module.md#id1)

- A role in the Identity and Access Management API .

## [Requirements](gcp_iam_role_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_iam_role_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **description**  string | Human-readable description for the role. |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **included_permissions**  list / elements=string | Names of permissions this role grants when bound in an IAM policy. |
| **name**  string / required | The name of the role. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **stage**  string | The current launch stage of the role.  Some valid choices include: “ALPHA”, “BETA”, “GA”, “DEPRECATED”, “DISABLED”, “EAP” |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |
| **title**  string | A human-readable title for the role. Typically this is limited to 100 UTF-8 bytes. |

## [Examples](gcp_iam_role_module.md#id4)

```yaml+jinja
- name: create a role
  google.cloud.gcp_iam_role:
    name: myCustomRole2
    title: My Custom Role
    description: My custom role description
    included_permissions:
    - iam.roles.list
    - iam.roles.create
    - iam.roles.delete
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_iam_role_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **deleted**  boolean | The current deleted state of the role.  Returned: success |
| **description**  string | Human-readable description for the role.  Returned: success |
| **includedPermissions**  list / elements=string | Names of permissions this role grants when bound in an IAM policy.  Returned: success |
| **name**  string | The name of the role.  Returned: success |
| **stage**  string | The current launch stage of the role.  Returned: success |
| **title**  string | A human-readable title for the role. Typically this is limited to 100 UTF-8 bytes.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
