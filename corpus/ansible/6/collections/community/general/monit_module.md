---
collection: ansible
version: "6"
title: "community.general.monit module – Manage the state of a program monitored via Monit"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/monit_module.html
fetched_at: 2026-07-27T17:10:59+00:00
---
# community.general.monit module – Manage the state of a program monitored via Monit

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
> To use it in a playbook, specify: `community.general.monit`.

- [Synopsis](monit_module.md#synopsis)
- [Parameters](monit_module.md#parameters)
- [Examples](monit_module.md#examples)

## [Synopsis](monit_module.md#id1)

- Manage the state of a program monitored via *Monit*.

## [Parameters](monit_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | The name of the *monit* program/process to manage. |
| **state**  string / required | The state of service.  Choices:   - `"present"` - `"started"` - `"stopped"` - `"restarted"` - `"monitored"` - `"unmonitored"` - `"reloaded"` |
| **timeout**  integer | If there are pending actions for the service monitored by monit, then Ansible will check for up to this many seconds to verify the requested action has been performed. Ansible will sleep for five seconds between each check.  Default: `300` |

## [Examples](monit_module.md#id3)

```yaml+jinja
- name: Manage the state of program httpd to be in started state
  community.general.monit:
    name: httpd
    state: started
```

### Authors

- Darryl Stoflet (@dstoflet)
- Simon Kelly (@snopoke)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
