---
collection: ansible
version: "6"
title: "community.vmware.vmware_vm_vss_dvs_migrate module – Migrates a virtual machine from a standard vswitch to distributed"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_vm_vss_dvs_migrate_module.html
fetched_at: 2026-07-27T17:22:57+00:00
---
# community.vmware.vmware_vm_vss_dvs_migrate module – Migrates a virtual machine from a standard vswitch to distributed

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
> To use it in a playbook, specify: `community.vmware.vmware_vm_vss_dvs_migrate`.

- [Synopsis](vmware_vm_vss_dvs_migrate_module.md#synopsis)
- [Parameters](vmware_vm_vss_dvs_migrate_module.md#parameters)
- [Notes](vmware_vm_vss_dvs_migrate_module.md#notes)
- [Examples](vmware_vm_vss_dvs_migrate_module.md#examples)

## [Synopsis](vmware_vm_vss_dvs_migrate_module.md#id1)

- Migrates a virtual machine from a standard vswitch to distributed

## [Parameters](vmware_vm_vss_dvs_migrate_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dvportgroup_name**  string / required | Name of the portgroup to migrate to the virtual machine to |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **vm_name**  string / required | Name of the virtual machine to migrate to a dvSwitch |

## [Notes](vmware_vm_vss_dvs_migrate_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vm_vss_dvs_migrate_module.md#id4)

```yaml+jinja
- name: Migrate VCSA to vDS
  community.vmware.vmware_vm_vss_dvs_migrate:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    vm_name: '{{ vm_name }}'
    dvportgroup_name: '{{ distributed_portgroup_name }}'
  delegate_to: localhost
```

### Authors

- Joseph Callen (@jcpowermac)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
