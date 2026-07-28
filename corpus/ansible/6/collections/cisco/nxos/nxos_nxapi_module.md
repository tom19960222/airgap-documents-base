---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_nxapi module – Manage NXAPI configuration on an NXOS device."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_nxapi_module.html
fetched_at: 2026-07-27T17:02:08+00:00
---
# cisco.nxos.nxos_nxapi module – Manage NXAPI configuration on an NXOS device.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_nxapi`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_nxapi_module.md#synopsis)
- [Parameters](nxos_nxapi_module.md#parameters)
- [Notes](nxos_nxapi_module.md#notes)
- [Examples](nxos_nxapi_module.md#examples)
- [Return Values](nxos_nxapi_module.md#return-values)

## [Synopsis](nxos_nxapi_module.md#id1)

- Configures the NXAPI feature on devices running Cisco NXOS. The NXAPI feature is absent from the configuration by default. Since this module manages the NXAPI feature it only supports the use of the `Cli` transport.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_nxapi_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **http**  aliases: enable_http  boolean | Controls the operating state of the HTTP protocol as one of the underlying transports for NXAPI. By default, NXAPI will enable the HTTP transport when the feature is first configured. To disable the use of the HTTP transport, set the value of this argument to False.  Choices:   - `false` - `true` ← (default) |
| **http_port**  integer | Configure the port with which the HTTP server will listen on for requests. By default, NXAPI will bind the HTTP service to the standard HTTP port 80. This argument accepts valid port values in the range of 1 to 65535.  Default: `80` |
| **https**  aliases: enable_https  boolean | Controls the operating state of the HTTPS protocol as one of the underlying transports for NXAPI. By default, NXAPI will disable the HTTPS transport when the feature is first configured. To enable the use of the HTTPS transport, set the value of this argument to True.  Choices:   - `false` ← (default) - `true` |
| **https_port**  integer | Configure the port with which the HTTPS server will listen on for requests. By default, NXAPI will bind the HTTPS service to the standard HTTPS port 443. This argument accepts valid port values in the range of 1 to 65535.  Default: `443` |
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
| **sandbox**  aliases: enable_sandbox  boolean | The NXAPI feature provides a web base UI for developers for entering commands. This feature is initially disabled when the NXAPI feature is configured for the first time. When the `sandbox` argument is set to True, the developer sandbox URL will accept requests and when the value is set to False, the sandbox URL is unavailable. This is supported on NX-OS 7K series.  Choices:   - `false` - `true` |
| **ssl_strong_ciphers**  boolean | Controls the use of whether strong or weak ciphers are configured. By default, this feature is disabled and weak ciphers are configured. To enable the use of strong ciphers, set the value of this argument to True.  Choices:   - `false` ← (default) - `true` |
| **state**  string | The `state` argument controls whether or not the NXAPI feature is configured on the remote device. When the value is `present` the NXAPI feature configuration is present in the device running-config. When the values is `absent` the feature configuration is removed from the running-config.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tlsv1_0**  boolean | Controls the use of the Transport Layer Security version 1.0 is configured. By default, this feature is enabled. To disable the use of TLSV1.0, set the value of this argument to True.  Choices:   - `false` - `true` ← (default) |
| **tlsv1_1**  boolean | Controls the use of the Transport Layer Security version 1.1 is configured. By default, this feature is disabled. To enable the use of TLSV1.1, set the value of this argument to True.  Choices:   - `false` ← (default) - `true` |
| **tlsv1_2**  boolean | Controls the use of the Transport Layer Security version 1.2 is configured. By default, this feature is disabled. To enable the use of TLSV1.2, set the value of this argument to True.  Choices:   - `false` ← (default) - `true` |

## [Notes](nxos_nxapi_module.md#id3)

> **Note:**
>
> - Limited Support for Cisco MDS
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_nxapi_module.md#id4)

```yaml+jinja
- name: Enable NXAPI access with default configuration
  cisco.nxos.nxos_nxapi:
    state: present

- name: Enable NXAPI with no HTTP, HTTPS at port 9443 and sandbox disabled
  cisco.nxos.nxos_nxapi:
    enable_http: false
    https_port: 9443
    https: yes
    enable_sandbox: no

- name: remove NXAPI configuration
  cisco.nxos.nxos_nxapi:
    state: absent
```

## [Return Values](nxos_nxapi_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **updates**  list / elements=string | Returns the list of commands that need to be pushed into the remote device to satisfy the arguments  Returned: always  Sample: `["no feature nxapi"]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
