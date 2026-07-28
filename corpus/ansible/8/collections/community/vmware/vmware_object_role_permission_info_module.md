---
collection: ansible
version: "8"
title: "community.vmware.vmware_object_role_permission_info module – Gather information about object’s permissions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_object_role_permission_info_module.html
fetched_at: 2026-07-28T02:01:06+00:00
---
# community.vmware.vmware_object_role_permission_info module – Gather information about object’s permissions

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
> To use it in a playbook, specify: `community.vmware.vmware_object_role_permission_info`.

- [Synopsis](vmware_object_role_permission_info_module.md#synopsis)
- [Parameters](vmware_object_role_permission_info_module.md#parameters)
- [Notes](vmware_object_role_permission_info_module.md#notes)
- [Examples](vmware_object_role_permission_info_module.md#examples)
- [Return Values](vmware_object_role_permission_info_module.md#return-values)

## [Synopsis](vmware_object_role_permission_info_module.md#id1)

- This module can be used to gather object permissions on the given VMware object.

## [Parameters](vmware_object_role_permission_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  aliases: object_moid  string | Managed object ID for the given object.  Mutually exclusive with *object_name*. |
| **object_name**  string | The object name to assigned permission.  Mutually exclusive with *moid*. |
| **object_type**  string | The object type being targeted.  **Choices:**   - `"Folder"` ← (default) - `"VirtualMachine"` - `"Datacenter"` - `"ResourcePool"` - `"Datastore"` - `"Network"` - `"HostSystem"` - `"ComputeResource"` - `"ClusterComputeResource"` - `"DistributedVirtualSwitch"` - `"DistributedVirtualPortgroup"` - `"StoragePod"` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **principal**  string | The optional name of an entity, such as a user, assigned permissions on an object.  If provided, actual permissions on the specified object are returned for the principal, instead of roles. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_object_role_permission_info_module.md#id3)

> **Note:**
>
> - The ESXi or vCenter login user must have the appropriate rights to administer permissions.
> - Supports check mode.
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_object_role_permission_info_module.md#id4)

```yaml+jinja
- name: Gather role information about Datastore
  community.vmware.vmware_object_role_permission_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    object_name: ds_200
    object_type: Datastore

- name: Gather permissions on Datastore for a User
  community.vmware.vmware_object_role_permission_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    principal: some.user@company.com
    object_name: ds_200
    object_type: Datastore
```

## [Return Values](vmware_object_role_permission_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **permission_info**  list / elements=string | information about object’s permission  **Returned:** always  **Sample:** `[{"principal": "VSPHERE.LOCAL\\vpxd-extension-12e0b667-892c-4694-8a5e-f13147e45dbd", "propagate": true, "role_id": -1, "role_name": "Admin"}]` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
