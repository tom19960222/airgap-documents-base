---
collection: ansible
version: "6"
title: "community.network.ce_bgp_af module – Manages BGP Address-family configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_bgp_af_module.html
fetched_at: 2026-07-27T17:17:18+00:00
---
# community.network.ce_bgp_af module – Manages BGP Address-family configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_bgp_af`.

- [Synopsis](ce_bgp_af_module.md#synopsis)
- [Parameters](ce_bgp_af_module.md#parameters)
- [Notes](ce_bgp_af_module.md#notes)
- [Examples](ce_bgp_af_module.md#examples)
- [Return Values](ce_bgp_af_module.md#return-values)

## [Synopsis](ce_bgp_af_module.md#id1)

- Manages BGP Address-family configurations on HUAWEI CloudEngine switches.

## [Parameters](ce_bgp_af_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **active_route_advertise**  string | If the value is true, BGP is enabled to advertise only optimal routes in the RM to peers. If the value is false, BGP is not enabled to advertise only optimal routes in the RM to peers.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **add_path_sel_num**  string | Number of Add-Path routes. The value is an integer ranging from 2 to 64. |
| **af_type**  string / required | Address family type of a BGP instance.  Choices:   - `"ipv4uni"` - `"ipv4multi"` - `"ipv4vpn"` - `"ipv6uni"` - `"ipv6vpn"` - `"evpn"` |
| **allow_invalid_as**  string | Allow routes with BGP origin AS validation result Invalid to be selected. If the value is true, invalid routes can participate in route selection. If the value is false, invalid routes cannot participate in route selection.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **always_compare_med**  string | If the value is true, the MEDs of routes learned from peers in different autonomous systems are compared when BGP selects an optimal route. If the value is false, the MEDs of routes learned from peers in different autonomous systems are not compared when BGP selects an optimal route.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **as_path_neglect**  string | If the value is true, the AS path attribute is ignored when BGP selects an optimal route. If the value is false, the AS path attribute is not ignored when BGP selects an optimal route. An AS path with a smaller length has a higher priority.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **auto_frr_enable**  string | If the value is true, BGP auto FRR is enabled. If the value is false, BGP auto FRR is disabled.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **default_local_pref**  string | Set the Local-Preference attribute. The value is an integer. The value is an integer ranging from 0 to 4294967295. |
| **default_med**  string | Specify the Multi-Exit-Discriminator (MED) of BGP routes. The value is an integer ranging from 0 to 4294967295. |
| **default_rt_import_enable**  string | If the value is true, importing default routes to the BGP routing table is allowed. If the value is false, importing default routes to the BGP routing table is not allowed.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **determin_med**  string | If the value is true, BGP deterministic-MED is enabled. If the value is false, BGP deterministic-MED is disabled.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **ebgp_ecmp_nexthop_changed**  string | If the value is true, the next hop of an advertised route is changed to the advertiser itself in EBGP load-balancing scenarios. If the value is false, the next hop of an advertised route is not changed to the advertiser itself in EBGP load-balancing scenarios.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **ebgp_if_sensitive**  string | If the value is true, after the fast EBGP interface awareness function is enabled, EBGP sessions on an interface are deleted immediately when the interface goes Down. If the value is false, after the fast EBGP interface awareness function is enabled, EBGP sessions on an interface are not deleted immediately when the interface goes Down.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **ecmp_nexthop_changed**  string | If the value is true, the next hop of an advertised route is changed to the advertiser itself in BGP load-balancing scenarios. If the value is false, the next hop of an advertised route is not changed to the advertiser itself in BGP load-balancing scenarios.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **ibgp_ecmp_nexthop_changed**  string | If the value is true, the next hop of an advertised route is changed to the advertiser itself in IBGP load-balancing scenarios. If the value is false, the next hop of an advertised route is not changed to the advertiser itself in IBGP load-balancing scenarios.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **igp_metric_ignore**  string | If the value is true, the metrics of next-hop IGP routes are not compared when BGP selects an optimal route. If the value is false, the metrics of next-hop IGP routes are not compared when BGP selects an optimal route. A route with a smaller metric has a higher priority.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **import_process_id**  string | Process ID of an imported routing protocol. The value is an integer ranging from 0 to 4294967295. |
| **import_protocol**  string | Routing protocol from which routes can be imported.  Choices:   - `"direct"` - `"ospf"` - `"isis"` - `"static"` - `"rip"` - `"ospfv3"` - `"ripng"` |
| **ingress_lsp_policy_name**  string | Ingress lsp policy name. |
| **load_balancing_as_path_ignore**  string | Load balancing as path ignore.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **lowest_priority**  string | If the value is true, enable reduce priority to advertise route. If the value is false, disable reduce priority to advertise route.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **mask_len**  string | Specify the mask length of an IP address. The value is an integer ranging from 0 to 128. |
| **max_load_ebgp_num**  string | Specify the maximum number of equal-cost EBGP routes. The value is an integer ranging from 1 to 65535. |
| **max_load_ibgp_num**  string | Specify the maximum number of equal-cost IBGP routes. The value is an integer ranging from 1 to 65535. |
| **maximum_load_balance**  string | Specify the maximum number of equal-cost routes in the BGP routing table. The value is an integer ranging from 1 to 65535. |
| **med_none_as_maximum**  string | If the value is true, when BGP selects an optimal route, the system uses 4294967295 as the MED value of a route if the route’s attribute does not carry a MED value. If the value is false, the system uses 0 as the MED value of a route if the route’s attribute does not carry a MED value.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **network_address**  string | Specify the IP address advertised by BGP. The value is a string of 0 to 255 characters. |
| **next_hop_sel_depend_type**  string | Next hop select depend type.  Choices:   - `"default"` ← (default) - `"dependTunnel"` - `"dependIp"` |
| **nexthop_third_party**  string | If the value is true, the third-party next hop function is enabled. If the value is false, the third-party next hop function is disabled.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **nhp_relay_route_policy_name**  string | Specify the name of a route-policy for route iteration. The value is a string of 1 to 40 characters. |
| **originator_prior**  string | Originator prior.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **policy_ext_comm_enable**  string | If the value is true, modifying extended community attributes is allowed. If the value is false, modifying extended community attributes is not allowed.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **policy_vpn_target**  string | If the value is true, VPN-Target filtering function is performed for received VPN routes. If the value is false, VPN-Target filtering function is not performed for received VPN routes.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **preference_external**  string | Set the protocol priority of EBGP routes. The value is an integer ranging from 1 to 255. |
| **preference_internal**  string | Set the protocol priority of IBGP routes. The value is an integer ranging from 1 to 255. |
| **preference_local**  string | Set the protocol priority of a local BGP route. The value is an integer ranging from 1 to 255. |
| **prefrence_policy_name**  string | Set a routing policy to filter routes so that a configured priority is applied to the routes that match the specified policy. The value is a string of 1 to 40 characters. |
| **reflect_between_client**  string | If the value is true, route reflection is enabled between clients. If the value is false, route reflection is disabled between clients.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **reflect_chg_path**  string | If the value is true, the route reflector is enabled to modify route path attributes based on an export policy. If the value is false, the route reflector is disabled from modifying route path attributes based on an export policy.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **reflector_cluster_id**  string | Set a cluster ID. Configuring multiple RRs in a cluster can enhance the stability of the network. The value is an integer ranging from 1 to 4294967295. |
| **reflector_cluster_ipv4**  string | Set a cluster ipv4 address. The value is expressed in the format of an IPv4 address. |
| **relay_delay_enable**  string | If the value is true, relay delay enable. If the value is false, relay delay disable.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **rib_only_enable**  string | If the value is true, BGP routes cannot be advertised to the IP routing table. If the value is false, Routes preferred by BGP are advertised to the IP routing table.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **rib_only_policy_name**  string | Specify the name of a routing policy. The value is a string of 1 to 40 characters. |
| **route_sel_delay**  string | Route selection delay. The value is an integer ranging from 0 to 3600. |
| **router_id**  string | ID of a router that is in IPv4 address format. The value is a string of 0 to 255 characters. The value is in dotted decimal notation. |
| **router_id_neglect**  string | If the value is true, the router ID attribute is ignored when BGP selects the optimal route. If the value is false, the router ID attribute is not ignored when BGP selects the optimal route.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **rr_filter_number**  string | Set the number of the extended community filter supported by an RR group. The value is a string of 1 to 51 characters. |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **summary_automatic**  string | If the value is true, automatic aggregation is enabled for locally imported routes. If the value is false, automatic aggregation is disabled for locally imported routes.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **supernet_label_adv**  string | If the value is true, the function to advertise supernetwork label is enabled. If the value is false, the function to advertise supernetwork label is disabled.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **supernet_uni_adv**  string | If the value is true, the function to advertise supernetwork unicast routes is enabled. If the value is false, the function to advertise supernetwork unicast routes is disabled.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **vrf_name**  string / required | Name of a BGP instance. The name is a case-sensitive string of characters. The BGP instance can be used only after the corresponding VPN instance is created. The value is a string of 1 to 31 case-sensitive characters. |
| **vrf_rid_auto_sel**  string | If the value is true, VPN BGP instances are enabled to automatically select router IDs. If the value is false, VPN BGP instances are disabled from automatically selecting router IDs.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |

## [Notes](ce_bgp_af_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_bgp_af_module.md#id4)

```yaml+jinja
- name: CloudEngine BGP address family test
  hosts: cloudengine
  connection: local
  gather_facts: no
  tasks:
  - name: "Config BGP Address_Family"
    community.network.ce_bgp_af:
      state: present
      vrf_name: js
      af_type: ipv4uni
  - name: "Undo BGP Address_Family"
    community.network.ce_bgp_af:
      state: absent
      vrf_name: js
      af_type: ipv4uni
  - name: "Config import route"
    community.network.ce_bgp_af:
      state: present
      vrf_name: js
      af_type: ipv4uni
      import_protocol: ospf
      import_process_id: 123
  - name: "Undo import route"
    community.network.ce_bgp_af:
      state: absent
      vrf_name: js
      af_type: ipv4uni
      import_protocol: ospf
      import_process_id: 123
  - name: "Config network route"
    community.network.ce_bgp_af:
      state: present
      vrf_name: js
      af_type: ipv4uni
      network_address: 1.1.1.1
      mask_len: 24
  - name: "Undo network route"
    community.network.ce_bgp_af:
      state: absent
      vrf_name: js
      af_type: ipv4uni
      network_address: 1.1.1.1
      mask_len: 24
```

## [Return Values](ce_bgp_af_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{"af_type": "ipv4uni", "vrf_name": "js"}` |
| **existing**  dictionary | k/v pairs of existing aaa server  Returned: always  Sample: `{}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"af_type": "ipv4uni", "state": "present", "vrf_name": "js"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["ipv4-family vpn-instance js"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
