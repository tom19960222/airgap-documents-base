---
collection: ansible
version: "8"
title: "community.network.ce_bgp_neighbor_af module – Manages BGP neighbor Address-family configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_bgp_neighbor_af_module.html
fetched_at: 2026-07-28T01:55:18+00:00
---
# community.network.ce_bgp_neighbor_af module – Manages BGP neighbor Address-family configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_bgp_neighbor_af`.

- [Synopsis](ce_bgp_neighbor_af_module.md#synopsis)
- [Parameters](ce_bgp_neighbor_af_module.md#parameters)
- [Notes](ce_bgp_neighbor_af_module.md#notes)
- [Examples](ce_bgp_neighbor_af_module.md#examples)
- [Return Values](ce_bgp_neighbor_af_module.md#return-values)

## [Synopsis](ce_bgp_neighbor_af_module.md#id1)

- Manages BGP neighbor Address-family configurations on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_bgp_neighbor_af

## [Parameters](ce_bgp_neighbor_af_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **add_path_mode**  string | null, Null. receive, Support receiving Add-Path routes. send, Support sending Add-Path routes. both, Support receiving and sending Add-Path routes.  **Choices:**   - `"null"` - `"receive"` - `"send"` - `"both"` |
| **adv_add_path_num**  string | The number of addPath advertise route. The value is an integer ranging from 2 to 64. |
| **advertise_arp**  string | If the value is true, advertised ARP routes are distinguished. If the value is false, advertised ARP routes are not distinguished.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **advertise_community**  string | If the value is true, the community attribute is advertised to peers. If the value is false, the community attribute is not advertised to peers.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **advertise_ext_community**  string | If the value is true, the extended community attribute is advertised to peers. If the value is false, the extended community attribute is not advertised to peers.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **advertise_irb**  string | If the value is true, advertised IRB routes are distinguished. If the value is false, advertised IRB routes are not distinguished.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **advertise_remote_nexthop**  string | If the value is true, the remote next-hop attribute is advertised to peers. If the value is false, the remote next-hop attribute is not advertised to any peers.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **af_type**  string / required | Address family type of a BGP instance.  **Choices:**   - `"ipv4uni"` - `"ipv4multi"` - `"ipv4vpn"` - `"ipv6uni"` - `"ipv6vpn"` - `"evpn"` |
| **allow_as_loop_enable**  string | If the value is true, repetitive local AS numbers are allowed. If the value is false, repetitive local AS numbers are not allowed.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **allow_as_loop_limit**  string | Set the maximum number of repetitive local AS number. The value is an integer ranging from 1 to 10. |
| **default_rt_adv_enable**  string | If the value is true, the function to advertise default routes to peers is enabled. If the value is false, the function to advertise default routes to peers is disabled.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **default_rt_adv_policy**  string | Specify the name of a used policy. The value is a string. The value is a string of 1 to 40 characters. |
| **default_rt_match_mode**  string | null, Null. matchall, Advertise the default route if all matching conditions are met. matchany, Advertise the default route if any matching condition is met.  **Choices:**   - `"null"` - `"matchall"` - `"matchany"` |
| **discard_ext_community**  string | If the value is true, the extended community attribute in the peer route information is discarded. If the value is false, the extended community attribute in the peer route information is not discarded.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **export_acl_name_or_num**  string | Apply an IPv4 ACL-based filtering policy to the routes to be advertised to a specified peer. The value is a string of 1 to 32 characters. |
| **export_as_path_filter**  string | Apply an AS_Path-based filtering policy to the routes to be advertised to a specified peer. The value is an integer ranging from 1 to 256. |
| **export_as_path_name_or_num**  string | Application of a AS path list based filtering policy to the routing of a specified peer. |
| **export_pref_filt_name**  string | Specify the IPv4 filtering policy applied to the routes to be advertised to a specified peer. The value is a string of 1 to 169 characters. |
| **export_rt_policy_name**  string | Specify the filtering policy applied to the routes to be advertised to a peer. The value is a string of 1 to 40 characters. |
| **import_acl_name_or_num**  string | Apply an IPv4 ACL-based filtering policy to the routes received from a specified peer. The value is a string of 1 to 32 characters. |
| **import_as_path_filter**  string | Apply an AS_Path-based filtering policy to the routes received from a specified peer. The value is an integer ranging from 1 to 256. |
| **import_as_path_name_or_num**  string | A routing strategy based on the AS path list for routing received by a designated peer. |
| **import_pref_filt_name**  string | Specify the IPv4 filtering policy applied to the routes received from a specified peer. The value is a string of 1 to 169 characters. |
| **import_rt_policy_name**  string | Specify the filtering policy applied to the routes learned from a peer. The value is a string of 1 to 40 characters. |
| **ipprefix_orf_enable**  string | If the value is true, the address prefix-based Outbound Route Filter (ORF) capability is enabled for peers. If the value is false, the address prefix-based Outbound Route Filter (ORF) capability is disabled for peers.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **is_nonstd_ipprefix_mod**  string | If the value is true, Non-standard capability codes are used during capability negotiation. If the value is false, RFC-defined standard ORF capability codes are used during capability negotiation.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **keep_all_routes**  string | If the value is true, the system stores all route update messages received from all peers (groups) after BGP connection setup. If the value is false, the system stores only BGP update messages that are received from peers and pass the configured import policy.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **nexthop_configure**  string | null, The next hop is not changed. local, The next hop is changed to the local IP address. invariable, Prevent the device from changing the next hop of each imported IGP route when advertising it to its BGP peers.  **Choices:**   - `"null"` - `"local"` - `"invariable"` |
| **orf_mode**  string | ORF mode. null, Default value. receive, ORF for incoming packets. send, ORF for outgoing packets. both, ORF for incoming and outgoing packets.  **Choices:**   - `"null"` - `"receive"` - `"send"` - `"both"` |
| **orftype**  string | ORF Type. The value is an integer ranging from 0 to 65535. |
| **origin_as_valid**  string | If the value is true, Application results of route announcement. If the value is false, Routing application results are not notified.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **preferred_value**  string | Assign a preferred value for the routes learned from a specified peer. The value is an integer ranging from 0 to 65535. |
| **public_as_only**  string | If the value is true, sent BGP update messages carry only the public AS number but do not carry private AS numbers. If the value is false, sent BGP update messages can carry private AS numbers.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **public_as_only_force**  string | If the value is true, sent BGP update messages carry only the public AS number but do not carry private AS numbers. If the value is false, sent BGP update messages can carry private AS numbers.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **public_as_only_limited**  string | Limited use public as number.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **public_as_only_replace**  string | Private as replaced by public as number.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **public_as_only_skip_peer_as**  string | Public as only skip peer as.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **redirect_ip**  string | Redirect ip.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **redirect_ip_validation**  aliases: redirect_ip_vaildation  string | Redirect ip validation.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **reflect_client**  string | If the value is true, the local device functions as the route reflector and a peer functions as a client of the route reflector. If the value is false, the route reflector and client functions are not configured.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **remote_address**  string / required | IPv4 or IPv6 peer connection address. |
| **route_limit**  string | Configure the maximum number of routes that can be accepted from a peer. The value is an integer ranging from 1 to 4294967295. |
| **route_limit_idle_timeout**  string | Specify the value of the idle-timeout timer to automatically reestablish the connections after they are cut off when the number of routes exceeds the set threshold. The value is an integer ranging from 1 to 1200. |
| **route_limit_percent**  string | Specify the percentage of routes when a router starts to generate an alarm. The value is an integer ranging from 1 to 100. |
| **route_limit_type**  string | Noparameter, After the number of received routes exceeds the threshold and the timeout timer expires,no action. AlertOnly, An alarm is generated and no additional routes will be accepted if the maximum number of routes allowed have been received. IdleForever, The connection that is interrupted is not automatically re-established if the maximum number of routes allowed have been received. IdleTimeout, After the number of received routes exceeds the threshold and the timeout timer expires, the connection that is interrupted is automatically re-established.  **Choices:**   - `"noparameter"` - `"alertOnly"` - `"idleForever"` - `"idleTimeout"` |
| **rt_updt_interval**  string | Specify the minimum interval at which Update packets are sent. The value is an integer, in seconds. The value is an integer ranging from 0 to 600. |
| **soostring**  string | Configure the Site-of-Origin (SoO) extended community attribute. The value is a string of 3 to 21 characters. |
| **substitute_as_enable**  string | If the value is true, the function to replace a specified peer’s AS number in the AS-Path attribute with the local AS number is enabled. If the value is false, the function to replace a specified peer’s AS number in the AS-Path attribute with the local AS number is disabled.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **update_pkt_standard_compatible**  string | If the value is true, When the vpnv4 multicast neighbor receives and updates the message, the message has no label. If the value is false, When the vpnv4 multicast neighbor receives and updates the message, the message has label.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **vpls_ad_disable**  string | If the value is true, enable vpls-ad. If the value is false, disable vpls-ad.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **vpls_enable**  string | If the value is true, vpls enable. If the value is false, vpls disable.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **vrf_name**  string / required | Name of a BGP instance. The name is a case-sensitive string of characters. The BGP instance can be used only after the corresponding VPN instance is created. |

## [Notes](ce_bgp_neighbor_af_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_bgp_neighbor_af_module.md#id4)

```yaml+jinja
- name: CloudEngine BGP neighbor address family test
  hosts: cloudengine
  connection: local
  gather_facts: false
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: "Config BGP peer Address_Family"
    community.network.ce_bgp_neighbor_af:
      state: present
      vrf_name: js
      af_type: ipv4uni
      remote_address: 192.168.10.10
      nexthop_configure: local
      provider: "{{ cli }}"

  - name: "Undo BGP peer Address_Family"
    community.network.ce_bgp_neighbor_af:
      state: absent
      vrf_name: js
      af_type: ipv4uni
      remote_address: 192.168.10.10
      nexthop_configure: local
      provider: "{{ cli }}"
```

## [Return Values](ce_bgp_neighbor_af_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  **Returned:** always  **Sample:** `{"bgp neighbor af": {"af_type": "ipv4uni", "remote_address": "192.168.10.10", "vrf_name": "js"}, "bgp neighbor af other": {"af_type": "ipv4uni", "nexthop_configure": "local", "vrf_name": "js"}}` |
| **existing**  dictionary | k/v pairs of existing aaa server  **Returned:** always  **Sample:** `{"bgp neighbor af": {"af_type": "ipv4uni", "remote_address": "192.168.10.10", "vrf_name": "js"}, "bgp neighbor af other": {"af_type": "ipv4uni", "nexthop_configure": "null", "vrf_name": "js"}}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"af_type": "ipv4uni", "nexthop_configure": "local", "remote_address": "192.168.10.10", "state": "present", "vrf_name": "js"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["peer 192.168.10.10 next-hop-local"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
