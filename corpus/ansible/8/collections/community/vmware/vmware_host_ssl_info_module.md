---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_ssl_info module – Gather info of ESXi host system about SSL"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_ssl_info_module.html
fetched_at: 2026-07-28T02:00:56+00:00
---
# community.vmware.vmware_host_ssl_info module – Gather info of ESXi host system about SSL

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
> To use it in a playbook, specify: `community.vmware.vmware_host_ssl_info`.

- [Synopsis](vmware_host_ssl_info_module.md#synopsis)
- [Parameters](vmware_host_ssl_info_module.md#parameters)
- [Notes](vmware_host_ssl_info_module.md#notes)
- [Examples](vmware_host_ssl_info_module.md#examples)
- [Return Values](vmware_host_ssl_info_module.md#return-values)

## [Synopsis](vmware_host_ssl_info_module.md#id1)

- This module can be used to gather information of the SSL thumbprint information for a host.

## [Parameters](vmware_host_ssl_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster.  SSL thumbprint information about all ESXi host system in the given cluster will be reported.  If `esxi_hostname` is not given, this parameter is required. |
| **esxi_hostname**  string | ESXi hostname.  SSL thumbprint information of this ESXi host system will be reported.  If `cluster_name` is not given, this parameter is required. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_host_ssl_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_ssl_info_module.md#id4)

```yaml+jinja
- name: Gather SSL thumbprint information about all ESXi Hosts in given Cluster
  community.vmware.vmware_host_ssl_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
  register: all_host_ssl_info

- name: Get SSL Thumbprint info about "{{ esxi_hostname }}"
  community.vmware.vmware_host_ssl_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: '{{ esxi_hostname }}'
  register: ssl_info
- set_fact:
    ssl_thumbprint: "{{ ssl_info['host_ssl_info'][esxi_hostname]['ssl_thumbprints'][0] }}"
- debug:
    msg: "{{ ssl_thumbprint }}"
- name: Add ESXi Host to vCenter
  vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    cluster_name: '{{ cluster_name }}'
    esxi_hostname: '{{ esxi_hostname }}'
    esxi_username: '{{ esxi_username }}'
    esxi_password: '{{ esxi_password }}'
    esxi_ssl_thumbprint: '{{ ssl_thumbprint }}'
    state: present
```

## [Return Values](vmware_host_ssl_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **host_ssl_info**  dictionary | dict with hostname as key and dict with SSL thumbprint related info  **Returned:** info  **Sample:** `{"10.76.33.215": {"owner_tag": "", "principal": "vpxuser", "ssl_thumbprints": ["E3:E8:A9:20:8D:32:AE:59:C6:8D:A5:91:B0:20:EF:00:A2:7C:27:EE", "F1:AC:DA:6E:D8:1E:37:36:4A:5C:07:E5:04:0B:87:C8:75:FB:42:01"]}}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
