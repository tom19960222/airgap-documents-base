---
collection: ansible
version: "6"
title: "community.vmware.vmware_migrate_vmk module – Migrate a VMK interface from VSS to VDS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_migrate_vmk_module.html
fetched_at: 2026-07-27T17:22:41+00:00
---
# community.vmware.vmware_migrate_vmk module – Migrate a VMK interface from VSS to VDS

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
> To use it in a playbook, specify: `community.vmware.vmware_migrate_vmk`.

- [Synopsis](vmware_migrate_vmk_module.md#synopsis)
- [Parameters](vmware_migrate_vmk_module.md#parameters)
- [Notes](vmware_migrate_vmk_module.md#notes)
- [Examples](vmware_migrate_vmk_module.md#examples)

## [Synopsis](vmware_migrate_vmk_module.md#id1)

- Migrate a VMK interface from VSS to VDS

## [Parameters](vmware_migrate_vmk_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **current_portgroup_name**  string / required | Portgroup name VMK interface is currently on |
| **current_switch_name**  string / required | Switch VMK interface is currently on |
| **device**  string / required | VMK interface name |
| **esxi_hostname**  string / required | ESXi hostname to be managed |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **migrate_portgroup_name**  string / required | Portgroup name to migrate VMK interface to |
| **migrate_switch_name**  string / required | Switch name to migrate VMK interface to |
| **migrate_vlan_id**  integer  added in community.vmware 2.4.0 | VLAN to use for the VMK interface when migrating from VDS to VSS  Will be ignored when migrating from VSS to VDS |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_migrate_vmk_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_migrate_vmk_module.md#id4)

```yaml+jinja
- name: Migrate Management vmk
  community.vmware.vmware_migrate_vmk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    device: vmk1
    current_switch_name: temp_vswitch
    current_portgroup_name: esx-mgmt
    migrate_switch_name: dvSwitch
    migrate_portgroup_name: Management
  delegate_to: localhost
```

### Authors

- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
