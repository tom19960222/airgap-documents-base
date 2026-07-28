---
collection: ansible
version: "8"
title: "google.cloud.gcp_resourcemanager_project module – Creates a GCP Project"
source_url: https://docs.ansible.com/projects/ansible/8/collections/google/cloud/gcp_resourcemanager_project_module.html
fetched_at: 2026-07-28T02:33:27+00:00
---
# google.cloud.gcp_resourcemanager_project module – Creates a GCP Project

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
> see [Requirements](gcp_resourcemanager_project_module.md#ansible-collections-google-cloud-gcp-resourcemanager-project-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_resourcemanager_project`.

- [Synopsis](gcp_resourcemanager_project_module.md#synopsis)
- [Requirements](gcp_resourcemanager_project_module.md#requirements)
- [Parameters](gcp_resourcemanager_project_module.md#parameters)
- [Examples](gcp_resourcemanager_project_module.md#examples)
- [Return Values](gcp_resourcemanager_project_module.md#return-values)

## [Synopsis](gcp_resourcemanager_project_module.md#id1)

- Represents a GCP Project. A project is a container for ACLs, APIs, App Engine Apps, VMs, and other Google Cloud Platform resources.

## [Requirements](gcp_resourcemanager_project_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_resourcemanager_project_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | An OAuth2 access token if credential type is accesstoken. |
| **auth_kind**  string / required | The type of credential used.  **Choices:**   - `"application"` - `"machineaccount"` - `"serviceaccount"` - `"accesstoken"` |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **id**  string / required | The unique, user-assigned ID of the Project. It must be 6 to 30 lowercase letters, digits, or hyphens. It must start with a letter.  Trailing hyphens are prohibited. |
| **labels**  dictionary | The labels associated with this Project.  Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]\*[a-z0-9])?`.  Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]\*[a-z0-9])?)?`.  No more than 256 labels can be associated with a given resource.  Clients should store labels in a representation such as JSON that does not depend on specific characters being disallowed . |
| **name**  string | The user-assigned display name of the Project. It must be 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point. |
| **parent**  dictionary | A parent organization. |
| **id**  string | Id of the organization. |
| **type**  string | Must be organization. |
| **project**  string | The Google Cloud Platform project to use. |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Examples](gcp_resourcemanager_project_module.md#id4)

```yaml+jinja
- name: create a project
  google.cloud.gcp_resourcemanager_project:
    name: My Sample Project
    id: ansible-test-{{ 10000000000 | random }}
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    parent:
      type: organization
      id: 636173955921
    state: present
```

## [Return Values](gcp_resourcemanager_project_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **createTime**  string | Time of creation.  **Returned:** success |
| **id**  string | The unique, user-assigned ID of the Project. It must be 6 to 30 lowercase letters, digits, or hyphens. It must start with a letter.  Trailing hyphens are prohibited.  **Returned:** success |
| **labels**  dictionary | The labels associated with this Project.  Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]\*[a-z0-9])?`.  Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]\*[a-z0-9])?)?`.  No more than 256 labels can be associated with a given resource.  Clients should store labels in a representation such as JSON that does not depend on specific characters being disallowed .  **Returned:** success |
| **lifecycleState**  string | The Project lifecycle state.  **Returned:** success |
| **name**  string | The user-assigned display name of the Project. It must be 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point.  **Returned:** success |
| **number**  integer | Number uniquely identifying the project.  **Returned:** success |
| **parent**  complex | A parent organization.  **Returned:** success |
| **id**  string | Id of the organization.  **Returned:** success |
| **type**  string | Must be organization.  **Returned:** success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/google.cloud/issues)
- [Homepage](http://cloud.google.com)
- [Repository (Sources)](https://github.com/ansible-collections/google.cloud)
