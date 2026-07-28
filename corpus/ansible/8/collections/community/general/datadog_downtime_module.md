---
collection: ansible
version: "8"
title: "community.general.datadog_downtime module – Manages Datadog downtimes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/datadog_downtime_module.html
fetched_at: 2026-07-28T01:45:18+00:00
---
# community.general.datadog_downtime module – Manages Datadog downtimes

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](datadog_downtime_module.md#ansible-collections-community-general-datadog-downtime-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.datadog_downtime`.

New in community.general 2.0.0

- [Synopsis](datadog_downtime_module.md#synopsis)
- [Requirements](datadog_downtime_module.md#requirements)
- [Parameters](datadog_downtime_module.md#parameters)
- [Attributes](datadog_downtime_module.md#attributes)
- [Examples](datadog_downtime_module.md#examples)
- [Return Values](datadog_downtime_module.md#return-values)

## [Synopsis](datadog_downtime_module.md#id1)

- Manages downtimes within Datadog.
- Options as described on <https://docs.datadoghq.com/api/v1/downtimes/>.

Aliases: monitoring.datadog.datadog_downtime

## [Requirements](datadog_downtime_module.md#id2)

The below requirements are needed on the host that executes this module.

- datadog-api-client
- Python 3.6+

## [Parameters](datadog_downtime_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string | The URL to the Datadog API.  This value can also be set with the `DATADOG_HOST` environment variable.  **Default:** `"https://api.datadoghq.com"` |
| **api_key**  string / required | Your Datadog API key. |
| **app_key**  string / required | Your Datadog app key. |
| **downtime_message**  string | A message to include with notifications for this downtime.  Email notifications can be sent to specific users by using the same “@username” notation as events. |
| **end**  integer | POSIX timestamp to end the downtime. If not provided, the downtime is in effect until you cancel it. |
| **id**  integer | The identifier of the downtime.  If empty, a new downtime gets created, otherwise it is either updated or deleted depending of the `state`.  To keep your playbook idempotent, you should save the identifier in a file and read it in a lookup. |
| **monitor_id**  integer | The ID of the monitor to mute. If not provided, the downtime applies to all monitors. |
| **monitor_tags**  list / elements=string | A list of monitor tags to which the downtime applies.  The resulting downtime applies to monitors that match ALL provided monitor tags. |
| **rrule**  string | The `RRULE` standard for defining recurring events.  For example, to have a recurring event on the first day of each month, select a type of rrule and set the `FREQ` to `MONTHLY` and `BYMONTHDAY` to `1`.  Most common rrule options from the iCalendar Spec are supported.  Attributes specifying the duration in `RRULE` are not supported (for example `DTSTART`, `DTEND`, `DURATION`). |
| **scope**  list / elements=string | A list of scopes to which the downtime applies.  The resulting downtime applies to sources that matches ALL provided scopes. |
| **start**  integer | POSIX timestamp to start the downtime. If not provided, the downtime starts the moment it is created. |
| **state**  string | The designated state of the downtime.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timezone**  string | The timezone for the downtime. |

## [Attributes](datadog_downtime_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](datadog_downtime_module.md#id5)

```yaml+jinja
- name: Create a downtime
  register: downtime_var
  community.general.datadog_downtime:
    state: present
    monitor_tags:
      - "foo:bar"
    downtime_message: "Downtime for foo:bar"
    scope: "test"
    api_key: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    app_key: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    # Lookup the id in the file and ignore errors if the file doesn't exits, so downtime gets created
    id: "{{ lookup('file', inventory_hostname ~ '_downtime_id.txt', errors='ignore') }}"
- name: Save downtime id to file for later updates and idempotence
  delegate_to: localhost
  copy:
    content: "{{ downtime.downtime.id }}"
    dest: "{{ inventory_hostname ~ '_downtime_id.txt' }}"
```

## [Return Values](datadog_downtime_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **downtime**  dictionary | The downtime returned by the API.  **Returned:** always  **Sample:** `{"active": true, "canceled": null, "creator_id": 1445416, "disabled": false, "downtime_type": 2, "end": null, "id": 1055751000, "message": "Downtime for foo:bar", "monitor_id": null, "monitor_tags": ["foo:bar"], "parent_id": null, "recurrence": null, "scope": ["test"], "start": 1607015009, "timezone": "UTC", "updater_id": null}` |

### Authors

- Datadog (@Datadog)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
