---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_ntp module – Manages core NTP configuration."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_ntp_module.html
fetched_at: 2026-07-27T17:02:06+00:00
---
# cisco.nxos.nxos_ntp module – Manages core NTP configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_ntp`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_ntp_module.md#deprecated)
- [Synopsis](nxos_ntp_module.md#synopsis)
- [Parameters](nxos_ntp_module.md#parameters)
- [Notes](nxos_ntp_module.md#notes)
- [Examples](nxos_ntp_module.md#examples)
- [Return Values](nxos_ntp_module.md#return-values)
- [Status](nxos_ntp_module.md#status)

## [DEPRECATED](nxos_ntp_module.md#id1)

Removed in:
:   major release after 2024-01-01

Why:
:   Updated module released with more functionality.

Alternative:
:   nxos_ntp_global

## [Synopsis](nxos_ntp_module.md#id2)

- Manages core NTP configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_ntp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **key_id**  string | Authentication key identifier to use with given NTP server or peer or keyword ‘default’. |
| **peer**  string | Network address of NTP peer. |
| **prefer**  string | Makes given NTP server or peer the preferred NTP server or peer for the device.  Choices:   - `"enabled"` - `"disabled"` |
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
| **server**  string | Network address of NTP server. |
| **source_addr**  string | Local source address from which NTP messages are sent or keyword ‘default’. |
| **source_int**  string | Local source interface from which NTP messages are sent. Must be fully qualified interface name or keyword ‘default’ |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vrf_name**  string | Makes the device communicate with the given NTP server or peer over a specific VRF or keyword ‘default’. |

## [Notes](nxos_ntp_module.md#id4)

> **Note:**
>
> - Limited Support for Cisco MDS
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_ntp_module.md#id5)

```yaml+jinja
# Set NTP Server with parameters
- cisco.nxos.nxos_ntp:
    server: 1.2.3.4
    key_id: 32
    prefer: enabled
    host: '{{ inventory_hostname }}'
    username: '{{ un }}'
    password: '{{ pwd }}'
```

## [Return Values](nxos_ntp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of ntp info after module execution  Returned: always  Sample: `{"address": "192.0.2.2", "key_id": "48", "peer_type": "server", "prefer": "enabled", "source": "192.0.2.3", "source_type": "source"}` |
| **existing**  dictionary | k/v pairs of existing ntp server/peer  Returned: always  Sample: `{"address": "192.0.2.2", "key_id": "32", "peer_type": "server", "prefer": "enabled", "source": "ethernet2/1", "source_type": "source-interface"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"address": "192.0.2.2", "key_id": "48", "peer_type": "server", "prefer": "enabled", "source": "192.0.2.3", "source_type": "source"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["ntp server 192.0.2.2 prefer key 48", "no ntp source-interface ethernet2/1", "ntp source 192.0.2.3"]` |

## [Status](nxos_ntp_module.md#id7)

- This module will be removed in a major release after 2024-01-01.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_ntp_module.md#deprecated).

### Authors

- Jason Edelman (@jedelman8)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
