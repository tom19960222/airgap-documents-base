---
collection: ansible
version: "6"
title: "community.network.pn_vrouter_bgp module – CLI command to add/modify/remove vrouter-bgp"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_vrouter_bgp_module.html
fetched_at: 2026-07-27T17:19:34+00:00
---
# community.network.pn_vrouter_bgp module – CLI command to add/modify/remove vrouter-bgp

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
> To use it in a playbook, specify: `community.network.pn_vrouter_bgp`.

- [Synopsis](pn_vrouter_bgp_module.md#synopsis)
- [Parameters](pn_vrouter_bgp_module.md#parameters)
- [Examples](pn_vrouter_bgp_module.md#examples)
- [Return Values](pn_vrouter_bgp_module.md#return-values)

## [Synopsis](pn_vrouter_bgp_module.md#id1)

- This module can be used to add Border Gateway Protocol neighbor to a vRouter modify Border Gateway Protocol neighbor to a vRouter and remove Border Gateway Protocol neighbor from a vRouter.

## [Parameters](pn_vrouter_bgp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_advertisement_interval**  string | Minimum interval between sending BGP routing updates. |
| **pn_allowas_in**  boolean | Allow/reject routes with local AS in AS_PATH.  Choices:   - `false` - `true` |
| **pn_bfd**  boolean | BFD protocol support for fault detection.  Choices:   - `false` ← (default) - `true` |
| **pn_bfd_multihop**  boolean | always use BFD multi-hop port for fault detection.  Choices:   - `false` - `true` |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_connect_retry_interval**  string | BGP Connect retry interval (seconds). |
| **pn_default_originate**  boolean | announce default routes to the neighbor or not.  Choices:   - `false` - `true` |
| **pn_ebgp_multihop**  string | value for external BGP from 1 to 255. |
| **pn_interface**  string | Interface to reach the neighbor. |
| **pn_max_prefix**  string | maximum number of prefixes. |
| **pn_max_prefix_warn_only**  boolean | warn if the maximum number of prefixes is exceeded.  Choices:   - `false` - `true` |
| **pn_multi_protocol**  string | Multi-protocol features.  Choices:   - `"ipv4-unicast"` - `"ipv6-unicast"` |
| **pn_neighbor**  string / required | IP address for BGP neighbor. |
| **pn_neighbor_holdtime**  string | BGP Holdtime (seconds). |
| **pn_neighbor_keepalive_interval**  string | BGP Keepalive interval (seconds). |
| **pn_next_hop_self**  boolean | BGP next hop is self or not.  Choices:   - `false` - `true` |
| **pn_no_route_map_in**  string | Remove ingress route-map from BGP neighbor. |
| **pn_no_route_map_out**  string | Remove egress route-map from BGP neighbor. |
| **pn_override_capability**  boolean | override capability.  Choices:   - `false` - `true` |
| **pn_password**  string | password for MD5 BGP. |
| **pn_prefix_list_in**  string | prefixes used for filtering. |
| **pn_prefix_list_out**  string | prefixes used for filtering outgoing packets. |
| **pn_remote_as**  string | BGP remote AS from 1 to 4294967295. |
| **pn_route_map_in**  string | route map in for nbr. |
| **pn_route_map_out**  string | route map out for nbr. |
| **pn_route_reflector_client**  boolean | set as route reflector client.  Choices:   - `false` - `true` |
| **pn_send_community**  boolean | send any community attribute to neighbor.  Choices:   - `false` - `true` |
| **pn_soft_reconfig_inbound**  boolean | soft reset to reconfigure inbound traffic.  Choices:   - `false` - `true` |
| **pn_update_source**  string | IP address of BGP packets required for peering over loopback interface. |
| **pn_vrouter_name**  string / required | name of service config. |
| **pn_weight**  string | default weight value between 0 and 65535 for the neighbor’s routes. |
| **state**  string | vrouter-bgp configuration command.  Choices:   - `"present"` ← (default) - `"absent"` - `"update"` |

## [Examples](pn_vrouter_bgp_module.md#id3)

```yaml+jinja
- name: "Add BGP to vRouter"
  community.network.pn_vrouter_bgp:
    state: 'present'
    pn_vrouter_name: 'sw01-vrouter'
    pn_neighbor: '105.104.104.1'
    pn_remote_as: 65000
    pn_bfd: true

- name: "Remove BGP to vRouter"
  community.network.pn_vrouter_bgp:
    state: 'absent'
    pn_vrouter_name: 'sw01-vrouter'
    pn_neighbor: '105.104.104.1'

- name: "Modify BGP to vRouter"
  community.network.pn_vrouter_bgp:
    state: 'update'
    pn_vrouter_name: 'sw01-vrouter'
    pn_neighbor: '105.104.104.1'
    pn_remote_as: 65000
    pn_bfd: false
    pn_allowas_in: true
```

## [Return Values](pn_vrouter_bgp_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the vrouter-bgp command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the vrouter-bgp command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
