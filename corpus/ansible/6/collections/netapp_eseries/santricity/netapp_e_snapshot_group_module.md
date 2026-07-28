---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.netapp_e_snapshot_group module – NetApp E-Series manage snapshot groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/netapp_e_snapshot_group_module.html
fetched_at: 2026-07-28T00:14:23+00:00
---
# netapp_eseries.santricity.netapp_e_snapshot_group module – NetApp E-Series manage snapshot groups

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/netapp_eseries/santricity) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_snapshot_group`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_snapshot_group_module.md#synopsis)
- [Parameters](netapp_e_snapshot_group_module.md#parameters)
- [Examples](netapp_e_snapshot_group_module.md#examples)
- [Return Values](netapp_e_snapshot_group_module.md#return-values)

## [Synopsis](netapp_e_snapshot_group_module.md#id1)

- Create, update, delete snapshot groups for NetApp E-series storage arrays

## [Parameters](netapp_e_snapshot_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **api_url**  string / required | The url to the SANtricity WebServices Proxy or embedded REST API. |
| **api_username**  string / required | The username to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **base_volume_name**  string / required | The name of the base volume or thin volume to use as the base for the new snapshot group.  If a snapshot group with an identical `name` already exists but with a different base volume an error will be returned. |
| **delete_limit**  integer | The automatic deletion indicator.  If non-zero, the oldest snapshot image will be automatically deleted when creating a new snapshot image to keep the total number of snapshot images limited to the number specified.  This value is overridden by the consistency group setting if this snapshot group is associated with a consistency group.  Default: `30` |
| **full_policy**  string | The behavior on when the data repository becomes full.  This value is overridden by consistency group setting if this snapshot group is associated with a consistency group  Choices:   - `"unknown"` - `"failbasewrites"` - `"purgepit"` ← (default) |
| **name**  string / required | The name to give the snapshot group |
| **repo_pct**  integer | The size of the repository in relation to the size of the base volume  Default: `20` |
| **rollback_priority**  string | The importance of the rollback operation.  This value is overridden by consistency group setting if this snapshot group is associated with a consistency group  Choices:   - `"highest"` - `"high"` - `"medium"` ← (default) - `"low"` - `"lowest"` |
| **ssid**  string | Storage system identifier |
| **state**  string / required | Whether to ensure the group is present or absent.  Choices:   - `"present"` - `"absent"` |
| **storage_pool_name**  string / required | The name of the storage pool on which to allocate the repository volume. |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |
| **warning_threshold**  integer | The repository utilization warning threshold, as a percentage of the repository volume capacity.  Default: `80` |

## [Examples](netapp_e_snapshot_group_module.md#id3)

```yaml+jinja
- name: Configure Snapshot group
  netapp_e_snapshot_group:
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    validate_certs: "{{ netapp_api_validate_certs }}"
    base_volume_name: SSGroup_test
    name=: OOSS_Group
    repo_pct: 20
    warning_threshold: 85
    delete_limit: 30
    full_policy: purgepit
    storage_pool_name: Disk_Pool_1
    rollback_priority: medium
```

## [Return Values](netapp_e_snapshot_group_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: success  Sample: `"json facts for newly created snapshot group."` |

### Authors

- Kevin Hulquest (@hulquest)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
