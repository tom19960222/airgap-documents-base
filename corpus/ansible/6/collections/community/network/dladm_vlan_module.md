---
collection: ansible
version: "6"
title: "community.network.dladm_vlan module – Manage VLAN interfaces on Solaris/illumos systems."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/dladm_vlan_module.html
fetched_at: 2026-07-27T17:18:23+00:00
---
# community.network.dladm_vlan module – Manage VLAN interfaces on Solaris/illumos systems.

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
> To use it in a playbook, specify: `community.network.dladm_vlan`.

- [Synopsis](dladm_vlan_module.md#synopsis)
- [Parameters](dladm_vlan_module.md#parameters)
- [Examples](dladm_vlan_module.md#examples)
- [Return Values](dladm_vlan_module.md#return-values)

## [Synopsis](dladm_vlan_module.md#id1)

- Create or delete VLAN interfaces on Solaris/illumos systems.

## [Parameters](dladm_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **link**  string / required | VLAN underlying link name. |
| **name**  string / required | VLAN interface name. |
| **state**  string | Create or delete Solaris/illumos VNIC.  Choices:   - `"present"` ← (default) - `"absent"` |
| **temporary**  boolean | Specifies that the VLAN interface is temporary. Temporary VLANs do not persist across reboots.  Choices:   - `false` ← (default) - `true` |
| **vlan_id**  aliases: vid  string | VLAN ID value for VLAN interface.  Default: `false` |

## [Examples](dladm_vlan_module.md#id3)

```yaml+jinja
- name: Create 'vlan42' VLAN over 'bnx0' link
  community.network.dladm_vlan: name=vlan42 link=bnx0 vlan_id=42 state=present

- name: Remove 'vlan1337' VLAN interface
  community.network.dladm_vlan: name=vlan1337 state=absent
```

## [Return Values](dladm_vlan_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **link**  string | VLAN’s underlying link name  Returned: always  Sample: `"e100g0"` |
| **name**  string | VLAN name  Returned: always  Sample: `"vlan42"` |
| **state**  string | state of the target  Returned: always  Sample: `"present"` |
| **temporary**  boolean | specifies if operation will persist across reboots  Returned: always  Sample: `true` |
| **vlan_id**  string | VLAN ID  Returned: always  Sample: `"42"` |

### Authors

- Adam Števko (@xen0l)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
