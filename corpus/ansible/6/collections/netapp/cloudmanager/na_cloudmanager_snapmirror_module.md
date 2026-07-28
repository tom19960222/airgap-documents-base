---
collection: ansible
version: "6"
title: "netapp.cloudmanager.na_cloudmanager_snapmirror module – NetApp Cloud Manager SnapMirror"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/cloudmanager/na_cloudmanager_snapmirror_module.html
fetched_at: 2026-07-28T00:11:40+00:00
---
# netapp.cloudmanager.na_cloudmanager_snapmirror module – NetApp Cloud Manager SnapMirror

> **Note:**
>
> This module is part of the [netapp.cloudmanager collection](https://galaxy.ansible.com/netapp/cloudmanager) (version 21.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.cloudmanager`.
>
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_snapmirror`.

New in netapp.cloudmanager 21.6.0

- [Synopsis](na_cloudmanager_snapmirror_module.md#synopsis)
- [Parameters](na_cloudmanager_snapmirror_module.md#parameters)
- [Notes](na_cloudmanager_snapmirror_module.md#notes)
- [Examples](na_cloudmanager_snapmirror_module.md#examples)

## [Synopsis](na_cloudmanager_snapmirror_module.md#id1)

- Create or Delete SnapMirror relationship on Cloud Manager.

## [Parameters](na_cloudmanager_snapmirror_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **capacity_tier**  string | The volume capacity tier for tiering cold data to object storage.  The default values for each cloud provider are as follows, Amazon ‘S3’, Azure ‘Blob’, GCP ‘cloudStorage’.  If NONE, the capacity tier will not be set on volume creation.  Choices:   - `"S3"` - `"Blob"` - `"cloudStorage"` - `"NONE"` |
| **client_id**  string / required | The connector ID of the Cloud Manager Connector. |
| **destination_aggregate_name**  string | The aggregate in which the volume will be created.  If not provided, Cloud Manager chooses the best aggregate for you. |
| **destination_svm_name**  string | The name of the destination SVM.  The default SVM name is used, if a name is not provided. |
| **destination_volume_name**  string / required | The name of the destination volume to be created for snapmirror relationship. |
| **destination_working_environment_id**  string | The public ID of the working environment of the destination volume. |
| **destination_working_environment_name**  string | The working environment name of the destination volume. |
| **environment**  string  added in netapp.cloudmanager 21.8.0 | The environment for NetApp Cloud Manager API operations.  Choices:   - `"prod"` ← (default) - `"stage"` |
| **feature_flags**  dictionary  added in netapp.cloudmanager 21.11.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **max_transfer_rate**  integer | Maximum transfer rate limit KB/s.  Use 0 for no limit, otherwise use number between 1024 and 2,147,482,624.  Default: `100000` |
| **policy**  string | The SnapMirror policy name.  Default: `"MirrorAllSnapshots"` |
| **provider_volume_type**  string | The underlying cloud provider volume type.  For AWS [‘gp3’, ‘gp2’, ‘io1’, ‘st1’, ‘sc1’].  For Azure [‘Premium_LRS’,’Standard_LRS’,’StandardSSD_LRS’].  For GCP [‘pd-balanced’,’pd-ssd’,’pd-standard’]. |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |
| **schedule**  string | The name of the Schedule.  Default: `"1hour"` |
| **source_svm_name**  string | The name of the source SVM.  The default SVM name is used, if a name is not provided. |
| **source_volume_name**  string / required | The name of the source volume. |
| **source_working_environment_id**  string | The public ID of the working environment of the source volume. |
| **source_working_environment_name**  string | The working environment name of the source volume. |
| **state**  string | Whether the specified snapmirror relationship should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tenant_id**  string  added in netapp.cloudmanager 21.14.0 | The NetApp account ID that the Connector will be associated with. To be used only when using FSx. |

## [Notes](na_cloudmanager_snapmirror_module.md#id3)

> **Note:**
>
> - Support check_mode.
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_snapmirror_module.md#id4)

```yaml+jinja
- name: Create snapmirror with working_environment_name
  netapp.cloudmanager.na_cloudmanager_snapmirror:
    state: present
    source_working_environment_name: source
    destination_working_environment_name: dest
    source_volume_name: source
    destination_volume_name: source_copy
    policy: MirrorAllSnapshots
    schedule: 5min
    max_transfer_rate: 102400
    client_id: client_id
    refresh_token: refresh_token

- name: Delete snapmirror
  netapp.cloudmanager.na_cloudmanager_snapmirror:
    state: absent
    source_working_environment_name: source
    destination_working_environment_name: dest
    source_volume_name: source
    destination_volume_name: source_copy
    client_id: client_id
    refresh_token: refresh_token
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
