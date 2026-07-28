---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_facts module – Collects facts on devices running Enterprise SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_facts_module.html
fetched_at: 2026-07-28T02:03:36+00:00
---
# dellemc.enterprise_sonic.sonic_facts module – Collects facts on devices running Enterprise SONiC

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_facts`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_facts_module.md#synopsis)
- [Parameters](sonic_facts_module.md#parameters)
- [Notes](sonic_facts_module.md#notes)
- [Examples](sonic_facts_module.md#examples)

## [Synopsis](sonic_facts_module.md#id1)

- Collects facts from devices running Enterprise SONiC Distribution by Dell Technologies. This module places the facts gathered in the fact tree keyed by the respective resource name. The facts module always collects a base set of facts from the device and can enable or disable collection of additional facts.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_network_resources**  list / elements=string | When supplied, this argument restricts the facts collected to a given subset. Possible values for this argument include all and the resources like ‘all’, ‘interfaces’, ‘vlans’, ‘lag_interfaces’, ‘l2_interfaces’, ‘l3_interfaces’. Can specify a list of values to include a larger subset. Values can also be used with an initial ‘!’ to specify that a specific subset should not be collected.  **Choices:**   - `"all"` - `"vlans"` - `"interfaces"` - `"l2_interfaces"` - `"l3_interfaces"` - `"lag_interfaces"` - `"bgp"` - `"bgp_af"` - `"bgp_neighbors"` - `"bgp_neighbors_af"` - `"bgp_as_paths"` - `"bgp_communities"` - `"bgp_ext_communities"` - `"mclag"` - `"prefix_lists"` - `"vlan_mapping"` - `"vrfs"` - `"vxlans"` - `"users"` - `"system"` - `"port_breakout"` - `"aaa"` - `"tacacs_server"` - `"radius_server"` - `"static_routes"` - `"ntp"` - `"logging"` - `"ip_neighbor"` - `"port_group"` - `"dhcp_relay"` - `"acl_interfaces"` - `"l2_acls"` - `"l3_acls"` - `"lldp_global"` - `"mac"` - `"bfd"` - `"copp"` - `"route_maps"` |
| **gather_subset**  list / elements=string | When supplied, this argument restricts the facts collected to a given subset. Possible values for this argument include all, min, hardware, config, legacy, and interfaces. Can specify a list of values to include a larger subset. Values can also be used with an initial ‘!’ to specify that a specific subset should not be collected.  **Default:** `["!config"]` |

## [Notes](sonic_facts_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_facts_module.md#id4)

```yaml+jinja
- name: Gather all facts
  dellemc.enterprise_sonic.sonic_facts:
    gather_subset: all
    gather_network_resources: all
- name: Collects VLAN and interfaces facts
  dellemc.enterprise_sonic.sonic_facts:
    gather_subset:
      - min
    gather_network_resources:
      - vlans
      - interfaces
- name: Do not collects VLAN and interfaces facts
  dellemc.enterprise_sonic.sonic_facts:
    gather_network_resources:
      - "!vlans"
      - "!interfaces"
- name: Collects VLAN and minimal default facts
  dellemc.enterprise_sonic.sonic_facts:
    gather_subset: min
    gather_network_resources: vlans
- name: Collect lag_interfaces and minimal default facts
  dellemc.enterprise_sonic.sonic_facts:
    gather_subset: min
    gather_network_resources: lag_interfaces
```

### Authors

- Mohamed Javeed (@javeedf)
- Abirami N (@abirami-n)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
