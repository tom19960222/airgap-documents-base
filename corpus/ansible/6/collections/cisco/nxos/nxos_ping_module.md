---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_ping module – Tests reachability using ping from Nexus switch."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_ping_module.html
fetched_at: 2026-07-27T17:02:16+00:00
---
# cisco.nxos.nxos_ping module – Tests reachability using ping from Nexus switch.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/cisco/nxos) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_ping`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_ping_module.md#synopsis)
- [Parameters](nxos_ping_module.md#parameters)
- [Notes](nxos_ping_module.md#notes)
- [Examples](nxos_ping_module.md#examples)
- [Return Values](nxos_ping_module.md#return-values)

## [Synopsis](nxos_ping_module.md#id1)

- Tests reachability using ping from switch to a remote destination.
- For a general purpose network module, see the [ansible.netcommon.net_ping](../../ansible/netcommon/net_ping_module.md#ansible-collections-ansible-netcommon-net-ping-module) module.
- For Windows targets, use the [ansible.windows.win_ping](../../ansible/windows/win_ping_module.md#ansible-collections-ansible-windows-win-ping-module) module instead.
- For targets running Python, use the [ansible.builtin.ping](../../ansible/builtin/ping_module.md#ansible-collections-ansible-builtin-ping-module) module instead.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_ping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **count**  integer | Number of packets to send.  Default: `5` |
| **dest**  string / required | IP address or hostname (resolvable by switch) of remote node. |
| **df_bit**  boolean | Set the DF bit.  Choices:   - `false` ← (default) - `true` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  Starting with Ansible 2.6 we recommend using `connection: httpapi` for NX-API.  This option will be removed in a release after 2022-06-01.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_nxos.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This is a common argument used for either *cli* or *nxapi* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. This value applies to either *cli* or *nxapi*. The port value will default to the appropriate transport common port if none is provided in the task. (cli=22, http=80, https=443). |
| **ssh_keyfile**  string | Specifies the SSH key to use to authenticate the connection to the remote device. This argument is only used for the *cli* transport. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc). |
| **transport**  string | Configures the transport connection to use when connecting to the remote device. The transport argument supports connectivity to the device over cli (ssh) or nxapi.  Choices:   - `"cli"` ← (default) - `"nxapi"` |
| **use_proxy**  boolean | If `no`, the environment variables `http_proxy` and `https_proxy` will be ignored.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | Configures the *transport* to use SSL if set to `yes` only when the `transport=nxapi`, otherwise this value is ignored.  Choices:   - `false` ← (default) - `true` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates. If the transport argument is not nxapi, this value is ignored.  Choices:   - `false` ← (default) - `true` |
| **size**  integer | Size of packets to send. |
| **source**  string | Source IP Address or hostname (resolvable by switch) |
| **state**  string | Determines if the expected result is success or fail.  Choices:   - `"absent"` - `"present"` ← (default) |
| **vrf**  string | Outgoing VRF. |

## [Notes](nxos_ping_module.md#id3)

> **Note:**
>
> - Unsupported for Cisco MDS
> - For a general purpose network module, see the [ansible.netcommon.net_ping](../../ansible/netcommon/net_ping_module.md#ansible-collections-ansible-netcommon-net-ping-module) module.
> - For Windows targets, use the [ansible.windows.win_ping](../../ansible/windows/win_ping_module.md#ansible-collections-ansible-windows-win-ping-module) module instead.
> - For targets running Python, use the [ansible.builtin.ping](../../ansible/builtin/ping_module.md#ansible-collections-ansible-builtin-ping-module) module instead.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_ping_module.md#id4)

```yaml+jinja
- name: Test reachability to 8.8.8.8 using mgmt vrf
  cisco.nxos.nxos_ping:
    dest: 8.8.8.8
    vrf: management
    host: 68.170.147.165

- name: Test reachability to a few different public IPs using mgmt vrf
  cisco.nxos.nxos_ping:
    dest: "{{ item }}"
    vrf: management
    host: 68.170.147.165
  with_items:
    - 8.8.8.8
    - 4.4.4.4
    - 198.6.1.4

- name: Test reachability to 8.8.8.8 using mgmt vrf, size and df-bit
  cisco.nxos.nxos_ping:
    dest: 8.8.8.8
    df_bit: true
    size: 1400
    vrf: management
```

## [Return Values](nxos_ping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | Show the command sent  Returned: always  Sample: `["ping 8.8.8.8 count 2 vrf management"]` |
| **packet_loss**  string | Percentage of packets lost  Returned: always  Sample: `"0.00%"` |
| **packets_rx**  integer | Packets successfully received  Returned: always  Sample: `2` |
| **packets_tx**  integer | Packets successfully transmitted  Returned: always  Sample: `2` |
| **rtt**  dictionary | Show RTT stats  Returned: always  Sample: `{"avg": 6.264, "max": 6.564, "min": 5.978}` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
