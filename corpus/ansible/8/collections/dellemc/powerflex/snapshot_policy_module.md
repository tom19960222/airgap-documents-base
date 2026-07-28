---
collection: ansible
version: "8"
title: "dellemc.powerflex.snapshot_policy module – Manage snapshot policies on Dell PowerFlex"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/snapshot_policy_module.html
fetched_at: 2026-07-28T02:05:15+00:00
---
# dellemc.powerflex.snapshot_policy module – Manage snapshot policies on Dell PowerFlex

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
> see [Requirements](snapshot_policy_module.md#ansible-collections-dellemc-powerflex-snapshot-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.powerflex.snapshot_policy`.

New in dellemc.powerflex 1.7.0

- [Synopsis](snapshot_policy_module.md#synopsis)
- [Requirements](snapshot_policy_module.md#requirements)
- [Parameters](snapshot_policy_module.md#parameters)
- [Notes](snapshot_policy_module.md#notes)
- [Examples](snapshot_policy_module.md#examples)
- [Return Values](snapshot_policy_module.md#return-values)

## [Synopsis](snapshot_policy_module.md#id1)

- Managing snapshot policies on PowerFlex storage system includes creating, getting details, modifying attributes, adding a source volume, removing a source volume and deleting a snapshot policy.

## [Requirements](snapshot_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.13 or later.
- PyPowerFlex 1.8.0.
- Python 3.9, 3.10 or 3.11.

## [Parameters](snapshot_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_mode**  string | Access mode of the snapshot policy.  **Choices:**   - `"READ_WRITE"` - `"READ_ONLY"` |
| **auto_snapshot_creation_cadence**  dictionary | The auto snapshot creation cadence of the snapshot policy. |
| **time**  integer | The time between creation of two snapshots. |
| **unit**  string | The unit of the auto snapshot creation cadence.  **Choices:**   - `"Minute"` ← (default) - `"Hour"` - `"Day"` - `"Week"` |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the PowerFlex host. |
| **new_name**  string | New name of the snapshot policy. |
| **num_of_retained_snapshots_per_level**  list / elements=integer | Number of retained snapshots per level. |
| **password**  string / required | The password of the PowerFlex host. |
| **pause**  boolean | Whether to pause or resume the snapshot policy.  **Choices:**   - `false` - `true` |
| **port**  integer | Port number through which communication happens with PowerFlex host.  **Default:** `443` |
| **secure_snapshots**  boolean | Whether to secure snapshots or not.  Used only in the create operation.  **Choices:**   - `false` - `true` |
| **snapshot_policy_id**  string | The unique identifier of the snapshot policy.  Except create operation, all other operations can be performed using *snapshot_policy_id*.  Mutually exclusive with *snapshot_policy_name*. |
| **snapshot_policy_name**  string | The name of the snapshot policy.  It is unique across the PowerFlex array.  Mutually exclusive with *snapshot_policy_id*. |
| **source_volume**  list / elements=dictionary | The source volume details to be added or removed. |
| **auto_snap_removal_action**  string | Ways to handle the snapshots created by the policy (auto snapshots).  Must be provided when *state* is set to `'absent'`.  **Choices:**   - `"Remove"` - `"Detach"` |
| **detach_locked_auto_snapshots**  boolean | Whether to detach the locked auto snapshots during removal of source volume.  **Choices:**   - `false` - `true` |
| **id**  string | The unique identifier of the source volume to be added or removed.  Mutually exclusive with *name*. |
| **name**  string | The name of the source volume to be added or removed.  Mutually exclusive with *id*. |
| **state**  string | The state of the source volume.  When `present`, source volume will be added to the snapshot policy.  When `absent`, source volume will be removed from the snapshot policy.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **state**  string | State of the snapshot policy.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **username**  string / required | The username of the PowerFlex host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](snapshot_policy_module.md#id4)

> **Note:**
>
> - The *check_mode* is supported.
> - The modules present in the collection named as ‘dellemc.powerflex’ are built to support the Dell PowerFlex storage platform.

## [Examples](snapshot_policy_module.md#id5)

```yaml+jinja
- name: Create a snapshot policy
  dellemc.powerflex.snapshot_policy:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_policy_name: "snapshot_policy_name_1"
    access_mode: "READ_WRITE"
    secure_snapshots: False
    auto_snapshot_creation_cadence:
      time: 1
      unit: "Hour"
    num_of_retained_snapshots_per_level:
      - 20
    state: "present"

- name: Get snapshot policy details using name
  dellemc.powerflex.snapshot_policy:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_policy_name: "snapshot_policy_name_1"

- name: Get snapshot policy details using id
  dellemc.powerflex.snapshot_policy:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_policy_id: "snapshot_policy_id_1"

- name: Modify a snapshot policy
  dellemc.powerflex.snapshot_policy:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_policy_name: "snapshot_policy_name_1"
    auto_snapshot_creation_cadence:
      time: 2
      unit: "Hour"
    num_of_retained_snapshots_per_level:
      - 40

- name: Rename a snapshot policy
  dellemc.powerflex.snapshot_policy:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_policy_name: "snapshot_policy_name_1"
    new_name: "snapshot_policy_name_1_new"

- name: Add source volume
  dellemc.powerflex.snapshot_policy:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_policy_name: "snapshot_policy_name_1"
    source_volume:
      - name: "source_volume_name_1"
      - id: "source_volume_id_2"
        state: "present"

- name: Remove source volume
  dellemc.powerflex.snapshot_policy:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_policy_name: "{{snapshot_policy_name}}"
    source_volume:
      - name: "source_volume_name_1"
        auto_snap_removal_action: 'Remove'
        state: "absent"
      - id: "source_volume_id_2"
        auto_snap_removal_action: 'Remove'
        detach_locked_auto_snapshots: True
        state: "absent"

- name: Pause a snapshot policy
  dellemc.powerflex.snapshot_policy:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_policy_name: "{{snapshot_policy_name}}"
    pause: True

- name: Resume a snapshot policy
  dellemc.powerflex.snapshot_policy:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_policy_name: "{{snapshot_policy_name}}"
    pause: False

- name: Delete a snapshot policy
  dellemc.powerflex.snapshot_policy:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    snapshot_policy_name: "snapshot_policy_name"
    state: "absent"
```

## [Return Values](snapshot_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `false` |
| **snapshot_policy_details**  dictionary | Details of the snapshot policy.  **Returned:** When snapshot policy exists  **Sample:** `{"autoSnapshotCreationCadenceInMin": 120, "id": "15ae842800000004", "lastAutoSnapshotCreationFailureReason": "NR", "lastAutoSnapshotFailureInFirstLevel": false, "links": [{"href": "/api/instances/SnapshotPolicy::15ae842800000004", "rel": "self"}, {"href": "/api/instances/SnapshotPolicy::15ae842800000004/relationships/Statistics", "rel": "/api/SnapshotPolicy/relationship/Statistics"}, {"href": "/api/instances/SnapshotPolicy::15ae842800000004/relationships/SourceVolume", "rel": "/api/SnapshotPolicy/relationship/SourceVolume"}, {"href": "/api/instances/SnapshotPolicy::15ae842800000004/relationships/AutoSnapshotVolume", "rel": "/api/SnapshotPolicy/relationship/AutoSnapshotVolume"}, {"href": "/api/instances/System::0e7a082862fedf0f", "rel": "/api/parent/relationship/systemId"}], "maxVTreeAutoSnapshots": 40, "name": "Sample_snapshot_policy_1", "nextAutoSnapshotCreationTime": 1683709201, "numOfAutoSnapshots": 0, "numOfCreationFailures": 0, "numOfExpiredButLockedSnapshots": 0, "numOfLockedSnapshots": 0, "numOfRetainedSnapshotsPerLevel": [40], "numOfSourceVolumes": 0, "secureSnapshots": false, "snapshotAccessMode": "ReadWrite", "snapshotPolicyState": "Active", "statistics": {"autoSnapshotVolIds": [], "expiredButLockedSnapshotsIds": [], "numOfAutoSnapshots": 0, "numOfExpiredButLockedSnapshots": 0, "numOfSrcVols": 0, "srcVolIds": []}, "systemId": "0e7a082862fedf0f", "timeOfLastAutoSnapshot": 0, "timeOfLastAutoSnapshotCreationFailure": 0}` |
| **autoSnapshotCreationCadenceInMin**  integer | The snapshot rule of the snapshot policy.  **Returned:** success |
| **id**  string | The ID of the snapshot policy.  **Returned:** success |
| **lastAutoSnapshotCreationFailureReason**  string | The reason for the failure of last auto snapshot creation .  **Returned:** success |
| **lastAutoSnapshotFailureInFirstLevel**  boolean | Whether the last auto snapshot in first level failed.  **Returned:** success |
| **maxVTreeAutoSnapshots**  integer | Maximum number of VTree auto snapshots.  **Returned:** success |
| **name**  string | Name of the snapshot policy.  **Returned:** success |
| **nextAutoSnapshotCreationTime**  integer | The time of creation of the next auto snapshot.  **Returned:** success |
| **numOfAutoSnapshots**  integer | Number of auto snapshots.  **Returned:** success |
| **numOfCreationFailures**  integer | Number of creation failures.  **Returned:** success |
| **numOfExpiredButLockedSnapshots**  integer | Number of expired but locked snapshots.  **Returned:** success |
| **numOfLockedSnapshots**  integer | Number of locked snapshots.  **Returned:** success |
| **numOfRetainedSnapshotsPerLevel**  list / elements=string | Number of snapshots retained per level  **Returned:** success |
| **numOfSourceVolumes**  integer | Number of source volumes.  **Returned:** success |
| **secureSnapshots**  boolean | Whether the snapshots are secured.  **Returned:** success |
| **snapshotAccessMode**  string | Access mode of the snapshots.  **Returned:** success |
| **snapshotPolicyState**  string | State of the snapshot policy.  **Returned:** success |
| **statistics**  dictionary | Statistics details of the snapshot policy.  **Returned:** success |
| **autoSnapshotVolIds**  list / elements=string | Volume Ids of all the auto snapshots.  **Returned:** success |
| **expiredButLockedSnapshotsIds**  list / elements=string | Ids of expired but locked snapshots.  **Returned:** success |
| **numOfAutoSnapshots**  integer | Number of auto snapshots.  **Returned:** success |
| **numOfExpiredButLockedSnapshots**  integer | Number of expired but locked snapshots.  **Returned:** success |
| **numOfSrcVols**  integer | Number of source volumes.  **Returned:** success |
| **srcVolIds**  list / elements=string | Ids of the source volumes.  **Returned:** success |
| **systemId**  string | Unique identifier of the PowerFlex system.  **Returned:** success |
| **timeOfLastAutoSnapshot**  string | Time of the last auto snapshot creation.  **Returned:** success |
| **timeOfLastAutoSnapshotCreationFailure**  string | Time of the failure of the last auto snapshot creation.  **Returned:** success |

### Authors

- Trisha Datta (@trisha-dell)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
