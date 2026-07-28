---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_aaa_server module – Manages AAA server global configuration."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_aaa_server_module.html
fetched_at: 2026-07-27T17:01:32+00:00
---
# cisco.nxos.nxos_aaa_server module – Manages AAA server global configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_aaa_server`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_aaa_server_module.md#synopsis)
- [Parameters](nxos_aaa_server_module.md#parameters)
- [Notes](nxos_aaa_server_module.md#notes)
- [Examples](nxos_aaa_server_module.md#examples)
- [Return Values](nxos_aaa_server_module.md#return-values)

## [Synopsis](nxos_aaa_server_module.md#id1)

- Manages AAA server global configuration

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_aaa_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **deadtime**  string | Duration for which a non-reachable AAA server is skipped, in minutes or keyword ‘default. Range is 1-1440. Device default is 0. |
| **directed_request**  string | Enables direct authentication requests to AAA server or keyword ‘default’ Device default is disabled.  Choices:   - `"enabled"` - `"disabled"` - `"default"` |
| **encrypt_type**  string | The state of encryption applied to the entered global key. O clear text, 7 encrypted. Type-6 encryption is not supported.  Choices:   - `"0"` - `"7"` |
| **global_key**  string | Global AAA shared secret or keyword ‘default’. |
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
| **server_timeout**  string | Global AAA server timeout period, in seconds or keyword ‘default. Range is 1-60. Device default is 5. |
| **server_type**  string / required | The server type is either radius or tacacs.  Choices:   - `"radius"` - `"tacacs"` |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"default"` |

## [Notes](nxos_aaa_server_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Limited Support for Cisco MDS
> - The server_type parameter is always required.
> - If encrypt_type is not supplied, the global AAA server key will be stored as encrypted (type 7).
> - Changes to the global AAA server key with encrypt_type=0 are not idempotent.
> - state=default will set the supplied parameters to their default values. The parameters that you want to default must also be set to default. If global_key=default, the global key will be removed.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_aaa_server_module.md#id4)

```yaml+jinja
# Radius Server Basic settings
- name: Radius Server Basic settings
  cisco.nxos.nxos_aaa_server:
    server_type: radius
    server_timeout: 9
    deadtime: 20
    directed_request: enabled

# Tacacs Server Basic settings
- name: Tacacs Server Basic settings
  cisco.nxos.nxos_aaa_server:
    server_type: tacacs
    server_timeout: 8
    deadtime: 19
    directed_request: disabled

# Setting Global Key
- name: AAA Server Global Key
  cisco.nxos.nxos_aaa_server:
    server_type: radius
    global_key: test_key
```

## [Return Values](nxos_aaa_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | command sent to the device  Returned: always  Sample: `["radius-server deadtime 22", "radius-server timeout 11", "radius-server directed-request"]` |

### Authors

- Jason Edelman (@jedelman8)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
