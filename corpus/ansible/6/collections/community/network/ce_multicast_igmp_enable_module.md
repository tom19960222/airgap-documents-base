---
collection: ansible
version: "6"
title: "community.network.ce_multicast_igmp_enable module – Manages multicast igmp enable configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_multicast_igmp_enable_module.html
fetched_at: 2026-07-27T17:17:40+00:00
---
# community.network.ce_multicast_igmp_enable module – Manages multicast igmp enable configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_multicast_igmp_enable`.

New in community.network 0.2.0

- [Synopsis](ce_multicast_igmp_enable_module.md#synopsis)
- [Parameters](ce_multicast_igmp_enable_module.md#parameters)
- [Notes](ce_multicast_igmp_enable_module.md#notes)
- [Examples](ce_multicast_igmp_enable_module.md#examples)
- [Return Values](ce_multicast_igmp_enable_module.md#return-values)

## [Synopsis](ce_multicast_igmp_enable_module.md#id1)

- Manages multicast igmp on HUAWEI CloudEngine switches.

## [Parameters](ce_multicast_igmp_enable_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aftype**  string / required | Destination ip address family type of static route.  Choices:   - `"v4"` - `"v6"` |
| **features**  string / required | Distinguish between Globally Enabled IGMP or  Enabled IGMP under vlanID.  Choices:   - `"global"` - `"vlan"` |
| **igmp**  boolean | Enable Layer 2 multicast Snooping in a VLAN.  Choices:   - `false` ← (default) - `true` |
| **proxy**  boolean | Layer 2 multicast snooping proxy is enabled.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **version**  integer | Specifies the IGMP version that can be processed.  Default: `2` |
| **vlan_id**  integer | Virtual LAN identity. |

## [Notes](ce_multicast_igmp_enable_module.md#id3)

> **Note:**
>
> - If no vrf is supplied, vrf is set to default. If *state=absent*, the route will be removed, regardless of the non-required parameters.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - This module works with connection `netconf`.

## [Examples](ce_multicast_igmp_enable_module.md#id4)

```yaml+jinja
- name: Configure global igmp enable
  community.network.ce_multicast_igmp_enable:
    aftype: v4
    features: 'global'
    state: present

- name: Configure global igmp disable
  community.network.ce_multicast_igmp_enable:
    features: 'global'
    aftype: v4
    state: absent

- name: Configure vlan igmp enable
  community.network.ce_multicast_igmp_enable:
    features: 'vlan'
    aftype: v4
    vlan_id: 1
    igmp: true

- name: New proxy,igmp,version
  community.network.ce_multicast_igmp_enable:
    features: 'vlan'
    aftype: v4
    vlan_id: 1
    proxy: true
    igmp: true
    version: 1

- name: Modify proxy,igmp,version
  community.network.ce_multicast_igmp_enable:
    features: 'vlan'
    aftype: v4
    vlan_id: 1
    version: 2

- name: Delete proxy,igmp,version
  community.network.ce_multicast_igmp_enable:
    features: 'vlan'
    aftype: v4
    vlan_id: 1
    state: absent
```

## [Return Values](ce_multicast_igmp_enable_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of switchport after module execution  Returned: always  Sample: `{}` |
| **existing**  dictionary | k/v pairs of existing switchport  Returned: always  Sample: `{}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"addrFamily": "ipv4unicast", "features": "vlan", "proxyEnable": "false", "snoopingEnable": "false", "state": "absent", "version": 2, "vlanId": 1}` |
| **updates**  list / elements=string | command list sent to the device  Returned: always  Sample: `["undo igmp snooping enable", "undo igmp snooping version", "undo igmp snooping proxy"]` |

### Authors

- xuxiaowei0512 (@CloudEngine-Ansible)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
