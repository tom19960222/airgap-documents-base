---
collection: ansible
version: "8"
title: "community.vmware.vmware_cluster_vsan module – Manages virtual storage area network (vSAN) configuration on VMware vSphere clusters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_cluster_vsan_module.html
fetched_at: 2026-07-28T01:59:41+00:00
---
# community.vmware.vmware_cluster_vsan module – Manages virtual storage area network (vSAN) configuration on VMware vSphere clusters

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this module,
> see [Requirements](vmware_cluster_vsan_module.md#ansible-collections-community-vmware-vmware-cluster-vsan-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_cluster_vsan`.

- [Synopsis](vmware_cluster_vsan_module.md#synopsis)
- [Requirements](vmware_cluster_vsan_module.md#requirements)
- [Parameters](vmware_cluster_vsan_module.md#parameters)
- [Notes](vmware_cluster_vsan_module.md#notes)
- [Examples](vmware_cluster_vsan_module.md#examples)

## [Synopsis](vmware_cluster_vsan_module.md#id1)

- Manages vSAN on VMware vSphere clusters.
- All values and VMware object names are case sensitive.

## [Requirements](vmware_cluster_vsan_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSAN Management SDK, which needs to be downloaded from VMware and installed manually.

## [Parameters](vmware_cluster_vsan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **advanced_options**  dictionary | Advanced VSAN Options. |
| **automatic_rebalance**  boolean | If enabled, vSAN automatically rebalances (moves the data among disks) when a capacity disk fullness hits proactive rebalance threshold.  **Choices:**   - `false` - `true` |
| **disable_site_read_locality**  boolean | For vSAN stretched clusters, reads to vSAN objects occur on the site the VM resides on.  Setting to `true` will force reads across all mirrors.  **Choices:**   - `false` - `true` |
| **large_cluster_support**  boolean | Allow > 32 VSAN hosts per cluster; if this is changed on an existing vSAN cluster, all hosts are required to reboot to apply this change.  **Choices:**   - `false` - `true` |
| **object_repair_timer**  integer | Delay time in minutes for VSAN to wait for the absent component to come back before starting to repair it. |
| **thin_swap**  boolean | When `enabled`, swap objects would not reserve 100% space of their size on vSAN datastore.  **Choices:**   - `false` - `true` |
| **cluster_name**  string / required | The name of the cluster to be managed. |
| **datacenter**  aliases: datacenter_name  string / required | The name of the datacenter. |
| **enable**  boolean | Whether to enable vSAN.  **Choices:**   - `false` - `true` ← (default) |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **vsan_auto_claim_storage**  boolean | Whether the VSAN service is configured to automatically claim local storage on VSAN-enabled hosts in the cluster.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](vmware_cluster_vsan_module.md#id4)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_cluster_vsan_module.md#id5)

```yaml+jinja
- name: Enable vSAN
  community.vmware.vmware_cluster_vsan:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
    enable: true
  delegate_to: localhost

- name: Enable vSAN and automatic rebalancing
  community.vmware.vmware_cluster_vsan:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
    enable: true
    advanced_options:
      automatic_rebalance: true
  delegate_to: localhost

- name: Enable vSAN and claim storage automatically
  community.vmware.vmware_cluster_vsan:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter_name: DC0
    cluster_name: "{{ cluster_name }}"
    enable: true
    vsan_auto_claim_storage: true
  delegate_to: localhost
```

### Authors

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
- Mario Lenz (@mariolenz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
