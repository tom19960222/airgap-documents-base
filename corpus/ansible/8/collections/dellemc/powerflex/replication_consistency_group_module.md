---
collection: ansible
version: "8"
title: "dellemc.powerflex.replication_consistency_group module – Manage replication consistency groups on Dell PowerFlex"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/powerflex/replication_consistency_group_module.html
fetched_at: 2026-07-28T02:05:11+00:00
---
# dellemc.powerflex.replication_consistency_group module – Manage replication consistency groups on Dell PowerFlex

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
> see [Requirements](replication_consistency_group_module.md#ansible-collections-dellemc-powerflex-replication-consistency-group-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.powerflex.replication_consistency_group`.

New in dellemc.powerflex 1.5.0

- [Synopsis](replication_consistency_group_module.md#synopsis)
- [Requirements](replication_consistency_group_module.md#requirements)
- [Parameters](replication_consistency_group_module.md#parameters)
- [Notes](replication_consistency_group_module.md#notes)
- [Examples](replication_consistency_group_module.md#examples)
- [Return Values](replication_consistency_group_module.md#return-values)

## [Synopsis](replication_consistency_group_module.md#id1)

- Managing replication consistency groups on PowerFlex storage system includes getting details, creating, modifying, creating snapshots, pause, resume, freeze, unfreeze, activate, failover, reverse, restore, sync, switchover, inactivate and deleting a replication consistency group.

## [Requirements](replication_consistency_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell PowerFlex storage system version 3.5 or later.
- Ansible-core 2.13 or later.
- PyPowerFlex 1.8.0.
- Python 3.9, 3.10 or 3.11.

## [Parameters](replication_consistency_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **activity_mode**  string | Activity mode of RCG.  This parameter is supported for version 3.6 and above.  **Choices:**   - `"Active"` - `"Inactive"` |
| **create_snapshot**  boolean | Whether to create the snapshot of the replication consistency group.  **Choices:**   - `false` - `true` |
| **force**  boolean | Force switchover the RCG.  **Choices:**   - `false` - `true` |
| **freeze**  boolean | Freeze or unfreeze the RCG.  This parameter is deprecated. Use rcg_state instead.  **Choices:**   - `false` - `true` |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the PowerFlex host. |
| **is_consistent**  boolean | Consistency of RCG.  **Choices:**   - `false` - `true` |
| **new_rcg_name**  string | Name of RCG to rename to. |
| **password**  string / required | The password of the PowerFlex host. |
| **pause**  boolean | Pause or resume the RCG.  This parameter is deprecated. Use rcg_state instead.  **Choices:**   - `false` - `true` |
| **pause_mode**  string | Pause mode.  It is required if pause is set as true.  **Choices:**   - `"StopDataTransfer"` - `"OnlyTrackChanges"` |
| **port**  integer | Port number through which communication happens with PowerFlex host.  **Default:** `443` |
| **protection_domain_id**  string | Protection domain id.  Mutually exclusive with *protection_domain_name*. |
| **protection_domain_name**  string | Protection domain name.  Mutually exclusive with *protection_domain_id*. |
| **rcg_id**  string | The ID of the replication consistency group.  Mutually exclusive with *rcg_name*. |
| **rcg_name**  string | The name of the replication consistency group.  It is unique across the PowerFlex array.  Mutually exclusive with *rcg_id*. |
| **rcg_state**  string | Specify an action for RCG.  Failover the RCG.  Reverse the RCG.  Restore the RCG.  Switchover the RCG.  Pause or resume the RCG.  Freeze or unfreeze the RCG.  Synchronize the RCG.  **Choices:**   - `"failover"` - `"reverse"` - `"restore"` - `"switchover"` - `"sync"` - `"pause"` - `"resume"` - `"freeze"` - `"unfreeze"` |
| **remote_peer**  dictionary | Remote peer system. |
| **hostname**  aliases: gateway_host  string / required | IP or FQDN of the remote peer gateway host. |
| **password**  string / required | The password of the remote peer gateway host. |
| **port**  integer | Port number through which communication happens with remote peer gateway host.  **Default:** `443` |
| **protection_domain_id**  string | Remote protection domain id.  Mutually exclusive with *protection_domain_name*. |
| **protection_domain_name**  string | Remote protection domain name.  Mutually exclusive with *protection_domain_id*. |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **username**  string / required | The username of the remote peer gateway host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |
| **rpo**  integer | Desired RPO in seconds. |
| **state**  string | State of the replication consistency group.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **target_volume_access_mode**  string | Target volume access mode.  **Choices:**   - `"ReadOnly"` - `"NoAccess"` |
| **timeout**  integer | Time after which connection will get terminated.  It is to be mentioned in seconds.  **Default:** `120` |
| **username**  string / required | The username of the PowerFlex host. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](replication_consistency_group_module.md#id4)

> **Note:**
>
> - The *check_mode* is supported.
> - Idempotency is not supported for create snapshot operation.
> - There is a delay in reflection of final state of RCG after few update operations on RCG.
> - In 3.6 and above, the replication consistency group will return back to consistent mode on changing to inconsistent mode if consistence barrier arrives. Hence idempotency on setting to inconsistent mode will return changed as true.
> - The modules present in the collection named as ‘dellemc.powerflex’ are built to support the Dell PowerFlex storage platform.

## [Examples](replication_consistency_group_module.md#id5)

```yaml+jinja
- name: Get RCG details
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "{{rcg_name}}"

- name: Create a snapshot of the RCG
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_id: "{{rcg_id}}"
    create_snapshot: true
    state: "present"

- name: Create a replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    rpo: 60
    protection_domain_name: "domain1"
    activity_mode: "active"
    remote_peer:
      hostname: "{{hostname}}"
      username: "{{username}}"
      password: "{{password}}"
      validate_certs: "{{validate_certs}}"
      port: "{{port}}"
      protection_domain_name: "domain1"

- name: Modify replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    rpo: 60
    target_volume_access_mode: "ReadOnly"
    activity_mode: "Inactive"
    is_consistent: true

- name: Rename replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    new_rcg_name: "rcg_test_rename"

- name: Pause replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    rcg_state: "pause"
    pause_mode: "StopDataTransfer"

- name: Resume replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    rcg_state: "resume"

- name: Freeze replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    rcg_state: "freeze"

- name: UnFreeze replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    rcg_state: "unfreeze"

- name: Failover replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    rcg_state: "failover"

- name: Reverse replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    rcg_state: "reverse"

- name: Restore replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    rcg_state: "restore"

- name: Switchover replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    rcg_state: "switchover"

- name: Synchronize replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    rcg_state: "sync"

- name: Delete replication consistency group
  dellemc.powerflex.replication_consistency_group:
    hostname: "{{hostname}}"
    username: "{{username}}"
    password: "{{password}}"
    validate_certs: "{{validate_certs}}"
    port: "{{port}}"
    rcg_name: "rcg_test"
    state: "absent"
```

## [Return Values](replication_consistency_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `false` |
| **replication_consistency_group_details**  dictionary | Details of the replication consistency group.  **Returned:** When replication consistency group exists  **Sample:** `{"abstractState": "Ok", "activeLocal": true, "activeRemote": true, "currConsistMode": "Consistent", "disasterRecoveryState": "None", "error": 65, "failoverState": "None", "failoverType": "None", "freezeState": "Unfrozen", "id": "aadc17d500000000", "inactiveReason": 11, "lastSnapCreationRc": "SUCCESS", "lastSnapGroupId": "e58280b300000001", "lifetimeState": "Normal", "localActivityState": "Active", "name": "test_rcg", "pauseMode": "None", "peerMdmId": "6c3d94f600000000", "protectionDomainId": "b969400500000000", "remoteActivityState": "Active", "remoteDisasterRecoveryState": "None", "remoteId": "2130961a00000000", "remoteMdmId": "0e7a082862fedf0f", "remoteProtectionDomainId": "4eeb304600000000", "remoteProtectionDomainName": "domain1", "replicationDirection": "LocalToRemote", "rpoInSeconds": 30, "snapCreationInProgress": false, "targetVolumeAccessMode": "NoAccess", "type": "User"}` |
| **abstractState**  string | The abstract state of the replication consistency group.  **Returned:** success |
| **activeLocal**  boolean | Whether the local replication consistency group is active.  **Returned:** success |
| **activeRemote**  boolean | Whether the remote replication consistency group is active  **Returned:** success |
| **currConsistMode**  string | The current consistency mode of the replication consistency group.  **Returned:** success |
| **disasterRecoveryState**  string | The state of disaster recovery of the local replication consistency group.  **Returned:** success |
| **error**  integer | The error code of the replication consistency group.  **Returned:** success |
| **failoverState**  string | The state of failover of the replication consistency group.  **Returned:** success |
| **failoverType**  string | The type of failover of the replication consistency group.  **Returned:** success |
| **freezeState**  string | The freeze state of the replication consistency group.  **Returned:** success |
| **id**  string | The ID of the replication consistency group.  **Returned:** success |
| **inactiveReason**  integer | The reason for the inactivity of the replication consistency group.  **Returned:** success |
| **lastSnapCreationRc**  integer | The return code of the last snapshot of the replication consistency group.  **Returned:** success |
| **lastSnapGroupId**  string | ID of the last snapshot of the replication consistency group.  **Returned:** success |
| **lifetimeState**  string | The Lifetime state of the replication consistency group.  **Returned:** success |
| **localActivityState**  string | The state of activity of the local replication consistency group.  **Returned:** success |
| **name**  string | The name of the replication consistency group.  **Returned:** success |
| **pauseMode**  string | The Lifetime state of the replication consistency group.  **Returned:** success |
| **peerMdmId**  string | The ID of the peer MDM of the replication consistency group.  **Returned:** success |
| **protectionDomainId**  string | The Protection Domain ID of the replication consistency group.  **Returned:** success |
| **remoteActivityState**  string | The state of activity of the remote replication consistency group..  **Returned:** success |
| **remoteDisasterRecoveryState**  string | The state of disaster recovery of the remote replication consistency group.  **Returned:** success |
| **remoteId**  string | The ID of the remote replication consistency group.  **Returned:** success |
| **remoteMdmId**  string | The ID of the remote MDM of the replication consistency group.  **Returned:** success |
| **remoteProtectionDomainId**  string | The ID of the remote Protection Domain.  **Returned:** success |
| **remoteProtectionDomainName**  string | The Name of the remote Protection Domain.  **Returned:** success |
| **replicationDirection**  string | The direction of the replication of the replication consistency group.  **Returned:** success |
| **rpoInSeconds**  integer | The RPO value of the replication consistency group in seconds.  **Returned:** success |
| **snapCreationInProgress**  boolean | Whether the process of snapshot creation of the replication consistency group is in progress or not.  **Returned:** success |
| **targetVolumeAccessMode**  string | The access mode of the target volume of the replication consistency group.  **Returned:** success |
| **type**  string | The type of the replication consistency group.  **Returned:** success |

### Authors

- Trisha Datta (@Trisha-Datta)
- Jennifer John (@Jennifer-John)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-powerflex/tree/1.9.0)
