---
collection: ansible
version: "8"
title: "inspur.ispim.edit_virtual_media module – Set virtual media"
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/ispim/edit_virtual_media_module.html
fetched_at: 2026-07-28T02:37:01+00:00
---
# inspur.ispim.edit_virtual_media module – Set virtual media

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
> see [Requirements](edit_virtual_media_module.md#ansible-collections-inspur-ispim-edit-virtual-media-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.edit_virtual_media`.

New in inspur.ispim 1.0.0

- [Synopsis](edit_virtual_media_module.md#synopsis)
- [Requirements](edit_virtual_media_module.md#requirements)
- [Parameters](edit_virtual_media_module.md#parameters)
- [Notes](edit_virtual_media_module.md#notes)
- [Examples](edit_virtual_media_module.md#examples)
- [Return Values](edit_virtual_media_module.md#return-values)

## [Synopsis](edit_virtual_media_module.md#id1)

- Set virtual media on Inspur server.

## [Requirements](edit_virtual_media_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](edit_virtual_media_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **local_media_support**  string | To enable or disable Local Media Support,check or uncheck the checkbox respectively.  Only the M5 model supports this parameter.  **Choices:**   - `"Enable"` - `"Disable"` |
| **mount**  string | Whether to mount virtual media.  Only the M5 model supports this parameter.  **Choices:**   - `"Enable"` - `"Disable"` |
| **mount_type**  string | Virtual mount type.  The *FD* option is not supported in M6.  **Choices:**   - `"CD"` - `"FD"` - `"HD"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **remote_domain_name**  string | Remote Domain Name,Domain Name field is optional. |
| **remote_media_support**  string | To enable or disable Remote Media support,check or uncheck the checbox respectively.  **Choices:**   - `"Enable"` - `"Disable"` |
| **remote_password**  string | Remote Password.  Required when *remote_share_type=cifs*. |
| **remote_server_address**  string | Address of the server where the remote media images are stored. |
| **remote_share_type**  string | Share Type of the remote media server either NFS or Samba(CIFS).  **Choices:**   - `"nfs"` - `"cifs"` |
| **remote_source_path**  string | Source path to the remote media images.. |
| **remote_user_name**  string | Remote User Name.  Required when *remote_share_type=cifs*. |
| **same_settings**  integer | Same settings with CD,0 is No,1 is Yes.  Required when *mount_type=0*.  **Choices:**   - `0` - `1` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](edit_virtual_media_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](edit_virtual_media_module.md#id5)

```yaml+jinja
- name: Media test
  hosts: ism
  no_log: true
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set local media"
    inspur.ispim.edit_virtual_media:
      local_media_support: "Enable"
      provider: "{{ ism }}"

  - name: "Set remote media"
    inspur.ispim.edit_virtual_media:
      remote_media_support: "Enable"
      mount_type: 'CD'
      same_settings: 0
      mount: "Enable"
      remote_server_address: "100.2.28.203"
      remote_source_path: "/data/nfs/server/"
      remote_share_type: "nfs"
      provider: "{{ ism }}"
```

## [Return Values](edit_virtual_media_module.md#id6)

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
