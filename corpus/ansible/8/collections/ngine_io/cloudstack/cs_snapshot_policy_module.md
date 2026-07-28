---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_snapshot_policy module – Manages volume snapshot policies on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_snapshot_policy_module.html
fetched_at: 2026-07-28T02:46:24+00:00
---
# ngine_io.cloudstack.cs_snapshot_policy module – Manages volume snapshot policies on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/cloudstack/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_snapshot_policy_module.md#ansible-collections-ngine-io-cloudstack-cs-snapshot-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_snapshot_policy`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_snapshot_policy_module.md#synopsis)
- [Requirements](cs_snapshot_policy_module.md#requirements)
- [Parameters](cs_snapshot_policy_module.md#parameters)
- [Notes](cs_snapshot_policy_module.md#notes)
- [Examples](cs_snapshot_policy_module.md#examples)
- [Return Values](cs_snapshot_policy_module.md#return-values)

## [Synopsis](cs_snapshot_policy_module.md#id1)

- Create, update and delete volume snapshot policies.

## [Requirements](cs_snapshot_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_snapshot_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the volume is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **device_id**  integer | ID of the device on a VM the volume is attached to.  This will only be considered if VM has multiple DATADISK volumes. |
| **domain**  string | Domain the volume is related to. |
| **interval_type**  aliases: interval  string | Interval of the snapshot.  **Choices:**   - `"hourly"` - `"daily"` ← (default) - `"weekly"` - `"monthly"` |
| **max_snaps**  aliases: max  integer | Max number of snapshots.  **Default:** `8` |
| **project**  string | Name of the project the volume is related to. |
| **schedule**  string | Time the snapshot is scheduled. Required if *state=present*.  Format for *interval_type=HOURLY*: `MM`  Format for *interval_type=DAILY*: `MM:HH`  Format for *interval_type=WEEKLY*: `MM:HH:DD (1-7`)  Format for *interval_type=MONTHLY*: `MM:HH:DD (1-28`) |
| **state**  string | State of the snapshot policy.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **time_zone**  aliases: timezone  string | Specifies a timezone for this command.  **Default:** `"UTC"` |
| **vm**  string | Name of the instance to select the volume from.  Use *volume_type* if VM has a DATADISK and ROOT volume.  In case of *volume_type=DATADISK*, additionally use *device_id* if VM has more than one DATADISK volume.  Either *volume* or *vm* is required. |
| **volume**  string | Name of the volume.  Either *volume* or *vm* is required. |
| **volume_type**  string | Type of the volume.  **Choices:**   - `"DATADISK"` - `"ROOT"` |
| **vpc**  string | Name of the vpc the instance is deployed in. |

## [Notes](cs_snapshot_policy_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_snapshot_policy_module.md#id5)

```yaml+jinja
- name: ensure a snapshot policy daily at 1h00 UTC
  ngine_io.cloudstack.cs_snapshot_policy:
    volume: ROOT-478
    schedule: '00:1'
    max_snaps: 3

- name: ensure a snapshot policy daily at 1h00 UTC on the second DATADISK of VM web-01
  ngine_io.cloudstack.cs_snapshot_policy:
    vm: web-01
    volume_type: DATADISK
    device_id: 2
    schedule: '00:1'
    max_snaps: 3

- name: ensure a snapshot policy hourly at minute 5 UTC
  ngine_io.cloudstack.cs_snapshot_policy:
    volume: ROOT-478
    schedule: '5'
    interval_type: hourly
    max_snaps: 1

- name: ensure a snapshot policy weekly on Sunday at 05h00, TZ Europe/Zurich
  ngine_io.cloudstack.cs_snapshot_policy:
    volume: ROOT-478
    schedule: '00:5:1'
    interval_type: weekly
    max_snaps: 1
    time_zone: 'Europe/Zurich'

- name: ensure a snapshot policy is absent
  ngine_io.cloudstack.cs_snapshot_policy:
    volume: ROOT-478
    interval_type: hourly
    state: absent
```

## [Return Values](cs_snapshot_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the volume is related to.  **Returned:** success  **Sample:** `"example account"` |
| **domain**  string | Domain the volume is related to.  **Returned:** success  **Sample:** `"example domain"` |
| **id**  string | UUID of the snapshot policy.  **Returned:** success  **Sample:** `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **interval_type**  string | interval type of the snapshot policy.  **Returned:** success  **Sample:** `"daily"` |
| **max_snaps**  integer | maximum number of snapshots retained.  **Returned:** success  **Sample:** `10` |
| **project**  string | Name of project the volume is related to.  **Returned:** success  **Sample:** `"Production"` |
| **schedule**  string | schedule of the snapshot policy.  **Returned:** success |
| **time_zone**  string | the time zone of the snapshot policy.  **Returned:** success  **Sample:** `"Etc/UTC"` |
| **volume**  string | the volume of the snapshot policy.  **Returned:** success  **Sample:** `"Etc/UTC"` |
| **zone**  string | Name of zone the volume is related to.  **Returned:** success  **Sample:** `"ch-gva-2"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
