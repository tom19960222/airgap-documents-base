---
collection: ansible
version: "6"
title: "ansible.netcommon.net_ping module – Tests reachability using ping from a network device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_ping_module.html
fetched_at: 2026-07-27T16:44:31+00:00
---
# ansible.netcommon.net_ping module – Tests reachability using ping from a network device

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.net_ping`.

New in ansible.netcommon 1.0.0

- [Synopsis](net_ping_module.md#synopsis)
- [Parameters](net_ping_module.md#parameters)
- [Notes](net_ping_module.md#notes)
- [Examples](net_ping_module.md#examples)
- [Return Values](net_ping_module.md#return-values)

## [Synopsis](net_ping_module.md#id1)

- Tests reachability using ping from network device to a remote destination.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](net_ping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **count**  string | Number of packets to send.  Default: `5` |
| **dest**  string / required | The IP Address or hostname (resolvable by switch) of the remote node. |
| **source**  string | The source IP Address. |
| **state**  string | Determines if the expected result is success or fail.  Choices:   - `"absent"` - `"present"` ← (default) |
| **vrf**  string | The VRF to use for forwarding.  Default: `"default"` |

## [Notes](net_ping_module.md#id3)

> **Note:**
>
> - For targets running Python, use the [ansible.builtin.shell](../builtin/shell_module.md#ansible-collections-ansible-builtin-shell-module) module along with ping command instead.
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_ping_module.md#id4)

```yaml+jinja
- name: Test reachability to 10.10.10.10 using default vrf
  ansible.netcommon.net_ping:
    dest: 10.10.10.10

- name: Test reachability to 10.20.20.20 using prod vrf
  ansible.netcommon.net_ping:
    dest: 10.20.20.20
    vrf: prod

- name: Test unreachability to 10.30.30.30 using default vrf
  ansible.netcommon.net_ping:
    dest: 10.30.30.30
    state: absent

- name: Test reachability to 10.40.40.40 using prod vrf and setting count and source
  ansible.netcommon.net_ping:
    dest: 10.40.40.40
    source: loopback0
    vrf: prod
    count: 20

- Note:
    - For targets running Python, use the M(ansible.builtin.shell) module along with ping command instead.
    - Example:
        name: ping
        shell: ping -c 1 <remote-ip>
```

## [Return Values](net_ping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | Show the command sent.  Returned: always  Sample: `["ping vrf prod 10.40.40.40 count 20 source loopback0"]` |
| **packet_loss**  string | Percentage of packets lost.  Returned: always  Sample: `"0%"` |
| **packets_rx**  integer | Packets successfully received.  Returned: always  Sample: `20` |
| **packets_tx**  integer | Packets successfully transmitted.  Returned: always  Sample: `20` |
| **rtt**  dictionary | Show RTT stats.  Returned: always  Sample: `{"avg": 2, "max": 8, "min": 1}` |

### Authors

- Jacob McGill (@jmcgill298)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
