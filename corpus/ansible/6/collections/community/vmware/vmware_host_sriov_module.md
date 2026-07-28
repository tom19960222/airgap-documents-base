---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_sriov module – Manage SR-IOV settings on host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_sriov_module.html
fetched_at: 2026-07-27T17:22:33+00:00
---
# community.vmware.vmware_host_sriov module – Manage SR-IOV settings on host

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
> To use it in a playbook, specify: `community.vmware.vmware_host_sriov`.

New in community.vmware 1.0.0

- [Synopsis](vmware_host_sriov_module.md#synopsis)
- [Parameters](vmware_host_sriov_module.md#parameters)
- [Notes](vmware_host_sriov_module.md#notes)
- [Examples](vmware_host_sriov_module.md#examples)
- [Return Values](vmware_host_sriov_module.md#return-values)

## [Synopsis](vmware_host_sriov_module.md#id1)

- This module can be used to configure, enable or disable SR-IOV functions on ESXi host.
- Module does not reboot the host after changes, but puts it in output “rebootRequired” state.
- User can specify an ESXi hostname or Cluster name. In case of cluster name, all ESXi hosts are updated.

## [Parameters](vmware_host_sriov_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster from which all host systems will be used.  This parameter is required if `esxi_hostname` is not specified. |
| **esxi_hostname**  string | Name of the host system to work with.  This parameter is required if `cluster_name` is not specified.  User can specify specific host from the cluster. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **num_virt_func**  integer / required | number of functions to activate on interface.  0 means SR-IOV disabled.  number greater than 0 means SR-IOV enabled. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **sriov_on**  boolean | optional parameter, related to `num_virt_func`.  SR-IOV can be enabled only if `num_virt_func` > 0.  Choices:   - `false` - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **vmnic**  string / required | Interface name, like vmnic0. |

## [Notes](vmware_host_sriov_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_sriov_module.md#id4)

```yaml+jinja
- name: enable SR-IOV on vmnic0 with 8 functions
  community.vmware.vmware_host_sriov:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi1 }}"
    vmnic: vmnic0
    sriov_on: true
    num_virt_func: 8

- name: enable SR-IOV on already enabled interface vmnic0
  community.vmware.vmware_host_sriov:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi1 }}"
    vmnic: vmnic0
    sriov_on: true
    num_virt_func: 8

- name: enable SR-IOV on vmnic0 with big number of functions
  community.vmware.vmware_host_sriov:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi1 }}"
    vmnic: vmnic0
    sriov_on: true
    num_virt_func: 100
  ignore_errors: true

- name: disable SR-IOV on vmnic0
  community.vmware.vmware_host_sriov:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi1 }}"
    vmnic: vmnic0
    sriov_on: false
    num_virt_func: 0
```

## [Return Values](vmware_host_sriov_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **host_sriov_diff**  dictionary | contains info about SR-IOV status on vmnic before, after and requested changes  sometimes vCenter slowly update info, as result “after” contains same info as “before” need to run again in check_mode or reboot host, as ESXi requested  Returned: always  Sample: `{"changed": true, "diff": {"after": {"host_test": {"maxVirtualFunctionSupported": 63, "numVirtualFunction": 0, "numVirtualFunctionRequested": 8, "rebootRequired": true, "sriovActive": false, "sriovCapable": true, "sriovEnabled": true}}, "before": {"host_test": {"maxVirtualFunctionSupported": 63, "numVirtualFunction": 0, "numVirtualFunctionRequested": 0, "rebootRequired": false, "sriovActive": false, "sriovCapable": true, "sriovEnabled": false}}, "changes": {"host_test": {"numVirtualFunction": 8, "rebootRequired": true, "sriovEnabled": true}}}}` |

### Authors

- Viktor Tsymbalyuk (@victron)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
