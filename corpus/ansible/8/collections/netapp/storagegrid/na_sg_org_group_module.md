---
collection: ansible
version: "8"
title: "netapp.storagegrid.na_sg_org_group module – NetApp StorageGRID manage groups within a tenancy."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/storagegrid/na_sg_org_group_module.html
fetched_at: 2026-07-28T02:43:56+00:00
---
# netapp.storagegrid.na_sg_org_group module – NetApp StorageGRID manage groups within a tenancy.

> **Note:**
>
> This module is part of the [netapp.storagegrid collection](https://galaxy.ansible.com/ui/repo/published/netapp/storagegrid/) (version 21.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.storagegrid`.
>
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_org_group`.

New in netapp.storagegrid 20.6.0

- [Synopsis](na_sg_org_group_module.md#synopsis)
- [Parameters](na_sg_org_group_module.md#parameters)
- [Notes](na_sg_org_group_module.md#notes)
- [Examples](na_sg_org_group_module.md#examples)
- [Return Values](na_sg_org_group_module.md#return-values)

## [Synopsis](na_sg_org_group_module.md#id1)

- Create, Update, Delete Groups within NetApp StorageGRID tenant.

## [Parameters](na_sg_org_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **display_name**  string | Name of the group.  Required for create operation. |
| **management_policy**  dictionary | Management access controls granted to the group within the tenancy. |
| **manage_all_containers**  boolean | Allows users to manage the settings for all S3 buckets in the tenant account, regardless of S3 bucket or group policies.  **Choices:**   - `false` - `true` |
| **manage_endpoints**  boolean | Allows users to use the Tenant Manager or the Tenant Management API to create or edit endpoints.  Endpoints are used as the destination for StorageGRID platform services.  **Choices:**   - `false` - `true` |
| **manage_own_s3_credentials**  boolean | Allows users to create and remove their own S3 access keys.  Users who do not have this permission do not see the S3 > My Credentials menu option.  **Choices:**   - `false` - `true` |
| **root_access**  boolean | Provides full access to the Tenant Manager and the Tenant Management API.  **Choices:**   - `false` - `true` |
| **s3_policy**  json | StorageGRID S3 Group Policy.  **Default:** `""` |
| **state**  string | Whether the specified group should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **unique_name**  string / required | Unique Name for the group. Must begin with `group/` or `federated-group/`.  Required for create, modify or delete operation. |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_sg_org_group_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_org_group_module.md#id4)

```yaml+jinja
- name: create a group
  netapp.storagegrid.na_sg_org_group:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    display_name: ansiblegroup1
    unique_name: group/ansiblegroup1
    management_policy:
      manage_all_containers: true
      manage_endpoints: true
      manage_own_s3_credentials: false
      root_access: false
    s3_policy: {"Statement":[{"Effect":"Deny","Action":"s3:*","Resource":"arn:aws:s3:::*"}]}
```

## [Return Values](na_sg_org_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  dictionary | Returns information about the StorageGRID tenant group attributes.  **Returned:** success  **Sample:** `{"accountId": "12345678901234567890", "displayName": "Example Group", "federated": false, "groupURN": "urn:sgws:identity::12345678901234567890:group/examplegroup", "id": "00000000-0000-0000-0000-000000000000", "policies": {"management": {"manageAllContainers": true, "manageEndpoints": true, "manageOwnS3Credentials": true, "rootAccess": true}, "s3": {"...": null}, "swift": {"...": null}}, "uniqueName": "group/examplegroup"}` |

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
