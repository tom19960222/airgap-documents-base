---
collection: ansible
version: "6"
title: "community.network.edgeswitch_vlan module – Manage VLANs on Ubiquiti Edgeswitch network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/edgeswitch_vlan_module.html
fetched_at: 2026-07-27T17:18:27+00:00
---
# community.network.edgeswitch_vlan module – Manage VLANs on Ubiquiti Edgeswitch network devices

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.edgeswitch_vlan`.

- [Synopsis](edgeswitch_vlan_module.md#synopsis)
- [Parameters](edgeswitch_vlan_module.md#parameters)
- [Notes](edgeswitch_vlan_module.md#notes)
- [Examples](edgeswitch_vlan_module.md#examples)
- [Return Values](edgeswitch_vlan_module.md#return-values)

## [Synopsis](edgeswitch_vlan_module.md#id1)

- This module provides declarative management of VLANs on Ubiquiti Edgeswitch network devices.

## [Parameters](edgeswitch_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of VLANs definitions. |
| **auto_exclude**  boolean | Each of the switch interfaces will be excluded from *vlan_id* unless defined in *\*_interfaces*. This is a default setting for all switch interfaces.  Choices:   - `false` - `true` |
| **auto_tag**  boolean | Each of the switch interfaces will be set to accept and transmit untagged frames for *vlan_id* unless defined in *\*_interfaces*. This is a default setting for all switch interfaces.  Choices:   - `false` - `true` |
| **auto_untag**  boolean | Each of the switch interfaces will be set to accept untagged frames and transmit them tagged for *vlan_id* unless defined in *\*_interfaces*. This is a default setting for all switch interfaces.  Choices:   - `false` - `true` |
| **excluded_interfaces**  string | List of interfaces that should be excluded of the VLAN. Accept range of interfaces. |
| **name**  string | Name of the VLAN. |
| **purge**  boolean | Purge VLANs not defined in the *aggregate* parameter.  Choices:   - `false` ← (default) - `true` |
| **state**  string | action on the VLAN configuration.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tagged_interfaces**  string | List of interfaces that should accept and transmit tagged frames for the VLAN. Accept range of interfaces. |
| **untagged_interfaces**  string | List of interfaces that should accept untagged frames and transmit them tagged for the VLAN. Accept range of interfaces. |
| **vlan_id**  string | ID of the VLAN. Range 1-4093. |

## [Notes](edgeswitch_vlan_module.md#id3)

> **Note:**
>
> - Tested against edgeswitch 1.7.4
> - This module use native Ubiquiti vlan syntax and does not support switchport compatibility syntax. For clarity, it is strongly advised to not use both syntaxes on the same interface.
> - Edgeswitch does not support deleting or changing name of VLAN 1
> - As auto_tag, auto_untag and auto_exclude are a kind of default setting for all interfaces, they are mutually exclusive

## [Examples](edgeswitch_vlan_module.md#id4)

```yaml+jinja
- name: Create vlan
  community.network.edgeswitch_vlan:
    vlan_id: 100
    name: voice
    action: present

- name: Add interfaces to VLAN
  community.network.edgeswitch_vlan:
    vlan_id: 100
    tagged_interfaces:
      - 0/1
      - 0/4-0/6

- name: Setup three vlans and delete the rest
  community.network.edgeswitch_vlan:
    purge: true
    aggregate:
      - { vlan_id: 1, name: default, auto_untag: true, excluded_interfaces: 0/45-0/48 }
      - { vlan_id: 100, name: voice, auto_tag: true }
      - { vlan_id: 200, name: video, auto_exclude: true, untagged_interfaces: 0/45-0/48, tagged_interfaces: 0/49 }

- name: Delete vlan
  community.network.edgeswitch_vlan:
    vlan_id: 100
    state: absent
```

## [Return Values](edgeswitch_vlan_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["vlan database", "vlan 100", "vlan name 100 \"test vlan\"", "exit", "interface 0/1", "vlan pvid 50", "vlan participation include 50,100", "vlan tagging 100", "vlan participation exclude 200", "no vlan tagging 200"]` |

### Authors

- Frederic Bor (@f-bor)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
