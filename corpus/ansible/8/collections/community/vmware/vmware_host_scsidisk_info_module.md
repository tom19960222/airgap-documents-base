---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_scsidisk_info module – Gather information about SCSI disk attached to the given ESXi"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_scsidisk_info_module.html
fetched_at: 2026-07-28T02:00:52+00:00
---
# community.vmware.vmware_host_scsidisk_info module – Gather information about SCSI disk attached to the given ESXi

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
> To use it in a playbook, specify: `community.vmware.vmware_host_scsidisk_info`.

- [Synopsis](vmware_host_scsidisk_info_module.md#synopsis)
- [Parameters](vmware_host_scsidisk_info_module.md#parameters)
- [Notes](vmware_host_scsidisk_info_module.md#notes)
- [Examples](vmware_host_scsidisk_info_module.md#examples)
- [Return Values](vmware_host_scsidisk_info_module.md#return-values)

## [Synopsis](vmware_host_scsidisk_info_module.md#id1)

- This module can be used to gather information about SCSI disk attached to the given ESXi.

## [Parameters](vmware_host_scsidisk_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster from which all host systems will be used.  SCSI disk information about each ESXi server will be returned for the given cluster.  This parameter is required if *esxi_hostname* is not specified. |
| **esxi_hostname**  string | Name of the host system to work with.  SCSI disk information about this ESXi server will be returned.  This parameter is required if *cluster_name* is not specified. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_host_scsidisk_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_scsidisk_info_module.md#id4)

```yaml+jinja
- name: Gather information SCSI disk attached to the given ESXi
  community.vmware.vmware_host_scsidisk_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost

- name: Gather information of all host systems from the given cluster
  community.vmware.vmware_host_scsidisk_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
```

## [Return Values](vmware_host_scsidisk_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hosts_scsidisk_info**  dictionary | metadata about host system SCSI disk information  **Returned:** always  **Sample:** `{"10.65.201.106": [{"block": 41943040, "block_size": 512, "canonical_name": "t10.ATA_QEMU_HARDDISK_QM00001_", "device_name": "/vmfs/devices/disks/t10.ATA_QEMU_HARDDISK_QM00001_", "device_path": "/vmfs/devices/disks/t10.ATA_QEMU_HARDDISK_QM00001_", "device_type": "disk", "display_name": "Local ATA Disk (t10.ATA_QEMU_HARDDISK_QM00001_)", "key": "key-vim.host.ScsiDisk-0100000000514d30303030312020202020202020202020202051454d552048", "local_disk": true, "lun_type": "disk", "model": "QEMU HARDDISK   ", "perenniallyReserved": null, "protocol_endpoint": false, "revision": "1.5.", "scsi_disk_type": "native512", "scsi_level": 5, "serial_number": "unavailable", "ssd": false, "uuid": "0100000000514d30303030312020202020202020202020202051454d552048", "vStorageSupport": "vStorageUnsupported", "vendor": "ATA     "}]}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
