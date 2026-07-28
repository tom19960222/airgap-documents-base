---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_snapshot module – NetApp E-Series storage system’s snapshots."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_snapshot_module.html
fetched_at: 2026-07-28T00:14:07+00:00
---
# netapp_eseries.santricity.na_santricity_snapshot module – NetApp E-Series storage system’s snapshots.

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
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_snapshot`.

- [Synopsis](na_santricity_snapshot_module.md#synopsis)
- [Parameters](na_santricity_snapshot_module.md#parameters)
- [Notes](na_santricity_snapshot_module.md#notes)
- [Examples](na_santricity_snapshot_module.md#examples)
- [Return Values](na_santricity_snapshot_module.md#return-values)

## [Synopsis](na_santricity_snapshot_module.md#id1)

- Manage NetApp E-Series manage the storage system’s snapshots.

## [Parameters](na_santricity_snapshot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **alert_threshold_pct**  integer | Percent of filled reserve capacity to issue alert.  Default: `75` |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **group_name**  string / required | Name of the snapshot consistency group or snapshot volume.  Be sure to use different names for snapshot consistency groups and snapshot volumes to avoid name conflicts. |
| **maximum_snapshots**  integer | Total number of snapshot images to maintain.  Default: `32` |
| **pit_description**  string | Arbitrary description for a consistency group’s snapshot images |
| **pit_name**  string | Name of a consistency group’s snapshot images. |
| **pit_timestamp**  string | Snapshot image timestamp in the YYYY-MM-DD HH:MM:SS (AM|PM) (hours, minutes, seconds, and day-period are optional)  Define only as much time as necessary to distinguish the desired snapshot image from the others.  24 hour time will be assumed if day-period indicator (AM, PM) is not specified.  The terms latest and oldest may be used to select newest and oldest consistency group images.  Mutually exclusive with *pit_name or pit_description* |
| **preferred_reserve_storage_pool**  string | Default preferred storage pool or volume group for the reserve capacity volume.  The base volume’s storage pool or volume group will be selected by default if not defined.  Used to specify storage pool or volume group for both snapshot consistency group volume members and snapshot volumes |
| **reserve_capacity_full_policy**  string | Policy for full reserve capacity.  Purge deletes the oldest snapshot image for the base volume in the consistency group.  Reject writes to base volume (keep snapshot images valid).  Choices:   - `"purge"` ← (default) - `"reject"` |
| **reserve_capacity_pct**  integer | Default percentage of base volume capacity to reserve for snapshot copy-on-writes (COW).  Used to define reserve capacity for both snapshot consistency group volume members and snapshot volumes.  Default: `40` |
| **rollback_backup**  boolean | Whether a point-in-time snapshot should be taken prior to performing a rollback.  Choices:   - `false` - `true` ← (default) |
| **rollback_priority**  string | Storage system priority given to restoring snapshot point in time.  Choices:   - `"highest"` - `"high"` - `"medium"` ← (default) - `"low"` - `"lowest"` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **state**  string | When *state==absent* ensures the *type* has been removed.  When *state==present* ensures the *type* is available.  When *state==rollback* the consistency group will be rolled back to the point-in-time snapshot images selected by *pit_name or pit_timestamp*.  *state==rollback* will always return changed since it is not possible to evaluate the current state of the base volume in relation to a snapshot image.  Choices:   - `"absent"` - `"present"` ← (default) - `"rollback"` |
| **type**  string | Type of snapshot object to effect.  Group indicates a snapshot consistency group; consistency groups may have one or more base volume members which are defined in *volumes*.  Pit indicates a snapshot consistency group point-in-time image(s); a snapshot image will be taken of each base volume when *state==present*.  Warning! When *state==absent and type==pit*, *pit_name* or *pit_timestamp* must be defined and all point-in-time images created prior to the selection will also be deleted.  View indicates a consistency group snapshot volume of particular point-in-time image(s); snapshot volumes will be created for each base volume member.  Views are created from images from a single point-in-time so once created they cannot be modified.  Choices:   - `"group"` ← (default) - `"pit"` - `"view"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |
| **view_host**  string | Default host or host group to map snapshot volumes. |
| **view_name**  string | Consistency group snapshot volume group.  Required when *state==volume* or when ensuring the views absence when *state==absent*. |
| **view_validate**  boolean | Default whether snapshop volumes should be validated.  Choices:   - `false` ← (default) - `true` |
| **view_writable**  boolean | Default whether snapshot volumes should be writable.  Choices:   - `false` - `true` ← (default) |
| **volumes**  list / elements=string | Details for each consistency group base volume for defining reserve capacity, preferred reserve capacity storage pool, and snapshot volume options.  When *state==present and type==group* the volume entries will be used to add or remove base volume from a snapshot consistency group.  When *state==present and type==view* the volume entries will be used to select images from a point-in-time for their respective snapshot volumes.  If *state==present and type==view* and *volume* is not specified then all volumes will be selected with the defaults.  Views are created from images from a single point-in-time so once created they cannot be modified.  When *state==rollback* then *volumes* can be used to specify which base volumes to rollback; otherwise all consistency group volumes will rollback. |
| **preferred_reserve_storage_pool**  string | Preferred storage pool or volume group for the reserve capacity volume.  The base volume’s storage pool or volume group will be selected by default if not defined.  Used to specify storage pool or volume group for both snapshot consistency group volume members and snapshot volumes |
| **reserve_capacity_pct**  integer | Percentage of base volume capacity to reserve for snapshot copy-on-writes (COW).  Used to define reserve capacity for both snapshot consistency group volume members and snapshot volumes.  Default: `40` |
| **snapshot_volume_host**  string | Host or host group to map snapshot volume. |
| **snapshot_volume_validate**  boolean | Whether snapshot volume should be validated which includes both a media scan and parity validation.  Choices:   - `false` ← (default) - `true` |
| **snapshot_volume_writable**  boolean | Whether snapshot volume of base volume images should be writable.  Choices:   - `false` - `true` ← (default) |
| **volume**  string / required | Base volume for consistency group. |

