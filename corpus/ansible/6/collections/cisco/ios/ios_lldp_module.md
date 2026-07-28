---
collection: ansible
version: "6"
title: "cisco.ios.ios_lldp module – (deprecated, removed after 2024-06-01) Manage LLDP configuration on Cisco IOS network devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_lldp_module.html
fetched_at: 2026-07-27T16:55:18+00:00
---
# cisco.ios.ios_lldp module – (deprecated, removed after 2024-06-01) Manage LLDP configuration on Cisco IOS network devices.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/cisco/ios) (version 3.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_lldp`.

New in cisco.ios 1.0.0

- [DEPRECATED](ios_lldp_module.md#deprecated)
- [Synopsis](ios_lldp_module.md#synopsis)
- [Parameters](ios_lldp_module.md#parameters)
- [Notes](ios_lldp_module.md#notes)
- [Examples](ios_lldp_module.md#examples)
- [Return Values](ios_lldp_module.md#return-values)
- [Status](ios_lldp_module.md#status)

## [DEPRECATED](ios_lldp_module.md#id1)

Removed in:
:   major release after 2024-06-01

Why:
:   Newer and updated modules released with more functionality.

Alternative:
:   ios_lldp_global

## [Synopsis](ios_lldp_module.md#id2)

- This module provides declarative management of LLDP service on Cisco IOS network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_lldp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **state**  string | State of the LLDP configuration. If value is *present* lldp will be enabled else if it is *absent* it will be disabled.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |

## [Notes](ios_lldp_module.md#id4)

> **Note:**
>
> - Tested against IOS 15.2
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_lldp_module.md#id5)

```yaml+jinja
- name: Enable LLDP service
  cisco.ios.ios_lldp:
    state: present

- name: Disable LLDP service
  cisco.ios.ios_lldp:
    state: absent
```

## [Return Values](ios_lldp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["lldp run"]` |

## [Status](ios_lldp_module.md#id7)

- This module will be removed in a major release after 2024-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](ios_lldp_module.md#deprecated).

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
