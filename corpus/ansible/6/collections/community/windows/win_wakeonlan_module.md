---
collection: ansible
version: "6"
title: "community.windows.win_wakeonlan module – Send a magic Wake-on-LAN (WoL) broadcast packet"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_wakeonlan_module.html
fetched_at: 2026-07-27T17:24:03+00:00
---
# community.windows.win_wakeonlan module – Send a magic Wake-on-LAN (WoL) broadcast packet

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_wakeonlan`.

- [Synopsis](win_wakeonlan_module.md#synopsis)
- [Parameters](win_wakeonlan_module.md#parameters)
- [Notes](win_wakeonlan_module.md#notes)
- [See Also](win_wakeonlan_module.md#see-also)
- [Examples](win_wakeonlan_module.md#examples)

## [Synopsis](win_wakeonlan_module.md#id1)

- The `win_wakeonlan` module sends magic Wake-on-LAN (WoL) broadcast packets.
- For non-Windows targets, use the [community.general.wakeonlan](../general/wakeonlan_module.md#ansible-collections-community-general-wakeonlan-module) module instead.

## [Parameters](win_wakeonlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **broadcast**  string | Network broadcast address to use for broadcasting magic Wake-on-LAN packet.  Default: `"255.255.255.255"` |
| **mac**  string / required | MAC address to send Wake-on-LAN broadcast packet for. |
| **port**  integer | UDP port to use for magic Wake-on-LAN packet.  Default: `7` |

## [Notes](win_wakeonlan_module.md#id3)

> **Note:**
>
> - This module sends a magic packet, without knowing whether it worked. It always report a change.
> - Only works if the target system was properly configured for Wake-on-LAN (in the BIOS and/or the OS).
> - Some BIOSes have a different (configurable) Wake-on-LAN boot order (i.e. PXE first).

## [See Also](win_wakeonlan_module.md#id4)

> **See also:**
>
> [community.general.wakeonlan](../general/wakeonlan_module.md#ansible-collections-community-general-wakeonlan-module)
> :   Send a magic Wake-on-LAN (WoL) broadcast packet.

## [Examples](win_wakeonlan_module.md#id5)

```yaml+jinja
- name: Send a magic Wake-on-LAN packet to 00:00:5E:00:53:66
  community.windows.win_wakeonlan:
    mac: 00:00:5E:00:53:66
    broadcast: 192.0.2.23

- name: Send a magic Wake-On-LAN packet on port 9 to 00-00-5E-00-53-66
  community.windows.win_wakeonlan:
    mac: 00-00-5E-00-53-66
    port: 9
  delegate_to: remote_system
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
