---
collection: ansible
version: "8"
title: "community.general.simpleinit_msb module – Manage services on Source Mage GNU/Linux"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/simpleinit_msb_module.html
fetched_at: 2026-07-28T01:50:36+00:00
---
# community.general.simpleinit_msb module – Manage services on Source Mage GNU/Linux

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
> To use it in a playbook, specify: `community.general.simpleinit_msb`.

New in community.general 7.5.0

- [Synopsis](simpleinit_msb_module.md#synopsis)
- [Parameters](simpleinit_msb_module.md#parameters)
- [Attributes](simpleinit_msb_module.md#attributes)
- [Notes](simpleinit_msb_module.md#notes)
- [Examples](simpleinit_msb_module.md#examples)

## [Synopsis](simpleinit_msb_module.md#id1)

- Controls services on remote hosts using `simpleinit-msb`.

## [Parameters](simpleinit_msb_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean | Whether the service should start on boot.  At least one of `state` and `enabled` are required.  **Choices:**   - `false` - `true` |
| **name**  aliases: service  string / required | Name of the service. |
| **state**  string | `started`/`stopped` are idempotent actions that will not run commands unless necessary. `restarted` will always bounce the service. `reloaded` will always reload.  At least one of `state` and `enabled` are required.  Note that `reloaded` will start the service if it is not already started, even if your chosen init system would not normally.  **Choices:**   - `"running"` - `"started"` - `"stopped"` - `"restarted"` - `"reloaded"` |

## [Attributes](simpleinit_msb_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](simpleinit_msb_module.md#id4)

> **Note:**
>
> - This module needs ansible-core 2.15.5 or newer. Older versions have a broken and insufficient daemonize functionality.

## [Examples](simpleinit_msb_module.md#id5)

```yaml+jinja
- name: Example action to start service httpd, if not running
  community.general.simpleinit_msb:
    name: httpd
    state: started

- name: Example action to stop service httpd, if running
  community.general.simpleinit_msb:
    name: httpd
    state: stopped

- name: Example action to restart service httpd, in all cases
  community.general.simpleinit_msb:
    name: httpd
    state: restarted

- name: Example action to reload service httpd, in all cases
  community.general.simpleinit_msb:
    name: httpd
    state: reloaded

- name: Example action to enable service httpd, and not touch the running state
  community.general.simpleinit_msb:
    name: httpd
    enabled: true
```

### Authors

- Vlad Glagolev (@vaygr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
