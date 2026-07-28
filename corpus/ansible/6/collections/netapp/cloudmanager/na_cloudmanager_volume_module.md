---
collection: ansible
version: "6"
title: "netapp.cloudmanager.na_cloudmanager_volume module – NetApp Cloud Manager volume"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/cloudmanager/na_cloudmanager_volume_module.html
fetched_at: 2026-07-28T00:11:41+00:00
---
# netapp.cloudmanager.na_cloudmanager_volume module – NetApp Cloud Manager volume

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
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_volume`.

New in netapp.cloudmanager 21.3.0

- [Synopsis](na_cloudmanager_volume_module.md#synopsis)
- [Parameters](na_cloudmanager_volume_module.md#parameters)
- [Notes](na_cloudmanager_volume_module.md#notes)
- [Examples](na_cloudmanager_volume_module.md#examples)

## [Synopsis](na_cloudmanager_volume_module.md#id1)

- Create, Modify or Delete volume on Cloud Manager.

## [Parameters](na_cloudmanager_volume_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate_name**  string | The aggregate in which the volume will be created. If not provided, Cloud Manager chooses the best aggregate. |
| **capacity_tier**  string | The volume’s capacity tier for tiering cold data to object storage.  The default values for each cloud provider are as follows. Amazon as ‘S3’, Azure as ‘Blob’, GCP as ‘cloudStorage’.  If ‘NONE’, the capacity tier will not be set on volume creation.  Choices:   - `"NONE"` - `"S3"` - `"Blob"` - `"cloudStorage"` |
| **client_id**  string / required | The connector ID of the Cloud Manager Connector. |
| **enable_compression**  boolean | Enabling cpmpression.  Default to true if not specified.  Choices:   - `false` - `true` |
| **enable_deduplication**  boolean | Enabling deduplication.  Default to true if not specified.  Choices:   - `false` - `true` |
| **enable_thin_provisioning**  boolean | Enabling thin provisioning.  Default to true if not specified.  Choices:   - `false` - `true` |
| **environment**  string  added in netapp.cloudmanager 21.8.0 | The environment for NetApp Cloud Manager API operations.  Choices:   - `"prod"` ← (default) - `"stage"` |
| **export_policy_ip**  list / elements=string | Custom export policy list of IPs (NFS protocol parameters). |
| **export_policy_nfs_version**  list / elements=string | Export policy protocol (NFS protocol parameters). |
| **export_policy_type**  string | The export policy type (NFS protocol parameters). |
| **feature_flags**  dictionary  added in netapp.cloudmanager 21.11.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **igroups**  list / elements=string | List of igroups (iSCSI protocol parameters). |
| **initiators**  list / elements=dictionary | Set of attributes of Initiators (iSCSI protocol parameters). |
| **alias**  string / required | The alias which associates with the node. |
| **iqn**  string / required | The initiator node name. |
| **iops**  integer | Provisioned IOPS. Needed only when provider_volume_type is “io1”. |
| **name**  string / required | The name of the volume. |
| **os_name**  string | Operating system (iSCSI protocol parameters). |
| **permission**  string | CIFS share permission type (CIFS protocol parameters). |
| **provider_volume_type**  string | The underlying cloud provider volume type.  For AWS is [“gp3”, “gp2”, “io1”, “st1”, “sc1”].  For Azure is [‘Premium_LRS’,’Standard_LRS’,’StandardSSD_LRS’].  For GCP is [‘pd-balanced’,’pd-ssd’,’pd-standard’]. |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |
| **share_name**  string | Share name (CIFS protocol parameters). |
| **size**  float | The size of the volume. |
| **size_unit**  string | The size unit of volume.  Choices:   - `"GB"` ← (default) |
| **snapshot_policy_name**  string | The snapshot policy name. |
| **state**  string | Whether the specified volume should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **svm_name**  string | The name of the SVM. The default SVM name is used, if a name is not provided. |
| **tenant_id**  string  added in netapp.cloudmanager 21.20.0 | The NetApp account ID that the Connector will be associated with. To be used only when using FSx. |
| **throughput**  integer | Unit is Mb/s. Valid range 125-1000.  Required only when provider_volume_type is ‘gp3’. |
| **tiering_policy**  string | The tiering policy.  Choices:   - `"none"` - `"snapshot_only"` - `"auto"` - `"all"` |
| **users**  list / elements=string | List of users with the permission (CIFS protocol parameters). |
| **volume_protocol**  string | The protocol for the volume. This affects the provided parameters.  Choices:   - `"nfs"` ← (default) - `"cifs"` - `"iscsi"` |
| **working_environment_id**  string | The public ID of the working environment where the volume will be created. |
| **working_environment_name**  string | The working environment name where the volume will be created. |

## [Notes](na_cloudmanager_volume_module.md#id3)

> **Note:**
>
> - Support check_mode.
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_volume_module.md#id4)

```yaml+jinja
- name: Create nfs volume with working_environment_name
  netapp.cloudmanager.na_cloudmanager_volume:
    state: present
    name: test_vol
    size: 15
    size_unit: GB
    working_environment_name: working_environment_1
    client_id: client_id
    refresh_token: refresh_token
    svm_name: svm_1
    snapshot_policy_name: default
    export_policy_type: custom
    export_policy_ip: ["10.0.0.1/16"]
    export_policy_nfs_version: ["nfs3","nfs4"]

- name: Delete volume
  netapp.cloudmanager.na_cloudmanager_volume:
    state: absent
    name: test_vol
    working_environment_name: working_environment_1
    client_id: client_id
    refresh_token: refresh_token
    svm_name: svm_1
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
