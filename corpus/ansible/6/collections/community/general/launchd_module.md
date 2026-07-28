---
collection: ansible
version: "6"
title: "community.general.launchd module – Manage macOS services"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/launchd_module.html
fetched_at: 2026-07-27T17:10:26+00:00
---
# community.general.launchd module – Manage macOS services

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
> see [Requirements](launchd_module.md#ansible-collections-community-general-launchd-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.launchd`.

New in community.general 1.0.0

- [Synopsis](launchd_module.md#synopsis)
- [Requirements](launchd_module.md#requirements)
- [Parameters](launchd_module.md#parameters)
- [Notes](launchd_module.md#notes)
- [Examples](launchd_module.md#examples)
- [Return Values](launchd_module.md#return-values)

## [Synopsis](launchd_module.md#id1)

- Manage launchd services on target macOS hosts.

## [Requirements](launchd_module.md#id2)

The below requirements are needed on the host that executes this module.

- A system managed by launchd
- The plistlib python library

## [Parameters](launchd_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean | Whether the service should start on boot.  **At least one of state and enabled are required.**  Choices:   - `false` - `true` |
| **force_stop**  boolean | Whether the service should not be restarted automatically by launchd.  Services might have the ‘KeepAlive’ attribute set to true in a launchd configuration. In case this is set to true, stopping a service will cause that launchd starts the service again.  Set this option to `true` to let this module change the ‘KeepAlive’ attribute to false.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Name of the service. |
| **state**  string | `started`/`stopped` are idempotent actions that will not run commands unless necessary.  Launchd does not support `restarted` nor `reloaded` natively. These will trigger a stop/start (restarted) or an unload/load (reloaded).  `restarted` unloads and loads the service before start to ensure that the latest job definition (plist) is used.  `reloaded` unloads and loads the service to ensure that the latest job definition (plist) is used. Whether a service is started or stopped depends on the content of the definition file.  Choices:   - `"reloaded"` - `"restarted"` - `"started"` - `"stopped"` - `"unloaded"` |

## [Notes](launchd_module.md#id4)

> **Note:**
>
> - A user must privileged to manage services using this module.

## [Examples](launchd_module.md#id5)

```yaml+jinja
- name: Make sure spotify webhelper is started
  community.general.launchd:
    name: com.spotify.webhelper
    state: started

- name: Deploy custom memcached job definition
  template:
    src: org.memcached.plist.j2
    dest: /Library/LaunchDaemons/org.memcached.plist

- name: Run memcached
  community.general.launchd:
    name: org.memcached
    state: started

- name: Stop memcached
  community.general.launchd:
    name: org.memcached
    state: stopped

- name: Stop memcached
  community.general.launchd:
    name: org.memcached
    state: stopped
    force_stop: true

- name: Restart memcached
  community.general.launchd:
    name: org.memcached
    state: restarted

- name: Unload memcached
  community.general.launchd:
    name: org.memcached
    state: unloaded
```

## [Return Values](launchd_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **status**  dictionary | Metadata about service status  Returned: always  Sample: `{"current_pid": "-", "current_state": "stopped", "previous_pid": "82636", "previous_state": "running"}` |

### Authors

- Martin Migasiewicz (@martinm82)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
