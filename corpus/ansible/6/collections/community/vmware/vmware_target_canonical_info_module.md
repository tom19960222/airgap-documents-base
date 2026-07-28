---
collection: ansible
version: "6"
title: "community.vmware.vmware_target_canonical_info module – Return canonical (NAA) from an ESXi host system"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_target_canonical_info_module.html
fetched_at: 2026-07-27T17:22:49+00:00
---
# community.vmware.vmware_target_canonical_info module – Return canonical (NAA) from an ESXi host system

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
> To use it in a playbook, specify: `community.vmware.vmware_target_canonical_info`.

- [Synopsis](vmware_target_canonical_info_module.md#synopsis)
- [Parameters](vmware_target_canonical_info_module.md#parameters)
- [Notes](vmware_target_canonical_info_module.md#notes)
- [Examples](vmware_target_canonical_info_module.md#examples)
- [Return Values](vmware_target_canonical_info_module.md#return-values)

## [Synopsis](vmware_target_canonical_info_module.md#id1)

- This module can be used to gather information about canonical (NAA) from an ESXi host based on SCSI target ID.

## [Parameters](vmware_target_canonical_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster.  Info about all SCSI devices for all host system in the given cluster is returned.  This parameter is required, if `esxi_hostname` is not provided. |
| **esxi_hostname**  string | Name of the ESXi host system.  Info about all SCSI devices for the given ESXi host system is returned.  This parameter is required, if `cluster_name` is not provided. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **target_id**  integer | The target id based on order of scsi device.  version 2.6 onwards, this parameter is optional. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_target_canonical_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_target_canonical_info_module.md#id4)

```yaml+jinja
- name: Get Canonical name of particular target on particular ESXi host system
  community.vmware.vmware_target_canonical_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    target_id: 7
    esxi_hostname: esxi_hostname
  delegate_to: localhost

- name: Get Canonical name of all target on particular ESXi host system
  community.vmware.vmware_target_canonical_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost

- name: Get Canonical name of all ESXi hostname on particular Cluster
  community.vmware.vmware_target_canonical_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
```

## [Return Values](vmware_target_canonical_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **canonical**  string | metadata about SCSI Target device  Returned: if host system and target id is given  Sample: `"mpx.vmhba0:C0:T0:L0"` |
| **scsi_tgt_info**  dictionary | metadata about all SCSI Target devices  Returned: if host system or cluster is given  Sample: `{"DC0_C0_H0": {"scsilun_canonical": {"key-vim.host.ScsiDisk-0000000000766d686261303a303a30": "mpx.vmhba0:C0:T0:L0", "key-vim.host.ScsiLun-0005000000766d686261313a303a30": "mpx.vmhba1:C0:T0:L0"}, "target_lun_uuid": {"0": "key-vim.host.ScsiDisk-0000000000766d686261303a303a30"}}, "DC0_C0_H1": {"scsilun_canonical": {"key-vim.host.ScsiDisk-0000000000766d686261303a303a30": "mpx.vmhba0:C0:T0:L0", "key-vim.host.ScsiLun-0005000000766d686261313a303a30": "mpx.vmhba1:C0:T0:L0"}, "target_lun_uuid": {"0": "key-vim.host.ScsiDisk-0000000000766d686261303a303a30"}}}` |

### Authors

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
