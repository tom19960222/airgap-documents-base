---
collection: ansible
version: "8"
title: "community.general.cobbler_sync module – Sync Cobbler"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/cobbler_sync_module.html
fetched_at: 2026-07-28T01:45:08+00:00
---
# community.general.cobbler_sync module – Sync Cobbler

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
> To use it in a playbook, specify: `community.general.cobbler_sync`.

- [Synopsis](cobbler_sync_module.md#synopsis)
- [Parameters](cobbler_sync_module.md#parameters)
- [Attributes](cobbler_sync_module.md#attributes)
- [Notes](cobbler_sync_module.md#notes)
- [Examples](cobbler_sync_module.md#examples)

## [Synopsis](cobbler_sync_module.md#id1)

- Sync Cobbler to commit changes.

Aliases: remote_management.cobbler.cobbler_sync

## [Parameters](cobbler_sync_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **host**  string | The name or IP address of the Cobbler system.  **Default:** `"127.0.0.1"` |
| **password**  string | The password to log in to Cobbler. |
| **port**  integer | Port number to be used for REST connection.  The default value depends on parameter `use_ssl`. |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | The username to log in to Cobbler.  **Default:** `"cobbler"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](cobbler_sync_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](cobbler_sync_module.md#id4)

> **Note:**
>
> - Concurrently syncing Cobbler is bound to fail with weird errors.
> - On python 2.7.8 and older (i.e. on RHEL7) you may need to tweak the python behaviour to disable certificate validation. More information at [Certificate verification in Python standard library HTTP clients](https://access.redhat.com/articles/2039753).

## [Examples](cobbler_sync_module.md#id5)

```yaml+jinja
- name: Commit Cobbler changes
  community.general.cobbler_sync:
    host: cobbler01
    username: cobbler
    password: MySuperSecureP4sswOrd
  run_once: true
  delegate_to: localhost
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
