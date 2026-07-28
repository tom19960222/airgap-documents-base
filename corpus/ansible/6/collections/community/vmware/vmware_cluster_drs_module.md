---
collection: ansible
version: "6"
title: "community.vmware.vmware_cluster_drs module – Manage Distributed Resource Scheduler (DRS) on VMware vSphere clusters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_cluster_drs_module.html
fetched_at: 2026-07-27T17:21:24+00:00
---
# community.vmware.vmware_cluster_drs module – Manage Distributed Resource Scheduler (DRS) on VMware vSphere clusters

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
> To use it in a playbook, specify: `community.vmware.vmware_cluster_drs`.

- [Synopsis](vmware_cluster_drs_module.md#synopsis)
- [Parameters](vmware_cluster_drs_module.md#parameters)
- [Notes](vmware_cluster_drs_module.md#notes)
- [Examples](vmware_cluster_drs_module.md#examples)

## [Synopsis](vmware_cluster_drs_module.md#id1)

- Manages DRS on VMware vSphere clusters.
- All values and VMware object names are case sensitive.

## [Parameters](vmware_cluster_drs_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **advanced_settings**  dictionary | A dictionary of advanced DRS settings.  Default: `{}` |
| **cluster_name**  string / required | The name of the cluster to be managed. |
| **datacenter**  aliases: datacenter_name  string / required | The name of the datacenter. |
| **drs_default_vm_behavior**  string | Specifies the cluster-wide default DRS behavior for virtual machines.  If set to `partiallyAutomated`, vCenter generates recommendations for virtual machine migration and for the placement with a host, then automatically implements placement recommendations at power on.  If set to `manual`, then vCenter generates recommendations for virtual machine migration and for the placement with a host, but does not implement the recommendations automatically.  If set to `fullyAutomated`, then vCenter automates both the migration of virtual machines and their placement with a host at power on.  Choices:   - `"fullyAutomated"` ← (default) - `"manual"` - `"partiallyAutomated"` |
| **drs_enable_vm_behavior_overrides**  boolean | Whether DRS Behavior overrides for individual virtual machines are enabled.  If set to `True`, overrides `drs_default_vm_behavior`.  Choices:   - `false` - `true` ← (default) |
| **drs_vmotion_rate**  integer | Threshold for generated ClusterRecommendations.  Choices:   - `1` - `2` - `3` ← (default) - `4` - `5` |
| **enable**  boolean | Whether to enable DRS.  Choices:   - `false` - `true` ← (default) |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_cluster_drs_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_cluster_drs_module.md#id4)

```yaml+jinja
- name: Enable DRS
  community.vmware.vmware_cluster_drs:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
    enable: true
  delegate_to: localhost

- name: Enable DRS and distribute a more even number of virtual machines across hosts for availability
  community.vmware.vmware_cluster_drs:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
    enable: true
    advanced_settings:
      'TryBalanceVmsPerHost': '1'
  delegate_to: localhost

- name: Enable DRS and set default VM behavior to partially automated
  community.vmware.vmware_cluster_drs:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter_name: DC0
    cluster_name: "{{ cluster_name }}"
    enable: True
    drs_default_vm_behavior: partiallyAutomated
  delegate_to: localhost
```

### Authors

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
