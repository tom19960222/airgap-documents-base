---
collection: ansible
version: "6"
title: "community.network.ce_switchport module – Manages Layer 2 switchport interfaces on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_switchport_module.html
fetched_at: 2026-07-27T17:17:55+00:00
---
# community.network.ce_switchport module – Manages Layer 2 switchport interfaces on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_switchport`.

- [Synopsis](ce_switchport_module.md#synopsis)
- [Parameters](ce_switchport_module.md#parameters)
- [Notes](ce_switchport_module.md#notes)
- [Examples](ce_switchport_module.md#examples)
- [Return Values](ce_switchport_module.md#return-values)

## [Synopsis](ce_switchport_module.md#id1)

- Manages Layer 2 switchport interfaces on HUAWEI CloudEngine switches.

## [Parameters](ce_switchport_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **default_vlan**  string | If `mode=access, or mode=dot1qtunnel`, used as the access VLAN ID, in the range from 1 to 4094. |
| **interface**  string / required | Full name of the interface, i.e. 40GE1/0/22. |
| **mode**  string | The link type of an interface.  Choices:   - `"access"` - `"trunk"` - `"hybrid"` - `"dot1qtunnel"` |
| **pvid_vlan**  string | If `mode=trunk, or mode=hybrid`, used as the trunk native VLAN ID, in the range from 1 to 4094. |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` - `"unconfigured"` |
| **tagged_vlans**  string | If `mode=hybrid`, used as the VLAN range to ADD or REMOVE from the trunk, such as 2-10 or 2,5,10-15, etc. |
| **trunk_vlans**  string | If `mode=trunk`, used as the VLAN range to ADD or REMOVE from the trunk, such as 2-10 or 2,5,10-15, etc. |
| **untagged_vlans**  string | If `mode=hybrid`, used as the VLAN range to ADD or REMOVE from the trunk, such as 2-10 or 2,5,10-15, etc. |

## [Notes](ce_switchport_module.md#id3)

> **Note:**
>
> - When `state=absent`, VLANs can be added/removed from trunk links and the existing access VLAN can be ‘unconfigured’ to just having VLAN 1 on that interface.
> - When working with trunks VLANs the keywords add/remove are always sent in the `port trunk allow-pass vlan` command. Use verbose mode to see commands sent.
> - When `state=unconfigured`, the interface will result with having a default Layer 2 interface, i.e. vlan 1 in access mode.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `ansible.netcommon.netconf`.

## [Examples](ce_switchport_module.md#id4)

```yaml+jinja
- name: Switchport module test
  hosts: cloudengine
  gather_facts: no
  vars:
    ansible_user: root
    ansible_password: PASSWORD
    ansible_connection: ansible.netcommon.netconf
    ansible_network_os: community.network.ce

  tasks:
  - name: Ensure 10GE1/0/22 is in its default switchport state
    community.network.ce_switchport:
      interface: 10GE1/0/22
      state: unconfigured

  - name: Ensure 10GE1/0/22 is configured for access vlan 20
    community.network.ce_switchport:
      interface: 10GE1/0/22
      mode: access
      default_vlan: 20

  - name: Ensure 10GE1/0/22 only has vlans 5-10 as trunk vlans
    community.network.ce_switchport:
      interface: 10GE1/0/22
      mode: trunk
      pvid_vlan: 10
      trunk_vlans: 5-10

  - name: Ensure 10GE1/0/22 is a trunk port and ensure 2-50 are being tagged (doesn't mean others aren't also being tagged)
    community.network.ce_switchport:
      interface: 10GE1/0/22
      mode: trunk
      pvid_vlan: 10
      trunk_vlans: 2-50

  - name: Ensure these VLANs are not being tagged on the trunk
    community.network.ce_switchport:
      interface: 10GE1/0/22
      mode: trunk
      trunk_vlans: 51-4000
      state: absent
```

## [Return Values](ce_switchport_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of switchport after module execution  Returned: always  Sample: `{"default_vlan": "20", "interface": "10GE1/0/22", "mode": "access", "switchport": "enable"}` |
| **existing**  dictionary | k/v pairs of existing switchport  Returned: always  Sample: `{"default_vlan": "10", "interface": "10GE1/0/22", "mode": "access", "switchport": "enable"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"default_vlan": "20", "interface": "10GE1/0/22", "mode": "access"}` |
| **updates**  list / elements=string | command string sent to the device  Returned: always  Sample: `["10GE1/0/22", "port default vlan 20"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
