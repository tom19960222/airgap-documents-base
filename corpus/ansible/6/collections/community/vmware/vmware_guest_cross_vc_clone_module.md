---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_cross_vc_clone module – Cross-vCenter VM/template clone"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_cross_vc_clone_module.html
fetched_at: 2026-07-27T17:21:51+00:00
---
# community.vmware.vmware_guest_cross_vc_clone module – Cross-vCenter VM/template clone

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_cross_vc_clone`.

- [Synopsis](vmware_guest_cross_vc_clone_module.md#synopsis)
- [Parameters](vmware_guest_cross_vc_clone_module.md#parameters)
- [Notes](vmware_guest_cross_vc_clone_module.md#notes)
- [Examples](vmware_guest_cross_vc_clone_module.md#examples)
- [Return Values](vmware_guest_cross_vc_clone_module.md#return-values)

## [Synopsis](vmware_guest_cross_vc_clone_module.md#id1)

- This module can be used for Cross-vCenter vm/template clone

## [Parameters](vmware_guest_cross_vc_clone_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **destination_datastore**  string / required | The name of the destination datastore or the datastore cluster.  If datastore cluster name is specified, we will find the Storage DRS recommended datastore in that cluster. |
| **destination_host**  string / required | The name of the destination host. |
| **destination_resource_pool**  string | Destination resource pool.  If not provided, the destination host’s parent’s resource pool will be used. |
| **destination_vcenter**  string / required | The hostname or IP address of the destination VCenter. |
| **destination_vcenter_password**  string / required | The password of the destination VCenter. |
| **destination_vcenter_port**  integer | The port to establish connection in the destination VCenter.  Default: `443` |
| **destination_vcenter_username**  string / required | The username of the destination VCenter. |
| **destination_vcenter_validate_certs**  boolean | Parameter to indicate if certification validation needs to be done on destination VCenter.  Choices:   - `false` ← (default) - `true` |
| **destination_vm_folder**  string / required | Destination folder, absolute path to deploy the cloned vm.  This parameter is case sensitive.  Examples:  folder: vm  folder: ha-datacenter/vm  folder: /datacenter1/vm |
| **destination_vm_name**  string / required | The name of the cloned VM. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **is_template**  boolean  added in community.vmware 1.16.0 | Specifies whether or not the new virtual machine should be marked as a template.  Choices:   - `false` ← (default) - `true` |
| **moid**  string | Managed Object ID of the vm/template instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine or template.  This is a required parameter, if parameter `uuid` or `moid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | The state of Virtual Machine deployed.  If set to `present` and VM does not exists, then VM is created.  If set to `present` and VM exists, no action is taken.  If set to `poweredon` and VM does not exists, then VM is created with powered on state.  If set to `poweredon` and VM exists, no action is taken.  Choices:   - `"present"` ← (default) - `"poweredon"` |
| **use_instance_uuid**  boolean | Whether to use the VMware instance UUID rather than the BIOS UUID.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the vm/template instance to clone from, this is VMware’s unique identifier.  This is a required parameter, if parameter `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_guest_cross_vc_clone_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_cross_vc_clone_module.md#id4)

```yaml+jinja
# Clone template
- name: clone a template across VC
  community.vmware.vmware_guest_cross_vc_clone:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    name: "test_vm1"
    destination_vm_name: "cloned_vm_from_template"
    destination_vcenter: '{{ destination_vcenter_hostname }}'
    destination_vcenter_username: '{{ destination_vcenter_username }}'
    destination_vcenter_password: '{{ destination_vcenter_password }}'
    destination_vcenter_port: '{{ destination_vcenter_port }}'
    destination_vcenter_validate_certs: '{{ destination_vcenter_validate_certs }}'
    destination_host: '{{ destination_esxi }}'
    destination_datastore: '{{ destination_datastore }}'
    destination_vm_folder: '{{ destination_vm_folder }}'
    state: present
  register: cross_vc_clone_from_template

- name: clone a VM across VC
  community.vmware.vmware_guest_cross_vc_clone:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: "{{ vcenter_password }}"
    name: "test_vm1"
    destination_vm_name: "cloned_vm_from_vm"
    destination_vcenter: '{{ destination_vcenter_hostname }}'
    destination_vcenter_username: '{{ destination_vcenter_username }}'
    destination_vcenter_password: '{{ destination_vcenter_password }}'
    destination_host: '{{ destination_esxi }}'
    destination_datastore: '{{ destination_datastore }}'
    destination_vm_folder: '{{ destination_vm_folder }}'
    state: poweredon
  register: cross_vc_clone_from_vm

- name: check_mode support
  community.vmware.vmware_guest_cross_vc_clone:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: "{{ vcenter_password }}"
    name: "test_vm1"
    destination_vm_name: "cloned_vm_from_vm"
    destination_vcenter: '{{ destination_vcenter_hostname }}'
    destination_vcenter_username: '{{ destination_vcenter_username }}'
    destination_vcenter_password: '{{ destination_vcenter_password }}'
    destination_host: '{{ destination_esxi }}'
    destination_datastore: '{{ destination_datastore }}'
    destination_vm_folder: '{{ destination_vm_folder }}'
  check_mode: true
```

## [Return Values](vmware_guest_cross_vc_clone_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vm_info**  dictionary | metadata about the virtual machine  Returned: always  Sample: `{"datastore": "", "host": "", "power_on": "", "vcenter": "", "vm_folder": "", "vm_name": ""}` |

### Authors

- Anusha Hegde (@anusha94)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
