---
collection: ansible
version: "8"
title: "community.vmware.vmware_cluster_dpm module – Manage Distributed Power Management (DPM) on VMware vSphere clusters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_cluster_dpm_module.html
fetched_at: 2026-07-28T01:59:37+00:00
---
# community.vmware.vmware_cluster_dpm module – Manage Distributed Power Management (DPM) on VMware vSphere clusters

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
> To use it in a playbook, specify: `community.vmware.vmware_cluster_dpm`.

- [Synopsis](vmware_cluster_dpm_module.md#synopsis)
- [Parameters](vmware_cluster_dpm_module.md#parameters)
- [Notes](vmware_cluster_dpm_module.md#notes)
- [Examples](vmware_cluster_dpm_module.md#examples)

## [Synopsis](vmware_cluster_dpm_module.md#id1)

- Manages DPM on VMware vSphere clusters.
- All values and VMware object names are case sensitive.

## [Parameters](vmware_cluster_dpm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string / required | The name of the cluster to be managed. |
| **datacenter**  aliases: datacenter_name  string / required | The name of the datacenter. |
| **default_dpm_behaviour**  string | Whether dpm should be automated or manual  **Choices:**   - `"automated"` ← (default) - `"manual"` |
| **enable_dpm**  boolean | Whether to enable DPM.  **Choices:**   - `false` ← (default) - `true` |
| **host_power_action_rate**  integer | specify host power action rate  1 is the lowest and 5 the highest  **Choices:**   - `1` - `2` - `3` ← (default) - `4` - `5` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_cluster_dpm_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_cluster_dpm_module.md#id4)

```yaml+jinja
- name: Enable DPM
  community.vmware.vmware_cluster_dpm:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
    enable_dpm: true
    default_dpm_behaviour: automated
    host_power_action_rate: 2
  delegate_to: localhost
```

### Authors

- Olivia Luetolf (@olilu)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
