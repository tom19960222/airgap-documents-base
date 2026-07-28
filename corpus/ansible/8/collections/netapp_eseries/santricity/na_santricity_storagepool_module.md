---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.na_santricity_storagepool module – NetApp E-Series manage volume groups and disk pools"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/na_santricity_storagepool_module.html
fetched_at: 2026-07-28T02:44:20+00:00
---
# netapp_eseries.santricity.na_santricity_storagepool module – NetApp E-Series manage volume groups and disk pools

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/ui/repo/published/netapp_eseries/santricity/) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_storagepool`.

- [Synopsis](na_santricity_storagepool_module.md#synopsis)
- [Parameters](na_santricity_storagepool_module.md#parameters)
- [Notes](na_santricity_storagepool_module.md#notes)
- [Examples](na_santricity_storagepool_module.md#examples)
- [Return Values](na_santricity_storagepool_module.md#return-values)

## [Synopsis](na_santricity_storagepool_module.md#id1)

- Create or remove volume groups and disk pools for NetApp E-series storage arrays.

## [Parameters](na_santricity_storagepool_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **criteria_drive_count**  integer | The number of disks to use for building the storage pool.  When *state==”present”* then *criteria_drive_count* or *criteria_min_usable_capacity* must be specified.  The pool will be expanded if this number exceeds the number of disks already in place (See expansion note below) |
| **criteria_drive_interface_type**  string | The interface type to use when selecting drives for the storage pool  If not provided then all interface types will be considered.  **Choices:**   - `"scsi"` - `"fibre"` - `"sata"` - `"pata"` - `"fibre520b"` - `"sas"` - `"sas4k"` - `"nvme4k"` |
| **criteria_drive_max_size**  float | The maximum individual drive size (in size_unit) to consider when choosing drives for the storage pool. |
| **criteria_drive_min_size**  float | The minimum individual drive size (in size_unit) to consider when choosing drives for the storage pool. |
| **criteria_drive_require_da**  boolean | Ensures the storage pool will be created with only data assurance (DA) capable drives.  Only available for new storage pools; existing storage pools cannot be converted.  **Choices:**   - `false` ← (default) - `true` |
| **criteria_drive_require_fde**  boolean | Whether full disk encryption ability is required for drives to be added to the storage pool  **Choices:**   - `false` ← (default) - `true` |
| **criteria_drive_type**  string | The type of disk (hdd or ssd) to use when searching for candidates to use.  When not specified each drive type will be evaluated until successful drive candidates are found starting with the most prevalent drive type.  **Choices:**   - `"hdd"` - `"ssd"` |
| **criteria_min_usable_capacity**  float | The minimum size of the storage pool (in size_unit).  When *state==”present”* then *criteria_drive_count* or *criteria_min_usable_capacity* must be specified.  The pool will be expanded if this value exceeds its current size. (See expansion note below)  Do not use when the storage system contains mixed drives and *usable_drives* is specified since usable capacities may not be accurate. |
| **criteria_size_unit**  string | The unit used to interpret size parameters  **Choices:**   - `"bytes"` - `"b"` - `"kb"` - `"mb"` - `"gb"` ← (default) - `"tb"` - `"pb"` - `"eb"` - `"zb"` - `"yb"` |
| **ddp_critical_threshold_pct**  integer | Issues a critical alert when threshold of storage has been allocated.  Only applicable when *raid_level==”raidDiskPool”*.  Set *ddp_critical_threshold_pct==0* to disable alert.  **Default:** `85` |
| **ddp_warning_threshold_pct**  integer | Issues a warning alert when threshold of storage has been allocated.  Only applicable when *raid_level==”raidDiskPool”*.  Set *ddp_warning_threshold_pct==0* to disable alert.  **Default:** `85` |
| **erase_secured_drives**  boolean | If *state==”absent”* then all storage pool drives will be erase  If *state==”present”* then delete all available storage array drives that have security enabled.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | The name of the storage pool to manage |
| **raid_level**  string | The RAID level of the storage pool to be created.  Required only when *state==”present”*.  When *raid_level==”raidDiskPool”* then *criteria_drive_count >= 10 or criteria_drive_count >= 11* is required depending on the storage array specifications.  When *raid_level==”raid0”* then *1<=criteria_drive_count* is required.  When *raid_level==”raid1”* then *2<=criteria_drive_count* is required.  When *raid_level==”raid3”* then *3<=criteria_drive_count<=30* is required.  When *raid_level==”raid5”* then *3<=criteria_drive_count<=30* is required.  When *raid_level==”raid6”* then *5<=criteria_drive_count<=30* is required.  Note that raidAll will be treated as raidDiskPool and raid3 as raid5.  **Choices:**   - `"raidAll"` - `"raid0"` - `"raid1"` - `"raid3"` - `"raid5"` - `"raid6"` - `"raidDiskPool"` ← (default) |
| **remove_volumes**  boolean | Prior to removing a storage pool, delete all volumes in the pool.  **Choices:**   - `false` - `true` ← (default) |
| **reserve_drive_count**  integer | Set the number of drives reserved by the storage pool for reconstruction operations.  Only valid on raid disk pools. |
| **secure_pool**  boolean | Enables security at rest feature on the storage pool.  Will only work if all drives in the pool are security capable (FDE, FIPS, or mix)  Warning, once security is enabled it is impossible to disable without erasing the drives.  **Choices:**   - `false` - `true` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  **Default:** `"1"` |
| **state**  string | Whether the specified storage pool should exist or not.  Note that removing a storage pool currently requires the removal of all defined volumes first.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **usable_drives**  string | Ordered comma-separated list of tray/drive slots to be selected for drive candidates (drives that are used will be skipped).  Each drive entry is represented as <tray_number>:<(optional) drawer_number>:<drive_slot_number> (e.g. 99:0 is the base tray’s drive slot 0).  The base tray’s default identifier is 99 and expansion trays are added in the order they are attached but these identifiers can be changed by the user.  Be aware that trays with multiple drawers still have a dedicated drive slot for all drives and the slot number does not rely on the drawer; however, if you’re planing to have drawer protection you need to order accordingly.  When *usable_drives* are not provided then the drive candidates will be selected by the storage system. |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_santricity_storagepool_module.md#id3)

> **Note:**
>
> - The expansion operations are non-blocking due to the time consuming nature of expanding volume groups
> - Traditional volume groups (raid0, raid1, raid5, raid6) are performed in steps dictated by the storage array. Each required step will be attempted until the request fails which is likely because of the required expansion time.
> - raidUnsupported will be treated as raid0, raidAll as raidDiskPool and raid3 as raid5.
> - Tray loss protection and drawer loss protection will be chosen if at all possible.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing “M(netapp_e_storage_system)” at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_storagepool_module.md#id4)

```yaml+jinja
- name: No disk groups
  na_santricity_storagepool:
    ssid: "{{ ssid }}"
    name: "{{ item }}"
    state: absent
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
    validate_certs: "{{ netapp_api_validate_certs }}"
```

## [Return Values](na_santricity_storagepool_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  **Returned:** success  **Sample:** `"Json facts for the pool that was created."` |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
