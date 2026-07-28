---
collection: ansible
version: "6"
title: "ansible.windows.win_ping module – A windows version of the classic ping module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_ping_module.html
fetched_at: 2026-07-27T16:45:00+00:00
---
# ansible.windows.win_ping module – A windows version of the classic ping module

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_ping`.

- [Synopsis](win_ping_module.md#synopsis)
- [Parameters](win_ping_module.md#parameters)
- [See Also](win_ping_module.md#see-also)
- [Examples](win_ping_module.md#examples)
- [Return Values](win_ping_module.md#return-values)

## [Synopsis](win_ping_module.md#id1)

- Checks management connectivity of a windows host.
- This is NOT ICMP ping, this is just a trivial test module.
- For non-Windows targets, use the [ansible.builtin.ping](../builtin/ping_module.md#ansible-collections-ansible-builtin-ping-module) module instead.

## [Parameters](win_ping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **data**  string | Alternate data to return instead of ‘pong’.  If this parameter is set to `crash`, the module will cause an exception.  Default: `"pong"` |

## [See Also](win_ping_module.md#id3)

> **See also:**
>
> [ansible.builtin.ping](../builtin/ping_module.md#ansible-collections-ansible-builtin-ping-module)
> :   Try to connect to host, verify a usable python and return `pong` on success.

## [Examples](win_ping_module.md#id4)

```yaml+jinja
# Test connectivity to a windows host
# ansible winserver -m ansible.windows.win_ping

- name: Example from an Ansible Playbook
  ansible.windows.win_ping:

- name: Induce an exception to see what happens
  ansible.windows.win_ping:
    data: crash
```

## [Return Values](win_ping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ping**  string | Value provided with the data parameter.  Returned: success  Sample: `"pong"` |

### Authors

- Chris Church (@cchurch)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
