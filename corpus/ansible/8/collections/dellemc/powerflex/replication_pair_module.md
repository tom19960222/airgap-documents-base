---
collection: ansible
version: "8"
title: "dellemc.powerflex.replication_pair module – Manage replication pairs on Dell PowerFlex"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/replication_pair_module.html
fetched_at: 2026-07-28T02:05:12+00:00
---
# dellemc.powerflex.replication_pair module – Manage replication pairs on Dell PowerFlex

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
> see [Requirements](replication_pair_module.md#ansible-collections-dellemc-powerflex-replication-pair-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.powerflex.replication_pair`.

New in dellemc.powerflex 1.6.0

- [Synopsis](replication_pair_module.md#synopsis)
- [Requirements](replication_pair_module.md#requirements)
- [Parameters](replication_pair_module.md#parameters)
- [Notes](replication_pair_module.md#notes)
- [Examples](replication_pair_module.md#examples)
- [Return Values](replication_pair_module.md#return-values)

## [Synopsis](replication_pair_module.md#id1)

- Managing replication pairs on PowerFlex storage system includes getting details, creating, pause, resume initial copy and deleting a replication pair.

## [Requirements](replication_pair_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.13 or later.
- PyPowerFlex 1.8.0.
- Python 3.9, 3.10 or 3.11.

## [Parameters](replication_pair_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the PowerFlex host. |
| **pair_id**  string | The ID of the replication pair.  Mutually exclusive with *pair_name*. |
| **pair_name**  string | The name of the replication pair.  Mutually exclusive with *pair_id*. |
| **pairs**  list / elements=dictionary | List of replication pairs to add to rcg. |
| **copy_type**  string / required | Copy type.  **Choices:**   - `"Identical"` - `"OnlineCopy"` - `"OnlineHashCopy"` - `"OfflineCopy"` |
| **name**  string | Name of replication pair. |
| **source_volume_id**  string | Source volume ID.  Mutually exclusive with *source_volume_name*. |
| **source_volume_name**  string | Source volume name.  Mutually exclusive with *source_volume_id*. |
| **target_volume_id**  string | Target volume ID.  Mutually exclusive with *target_volume_name*. |
| **target_volume_name**  string | Target volume name.  If specified, *remote_peer* details should also be specified.  Mutually exclusive with *target_volume_id*. |
| **password**  string / required | The password of the PowerFlex host. |
| **pause**  boolean | Pause or resume the initial copy of replication pair.  **Choices:**   - `false` - `true` |
| **port**  integer | Port number through which communication happens with PowerFlex host.  **Default:** `443` |
| **rcg_id**  string | The ID of the replication consistency group.  Mutually exclusive with *rcg_name*. |
| **rcg_name**  string | The name of the replication consistency group.  Mutually exclusive with *rcg_id*. |
| **remote_peer**  dictionary | Remote peer system. |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the remote peer gateway host. |
| **password**  string / required | The password of the remote peer gateway host. |
| **port**  integer | Port number through which communication happens with remote peer gateway host.  **Default:** `443` |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **username**  string / required | The username of the remote peer gateway host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | State of the replication pair.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **username**  string / required | The username of the PowerFlex host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](replication_pair_module.md#id4)

> **Note:**
>
> - The *check_mode* is supported.
> - In 4.0 the creation of replication pair fails when *copy_type* is specified as `OfflineCopy`.
> - The modules present in the collection named as ‘dellemc.powerflex’ are built to support the Dell PowerFlex storage platform.

## [Examples](replication_pair_module.md#id5)

```yaml+jinja
- name: Get replication pair details
  dellemc.powerflex.replication_pair:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    pair_id: "123"

- name: Create a replication pair
  dellemc.powerflex.replication_pair:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "test_rcg"
    pairs:
      - source_volume_id: "002"
        target_volume_id: "001"
        copy_type: "OnlineCopy"
        name: "pair1"

- name: Create a replication pair with target volume name
  dellemc.powerflex.replication_pair:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "test_rcg"
    pairs:
      - source_volume_name: "src_vol"
        target_volume_name: "dest_vol"
        copy_type: "OnlineCopy"
        name: "pair1"
    remote_peer:
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        validate_certs: "{{validate_certs}}"
        port: "{{port}}"

- name: Pause replication pair
  dellemc.powerflex.replication_pair:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    pair_name: "pair1"
    pause: true

- name: Resume replication pair
  dellemc.powerflex.replication_pair:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    pair_name: "pair1"
    pause: false

- name: Delete replication pair
  dellemc.powerflex.replication_pair:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    pair_name: "pair1"
    state: "absent"
```

## [Return Values](replication_pair_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `false` |
| **rcg_replication_pairs**  list / elements=string | Details of the replication pairs of rcg.  **Returned:** When rcg exists  **Sample:** `[{"copyType": "OnlineCopy", "id": "23aa0bc900000001", "initialCopyPriority": -1, "initialCopyState": "Done", "lifetimeState": "Normal", "localActivityState": "RplEnabled", "localVolumeId": "e2bc1fab00000008", "localVolumeName": "vol1", "name": null, "peerSystemName": null, "remoteActivityState": "RplEnabled", "remoteCapacityInMB": 8192, "remoteId": "a058446700000001", "remoteVolumeId": "1cda7af20000000d", "remoteVolumeName": "vol", "replicationConsistencyGroupId": "e2ce036b00000002", "userRequestedPauseTransmitInitCopy": false}]` |
| **copyType**  string | The copy type of the replication pair.  **Returned:** success |
| **id**  string | The ID of the replication pair.  **Returned:** success |
| **initialCopyPriority**  integer | Initial copy priority.  **Returned:** success |
| **initialCopyState**  string | The inital copy state of the replication pair.  **Returned:** success |
| **lifetimeState**  integer | Lifetime state of replication pair.  **Returned:** success |
| **localActivityState**  string | The state of activity of the local replication pair.  **Returned:** success |
| **localVolumeId**  string | The ID of the local volume.  **Returned:** success |
| **localVolumeName**  string | The name of the local volume.  **Returned:** success |
| **name**  string | The name of the replication pair.  **Returned:** success |
| **peerSystemName**  integer | Peer system name.  **Returned:** success |
| **remoteActivityState**  string | The state of activity of the remote replication pair.  **Returned:** success |
| **remoteCapacityInMB**  integer | Remote Capacity in MB.  **Returned:** success |
| **remoteId**  string | The ID of the remote replication pair.  **Returned:** success |
| **remoteVolumeId**  integer | Remote Volume ID.  **Returned:** success |
| **remoteVolumeName**  integer | Remote Volume Name.  **Returned:** success |
| **replicationConsistencyGroupId**  string | The ID of the replication consistency group.  **Returned:** success |
| **userRequestedPauseTransmitInitCopy**  integer | Value of user requested pause transmit initial copy.  **Returned:** success |
| **replication_pair_details**  dictionary | Details of the replication pair.  **Returned:** When replication pair exists  **Sample:** `{"copyType": "OnlineCopy", "id": "23aa0bc900000001", "initialCopyPriority": -1, "initialCopyState": "Done", "lifetimeState": "Normal", "localActivityState": "RplEnabled", "localVolumeId": "e2bc1fab00000008", "localVolumeName": "vol1", "name": null, "peerSystemName": null, "remoteActivityState": "RplEnabled", "remoteCapacityInMB": 8192, "remoteId": "a058446700000001", "remoteVolumeId": "1cda7af20000000d", "remoteVolumeName": "vol", "replicationConsistencyGroupId": "e2ce036b00000002", "userRequestedPauseTransmitInitCopy": false}` |
| **copyType**  string | The copy type of the replication pair.  **Returned:** success |
| **id**  string | The ID of the replication pair.  **Returned:** success |
| **initialCopyPriority**  integer | Initial copy priority.  **Returned:** success |
| **initialCopyState**  string | The inital copy state of the replication pair.  **Returned:** success |
| **lifetimeState**  integer | Lifetime state of replication pair.  **Returned:** success |
| **localActivityState**  string | The state of activity of the local replication pair.  **Returned:** success |
| **localVolumeId**  string | The ID of the local volume.  **Returned:** success |
| **localVolumeName**  string | The name of the local volume.  **Returned:** success |
| **name**  string | The name of the replication pair.  **Returned:** success |
| **peerSystemName**  integer | Peer system name.  **Returned:** success |
| **remoteActivityState**  string | The state of activity of the remote replication pair.  **Returned:** success |
| **remoteCapacityInMB**  integer | Remote Capacity in MB.  **Returned:** success |
| **remoteId**  string | The ID of the remote replication pair.  **Returned:** success |
| **remoteVolumeId**  integer | Remote Volume ID.  **Returned:** success |
| **remoteVolumeName**  integer | Remote Volume Name.  **Returned:** success |
| **replicationConsistencyGroupId**  string | The ID of the replication consistency group.  **Returned:** success |
| **userRequestedPauseTransmitInitCopy**  integer | Value of user requested pause transmit initial copy.  **Returned:** success |

### Authors

- Jennifer John (@Jennifer-John)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
