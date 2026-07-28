---
collection: ansible
version: "6"
title: "google.cloud.gcp_storage_default_object_acl module – Creates a GCP DefaultObjectACL"
source_url: https://docs.ansible.com/projects/ansible/6/collections/google/cloud/gcp_storage_default_object_acl_module.html
fetched_at: 2026-07-27T17:49:34+00:00
---
# google.cloud.gcp_storage_default_object_acl module – Creates a GCP DefaultObjectACL

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
> see [Requirements](gcp_storage_default_object_acl_module.md#ansible-collections-google-cloud-gcp-storage-default-object-acl-module-requirements) for details.
>
> To use it in a playbook, specify: `google.cloud.gcp_storage_default_object_acl`.

- [Synopsis](gcp_storage_default_object_acl_module.md#synopsis)
- [Requirements](gcp_storage_default_object_acl_module.md#requirements)
- [Parameters](gcp_storage_default_object_acl_module.md#parameters)
- [Notes](gcp_storage_default_object_acl_module.md#notes)
- [Examples](gcp_storage_default_object_acl_module.md#examples)
- [Return Values](gcp_storage_default_object_acl_module.md#return-values)

## [Synopsis](gcp_storage_default_object_acl_module.md#id1)

- The DefaultObjectAccessControls resources represent the Access Control Lists (ACLs) applied to a new object within a Google Cloud Storage bucket when no ACL was provided for that object. ACLs let you specify who has access to your bucket contents and to what extent.
- There are two roles that can be assigned to an entity: READERs can get an object, though the acl property will not be revealed.
- OWNERs are READERs, and they can get the acl property, update an object, and call all objectAccessControls methods on the object. The owner of an object is always an OWNER.
- For more information, see Access Control, with the caveat that this API uses READER and OWNER instead of READ and FULL_CONTROL.

## [Requirements](gcp_storage_default_object_acl_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0

## [Parameters](gcp_storage_default_object_acl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_kind**  string / required | The type of credential used.  Choices:   - `"application"` - `"machineaccount"` - `"serviceaccount"` |
| **bucket**  dictionary / required | The name of the bucket.  This field represents a link to a Bucket resource in GCP. It can be specified in two ways. First, you can place a dictionary with key ‘name’ and value of your resource’s name Alternatively, you can add `register: name-of-resource` to a gcp_storage_bucket task and then set this bucket field to “{{ name-of-resource }}” |
| **entity**  string / required | The entity holding the permission, in one of the following forms: \* user-{{userId}} \* user-{{email}} (such as “[user-liz@example.com](mailto:user-liz%40example.com)”) \* group-{{groupId}} \* group-{{email}} (such as “[group-example@googlegroups.com](mailto:group-example%40googlegroups.com)”) \* domain-{{domain}} (such as “domain-example.com”) \* project-team-{{projectId}} \* allUsers \* allAuthenticatedUsers . |
| **env_type**  string | Specifies which Ansible environment you’re running this module within.  This should not be set unless you know what you’re doing.  This only alters the User Agent string for any API requests. |
| **object**  string | The name of the object, if applied to an object. |
| **project**  string | The Google Cloud Platform project to use. |
| **role**  string / required | The access permission for the entity.  Some valid choices include: “OWNER”, “READER” |
| **scopes**  list / elements=string | Array of scopes to be used |
| **service_account_contents**  jsonarg | The contents of a Service Account JSON file, either in a dictionary or as a JSON string that represents it. |
| **service_account_email**  string | An optional service account email address if machineaccount is selected and the user does not wish to use the default email. |
| **service_account_file**  path | The path of a Service Account JSON file if serviceaccount is selected as type. |
| **state**  string | Whether the given object should exist in GCP  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](gcp_storage_default_object_acl_module.md#id4)

> **Note:**
>
> - API Reference: <https://cloud.google.com/storage/docs/json_api/v1/defaultObjectAccessControls>
> - Official Documentation: <https://cloud.google.com/storage/docs/access-control/create-manage-lists>
> - for authentication, you can set service_account_file using the `gcp_service_account_file` env variable.
> - for authentication, you can set service_account_contents using the `GCP_SERVICE_ACCOUNT_CONTENTS` env variable.
> - For authentication, you can set service_account_email using the `GCP_SERVICE_ACCOUNT_EMAIL` env variable.
> - For authentication, you can set auth_kind using the `GCP_AUTH_KIND` env variable.
> - For authentication, you can set scopes using the `GCP_SCOPES` env variable.
> - Environment variables values will only be used if the playbook values are not set.
> - The *service_account_email* and *service_account_file* options are mutually exclusive.

## [Examples](gcp_storage_default_object_acl_module.md#id5)

```yaml+jinja
- name: create a bucket
  google.cloud.gcp_storage_bucket:
    name: "{{ resource_name }}"
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: bucket

- name: create a default object acl
  google.cloud.gcp_storage_default_object_acl:
    bucket: "{{ bucket }}"
    entity: OWNER:user-alexstephen@google.com
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
```

## [Return Values](gcp_storage_default_object_acl_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bucket**  dictionary | The name of the bucket.  Returned: success |
| **domain**  string | The domain associated with the entity.  Returned: success |
| **email**  string | The email address associated with the entity.  Returned: success |
| **entity**  string | The entity holding the permission, in one of the following forms: \* user-{{userId}} \* user-{{email}} (such as “[user-liz@example.com](mailto:user-liz%40example.com)”) \* group-{{groupId}} \* group-{{email}} (such as “[group-example@googlegroups.com](mailto:group-example%40googlegroups.com)”) \* domain-{{domain}} (such as “domain-example.com”) \* project-team-{{projectId}} \* allUsers \* allAuthenticatedUsers .  Returned: success |
| **entityId**  string | The ID for the entity.  Returned: success |
| **generation**  integer | The content generation of the object, if applied to an object.  Returned: success |
| **id**  string | The ID of the access-control entry.  Returned: success |
| **object**  string | The name of the object, if applied to an object.  Returned: success |
| **projectTeam**  complex | The project team associated with the entity.  Returned: success |
| **projectNumber**  string | The project team associated with the entity.  Returned: success |
| **team**  string | The team.  Returned: success |
| **role**  string | The access permission for the entity.  Returned: success |

### Authors

- Google Inc. (@googlecloudplatform)

### Collection links

[Homepage](http://cloud.google.com)
[Repository (Sources)](http://github.com/ansible/ansible_collections_google)
