---
collection: ansible
version: "6"
title: "cisco.ios.ios_system module – Module to manage the system attributes."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_system_module.html
fetched_at: 2026-07-27T16:55:30+00:00
---
# cisco.ios.ios_system module – Module to manage the system attributes.

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
> To use it in a playbook, specify: `cisco.ios.ios_system`.

New in cisco.ios 1.0.0

- [Synopsis](ios_system_module.md#synopsis)
- [Parameters](ios_system_module.md#parameters)
- [Notes](ios_system_module.md#notes)
- [Examples](ios_system_module.md#examples)
- [Return Values](ios_system_module.md#return-values)

## [Synopsis](ios_system_module.md#id1)

- This module provides declarative management of node system attributes on Cisco IOS devices. It provides an option to configure host system parameters or remove those parameters from the device active configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_system_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain_name**  list / elements=any | Configure the IP domain name on the remote device to the provided value. Value should be in the dotted name form and will be appended to the `hostname` to create a fully-qualified domain name. |
| **domain_search**  list / elements=any | Provides the list of domain suffixes to append to the hostname for the purpose of doing name resolution. This argument accepts a list of names and will be reconciled with the current active configuration on the running node. |
| **hostname**  string | Configure the device hostname parameter. This option takes an ASCII string value. |
| **lookup_enabled**  boolean | Administrative control for enabling or disabling DNS lookups. When this argument is set to True, lookups are performed and when it is set to False, lookups are not performed.  Choices:   - `false` - `true` |
| **lookup_source**  string | Provides one or more source interfaces to use for performing DNS lookups. The interface provided in `lookup_source` must be a valid interface configured on the device. |
| **name_servers**  list / elements=any | List of DNS name servers by IP address to use to perform name resolution lookups. This argument accepts either a list of DNS servers See examples. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **state**  string | State of the configuration values in the device’s current active configuration. When set to *present*, the values should be configured in the device active configuration and when set to *absent* the values should not be in the device active configuration  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](ios_system_module.md#id3)

> **Note:**
>
> - Tested against IOS 15.6
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_system_module.md#id4)

```yaml+jinja
- name: configure hostname and domain name
  cisco.ios.ios_system:
    hostname: ios01
    domain_name: test.example.com
    domain_search:
    - ansible.com
    - redhat.com
    - cisco.com

- name: remove configuration
  cisco.ios.ios_system:
    state: absent

- name: configure DNS lookup sources
  cisco.ios.ios_system:
    lookup_source: MgmtEth0/0/CPU0/0
    lookup_enabled: yes

- name: configure name servers
  cisco.ios.ios_system:
    name_servers:
    - 8.8.8.8
    - 8.8.4.4
```

## [Return Values](ios_system_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["hostname ios01", "ip domain name test.example.com"]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