## [Notes](na_santricity_snapshot_module.md#id3)

> **Note:**
>
> - Key-value pairs are used to keep track of snapshot names and descriptions since the snapshot point-in-time images do have metadata associated with their data structures; therefore, it is necessary to clean out old keys that are no longer associated with an actual image. This cleaning action is performed each time this module is executed.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_snapshot_module.md#id4)

```yaml+jinja
- name: Ensure snapshot consistency group exists.
  na_santricity_snapshot:
    ssid: "1"
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
    state: present
    type: group
    group_name: snapshot_group1
    volumes:
      - volume: vol1
        reserve_capacity_pct: 20
        preferred_reserve_storage_pool: vg1
      - volume: vol2
        reserve_capacity_pct: 30
      - volume: vol3
    alert_threshold_pct: 80
    maximum_snapshots: 30
- name: Take the current consistency group's base volumes point-in-time snapshot images.
  na_santricity_snapshot:
    ssid: "1"
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
    state: present
    type: pit
    group_name: snapshot_group1
    pit_name: pit1
    pit_description: Initial consistency group's point-in-time snapshot images.
- name: Ensure snapshot consistency group view exists and is mapped to host group.
  na_santricity_snapshot:
    ssid: "1"
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
    state: present
    type: view
    group_name: snapshot_group1
    pit_name: pit1
    view_name: view1
    view_host: view1_hosts_group
    volumes:
      - volume: vol1
        reserve_capacity_pct: 20
        preferred_reserve_storage_pool: vg4
        snapshot_volume_writable: false
        snapshot_volume_validate: true
      - volume: vol2
        reserve_capacity_pct: 20
        preferred_reserve_storage_pool: vg4
        snapshot_volume_writable: true
        snapshot_volume_validate: true
      - volume: vol3
        reserve_capacity_pct: 20
        preferred_reserve_storage_pool: vg4
        snapshot_volume_writable: false
        snapshot_volume_validate: true
    alert_threshold_pct: 80
    maximum_snapshots: 30
- name: Rollback base volumes to consistency group's point-in-time pit1.
  na_santricity_snapshot:
    ssid: "1"
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
    state: present
    type: group
    group_name: snapshot_group1
    pit_name: pit1
    rollback: true
    rollback_priority: high
- name: Ensure snapshot consistency group view no longer exists.
  na_santricity_snapshot:
    ssid: "1"
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
    state: absent
    type: view
    group_name: snapshot_group1
    view_name: view1
- name: Ensure that the consistency group's base volumes point-in-time snapshot images pit1 no longer exists.
  na_santricity_snapshot:
    ssid: "1"
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
    state: absent
    type: image
    group_name: snapshot_group1
    pit_name: pit1
- name: Ensure snapshot consistency group no longer exists.
  na_santricity_snapshot:
    ssid: "1"
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
    state: absent
    type: group
    group_name: snapshot_group1
```

## [Return Values](na_santricity_snapshot_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether changes have been made.  Returned: always |
| **deleted_metadata_keys**  list / elements=string | Keys that were purged from the key-value datastore.  Returned: always |
| **group_changes**  dictionary | All changes performed to the consistency group.  Returned: always |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
