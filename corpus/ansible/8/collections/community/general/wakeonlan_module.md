---
collection: ansible
version: "8"
title: "community.general.wakeonlan module – Send a magic Wake-on-LAN (WoL) broadcast packet"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/wakeonlan_module.html
fetched_at: 2026-07-28T01:51:22+00:00
---
# community.general.wakeonlan module – Send a magic Wake-on-LAN (WoL) broadcast packet

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
> To use it in a playbook, specify: `community.general.wakeonlan`.

- [Synopsis](wakeonlan_module.md#synopsis)
- [Parameters](wakeonlan_module.md#parameters)
- [Attributes](wakeonlan_module.md#attributes)
- [Notes](wakeonlan_module.md#notes)
- [See Also](wakeonlan_module.md#see-also)
- [Examples](wakeonlan_module.md#examples)

## [Synopsis](wakeonlan_module.md#id1)

- The `wakeonlan` module sends magic Wake-on-LAN (WoL) broadcast packets.

Aliases: remote_management.wakeonlan

## [Parameters](wakeonlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **broadcast**  string | Network broadcast address to use for broadcasting magic Wake-on-LAN packet.  **Default:** `"255.255.255.255"` |
| **mac**  string / required | MAC address to send Wake-on-LAN broadcast packet for. |
| **port**  integer | UDP port to use for magic Wake-on-LAN packet.  **Default:** `7` |

## [Attributes](wakeonlan_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](wakeonlan_module.md#id4)

> **Note:**
>
> - This module sends a magic packet, without knowing whether it worked
> - Only works if the target system was properly configured for Wake-on-LAN (in the BIOS and/or the OS)
> - Some BIOSes have a different (configurable) Wake-on-LAN boot order (i.e. PXE first).

## [See Also](wakeonlan_module.md#id5)

> **See also:**
>
> [community.windows.win_wakeonlan](../windows/win_wakeonlan_module.md#ansible-collections-community-windows-win-wakeonlan-module)
> :   Send a magic Wake-on-LAN (WoL) broadcast packet.

## [Examples](wakeonlan_module.md#id6)

```yaml+jinja
- name: Send a magic Wake-on-LAN packet to 00:00:5E:00:53:66
  community.general.wakeonlan:
    mac: '00:00:5E:00:53:66'
    broadcast: 192.0.2.23
  delegate_to: localhost

- community.general.wakeonlan:
    mac: 00:00:5E:00:53:66
    port: 9
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
