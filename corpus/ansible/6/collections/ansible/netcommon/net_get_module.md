---
collection: ansible
version: "6"
title: "ansible.netcommon.net_get module – Copy a file from a network device to Ansible Controller"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_get_module.html
fetched_at: 2026-07-27T16:44:28+00:00
---
# ansible.netcommon.net_get module – Copy a file from a network device to Ansible Controller

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
> You need further requirements to be able to use this module,
> see [Requirements](net_get_module.md#ansible-collections-ansible-netcommon-net-get-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.netcommon.net_get`.

New in ansible.netcommon 1.0.0

- [Synopsis](net_get_module.md#synopsis)
- [Requirements](net_get_module.md#requirements)
- [Parameters](net_get_module.md#parameters)
- [Notes](net_get_module.md#notes)
- [Examples](net_get_module.md#examples)

## [Synopsis](net_get_module.md#id1)

- This module provides functionality to copy file from network device to ansible controller.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](net_get_module.md#id2)

The below requirements are needed on the host that executes this module.

- scp if using protocol=scp with paramiko

## [Parameters](net_get_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dest**  string | Specifies the destination file. The path to the destination file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory.  Default: `["Same filename as specified in I(src). The path will be playbook root or role root directory if playbook is part of a role."]` |
| **protocol**  string | Protocol used to transfer file.  Choices:   - `"scp"` ← (default) - `"sftp"` |
| **src**  string / required | Specifies the source file. The path to the source file can either be the full path on the network device or a relative path as per path supported by destination network device. |

## [Notes](net_get_module.md#id4)

> **Note:**
>
> - Some devices need specific configurations to be enabled before scp can work These configuration should be pre-configured before using this module e.g ios - `ip scp server enable`.
> - User privilege to do scp on network device should be pre-configured e.g. ios - need user privilege 15 by default for allowing scp.
> - Default destination of source file.
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_get_module.md#id5)

```yaml+jinja
- name: copy file from the network device to Ansible controller
  ansible.netcommon.net_get:
    src: running_cfg_ios1.txt

- name: copy file from ios to common location at /tmp
  ansible.netcommon.net_get:
    src: running_cfg_sw1.txt
    dest: /tmp/ios1.txt
```

### Authors

- Deepak Agrawal (@dagrawal)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
