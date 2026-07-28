---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_ping module – Tests reachability using ping from devices running Juniper JUNOS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_ping_module.html
fetched_at: 2026-07-27T17:54:32+00:00
---
# junipernetworks.junos.junos_ping module – Tests reachability using ping from devices running Juniper JUNOS

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_ping`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_ping_module.md#synopsis)
- [Parameters](junos_ping_module.md#parameters)
- [Notes](junos_ping_module.md#notes)
- [Examples](junos_ping_module.md#examples)
- [Return Values](junos_ping_module.md#return-values)

## [Synopsis](junos_ping_module.md#id1)

- Tests reachability using ping from devices running Juniper JUNOS to a remote destination.
- Tested against Junos (17.3R1.10)
- For a general purpose network module, see the [ansible.netcommon.net_ping](../../ansible/netcommon/net_ping_module.md#ansible-collections-ansible-netcommon-net-ping-module) module.
- For Windows targets, use the [ansible.windows.win_ping](../../ansible/windows/win_ping_module.md#ansible-collections-ansible-windows-win-ping-module) module instead.
- For targets running Python, use the [ansible.builtin.ping](../../ansible/builtin/ping_module.md#ansible-collections-ansible-builtin-ping-module) module instead.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](junos_ping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **count**  integer | Number of packets to send to check reachability.  Default: `5` |
| **dest**  string / required | The IP Address or hostname (resolvable by the device) of the remote node. |
| **df_bit**  boolean | Determines whether to set the DF bit.  Choices:   - `false` ← (default) - `true` |
| **interface**  string | The source interface to use while sending the ping packet(s). |
| **interval**  integer | Determines the interval (in seconds) between consecutive pings. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` or `connection: netconf`.  For more information please see the [Junos OS Platform Options guide](../network/user_guide/platform_junos.md).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. The port value will default to the well known SSH port of 22 (for `transport=cli`) or port 830 (for `transport=netconf`) device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` - `"netconf"` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **rapid**  boolean | Determines whether to send the packets rapidly.  Choices:   - `false` ← (default) - `true` |
| **size**  integer | Determines the size (in bytes) of the ping packet(s). |
| **source**  string | The IP Address to use while sending the ping packet(s). |
| **state**  string | Determines if the expected result is success or fail.  Choices:   - `"absent"` - `"present"` ← (default) |
| **ttl**  integer | The time-to-live value for the ICMP packet(s). |

## [Notes](junos_ping_module.md#id3)

> **Note:**
>
> - For a general purpose network module, see the [ansible.netcommon.net_ping](../../ansible/netcommon/net_ping_module.md#ansible-collections-ansible-netcommon-net-ping-module) module.
> - For Windows targets, use the [ansible.windows.win_ping](../../ansible/windows/win_ping_module.md#ansible-collections-ansible-windows-win-ping-module) module instead.
> - For targets running Python, use the [ansible.builtin.ping](../../ansible/builtin/ping_module.md#ansible-collections-ansible-builtin-ping-module) module instead.
> - This module works only with connection `network_cli`.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_ping_module.md#id4)

```yaml+jinja
- name: Test reachability to 10.10.10.10
  junipernetworks.junos.junos_ping:
    dest: 10.10.10.10

- name: Test reachability to 10.20.20.20 using source and size set
  junipernetworks.junos.junos_ping:
    dest: 10.20.20.20
    size: 1024
    ttl: 128

- name: Test unreachability to 10.30.30.30 using interval
  junipernetworks.junos.junos_ping:
    dest: 10.30.30.30
    interval: 3
    state: absent

- name: Test reachability to 10.40.40.40 setting count and interface
  junipernetworks.junos.junos_ping:
    dest: 10.40.40.40
    interface: fxp0
    count: 20
    size: 512

- name: Test reachability to 10.50.50.50 using do-not-fragment and rapid
  junipernetworks.junos.junos_ping:
    dest: 10.50.50.50
    df_bit: True
    rapid: True
```

## [Return Values](junos_ping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | List of commands sent.  Returned: always  Sample: `["ping 10.8.38.44 count 10 source 10.8.38.38 ttl 128"]` |
| **packet_loss**  string | Percentage of packets lost.  Returned: always  Sample: `"0%"` |
| **packets_rx**  integer | Packets successfully received.  Returned: always  Sample: `20` |
| **packets_tx**  integer | Packets successfully transmitted.  Returned: always  Sample: `20` |
| **rtt**  dictionary | The round trip time (RTT) stats.  Returned: when ping succeeds  Sample: `{"avg": 2, "max": 8, "min": 1, "stddev": 24}` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
