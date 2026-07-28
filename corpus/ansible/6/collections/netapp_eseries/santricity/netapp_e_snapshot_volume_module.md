---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.netapp_e_snapshot_volume module – NetApp E-Series manage snapshot volumes."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/netapp_e_snapshot_volume_module.html
fetched_at: 2026-07-28T00:14:24+00:00
---
# netapp_eseries.santricity.netapp_e_snapshot_volume module – NetApp E-Series manage snapshot volumes.

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
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_snapshot_volume`.

New in netapp_eseries.santricity 2.2

- [Synopsis](netapp_e_snapshot_volume_module.md#synopsis)
- [Parameters](netapp_e_snapshot_volume_module.md#parameters)
- [Notes](netapp_e_snapshot_volume_module.md#notes)
- [Examples](netapp_e_snapshot_volume_module.md#examples)
- [Return Values](netapp_e_snapshot_volume_module.md#return-values)

## [Synopsis](netapp_e_snapshot_volume_module.md#id1)

- Create, update, remove snapshot volumes for NetApp E/EF-Series storage arrays.

## [Parameters](netapp_e_snapshot_volume_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **api_url**  string / required | The url to the SANtricity WebServices Proxy or embedded REST API. |
| **api_username**  string / required | The username to authenticate with the SANtricity WebServices Proxy or embedded REST API. |
| **full_threshold**  integer | The repository utilization warning threshold percentage  Default: `85` |
| **name**  string / required | The name you wish to give the snapshot volume |
| **repo_percentage**  integer | The size of the view in relation to the size of the base volume  Default: `20` |
| **snapshot_image_id**  string / required | The identifier of the snapshot image used to create the new snapshot volume.  Note: You’ll likely want to use the **ERROR while parsing**: While parsing M() at index 37: Module name “netapp_e_facts” is not a FQCN module to find the ID of the image you want. |
| **ssid**  string / required | storage array ID |
| **state**  string / required | Whether to create or remove the snapshot volume  Choices:   - `"absent"` - `"present"` |
| **storage_pool_name**  string / required | Name of the storage pool on which to allocate the repository volume. |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |
| **view_mode**  string / required | The snapshot volume access mode  Choices:   - `"readOnly"` ← (default) - `"readWrite"` - `"modeUnknown"` - `"__Undefined"` |

## [Notes](netapp_e_snapshot_volume_module.md#id3)

> **Note:**
>
> - Only *full_threshold* is supported for update operations. If the snapshot volume already exists and the threshold matches, then an `ok` status will be returned, no other changes can be made to a pre-existing snapshot volume.

## [Examples](netapp_e_snapshot_volume_module.md#id4)

```yaml+jinja
- name: Snapshot volume
  netapp_e_snapshot_volume:
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}/"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    state: present
    storage_pool_name: "{{ snapshot_volume_storage_pool_name }}"
    snapshot_image_id: "{{ snapshot_volume_image_id }}"
    name: "{{ snapshot_volume_name }}"
```

## [Return Values](netapp_e_snapshot_volume_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: success  Sample: `"Json facts for the volume that was created."` |

### Authors

- Kevin Hulquest (@hulquest)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
