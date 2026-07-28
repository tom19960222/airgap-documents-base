---
collection: ansible
version: "8"
title: "ansible.netcommon.net_put module – Copy a file from Ansible Controller to a network device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/net_put_module.html
fetched_at: 2026-07-28T01:09:08+00:00
---
# ansible.netcommon.net_put module – Copy a file from Ansible Controller to a network device

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
> You need further requirements to be able to use this module,
> see [Requirements](net_put_module.md#ansible-collections-ansible-netcommon-net-put-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.netcommon.net_put`.

New in ansible.netcommon 1.0.0

- [Synopsis](net_put_module.md#synopsis)
- [Requirements](net_put_module.md#requirements)
- [Parameters](net_put_module.md#parameters)
- [Notes](net_put_module.md#notes)
- [Examples](net_put_module.md#examples)

## [Synopsis](net_put_module.md#id1)

- This module provides functionality to copy file from Ansible controller to network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](net_put_module.md#id2)

The below requirements are needed on the host that executes this module.

- scp if using protocol=scp with paramiko

## [Parameters](net_put_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dest**  string | Specifies the destination file. The path to destination file can either be the full path or relative path as supported by network_os.  **Default:** `["Filename from src and at default directory of user shell on network_os."]` |
| **mode**  string | Set the file transfer mode. If mode is set to *text* then *src* file will go through Jinja2 template engine to replace any vars if present in the src file. If mode is set to *binary* then file will be copied as it is to destination device.  **Choices:**   - `"binary"` ← (default) - `"text"` |
| **protocol**  string | Protocol used to transfer file.  **Choices:**   - `"scp"` ← (default) - `"sftp"` |
| **src**  string / required | Specifies the source file. The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory. |

## [Notes](net_put_module.md#id4)

> **Note:**
>
> - Some devices need specific configurations to be enabled before scp can work These configuration should be pre-configured before using this module e.g ios - `ip scp server enable`.
> - User privilege to do scp on network device should be pre-configured e.g. ios - need user privilege 15 by default for allowing scp.
> - Default destination of source file.
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_put_module.md#id5)

```yaml+jinja
- name: copy file from ansible controller to a network device
  ansible.netcommon.net_put:
    src: running_cfg_ios1.txt

- name: copy file at root dir of flash in slot 3 of sw1(ios)
  ansible.netcommon.net_put:
    src: running_cfg_sw1.txt
    protocol: sftp
    dest: flash3:/running_cfg_sw1.txt
```

### Authors

- Deepak Agrawal (@dagrawal)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
