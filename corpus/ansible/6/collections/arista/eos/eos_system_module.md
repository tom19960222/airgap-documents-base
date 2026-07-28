---
collection: ansible
version: "6"
title: "arista.eos.eos_system module – Manage the system attributes on Arista EOS devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_system_module.html
fetched_at: 2026-07-27T16:45:19+00:00
---
# arista.eos.eos_system module – Manage the system attributes on Arista EOS devices

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/arista/eos) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_system`.

New in arista.eos 1.0.0

- [Synopsis](eos_system_module.md#synopsis)
- [Parameters](eos_system_module.md#parameters)
- [Notes](eos_system_module.md#notes)
- [Examples](eos_system_module.md#examples)
- [Return Values](eos_system_module.md#return-values)

## [Synopsis](eos_system_module.md#id1)

- This module provides declarative management of node system attributes on Arista EOS devices. It provides an option to configure host system parameters or remove those parameters from the device active configuration.

## [Parameters](eos_system_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain_list**  aliases: domain_search  list / elements=string | Provides the list of domain suffixes to append to the hostname for the purpose of doing name resolution. This argument accepts a list of names and will be reconciled with the current active configuration on the running node. |
| **domain_name**  string | Configure the IP domain name on the remote device to the provided value. Value should be in the dotted name form and will be appended to the `hostname` to create a fully-qualified domain name. |
| **hostname**  string | Configure the device hostname parameter. This option takes an ASCII string value. |
| **lookup_source**  list / elements=any | Provides one or more source interfaces to use for performing DNS lookups. The interface provided in `lookup_source` can only exist in a single VRF. This argument accepts either a list of interface names or a list of hashes that configure the interface name and VRF name. See examples. |
| **name_servers**  list / elements=string | List of DNS name servers by IP address to use to perform name resolution lookups. This argument accepts either a list of DNS servers or a list of hashes that configure the name server and VRF name. See examples. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  Starting with Ansible 2.6 we recommend using `connection: httpapi` for eAPI.  This option will be removed in a release after 2022-06-01.  For more information please see the [EOS Platform Options guide](../network/user_guide/platform_eos.md).   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This is a common argument used for either *cli* or *eapi* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. This value applies to either *cli* or *eapi*.  The port value will default to the appropriate transport common port if none is provided in the task (cli=22, http=80, https=443).  Default: `0` |
| **ssh_keyfile**  path | Specifies the SSH keyfile to use to authenticate the connection to the remote device. This argument is only used for *cli* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` ← (default) - `"eapi"` |
| **use_proxy**  boolean | If `no`, the environment variables `http_proxy` and `https_proxy` will be ignored.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | Configures the *transport* to use SSL if set to `yes` only when the `transport=eapi`. If the transport argument is not eapi, this value is ignored.  Choices:   - `false` - `true` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate either the CLI login or the eAPI authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates. If the transport argument is not eapi, this value is ignored.  Choices:   - `false` - `true` ← (default) |
| **state**  string | State of the configuration values in the device’s current active configuration. When set to *present*, the values should be configured in the device active configuration and when set to *absent* the values should not be in the device active configuration  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](eos_system_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - For information on using CLI, eAPI and privileged mode see the :ref:`EOS Platform Options guide <eos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Arista EOS devices see the `Arista integration page <<https://www.ansible.com/ansible-arista-networks>>`_.

## [Examples](eos_system_module.md#id4)

```yaml+jinja
- name: configure hostname and domain-name
  arista.eos.eos_system:
    hostname: eos01
    domain_name: test.example.com

- name: remove configuration
  arista.eos.eos_system:
    state: absent

- name: configure DNS lookup sources
  arista.eos.eos_system:
    lookup_source: Management1

- name: configure DNS lookup sources with VRF support
  arista.eos.eos_system:
    lookup_source:
    - interface: Management1
      vrf: mgmt
    - interface: Ethernet1
      vrf: myvrf

- name: configure name servers
  arista.eos.eos_system:
    name_servers:
    - 8.8.8.8
    - 8.8.4.4

- name: configure name servers with VRF support
  arista.eos.eos_system:
    name_servers:
    - {server: 8.8.8.8, vrf: mgmt}
    - {server: 8.8.4.4, vrf: mgmt}
```

## [Return Values](eos_system_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["hostname eos01", "dns domain test.example.com"]` |
| **session_name**  string | The EOS config session name used to load the configuration  Returned: changed  Sample: `"ansible_1479315771"` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
