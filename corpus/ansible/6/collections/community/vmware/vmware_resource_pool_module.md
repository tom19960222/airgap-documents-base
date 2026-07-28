---
collection: ansible
version: "6"
title: "community.vmware.vmware_resource_pool module – Add/remove resource pools to/from vCenter"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_resource_pool_module.html
fetched_at: 2026-07-27T17:22:46+00:00
---
# community.vmware.vmware_resource_pool module – Add/remove resource pools to/from vCenter

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
> To use it in a playbook, specify: `community.vmware.vmware_resource_pool`.

- [Synopsis](vmware_resource_pool_module.md#synopsis)
- [Parameters](vmware_resource_pool_module.md#parameters)
- [Notes](vmware_resource_pool_module.md#notes)
- [Examples](vmware_resource_pool_module.md#examples)
- [Return Values](vmware_resource_pool_module.md#return-values)

## [Synopsis](vmware_resource_pool_module.md#id1)

- This module can be used to add/remove a resource pool to/from vCenter

## [Parameters](vmware_resource_pool_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster**  string | Name of the cluster to configure the resource pool.  This parameter is required if `esxi_hostname` or `parent_resource_pool` is not specified.  The `cluster`, `esxi_hostname` and `parent_resource_pool` parameters are mutually exclusive. |
| **cpu_allocation_shares**  integer  added in community.vmware 1.4.0 | The number of cpu shares allocated.  This value is only set if *cpu_shares* is set to `custom`.  Default: `4000` |
| **cpu_expandable_reservations**  boolean | In a resource pool with an expandable reservation, the reservation on a resource pool can grow beyond the specified value.  Choices:   - `false` - `true` ← (default) |
| **cpu_limit**  integer | The utilization of a virtual machine/resource pool will not exceed this limit, even if there are available resources.  The default value -1 indicates no limit.  Default: `-1` |
| **cpu_reservation**  integer | Amount of resource that is guaranteed available to the virtual machine or resource pool.  Default: `0` |
| **cpu_shares**  string | Memory shares are used in case of resource contention.  Choices:   - `"high"` - `"custom"` - `"low"` - `"normal"` ← (default) |
| **datacenter**  string / required | Name of the datacenter. |
| **esxi_hostname**  string  added in community.vmware 1.5.0 | Name of the host to configure the resource pool.  The host must not be member of a cluster.  This parameter is required if `cluster` or `parent_resource_pool` is not specified.  The `cluster`, `esxi_hostname` and `parent_resource_pool` parameters are mutually exclusive. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **mem_allocation_shares**  integer  added in community.vmware 1.4.0 | The number of memory shares allocated.  This value is only set if *mem_shares* is set to `custom`.  Default: `163840` |
| **mem_expandable_reservations**  boolean | In a resource pool with an expandable reservation, the reservation on a resource pool can grow beyond the specified value.  Choices:   - `false` - `true` ← (default) |
| **mem_limit**  integer | The utilization of a virtual machine/resource pool will not exceed this limit, even if there are available resources.  The default value -1 indicates no limit.  Default: `-1` |
| **mem_reservation**  integer | Amount of resource that is guaranteed available to the virtual machine or resource pool.  Default: `0` |
| **mem_shares**  string | Memory shares are used in case of resource contention.  Choices:   - `"high"` - `"custom"` - `"low"` - `"normal"` ← (default) |
| **parent_resource_pool**  string  added in community.vmware 1.9.0 | Name of the parent resource pool.  This parameter is required if `cluster` or `esxi_hostname` is not specified.  The `cluster`, `esxi_hostname` and `parent_resource_pool` parameters are mutually exclusive. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **resource_pool**  string / required | Resource pool name to manage. |
| **state**  string | Add or remove the resource pool  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_resource_pool_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_resource_pool_module.md#id4)

```yaml+jinja
- name: Add resource pool to vCenter
  community.vmware.vmware_resource_pool:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter_name }}'
    cluster: '{{ cluster_name }}'
    resource_pool: '{{ resource_pool_name }}'
    mem_shares: normal
    mem_limit: -1
    mem_reservation: 0
    mem_expandable_reservations: true
    cpu_shares: normal
    cpu_limit: -1
    cpu_reservation: 0
    cpu_expandable_reservations: true
    state: present
  delegate_to: localhost
```

## [Return Values](vmware_resource_pool_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance**  dictionary | metadata about the new resource pool  Returned: always  Sample: `"None"` |
| **resource_pool_config**  dictionary | config data about the resource pool, version added 1.4.0  Returned: always  Sample: `{"_vimtype": "vim.ResourceConfigSpec", "changeVersion": null, "cpuAllocation": {"_vimtype": "vim.ResourceAllocationInfo", "expandableReservation": true, "limit": -1, "overheadLimit": null, "reservation": 0, "shares": {"_vimtype": "vim.SharesInfo", "level": "normal", "shares": 4000}}, "entity": "vim.ResourcePool:resgroup-1108", "lastModified": null, "memoryAllocation": {"_vimtype": "vim.ResourceAllocationInfo", "expandableReservation": true, "limit": -1, "overheadLimit": null, "reservation": 0, "shares": {"_vimtype": "vim.SharesInfo", "level": "high", "shares": 327680}}, "name": "test_pr1", "scaleDescendantsShares": null}` |

### Authors

- Davis Phillips (@dav1x)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
