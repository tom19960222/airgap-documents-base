---
collection: ansible
version: "8"
title: "community.general.statusio_maintenance module – Create maintenance windows for your status.io dashboard"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/statusio_maintenance_module.html
fetched_at: 2026-07-28T01:50:49+00:00
---
# community.general.statusio_maintenance module – Create maintenance windows for your status.io dashboard

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.statusio_maintenance`.

- [Synopsis](statusio_maintenance_module.md#synopsis)
- [Parameters](statusio_maintenance_module.md#parameters)
- [Attributes](statusio_maintenance_module.md#attributes)
- [Notes](statusio_maintenance_module.md#notes)
- [Examples](statusio_maintenance_module.md#examples)

## [Synopsis](statusio_maintenance_module.md#id1)

- Creates a maintenance window for status.io
- Deletes a maintenance window for status.io

Aliases: monitoring.statusio_maintenance

## [Parameters](statusio_maintenance_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **all_infrastructure_affected**  boolean | If it affects all components and containers  **Choices:**   - `false` ← (default) - `true` |
| **api_id**  string / required | Your unique API ID from status.io |
| **api_key**  string / required | Your unique API Key from status.io |
| **automation**  boolean | Automatically start and end the maintenance window  **Choices:**   - `false` ← (default) - `true` |
| **components**  aliases: component  list / elements=string | The given name of your component (server name) |
| **containers**  aliases: container  list / elements=string | The given name of your container (data center) |
| **desc**  string | Message describing the maintenance window  **Default:** `"Created by Ansible"` |
| **maintenance_id**  string | The maintenance id number when deleting a maintenance window |
| **maintenance_notify_1_hr**  boolean | Notify subscribers 1 hour before maintenance start time  **Choices:**   - `false` ← (default) - `true` |
| **maintenance_notify_24_hr**  boolean | Notify subscribers 24 hours before maintenance start time  **Choices:**   - `false` ← (default) - `true` |
| **maintenance_notify_72_hr**  boolean | Notify subscribers 72 hours before maintenance start time  **Choices:**   - `false` ← (default) - `true` |
| **maintenance_notify_now**  boolean | Notify subscribers now  **Choices:**   - `false` ← (default) - `true` |
| **minutes**  integer | The length of time in UTC that the maintenance will run (starting from playbook runtime)  **Default:** `10` |
| **start_date**  string | Date maintenance is expected to start (Month/Day/Year) (UTC)  End Date is worked out from start_date + minutes |
| **start_time**  string | Time maintenance is expected to start (Hour:Minutes) (UTC)  End Time is worked out from start_time + minutes |
| **state**  string | Desired state of the package.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **statuspage**  string / required | Your unique StatusPage ID from status.io |
| **title**  string | A descriptive title for the maintenance window  **Default:** `"A new maintenance window"` |
| **url**  string | Status.io API URL. A private apiary can be used instead.  **Default:** `"https://api.status.io"` |

## [Attributes](statusio_maintenance_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](statusio_maintenance_module.md#id4)

> **Note:**
>
> - You can use the apiary API url (<http://docs.statusio.apiary.io/>) to capture API traffic
> - Use start_date and start_time with minutes to set future maintenance window

## [Examples](statusio_maintenance_module.md#id5)

```yaml+jinja
- name: Create a maintenance window for 10 minutes on server1, with automation to stop the maintenance
  community.general.statusio_maintenance:
    title: Router Upgrade from ansible
    desc: Performing a Router Upgrade
    components: server1.example.com
    api_id: api_id
    api_key: api_key
    statuspage: statuspage_id
    maintenance_notify_1_hr: true
    automation: true

- name: Create a maintenance window for 60 minutes on server1 and server2
  community.general.statusio_maintenance:
    title: Routine maintenance
    desc: Some security updates
    components:
      - server1.example.com
      - server2.example.com
    minutes: 60
    api_id: api_id
    api_key: api_key
    statuspage: statuspage_id
    maintenance_notify_1_hr: true
    automation: true
  delegate_to: localhost

- name: Create a future maintenance window for 24 hours to all hosts inside the Primary Data Center
  community.general.statusio_maintenance:
    title: Data center downtime
    desc: Performing a Upgrade to our data center
    components: Primary Data Center
    api_id: api_id
    api_key: api_key
    statuspage: statuspage_id
    start_date: 01/01/2016
    start_time: 12:00
    minutes: 1440

- name: Delete a maintenance window
  community.general.statusio_maintenance:
    title: Remove a maintenance window
    maintenance_id: 561f90faf74bc94a4700087b
    statuspage: statuspage_id
    api_id: api_id
    api_key: api_key
    state: absent
```

### Authors

- Benjamin Copeland (@bhcopeland)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
