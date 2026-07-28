---
collection: ansible
version: "8"
title: "community.vmware.vmware_resource_pool_info module – Gathers info about resource pool information"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_resource_pool_info_module.html
fetched_at: 2026-07-28T02:01:09+00:00
---
# community.vmware.vmware_resource_pool_info module – Gathers info about resource pool information

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
> To use it in a playbook, specify: `community.vmware.vmware_resource_pool_info`.

- [Synopsis](vmware_resource_pool_info_module.md#synopsis)
- [Parameters](vmware_resource_pool_info_module.md#parameters)
- [Notes](vmware_resource_pool_info_module.md#notes)
- [Examples](vmware_resource_pool_info_module.md#examples)
- [Return Values](vmware_resource_pool_info_module.md#return-values)

## [Synopsis](vmware_resource_pool_info_module.md#id1)

- This module can be used to gather information about all resource configuration information.

## [Parameters](vmware_resource_pool_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_resource_pool_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_resource_pool_info_module.md#id4)

```yaml+jinja
- name: Gather resource pool info about all resource pools available
  community.vmware.vmware_resource_pool_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  register: rp_info
  delegate_to: localhost
```

## [Return Values](vmware_resource_pool_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resource_pool_info**  list / elements=string | metadata about resource pool configuration  **Returned:** on success  **Sample:** `[{"cpu_allocation_expandable_reservation": false, "cpu_allocation_limit": 4121, "cpu_allocation_overhead_limit": null, "cpu_allocation_reservation": 4121, "cpu_allocation_shares": 9000, "cpu_allocation_shares_level": "custom", "mem_allocation_expandable_reservation": false, "mem_allocation_limit": 961, "mem_allocation_overhead_limit": null, "mem_allocation_reservation": 961, "mem_allocation_shares": 9000, "mem_allocation_shares_level": "custom", "name": "Resources", "overall_status": "green", "owner": "DC0_H0", "runtime_cpu_max_usage": 4121, "runtime_cpu_overall_usage": 0, "runtime_cpu_reservation_used": 0, "runtime_cpu_reservation_used_vm": 0, "runtime_cpu_unreserved_for_pool": 4121, "runtime_cpu_unreserved_for_vm": 4121, "runtime_memory_max_usage": 1007681536, "runtime_memory_overall_usage": 0, "runtime_memory_reservation_used": 0, "runtime_memory_reservation_used_vm": 0, "runtime_memory_unreserved_for_pool": 1007681536, "runtime_memory_unreserved_for_vm": 1007681536}]` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
