---
collection: ansible
version: "6"
title: "community.vmware.vsphere_copy module – Copy a file to a VMware datastore"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vsphere_copy_module.html
fetched_at: 2026-07-27T17:23:04+00:00
---
# community.vmware.vsphere_copy module – Copy a file to a VMware datastore

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
> To use it in a playbook, specify: `community.vmware.vsphere_copy`.

- [Synopsis](vsphere_copy_module.md#synopsis)
- [Parameters](vsphere_copy_module.md#parameters)
- [Notes](vsphere_copy_module.md#notes)
- [Examples](vsphere_copy_module.md#examples)

## [Synopsis](vsphere_copy_module.md#id1)

- Upload files to a VMware datastore through a vCenter REST API.

## [Parameters](vsphere_copy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string | The datacenter on the vCenter server that holds the datastore. |
| **datastore**  string / required | The datastore to push files to. |
| **hostname**  aliases: host  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **path**  aliases: dest  string / required | The file to push to the datastore. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **src**  aliases: name  string / required | The file to push to vCenter. |
| **timeout**  integer | The timeout in seconds for the upload to the datastore.  Default: `10` |
| **username**  aliases: login  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vsphere_copy_module.md#id3)

> **Note:**
>
> - This module ought to be run from a system that can access the vCenter or the ESXi directly and has the file to transfer. It can be the normal remote target or you can change it either by using `transport: local` or using `delegate_to`.
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vsphere_copy_module.md#id4)

```yaml+jinja
- name: Copy file to datastore using delegate_to
  community.vmware.vsphere_copy:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    src: /some/local/file
    datacenter: DC1 Someplace
    datastore: datastore1
    path: some/remote/file
  delegate_to: localhost

- name: Copy file to datastore when datacenter is inside folder called devel
  community.vmware.vsphere_copy:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    src: /some/local/file
    datacenter: devel/DC1
    datastore: datastore1
    path: some/remote/file
  delegate_to: localhost

- name: Copy file to datastore using other_system
  community.vmware.vsphere_copy:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    src: /other/local/file
    datacenter: DC2 Someplace
    datastore: datastore2
    path: other/remote/file
  delegate_to: other_system
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
