---
collection: ansible
version: "6"
title: "community.general.aix_devices module – Manages AIX devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/aix_devices_module.html
fetched_at: 2026-07-27T17:07:59+00:00
---
# community.general.aix_devices module – Manages AIX devices

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
> To use it in a playbook, specify: `community.general.aix_devices`.

- [Synopsis](aix_devices_module.md#synopsis)
- [Parameters](aix_devices_module.md#parameters)
- [Examples](aix_devices_module.md#examples)

## [Synopsis](aix_devices_module.md#id1)

- This module discovers, defines, removes and modifies attributes of AIX devices.

## [Parameters](aix_devices_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | A list of device attributes. |
| **device**  string | The name of the device.  `all` is valid to rescan `available` all devices (AIX cfgmgr command). |
| **force**  boolean | Forces action.  Choices:   - `false` ← (default) - `true` |
| **recursive**  boolean | Removes or defines a device and children devices.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Controls the device state.  `available` (alias `present`) rescan a specific device or all devices (when `device` is not specified).  `removed` (alias `absent` removes a device.  `defined` changes device to Defined state.  Choices:   - `"available"` ← (default) - `"defined"` - `"removed"` |

## [Examples](aix_devices_module.md#id3)

```yaml+jinja
- name: Scan new devices
  community.general.aix_devices:
    device: all
    state: available

- name: Scan new virtual devices (vio0)
  community.general.aix_devices:
    device: vio0
    state: available

- name: Removing IP alias to en0
  community.general.aix_devices:
    device: en0
    attributes:
      delalias4: 10.0.0.100,255.255.255.0

- name: Removes ent2
  community.general.aix_devices:
    device: ent2
    state: removed

- name: Put device en2 in Defined
  community.general.aix_devices:
    device: en2
    state: defined

- name: Removes ent4 (inexistent).
  community.general.aix_devices:
    device: ent4
    state: removed

- name: Put device en4 in Defined (inexistent)
  community.general.aix_devices:
    device: en4
    state: defined

- name: Put vscsi1 and children devices in Defined state.
  community.general.aix_devices:
    device: vscsi1
    recursive: true
    state: defined

- name: Removes vscsi1 and children devices.
  community.general.aix_devices:
    device: vscsi1
    recursive: true
    state: removed

- name: Changes en1 mtu to 9000 and disables arp.
  community.general.aix_devices:
    device: en1
    attributes:
      mtu: 900
      arp: off
    state: available

- name: Configure IP, netmask and set en1 up.
  community.general.aix_devices:
    device: en1
    attributes:
      netaddr: 192.168.0.100
      netmask: 255.255.255.0
      state: up
    state: available

- name: Adding IP alias to en0
  community.general.aix_devices:
    device: en0
    attributes:
      alias4: 10.0.0.100,255.255.255.0
    state: available
```

### Authors

- Kairo Araujo (@kairoaraujo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
