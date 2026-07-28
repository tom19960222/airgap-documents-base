---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_vmhba_info module – Gathers info about vmhbas available on the given ESXi host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_vmhba_info_module.html
fetched_at: 2026-07-28T02:00:58+00:00
---
# community.vmware.vmware_host_vmhba_info module – Gathers info about vmhbas available on the given ESXi host

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
> To use it in a playbook, specify: `community.vmware.vmware_host_vmhba_info`.

- [Synopsis](vmware_host_vmhba_info_module.md#synopsis)
- [Parameters](vmware_host_vmhba_info_module.md#parameters)
- [Notes](vmware_host_vmhba_info_module.md#notes)
- [Examples](vmware_host_vmhba_info_module.md#examples)
- [Return Values](vmware_host_vmhba_info_module.md#return-values)

## [Synopsis](vmware_host_vmhba_info_module.md#id1)

- This module can be used to gather information about vmhbas available on the given ESXi host.
- If `cluster_name` is provided, then vmhba information about all hosts from given cluster will be returned.
- If `esxi_hostname` is provided, then vmhba information about given host system will be returned.

## [Parameters](vmware_host_vmhba_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster from which all host systems will be used.  Vmhba information about each ESXi server will be returned for the given cluster.  This parameter is required if `esxi_hostname` is not specified. |
| **esxi_hostname**  string | Name of the host system to work with.  Vmhba information about this ESXi server will be returned.  This parameter is required if `cluster_name` is not specified. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_host_vmhba_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_vmhba_info_module.md#id4)

```yaml+jinja
- name: Gather info about vmhbas of all ESXi Host in the given Cluster
  community.vmware.vmware_host_vmhba_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
  register: cluster_host_vmhbas

- name: Gather info about vmhbas of an ESXi Host
  community.vmware.vmware_host_vmhba_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
  register: host_vmhbas
```

## [Return Values](vmware_host_vmhba_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hosts_vmhbas_info**  dictionary | dict with hostname as key and dict with vmhbas information as value.  **Returned:** hosts_vmhbas_info  **Sample:** `{"10.76.33.204": {"vmhba_details": [{"adapter": "HPE Smart Array P440ar", "bus": 3, "device": "vmhba0", "driver": "nhpsa", "location": "0000:03:00.0", "model": "Smart Array P440ar", "node_wwn": "50:01:43:80:37:18:9e:a0", "status": "unknown", "type": "SAS"}, {"adapter": "QLogic Corp ISP2532-based 8Gb Fibre Channel to PCI Express HBA", "bus": 5, "device": "vmhba1", "driver": "qlnativefc", "location": "0000:05:00.0", "model": "ISP2532-based 8Gb Fibre Channel to PCI Express HBA", "node_wwn": "57:64:96:32:15:90:23:95:82", "port_type": "unknown", "port_wwn": "57:64:96:32:15:90:23:95:82", "speed": 8, "status": "online", "type": "Fibre Channel"}, {"adapter": "QLogic Corp ISP2532-based 8Gb Fibre Channel to PCI Express HBA", "bus": 8, "device": "vmhba2", "driver": "qlnativefc", "location": "0000:08:00.0", "model": "ISP2532-based 8Gb Fibre Channel to PCI Express HBA", "node_wwn": "57:64:96:32:15:90:23:95:21", "port_type": "unknown", "port_wwn": "57:64:96:32:15:90:23:95:21", "speed": 8, "status": "online", "type": "Fibre Channel"}]}}` |

### Authors

- Christian Kotte (@ckotte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
