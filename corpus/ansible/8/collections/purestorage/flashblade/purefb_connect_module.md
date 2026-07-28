---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_connect module – Manage replication connections between two FlashBlades"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_connect_module.html
fetched_at: 2026-07-28T02:51:53+00:00
---
# purestorage.flashblade.purefb_connect module – Manage replication connections between two FlashBlades

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flashblade/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_connect_module.md#ansible-collections-purestorage-flashblade-purefb-connect-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_connect`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_connect_module.md#synopsis)
- [Requirements](purefb_connect_module.md#requirements)
- [Parameters](purefb_connect_module.md#parameters)
- [Notes](purefb_connect_module.md#notes)
- [Examples](purefb_connect_module.md#examples)

## [Synopsis](purefb_connect_module.md#id1)

- Manage replication connections to specified remote FlashBlade system

## [Requirements](purefb_connect_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_connect_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **default_limit**  string  *added in purestorage.flashblade 1.9.0* | Default maximum bandwidth threshold for outbound traffic in bytes.  B, K, M, or G units. See examples.  Must be 0 or between 5MB and 28GB  Once exceeded, bandwidth throttling occurs |
| **encrypted**  boolean | Define if replication connection is encrypted  **Choices:**   - `false` ← (default) - `true` |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **state**  string | Create or delete replication connection  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **target_api**  string | API token for target FlashBlade system |
| **target_repl**  list / elements=string  *added in purestorage.flashblade 1.9.0* | Replication IP address of target FlashBlade system  If not set at time of connection creation, will default to all the replication addresses available on the target array at the time of connection creation. |
| **target_url**  string / required | Management IP address of target FlashBlade system |
| **window_end**  string  *added in purestorage.flashblade 1.9.0* | The window end time.  The time must be set to the hour. |
| **window_limit**  string  *added in purestorage.flashblade 1.9.0* | Maximum bandwidth threshold for outbound traffic during the specified time range in bytes.  B, K, M, or G units. See examples.  Must be 0 or between 5MB and 28GB  Once exceeded, bandwidth throttling occurs |
| **window_start**  string  *added in purestorage.flashblade 1.9.0* | The window start time.  The time must be set to the hour. |

## [Notes](purefb_connect_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_connect_module.md#id5)

```yaml+jinja
- name: Create a connection to remote FlashBlade system
  purestorage.flashblade.purefb_connect:
    target_url: 10.10.10.20
    target_api: T-b3275b1c-8958-4190-9052-eb46b0bd09f8
    fb_url: 10.10.10.2
    api_token: T-91528421-fe42-47ee-bcb1-47eefb0a9220
- name: Create a connection to remote FlashBlade system with bandwidth limits
  purestorage.flashblade.purefb_connect:
    target_url: 10.10.10.20
    target_api: T-b3275b1c-8958-4190-9052-eb46b0bd09f8
    window_limit: 28G
    window_start: 1AM
    window_end: 7AM
    default_limit: 5M
    fb_url: 10.10.10.2
    api_token: T-91528421-fe42-47ee-bcb1-47eefb0a9220
- name: Delete connection to target FlashBlade system
  purestorage.flashblade.purefb_connect:
    state: absent
    target_url: 10.10.10.20
    target_api: T-b3275b1c-8958-4190-9052-eb46b0bd09f8
    fb_url: 10.10.10.2
    api_token: T-91528421-fe42-47ee-bcb1-47eefb0a9220
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
