---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_user_manager module – Manage users of ESXi"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_user_manager_module.html
fetched_at: 2026-07-27T17:22:35+00:00
---
# community.vmware.vmware_host_user_manager module – Manage users of ESXi

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
> To use it in a playbook, specify: `community.vmware.vmware_host_user_manager`.

New in community.vmware 2.1.0

- [Synopsis](vmware_host_user_manager_module.md#synopsis)
- [Parameters](vmware_host_user_manager_module.md#parameters)
- [Notes](vmware_host_user_manager_module.md#notes)
- [Examples](vmware_host_user_manager_module.md#examples)
- [Return Values](vmware_host_user_manager_module.md#return-values)

## [Synopsis](vmware_host_user_manager_module.md#id1)

- This module can add, update or delete local users on ESXi host.

## [Parameters](vmware_host_user_manager_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **esxi_hostname**  string / required | Name of the ESXi host that is managing the local user. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **override_user_password**  boolean | If the local user exists and updates the password, change this parameter value is true.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If set to `present`, add a new local user or update information.  If set to `absent`, delete the local user.  Choices:   - `"present"` ← (default) - `"absent"` |
| **user_description**  aliases: local_user_description  string | The local user description. |
| **user_name**  aliases: local_user_name  string / required | Name of the local user. |
| **user_password**  aliases: local_user_password  string | The local user password.  If you’d like to update the password, require the *override_user_password* is true. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_host_user_manager_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_user_manager_module.md#id4)

```yaml+jinja
- name: Add new local user to ESXi host
  community.vmware.vmware_host_user_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi1 }}"
    user_name: example
    user_description: "example user"
    user_password: "{{ local_user_password }}"
    state: present

- name: Update the local user password in ESXi host
  community.vmware.vmware_host_user_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi1 }}"
    user_name: example
    user_description: "example user"
    user_password: "{{ local_user_password }}"
    override_user_password: true
    state: present

- name: Delete the local user in ESXi host
  community.vmware.vmware_host_user_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi1 }}"
    user_name: example
    state: absent
```

## [Return Values](vmware_host_user_manager_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The executed result for the module.  Returned: always  Sample: `"{\n    \"msg\": \"Added the new user.\n}"` |

### Authors

- sky-joker (@sky-joker)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
