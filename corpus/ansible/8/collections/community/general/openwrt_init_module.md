---
collection: ansible
version: "8"
title: "community.general.openwrt_init module – Manage services on OpenWrt"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/openwrt_init_module.html
fetched_at: 2026-07-28T01:48:43+00:00
---
# community.general.openwrt_init module – Manage services on OpenWrt

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
> see [Requirements](openwrt_init_module.md#ansible-collections-community-general-openwrt-init-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.openwrt_init`.

- [Synopsis](openwrt_init_module.md#synopsis)
- [Requirements](openwrt_init_module.md#requirements)
- [Parameters](openwrt_init_module.md#parameters)
- [Attributes](openwrt_init_module.md#attributes)
- [Notes](openwrt_init_module.md#notes)
- [Examples](openwrt_init_module.md#examples)

## [Synopsis](openwrt_init_module.md#id1)

- Controls OpenWrt services on remote hosts.

Aliases: system.openwrt_init

## [Requirements](openwrt_init_module.md#id2)

The below requirements are needed on the host that executes this module.

- An OpenWrt system (with python)

## [Parameters](openwrt_init_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean | Whether the service should start on boot. **At least one of state and enabled are required.**  **Choices:**   - `false` - `true` |
| **name**  aliases: service  string / required | Name of the service. |
| **pattern**  string | If the service does not respond to the ‘running’ command, name a substring to look for as would be found in the output of the `ps` command as a stand-in for a ‘running’ result. If the string is found, the service will be assumed to be running. |
| **state**  string | `started`/`stopped` are idempotent actions that will not run commands unless necessary.  `restarted` will always bounce the service.  `reloaded` will always reload.  **Choices:**   - `"started"` - `"stopped"` - `"restarted"` - `"reloaded"` |

## [Attributes](openwrt_init_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](openwrt_init_module.md#id5)

> **Note:**
>
> - One option other than name is required.

## [Examples](openwrt_init_module.md#id6)

```yaml+jinja
- name: Start service httpd, if not running
  community.general.openwrt_init:
    state: started
    name: httpd

- name: Stop service cron, if running
  community.general.openwrt_init:
    name: cron
    state: stopped

- name: Reload service httpd, in all cases
  community.general.openwrt_init:
    name: httpd
    state: reloaded

- name: Enable service httpd
  community.general.openwrt_init:
    name: httpd
    enabled: true
```

### Authors

- Andrew Gaffney (@agaffney)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
