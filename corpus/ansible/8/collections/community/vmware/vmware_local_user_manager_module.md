---
collection: ansible
version: "8"
title: "community.vmware.vmware_local_user_manager module – Manage local users on an ESXi host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_local_user_manager_module.html
fetched_at: 2026-07-28T02:01:02+00:00
---
# community.vmware.vmware_local_user_manager module – Manage local users on an ESXi host

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
> To use it in a playbook, specify: `community.vmware.vmware_local_user_manager`.

- [Synopsis](vmware_local_user_manager_module.md#synopsis)
- [Parameters](vmware_local_user_manager_module.md#parameters)
- [Notes](vmware_local_user_manager_module.md#notes)
- [Examples](vmware_local_user_manager_module.md#examples)

## [Synopsis](vmware_local_user_manager_module.md#id1)

- Manage local users on an ESXi host

## [Parameters](vmware_local_user_manager_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **local_user_description**  string | Description for the user. |
| **local_user_name**  string / required | The local user name to be changed. |
| **local_user_password**  string | The password to be set. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | Indicate desired state of the user. If the user already exists when `state=present`, the user info is updated  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_local_user_manager_module.md#id3)

> **Note:**
>
> - Be sure that the ESXi user used for login, has the appropriate rights to create / delete / edit users
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_local_user_manager_module.md#id4)

```yaml+jinja
- name: Add local user to ESXi
  community.vmware.vmware_local_user_manager:
    hostname: esxi_hostname
    username: root
    password: vmware
    local_user_name: foo
    local_user_password: password
  delegate_to: localhost
```

### Authors

- Andreas Nafpliotis (@nafpliot-ibm)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
