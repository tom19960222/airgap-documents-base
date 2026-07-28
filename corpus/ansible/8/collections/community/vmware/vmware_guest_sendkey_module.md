---
collection: ansible
version: "8"
title: "community.vmware.vmware_guest_sendkey module – Send USB HID codes to the Virtual Machine’s keyboard."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_guest_sendkey_module.html
fetched_at: 2026-07-28T02:00:20+00:00
---
# community.vmware.vmware_guest_sendkey module – Send USB HID codes to the Virtual Machine’s keyboard.

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_guest_sendkey`.

- [Synopsis](vmware_guest_sendkey_module.md#synopsis)
- [Parameters](vmware_guest_sendkey_module.md#parameters)
- [Notes](vmware_guest_sendkey_module.md#notes)
- [Examples](vmware_guest_sendkey_module.md#examples)
- [Return Values](vmware_guest_sendkey_module.md#return-values)

## [Synopsis](vmware_guest_sendkey_module.md#id1)

- This module is used to send keystrokes to given virtual machine.
- All parameters and VMware object names are case sensitive.

## [Parameters](vmware_guest_sendkey_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | The name of cluster where the virtual machine is running.  This is a required parameter, if `esxi_hostname` is not set.  `esxi_hostname` and `cluster` are mutually exclusive parameters. |
| **datacenter**  string | The datacenter name to which virtual machine belongs to. |
| **esxi_hostname**  string | The ESXi hostname where the virtual machine is running.  This is a required parameter, if `cluster` is not set.  `esxi_hostname` and `cluster` are mutually exclusive parameters. |
| **folder**  string | Destination folder, absolute or relative path to find an existing guest.  This is a required parameter, only if multiple VMs are found with same name.  The folder should include the datacenter. ESXi server’s datacenter is ha-datacenter.  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **keys_send**  list / elements=string | The list of the keys will be sent to the virtual machine.  Valid values are `ENTER`, `ESC`, `BACKSPACE`, `TAB`, `SPACE`, `CAPSLOCK`, `HOME`, `DELETE`, `END`, `CTRL_ALT_DEL`, `CTRL_C`, `CTRL_X` and `F1` to `F12`, `RIGHTARROW`, `LEFTARROW`, `DOWNARROW`, `UPARROW`.  If both `keys_send` and `string_send` are specified, keys in `keys_send` list will be sent in front of the `string_send`.  Values `HOME` and `END` are added in version 1.17.0.  **Default:** `[]` |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine.  This is a required parameter, if parameter `uuid` or `moid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **sleep_time**  integer | Sleep time in seconds between two keys or string sent to the virtual machine.  API is faster than actual key or string send to virtual machine, this parameter allow to control delay between keys and/or strings.  **Default:** `0` |
| **string_send**  string | The string will be sent to the virtual machine.  This string can contain valid special character, alphabet and digit on the keyboard. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the instance to gather facts if known, this is VMware’s unique identifier.  This is a required parameter, if parameter `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_guest_sendkey_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_sendkey_module.md#id4)

```yaml+jinja
- name: Send list of keys to virtual machine
  community.vmware.vmware_guest_sendkey:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "{{ folder_name }}"
    name: "{{ vm_name }}"
    keys_send:
      - TAB
      - TAB
      - ENTER
  delegate_to: localhost
  register: keys_num_sent

- name: Send list of keys to virtual machine using MoID
  community.vmware.vmware_guest_sendkey:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "{{ folder_name }}"
    moid: vm-42
    keys_send:
      - CTRL_ALT_DEL
  delegate_to: localhost
  register: ctrl_alt_del_sent

- name: Send a string to virtual machine
  community.vmware.vmware_guest_sendkey:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    folder: "{{ folder_name }}"
    name: "{{ vm_name }}"
    string_send: "user_logon"
  delegate_to: localhost
  register: keys_num_sent
```

## [Return Values](vmware_guest_sendkey_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **sendkey_info**  dictionary | display the keys and the number of keys sent to the virtual machine  **Returned:** always  **Sample:** `{"keys_send": ["SPACE", "DOWNARROW", "DOWNARROW", "ENTER"], "keys_send_number": 4, "returned_keys_send_number": 4, "string_send": null, "virtual_machine": "test_vm"}` |

### Authors

- Diane Wang (@Tomorrow9)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
