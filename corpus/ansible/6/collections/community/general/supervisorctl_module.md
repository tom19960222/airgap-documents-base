---
collection: ansible
version: "6"
title: "community.general.supervisorctl module – Manage the state of a program or group of programs running via supervisord"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/supervisorctl_module.html
fetched_at: 2026-07-27T17:13:27+00:00
---
# community.general.supervisorctl module – Manage the state of a program or group of programs running via supervisord

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
> see [Requirements](supervisorctl_module.md#ansible-collections-community-general-supervisorctl-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.supervisorctl`.

- [Synopsis](supervisorctl_module.md#synopsis)
- [Requirements](supervisorctl_module.md#requirements)
- [Parameters](supervisorctl_module.md#parameters)
- [Notes](supervisorctl_module.md#notes)
- [Examples](supervisorctl_module.md#examples)

## [Synopsis](supervisorctl_module.md#id1)

- Manage the state of a program or group of programs running via supervisord

## [Requirements](supervisorctl_module.md#id2)

The below requirements are needed on the host that executes this module.

- supervisorctl

## [Parameters](supervisorctl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  path | The supervisor configuration file path |
| **name**  string / required | The name of the supervisord program or group to manage.  The name will be taken as group name when it ends with a colon *:*  Group support is only available in Ansible version 1.6 or later.  If *name=all*, all programs and program groups will be managed. |
| **password**  string | password to use for authentication |
| **server_url**  string | URL on which supervisord server is listening |
| **signal**  string | The signal to send to the program/group, when combined with the ‘signalled’ state. Required when l(state=signalled). |
| **state**  string / required | The desired state of program/group.  Choices:   - `"present"` - `"started"` - `"stopped"` - `"restarted"` - `"absent"` - `"signalled"` |
| **supervisorctl_path**  path | path to supervisorctl executable |
| **username**  string | username to use for authentication |

## [Notes](supervisorctl_module.md#id4)

> **Note:**
>
> - When `state` = *present*, the module will call `supervisorctl reread` then `supervisorctl add` if the program/group does not exist.
> - When `state` = *restarted*, the module will call `supervisorctl update` then call `supervisorctl restart`.
> - When `state` = *absent*, the module will call `supervisorctl reread` then `supervisorctl remove` to remove the target program/group.

## [Examples](supervisorctl_module.md#id5)

```yaml+jinja
- name: Manage the state of program to be in started state
  community.general.supervisorctl:
    name: my_app
    state: started

- name: Manage the state of program group to be in started state
  community.general.supervisorctl:
    name: 'my_apps:'
    state: started

- name: Restart my_app, reading supervisorctl configuration from a specified file
  community.general.supervisorctl:
    name: my_app
    state: restarted
    config: /var/opt/my_project/supervisord.conf

- name: Restart my_app, connecting to supervisord with credentials and server URL
  community.general.supervisorctl:
    name: my_app
    state: restarted
    username: test
    password: testpass
    server_url: http://localhost:9001

- name: Send a signal to my_app via supervisorctl
  community.general.supervisorctl:
    name: my_app
    state: signalled
    signal: USR1

- name: Restart all programs and program groups
  community.general.supervisorctl:
    name: all
    state: restarted
```

### Authors

- Matt Wright (@mattupstate)
- Aaron Wang (@inetfuture)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
