---
collection: ansible
version: "6"
title: "community.network.pn_ipv6security_raguard_vlan module – CLI command to add/remove ipv6security-raguard-vlan"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_ipv6security_raguard_vlan_module.html
fetched_at: 2026-07-27T17:19:24+00:00
---
# community.network.pn_ipv6security_raguard_vlan module – CLI command to add/remove ipv6security-raguard-vlan

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
> To use it in a playbook, specify: `community.network.pn_ipv6security_raguard_vlan`.

- [Synopsis](pn_ipv6security_raguard_vlan_module.md#synopsis)
- [Parameters](pn_ipv6security_raguard_vlan_module.md#parameters)
- [Examples](pn_ipv6security_raguard_vlan_module.md#examples)
- [Return Values](pn_ipv6security_raguard_vlan_module.md#return-values)

## [Synopsis](pn_ipv6security_raguard_vlan_module.md#id1)

- This module can be used to Add vlans to RA Guard Policy and Remove vlans to RA Guard Policy.

## [Parameters](pn_ipv6security_raguard_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_name**  string / required | RA Guard Policy Name. |
| **pn_vlans**  string / required | Vlans attached to RA Guard Policy. |
| **state**  string | ipv6security-raguard-vlan configuration command.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](pn_ipv6security_raguard_vlan_module.md#id3)

```yaml+jinja
- name: Ipv6 security raguard vlan add
  community.network.pn_ipv6security_raguard_vlan:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    pn_vlans: "100-105"

- name: Ipv6 security raguard vlan add
  community.network.pn_ipv6security_raguard_vlan:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    pn_vlans: "100"

- name: Ipv6 security raguard vlan remove
  community.network.pn_ipv6security_raguard_vlan:
    pn_cliswitch: "sw01"
    pn_name: "foo"
    pn_vlans: "100-105"
    state: 'absent'
```

## [Return Values](pn_ipv6security_raguard_vlan_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the ipv6security-raguard-vlan command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the ipv6security-raguard-vlan command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
