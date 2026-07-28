---
collection: ansible
version: "8"
title: "netapp.cloudmanager.na_cloudmanager_aggregate module – NetApp Cloud Manager Aggregate"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/cloudmanager/na_cloudmanager_aggregate_module.html
fetched_at: 2026-07-28T02:41:04+00:00
---
# netapp.cloudmanager.na_cloudmanager_aggregate module – NetApp Cloud Manager Aggregate

> **Note:**
>
> This module is part of the [netapp.cloudmanager collection](https://galaxy.ansible.com/ui/repo/published/netapp/cloudmanager/) (version 21.22.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.cloudmanager`.
>
> To use it in a playbook, specify: `netapp.cloudmanager.na_cloudmanager_aggregate`.

New in netapp.cloudmanager 21.3.0

- [Synopsis](na_cloudmanager_aggregate_module.md#synopsis)
- [Parameters](na_cloudmanager_aggregate_module.md#parameters)
- [Notes](na_cloudmanager_aggregate_module.md#notes)
- [Examples](na_cloudmanager_aggregate_module.md#examples)
- [Return Values](na_cloudmanager_aggregate_module.md#return-values)

## [Synopsis](na_cloudmanager_aggregate_module.md#id1)

- Create, Modify or Delete Aggregate on Cloud Manager.

## [Parameters](na_cloudmanager_aggregate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **capacity_tier**  string | The aggregate’s capacity tier for tiering cold data to object storage.  If the value is NONE, the capacity_tier will not be set on aggregate creation.  **Choices:**   - `"NONE"` - `"S3"` - `"Blob"` - `"cloudStorage"` |
| **client_id**  string / required | The connector ID of the Cloud Manager Connector. |
| **disk_size_size**  integer | The required size of the disks. |
| **disk_size_unit**  string | The disk size unit [‘GB’ or ‘TB’]. The default is ‘TB’.  **Choices:**   - `"GB"` - `"TB"` ← (default) |
| **environment**  string  *added in netapp.cloudmanager 21.8.0* | The environment for NetApp Cloud Manager API operations.  **Choices:**   - `"prod"` ← (default) - `"stage"` |
| **feature_flags**  dictionary  *added in netapp.cloudmanager 21.11.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **home_node**  string | The home node that the new aggregate should belong to. |
| **iops**  integer | Provisioned IOPS. Needed only when providerVolumeType is “io1”. |
| **name**  string / required | The name of the new aggregate. |
| **number_of_disks**  integer | The required number of disks in the new aggregate. |
| **provider_volume_type**  string | The cloud provider volume type. |
| **refresh_token**  string | The refresh token for NetApp Cloud Manager API operations. |
| **sa_client_id**  string | The service account secret client ID for NetApp Cloud Manager API operations. |
| **sa_secret_key**  string | The service account secret key for NetApp Cloud Manager API operations. |
| **state**  string / required | Whether the specified aggregate should exist or not.  **Choices:**   - `"present"` - `"absent"` |
| **throughput**  integer | Unit is Mb/s. Valid range 125-1000.  Required only when provider_volume_type is ‘gp3’. |
| **working_environment_id**  string | The public ID of the working environment where the aggregate will be created. |
| **working_environment_name**  string | The working environment name where the aggregate will be created. |

## [Notes](na_cloudmanager_aggregate_module.md#id3)

> **Note:**
>
> - Support check_mode.
> - The modules prefixed with na_cloudmanager are built to manage CloudManager and CVO deployments in AWS/GCP/Azure clouds.
> - If sa_client_id and sa_secret_key are provided, service account will be used in operations. refresh_token will be ignored.

## [Examples](na_cloudmanager_aggregate_module.md#id4)

```yaml+jinja
- name: Create Aggregate
  netapp.cloudmanager.na_cloudmanager_aggregate:
    state: present
    name: AnsibleAggregate
    working_environment_name: testAWS
    client_id: "{{ client_id }}"
    number_of_disks: 2
    refresh_token: xxx

- name: Delete Volume
  netapp.cloudmanager.na_cloudmanager_aggregate:
    state: absent
    name: AnsibleAggregate
    working_environment_name: testAWS
    client_id: "{{ client_id }}"
    refresh_token: xxx
```

## [Return Values](na_cloudmanager_aggregate_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message.  **Returned:** success  **Sample:** `"Aggregate Created"` |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.cloudmanager)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.cloudmanager)
