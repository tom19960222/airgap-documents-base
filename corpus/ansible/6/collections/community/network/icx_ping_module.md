---
collection: ansible
version: "6"
title: "community.network.icx_ping module – Tests reachability using ping from Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/icx_ping_module.html
fetched_at: 2026-07-27T17:18:47+00:00
---
# community.network.icx_ping module – Tests reachability using ping from Ruckus ICX 7000 series switches

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
> To use it in a playbook, specify: `community.network.icx_ping`.

- [Synopsis](icx_ping_module.md#synopsis)
- [Parameters](icx_ping_module.md#parameters)
- [Notes](icx_ping_module.md#notes)
- [Examples](icx_ping_module.md#examples)
- [Return Values](icx_ping_module.md#return-values)

## [Synopsis](icx_ping_module.md#id1)

- Tests reachability using ping from switch to a remote destination.

## [Parameters](icx_ping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **count**  integer | Number of packets to send. Default is 1. |
| **dest**  string / required | ip-addr | host-name | vrf vrf-name | ipv6 [ ipv6-addr | host-name | vrf vrf-name] (resolvable by switch) of the remote node. |
| **size**  integer | Specifies the size of the ICMP data portion of the packet, in bytes. This is the payload and does not include the header. The value can range from 0 to 10000. The default is 16.. |
| **source**  string | IP address to be used as the origin of the ping packets. |
| **state**  string | Determines if the expected result is success or fail.  Choices:   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | Specifies the time, in milliseconds for which the device waits for a reply from the pinged device. The value can range from 1 to 4294967296. The default is 5000 (5 seconds). |
| **ttl**  integer | Specifies the time to live as a maximum number of hops. The value can range from 1 to 255. The default is 64. |
| **vrf**  string | Specifies the Virtual Routing and Forwarding (VRF) instance of the device to be pinged. |

## [Notes](icx_ping_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1

## [Examples](icx_ping_module.md#id4)

```yaml+jinja
- name: Test reachability to 10.10.10.10
  community.network.icx_ping:
    dest: 10.10.10.10

- name: Test reachability to ipv6 address from source with timeout
  community.network.icx_ping:
    dest: ipv6 2001:cdba:0000:0000:0000:0000:3257:9652
    source: 10.1.1.1
    timeout: 100000

- name: Test reachability to 10.1.1.1 through vrf using 5 packets
  community.network.icx_ping:
    dest: 10.1.1.1
    vrf: x.x.x.x
    count: 5

- name: Test unreachability to 10.30.30.30
  community.network.icx_ping:
    dest: 10.40.40.40
    state: absent

- name: Test reachability to ipv4 with ttl and packet size
  community.network.icx_ping:
    dest: 10.10.10.10
    ttl: 20
    size: 500
```

## [Return Values](icx_ping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | Show the command sent.  Returned: always  Sample: `["ping 10.40.40.40 count 20 source loopback0", "ping 10.40.40.40"]` |
| **packet_loss**  string | Percentage of packets lost.  Returned: always  Sample: `"0%"` |
| **packets_rx**  integer | Packets successfully received.  Returned: always  Sample: `20` |
| **packets_tx**  integer | Packets successfully transmitted.  Returned: always  Sample: `20` |
| **rtt**  dictionary | Show RTT stats.  Returned: always  Sample: `{"avg": 2, "max": 8, "min": 1}` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
