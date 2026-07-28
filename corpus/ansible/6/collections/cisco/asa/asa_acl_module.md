---
collection: ansible
version: "6"
title: "cisco.asa.asa_acl module – (deprecated, removed after 2022-06-01) Manage access-lists on a Cisco ASA"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/asa/asa_acl_module.html
fetched_at: 2026-07-27T16:50:45+00:00
---
# cisco.asa.asa_acl module – (deprecated, removed after 2022-06-01) Manage access-lists on a Cisco ASA

> **Note:**
>
> This module is part of the [cisco.asa collection](https://galaxy.ansible.com/cisco/asa) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.asa`.
>
> To use it in a playbook, specify: `cisco.asa.asa_acl`.

New in cisco.asa 1.0.0

- [DEPRECATED](asa_acl_module.md#deprecated)
- [Synopsis](asa_acl_module.md#synopsis)
- [Parameters](asa_acl_module.md#parameters)
- [Notes](asa_acl_module.md#notes)
- [Examples](asa_acl_module.md#examples)
- [Return Values](asa_acl_module.md#return-values)
- [Status](asa_acl_module.md#status)

## [DEPRECATED](asa_acl_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Newer and updated modules released with more functionality in Ansible 2.10

Alternative:
:   asa_acls

## [Synopsis](asa_acl_module.md#id2)

- This module allows you to work with access-lists on a Cisco ASA device.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](asa_acl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **after**  list / elements=string | The ordered set of commands to append to the end of the command stack if a changed needs to be made. Just like with *before* this allows the playbook designer to append a set of commands to be executed after the command set. |
| **authorize**  boolean | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` and `become: yes`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` - `true` |
| **before**  list / elements=string | The ordered set of commands to push on to the command stack if a change needs to be made. This allows the playbook designer the opportunity to perform configuration commands prior to pushing any changes without affecting how the set of commands are matched against the system. |
| **config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *config* argument allows the implementer to pass in the configuration to use as the base config for comparison. |
| **context**  string | Specifies which context to target if you are running in the ASA in multiple context mode. Defaults to the current context you login to. |
| **force**  boolean | The force argument instructs the module to not consider the current devices running-config. When set to true, this will cause the module to push the contents of *src* into the device without first checking if already configured.  Choices:   - `false` ← (default) - `true` |
| **lines**  aliases: commands  list / elements=string / required | The ordered set of commands that should be configured in the section. The commands must be the exact same commands as found in the device running-config. Be sure to note the configuration command syntax as some commands are automatically modified by the device config parser. |
| **match**  string | Instructs the module on the way to perform the matching of the set of commands against the current device config. If match is set to *line*, commands are matched line by line. If match is set to *strict*, command lines are matched with respect to position. Finally if match is set to *exact*, command lines must be an equal match.  Choices:   - `"line"` ← (default) - `"strict"` - `"exact"` |
| **passwords**  boolean | Saves running-config passwords in clear-text when set to True. Defaults to False  Choices:   - `false` - `true` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies idle timeout in seconds for the connection, in seconds. Useful if the console freezes before continuing. For example when saving configurations. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **replace**  string | Instructs the module on the way to perform the configuration on the device. If the replace argument is set to *line* then the modified lines are pushed to the device in configuration mode. If the replace argument is set to *block* then the entire command block is pushed to the device in configuration mode if any line is not correct.  Choices:   - `"line"` ← (default) - `"block"` |

## [Notes](asa_acl_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](asa_acl_module.md#id5)

```yaml+jinja
- cisco.asa.asa_acl:
    lines:
    - access-list ACL-ANSIBLE extended permit tcp any any eq 82
    - access-list ACL-ANSIBLE extended permit tcp any any eq www
    - access-list ACL-ANSIBLE extended permit tcp any any eq 97
    - access-list ACL-ANSIBLE extended permit tcp any any eq 98
    - access-list ACL-ANSIBLE extended permit tcp any any eq 99
    before: clear configure access-list ACL-ANSIBLE
    match: strict
    replace: block
    provider: '{{ cli }}'

- cisco.asa.asa_acl:
    lines:
    - access-list ACL-OUTSIDE extended permit tcp any any eq www
    - access-list ACL-OUTSIDE extended permit tcp any any eq https
    context: customer_a
    provider: '{{ cli }}'
```

## [Return Values](asa_acl_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **updates**  list / elements=string | The set of commands that will be pushed to the remote device  Returned: always  Sample: `["access-list ACL-OUTSIDE extended permit tcp any any eq www"]` |

## [Status](asa_acl_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](asa_acl_module.md#deprecated).

### Authors

- Patrick Ogenstad (@ogenstad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.asa/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.asa)
