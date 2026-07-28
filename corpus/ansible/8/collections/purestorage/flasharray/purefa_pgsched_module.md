---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_pgsched module – Manage protection groups replication schedules on Pure Storage FlashArrays"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_pgsched_module.html
fetched_at: 2026-07-28T02:51:12+00:00
---
# purestorage.flasharray.purefa_pgsched module – Manage protection groups replication schedules on Pure Storage FlashArrays

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_pgsched_module.md#ansible-collections-purestorage-flasharray-purefa-pgsched-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_pgsched`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_pgsched_module.md#synopsis)
- [Requirements](purefa_pgsched_module.md#requirements)
- [Parameters](purefa_pgsched_module.md#parameters)
- [Notes](purefa_pgsched_module.md#notes)
- [Examples](purefa_pgsched_module.md#examples)

## [Synopsis](purefa_pgsched_module.md#id1)

- Modify or delete protection groups replication schedules on Pure Storage FlashArrays.

## [Requirements](purefa_pgsched_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_pgsched_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **all_for**  integer | Specifies the length of time, in seconds, to keep the snapshots on the source array before they are eradicated.  Range available 1 - 34560000. |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **blackout_end**  string | Specifies the time at which to restart replication.  Provide a time in 12-hour AM/PM format, eg. 5PM |
| **blackout_start**  string | Specifies the time at which to suspend replication.  Provide a time in 12-hour AM/PM format, eg. 11AM |
| **days**  integer | Specifies the number of days to keep the *per_day* snapshots beyond the *all_for* period before they are eradicated  Max retention period is 4000 days |
| **enabled**  boolean | Enable the schedule being configured.  **Choices:**   - `false` - `true` ← (default) |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **name**  string / required | The name of the protection group. |
| **per_day**  integer | Specifies the number of *per_day* snapshots to keep beyond the *all_for* period.  Maximum number is 1440 |
| **replicate_at**  string | Provide a time in 12-hour AM/PM format, eg. 11AM  Only valid if *replicate_frequency* is an exact multiple of 86400, ie 1 day. |
| **replicate_frequency**  integer | Specifies the replication frequency in seconds.  Range 900 - 34560000 (FA-405, //M10, //X10i and Cloud Block Store).  Range 300 - 34560000 (all other arrays). |
| **schedule**  string / required | Which schedule to change.  **Choices:**   - `"replication"` - `"snapshot"` |
| **snap_at**  string | Provide a time in 12-hour AM/PM format, eg. 11AM  Only valid if *snap_frequency* is an exact multiple of 86400, ie 1 day. |
| **snap_frequency**  integer | Specifies the snapshot frequency in seconds.  Range available 300 - 34560000. |
| **state**  string | Define whether to set or delete the protection group schedule.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **target_all_for**  integer | Specifies the length of time, in seconds, to keep the replicated snapshots on the targets.  Range is 1 - 34560000 seconds. |
| **target_days**  integer | Specifies the number of days to keep the *target_per_day* replicated snapshots beyond the *target_all_for* period before they are eradicated.  Max retention period is 4000 days |
| **target_per_day**  integer | Specifies the number of *per_day* replicated snapshots to keep beyond the *target_all_for* period.  Maximum number is 1440 |

## [Notes](purefa_pgsched_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_pgsched_module.md#id5)

```yaml+jinja
- name: Update protection group snapshot schedule
  purestorage.flasharray.purefa_pgsched:
    name: foo
    schedule: snapshot
    enabled: true
    snap_frequency: 86400
    snap_at: 3PM
    per_day: 5
    all_for: 5
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Update protection group replication schedule
  purestorage.flasharray.purefa_pgsched:
    name: foo
    schedule: replication
    enabled: true
    replicate_frequency: 86400
    replicate_at: 3PM
    target_per_day: 5
    target_all_for: 5
    blackout_start: 2AM
    blackout_end: 5AM
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete protection group snapshot schedule
  purestorage.flasharray.purefa_pgsched:
    name: foo
    schedule: snapshot
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete protection group replication schedule
  purestorage.flasharray.purefa_pgsched:
    name: foo
    schedule: replication
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
