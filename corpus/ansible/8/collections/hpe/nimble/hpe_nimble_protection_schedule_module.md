---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_protection_schedule module – Manage the HPE Nimble Storage protection schedules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_protection_schedule_module.html
fetched_at: 2026-07-28T02:34:25+00:00
---
# hpe.nimble.hpe_nimble_protection_schedule module – Manage the HPE Nimble Storage protection schedules

> **Note:**
>
> This module is part of the [hpe.nimble collection](https://galaxy.ansible.com/ui/repo/published/hpe/nimble/) (version 1.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hpe.nimble`.
> You need further requirements to be able to use this module,
> see [Requirements](hpe_nimble_protection_schedule_module.md#ansible-collections-hpe-nimble-hpe-nimble-protection-schedule-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_protection_schedule`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_protection_schedule_module.md#synopsis)
- [Requirements](hpe_nimble_protection_schedule_module.md#requirements)
- [Parameters](hpe_nimble_protection_schedule_module.md#parameters)
- [Notes](hpe_nimble_protection_schedule_module.md#notes)
- [Examples](hpe_nimble_protection_schedule_module.md#examples)

## [Synopsis](hpe_nimble_protection_schedule_module.md#id1)

- Manage the protection schedules on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_protection_schedule_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_protection_schedule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **at_time**  integer | Time of day when snapshot should be taken. In case repeat frequency specifies more than one snapshot in a day then the until_time option specifies until what time of day to take snapshots.  **Default:** `0` |
| **change_name**  string | Change the name of existing protection schedule. |
| **days**  string | Specifies which days snapshots should be taken. Comma separated list of days of the week or ‘all’. |
| **description**  string | Description of the schedule. |
| **disable_appsync**  boolean | Disables application synchronized snapshots and creates crash consistent snapshots instead.  **Choices:**   - `false` - `true` |
| **downstream_partner**  string | Specifies the partner name if snapshots created by this schedule should be replicated. |
| **host**  string / required | HPE Nimble Storage IP address. |
| **name**  string / required | Name of the protection schedule to create. |
| **num_retain**  integer | Number of snapshots to retain. If replication is enabled on this schedule the array will always retain the latest replicated snapshot, which may exceed the specified retention value. This is necessary to ensure efficient replication performance. |
| **num_retain_replica**  integer | Number of snapshots to retain on the replica.  **Default:** `0` |
| **password**  string / required | HPE Nimble Storage password. |
| **period**  integer | Repeat interval for snapshots with respect to the period_unit. For example, a value of 2 with the ‘period_unit’ of ‘hours’ results in one snapshot every 2 hours. |
| **period_unit**  string | Time unit over which to take the number of snapshots specified in ‘period’. For example, a value of ‘days’ with a ‘period’ of ‘1’ results in one snapshot every day.  **Choices:**   - `"minutes"` - `"hours"` - `"days"` - `"weeks"` |
| **prot_template_name**  string | Name of the protection template in which this protection schedule is attached to. |
| **repl_alert_thres**  integer | Replication alert threshold in seconds. If the replication of a snapshot takes more than this amount of time to complete an alert will be generated. Enter 0 to disable this alert. |
| **replicate_every**  integer | Specifies which snapshots should be replicated. If snapshots are replicated and this option is not specified, every snapshot is replicated. |
| **schedule_type**  string | Normal schedules have internal timers which drive snapshot creation. An externally driven schedule has no internal timers. All snapshot activity is driven by an external trigger. In other words, these schedules are used only for externally driven manual snapshots.  **Choices:**   - `"regular"` - `"external_trigger"` |
| **skip_db_consistency_check**  boolean | Skip consistency check for database files on snapshots created by this schedule. This option only applies to snapshot schedules of a protection template with application synchronization set to VSS, application ID set to MS Exchange 2010 or later w/DAG, this schedule’s snap_verify option set to yes, and its disable_appsync option set to false. Skipping consistency checks is only recommended if each database in a DAG has multiple copies.  **Choices:**   - `false` - `true` |
| **snap_verify**  boolean | Run verification tool on snapshot created by this schedule. This option can only be used with snapshot schedules of a protection template that has application synchronization. The tool used to verify snapshot depends on the type of application. For example, if application synchronization is VSS and the application ID is Exchange, eseutil tool is run on the snapshots. If verification fails, the logs are not truncated.  **Choices:**   - `false` - `true` |
| **state**  string / required | The protection schedule operations  **Choices:**   - `"present"` - `"absent"` - `"create"` |
| **until_time**  integer | Time of day to stop taking snapshots. Applicable only when repeat frequency specifies more than one snapshot in a day. |
| **use_downstream_for_DR**  boolean | Break synchronous replication for the specified volume collection and present downstream volumes to host(s). Downstream volumes in the volume collection will be set to online and presented to the host(s) using new serial and LUN numbers. No changes will be made to the upstream volumes, their serial and LUN numbers, and their online state. The existing ACLs on the upstream volumes will be copied to the downstream volumes. Use this in conjunction with an empty downstream_partner_id. This unconfigures synchronous replication when the partner is removed from the last replicating schedule in the specified volume collection and presents the downstream volumes to host(s). Host(s) will need to be configured to access the new volumes with the newly assigned serial and LUN numbers. Use this option to expose downstream volumes in a synchronously replicated volume collection to host(s) only when the upstream partner is confirmed to be down and there is no communication between partners. Do not execute this operation if a previous Group Management Service takeover has been performed on a different array. Do not perform a subsequent Group Management Service takeover on a different array as it will lead to irreconcilable conflicts. This limitation is cleared once the Group management service backup array has successfully synchronized after reconnection.  **Choices:**   - `false` - `true` |
| **username**  string / required | HPE Nimble Storage user name. |
| **volcoll_name**  string | Name of the volume collection in which this protection schedule is attached to. |
| **volcoll_or_prottmpl_type**  string / required | Type of the protection policy this schedule is attached to.  **Choices:**   - `"protection_template"` - `"volume_collection"` |

## [Notes](hpe_nimble_protection_schedule_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_protection_schedule_module.md#id5)

```yaml+jinja
# if state is create , then create a protection schedule if not present. Fails if already present.
# if state is present, then create a protection schedule if not present. Succeed if it already exists.
- name: Create protection schedule if not present
  hpe.nimble.hpe_nimble_protection_schedule:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    description: "{{ description | default(None)}}"
    state: "{{ state | default('present') }}"
    volcoll_or_prottmpl_type: "{{ volcoll_or_prottmpl_type }}"
    prot_template_name: "{{ prot_template_name }}"
    num_retain: "{{ num_retain }}"

- name: Delete protection schedule
  hpe.nimble.hpe_nimble_protection_schedule:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    volcoll_or_prottmpl_type: "{{ volcoll_or_prottmpl_type }}"
    volcoll_name: "{{ volcoll_name }}"
    state: absent
```

### Authors

- Alok Ranjan (@ranjanal)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
