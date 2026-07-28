---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_ping module – Tests reachability using ping from IOSXR switch."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_ping_module.html
fetched_at: 2026-07-28T01:26:57+00:00
---
# cisco.iosxr.iosxr_ping module – Tests reachability using ping from IOSXR switch.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_ping`.

- [Synopsis](iosxr_ping_module.md#synopsis)
- [Parameters](iosxr_ping_module.md#parameters)
- [Notes](iosxr_ping_module.md#notes)
- [Examples](iosxr_ping_module.md#examples)
- [Return Values](iosxr_ping_module.md#return-values)

## [Synopsis](iosxr_ping_module.md#id1)

- Tests reachability using ping from switch to a remote destination.
- For a general purpose network module, see the [net_ping](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/net_ping_module.html) module.
- For Windows targets, use the [win_ping](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_ping_module.html) module instead.
- For targets running Python, use the [ping](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html) module instead.

## [Parameters](iosxr_ping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **afi**  string | Define echo type ipv4 or ipv6.  **Choices:**   - `"ipv4"` ← (default) - `"ipv6"` |
| **count**  integer | Repeat count the number of packets to send. |
| **dest**  string / required | The IP Address or hostname (resolvable by switch) of the remote node. |
| **df_bit**  boolean | Set the DF bit in IP-header.  **Choices:**   - `false` ← (default) - `true` |
| **size**  integer | Datagram size the size of packets to send. |
| **source**  string | Source address or source interface. |
| **state**  string | Determines if the expected result is success or fail.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **sweep**  boolean | Sweep ping.  **Choices:**   - `false` ← (default) - `true` |
| **validate**  boolean | Validate return packet.  **Choices:**   - `false` ← (default) - `true` |
| **vrf**  string | The VRF to use for forwarding. |

## [Notes](iosxr_ping_module.md#id3)

> **Note:**
>
> - Tested against IOSXR 7.2.2.
> - This module works with connection `network_cli`.
> - For a general purpose network module, see the [net_ping](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/net_ping_module.html) module.
> - For Windows targets, use the [win_ping](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_ping_module.html) module instead.
> - For targets running Python, use the [ping](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html) module instead.

## [Examples](iosxr_ping_module.md#id4)

```yaml+jinja
- name: Test reachability to 198.51.100.251 using default vrf
  cisco.iosxr.iosxr_ping:
    dest: 198.51.100.251

- name: Test reachability to 198.51.100.252 using prod vrf
  cisco.iosxr.iosxr_ping:
    dest: 198.51.100.252
    vrf: prod
    afi: ipv4

- name: Test unreachability to 198.51.100.253 using default vrf
  cisco.iosxr.iosxr_ping:
    dest: 198.51.100.253
    state: absent

- name: Test reachability to 198.51.100.250 using prod vrf and setting count and source
  cisco.iosxr.iosxr_ping:
    dest: 198.51.100.250
    source: loopback0
    vrf: prod
    count: 20

- name: Test reachability to 198.51.100.249 using df-bit and size
  cisco.iosxr.iosxr_ping:
    dest: 198.51.100.249
    df_bit: true
    size: 1400

- name: Test reachability to ipv6 address
  cisco.iosxr.iosxr_ping:
    dest: 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff
    afi: ipv6
```

## [Return Values](iosxr_ping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | Show the command sent.  **Returned:** always  **Sample:** `["ping vrf prod 198.51.100.251 count 20 source loopback0"]` |
| **packet_loss**  string | Percentage of packets lost.  **Returned:** always  **Sample:** `"0%"` |
| **packets_rx**  integer | Packets successfully received.  **Returned:** always  **Sample:** `20` |
| **packets_tx**  integer | Packets successfully transmitted.  **Returned:** always  **Sample:** `20` |
| **rtt**  dictionary | Show RTT stats.  **Returned:** always  **Sample:** `{"avg": 2, "max": 8, "min": 1}` |

### Authors

- Sagar Paul (@KB-perByte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
