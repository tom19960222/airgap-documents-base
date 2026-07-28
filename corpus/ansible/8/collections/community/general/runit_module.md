---
collection: ansible
version: "8"
title: "community.general.runit module – Manage runit services"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/runit_module.html
fetched_at: 2026-07-28T01:50:06+00:00
---
# community.general.runit module – Manage runit services

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
> To use it in a playbook, specify: `community.general.runit`.

- [Synopsis](runit_module.md#synopsis)
- [Parameters](runit_module.md#parameters)
- [Attributes](runit_module.md#attributes)
- [Examples](runit_module.md#examples)

## [Synopsis](runit_module.md#id1)

- Controls runit services on remote hosts using the sv utility.

Aliases: system.runit

## [Parameters](runit_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean | Whether the service is enabled or not, if disabled it also implies stopped.  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the service to manage. |
| **service_dir**  string | directory runsv watches for services  **Default:** `"/var/service"` |
| **service_src**  string | directory where services are defined, the source of symlinks to service_dir.  **Default:** `"/etc/sv"` |
| **state**  string | `started`/`stopped` are idempotent actions that will not run commands unless necessary. `restarted` will always bounce the service (sv restart) and `killed` will always bounce the service (sv force-stop). `reloaded` will send a HUP (sv reload). `once` will run a normally downed sv once (sv once), not really an idempotent operation.  **Choices:**   - `"killed"` - `"once"` - `"reloaded"` - `"restarted"` - `"started"` - `"stopped"` |

## [Attributes](runit_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](runit_module.md#id4)

```yaml+jinja
- name: Start sv dnscache, if not running
  community.general.runit:
    name: dnscache
    state: started

- name: Stop sv dnscache, if running
  community.general.runit:
    name: dnscache
    state: stopped

- name: Kill sv dnscache, in all cases
  community.general.runit:
    name: dnscache
    state: killed

- name: Restart sv dnscache, in all cases
  community.general.runit:
    name: dnscache
    state: restarted

- name: Reload sv dnscache, in all cases
  community.general.runit:
    name: dnscache
    state: reloaded

- name: Use alternative sv directory location
  community.general.runit:
    name: dnscache
    state: reloaded
    service_dir: /run/service
```

### Authors

- James Sumners (@jsumners)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
