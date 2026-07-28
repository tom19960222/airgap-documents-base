---
collection: ansible
version: "8"
title: "netapp.storagegrid.na_sg_org_container module – Manage buckets on StorageGRID."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/storagegrid/na_sg_org_container_module.html
fetched_at: 2026-07-28T02:43:55+00:00
---
# netapp.storagegrid.na_sg_org_container module – Manage buckets on StorageGRID.

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
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_org_container`.

New in netapp.storagegrid 20.6.0

- [Synopsis](na_sg_org_container_module.md#synopsis)
- [Parameters](na_sg_org_container_module.md#parameters)
- [Notes](na_sg_org_container_module.md#notes)
- [Examples](na_sg_org_container_module.md#examples)
- [Return Values](na_sg_org_container_module.md#return-values)

## [Synopsis](na_sg_org_container_module.md#id1)

- Create S3 buckets on NetApp StorageGRID.

## [Parameters](na_sg_org_container_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **bucket_versioning_enabled**  boolean  *added in netapp.storagegrid 21.11.0* | Enable versioning on the bucket.  This API requires StorageGRID 11.6 or greater.  **Choices:**   - `false` - `true` |
| **compliance**  dictionary | Configure compliance settings for an S3 bucket.  Cannot be specified along with *s3_object_lock_enabled*. |
| **auto_delete**  boolean | If enabled, objects will be deleted automatically when its retention period expires, unless the bucket is under a legal hold.  **Choices:**   - `false` - `true` |
| **legal_hold**  boolean | If enabled, objects in this bucket cannot be deleted, even if their retention period has expired.  **Choices:**   - `false` - `true` |
| **retention_period_minutes**  integer | specify the length of the retention period for objects added to this bucket, in minutes. |
| **name**  string / required | Name of the bucket. |
| **region**  string | Set a region for the bucket. |
| **s3_object_lock_enabled**  boolean  *added in netapp.storagegrid 21.9.0* | Enable S3 Object Lock on the bucket.  S3 Object Lock requires StorageGRID 11.5 or greater.  **Choices:**   - `false` - `true` |
| **state**  string | Whether the specified bucket should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_sg_org_container_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_org_container_module.md#id4)

```yaml+jinja
- name: create a s3 bucket
  netapp.storagegrid.na_sg_org_container:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    name: ansiblebucket1

- name: delete a s3 bucket
  netapp.storagegrid.na_sg_org_container:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: absent
    name: ansiblebucket1

- name: create a s3 bucket with Object Lock
  netapp.storagegrid.na_sg_org_container:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    name: objectlock-bucket1
    s3_object_lock_enabled: true

- name: create a s3 bucket with versioning enabled
  netapp.storagegrid.na_sg_org_container:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    validate_certs: false
    state: present
    name: ansiblebucket1
    bucket_versioning_enabled: true
```

## [Return Values](na_sg_org_container_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  dictionary | Returns information about the StorageGRID bucket.  **Returned:** always  **Sample:** `{"compliance": {"autoDelete": false, "legalHold": false, "retentionPeriodMinutes": 2629800}, "creationTime": "2021-01-01T00:00:00.000Z", "name": "example-bucket", "region": "us-east-1", "s3ObjectLock": {"enabled": false}}` |

### Authors

- NetApp Ansible Team (@joshedmonds)

### Collection links

- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
