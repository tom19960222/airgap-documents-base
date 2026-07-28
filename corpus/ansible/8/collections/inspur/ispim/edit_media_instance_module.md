---
collection: ansible
version: "8"
title: "inspur.ispim.edit_media_instance module – Set Virtual Media Instance"
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/ispim/edit_media_instance_module.html
fetched_at: 2026-07-28T02:36:44+00:00
---
# inspur.ispim.edit_media_instance module – Set Virtual Media Instance

> **Note:**
>
> This module is part of the [inspur.ispim collection](https://galaxy.ansible.com/ui/repo/published/inspur/ispim/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install inspur.ispim`.
> You need further requirements to be able to use this module,
> see [Requirements](edit_media_instance_module.md#ansible-collections-inspur-ispim-edit-media-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.edit_media_instance`.

New in inspur.ispim 1.0.0

- [Synopsis](edit_media_instance_module.md#synopsis)
- [Requirements](edit_media_instance_module.md#requirements)
- [Parameters](edit_media_instance_module.md#parameters)
- [Notes](edit_media_instance_module.md#notes)
- [Examples](edit_media_instance_module.md#examples)
- [Return Values](edit_media_instance_module.md#return-values)

## [Synopsis](edit_media_instance_module.md#id1)

- Set Virtual Media Instance on Inspur server.

## [Requirements](edit_media_instance_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](edit_media_instance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **kvm_num_cd**  integer | Select the number of Remote KVM CD/DVD devices that support for virtual Media redirection,  The max support number of html5 KVM is 2 and java KVM is 4.  **Choices:**   - `0` - `1` - `2` - `3` - `4` |
| **kvm_num_fd**  integer | Select the number of Remote KVM floppy devices that support for Virtual Media redirection.  **Choices:**   - `0` - `1` - `2` - `3` - `4` |
| **kvm_num_hd**  integer | Select the number of Remote KVM Hard disk devices to support for Virtual Media redirection.  **Choices:**   - `0` - `1` - `2` - `3` - `4` |
| **num_cd**  integer | Select the number of CD/DVD devices that support for Virtual Media redirection.  **Choices:**   - `0` - `1` - `2` - `3` - `4` |
| **num_fd**  integer | Select the number of floppy devices that support for Virtual Media redirection.  **Choices:**   - `0` - `1` - `2` - `3` - `4` |
| **num_hd**  integer | Select the number of harddisk devices that support for Virtual Media redirection.  **Choices:**   - `0` - `1` - `2` - `3` - `4` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **power_save_mode**  string | Check this option to enable Power Save Mode in BMC.  **Choices:**   - `"Enable"` - `"Disable"` |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **sd_media**  string | Check this option to enable SD Media support in BMC.  **Choices:**   - `"Enable"` - `"Disable"` |
| **secure_channel**  string | Check this option to enable encrypt media recirection packets.  Only the M5/M6 model supports this parameter.  **Choices:**   - `"Enable"` - `"Disable"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](edit_media_instance_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](edit_media_instance_module.md#id5)

```yaml+jinja
- name: Media instance test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set media instance"
    inspur.ispim.edit_media_instance:
      num_fd: 1
      num_cd: 1
      num_hd: 1
      kvm_num_fd: 1
      kvm_num_cd: 1
      kvm_num_hd: 1
      sd_media: "Enable"
      secure_channel: "Enable"
      power_save_mode: "Enable"
      provider: "{{ ism }}"
```

## [Return Values](edit_media_instance_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  **Returned:** always |
| **message**  string | Messages returned after module execution.  **Returned:** always |
| **state**  string | Status after module execution.  **Returned:** always |

### Authors

- WangBaoshan (@ispim)

### Collection links

- [Issue Tracker](https://github.com/ispim/inspur.ispim/issues)
- [Repository (Sources)](https://github.com/ispim/inspur.ispim)
