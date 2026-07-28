---
collection: ansible
version: "6"
title: "community.general.wakeonlan module – Send a magic Wake-on-LAN (WoL) broadcast packet"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/wakeonlan_module.html
fetched_at: 2026-07-27T17:13:57+00:00
---
# community.general.wakeonlan module – Send a magic Wake-on-LAN (WoL) broadcast packet

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
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
- [Notes](wakeonlan_module.md#notes)
- [See Also](wakeonlan_module.md#see-also)
- [Examples](wakeonlan_module.md#examples)

## [Synopsis](wakeonlan_module.md#id1)

- The `wakeonlan` module sends magic Wake-on-LAN (WoL) broadcast packets.

## [Parameters](wakeonlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **broadcast**  string | Network broadcast address to use for broadcasting magic Wake-on-LAN packet.  Default: `"255.255.255.255"` |
| **mac**  string / required | MAC address to send Wake-on-LAN broadcast packet for. |
| **port**  integer | UDP port to use for magic Wake-on-LAN packet.  Default: `7` |

## [Notes](wakeonlan_module.md#id3)

> **Note:**
>
> - This module sends a magic packet, without knowing whether it worked
> - Only works if the target system was properly configured for Wake-on-LAN (in the BIOS and/or the OS)
> - Some BIOSes have a different (configurable) Wake-on-LAN boot order (i.e. PXE first).

## [See Also](wakeonlan_module.md#id4)

> **See also:**
>
> [community.windows.win_wakeonlan](../windows/win_wakeonlan_module.md#ansible-collections-community-windows-win-wakeonlan-module)
> :   Send a magic Wake-on-LAN (WoL) broadcast packet.

## [Examples](wakeonlan_module.md#id5)

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

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
