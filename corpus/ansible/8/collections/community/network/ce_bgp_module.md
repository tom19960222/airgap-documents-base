---
collection: ansible
version: "8"
title: "community.network.ce_bgp module – Manages BGP configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_bgp_module.html
fetched_at: 2026-07-28T01:55:16+00:00
---
# community.network.ce_bgp module – Manages BGP configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_bgp`.

- [Synopsis](ce_bgp_module.md#synopsis)
- [Parameters](ce_bgp_module.md#parameters)
- [Notes](ce_bgp_module.md#notes)
- [Examples](ce_bgp_module.md#examples)
- [Return Values](ce_bgp_module.md#return-values)

## [Synopsis](ce_bgp_module.md#id1)

- Manages BGP configurations on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_bgp

## [Parameters](ce_bgp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **as_number**  string | Local AS number. The value is a string of 1 to 11 characters. |
| **as_path_limit**  string | Maximum number of AS numbers in the AS_Path attribute. The default value is 255. |
| **bgp_rid_auto_sel**  string | The function to automatically select router IDs for all VPN BGP instances is enabled.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **check_first_as**  string | Check the first AS in the AS_Path of the update messages from EBGP peers.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **clear_interval**  string | Clear interval. |
| **confed_id_number**  string | Confederation ID. The value is a string of 1 to 11 characters. |
| **confed_nonstanded**  string | Configure the device to be compatible with devices in a nonstandard confederation.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **confed_peer_as_num**  string | Confederation AS number, in two-byte or four-byte format. The value is a string of 1 to 11 characters. |
| **conn_retry_time**  string | ConnectRetry interval. The value is an integer, in seconds. The default value is 32s. |
| **default_af_type**  string | Type of a created address family, which can be IPv4 unicast or IPv6 unicast. The default type is IPv4 unicast.  **Choices:**   - `"ipv4uni"` - `"ipv6uni"` |
| **ebgp_if_sensitive**  string | If the value is true, After the fast EBGP interface awareness function is enabled, EBGP sessions on an interface are deleted immediately when the interface goes Down. If the value is false, After the fast EBGP interface awareness function is enabled, EBGP sessions on an interface are not deleted immediately when the interface goes Down.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **gr_peer_reset**  string | Peer disconnection through GR.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **graceful_restart**  string | Enable GR of the BGP speaker in the specified address family, peer address, or peer group.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **hold_interval**  string | Hold interval. |
| **hold_time**  string | Hold time, in seconds. The value of the hold time can be 0 or range from 3 to 65535. |
| **is_shutdown**  string | Interrupt BGP all neighbor.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **keep_all_routes**  string | If the value is true, the system stores all route update messages received from all peers (groups) after BGP connection setup. If the value is false, the system stores only BGP update messages that are received from peers and pass the configured import policy.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **keepalive_time**  string | If the value of a timer changes, the BGP peer relationship between the routers is disconnected. The value is an integer ranging from 0 to 21845. The default value is 60. |
| **memory_limit**  string | Support BGP RIB memory protection.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **min_hold_time**  string | Min hold time, in seconds. The value of the hold time can be 0 or range from 20 to 65535. |
| **router_id**  string | ID of a router that is in IPv4 address format. |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **suppress_interval**  string | Suppress interval. |
| **time_wait_for_rib**  string | Period of waiting for the End-Of-RIB flag. The value is an integer ranging from 3 to 3000. The default value is 600. |
| **vrf_name**  string | Name of a BGP instance. The name is a case-sensitive string of characters. |
| **vrf_rid_auto_sel**  string | If the value is true, VPN BGP instances are enabled to automatically select router IDs. If the value is false, VPN BGP instances are disabled from automatically selecting router IDs.  **Choices:**   - `"no_use"` ← (default) - `"true"` - `"false"` |

## [Notes](ce_bgp_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_bgp_module.md#id4)

```yaml+jinja
- name: CloudEngine BGP test
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

  - name: "Enable BGP"
    community.network.ce_bgp:
      state: present
      as_number: 100
      confed_id_number: 250
      provider: "{{ cli }}"

  - name: "Disable BGP"
    community.network.ce_bgp:
      state: absent
      as_number: 100
      confed_id_number: 250
      provider: "{{ cli }}"

  - name: "Create confederation peer AS num"
    community.network.ce_bgp:
      state: present
      confed_peer_as_num: 260
      provider: "{{ cli }}"
```

## [Return Values](ce_bgp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  **Returned:** always  **Sample:** `{"bgp_enable": [["100"], ["true"]]}` |
| **existing**  dictionary | k/v pairs of existing aaa server  **Returned:** always  **Sample:** `{"bgp_enable": [["100"], ["true"]]}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"as_number": "100", "state\"": "present"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["bgp 100"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
