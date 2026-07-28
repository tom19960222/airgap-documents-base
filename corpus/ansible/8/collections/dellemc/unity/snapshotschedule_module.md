---
collection: ansible
version: "8"
title: "dellemc.unity.snapshotschedule module – Manage snapshot schedules on Unity storage system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/unity/snapshotschedule_module.html
fetched_at: 2026-07-28T02:05:30+00:00
---
# dellemc.unity.snapshotschedule module – Manage snapshot schedules on Unity storage system

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
> see [Requirements](snapshotschedule_module.md#ansible-collections-dellemc-unity-snapshotschedule-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.unity.snapshotschedule`.

New in dellemc.unity 1.1.0

- [Synopsis](snapshotschedule_module.md#synopsis)
- [Requirements](snapshotschedule_module.md#requirements)
- [Parameters](snapshotschedule_module.md#parameters)
- [Notes](snapshotschedule_module.md#notes)
- [Examples](snapshotschedule_module.md#examples)
- [Return Values](snapshotschedule_module.md#return-values)

## [Synopsis](snapshotschedule_module.md#id1)

- Managing snapshot schedules on Unity storage system includes creating new snapshot schedule, getting details of snapshot schedule, modifying attributes of snapshot schedule, and deleting snapshot schedule.

Aliases: dellemc_unity_snapshotschedule

## [Requirements](snapshotschedule_module.md#id2)

The below requirements are needed on the host that executes this module.

- A Dell Unity Storage device version 5.1 or later.
- Ansible-core 2.13 or later.
- Python 3.9, 3.10 or 3.11.
- Storops Python SDK 1.2.11.

## [Parameters](snapshotschedule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_delete**  boolean | Indicates whether the system can automatically delete the snapshot.  **Choices:**   - `false` - `true` |
| **day_interval**  integer | Number of days between snapshots.  Applicable only when rule type is `every_n_days`. |
| **day_of_month**  integer | Day of the month for which the snapshot schedule rule applies.  Applicable only when rule type is `every_month`.  Value should be [1, 31]. |
| **days_of_week**  list / elements=string | Days of the week for which the snapshot schedule rule applies.  Applicable only when rule type is `every_week`.  **Choices:**   - `"SUNDAY"` - `"MONDAY"` - `"TUESDAY"` - `"WEDNESDAY"` - `"THURSDAY"` - `"FRIDAY"` - `"SATURDAY"` |
| **desired_retention**  integer | The number of days/hours for which snapshot will be retained.  When *auto_delete* is `true`, *desired_retention* cannot be specified.  Maximum desired retention supported is 31 days or 744 hours. |
| **hour**  integer | The hour when the snapshot will be taken.  Applicable for `every_n_days`, `every_week`, `every_month` rule types.  For create operation, if *hour* parameter is not specified, value will be taken as `0`.  Value should be [0, 23]. |
| **hours_of_day**  list / elements=integer | Hours of the day when the snapshot will be taken.  Applicable only when rule type is `every_day`. |
| **id**  string | The ID of the snapshot schedule. |
| **interval**  integer | Number of hours between snapshots.  Applicable only when rule type is `every_n_hours`. |
| **minute**  integer | Minute offset from the hour when the snapshot will be taken.  Applicable for all rule types.  For a create operation, if *minute* parameter is not specified, value will be taken as `0`.  Value should be [0, 59]. |
| **name**  string | The name of the snapshot schedule.  Name is mandatory for a create operation.  Specify either *name* or *id* (but not both) for any operation. |
| **password**  string / required | The password of the Unity management server. |
| **port**  integer | Port number through which communication happens with Unity management server.  **Default:** `443` |
| **retention_unit**  string | The retention unit for the snapshot.  **Choices:**   - `"hours"` ← (default) - `"days"` |
| **state**  string / required | Define whether the snapshot schedule should exist or not.  **Choices:**   - `"absent"` - `"present"` |
| **type**  string | Type of the rule to be included in snapshot schedule.  Type is mandatory for any create or modify operation.  Once the snapshot schedule is created with one type it can be modified.  **Choices:**   - `"every_n_hours"` - `"every_day"` - `"every_n_days"` - `"every_week"` - `"every_month"` |
| **unispherehost**  string / required | IP or FQDN of the Unity management server. |
| **username**  string / required | The username of the Unity management server. |
| **validate_certs**  aliases: verifycert  boolean | Boolean variable to specify whether or not to validate SSL certificate.  `true` - Indicates that the SSL certificate should be verified.  `false` - Indicates that the SSL certificate should not be verified.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](snapshotschedule_module.md#id4)

> **Note:**
>
> - Snapshot schedule created through Ansible will have only one rule.
> - Modification of rule type is not allowed. Within the same type, other parameters can be modified.
> - If an existing snapshot schedule has more than 1 rule in it, only get and delete operation is allowed.
> - The *check_mode* is not supported.
> - The modules present in this collection named as ‘dellemc.unity’ are built to support the Dell Unity storage platform.

## [Examples](snapshotschedule_module.md#id5)

```yaml+jinja
- name: Create snapshot schedule (Rule Type - every_n_hours)
  dellemc.unity.snapshotschedule:
      unispherehost: "{{unispherehost}}"
      validate_certs: "{{validate_certs}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_N_Hours_Testing"
      type: "every_n_hours"
      interval: 6
      desired_retention: 24
      state: "{{state_present}}"

- name: Create snapshot schedule (Rule Type - every_day)
  dellemc.unity.snapshotschedule:
      unispherehost: "{{unispherehost}}"
      validate_certs: "{{validate_certs}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_Day_Testing"
      type: "every_day"
      hours_of_day:
        - 8
        - 14
      auto_delete: true
      state: "{{state_present}}"

- name: Create snapshot schedule (Rule Type - every_n_days)
  dellemc.unity.snapshotschedule:
      unispherehost: "{{unispherehost}}"
      validate_certs: "{{validate_certs}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_N_Day_Testing"
      type: "every_n_days"
      day_interval: 2
      desired_retention: 16
      retention_unit: "days"
      state: "{{state_present}}"

- name: Create snapshot schedule (Rule Type - every_week)
  dellemc.unity.snapshotschedule:
      unispherehost: "{{unispherehost}}"
      validate_certs: "{{validate_certs}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_Week_Testing"
      type: "every_week"
      days_of_week:
        - MONDAY
        - FRIDAY
      hour: 12
      minute: 30
      desired_retention: 200
      state: "{{state_present}}"

- name: Create snapshot schedule (Rule Type - every_month)
  dellemc.unity.snapshotschedule:
      unispherehost: "{{unispherehost}}"
      validate_certs: "{{validate_certs}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_Month_Testing"
      type: "every_month"
      day_of_month: 17
      auto_delete: true
      state: "{{state_present}}"

- name: Get snapshot schedule details using name
  dellemc.unity.snapshotschedule:
      unispherehost: "{{unispherehost}}"
      validate_certs: "{{validate_certs}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_N_Hours_Testing"
      state: "{{state_present}}"

- name: Get snapshot schedule details using id
  dellemc.unity.snapshotschedule:
      unispherehost: "{{unispherehost}}"
      validate_certs: "{{validate_certs}}"
      username: "{{username}}"
      password: "{{password}}"
      id: "{{id}}"
      state: "{{state_present}}"

- name: Modify snapshot schedule details id
  dellemc.unity.snapshotschedule:
      unispherehost: "{{unispherehost}}"
      validate_certs: "{{validate_certs}}"
      username: "{{username}}"
      password: "{{password}}"
      id: "{{id}}"
      type: "every_n_hours"
      interval: 8
      state: "{{state_present}}"

- name: Modify snapshot schedule using name
  dellemc.unity.snapshotschedule:
      unispherehost: "{{unispherehost}}"
      validate_certs: "{{validate_certs}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_Day_Testing"
      type: "every_day"
      desired_retention: 200
      auto_delete: false
      state: "{{state_present}}"

- name: Delete snapshot schedule using id
  dellemc.unity.snapshotschedule:
      unispherehost: "{{unispherehost}}"
      validate_certs: "{{validate_certs}}"
      username: "{{username}}"
      password: "{{password}}"
      id: "{{id}}"
      state: "{{state_absent}}"

- name: Delete snapshot schedule using name
  dellemc.unity.snapshotschedule:
      unispherehost: "{{unispherehost}}"
      validate_certs: "{{validate_certs}}"
      username: "{{username}}"
      password: "{{password}}"
      name: "Ansible_Every_Day_Testing"
      state: "{{state_absent}}"
```

## [Return Values](snapshotschedule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether or not the resource has changed.  **Returned:** always  **Sample:** `true` |
| **snapshot_schedule_details**  dictionary | Details of the snapshot schedule.  **Returned:** When snapshot schedule exists  **Sample:** `{"existed": true, "hash": 8742032390151, "id": "snapSch_63", "is_default": false, "is_modified": null, "is_sync_replicated": false, "luns": null, "modification_time": "2021-12-14 21:37:47.905000+00:00", "name": "SS7_empty_hour_SS", "rules": [{"access_type": "FilesystemSnapAccessTypeEnum.CHECKPOINT", "days_of_month": null, "days_of_week": {"DayOfWeekEnumList": []}, "existed": true, "hash": 8742032280772, "hours": [0], "id": "SchedRule_109", "interval": 2, "is_auto_delete": false, "minute": 0, "retention_time": 86400, "retention_time_in_hours": 24, "rule_type": "every_n_days", "type": "ScheduleTypeEnum.N_DAYS_AT_HHMM"}], "storage_resources": null, "version": "ScheduleVersionEnum.LEGACY"}` |
| **id**  string | The system ID given to the snapshot schedule.  **Returned:** success |
| **luns**  dictionary | Details of volumes for which snapshot schedule applied.  **Returned:** success |
| **UnityLunList**  list / elements=string | List of volumes for which snapshot schedule applied.  **Returned:** success |
| **UnityLun**  dictionary | Detail of volume.  **Returned:** success |
| **id**  string | The system ID given to volume.  **Returned:** success |
| **name**  string | The name of the snapshot schedule.  **Returned:** success |
| **rules**  list / elements=string | Details of rules that apply to snapshot schedule.  **Returned:** success |
| **days_of_month**  list / elements=string | Days of the month for which the snapshot schedule rule applies.  **Returned:** success |
| **days_of_week**  dictionary | Days of the week for which the snapshot schedule rule applies.  **Returned:** success |
| **DayOfWeekEnumList**  list / elements=string | Enumeration of days of the week.  **Returned:** success |
| **hours**  list / elements=string | Hourly frequency for the snapshot schedule rule.  **Returned:** success |
| **id**  string | The system ID of the rule.  **Returned:** success |
| **interval**  integer | Number of days or hours between snaps, depending on the rule type.  **Returned:** success |
| **is_auto_delete**  boolean | Indicates whether the system can automatically delete the snapshot based on pool automatic-deletion thresholds.  **Returned:** success |
| **minute**  integer | Minute frequency for the snapshot schedule rule.  **Returned:** success |
| **retention_time**  integer | Period of time in seconds for which to keep the snapshot.  **Returned:** success |
| **retention_time_in_hours**  integer | Period of time in hours for which to keep the snapshot.  **Returned:** success |
| **rule_type**  string | Type of the rule applied to snapshot schedule.  **Returned:** success |
| **storage_resources**  dictionary | Details of storage resources for which snapshot. schedule applied.  **Returned:** success |
| **UnityStorageResourceList**  list / elements=string | List of storage resources for which snapshot schedule applied.  **Returned:** success |
| **UnityStorageResource**  dictionary | Detail of storage resource.  **Returned:** success |
| **id**  string | The system ID given to storage resource.  **Returned:** success |

### Authors

- Akash Shendge (@shenda1)

### Collection links

- [Issue Tracker](https://www.dell.com/community/Automation/bd-p/Automation)
- [Repository (Sources)](https://github.com/dell/ansible-unity/tree/1.7.1)
