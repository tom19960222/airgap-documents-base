---
collection: ansible
version: "8"
title: "dellemc.powerflex.snapshot module – Manage Snapshots on Dell PowerFlex"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/snapshot_module.html
fetched_at: 2026-07-28T02:05:15+00:00
---
# dellemc.powerflex.snapshot module – Manage Snapshots on Dell PowerFlex

> **Note:**
>
> This module is part of the [dellemc.powerflex collection](https://galaxy.ansible.com/ui/repo/published/dellemc/powerflex/) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.powerflex`.
> You need further requirements to be able to use this module,
> see [Requirements](snapshot_module.md#ansible-collections-dellemc-powerflex-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.powerflex.snapshot`.

New in dellemc.powerflex 1.0.0

- [Synopsis](snapshot_module.md#synopsis)
- [Requirements](snapshot_module.md#requirements)
- [Parameters](snapshot_module.md#parameters)
- [Notes](snapshot_module.md#notes)
- [Examples](snapshot_module.md#examples)
- [Return Values](snapshot_module.md#return-values)

## [Synopsis](snapshot_module.md#id1)

- Managing snapshots on PowerFlex Storage System includes creating, getting details, mapping/unmapping to/from SDC, modifying the attributes and deleting snapshot.

Aliases: dellemc_powerflex_snapshot

## [Requirements](snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.13 or later.
- PyPowerFlex 1.8.0.
- Python 3.9, 3.10 or 3.11.

## [Parameters](snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_multiple_mappings**  boolean | Specifies whether to allow multiple mappings or not.  **Choices:**   - `false` - `true` |
| **cap_unit**  string | The unit of the volume size. It defaults to `GB`, if not specified.  **Choices:**   - `"GB"` - `"TB"` |
| **desired_retention**  integer | The retention value for the Snapshot.  If the desired_retention is not mentioned during creation, snapshot will be created with unlimited retention.  Maximum supported desired retention is 31 days. |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the PowerFlex host. |
| **password**  string / required | The password of the PowerFlex host. |
| **port**  integer | Port number through which communication happens with PowerFlex host.  **Default:** `443` |
| **read_only**  boolean | Specifies whether mapping of the created snapshot volume will have read-write access or limited to read-only access.  If `true`, snapshot is created with read-only access.  If `false`, snapshot is created with read-write access.  **Choices:**   - `false` - `true` |
| **remove_mode**  string | Removal mode for the snapshot.  It defaults to `ONLY_ME`, if not specified.  **Choices:**   - `"ONLY_ME"` - `"INCLUDING_DESCENDANTS"` |
| **retention_unit**  string | The unit for retention. It defaults to `hours`, if not specified.  **Choices:**   - `"hours"` - `"days"` |
| **sdc**  list / elements=dictionary | Specifies SDC parameters. |
| **access_mode**  string | Define the access mode for all mappings of the snapshot.  **Choices:**   - `"READ_WRITE"` - `"READ_ONLY"` - `"NO_ACCESS"` |
| **bandwidth_limit**  integer | Limit of snapshot network bandwidth.  Need to mention in multiple of 1024 Kbps.  To set no limit, 0 is to be passed. |
| **iops_limit**  integer | Limit of snapshot IOPS.  Minimum IOPS limit is 11 and specify 0 for unlimited iops. |
| **sdc_id**  string | ID of the SDC.  Specify either *sdc_name*, *sdc_id* or *sdc_ip*.  Mutually exclusive with *sdc_name* and *sdc_ip*. |
| **sdc_ip**  string | IP of the SDC.  Specify either *sdc_name*, *sdc_id* or *sdc_ip*.  Mutually exclusive with *sdc_id* and *sdc_ip*. |
| **sdc_name**  string | Name of the SDC.  Specify either *sdc_name*, *sdc_id* or *sdc_ip*.  Mutually exclusive with *sdc_id* and *sdc_ip*. |
| **sdc_state**  string | Mapping state of the SDC.  **Choices:**   - `"mapped"` - `"unmapped"` |
| **size**  integer | The size of the snapshot. |
| **snapshot_id**  string | The ID of the Snapshot. |
| **snapshot_name**  string | The name of the snapshot.  Mandatory for create operation.  Specify either *snapshot_name* or *snapshot_id* (but not both) for any operation. |
| **snapshot_new_name**  string | New name of the snapshot. Used to rename the snapshot. |
| **state**  string / required | State of the snapshot.  **Choices:**   - `"present"` - `"absent"` |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **username**  string / required | The username of the PowerFlex host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **vol_id**  string | The ID of the volume. |
| **vol_name**  string | The name of the volume for which snapshot will be taken.  Specify either *vol_name* or *vol_id* while creating snapshot. |

## [Notes](snapshot_module.md#id4)

> **Note:**
>
> - The *check_mode* is not supported.
> - The modules present in the collection named as ‘dellemc.powerflex’ are built to support the Dell PowerFlex storage platform.

## [Examples](snapshot_module.md#id5)

```yaml+jinja
- name: Create snapshot
  dellemc.powerflex.snapshot:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_name: "ansible_snapshot"
    vol_name: "ansible_volume"
    read_only: false
    desired_retention: 2
    state: "present"

- name: Get snapshot details using snapshot id
  dellemc.powerflex.snapshot:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_id: "fe6cb28200000007"
    state: "present"

- name: Map snapshot to SDC
  dellemc.powerflex.snapshot:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_id: "fe6cb28200000007"
    sdc:
        - sdc_ip: "198.10.xxx.xxx"
        - sdc_id: "663ac0d200000001"
    allow_multiple_mappings: true
    sdc_state: "mapped"
    state: "present"

- name: Modify the attributes of SDC mapped to snapshot
  dellemc.powerflex.snapshot:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_id: "fe6cb28200000007"
    sdc:
    - sdc_ip: "198.10.xxx.xxx"
      iops_limit: 11
      bandwidth_limit: 4096
    - sdc_id: "663ac0d200000001"
      iops_limit: 20
      bandwidth_limit: 2048
    allow_multiple_mappings: true
    sdc_state: "mapped"
    state: "present"

- name: Extend the size of snapshot
  dellemc.powerflex.snapshot:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_id: "fe6cb28200000007"
    size: 16
    state: "present"

- name: Unmap SDCs from snapshot
  dellemc.powerflex.snapshot:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_id: "fe6cb28200000007"
    sdc:
      - sdc_ip: "198.10.xxx.xxx"
      - sdc_id: "663ac0d200000001"
    sdc_state: "unmapped"
    state: "present"

- name: Rename snapshot
  dellemc.powerflex.snapshot:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_id: "fe6cb28200000007"
    snapshot_new_name: "ansible_renamed_snapshot_10"
    state: "present"

- name: Delete snapshot
  dellemc.powerflex.snapshot:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_id: "fe6cb28200000007"
    remove_mode: "ONLY_ME"
    state: "absent"
```

## [Return Values](snapshot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `false` |
| **snapshot_details**  dictionary | Details of the snapshot.  **Returned:** When snapshot exists  **Sample:** `{"accessModeLimit": "ReadOnly", "ancestorVolumeId": "cdd883cf00000002", "ancestorVolumeName": "ansible-volume-1", "autoSnapshotGroupId": null, "compressionMethod": "Invalid", "consistencyGroupId": "22f1e80c00000001", "creationTime": 1631619229, "dataLayout": "MediumGranularity", "id": "cdd883d000000004", "links": [{"href": "/api/instances/Volume::cdd883d000000004", "rel": "self"}, {"href": "/api/instances/Volume::cdd883d000000004/relationships /Statistics", "rel": "/api/Volume/relationship/Statistics"}, {"href": "/api/instances/Volume::cdd883cf00000002", "rel": "/api/parent/relationship/ancestorVolumeId"}, {"href": "/api/instances/VTree::6e86255c00000001", "rel": "/api/parent/relationship/vtreeId"}, {"href": "/api/instances/StoragePool::e0d8f6c900000000", "rel": "/api/parent/relationship/storagePoolId"}], "lockedAutoSnapshot": false, "lockedAutoSnapshotMarkedForRemoval": false, "managedBy": "ScaleIO", "mappedSdcInfo": null, "name": "ansible_vol_snap_1", "notGenuineSnapshot": false, "originalExpiryTime": 0, "pairIds": null, "replicationJournalVolume": false, "replicationTimeStamp": 0, "retentionInHours": 0, "retentionLevels": [], "secureSnapshotExpTime": 0, "sizeInGb": 16, "sizeInKb": 16777216, "snplIdOfAutoSnapshot": null, "snplIdOfSourceVolume": null, "storagePoolId": "e0d8f6c900000000", "storagePoolName": "pool1", "timeStampIsAccurate": false, "useRmcache": false, "volumeReplicationState": "UnmarkedForReplication", "volumeType": "Snapshot", "vtreeId": "6e86255c00000001"}` |
| **ancestorVolumeId**  string | The ID of the root of the specified volume’s V-Tree.  **Returned:** success |
| **ancestorVolumeName**  string | The name of the root of the specified volume’s V-Tree.  **Returned:** success |
| **creationTime**  integer | The creation time of the snapshot.  **Returned:** success |
| **id**  string | The ID of the snapshot.  **Returned:** success |
| **mappedSdcInfo**  dictionary | The details of the mapped SDC.  **Returned:** success |
| **accessMode**  string | Mapping access mode for the specified snapshot.  **Returned:** success |
| **limitBwInMbps**  integer | Bandwidth limit for the SDC.  **Returned:** success |
| **limitIops**  integer | IOPS limit for the SDC.  **Returned:** success |
| **sdcId**  string | ID of the SDC.  **Returned:** success |
| **sdcIp**  string | IP of the SDC.  **Returned:** success |
| **sdcName**  string | Name of the SDC.  **Returned:** success |
| **name**  string | Name of the snapshot.  **Returned:** success |
| **retentionInHours**  integer | Retention of the snapshot in hours.  **Returned:** success |
| **secureSnapshotExpTime**  integer | Expiry time of the snapshot.  **Returned:** success |
| **sizeInGb**  integer | Size of the snapshot.  **Returned:** success |
| **sizeInKb**  integer | Size of the snapshot.  **Returned:** success |
| **storagePoolId**  string | The ID of the Storage pool in which snapshot resides.  **Returned:** success |
| **storagePoolName**  string | The name of the Storage pool in which snapshot resides.  **Returned:** success |

### Authors

- Akash Shendge (@shenda1)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
