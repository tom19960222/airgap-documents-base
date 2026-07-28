---
collection: ansible
version: "8"
title: "community.general.nagios module – Perform common tasks in Nagios related to downtime and notifications"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/nagios_module.html
fetched_at: 2026-07-28T01:48:04+00:00
---
# community.general.nagios module – Perform common tasks in Nagios related to downtime and notifications

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
> To use it in a playbook, specify: `community.general.nagios`.

- [Synopsis](nagios_module.md#synopsis)
- [Parameters](nagios_module.md#parameters)
- [Attributes](nagios_module.md#attributes)
- [Examples](nagios_module.md#examples)

## [Synopsis](nagios_module.md#id1)

- The `nagios` module has two basic functions: scheduling downtime and toggling alerts for services or hosts.
- The `nagios` module is not idempotent.
- All actions require the `host` parameter to be given explicitly. In playbooks you can use the `{{inventory_hostname}}` variable to refer to the host the playbook is currently running on.
- You can specify multiple services at once by separating them with commas, .e.g. `services=httpd,nfs,puppet`.
- When specifying what service to handle there is a special service value, `host`, which will handle alerts/downtime/acknowledge for the *host itself*, for example `services=host`. This keyword may not be given with other services at the same time. **Setting alerts/downtime/acknowledge for a host does not affect alerts/downtime/acknowledge for any of the services running on it.** To schedule downtime for all services on particular host use keyword “all”, for example `services=all`.

Aliases: monitoring.nagios

## [Parameters](nagios_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string / required | Action to take.  servicegroup options were added in 2.0.  delete_downtime options were added in 2.2.  The `acknowledge` and `forced_check` actions were added in community.general 1.2.0.  **Choices:**   - `"downtime"` - `"delete_downtime"` - `"enable_alerts"` - `"disable_alerts"` - `"silence"` - `"unsilence"` - `"silence_nagios"` - `"unsilence_nagios"` - `"command"` - `"servicegroup_service_downtime"` - `"servicegroup_host_downtime"` - `"acknowledge"` - `"forced_check"` |
| **author**  string | Author to leave downtime comments as. Only used when `action` is `downtime` or `acknowledge`.  **Default:** `"Ansible"` |
| **cmdfile**  string | Path to the nagios *command file* (FIFO pipe). Only required if auto-detection fails. |
| **command**  string | The raw command to send to nagios, which should not include the submitted time header or the line-feed.  **Required** option when using the `command` `action`. |
| **comment**  string | Comment when `action` is `downtime` or `acknowledge`.  **Default:** `"Scheduling downtime"` |
| **host**  string | Host to operate on in Nagios. |
| **minutes**  integer | Minutes to schedule downtime for.  Only usable with `action=downtime`.  **Default:** `30` |
| **servicegroup**  string | The Servicegroup we want to set downtimes/alerts for.  **Required** option when using the `servicegroup_service_downtime` and `servicegroup_host_downtime` `action`. |
| **services**  aliases: service  string | What to manage downtime/alerts for. Separate multiple services with commas.  **Required** option when `action` is one of: `downtime`, `acknowledge`, `forced_check`, `enable_alerts`, `disable_alerts`. |
| **start**  string  *added in community.general 0.2.0* | When downtime should start, in `time_t` format (epoch seconds). |

## [Attributes](nagios_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](nagios_module.md#id4)

```yaml+jinja
- name: Set 30 minutes of apache downtime
  community.general.nagios:
    action: downtime
    minutes: 30
    service: httpd
    host: '{{ inventory_hostname }}'

- name: Schedule an hour of HOST downtime
  community.general.nagios:
    action: downtime
    minutes: 60
    service: host
    host: '{{ inventory_hostname }}'

- name: Schedule an hour of HOST downtime starting at 2019-04-23T02:00:00+00:00
  community.general.nagios:
    action: downtime
    start: 1555984800
    minutes: 60
    service: host
    host: '{{ inventory_hostname }}'

- name: Schedule an hour of HOST downtime, with a comment describing the reason
  community.general.nagios:
    action: downtime
    minutes: 60
    service: host
    host: '{{ inventory_hostname }}'
    comment: Rebuilding machine

- name: Schedule downtime for ALL services on HOST
  community.general.nagios:
    action: downtime
    minutes: 45
    service: all
    host: '{{ inventory_hostname }}'

- name: Schedule downtime for a few services
  community.general.nagios:
    action: downtime
    services: frob,foobar,qeuz
    host: '{{ inventory_hostname }}'

- name: Set 30 minutes downtime for all services in servicegroup foo
  community.general.nagios:
    action: servicegroup_service_downtime
    minutes: 30
    servicegroup: foo
    host: '{{ inventory_hostname }}'

- name: Set 30 minutes downtime for all host in servicegroup foo
  community.general.nagios:
    action: servicegroup_host_downtime
    minutes: 30
    servicegroup: foo
    host: '{{ inventory_hostname }}'

- name: Delete all downtime for a given host
  community.general.nagios:
    action: delete_downtime
    host: '{{ inventory_hostname }}'
    service: all

- name: Delete all downtime for HOST with a particular comment
  community.general.nagios:
    action: delete_downtime
    host: '{{ inventory_hostname }}'
    service: host
    comment: Planned maintenance

- name: Acknowledge an HOST with a particular comment
  community.general.nagios:
    action: acknowledge
    service: host
    host: '{{ inventory_hostname }}'
    comment: 'power outage - see casenr 12345'

- name: Acknowledge an active service problem for the httpd service with a particular comment
  community.general.nagios:
    action: acknowledge
    service: httpd
    host: '{{ inventory_hostname }}'
    comment: 'service crashed - see casenr 12345'

- name: Reset a passive service check for snmp trap
  community.general.nagios:
    action: forced_check
    service: snmp
    host: '{{ inventory_hostname }}'

- name: Force an active service check for the httpd service
  community.general.nagios:
    action: forced_check
    service: httpd
    host: '{{ inventory_hostname }}'

- name: Force an active service check for all services of a particular host
  community.general.nagios:
    action: forced_check
    service: all
    host: '{{ inventory_hostname }}'

- name: Force an active service check for a particular host
  community.general.nagios:
    action: forced_check
    service: host
    host: '{{ inventory_hostname }}'

- name: Enable SMART disk alerts
  community.general.nagios:
    action: enable_alerts
    service: smart
    host: '{{ inventory_hostname }}'

- name: Disable httpd and nfs alerts
  community.general.nagios:
    action: disable_alerts
    service: httpd,nfs
    host: '{{ inventory_hostname }}'

- name: Disable HOST alerts
  community.general.nagios:
    action: disable_alerts
    service: host
    host: '{{ inventory_hostname }}'

- name: Silence ALL alerts
  community.general.nagios:
    action: silence
    host: '{{ inventory_hostname }}'

- name: Unsilence all alerts
  community.general.nagios:
    action: unsilence
    host: '{{ inventory_hostname }}'

- name: Shut up nagios
  community.general.nagios:
    action: silence_nagios

- name: Annoy me negios
  community.general.nagios:
    action: unsilence_nagios

- name: Command something
  community.general.nagios:
    action: command
    command: DISABLE_FAILURE_PREDICTION
```

### Authors

- Tim Bielawa (@tbielawa)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
