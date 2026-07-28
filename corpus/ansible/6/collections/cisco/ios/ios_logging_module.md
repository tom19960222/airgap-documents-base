---
collection: ansible
version: "6"
title: "cisco.ios.ios_logging module – (deprecated, removed after 2023-06-01) Manage logging on network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_logging_module.html
fetched_at: 2026-07-27T16:55:20+00:00
---
# cisco.ios.ios_logging module – (deprecated, removed after 2023-06-01) Manage logging on network devices

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
> To use it in a playbook, specify: `cisco.ios.ios_logging`.

New in cisco.ios 1.0.0

- [DEPRECATED](ios_logging_module.md#deprecated)
- [Synopsis](ios_logging_module.md#synopsis)
- [Parameters](ios_logging_module.md#parameters)
- [Notes](ios_logging_module.md#notes)
- [Examples](ios_logging_module.md#examples)
- [Return Values](ios_logging_module.md#return-values)
- [Status](ios_logging_module.md#status)

## [DEPRECATED](ios_logging_module.md#id1)

Removed in:
:   major release after 2023-06-01

Why:
:   Newer and updated modules released with more functionality.

Alternative:
:   ios_logging_global

## [Synopsis](ios_logging_module.md#id2)

- This module provides declarative management of logging on Cisco Ios devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_logging_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of logging definitions. |
| **dest**  string | Destination of the logs.  On dest has to be quoted as ‘on’ or else pyyaml will convert to True before it gets to Ansible.  Choices:   - `"on"` - `"host"` - `"console"` - `"monitor"` - `"buffered"` - `"trap"` |
| **facility**  string | Set logging facility. |
| **level**  string | Set logging severity levels.  Choices:   - `"emergencies"` - `"alerts"` - `"critical"` - `"errors"` - `"warnings"` - `"notifications"` - `"informational"` - `"debugging"` |
| **name**  string | The hostname or IP address of the destination.  Required when *dest=host*. |
| **size**  integer | Size of buffer. The acceptable value is in range from 4096 to 4294967295 bytes. |
| **state**  string | State of the logging configuration.  Choices:   - `"present"` - `"absent"` |
| **dest**  string | Destination of the logs.  On dest has to be quoted as ‘on’ or else pyyaml will convert to True before it gets to Ansible.  Choices:   - `"on"` - `"host"` - `"console"` - `"monitor"` - `"buffered"` - `"trap"` |
| **facility**  string | Set logging facility. |
| **level**  string | Set logging severity levels.  Choices:   - `"emergencies"` - `"alerts"` - `"critical"` - `"errors"` - `"warnings"` - `"notifications"` - `"informational"` - `"debugging"` ← (default) |
| **name**  string | The hostname or IP address of the destination.  Required when *dest=host*. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **size**  integer | Size of buffer. The acceptable value is in range from 4096 to 4294967295 bytes. |
| **state**  string | State of the logging configuration.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](ios_logging_module.md#id4)

> **Note:**
>
> - Tested against IOS 15.6
> - The ‘Default System Message Logging Configuration’ of the ios device like facility Local7 or logging on is not subjected to idempotency causes
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_logging_module.md#id5)

```yaml+jinja
- name: configure host logging
  cisco.ios.ios_logging:
    dest: host
    name: 172.16.0.1
    state: present

- name: remove host logging configuration
  cisco.ios.ios_logging:
    dest: host
    name: 172.16.0.1
    state: absent

- name: configure console logging level and facility
  cisco.ios.ios_logging:
    dest: console
    facility: local7
    level: debugging
    state: present

- name: enable logging to all
  cisco.ios.ios_logging:
    dest: on

- name: configure buffer size
  cisco.ios.ios_logging:
    dest: buffered
    size: 5000

- name: Configure logging using aggregate
  cisco.ios.ios_logging:
    aggregate:
    - {dest: console, level: notifications}
    - {dest: buffered, size: 9000}

- name: remove logging using aggregate
  cisco.ios.ios_logging:
    aggregate:
    - {dest: console, level: notifications}
    - {dest: buffered, size: 9000}
    state: absent
```

## [Return Values](ios_logging_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["logging facility local7", "logging host 172.16.0.1"]` |

## [Status](ios_logging_module.md#id7)

- This module will be removed in a major release after 2023-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](ios_logging_module.md#deprecated).

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
