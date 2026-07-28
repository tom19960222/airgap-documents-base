---
collection: ansible
version: "8"
title: "dellemc.powerflex.volume module – Manage volumes on Dell PowerFlex"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/volume_module.html
fetched_at: 2026-07-28T02:05:17+00:00
---
# dellemc.powerflex.volume module – Manage volumes on Dell PowerFlex

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
> see [Requirements](volume_module.md#ansible-collections-dellemc-powerflex-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.powerflex.volume`.

New in dellemc.powerflex 1.0.0

- [Synopsis](volume_module.md#synopsis)
- [Requirements](volume_module.md#requirements)
- [Parameters](volume_module.md#parameters)
- [Notes](volume_module.md#notes)
- [Examples](volume_module.md#examples)
- [Return Values](volume_module.md#return-values)

## [Synopsis](volume_module.md#id1)

- Managing volumes on PowerFlex storage system includes creating, getting details, modifying attributes and deleting volume.
- It also includes adding/removing snapshot policy, mapping/unmapping volume to/from SDC and listing associated snapshots.

Aliases: dellemc_powerflex_volume

## [Requirements](volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.13 or later.
- PyPowerFlex 1.8.0.
- Python 3.9, 3.10 or 3.11.

## [Parameters](volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_multiple_mappings**  boolean | Specifies whether to allow or not allow multiple mappings.  If the volume is mapped to one SDC then for every new mapping *allow_multiple_mappings* has to be passed as true.  **Choices:**   - `false` - `true` |
| **auto_snap_remove_type**  string | Whether to remove or detach the snapshot policy.  To remove/detach snapshot policy, empty *snapshot_policy_id*/*snapshot_policy_name* is to be passed along with *auto_snap_remove_type*.  If the snapshot policy name/id is passed empty then *auto_snap_remove_type* is defaulted to `detach`.  **Choices:**   - `"remove"` - `"detach"` |
| **cap_unit**  string | The unit of the volume size. It defaults to ‘GB’.  **Choices:**   - `"GB"` - `"TB"` |
| **compression_type**  string | Type of the compression method.  **Choices:**   - `"NORMAL"` - `"NONE"` |
| **delete_snapshots**  boolean | If `true`, the volume and all its dependent snapshots will be deleted.  If `false`, only the volume will be deleted.  It can be specified only when the *state* is `absent`.  It defaults to `false`, if not specified.  **Choices:**   - `false` - `true` |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the PowerFlex host. |
| **password**  string / required | The password of the PowerFlex host. |
| **port**  integer | Port number through which communication happens with PowerFlex host.  **Default:** `443` |
| **protection_domain_id**  string | The ID of the protection domain.  During creation of a volume, if more than one storage pool exists with the same name then either protection domain name or id must be mentioned along with it.  Mutually exclusive with *protection_domain_name*. |
| **protection_domain_name**  string | The name of the protection domain.  During creation of a volume, if more than one storage pool exists with the same name then either protection domain name or id must be mentioned along with it.  Mutually exclusive with *protection_domain_id*. |
| **sdc**  list / elements=dictionary | Specifies SDC parameters. |
| **access_mode**  string | Define the access mode for all mappings of the volume.  **Choices:**   - `"READ_WRITE"` - `"READ_ONLY"` - `"NO_ACCESS"` |
| **bandwidth_limit**  integer | Limit of volume network bandwidth.  Need to mention in multiple of 1024 Kbps.  To set no limit, 0 is to be passed. |
| **iops_limit**  integer | Limit of volume IOPS.  Minimum IOPS limit is 11 and specify 0 for unlimited iops. |
| **sdc_id**  string | ID of the SDC.  Specify either *sdc_name*, *sdc_id* or *sdc_ip*.  Mutually exclusive with *sdc_name* and *sdc_ip*. |
| **sdc_ip**  string | IP of the SDC.  Specify either *sdc_name*, *sdc_id* or *sdc_ip*.  Mutually exclusive with *sdc_id* and *sdc_ip*. |
| **sdc_name**  string | Name of the SDC.  Specify either *sdc_name*, *sdc_id* or *sdc_ip*.  Mutually exclusive with *sdc_id* and *sdc_ip*. |
| **sdc_state**  string | Mapping state of the SDC.  **Choices:**   - `"mapped"` - `"unmapped"` |
| **size**  integer | The size of the volume.  Size of the volume will be assigned as higher multiple of 8 GB. |
| **snapshot_policy_id**  string | ID of the snapshot policy.  To remove/detach snapshot policy, empty *snapshot_policy_id*/*snapshot_policy_name* is to be passed along with *auto_snap_remove_type*. |
| **snapshot_policy_name**  string | Name of the snapshot policy.  To remove/detach snapshot policy, empty *snapshot_policy_id*/*snapshot_policy_name* is to be passed along with *auto_snap_remove_type*. |
| **state**  string / required | State of the volume.  **Choices:**   - `"present"` - `"absent"` |
| **storage_pool_id**  string | The ID of the storage pool.  Either name or the id of the storage pool is required for creating a volume.  Mutually exclusive with *storage_pool_name*. |
| **storage_pool_name**  string | The name of the storage pool.  Either name or the id of the storage pool is required for creating a volume.  During creation, if storage pool name is provided then either protection domain name or id must be mentioned along with it.  Mutually exclusive with *storage_pool_id*. |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **use_rmcache**  boolean | Whether to use RM Cache or not.  **Choices:**   - `false` - `true` |
| **username**  string / required | The username of the PowerFlex host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **vol_id**  string | The ID of the volume.  Except create operation, all other operations can be performed using *vol_id*.  Mutually exclusive with *vol_name*. |
| **vol_name**  string | The name of the volume.  Mandatory for create operation.  It is unique across the PowerFlex array.  Mutually exclusive with *vol_id*. |
| **vol_new_name**  string | New name of the volume. Used to rename the volume. |
| **vol_type**  string | Type of volume provisioning.  **Choices:**   - `"THICK_PROVISIONED"` - `"THIN_PROVISIONED"` |

## [Notes](volume_module.md#id4)

> **Note:**
>
> - The *check_mode* is not supported.
> - The modules present in the collection named as ‘dellemc.powerflex’ are built to support the Dell PowerFlex storage platform.

## [Examples](volume_module.md#id5)

```yaml+jinja
- name: Create a volume
  dellemc.powerflex.volume:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    storage_pool_name: "pool_1"
    protection_domain_name: "pd_1"
    vol_type: "THICK_PROVISIONED"
    compression_type: "NORMAL"
    use_rmcache: true
    size: 16
    state: "present"

- name: Map a SDC to volume
  dellemc.powerflex.volume:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    allow_multiple_mappings: true
    sdc:
      - sdc_id: "92A304DB-EFD7-44DF-A07E-D78134CC9764"
        access_mode: "READ_WRITE"
    sdc_state: "mapped"
    state: "present"

- name: Unmap a SDC to volume
  dellemc.powerflex.volume:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    sdc:
      - sdc_id: "92A304DB-EFD7-44DF-A07E-D78134CC9764"
    sdc_state: "unmapped"
    state: "present"

- name: Map multiple SDCs to a volume
  dellemc.powerflex.volume:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    protection_domain_name: "pd_1"
    sdc:
      - sdc_id: "92A304DB-EFD7-44DF-A07E-D78134CC9764"
        access_mode: "READ_WRITE"
        bandwidth_limit: 2048
        iops_limit: 20
      - sdc_ip: "198.10.xxx.xxx"
        access_mode: "READ_ONLY"
    allow_multiple_mappings: true
    sdc_state: "mapped"
    state: "present"

- name: Get the details of the volume
  dellemc.powerflex.volume:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    vol_id: "fe6c8b7100000005"
    state: "present"

- name: Modify the details of the Volume
  dellemc.powerflex.volume:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    storage_pool_name: "pool_1"
    new_vol_name: "new_sample_volume"
    size: 64
    state: "present"

- name: Delete the Volume
  dellemc.powerflex.volume:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    delete_snapshots: false
    state: "absent"

- name: Delete the Volume and all its dependent snapshots
  dellemc.powerflex.volume:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    vol_name: "sample_volume"
    delete_snapshots: true
    state: "absent"
```

## [Return Values](volume_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `false` |
| **volume_details**  dictionary | Details of the volume.  **Returned:** When volume exists  **Sample:** `{"accessModeLimit": "ReadWrite", "ancestorVolumeId": null, "autoSnapshotGroupId": null, "compressionMethod": "Invalid", "consistencyGroupId": null, "creationTime": 1631618520, "dataLayout": "MediumGranularity", "id": "cdd883cf00000002", "links": [{"href": "/api/instances/Volume::cdd883cf00000002", "rel": "self"}, {"href": "/api/instances/Volume::cdd883cf00000002/relationships /Statistics", "rel": "/api/Volume/relationship/Statistics"}, {"href": "/api/instances/VTree::6e86255c00000001", "rel": "/api/parent/relationship/vtreeId"}, {"href": "/api/instances/StoragePool::e0d8f6c900000000", "rel": "/api/parent/relationship/storagePoolId"}], "lockedAutoSnapshot": false, "lockedAutoSnapshotMarkedForRemoval": false, "managedBy": "ScaleIO", "mappedSdcInfo": null, "name": "ansible-volume-1", "notGenuineSnapshot": false, "originalExpiryTime": 0, "pairIds": null, "protectionDomainId": "9300c1f900000000", "protectionDomainName": "domain1", "replicationJournalVolume": false, "replicationTimeStamp": 0, "retentionLevels": [], "secureSnapshotExpTime": 0, "sizeInGB": 16, "sizeInKb": 16777216, "snapshotPolicyId": null, "snapshotPolicyName": null, "snapshotsList": [{"accessModeLimit": "ReadOnly", "ancestorVolumeId": "cdd883cf00000002", "autoSnapshotGroupId": null, "compressionMethod": "Invalid", "consistencyGroupId": "22f1e80c00000001", "creationTime": 1631619229, "dataLayout": "MediumGranularity", "id": "cdd883d000000004", "links": [{"href": "/api/instances/Volume::cdd883d000000004", "rel": "self"}, {"href": "/api/instances/Volume::cdd883d000000004 /relationships/Statistics", "rel": "/api/Volume/relationship/Statistics"}, {"href": "/api/instances/Volume::cdd883cf00000002", "rel": "/api/parent/relationship/ancestorVolumeId"}, {"href": "/api/instances/VTree::6e86255c00000001", "rel": "/api/parent/relationship/vtreeId"}, {"href": "/api/instances/StoragePool::e0d8f6c900000000", "rel": "/api/parent/relationship/storagePoolId"}], "lockedAutoSnapshot": false, "lockedAutoSnapshotMarkedForRemoval": false, "managedBy": "ScaleIO", "mappedSdcInfo": null, "name": "ansible_vol_snap_1", "notGenuineSnapshot": false, "originalExpiryTime": 0, "pairIds": null, "replicationJournalVolume": false, "replicationTimeStamp": 0, "retentionLevels": [], "secureSnapshotExpTime": 0, "sizeInKb": 16777216, "snplIdOfAutoSnapshot": null, "snplIdOfSourceVolume": null, "storagePoolId": "e0d8f6c900000000", "timeStampIsAccurate": false, "useRmcache": false, "volumeReplicationState": "UnmarkedForReplication", "volumeType": "Snapshot", "vtreeId": "6e86255c00000001"}], "snplIdOfAutoSnapshot": null, "snplIdOfSourceVolume": null, "statistics": {"childVolumeIds": [], "descendantVolumeIds": [], "initiatorSdcId": null, "mappedSdcIds": ["c42425XXXXXX"], "numOfChildVolumes": 0, "numOfDescendantVolumes": 0, "numOfMappedSdcs": 1, "registrationKey": null, "registrationKeys": [], "replicationJournalVolume": false, "replicationState": "UnmarkedForReplication", "reservationType": "NotReserved", "rplTotalJournalCap": 0, "rplUsedJournalCap": 0, "userDataReadBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataSdcReadLatency": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataSdcTrimLatency": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataSdcWriteLatency": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataTrimBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}, "userDataWriteBwc": {"numOccured": 0, "numSeconds": 0, "totalWeightInKb": 0}}, "storagePoolId": "e0d8f6c900000000", "storagePoolName": "pool1", "timeStampIsAccurate": false, "useRmcache": false, "volumeReplicationState": "UnmarkedForReplication", "volumeType": "ThinProvisioned", "vtreeId": "6e86255c00000001"}` |
| **id**  string | The ID of the volume.  **Returned:** success |
| **mappedSdcInfo**  dictionary | The details of the mapped SDC.  **Returned:** success |
| **accessMode**  string | Mapping access mode for the specified volume.  **Returned:** success |
| **limitBwInMbps**  integer | Bandwidth limit for the SDC.  **Returned:** success |
| **limitIops**  integer | IOPS limit for the SDC.  **Returned:** success |
| **sdcId**  string | ID of the SDC.  **Returned:** success |
| **sdcIp**  string | IP of the SDC.  **Returned:** success |
| **sdcName**  string | Name of the SDC.  **Returned:** success |
| **name**  string | Name of the volume.  **Returned:** success |
| **protectionDomainId**  string | ID of the protection domain in which volume resides.  **Returned:** success |
| **protectionDomainName**  string | Name of the protection domain in which volume resides.  **Returned:** success |
| **sizeInGb**  integer | Size of the volume in Gb.  **Returned:** success |
| **sizeInKb**  integer | Size of the volume in Kb.  **Returned:** success |
| **snapshotPolicyId**  string | ID of the snapshot policy associated with volume.  **Returned:** success |
| **snapshotPolicyName**  string | Name of the snapshot policy associated with volume.  **Returned:** success |
| **snapshotsList**  string | List of snapshots associated with the volume.  **Returned:** success |
| **statistics**  dictionary | Statistics details of the storage pool.  **Returned:** success |
| **numOfChildVolumes**  integer | Number of child volumes.  **Returned:** success |
| **numOfMappedSdcs**  integer | Number of mapped Sdcs of the volume.  **Returned:** success |
| **storagePoolId**  string | ID of the storage pool in which volume resides.  **Returned:** success |
| **storagePoolName**  string | Name of the storage pool in which volume resides.  **Returned:** success |

### Authors

- P Srinivas Rao (@srinivas-rao5)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
