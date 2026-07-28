---
collection: ansible
version: "8"
title: "dellemc.unity.volume module – Manage volume on Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/volume_module.html
fetched_at: 2026-07-28T01:05:41+00:00
---
# dellemc.unity.volume module – Manage volume on Unity storage system

> **Note:**
>
> This module is part of the [dellemc.unity collection](https://galaxy.ansible.com/ui/repo/published/dellemc/unity/) (version 1.7.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.unity`.
> You need further requirements to be able to use this module,
> see [Requirements](volume_module.md#ansible-collections-dellemc-unity-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.volume`.

New in dellemc.unity 1.1.0

- [Synopsis](volume_module.md#synopsis)
- [Requirements](volume_module.md#requirements)
- [Parameters](volume_module.md#parameters)
- [Notes](volume_module.md#notes)
- [Examples](volume_module.md#examples)
- [Return Values](volume_module.md#return-values)

## [Synopsis](volume_module.md#id1)

- Managing volume on Unity storage system includes- Create new volume, Modify volume attributes, Map Volume to host, Unmap volume to host, Display volume details, Delete volume.

Aliases: dellemc_unity_volume

## [Requirements](volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **advanced_dedup**  boolean | Boolean variable, Indicates whether or not to enable advanced deduplication.  Compression should be enabled to enable advanced deduplication.  It can only be enabled on the all flash high end platforms.  Deduplicated data will remain as is even after advanced deduplication is disabled.  **Choices:**   - `false` - `true` |
| **cap_unit**  string | The unit of the volume size. It defaults to `GB`, if not specified.  **Choices:**   - `"GB"` - `"TB"` |
| **compression**  boolean | Boolean variable, Specifies whether or not to enable compression. Compression is supported only for thin volumes.  **Choices:**   - `false` - `true` |
| **description**  string | Description about the volume.  Description can be removed by passing empty string (“”). |
| **hlu**  integer | Host Lun Unit to be mapped/unmapped with this volume.  It is an optional parameter, hlu can be specified along with *host_name* or *host_id* and *mapping_state*.  If *hlu* is not specified, unity will choose it automatically. The maximum value supported is `255`. |
| **host_id**  string | ID of the host to be mapped/unmapped with this volume.  Either *host_name* or *host_id* can be specified in one task along with *mapping_state*. |
| **host_name**  string | Name of the host to be mapped/unmapped with this volume.  Either *host_name* or *host_id* can be specified in one task along with *mapping_state*. |
| **hosts**  list / elements=dictionary | Name of hosts for mapping to a volume. |
| **hlu**  string | Host Lun Unit to be mapped/unmapped with this volume.  It is an optional parameter, *hlu* can be specified along with *host_name* or *host_id* and *mapping_state*.  If *hlu* is not specified, unity will choose it automatically. The maximum value supported is `255`. |
| **host_id**  string | ID of the host. |
| **host_name**  string | Name of the host. |
| **io_limit_policy**  string | IO limit policy associated with this volume. Once it is set, it cannot be removed through ansible module but it can be changed. |
| **is_thin**  boolean | Boolean variable, Specifies whether or not it is a thin volume.  The value is set as `true` by default if not specified.  **Choices:**   - `false` - `true` |
| **mapping_state**  string | State of host access for volume.  **Choices:**   - `"mapped"` - `"unmapped"` |
| **new_vol_name**  string | New name of the volume for rename operation. |
| **password**  string / required | The password of the Unity management server. |
| **pool_id**  string | This is the id of the pool where the volume will be created.  Either the *pool_name* or *pool_id* must be provided to create a new volume. |
| **pool_name**  string | This is the name of the pool where the volume will be created.  Either the *pool_name* or *pool_id* must be provided to create a new volume. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **size**  integer | The size of the volume. |
| **snap_schedule**  string | Snapshot schedule assigned to the volume.  Add/Remove/Modify the snapshot schedule for the volume. |
| **sp**  string | Storage Processor for this volume.  **Choices:**   - `"SPA"` - `"SPB"` |
| **state**  string / required | State variable to determine whether volume will exist or not.  **Choices:**   - `"absent"` - `"present"` |
| **tiering_policy**  string | Tiering policy choices for how the storage resource data will be distributed among the tiers available in the pool.  **Choices:**   - `"AUTOTIER_HIGH"` - `"AUTOTIER"` - `"HIGHEST"` - `"LOWEST"` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **vol_id**  string | The id of the volume.  It can be used only for get, modify, map/unmap host, or delete operation. |
| **vol_name**  string | The name of the volume. Mandatory only for create operation. |

## [Notes](volume_module.md#id4)

> **Note:**
>
> - The *check_mode* is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](volume_module.md#id5)

```yaml+jinja
- name: Create Volume
  dellemc.unity.volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    vol_name: "{{vol_name}}"
    description: "{{description}}"
    pool_name: "{{pool}}"
    size: 2
    cap_unit: "{{cap_GB}}"
    is_thin: true
    compression: true
    advanced_dedup: true
    state: "{{state_present}}"

- name: Expand Volume by volume id
  dellemc.unity.volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    vol_id: "{{vol_id}}"
    size: 5
    cap_unit: "{{cap_GB}}"
    state: "{{state_present}}"

- name: Modify Volume, map host by host_name
  dellemc.unity.volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    vol_name: "{{vol_name}}"
    host_name: "{{host_name}}"
    hlu: 5
    mapping_state: "{{state_mapped}}"
    state: "{{state_present}}"

- name: Modify Volume, unmap host mapping by host_name
  dellemc.unity.volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    vol_name: "{{vol_name}}"
    host_name: "{{host_name}}"
    mapping_state: "{{state_unmapped}}"
    state: "{{state_present}}"

- name: Map multiple hosts to a Volume
  dellemc.unity.volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    vol_id: "{{vol_id}}"
    hosts:
        - host_name: "10.226.198.248"
          hlu: 1
        - host_id: "Host_929"
          hlu: 2
    mapping_state: "mapped"
    state: "present"

- name: Modify Volume attributes
  dellemc.unity.volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    vol_name: "{{vol_name}}"
    new_vol_name: "{{new_vol_name}}"
    tiering_policy: "AUTOTIER"
    compression: true
    is_thin: true
    advanced_dedup: true
    state: "{{state_present}}"

- name: Delete Volume by vol name
  dellemc.unity.volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    vol_name: "{{vol_name}}"
    state: "{{state_absent}}"

- name: Delete Volume by vol id
  dellemc.unity.volume:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    vol_id: "{{vol_id}}"
    state: "{{state_absent}}"
```

## [Return Values](volume_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **volume_details**  dictionary | Details of the volume.  **Returned:** When volume exists  **Sample:** `{"current_node": "NodeEnum.SPB", "data_reduction_percent": 0, "data_reduction_ratio": 1.0, "data_reduction_size_saved": 0, "default_node": "NodeEnum.SPB", "description": null, "effective_io_limit_max_iops": null, "effective_io_limit_max_kbps": null, "existed": true, "family_base_lun": {"UnityLun": {"hash": 8774954523796, "id": "sv_27"}}, "family_clone_count": 0, "hash": 8774954522426, "health": {"UnityHealth": {"hash": 8774954528278}}, "host_access": [{"accessMask": "PRODUCTION", "hlu": 0, "id": "Host_75", "name": "10.226.198.250"}], "id": "sv_27", "io_limit_policy": null, "is_advanced_dedup_enabled": false, "is_compression_enabled": null, "is_data_reduction_enabled": false, "is_replication_destination": false, "is_snap_schedule_paused": false, "is_thin_clone": false, "is_thin_enabled": false, "metadata_size": 4294967296, "metadata_size_allocated": 4026531840, "name": "VSI-UNITY-test-task", "per_tier_size_used": [111400714240, 0, 0], "pool": {"id": "pool_3", "name": "Extreme_Perf_tier"}, "size_allocated": 107374182400, "size_total": 107374182400, "size_total_with_unit": "100.0 GB", "size_used": null, "snap_count": 0, "snap_schedule": null, "snap_wwn": "60:06:01:60:5C:F0:50:00:94:3E:91:4D:51:5A:4F:97", "snaps_size": 0, "snaps_size_allocated": 0, "storage_resource": {"UnityStorageResource": {"hash": 8774954518887}}, "tiering_policy": "TieringPolicyEnum.AUTOTIER_HIGH", "type": "LUNTypeEnum.VMWARE_ISCSI", "wwn": "60:06:01:60:5C:F0:50:00:00:B5:95:61:2E:34:DB:B2"}` |
| **current_sp**  string | Current storage processor for this volume.  **Returned:** success |
| **description**  string | Description about the volume.  **Returned:** success |
| **host_access**  list / elements=string | Host mapped to this volume.  **Returned:** success |
| **id**  string | The system generated ID given to the volume.  **Returned:** success |
| **io_limit_policy**  dictionary | IO limit policy associated with this volume.  **Returned:** success |
| **is_data_reduction_enabled**  boolean | Whether or not compression enabled on this volume.  **Returned:** success |
| **is_thin_enabled**  boolean | Indicates whether thin provisioning is enabled for this volume.  **Returned:** success |
| **name**  string | Name of the volume.  **Returned:** success |
| **pool**  dictionary | The pool in which this volume is allocated.  **Returned:** success |
| **size_total_with_unit**  string | Size of the volume with actual unit.  **Returned:** success |
| **snap_schedule**  dictionary | Snapshot schedule applied to this volume.  **Returned:** success |
| **tiering_policy**  string | Tiering policy applied to this volume.  **Returned:** success |
| **wwn**  string | The world wide name of this volume.  **Returned:** success |

### Authors

- Arindam Datta (@arindam-emc)
- Pavan Mudunuri(@Pavan-Mudunuri)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
