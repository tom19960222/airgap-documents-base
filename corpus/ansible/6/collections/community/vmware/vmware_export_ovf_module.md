---
collection: ansible
version: "6"
title: "community.vmware.vmware_export_ovf module – Exports a VMware virtual machine to an OVF file, device files and a manifest file"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_export_ovf_module.html
fetched_at: 2026-07-27T17:21:46+00:00
---
# community.vmware.vmware_export_ovf module – Exports a VMware virtual machine to an OVF file, device files and a manifest file

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
> To use it in a playbook, specify: `community.vmware.vmware_export_ovf`.

- [Synopsis](vmware_export_ovf_module.md#synopsis)
- [Parameters](vmware_export_ovf_module.md#parameters)
- [Notes](vmware_export_ovf_module.md#notes)
- [Examples](vmware_export_ovf_module.md#examples)
- [Return Values](vmware_export_ovf_module.md#return-values)

## [Synopsis](vmware_export_ovf_module.md#id1)

- This module can be used to export a VMware virtual machine to OVF template from vCenter server or ESXi host.

## [Parameters](vmware_export_ovf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string | Datacenter name of the virtual machine to export.  This parameter is case sensitive.  Default: `"ha-datacenter"` |
| **download_timeout**  integer | The user defined timeout in second of exporting file.  If the vmdk file is too large, you can increase the value.  Default: `30` |
| **export_dir**  path / required | Absolute path to place the exported files on the server running this task, must have write permission.  If folder not exist will create it, also create a folder under this path named with VM name. |
| **export_with_extraconfig**  boolean  added in community.vmware 2.0.0 | All extra configuration options are exported for a virtual machine.  Choices:   - `false` ← (default) - `true` |
| **export_with_images**  boolean | Export an ISO image of the media mounted on the CD/DVD Drive within the virtual machine.  Choices:   - `false` ← (default) - `true` |
| **folder**  string | Destination folder, absolute path to find the specified guest.  The folder should include the datacenter. ESX datacenter is ha-datacenter.  This parameter is case sensitive.  If multiple machines are found with same name, this parameter is used to identify  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **moid**  string | Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.  This is required if `name` or `uuid` is not supplied. |
| **name**  string | Name of the virtual machine to export.  This is a required parameter, if parameter `uuid` or `moid` is not supplied. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **uuid**  string | Uuid of the virtual machine to export.  This is a required parameter, if parameter `name` or `moid` is not supplied. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_export_ovf_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_export_ovf_module.md#id4)

```yaml+jinja
- community.vmware.vmware_export_ovf:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    name: '{{ vm_name }}'
    export_with_images: true
    export_dir: /path/to/ovf_template/
  delegate_to: localhost
```

## [Return Values](vmware_export_ovf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance**  dictionary | list of the exported files, if exported from vCenter server, device file is not named with vm name  Returned: always  Sample: `"None"` |

### Authors

- Diane Wang (@Tomorrow9)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
