---
collection: ansible
version: "6"
title: "community.general.logentries module – Module for tracking logs via logentries.com"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/logentries_module.html
fetched_at: 2026-07-27T17:10:35+00:00
---
# community.general.logentries module – Module for tracking logs via logentries.com

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
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
- [Notes](logentries_module.md#notes)
- [Examples](logentries_module.md#examples)

## [Synopsis](logentries_module.md#id1)

- Sends logs to LogEntries in realtime

## [Parameters](logentries_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **logtype**  aliases: type  string | type of the log |
| **name**  string | name of the log |
| **path**  string / required | path to a log file |
| **state**  string | following state of the log  Choices:   - `"present"` ← (default) - `"absent"` - `"followed"` - `"unfollowed"` |

## [Notes](logentries_module.md#id3)

> **Note:**
>
> - Requires the LogEntries agent which can be installed following the instructions at logentries.com

## [Examples](logentries_module.md#id4)

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

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
