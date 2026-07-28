---
collection: ansible
version: "8"
title: "community.vmware.vcenter_folder module – Manage folders on given datacenter"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vcenter_folder_module.html
fetched_at: 2026-07-28T01:59:30+00:00
---
# community.vmware.vcenter_folder module – Manage folders on given datacenter

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
> To use it in a playbook, specify: `community.vmware.vcenter_folder`.

- [Synopsis](vcenter_folder_module.md#synopsis)
- [Parameters](vcenter_folder_module.md#parameters)
- [Notes](vcenter_folder_module.md#notes)
- [Examples](vcenter_folder_module.md#examples)
- [Return Values](vcenter_folder_module.md#return-values)

## [Synopsis](vcenter_folder_module.md#id1)

- This module can be used to create, delete, move and rename folder on then given datacenter.
- This module is only supported for vCenter.

## [Parameters](vcenter_folder_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  aliases: datacenter_name  string / required | Name of the datacenter. |
| **folder_name**  string / required | Name of folder to be managed.  This is case sensitive parameter.  Folder name should be under 80 characters. This is a VMware restriction. |
| **folder_type**  string | This is type of folder.  If set to `vm`, then ‘VM and Template Folder’ is created under datacenter.  If set to `host`, then ‘Host and Cluster Folder’ is created under datacenter.  If set to `datastore`, then ‘Storage Folder’ is created under datacenter.  If set to `network`, then ‘Network Folder’ is created under datacenter.  This parameter is required, if `state` is set to `present` and parent_folder is absent.  This option is ignored, if `parent_folder` is set.  **Choices:**   - `"datastore"` - `"host"` - `"network"` - `"vm"` ← (default) |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **parent_folder**  string | Name of the parent folder under which new folder needs to be created.  This is case sensitive parameter.  If user wants to create a folder under ‘/DC0/vm/vm_folder’, this value will be ‘vm_folder’.  If user wants to create a folder under ‘/DC0/vm/folder1/folder2’, this value will be ‘folder1/folder2’. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | State of folder.  If set to `present` without parent folder parameter, then folder with `folder_type` is created.  If set to `present` with parent folder parameter, then folder in created under parent folder. `folder_type` is ignored.  If set to `absent`, then folder is unregistered and destroyed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vcenter_folder_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vcenter_folder_module.md#id4)

```yaml+jinja
- name: Create a VM folder on given datacenter
  community.vmware.vcenter_folder:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter_name
    folder_name: sample_vm_folder
    folder_type: vm
    state: present
  register: vm_folder_creation_result
  delegate_to: localhost

- name: Create a datastore folder on given datacenter
  community.vmware.vcenter_folder:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter_name
    folder_name: sample_datastore_folder
    folder_type: datastore
    state: present
  register: datastore_folder_creation_result
  delegate_to: localhost

- name: Create a sub folder under VM folder on given datacenter
  community.vmware.vcenter_folder:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter_name
    folder_name: sample_sub_folder
    parent_folder: vm_folder
    state: present
  register: sub_folder_creation_result
  delegate_to: localhost

- name: Delete a VM folder on given datacenter
  community.vmware.vcenter_folder:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter_name
    folder_name: sample_vm_folder
    folder_type: vm
    state: absent
  register: vm_folder_deletion_result
  delegate_to: localhost
```

## [Return Values](vcenter_folder_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  complex | The detail about the new folder  **Returned:** On success |
| **msg**  string | string stating about result  **Returned:** success |
| **path**  string | the full path of the new folder  **Returned:** success |

### Authors

- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)
- Jan Meerkamp (@meerkampdvv)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
