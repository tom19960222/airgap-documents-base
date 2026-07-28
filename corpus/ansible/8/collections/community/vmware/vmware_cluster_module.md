---
collection: ansible
version: "8"
title: "community.vmware.vmware_cluster module – Manage VMware vSphere clusters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_cluster_module.html
fetched_at: 2026-07-28T01:59:36+00:00
---
# community.vmware.vmware_cluster module – Manage VMware vSphere clusters

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
> To use it in a playbook, specify: `community.vmware.vmware_cluster`.

- [Synopsis](vmware_cluster_module.md#synopsis)
- [Parameters](vmware_cluster_module.md#parameters)
- [Notes](vmware_cluster_module.md#notes)
- [See Also](vmware_cluster_module.md#see-also)
- [Examples](vmware_cluster_module.md#examples)

## [Synopsis](vmware_cluster_module.md#id1)

- Adds or removes VMware vSphere clusters.
- To manage DRS, HA and VSAN related configurations, use the new modules vmware_cluster_drs, vmware_cluster_ha and vmware_cluster_vsan.
- All values and VMware object names are case sensitive.

## [Parameters](vmware_cluster_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string / required | The name of the cluster to be managed. |
| **datacenter**  aliases: datacenter_name  string / required | The name of the datacenter. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | Create `present` or remove `absent` a VMware vSphere cluster.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_cluster_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [See Also](vmware_cluster_module.md#id4)

> **See also:**
>
> [community.vmware.vmware_cluster_drs](vmware_cluster_drs_module.md#ansible-collections-community-vmware-vmware-cluster-drs-module)
> :   Manage Distributed Resource Scheduler (DRS) on VMware vSphere clusters.
>
> [community.vmware.vmware_cluster_ha](vmware_cluster_ha_module.md#ansible-collections-community-vmware-vmware-cluster-ha-module)
> :   Manage High Availability (HA) on VMware vSphere clusters.
>
> [community.vmware.vmware_cluster_vsan](vmware_cluster_vsan_module.md#ansible-collections-community-vmware-vmware-cluster-vsan-module)
> :   Manages virtual storage area network (vSAN) configuration on VMware vSphere clusters.

## [Examples](vmware_cluster_module.md#id5)

```yaml+jinja
- name: Create Cluster
  community.vmware.vmware_cluster:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
  delegate_to: localhost

- name: Delete Cluster
  community.vmware.vmware_cluster:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter_name: datacenter
    cluster_name: cluster
    state: absent
  delegate_to: localhost
```

### Authors

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
