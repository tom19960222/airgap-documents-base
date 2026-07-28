---
collection: ansible
version: "8"
title: "community.network.dladm_vnic module – Manage VNICs on Solaris/illumos systems."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/dladm_vnic_module.html
fetched_at: 2026-07-28T01:56:27+00:00
---
# community.network.dladm_vnic module – Manage VNICs on Solaris/illumos systems.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.dladm_vnic`.

- [Synopsis](dladm_vnic_module.md#synopsis)
- [Parameters](dladm_vnic_module.md#parameters)
- [Examples](dladm_vnic_module.md#examples)
- [Return Values](dladm_vnic_module.md#return-values)

## [Synopsis](dladm_vnic_module.md#id1)

- Create or delete VNICs on Solaris/illumos systems.

Aliases: network.illumos.dladm_vnic

## [Parameters](dladm_vnic_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **link**  string / required | VNIC underlying link name. |
| **mac**  aliases: macaddr  string | Sets the VNIC’s MAC address. Must be valid unicast MAC address. |
| **name**  string / required | VNIC name. |
| **state**  string | Create or delete Solaris/illumos VNIC.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **temporary**  boolean | Specifies that the VNIC is temporary. Temporary VNICs do not persist across reboots.  **Choices:**   - `false` ← (default) - `true` |
| **vlan**  aliases: vlan_id  integer | Enable VLAN tagging for this VNIC. The VLAN tag will have id *vlan*.  **Default:** `false` |

## [Examples](dladm_vnic_module.md#id3)

```yaml+jinja
- name: Create 'vnic0' VNIC over 'bnx0' link
  community.network.dladm_vnic:
    name: vnic0
    link: bnx0
    state: present

- name: Create VNIC with specified MAC and VLAN tag over 'aggr0'
  community.network.dladm_vnic:
    name: vnic1
    link: aggr0
    mac: '00:00:5E:00:53:23'
    vlan: 4

- name: Remove 'vnic0' VNIC
  community.network.dladm_vnic:
    name: vnic0
    link: bnx0
    state: absent
```

## [Return Values](dladm_vnic_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **link**  string | VNIC underlying link name  **Returned:** always  **Sample:** `"igb0"` |
| **mac**  string | MAC address to use for VNIC  **Returned:** if mac is specified  **Sample:** `"00:00:5E:00:53:42"` |
| **name**  string | VNIC name  **Returned:** always  **Sample:** `"vnic0"` |
| **state**  string | state of the target  **Returned:** always  **Sample:** `"present"` |
| **temporary**  boolean | VNIC’s persistence  **Returned:** always  **Sample:** `true` |
| **vlan**  integer | VLAN to use for VNIC  **Returned:** success  **Sample:** `42` |

### Authors

- Adam Števko (@xen0l)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
