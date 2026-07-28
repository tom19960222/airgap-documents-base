---
collection: ansible
version: "6"
title: "community.vmware.vmware_host_acceptance module – Manage the host acceptance level of an ESXi host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_host_acceptance_module.html
fetched_at: 2026-07-27T17:22:11+00:00
---
# community.vmware.vmware_host_acceptance module – Manage the host acceptance level of an ESXi host

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
> To use it in a playbook, specify: `community.vmware.vmware_host_acceptance`.

- [Synopsis](vmware_host_acceptance_module.md#synopsis)
- [Parameters](vmware_host_acceptance_module.md#parameters)
- [Notes](vmware_host_acceptance_module.md#notes)
- [Examples](vmware_host_acceptance_module.md#examples)
- [Return Values](vmware_host_acceptance_module.md#return-values)

## [Synopsis](vmware_host_acceptance_module.md#id1)

- This module can be used to manage the host acceptance level of an ESXi host.
- The host acceptance level controls the acceptance level of each VIB on a ESXi host.

## [Parameters](vmware_host_acceptance_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **acceptance_level**  string | Name of acceptance level.  If set to `partner`, then accept only partner and VMware signed and certified VIBs.  If set to `vmware_certified`, then accept only VIBs that are signed and certified by VMware.  If set to `vmware_accepted`, then accept VIBs that have been accepted by VMware.  If set to `community`, then accept all VIBs, even those that are not signed.  Choices:   - `"community"` - `"partner"` - `"vmware_accepted"` - `"vmware_certified"` |
| **cluster_name**  string | Name of the cluster.  Acceptance level of all ESXi host system in the given cluster will be managed.  If `esxi_hostname` is not given, this parameter is required. |
| **esxi_hostname**  string | ESXi hostname.  Acceptance level of this ESXi host system will be managed.  If `cluster_name` is not given, this parameter is required. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | Set or list acceptance level of the given ESXi host.  If set to `list`, then will return current acceptance level of given host system/s.  If set to `present`, then will set given acceptance level.  Choices:   - `"list"` ← (default) - `"present"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_host_acceptance_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_acceptance_module.md#id4)

```yaml+jinja
- name: Set acceptance level to community for all ESXi Host in given Cluster
  community.vmware.vmware_host_acceptance:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: cluster_name
    acceptance_level: 'community'
    state: present
  delegate_to: localhost
  register: cluster_acceptance_level

- name: Set acceptance level to vmware_accepted for the given ESXi Host
  community.vmware.vmware_host_acceptance:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    acceptance_level: 'vmware_accepted'
    state: present
  delegate_to: localhost
  register: host_acceptance_level

- name: Get acceptance level from the given ESXi Host
  community.vmware.vmware_host_acceptance:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: list
  delegate_to: localhost
  register: host_acceptance_level
```

## [Return Values](vmware_host_acceptance_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **facts**  dictionary | dict with hostname as key and dict with acceptance level facts, error as value  Returned: facts  Sample: `{"facts": {"localhost.localdomain": {"error": "NA", "level": "vmware_certified"}}}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
