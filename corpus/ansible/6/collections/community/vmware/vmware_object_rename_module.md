---
collection: ansible
version: "6"
title: "community.vmware.vmware_object_rename module – Renames VMware objects"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_object_rename_module.html
fetched_at: 2026-07-27T17:22:42+00:00
---
# community.vmware.vmware_object_rename module – Renames VMware objects

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this module,
> see [Requirements](vmware_object_rename_module.md#ansible-collections-community-vmware-vmware-object-rename-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_object_rename`.

- [Synopsis](vmware_object_rename_module.md#synopsis)
- [Requirements](vmware_object_rename_module.md#requirements)
- [Parameters](vmware_object_rename_module.md#parameters)
- [Examples](vmware_object_rename_module.md#examples)
- [Return Values](vmware_object_rename_module.md#return-values)

## [Synopsis](vmware_object_rename_module.md#id1)

- This module can be used to rename VMware objects.
- All variables and VMware object names are case sensitive.
- Renaming Host and Network is not supported by VMware APIs.

## [Requirements](vmware_object_rename_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere Automation SDK

## [Parameters](vmware_object_rename_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **new_name**  aliases: object_new_name  string / required | New name for VMware object. |
| **object_moid**  string | Managed object id of the VMware object to work with.  Mutually exclusive with `object_name`. |
| **object_name**  string | Name of the object to work with.  Mutually exclusive with `object_moid`. |
| **object_type**  string / required | Type of object to work with.  Valid options are Cluster, ClusterComputeResource, Datacenter, Datastore, Folder, ResourcePool, VM or VirtualMachine.  Choices:   - `"ClusterComputeResource"` - `"Cluster"` - `"Datacenter"` - `"Datastore"` - `"Folder"` - `"Network"` - `"ResourcePool"` - `"VM"` - `"VirtualMachine"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **port**  integer | The port number of the vSphere vCenter.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Default: `443` |
| **protocol**  string | The connection to protocol.  Choices:   - `"http"` - `"https"` ← (default) |
| **proxy_host**  string  added in community.vmware 1.12.0 | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead. |
| **proxy_port**  integer  added in community.vmware 1.12.0 | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid.  Set to `False` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](vmware_object_rename_module.md#id4)

```yaml+jinja
- name: Rename a virtual machine
  community.vmware.vmware_object_rename:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    new_name: Fedora_31
    object_name: Fedora_VM
    object_type: VirtualMachine
  delegate_to: localhost

- name: Rename a virtual machine using moid
  community.vmware.vmware_object_rename:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    new_name: Fedora_31
    object_moid: vm-14
    object_type: VirtualMachine
  delegate_to: localhost

- name: Rename a datacenter
  community.vmware.vmware_object_rename:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    new_name: Asia_Datacenter
    object_name: dc1
    object_type: Datacenter
  delegate_to: localhost

- name: Rename a folder with moid
  community.vmware.vmware_object_rename:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    new_name: backup
    object_moid: group-v46
    object_type: Folder
  delegate_to: localhost

- name: Rename a cluster with moid
  community.vmware.vmware_object_rename:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    new_name: CCR_1
    object_moid: domain-c33
    object_type: Cluster
  delegate_to: localhost
```

## [Return Values](vmware_object_rename_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **rename_status**  dictionary | metadata about VMware object rename operation  Returned: on success  Sample: `{"current_name": "Fedora_31", "desired_name": "Fedora_31", "previous_name": "Fedora_VM"}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
