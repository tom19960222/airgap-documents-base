---
collection: ansible
version: "8"
title: "community.general.logentries module – Module for tracking logs via logentries.com"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/logentries_module.html
fetched_at: 2026-07-28T01:47:34+00:00
---
# community.general.logentries module – Module for tracking logs via logentries.com

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
> To use it in a playbook, specify: `community.general.logentries`.

- [Synopsis](logentries_module.md#synopsis)
- [Parameters](logentries_module.md#parameters)
- [Attributes](logentries_module.md#attributes)
- [Notes](logentries_module.md#notes)
- [Examples](logentries_module.md#examples)

## [Synopsis](logentries_module.md#id1)

- Sends logs to LogEntries in realtime

Aliases: monitoring.logentries

## [Parameters](logentries_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **logtype**  aliases: type  string | type of the log |
| **name**  string | name of the log |
| **path**  string / required | path to a log file |
| **state**  string | following state of the log  **Choices:**   - `"present"` ← (default) - `"absent"` - `"followed"` - `"unfollowed"` |

## [Attributes](logentries_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](logentries_module.md#id4)

> **Note:**
>
> - Requires the LogEntries agent which can be installed following the instructions at logentries.com

## [Examples](logentries_module.md#id5)

```yaml+jinja
- name: Track nginx logs
  community.general.logentries:
    path: /var/log/nginx/access.log
    state: present
    name: nginx-access-log

- name: Stop tracking nginx logs
  community.general.logentries:
    path: /var/log/nginx/error.log
    state: absent
```

### Authors

- Ivan Vanderbyl (@ivanvanderbyl)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
