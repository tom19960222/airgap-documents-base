---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_move module – Moves virtual machines in vCenter"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_move_module.html
fetched_at: 2026-07-27T17:21:58+00:00
---
# community.vmware.vmware_guest_move module – Moves virtual machines in vCenter

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_guest_move`.

- [Synopsis](vmware_guest_move_module.md#synopsis)
- [Parameters](vmware_guest_move_module.md#parameters)
- [Notes](vmware_guest_move_module.md#notes)
- [Examples](vmware_guest_move_module.md#examples)
- [Return Values](vmware_guest_move_module.md#return-values)

## [Synopsis](vmware_guest_move_module.md#id1)

- This module can be used to move virtual machines between folders.

## [Parameters](vmware_guest_move_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string / required | Destination datacenter for the move operation |
| **dest_folder**  string / required | Absolute path to move an existing guest  The dest_folder should include the datacenter. ESX’s datacenter is ha-datacenter.  This parameter is case sensitive.  Examples:  dest_folder: /ha-datacenter/vm  dest_folder: ha-datacenter/vm  dest_folder: /datacenter1/vm  dest_folder: datacenter1/vm  dest_folder: /datacenter1/vm/folder1  dest_folder: datacenter1/vm/folder1  dest_folder: /folder1/datacenter1/vm  dest_folder: folder1/datacenter1/vm  dest_folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the existing virtual machine to move.  This is required if `uuid` or `moid` is not supplied. |
| **name_match**  string | If multiple virtual machines matching the name, use the first or last found.  Choices:   - `"first"` ← (default) - `"last"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the virtual machine to manage if known, this is VMware’s unique identifier.  This is required if `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_guest_move_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_move_module.md#id4)

```yaml+jinja
- name: Move Virtual Machine
  community.vmware.vmware_guest_move:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: datacenter
    name: testvm-1
    dest_folder: "/{{ datacenter }}/vm"
  delegate_to: localhost

- name: Move Virtual Machine using MoID
  community.vmware.vmware_guest_move:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: datacenter
    moid: vm-42
    dest_folder: "/{{ datacenter }}/vm"
  delegate_to: localhost

- name: Get VM UUID
  vmware_guest_facts:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: "/{{ datacenter }}/vm"
    name: "{{ vm_name }}"
  delegate_to: localhost
  register: vm_facts

- name: Get UUID from previous task and pass it to this task
  community.vmware.vmware_guest_move:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    uuid: "{{ vm_facts.instance.hw_product_uuid }}"
    dest_folder: "/DataCenter/vm/path/to/new/folder/where/we/want"
  delegate_to: localhost
  register: facts
```

## [Return Values](vmware_guest_move_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance**  dictionary | metadata about the virtual machine  Returned: always  Sample: `{"annotation": null, "current_snapshot": null, "customvalues": {}, "guest_consolidation_needed": false, "guest_question": null, "guest_tools_status": null, "guest_tools_version": "0", "hw_cores_per_socket": 1, "hw_datastores": ["LocalDS_0"], "hw_esxi_host": "DC0_H0", "hw_eth0": {"addresstype": "generated", "ipaddresses": null, "label": "ethernet-0", "macaddress": "00:0c:29:6b:34:2c", "macaddress_dash": "00-0c-29-6b-34-2c", "summary": "DVSwitch: 43cdd1db-1ef7-4016-9bbe-d96395616199"}, "hw_files": ["[LocalDS_0] DC0_H0_VM0/DC0_H0_VM0.vmx"], "hw_folder": "/F0/DC0/vm/F0", "hw_guest_full_name": null, "hw_guest_ha_state": null, "hw_guest_id": "otherGuest", "hw_interfaces": ["eth0"], "hw_is_template": false, "hw_memtotal_mb": 32, "hw_name": "DC0_H0_VM0", "hw_power_status": "poweredOn", "hw_processor_count": 1, "hw_product_uuid": "581c2808-64fb-45ee-871f-6a745525cb29", "instance_uuid": "8bcb0b6e-3a7d-4513-bf6a-051d15344352", "ipv4": null, "ipv6": null, "module_hw": true, "snapshots": []}` |

### Authors

- Jose Angel Munoz (@imjoseangel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
