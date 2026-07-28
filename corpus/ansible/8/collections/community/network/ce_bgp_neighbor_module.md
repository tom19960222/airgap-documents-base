---
collection: ansible
version: "8"
title: "community.network.ce_bgp_neighbor module – Manages BGP peer configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_bgp_neighbor_module.html
fetched_at: 2026-07-28T01:55:17+00:00
---
# community.network.ce_bgp_neighbor module – Manages BGP peer configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_bgp_neighbor`.

- [Synopsis](ce_bgp_neighbor_module.md#synopsis)
- [Parameters](ce_bgp_neighbor_module.md#parameters)
- [Notes](ce_bgp_neighbor_module.md#notes)
- [Examples](ce_bgp_neighbor_module.md#examples)
- [Return Values](ce_bgp_neighbor_module.md#return-values)

## [Synopsis](ce_bgp_neighbor_module.md#id1)

- Manages BGP peer configurations on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_bgp_neighbor

## [Parameters](ce_bgp_neighbor_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **conn_retry_time**  string | ConnectRetry interval. The value is an integer ranging from 1 to 65535. |
| **connect_mode**  string | The value can be Connect-only, Listen-only, or Both. |
| **conventional**  string | If the value is true, the router has all extended capabilities. If the value is false, the router does not have all extended capabilities.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **description**  string | Description of a peer, which can be letters or digits. The value is a string of 1 to 80 characters. |
| **dual_as**  string | If the value is true, the EBGP peer can use either a fake AS number or the actual AS number. If the value is false, the EBGP peer can only use a fake AS number.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **ebgp_max_hop**  string | Maximum number of hops in an indirect EBGP connection. The value is an ranging from 1 to 255. |
| **fake_as**  string | Fake AS number that is specified for a local peer. The value is a string of 1 to 11 characters. |
| **hold_time**  string | Specify the Hold time of a peer or peer group. The value is 0 or an integer ranging from 3 to 65535. |
| **is_bfd_block**  string | If the value is true, peers are enabled to inherit the BFD function from the peer group. If the value is false, peers are disabled to inherit the BFD function from the peer group.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **is_bfd_enable**  string | If the value is true, BFD is enabled. If the value is false, BFD is disabled.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **is_ignore**  string | If the value is true, the session with a specified peer is torn down and all related routing entries are cleared. If the value is false, the session with a specified peer is retained.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **is_log_change**  string | If the value is true, BGP is enabled to record peer session status and event information. If the value is false, BGP is disabled from recording peer session status and event information.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **is_single_hop**  string | If the value is true, the system is enabled to preferentially use the single-hop mode for BFD session setup between IBGP peers. If the value is false, the system is disabled from preferentially using the single-hop mode for BFD session setup between IBGP peers.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **keep_alive_time**  string | Specify the Keepalive time of a peer or peer group. The value is an integer ranging from 0 to 21845. The default value is 60. |
| **key_chain_name**  string | Specify the Keychain authentication name used when BGP peers establish a TCP connection. The value is a string of 1 to 47 case-insensitive characters. |
| **local_if_name**  string | Name of a source interface that sends BGP packets. The value is a string of 1 to 63 characters. |
| **min_hold_time**  string | Specify the Min hold time of a peer or peer group. |
| **mpls_local_ifnet_disable**  string | If the value is true, peer create MPLS Local IFNET disable. If the value is false, peer create MPLS Local IFNET enable.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **multiplier**  string | Specify the detection multiplier. The default value is 3. The value is an integer ranging from 3 to 50. |
| **peer_addr**  string / required | Connection address of a peer, which can be an IPv4 or IPv6 address. |
| **prepend_fake_as**  string | Add the Fake AS number to received Update packets.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **prepend_global_as**  string | Add the global AS number to the Update packets to be advertised.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **pswd_cipher_text**  string | The character string in a password identifies the contents of the password, spaces not supported. The value is a string of 1 to 255 characters. |
| **pswd_type**  string | Enable BGP peers to establish a TCP connection and perform the Message Digest 5 (MD5) authentication for BGP messages.  **Choices:**   - `"null"` - `"cipher"` - `"simple"` |
| **remote_as**  string / required | AS number of a peer. The value is a string of 1 to 11 characters. |
| **route_refresh**  string | If the value is true, BGP is enabled to advertise REFRESH packets. If the value is false, the route refresh function is enabled.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **rx_interval**  string | Specify the minimum interval at which BFD packets are received. The value is an integer ranging from 50 to 1000, in milliseconds. |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tcp_MSS**  string | Maximum TCP MSS value used for TCP connection establishment for a peer. The value is an integer ranging from 176 to 4096. |
| **tx_interval**  string | Specify the minimum interval at which BFD packets are sent. The value is an integer ranging from 50 to 1000, in milliseconds. |
| **valid_ttl_hops**  string | Enable GTSM on a peer or peer group. The valid-TTL-Value parameter is used to specify the number of TTL hops to be detected. The value is an integer ranging from 1 to 255. |
| **vrf_name**  string / required | Name of a BGP instance. The name is a case-sensitive string of characters. The BGP instance can be used only after the corresponding VPN instance is created. |

## [Notes](ce_bgp_neighbor_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_bgp_neighbor_module.md#id4)

```yaml+jinja
- name: CloudEngine BGP neighbor test
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

  - name: "Config bgp peer"
    community.network.ce_bgp_neighbor:
      state: present
      vrf_name: js
      peer_addr: 192.168.10.10
      remote_as: 500
      provider: "{{ cli }}"

  - name: "Config bgp route id"
    community.network.ce_bgp_neighbor:
      state: absent
      vrf_name: js
      peer_addr: 192.168.10.10
      provider: "{{ cli }}"
```

## [Return Values](ce_bgp_neighbor_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  **Returned:** always  **Sample:** `{"bgp peer": [["192.168.10.10", "500"]]}` |
| **existing**  dictionary | k/v pairs of existing aaa server  **Returned:** always  **Sample:** `{"bgp peer": []}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"peer_addr": "192.168.10.10", "remote_as": "500", "state": "present", "vrf_name": "js"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["peer 192.168.10.10 as-number 500"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
