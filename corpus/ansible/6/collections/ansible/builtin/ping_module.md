---
collection: ansible
version: "6"
title: "ansible.builtin.ping module – Try to connect to host, verify a usable python and return pong on success"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/ping_module.html
fetched_at: 2026-07-27T16:44:05+00:00
---
# ansible.builtin.ping module – Try to connect to host, verify a usable python and return `pong` on success

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `ping` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](ping_module.md#synopsis)
- [Parameters](ping_module.md#parameters)
- [Attributes](ping_module.md#attributes)
- [See Also](ping_module.md#see-also)
- [Examples](ping_module.md#examples)
- [Return Values](ping_module.md#return-values)

## [Synopsis](ping_module.md#id1)

- A trivial test module, this module always returns `pong` on successful contact. It does not make sense in playbooks, but it is useful from `/usr/bin/ansible` to verify the ability to login and that a usable Python is configured.
- This is NOT ICMP ping, this is just a trivial test module that requires Python on the remote-node.
- For Windows targets, use the [ansible.windows.win_ping](../windows/win_ping_module.md#ansible-collections-ansible-windows-win-ping-module) module instead.
- For Network targets, use the [ansible.netcommon.net_ping](../netcommon/net_ping_module.md#ansible-collections-ansible-netcommon-net-ping-module) module instead.

## [Parameters](ping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **data**  string | Data to return for the `ping` return value.  If this parameter is set to `crash`, the module will cause an exception.  Default: `"pong"` |

## [Attributes](ping_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platform: posix | Target OS/families that can be operated against |

## [See Also](ping_module.md#id4)

> **See also:**
>
> [ansible.netcommon.net_ping](../netcommon/net_ping_module.md#ansible-collections-ansible-netcommon-net-ping-module)
> :   Tests reachability using ping from a network device.
>
> [ansible.windows.win_ping](../windows/win_ping_module.md#ansible-collections-ansible-windows-win-ping-module)
> :   A windows version of the classic ping module.

## [Examples](ping_module.md#id5)

```yaml+jinja
# Test we can logon to 'webservers' and execute python with json lib.
# ansible webservers -m ansible.builtin.ping

- name: Example from an Ansible Playbook
  ansible.builtin.ping:

- name: Induce an exception to see what happens
  ansible.builtin.ping:
    data: crash
```

## [Return Values](ping_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ping**  string | Value provided with the data parameter.  Returned: success  Sample: `"pong"` |

### Authors

- Ansible Core Team
- Michael DeHaan

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
