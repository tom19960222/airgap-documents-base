---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_ping module – Tests reachability using ping from VyOS network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_ping_module.html
fetched_at: 2026-07-28T00:23:29+00:00
---
# vyos.vyos.vyos_ping module – Tests reachability using ping from VyOS network devices

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/vyos/vyos) (version 3.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_ping`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_ping_module.md#synopsis)
- [Parameters](vyos_ping_module.md#parameters)
- [Notes](vyos_ping_module.md#notes)
- [Examples](vyos_ping_module.md#examples)
- [Return Values](vyos_ping_module.md#return-values)

## [Synopsis](vyos_ping_module.md#id1)

- Tests reachability using ping from a VyOS device to a remote destination.
- Tested against VyOS 1.1.8 (helium)
- For a general purpose network module, see the net_ping module.
- For Windows targets, use the win_ping module instead.
- For targets running Python, use the ping module instead.

## [Parameters](vyos_ping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **count**  integer | Number of packets to send to check reachability.  Default: `5` |
| **dest**  string / required | The IP Address or hostname (resolvable by the device) of the remote node. |
| **interval**  integer | Determines the interval (in seconds) between consecutive pings. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **size**  integer | Determines the size (in bytes) of the ping packet(s). |
| **source**  string | The source interface or IP Address to use while sending the ping packet(s). |
| **state**  string | Determines if the expected result is success or fail.  Choices:   - `"absent"` - `"present"` ← (default) |
| **ttl**  integer | The time-to-live value for the ICMP packet(s). |

## [Notes](vyos_ping_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - For a general purpose network module, see the net_ping module.
> - For Windows targets, use the win_ping module instead.
> - For targets running Python, use the ping module instead.
> - This module works with connection `network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_ping_module.md#id4)

```yaml+jinja
- name: Test reachability to 10.10.10.10
  vyos.vyos.vyos_ping:
    dest: 10.10.10.10

- name: Test reachability to 10.20.20.20 using source and ttl set
  vyos.vyos.vyos_ping:
    dest: 10.20.20.20
    source: eth0
    ttl: 128

- name: Test reachability to 10.30.30.30 using interval
  vyos.vyos.vyos_ping:
    dest: 10.30.30.30
    interval: 3
    state: absent

- name: Test reachability to 10.40.40.40 setting count and source
  vyos.vyos.vyos_ping:
    dest: 10.40.40.40
    source: eth1
    count: 20
    size: 512
```

## [Return Values](vyos_ping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | List of commands sent.  Returned: always  Sample: `["ping 10.8.38.44 count 10 interface eth0 ttl 128"]` |
| **packet_loss**  string | Percentage of packets lost.  Returned: always  Sample: `"0%"` |
| **packets_rx**  integer | Packets successfully received.  Returned: always  Sample: `20` |
| **packets_tx**  integer | Packets successfully transmitted.  Returned: always  Sample: `20` |
| **rtt**  dictionary | The round trip time (RTT) stats.  Returned: when ping succeeds  Sample: `{"avg": 2, "max": 8, "mdev": 24, "min": 1}` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
