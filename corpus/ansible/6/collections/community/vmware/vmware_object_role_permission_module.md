---
collection: ansible
version: "6"
title: "community.vmware.vmware_object_role_permission module – Manage local roles on an ESXi host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_object_role_permission_module.html
fetched_at: 2026-07-27T17:22:42+00:00
---
# community.vmware.vmware_object_role_permission module – Manage local roles on an ESXi host

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
> To use it in a playbook, specify: `community.vmware.vmware_object_role_permission`.

- [Synopsis](vmware_object_role_permission_module.md#synopsis)
- [Parameters](vmware_object_role_permission_module.md#parameters)
- [Notes](vmware_object_role_permission_module.md#notes)
- [Examples](vmware_object_role_permission_module.md#examples)
- [Return Values](vmware_object_role_permission_module.md#return-values)

## [Synopsis](vmware_object_role_permission_module.md#id1)

- This module can be used to manage object permissions on the given host.

## [Parameters](vmware_object_role_permission_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **group**  string | The group to be assigned permission.  Required if `principal` is not specified. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **object_name**  string / required | The object name to assigned permission. |
| **object_type**  string | The object type being targeted.  Choices:   - `"Folder"` ← (default) - `"VirtualMachine"` - `"Datacenter"` - `"ResourcePool"` - `"Datastore"` - `"Network"` - `"HostSystem"` - `"ComputeResource"` - `"ClusterComputeResource"` - `"DistributedVirtualSwitch"` - `"DistributedVirtualPortgroup"` - `"StoragePod"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **principal**  string | The user to be assigned permission.  Required if `group` is not specified.  If specifying domain user, required separator of domain uses backslash. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **recursive**  boolean | Should the permissions be recursively applied.  Choices:   - `false` - `true` ← (default) |
| **role**  string / required | The role to be assigned permission.  User can also specify role name presented in Web UI. Supported added in 1.5.0. |
| **state**  string | Indicate desired state of the object’s permission.  When `state=present`, the permission will be added if it doesn’t already exist.  When `state=absent`, the permission is removed if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_object_role_permission_module.md#id3)

> **Note:**
>
> - The ESXi login user must have the appropriate rights to administer permissions.
> - Permissions for a distributed switch must be defined and managed on either the datacenter or a folder containing the switch.
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_object_role_permission_module.md#id4)

```yaml+jinja
- name: Assign user to VM folder
  community.vmware.vmware_object_role_permission:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    role: Admin
    principal: user_bob
    object_name: services
    state: present
  delegate_to: localhost

- name: Remove user from VM folder
  community.vmware.vmware_object_role_permission:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    role: Admin
    principal: user_bob
    object_name: services
    state: absent
  delegate_to: localhost

- name: Assign finance group to VM folder
  community.vmware.vmware_object_role_permission:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    role: Limited Users
    group: finance
    object_name: Accounts
    state: present
  delegate_to: localhost

- name: Assign view_user Read Only permission at root folder
  community.vmware.vmware_object_role_permission:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    role: ReadOnly
    principal: view_user
    object_name: rootFolder
    state: present
  delegate_to: localhost

- name: Assign domain user to VM folder
  community.vmware.vmware_object_role_permission:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    role: Admin
    principal: "vsphere.local\\domainuser"
    object_name: services
    state: present
  delegate_to: localhost
```

## [Return Values](vmware_object_role_permission_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | whether or not a change was made to the object’s role  Returned: always |

### Authors

- Derek Rushing (@kryptsi)
- Joseph Andreatta (@vmwjoseph)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
