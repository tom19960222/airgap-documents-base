---
collection: ansible
version: "8"
title: "community.vmware.vcenter_root_password_expiration module – root password expiration of vCSA"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vcenter_root_password_expiration_module.html
fetched_at: 2026-07-28T01:59:32+00:00
---
# community.vmware.vcenter_root_password_expiration module – root password expiration of vCSA

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
> To use it in a playbook, specify: `community.vmware.vcenter_root_password_expiration`.

New in community.vmware 3.10.0

- [Synopsis](vcenter_root_password_expiration_module.md#synopsis)
- [Parameters](vcenter_root_password_expiration_module.md#parameters)
- [Notes](vcenter_root_password_expiration_module.md#notes)
- [Examples](vcenter_root_password_expiration_module.md#examples)

## [Synopsis](vcenter_root_password_expiration_module.md#id1)

- Manages password expiration configuration for root user of vCSA appliance

## [Parameters](vcenter_root_password_expiration_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **email**  string | e-mail to send password expiration warnings to |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **max_days_between_password_change**  integer | Maximum days between password change |
| **min_days_between_password_change**  integer | Minimum days between password change |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | present - represents that password expiration must be configured  absent - represents no expiration for root user  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **warn_days_before_password_expiration**  integer | Days before password expires and password expiration e-mail should be sent |

## [Notes](vcenter_root_password_expiration_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vcenter_root_password_expiration_module.md#id4)

```yaml+jinja
- name: Configures expiring root password
  vcenter_root_password_expiration:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_localos_username }}'
    password: '{{ vcenter_password }}'
    max_days_between_password_change: 60
    min_days_between_password_change: 6
    warn_days_before_password_expiration: 7
    email: example@vmware.com
    state: present
  delegate_to: localhost

- name: Configures non-expiring root password
  vcenter_root_password_expiration:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_localos_username }}'
    password: '{{ vcenter_localos_password }}'
    state: absent
  delegate_to: localhost
```

### Authors

- Valentin Yonev (@valentinJonev)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
