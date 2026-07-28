---
collection: ansible
version: "8"
title: "community.vmware.vmware_datacenter_info module – Gather information about VMware vSphere Datacenters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_datacenter_info_module.html
fetched_at: 2026-07-28T01:59:47+00:00
---
# community.vmware.vmware_datacenter_info module – Gather information about VMware vSphere Datacenters

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
> To use it in a playbook, specify: `community.vmware.vmware_datacenter_info`.

- [Synopsis](vmware_datacenter_info_module.md#synopsis)
- [Parameters](vmware_datacenter_info_module.md#parameters)
- [Notes](vmware_datacenter_info_module.md#notes)
- [Examples](vmware_datacenter_info_module.md#examples)
- [Return Values](vmware_datacenter_info_module.md#return-values)

## [Synopsis](vmware_datacenter_info_module.md#id1)

- This module can be used to gather information VMware vSphere Datacenters.

## [Parameters](vmware_datacenter_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  aliases: datacenter_name  string | The name of the datacenter to gather information for.  If not provided, will gather information about all datacenters from the VMware infra. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **properties**  list / elements=string | Specify the properties to retrieve.  If not specified, all properties are retrieved (deeply).  Results are returned in a structure identical to the vSphere API.  Example:  properties: [  “overallStatus”  ]  Only valid when `schema` is `vsphere`. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **schema**  string | Specify the output schema desired.  The ‘summary’ output schema is the legacy output from the module.  The ‘vsphere’ output schema is the vSphere API class definition which requires pyvmomi>6.7.1.  **Choices:**   - `"summary"` ← (default) - `"vsphere"` |
| **show_tag**  boolean | Tags related to Datacenter are shown if set to `true`.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_datacenter_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_datacenter_info_module.md#id4)

```yaml+jinja
- name: Gather information about all datacenters
  community.vmware.vmware_datacenter_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost

- name: Gather information about a particular datacenter
  community.vmware.vmware_datacenter_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter_name }}'
  delegate_to: localhost

- name: Gather information about a particular datacenter
  community.vmware.vmware_datacenter_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter_name }}'
    show_tag: true
  delegate_to: localhost

- name: Gather vSphere schema information
  community.vmware.vmware_datacenter_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter_name }}'
    schema: vsphere
    properties:
    - configStatus
    - overallStatus
```

## [Return Values](vmware_datacenter_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **datacenter_info**  list / elements=string | Information about datacenter  **Returned:** always  **Sample:** `[{"configStatus": "gray", "moid": "datacenter-2", "name": "Asia-Datacenter1"}]` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
