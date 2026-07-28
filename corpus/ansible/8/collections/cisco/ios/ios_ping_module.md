---
collection: ansible
version: "8"
title: "cisco.ios.ios_ping module – Tests reachability using ping from IOS switch."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_ping_module.html
fetched_at: 2026-07-28T01:26:24+00:00
---
# cisco.ios.ios_ping module – Tests reachability using ping from IOS switch.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_ping`.

New in cisco.ios 1.0.0

- [Synopsis](ios_ping_module.md#synopsis)
- [Parameters](ios_ping_module.md#parameters)
- [Notes](ios_ping_module.md#notes)
- [Examples](ios_ping_module.md#examples)
- [Return Values](ios_ping_module.md#return-values)

## [Synopsis](ios_ping_module.md#id1)

- Tests reachability using ping from switch to a remote destination.
- For a general purpose network module, see the [net_ping](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/net_ping_module.html) module.
- For Windows targets, use the [win_ping](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_ping_module.html) module instead.
- For targets running Python, use the [ping](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html) module instead.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: ping

## [Parameters](ios_ping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **afi**  string | Define echo type ip or ipv6.  **Choices:**   - `"ip"` ← (default) - `"ipv6"` |
| **count**  integer | Number of packets to send. |
| **dest**  string / required | The IP Address or hostname (resolvable by switch) of the remote node. |
| **df_bit**  boolean | Set the DF bit.  **Choices:**   - `false` ← (default) - `true` |
| **egress**  string | Force egress interface bypassing routing. |
| **ingress**  string | LAN source interface for Ingress. |
| **source**  string | The source IP Address. |
| **state**  string | Determines if the expected result is success or fail.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | specify timeout interval. |
| **vrf**  string | The VRF to use for forwarding. |

## [Notes](ios_ping_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - For a general purpose network module, see the [net_ping](https://docs.ansible.com/ansible/latest/collections/ansible/netcommon/net_ping_module.html) module.
> - For Windows targets, use the [win_ping](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_ping_module.html) module instead.
> - For targets running Python, use the [ping](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/ping_module.html) module instead.

## [Examples](ios_ping_module.md#id4)

```yaml+jinja
- name: Test reachability to 198.51.100.251 using default vrf
  cisco.ios.ios_ping:
    dest: 198.51.100.251

- name: Test reachability to 198.51.100.252 using prod vrf
  cisco.ios.ios_ping:
    dest: 198.51.100.252
    vrf: prod
    afi: ip

- name: Test un reachability to 198.51.100.253 using default vrf
  cisco.ios.ios_ping:
    dest: 198.51.100.253
    state: absent

- name: Test reachability to 198.51.100.250 using prod vrf and setting count and source
  cisco.ios.ios_ping:
    dest: 198.51.100.250
    source: loopback0
    vrf: prod
    count: 20

- name: Test reachability to 198.51.100.249 using df-bit and size
  cisco.ios.ios_ping:
    dest: 198.51.100.249
    df_bit: true
    size: 1400

- name: Test reachability to ipv6 address
  cisco.ios.ios_ping:
    dest: 2001:db8:ffff:ffff:ffff:ffff:ffff:ffff
    afi: ipv6
```

## [Return Values](ios_ping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | Show the command sent.  **Returned:** always  **Sample:** `["ping vrf prod 198.51.100.251 count 20 source loopback0"]` |
| **packet_loss**  string | Percentage of packets lost.  **Returned:** always  **Sample:** `"0%"` |
| **packets_rx**  integer | Packets successfully received.  **Returned:** always  **Sample:** `20` |
| **packets_tx**  integer | Packets successfully transmitted.  **Returned:** always  **Sample:** `20` |
| **rtt**  dictionary | Show RTT stats.  **Returned:** always  **Sample:** `{"avg": 2, "max": 8, "min": 1}` |

### Authors

- Jacob McGill (@jmcgill298)
- Sagar Paul (@KB-perByte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
