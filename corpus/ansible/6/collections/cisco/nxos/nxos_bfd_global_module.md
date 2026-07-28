---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_bfd_global module – Bidirectional Forwarding Detection (BFD) global-level configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_bfd_global_module.html
fetched_at: 2026-07-27T17:01:37+00:00
---
# cisco.nxos.nxos_bfd_global module – Bidirectional Forwarding Detection (BFD) global-level configuration

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
> To use it in a playbook, specify: `cisco.nxos.nxos_bfd_global`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_bfd_global_module.md#synopsis)
- [Parameters](nxos_bfd_global_module.md#parameters)
- [Notes](nxos_bfd_global_module.md#notes)
- [Examples](nxos_bfd_global_module.md#examples)
- [Return Values](nxos_bfd_global_module.md#return-values)

## [Synopsis](nxos_bfd_global_module.md#id1)

- Manages Bidirectional Forwarding Detection (BFD) global-level configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_bfd_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **echo_interface**  string | Loopback interface used for echo frames.  Valid values are loopback interface name or ‘deleted’.  Not supported on N5K/N6K |
| **echo_rx_interval**  integer | BFD Echo receive interval in milliseconds. |
| **fabricpath_interval**  dictionary | BFD fabricpath interval timer values.  Value must be a dict defining values for keys (tx, min_rx, and multiplier). |
| **fabricpath_slow_timer**  integer | BFD fabricpath slow rate timer in milliseconds. |
| **fabricpath_vlan**  integer | BFD fabricpath control vlan. |
| **interval**  dictionary | BFD interval timer values.  Value must be a dict defining values for keys (tx, min_rx, and multiplier) |
| **ipv4_echo_rx_interval**  integer | BFD IPv4 session echo receive interval in milliseconds. |
| **ipv4_interval**  dictionary | BFD IPv4 interval timer values.  Value must be a dict defining values for keys (tx, min_rx, and multiplier). |
| **ipv4_slow_timer**  integer | BFD IPv4 slow rate timer in milliseconds. |
| **ipv6_echo_rx_interval**  integer | BFD IPv6 session echo receive interval in milliseconds. |
| **ipv6_interval**  dictionary | BFD IPv6 interval timer values.  Value must be a dict defining values for keys (tx, min_rx, and multiplier). |
| **ipv6_slow_timer**  integer | BFD IPv6 slow rate timer in milliseconds. |
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
| **slow_timer**  integer | BFD slow rate timer in milliseconds. |
| **startup_timer**  integer | BFD delayed startup timer in seconds.  Not supported on N5K/N6K/N7K |

## [Notes](nxos_bfd_global_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 9.2(2)
> - Unsupported for Cisco MDS
> - BFD global will automatically enable ‘feature bfd’ if it is disabled.
> - BFD global does not have a ‘state’ parameter. All of the BFD commands are unique and are defined if ‘feature bfd’ is enabled.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_bfd_global_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_bfd_global:
    echo_interface: Ethernet1/2
    echo_rx_interval: 50
    interval:
      tx: 50
      min_rx: 50
      multiplier: 4
```

## [Return Values](nxos_bfd_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmds**  list / elements=string | commands sent to the device  Returned: always  Sample: `["bfd echo-interface loopback1", "bfd slow-timer 2000"]` |

### Authors

- Chris Van Heuveln (@chrisvanheuveln)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
