---
collection: ansible
version: "8"
title: "netapp.elementsw.na_elementsw_snapshot_schedule module – NetApp Element Software Snapshot Schedules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/elementsw/na_elementsw_snapshot_schedule_module.html
fetched_at: 2026-07-28T02:41:30+00:00
---
# netapp.elementsw.na_elementsw_snapshot_schedule module – NetApp Element Software Snapshot Schedules

> **Note:**
>
> This module is part of the [netapp.elementsw collection](https://galaxy.ansible.com/ui/repo/published/netapp/elementsw/) (version 21.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.elementsw`.
> You need further requirements to be able to use this module,
> see [Requirements](na_elementsw_snapshot_schedule_module.md#ansible-collections-netapp-elementsw-na-elementsw-snapshot-schedule-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_snapshot_schedule`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_snapshot_schedule_module.md#synopsis)
- [Requirements](na_elementsw_snapshot_schedule_module.md#requirements)
- [Parameters](na_elementsw_snapshot_schedule_module.md#parameters)
- [Notes](na_elementsw_snapshot_schedule_module.md#notes)
- [Examples](na_elementsw_snapshot_schedule_module.md#examples)
- [Return Values](na_elementsw_snapshot_schedule_module.md#return-values)

## [Synopsis](na_elementsw_snapshot_schedule_module.md#id1)

- Create, destroy, or update snapshot schedules on ElementSW

## [Requirements](na_elementsw_snapshot_schedule_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_snapshot_schedule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_id**  string | Account ID for the owner of this volume.  It accepts either account_name or account_id  if account_id is digit, it will consider as account_id  If account_id is string, it will consider as account_name |
| **days_of_month_hours**  integer | Time specified in hours |
| **days_of_month_minutes**  integer | Time specified in minutes. |
| **days_of_month_monthdays**  list / elements=integer | List of days of the month (1-31) |
| **days_of_week_hours**  integer | Time specified in hours |
| **days_of_week_minutes**  integer | Time specified in minutes. |
| **days_of_week_weekdays**  list / elements=string | List of days of the week (Sunday to Saturday) |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **name**  string / required | Name for the snapshot schedule.  It accepts either schedule_id or schedule_name  if name is digit, it will consider as schedule_id  If name is string, it will consider as schedule_name |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **paused**  boolean | Pause / Resume a schedule.  **Choices:**   - `false` - `true` |
| **recurring**  boolean | Should the schedule recur?  **Choices:**   - `false` - `true` |
| **retention**  string | Retention period for the snapshot.  Format is ‘HH:mm:ss’. |
| **schedule_type**  string | Schedule type for creating schedule.  **Choices:**   - `"DaysOfWeekFrequency"` - `"DaysOfMonthFrequency"` - `"TimeIntervalFrequency"` |
| **snapshot_name**  string | Name for the created snapshots. |
| **starting_date**  string | Starting date for the schedule.  Required when `state=present`.  Format: `2016-12-01T00:00:00Z` |
| **state**  string | Whether the specified schedule should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **time_interval_days**  integer | Time interval in days. |
| **time_interval_hours**  integer | Time interval in hours. |
| **time_interval_minutes**  integer | Time interval in minutes. |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US>. |
| **volumes**  list / elements=string | Volume IDs that you want to set the snapshot schedule for.  It accepts both volume_name and volume_id |

## [Notes](na_elementsw_snapshot_schedule_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_snapshot_schedule_module.md#id5)

```yaml+jinja
- name: Create Snapshot schedule
  na_elementsw_snapshot_schedule:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    name: Schedule_A
    schedule_type: TimeIntervalFrequency
    time_interval_days: 1
    starting_date: '2016-12-01T00:00:00Z'
    retention: '24:00:00'
    volumes:
    - 7
    - test
    account_id: 1

- name: Update Snapshot schedule
  na_elementsw_snapshot_schedule:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    name: Schedule_A
    schedule_type: TimeIntervalFrequency
    time_interval_days: 1
    starting_date: '2016-12-01T00:00:00Z'
    retention: '24:00:00'
    volumes:
    - 8
    - test1
    account_id: 1

- name: Delete Snapshot schedule
  na_elementsw_snapshot_schedule:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
    name: 6
```

## [Return Values](na_elementsw_snapshot_schedule_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **schedule_id**  string | Schedule ID of the newly created schedule  **Returned:** success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
