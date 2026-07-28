---
collection: ansible
version: "6"
title: "community.network.pn_igmp_snooping module – CLI command to modify igmp-snooping"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_igmp_snooping_module.html
fetched_at: 2026-07-27T17:19:22+00:00
---
# community.network.pn_igmp_snooping module – CLI command to modify igmp-snooping

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
> To use it in a playbook, specify: `community.network.pn_igmp_snooping`.

- [Synopsis](pn_igmp_snooping_module.md#synopsis)
- [Parameters](pn_igmp_snooping_module.md#parameters)
- [Examples](pn_igmp_snooping_module.md#examples)
- [Return Values](pn_igmp_snooping_module.md#return-values)

## [Synopsis](pn_igmp_snooping_module.md#id1)

- This module can be used to modify Internet Group Management Protocol (IGMP) snooping.

## [Parameters](pn_igmp_snooping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_enable**  boolean | enable or disable IGMP snooping.  Choices:   - `false` - `true` |
| **pn_enable_vlans**  string | enable per VLAN IGMP snooping. |
| **pn_igmpv2_vlans**  string | VLANs on which to use IGMPv2 protocol. |
| **pn_igmpv3_vlans**  string | VLANs on which to use IGMPv3 protocol. |
| **pn_no_snoop_linklocal_vlans**  string | Remove snooping of link-local groups(224.0.0.0/24) on these vlans. |
| **pn_query_interval**  string | IGMP query interval in seconds. |
| **pn_query_max_response_time**  string | maximum response time, in seconds, advertised in IGMP queries. |
| **pn_scope**  string | IGMP snooping scope - fabric or local.  Choices:   - `"local"` - `"fabric"` |
| **pn_snoop_linklocal_vlans**  string | Allow snooping of link-local groups(224.0.0.0/24) on these vlans. |
| **pn_vxlan**  boolean | enable or disable IGMP snooping on vxlans.  Choices:   - `false` - `true` |
| **state**  string / required | State the action to perform. Use `update` to modify the igmp-snooping.  Choices:   - `"update"` |

## [Examples](pn_igmp_snooping_module.md#id3)

```yaml+jinja
- name: 'Modify IGMP Snooping'
  community.network.pn_igmp_snooping:
    pn_cliswitch: 'sw01'
    state: 'update'
    pn_vxlan: True
    pn_enable_vlans: '1-399,401-4092'
    pn_no_snoop_linklocal_vlans: 'none'
    pn_igmpv3_vlans: '1-399,401-4092'

- name: 'Modify IGMP Snooping'
  community.network.pn_igmp_snooping:
    pn_cliswitch: 'sw01'
    state: 'update'
    pn_vxlan: False
    pn_enable_vlans: '1-399'
    pn_no_snoop_linklocal_vlans: 'none'
    pn_igmpv3_vlans: '1-399'
```

## [Return Values](pn_igmp_snooping_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the igmp-snooping command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the igmp-snooping command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
