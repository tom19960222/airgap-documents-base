---
collection: ansible
version: "6"
title: "community.vmware.vmware_vsan_health_info module – Gather information about a VMware vSAN cluster’s health"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_vsan_health_info_module.html
fetched_at: 2026-07-27T17:23:01+00:00
---
# community.vmware.vmware_vsan_health_info module – Gather information about a VMware vSAN cluster’s health

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/community/vmware) (version 2.10.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this module,
> see [Requirements](vmware_vsan_health_info_module.md#ansible-collections-community-vmware-vmware-vsan-health-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_vsan_health_info`.

- [Synopsis](vmware_vsan_health_info_module.md#synopsis)
- [Requirements](vmware_vsan_health_info_module.md#requirements)
- [Parameters](vmware_vsan_health_info_module.md#parameters)
- [Notes](vmware_vsan_health_info_module.md#notes)
- [Examples](vmware_vsan_health_info_module.md#examples)
- [Return Values](vmware_vsan_health_info_module.md#return-values)

## [Synopsis](vmware_vsan_health_info_module.md#id1)

- Gather information about a VMware vSAN cluster’s health.

## [Requirements](vmware_vsan_health_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- VMware vSAN Python’s SDK

## [Parameters](vmware_vsan_health_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string / required | Name of the vSAN cluster. |
| **datacenter**  aliases: datacenter_name  string  added in community.vmware 1.6.0 | Name of the Datacenter. |
| **fetch_from_cache**  boolean | `True` to return the result from cache directly instead of running the full health check.  Choices:   - `false` ← (default) - `true` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_vsan_health_info_module.md#id4)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vsan_health_info_module.md#id5)

```yaml+jinja
- name: Gather health info from a vSAN's cluster
  community.vmware.vmware_vsan_health_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    cluster_name: 'vSAN01'
    fetch_from_cache: False

- name: Gather health info from a vSAN's cluster with datacenter
  community.vmware.vmware_vsan_health_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    cluster_name: 'vSAN01'
    datacenter: 'Datacenter_01'
    fetch_from_cache: True
```

## [Return Values](vmware_vsan_health_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vsan_health_info**  dictionary | vSAN cluster health info  Returned: on success  Sample: `{"_vimtype": "vim.cluster.VsanClusterHealthSummary", "burnInTest": null, "clusterStatus": {"_vimtype": "vim.cluster.VsanClusterHealthSystemStatusResult", "goalState": "installed", "status": "green", "trackedHostsStatus": [{"_vimtype": "vim.host.VsanHostHealthSystemStatusResult", "hostname": "esxi01.example.com", "issues": [], "status": "green"}, {"_vimtype": "vim.host.VsanHostHealthSystemStatusResult", "hostname": "esxi04.example.com", "issues": [], "status": "green"}, {"_vimtype": "vim.host.VsanHostHealthSystemStatusResult", "hostname": "esxi02.example.com", "issues": [], "status": "green"}, {"_vimtype": "vim.host.VsanHostHealthSystemStatusResult", "hostname": "esxi03.example.com", "issues": [], "status": "green"}], "untrackedHosts": []}}` |

### Authors

- Erwan Quelin (@equelin)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
