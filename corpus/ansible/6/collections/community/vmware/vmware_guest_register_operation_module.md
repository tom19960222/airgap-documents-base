---
collection: ansible
version: "6"
title: "community.vmware.vmware_guest_register_operation module – VM inventory registration operation"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_guest_register_operation_module.html
fetched_at: 2026-07-27T17:22:01+00:00
---
# community.vmware.vmware_guest_register_operation module – VM inventory registration operation

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
> To use it in a playbook, specify: `community.vmware.vmware_guest_register_operation`.

- [Synopsis](vmware_guest_register_operation_module.md#synopsis)
- [Parameters](vmware_guest_register_operation_module.md#parameters)
- [Notes](vmware_guest_register_operation_module.md#notes)
- [Examples](vmware_guest_register_operation_module.md#examples)

## [Synopsis](vmware_guest_register_operation_module.md#id1)

- This module can register or unregister VMs to the inventory.

## [Parameters](vmware_guest_register_operation_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | Specify a cluster name to register VM. |
| **datacenter**  string | Destination datacenter for the register/unregister operation.  This parameter is case sensitive.  Default: `"ha-datacenter"` |
| **esxi_hostname**  string | The ESXi hostname where the virtual machine will run.  This parameter is case sensitive. |
| **folder**  string | Description folder, absolute path of the target folder.  The folder should include the datacenter. ESX’s datacenter is ha-datacenter.  This parameter is case sensitive.  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **name**  string / required | Specify VM name to be registered in the inventory. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **path**  string | Specify the path of vmx file.  Examples:  [datastore1] vm/vm.vmx  [datastore1] vm/vm.vmtx |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **resource_pool**  string | Specify a resource pool name to register VM.  This parameter is case sensitive.  Resource pool should be child of the selected host parent. |
| **state**  string | Specify the state the virtual machine should be in.  if set to `present`, register VM in inventory.  if set to `absent`, unregister VM from inventory.  Choices:   - `"present"` ← (default) - `"absent"` |
| **template**  boolean | Whether to register VM as a template.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | UUID of the virtual machine to manage if known, this is VMware’s unique identifier.  If virtual machine does not exists, then this parameter is ignored. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_guest_register_operation_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_guest_register_operation_module.md#id4)

```yaml+jinja
- name: Register VM to inventory
  community.vmware.vmware_guest_register_operation:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: "/vm"
    esxi_hostname: "{{ esxi_hostname }}"
    name: "{{ vm_name }}"
    template: false
    path: "[datastore1] vm/vm.vmx"
    state: present

- name: Register VM in resource pool
  community.vmware.vmware_guest_register_operation:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: "/vm"
    resource_pool: "{{ resource_pool }}"
    name: "{{ vm_name }}"
    template: false
    path: "[datastore1] vm/vm.vmx"
    state: present

- name: Register VM in Cluster
  community.vmware.vmware_guest_register_operation:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: "/vm"
    cluster: "{{ cluster_name }}"
    name: "{{ vm_name }}"
    template: false
    path: "[datastore1] vm/vm.vmx"
    state: present

- name: UnRegister VM from inventory
  community.vmware.vmware_guest_register_operation:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: "/vm"
    name: "{{ vm_name }}"
    state: absent
```

### Authors

- sky-joker (@sky-joker)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
