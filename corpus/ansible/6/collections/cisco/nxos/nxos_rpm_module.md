---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_rpm module – Install patch or feature rpms on Cisco NX-OS devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_rpm_module.html
fetched_at: 2026-07-27T17:02:19+00:00
---
# cisco.nxos.nxos_rpm module – Install patch or feature rpms on Cisco NX-OS devices.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_rpm`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_rpm_module.md#synopsis)
- [Parameters](nxos_rpm_module.md#parameters)
- [Notes](nxos_rpm_module.md#notes)
- [Examples](nxos_rpm_module.md#examples)
- [Return Values](nxos_rpm_module.md#return-values)

## [Synopsis](nxos_rpm_module.md#id1)

- Install software maintenance upgrade (smu) RPMS and 3rd party RPMS on Cisco NX-OS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_rpm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of RPM/patch definitions. |
| **file_system**  string | The remote file system of the device. If omitted, devices that support a file_system parameter will use their default values. |
| **pkg**  string / required | Name of the RPM package. |
| **state**  string | If the state is present, the rpm will be installed, If the state is absent, it will be removed.  Choices:   - `"present"` - `"absent"` |
| **file_system**  string | The remote file system of the device. If omitted, devices that support a file_system parameter will use their default values.  Default: `"bootflash"` |
| **pkg**  string | Name of the RPM package. |
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
| **state**  string | If the state is present, the rpm will be installed, If the state is absent, it will be removed.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](nxos_rpm_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.0(3)I2(5), 7.0(3)I4(6), 7.0(3)I5(3), 7.0(3)I6(1), 7.0(3)I7(3)
> - Unsupported for Cisco MDS
> - For patches, the minimum platform version needed is 7.0(3)I2(5)
> - For feature rpms, the minimum platform version needed is 7.0(3)I6(1)
> - The module manages the entire RPM lifecycle (Add, activate, commit, deactivate, remove)
> - For reload patches, this module is NOT idempotent until the patch is committed.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_rpm_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_rpm:
    pkg: nxos.sample-n9k_ALL-1.0.0-7.0.3.I7.3.lib32_n9000.rpm
```

## [Return Values](nxos_rpm_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  Returned: always  Sample: `["install add bootflash:nxos.sample-n9k_ALL-1.0.0-7.0.3.I7.3.lib32_n9000.rpm forced", "install activate nxos.sample-n9k_ALL-1.0.0-7.0.3.I7.3.lib32_n9000 forced", "install commit nxos.sample-n9k_ALL-1.0.0-7.0.3.I7.3.lib32_n9000"]` |

### Authors

- Sai Chintalapudi (@saichint)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
