---
collection: ansible
version: "8"
title: "community.vmware.vmware_local_role_manager module – Manage local roles on an ESXi host or vCenter"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_local_role_manager_module.html
fetched_at: 2026-07-28T02:01:00+00:00
---
# community.vmware.vmware_local_role_manager module – Manage local roles on an ESXi host or vCenter

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
> To use it in a playbook, specify: `community.vmware.vmware_local_role_manager`.

- [Synopsis](vmware_local_role_manager_module.md#synopsis)
- [Parameters](vmware_local_role_manager_module.md#parameters)
- [Notes](vmware_local_role_manager_module.md#notes)
- [Examples](vmware_local_role_manager_module.md#examples)
- [Return Values](vmware_local_role_manager_module.md#return-values)

## [Synopsis](vmware_local_role_manager_module.md#id1)

- This module can be used to manage local roles on an ESXi host or vCenter.

## [Parameters](vmware_local_role_manager_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | This parameter is only valid while updating an existing role with privileges.  `add` will add the privileges to the existing privilege list.  `remove` will remove the privileges from the existing privilege list.  `set` will replace the privileges of the existing privileges with user defined list of privileges.  **Choices:**   - `"add"` - `"remove"` - `"set"` ← (default) |
| **force_remove**  boolean | If set to `false` then prevents the role from being removed if any permissions are using it.  **Choices:**   - `false` ← (default) - `true` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **local_privilege_ids**  list / elements=string | The list of privileges that role needs to have.  Please see <https://docs.vmware.com/en/VMware-vSphere/6.0/com.vmware.vsphere.security.doc/GUID-ED56F3C4-77D0-49E3-88B6-B99B8B437B62.html>  **Default:** `[]` |
| **local_role_name**  string / required | The local role name to be managed. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | Indicate desired state of the role.  If the role already exists when `state=present`, the role info is updated.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_local_role_manager_module.md#id3)

> **Note:**
>
> - Be sure that the user used for login, has the appropriate rights to create / delete / edit roles
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_local_role_manager_module.md#id4)

```yaml+jinja
- name: Add local role to ESXi
  community.vmware.vmware_local_role_manager:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    local_role_name: vmware_qa
    state: present
  delegate_to: localhost

- name: Add local role with privileges to vCenter
  community.vmware.vmware_local_role_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    local_role_name: vmware_qa
    local_privilege_ids: [ 'Folder.Create', 'Folder.Delete']
    state: present
  delegate_to: localhost

- name: Remove local role from ESXi
  community.vmware.vmware_local_role_manager:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    local_role_name: vmware_qa
    state: absent
  delegate_to: localhost

- name: Add a privilege to an existing local role
  community.vmware.vmware_local_role_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    local_role_name: vmware_qa
    local_privilege_ids: [ 'Folder.Create' ]
    action: add
  delegate_to: localhost

- name: Remove a privilege to an existing local role
  community.vmware.vmware_local_role_manager:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    local_role_name: vmware_qa
    local_privilege_ids: [ 'Folder.Create' ]
    action: remove
  delegate_to: localhost

- name: Set a privilege to an existing local role
  community.vmware.vmware_local_role_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    local_role_name: vmware_qa
    local_privilege_ids: [ 'Folder.Create' ]
    action: set
  delegate_to: localhost
```

## [Return Values](vmware_local_role_manager_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **local_role_name**  string | Name of local role  **Returned:** always |
| **new_privileges**  list / elements=string | List of privileges  **Returned:** always |
| **old_privileges**  list / elements=string | List of privileges of role before the update  **Returned:** on update |
| **privileges**  list / elements=string | List of privileges  **Returned:** always |
| **privileges_previous**  list / elements=string | List of privileges of role before the update  **Returned:** on update |
| **role_id**  integer | Generated local role id  **Returned:** always |
| **role_name**  string | Name of local role  **Returned:** always |

### Authors

- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
