---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_pingtrace module – Employ the internal FlashBlade ping and trace mechanisms"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_pingtrace_module.html
fetched_at: 2026-07-28T02:52:10+00:00
---
# purestorage.flashblade.purefb_pingtrace module – Employ the internal FlashBlade ping and trace mechanisms

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
> see [Requirements](purefb_pingtrace_module.md#ansible-collections-purestorage-flashblade-purefb-pingtrace-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_pingtrace`.

New in purestorage.flashblade 1.11.0

- [Synopsis](purefb_pingtrace_module.md#synopsis)
- [Requirements](purefb_pingtrace_module.md#requirements)
- [Parameters](purefb_pingtrace_module.md#parameters)
- [Notes](purefb_pingtrace_module.md#notes)
- [Examples](purefb_pingtrace_module.md#examples)

## [Synopsis](purefb_pingtrace_module.md#id1)

- Ping or trace a destination

## [Requirements](purefb_pingtrace_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_pingtrace_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string | Which action is required, ping or trace  **Choices:**   - `"ping"` ← (default) - `"trace"` |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **component**  string | Used by ping and trace to specify where to run the operation.  Valid values are controllers and blades from hardware list.  If not specified defaults to all available controllers and selected blades |
| **count**  integer | Used by ping to specify the number of packets to send  **Default:** `1` |
| **destination**  string / required | IP addtress or hostname used to run ping or trace against. |
| **discover_mtu**  boolean | Used by trace to specify whether or not to discover the MTU along the path being traced  **Choices:**   - `false` ← (default) - `true` |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **fragment**  boolean | Used by trace to specify whether or not to fragment packets  **Choices:**   - `false` - `true` ← (default) |
| **latency**  boolean | Specify whether or not to print the full user-to-user latency  **Choices:**   - `false` ← (default) - `true` |
| **method**  string | Used by trace to specify the method to use for operations  **Choices:**   - `"icmp"` - `"tcp"` - `"udp"` ← (default) |
| **packet_size**  integer | Used by ping to specify the number of data bytes to send per packet  **Default:** `56` |
| **port**  string | Used by trace to specify a destination port |
| **resolve**  boolean | Specify whether or not to map IP addresses to host names  **Choices:**   - `false` - `true` ← (default) |
| **source**  string | IP address or hostname used by ping and trace to specify where to start to run the specified operation  If not specified will use all available sources |

## [Notes](purefb_pingtrace_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_pingtrace_module.md#id5)

```yaml+jinja
- name: ping Google DNS server
  purestorage.flashblade.purefb_pingtrace:
    destination: 8.8.8.8
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3

- name: trace to Google DNS server from CH1.FM0
  purestorage.flashblade.purefb_pingtrace:
    action: trace
    destination: 8.8.8.8
    fragment_packet: true
    source: CH1.FM0
    discover_mtu: true
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
