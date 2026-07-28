---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_powermgmt_policy module – Manages the Power Management Policy of an ESXI host system"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_powermgmt_policy_module.html
fetched_at: 2026-07-27T17:22:29+00:00
---
# community.vmware.vmware_host_powermgmt_policy module – Manages the Power Management Policy of an ESXI host system

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
> To use it in a playbook, specify: `community.vmware.vmware_host_powermgmt_policy`.

- [Synopsis](vmware_host_powermgmt_policy_module.md#synopsis)
- [Parameters](vmware_host_powermgmt_policy_module.md#parameters)
- [Notes](vmware_host_powermgmt_policy_module.md#notes)
- [Examples](vmware_host_powermgmt_policy_module.md#examples)
- [Return Values](vmware_host_powermgmt_policy_module.md#return-values)

## [Synopsis](vmware_host_powermgmt_policy_module.md#id1)

- This module can be used to manage the Power Management Policy of ESXi host systems in given vCenter infrastructure.

## [Parameters](vmware_host_powermgmt_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster from which all host systems will be used.  This is required parameter if `esxi_hostname` is not specified. |
| **esxi_hostname**  string | Name of the host system to work with.  This is required parameter if `cluster_name` is not specified. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **policy**  string | Set the Power Management Policy of the host system.  Choices:   - `"high-performance"` - `"balanced"` ← (default) - `"low-power"` - `"custom"` |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_host_powermgmt_policy_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_powermgmt_policy_module.md#id4)

```yaml+jinja
- name: Set the Power Management Policy of a host system to high-performance
  community.vmware.vmware_host_powermgmt_policy:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_host }}'
    policy: high-performance
  delegate_to: localhost

- name: Set the Power Management Policy of all host systems from cluster to high-performance
  community.vmware.vmware_host_powermgmt_policy:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    policy: high-performance
  delegate_to: localhost
```

## [Return Values](vmware_host_powermgmt_policy_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | metadata about host system’s Power Management Policy  Returned: always  Sample: `{"changed": true, "result": {"esxi01": {"changed": true, "current_state": "high-performance", "desired_state": "high-performance", "msg": "Power policy changed", "previous_state": "balanced"}}}` |

### Authors

- Christian Kotte (@ckotte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
