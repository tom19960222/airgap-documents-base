---
collection: ansible
version: "8"
title: "netapp.storagegrid.na_sg_org_user_s3_key module – Creates NetApp StorageGRID User S3 keys."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/storagegrid/na_sg_org_user_s3_key_module.html
fetched_at: 2026-07-28T02:43:59+00:00
---
# netapp.storagegrid.na_sg_org_user_s3_key module – Creates NetApp StorageGRID User S3 keys.

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
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_org_user_s3_key`.

New in netapp.storagegrid 20.6.0

- [Synopsis](na_sg_org_user_s3_key_module.md#synopsis)
- [Parameters](na_sg_org_user_s3_key_module.md#parameters)
- [Notes](na_sg_org_user_s3_key_module.md#notes)
- [Examples](na_sg_org_user_s3_key_module.md#examples)
- [Return Values](na_sg_org_user_s3_key_module.md#return-values)

## [Synopsis](na_sg_org_user_s3_key_module.md#id1)

- Create, Delete Users S3 keys on NetApp StorageGRID.

## [Parameters](na_sg_org_user_s3_key_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_key**  string | Access Key or S3 credential pair identifier.  Required for delete operation. |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **expires**  string | Date-Time string for the key to expire. |
| **state**  string | Whether the specified account should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **unique_user_name**  string / required | Unique user name owning the S3 Key. |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_sg_org_user_s3_key_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_org_user_s3_key_module.md#id4)

```yaml+jinja
- name: create a s3 key
  netapp.storagegrid.na_sg_org_user_s3_key:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    unique_user_name: user/ansibleuser1
```

## [Return Values](na_sg_org_user_s3_key_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  dictionary | Returns information about an S3 access key for the user.  **Returned:** always  **Sample:** `{"accountId": 12345678901234567000, "displayName": "****************AB12", "expires": "2020-09-04T00:00:00.000Z", "id": "abcABC_01234-0123456789abcABCabc0123456789==", "userURN": "urn:sgws:identity::12345678901234567000:root", "userUUID": "00000000-0000-0000-0000-000000000000"}` |

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
