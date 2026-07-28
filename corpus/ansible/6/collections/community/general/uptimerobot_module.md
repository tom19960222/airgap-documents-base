---
collection: ansible
version: "6"
title: "community.general.uptimerobot module – Pause and start Uptime Robot monitoring"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/uptimerobot_module.html
fetched_at: 2026-07-27T17:13:41+00:00
---
# community.general.uptimerobot module – Pause and start Uptime Robot monitoring

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](uptimerobot_module.md#ansible-collections-community-general-uptimerobot-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.uptimerobot`.

- [Synopsis](uptimerobot_module.md#synopsis)
- [Requirements](uptimerobot_module.md#requirements)
- [Parameters](uptimerobot_module.md#parameters)
- [Notes](uptimerobot_module.md#notes)
- [Examples](uptimerobot_module.md#examples)

## [Synopsis](uptimerobot_module.md#id1)

- This module will let you start and pause Uptime Robot Monitoring

## [Requirements](uptimerobot_module.md#id2)

The below requirements are needed on the host that executes this module.

- Valid Uptime Robot API Key

## [Parameters](uptimerobot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **apikey**  string / required | Uptime Robot API key. |
| **monitorid**  string / required | ID of the monitor to check. |
| **state**  string / required | Define whether or not the monitor should be running or paused.  Choices:   - `"started"` - `"paused"` |

## [Notes](uptimerobot_module.md#id4)

> **Note:**
>
> - Support for adding and removing monitors and alert contacts has not yet been implemented.

## [Examples](uptimerobot_module.md#id5)

```yaml+jinja
- name: Pause the monitor with an ID of 12345
  community.general.uptimerobot:
    monitorid: 12345
    apikey: 12345-1234512345
    state: paused

- name: Start the monitor with an ID of 12345
  community.general.uptimerobot:
    monitorid: 12345
    apikey: 12345-1234512345
    state: started
```

### Authors

- Nate Kingsley (@nate-kingsley)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
