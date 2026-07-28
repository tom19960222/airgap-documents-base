---
collection: ansible
version: "6"
title: "community.windows.win_netbios module – Manage NetBIOS over TCP/IP settings on Windows."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_netbios_module.html
fetched_at: 2026-07-27T17:23:38+00:00
---
# community.windows.win_netbios module – Manage NetBIOS over TCP/IP settings on Windows.

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
> To use it in a playbook, specify: `community.windows.win_netbios`.

- [Synopsis](win_netbios_module.md#synopsis)
- [Parameters](win_netbios_module.md#parameters)
- [Notes](win_netbios_module.md#notes)
- [Examples](win_netbios_module.md#examples)
- [Return Values](win_netbios_module.md#return-values)

## [Synopsis](win_netbios_module.md#id1)

- Enables or disables NetBIOS on Windows network adapters.
- Can be used to protect a system against NBT-NS poisoning and avoid NBNS broadcast storms.
- Settings can be applied system wide or per adapter.

## [Parameters](win_netbios_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adapter_names**  list / elements=string | List of adapter names for which to manage NetBIOS settings. If this option is omitted then configuration is applied to all adapters on the system.  The adapter name used is the connection caption in the Network Control Panel or via `Get-NetAdapter`, eg `Ethernet 2`. |
| **state**  string / required | Whether NetBIOS should be enabled, disabled, or default (use setting from DHCP server or if static IP address is assigned enable NetBIOS).  Choices:   - `"enabled"` - `"disabled"` - `"default"` |

## [Notes](win_netbios_module.md#id3)

> **Note:**
>
> - Changing NetBIOS settings does not usually require a reboot and will take effect immediately.
> - UDP port 137/138/139 will no longer be listening once NetBIOS is disabled.

## [Examples](win_netbios_module.md#id4)

```yaml+jinja
- name: Disable NetBIOS system wide
  community.windows.win_netbios:
    state: disabled

- name: Disable NetBIOS on Ethernet2
  community.windows.win_netbios:
    state: disabled
    adapter_names:
      - Ethernet2

- name: Enable NetBIOS on Public and Backup adapters
  community.windows.win_netbios:
    state: enabled
    adapter_names:
      - Public
      - Backup

- name: Set NetBIOS to system default on all adapters
  community.windows.win_netbios:
    state: default
```

## [Return Values](win_netbios_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **reboot_required**  boolean | Boolean value stating whether a system reboot is required.  Returned: always  Sample: `true` |

### Authors

- Thomas Moore (@tmmruk)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
