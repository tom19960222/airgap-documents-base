---
collection: ansible
version: "6"
title: "community.vmware.vmware_first_class_disk module – Manage VMware vSphere First Class Disks"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_first_class_disk_module.html
fetched_at: 2026-07-27T17:21:47+00:00
---
# community.vmware.vmware_first_class_disk module – Manage VMware vSphere First Class Disks

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
> To use it in a playbook, specify: `community.vmware.vmware_first_class_disk`.

New in community.vmware 1.7.0

- [Synopsis](vmware_first_class_disk_module.md#synopsis)
- [Parameters](vmware_first_class_disk_module.md#parameters)
- [Notes](vmware_first_class_disk_module.md#notes)
- [Examples](vmware_first_class_disk_module.md#examples)
- [Return Values](vmware_first_class_disk_module.md#return-values)

## [Synopsis](vmware_first_class_disk_module.md#id1)

- This module can be used to manage (create, delete, resize) VMware vSphere First Class Disks.

## [Parameters](vmware_first_class_disk_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter_name**  string | The name of the datacenter. |
| **datastore_name**  string / required | Name of datastore or datastore cluster to be used for the disk. |
| **disk_name**  string / required | The name of the disk. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **size**  string | Disk storage size, an integer plus a unit.  There is no space allowed in between size number and unit.  Allowed units are MB, GB and TB.  Examples:  size: 2048MB  size: 10GB  size: 1TB |
| **state**  string | If the disk should be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_first_class_disk_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_first_class_disk_module.md#id4)

```yaml+jinja
- name: Create Disk
  community.vmware.vmware_first_class_disk:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore_name: '{{ datastore_name }}'
    disk_name: '1GBDisk'
    size: '1GB'
    state: present
  delegate_to: localhost

- name: Delete Disk
  community.vmware.vmware_first_class_disk:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore_name: '{{ datastore_name }}'
    disk_name: 'FirstClassDisk'
    state: absent
  delegate_to: localhost
```

## [Return Values](vmware_first_class_disk_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **first_class_disk**  dictionary | First-class disk returned when created, deleted or changed  Returned: changed  Sample: `"{\n  \"name\": \"1GBDisk\"\n  \"datastore_name\": \"DS0\"\n  \"size_mb\": \"1024\"\n  \"state\": \"present\"\n}\n"` |

### Authors

- Mario Lenz (@mariolenz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
