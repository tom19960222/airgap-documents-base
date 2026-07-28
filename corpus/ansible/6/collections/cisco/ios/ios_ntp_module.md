---
collection: ansible
version: "6"
title: "cisco.ios.ios_ntp module – (deprecated, removed after 2024-01-01) Manages core NTP configuration."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_ntp_module.html
fetched_at: 2026-07-27T16:55:22+00:00
---
# cisco.ios.ios_ntp module – (deprecated, removed after 2024-01-01) Manages core NTP configuration.

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
> To use it in a playbook, specify: `cisco.ios.ios_ntp`.

New in cisco.ios 1.0.0

- [DEPRECATED](ios_ntp_module.md#deprecated)
- [Synopsis](ios_ntp_module.md#synopsis)
- [Parameters](ios_ntp_module.md#parameters)
- [Notes](ios_ntp_module.md#notes)
- [Examples](ios_ntp_module.md#examples)
- [Return Values](ios_ntp_module.md#return-values)
- [Status](ios_ntp_module.md#status)

## [DEPRECATED](ios_ntp_module.md#id1)

Removed in:
:   major release after 2024-01-01

Why:
:   Updated module released with more functionality.

Alternative:
:   ios_ntp_global

## [Synopsis](ios_ntp_module.md#id2)

- Manages core NTP configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_ntp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **acl**  string | ACL for peer/server access restricition. |
| **auth**  boolean | Enable NTP authentication. Data type boolean.  Choices:   - `false` ← (default) - `true` |
| **auth_key**  string | md5 NTP authentication key of tye 7. |
| **key_id**  string | auth_key id. Data type string |
| **logging**  boolean | Enable NTP logs. Data type boolean.  Choices:   - `false` ← (default) - `true` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **server**  string | Network address of NTP server. |
| **source_int**  string | Source interface for NTP packets. |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vrf**  string | VRF configuration for NTP servers |

## [Notes](ios_ntp_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_ntp_module.md#id5)

```yaml+jinja
# Set new NTP server and source interface
- cisco.ios.ios_ntp:
    server: 10.0.255.10
    source_int: Loopback0
    logging: false
    state: present
# Remove NTP ACL and logging
- cisco.ios.ios_ntp:
    acl: NTP_ACL
    logging: true
    state: absent
# Set NTP authentication
- cisco.ios.ios_ntp:
    key_id: 10
    auth_key: 15435A030726242723273C21181319000A
    auth: true
    state: present
# Set new NTP configuration
- cisco.ios.ios_ntp:
    server: 10.0.255.10
    source_int: Loopback0
    acl: NTP_ACL
    logging: true
    vrf: mgmt
    key_id: 10
    auth_key: 15435A030726242723273C21181319000A
    auth: true
    state: present
```

## [Return Values](ios_ntp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | command sent to the device  Returned: always  Sample: `["no ntp server 10.0.255.10", "no ntp source Loopback0"]` |

## [Status](ios_ntp_module.md#id7)

- This module will be removed in a major release after 2024-01-01.
  *[deprecated]*
- For more information see [DEPRECATED](ios_ntp_module.md#deprecated).

### Authors

- Federico Olivieri (@Federico87)
- Joanie Sylvain (@JoanieAda)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
