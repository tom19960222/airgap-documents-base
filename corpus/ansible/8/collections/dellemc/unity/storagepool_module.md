---
collection: ansible
version: "8"
title: "dellemc.unity.storagepool module – Manage storage pool on Unity"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/storagepool_module.html
fetched_at: 2026-07-28T02:05:31+00:00
---
# dellemc.unity.storagepool module – Manage storage pool on Unity

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
> see [Requirements](storagepool_module.md#ansible-collections-dellemc-unity-storagepool-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.storagepool`.

New in dellemc.unity 1.1.0

- [Synopsis](storagepool_module.md#synopsis)
- [Requirements](storagepool_module.md#requirements)
- [Parameters](storagepool_module.md#parameters)
- [Notes](storagepool_module.md#notes)
- [Examples](storagepool_module.md#examples)
- [Return Values](storagepool_module.md#return-values)

## [Synopsis](storagepool_module.md#id1)

- Managing storage pool on Unity storage system contains the operations Get details of storage pool, Create a storage pool, Modify storage pool.

Aliases: dellemc_unity_storagepool

## [Requirements](storagepool_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](storagepool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alert_threshold**  integer | Threshold at which the system will generate alerts about the free space in the pool, specified as a percentage.  Minimum threshold limit is 50.  Maximum threshold limit is 84. |
| **fast_cache**  string | Indicates whether the fast cache is enabled for the storage pool.  `Enabled` - FAST Cache is enabled for the pool.  `Disabled` - FAST Cache is disabled for the pool.  **Choices:**   - `"enabled"` - `"disabled"` |
| **fast_vp**  string | Indicates whether to enable scheduled data relocations for the pool.  `Enabled` - Enabled scheduled data relocations for the pool.  `Disabled` - Disabled scheduled data relocations for the pool.  **Choices:**   - `"enabled"` - `"disabled"` |
| **is_harvest_enabled**  boolean | Enable/Disable automatic deletion of snapshots based on pool space usage.  **Choices:**   - `false` - `true` |
| **is_snap_harvest_enabled**  boolean | Enable/Disable automatic deletion of snapshots based on pool space usage.  **Choices:**   - `false` - `true` |
| **new_pool_name**  string | New name of the storage pool, unique in the storage system. |
| **password**  string / required | The password of the Unity management server. |
| **pool_description**  string | The description of the storage pool. |
| **pool_harvest_high_threshold**  float | Max threshold for space used in pool beyond which the system automatically starts deleting snapshots in the pool.  Applies when the automatic deletion of snapshots based on pool space usage is enabled for the system and pool.  Minimum pool harvest high threshold value is 1.  Maximum pool harvest high threshold value is 99. |
| **pool_harvest_low_threshold**  float | Min threshold for space used in pool below which the system automatically stops deletion of snapshots in the pool.  Applies when the automatic deletion of snapshots based on pool space usage is enabled for the system and pool.  Minimum pool harvest low threshold value is 0.  Maximum pool harvest low threshold value is 98. |
| **pool_id**  string | Unique identifier of the pool instance. |
| **pool_name**  string | Name of the storage pool, unique in the storage system. |
| **pool_type**  string | Indicates storage pool type.  **Choices:**   - `"TRADITIONAL"` - `"DYNAMIC"` |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **raid_groups**  dictionary | Parameters to create RAID group from the disks and add it to the pool. |
| **disk_group_id**  string | Id of the disk group. |
| **disk_num**  integer | Number of disks. |
| **raid_type**  string | RAID group types or RAID levels.  **Choices:**   - `"None"` - `"RAID5"` - `"RAID0"` - `"RAID1"` - `"RAID3"` - `"RAID10"` - `"RAID6"` - `"Mixed"` - `"Automatic"` |
| **stripe_width**  string | RAID group stripe widths, including parity or mirror disks.  **Choices:**   - `"BEST_FIT"` - `"2"` - `"4"` - `"5"` - `"6"` - `"8"` - `"9"` - `"10"` - `"12"` - `"13"` - `"14"` - `"16"` |
| **snap_harvest_high_threshold**  float | Max threshold for space used in snapshot beyond which the system automatically starts deleting snapshots in the pool.  Applies when the automatic deletion of snapshots based on pool space usage is enabled for the pool.  Minimum snap harvest high threshold value is 1.  Maximum snap harvest high threshold value is 99. |
| **snap_harvest_low_threshold**  float | Min threshold for space used in snapshot below which the system will stop automatically deleting snapshots in the pool.  Applies when the automatic deletion of snapshots based on pool space usage is enabled for the pool.  Minimum snap harvest low threshold value is 0.  Maximum snap harvest low threshold value is 98. |
| **state**  string / required | Define whether the storage pool should exist or not.  `Present` - indicates that the storage pool should exist on the system.  `Absent` - indicates that the storage pool should not exist on the system.  **Choices:**   - `"absent"` - `"present"` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](storagepool_module.md#id4)

> **Note:**
>
> - Deletion of storage pool is not allowed through Ansible module.
> - The *check_mode* is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](storagepool_module.md#id5)

```yaml+jinja
- name: Get Storage pool details using pool_name
  dellemc.unity.storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    pool_name: "{{pool_name}}"
    state: "present"

- name: Get Storage pool details using pool_id
  dellemc.unity.storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    pool_id: "{{pool_id}}"
    state: "present"

- name: Modify Storage pool attributes using pool_name
  dellemc.unity.storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    pool_name: "{{pool_name}}"
    new_pool_name: "{{new_pool_name}}"
    pool_description: "{{pool_description}}"
    fast_cache: "{{fast_cache_enabled}}"
    fast_vp: "{{fast_vp_enabled}}"
    state: "present"

- name: Modify Storage pool attributes using pool_id
  dellemc.unity.storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    pool_id: "{{pool_id}}"
    new_pool_name: "{{new_pool_name}}"
    pool_description: "{{pool_description}}"
    fast_cache: "{{fast_cache_enabled}}"
    fast_vp: "{{fast_vp_enabled}}"
    state: "present"

- name: Create a StoragePool
  dellemc.unity.storagepool:
    unispherehost: "{{unispherehost}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    pool_name: "Test"
    pool_description: "test pool"
    raid_groups:
      disk_group_id : "dg_16"
      disk_num : 2
      raid_type : "RAID10"
      stripe_width : "BEST_FIT"
    alert_threshold : 50
    is_harvest_enabled : true
    pool_harvest_high_threshold : 60
    pool_harvest_low_threshold : 40
    is_snap_harvest_enabled : true
    snap_harvest_high_threshold : 70
    snap_harvest_low_threshold : 50
    fast_vp: "enabled"
    fast_cache: "enabled"
    pool_type : "DYNAMIC"
    state: "present"
```

## [Return Values](storagepool_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the storage pool has changed.  **Returned:** always  **Sample:** `true` |
| **storage_pool_details**  dictionary | The storage pool details.  **Returned:** When storage pool exists.  **Sample:** `{"alert_threshold": 50, "creation_time": "2022-03-08 14:05:32+00:00", "description": "", "drives": [{"disk_technology": "SAS", "id": "dpe_disk_22", "name": "DPE Drive 22", "size": 590860984320, "tier_type": "PERFORMANCE"}, {"disk_technology": "SAS", "id": "dpe_disk_23", "name": "DPE Drive 23", "size": 590860984320, "tier_type": "PERFORMANCE"}, {"disk_technology": "SAS", "id": "dpe_disk_24", "name": "DPE Drive 24", "size": 590860984320, "tier_type": "PERFORMANCE"}], "existed": true, "harvest_state": "UsageHarvestStateEnum.IDLE", "hash": 8744642897210, "health": {"UnityHealth": {"hash": 8744642799842}}, "id": "pool_280", "is_all_flash": false, "is_empty": false, "is_fast_cache_enabled": false, "is_fast_vp_enabled": false, "is_harvest_enabled": true, "is_snap_harvest_enabled": true, "metadata_size_subscribed": 105763569664, "metadata_size_used": 57176752128, "name": "test_pool", "object_id": 12884902146, "pool_fast_vp": {"UnityPoolFastVp": {"hash": 8744647518980}}, "pool_space_harvest_high_threshold": 59.0, "pool_space_harvest_low_threshold": 40.0, "pool_type": "StoragePoolTypeEnum.DYNAMIC", "raid_type": "RaidTypeEnum.RAID10", "rebalance_progress": null, "size_free": 470030483456, "size_free_with_unit": "437.75 GB", "size_subscribed": 447215820800, "size_subscribed_with_unit": "416.5 GB", "size_total": 574720311296, "size_total_with_unit": "535.25 GB", "size_used": 76838068224, "size_used_with_unit": "71.56 GB", "snap_size_subscribed": 128851369984, "snap_size_subscribed_with_unit": "120.0 GB", "snap_size_used": 2351104, "snap_size_used_with_unit": "2.24 MB", "snap_space_harvest_high_threshold": 80.0, "snap_space_harvest_low_threshold": 60.0, "tiers": {"UnityPoolTierList": [{"disk_count": [0, 3, 0], "existed": true, "hash": 8744643017382, "name": ["Extreme Performance", "Performance", "Capacity"], "pool_units": [null, {"UnityPoolUnitList": [{"UnityPoolUnit": {"hash": 8744642786759, "id": "rg_4"}}, {"UnityPoolUnit": {"hash": 8744642786795, "id": "rg_5"}}]}, null], "raid_type": ["RaidTypeEnum.NONE", "RaidTypeEnum.RAID10", "RaidTypeEnum.NONE"], "size_free": [0, 470030483456, 0], "size_moving_down": [0, 0, 0], "size_moving_up": [0, 0, 0], "size_moving_within": [0, 0, 0], "size_total": [0, 574720311296, 0], "size_used": [0, 104689827840, 0], "stripe_width": [null, "RaidStripeWidthEnum._2", null], "tier_type": ["TierTypeEnum.EXTREME_PERFORMANCE", "TierTypeEnum.PERFORMANCE", "TierTypeEnum.CAPACITY"]}]}}` |
| **drives**  list / elements=string | Indicates information about the drives associated with the storage pool.  **Returned:** success |
| **disk_technology**  string | Indicates disk technology of the drive.  **Returned:** success |
| **id**  string | Unique identifier of the drive.  **Returned:** success |
| **name**  string | Indicates name of the drive.  **Returned:** success |
| **size**  string | Indicates size of the drive.  **Returned:** success |
| **tier_type**  string | Indicates tier type of the drive.  **Returned:** success |
| **id**  string | Pool id, unique identifier of the pool.  **Returned:** success |
| **is_fast_cache_enabled**  boolean | Indicates whether the fast cache is enabled for the storage pool. true - FAST Cache is enabled for the pool. false - FAST Cache is disabled for the pool.  **Returned:** success |
| **is_fast_vp_enabled**  boolean | Indicates whether to enable scheduled data relocations for the storage pool. true - Enabled scheduled data relocations for the pool. false - Disabled scheduled data relocations for the pool.  **Returned:** success |
| **name**  string | Pool name, unique in the storage system.  **Returned:** success |
| **size_free_with_unit**  string | Indicates size_free with its appropriate unit in human readable form.  **Returned:** success |
| **size_subscribed_with_unit**  string | Indicates size_subscribed with its appropriate unit in human readable form.  **Returned:** success |
| **size_total_with_unit**  string | Indicates size_total with its appropriate unit in human readable form.  **Returned:** success |
| **size_used_with_unit**  string | Indicates size_used with its appropriate unit in human readable form.  **Returned:** success |
| **snap_size_subscribed_with_unit**  string | Indicates snap_size_subscribed with its appropriate unit in human readable form.  **Returned:** success |
| **snap_size_used_with_unit**  string | Indicates snap_size_used with its appropriate unit in human readable form.  **Returned:** success |

### Authors

- Ambuj Dubey (@AmbujDube)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
