---
collection: ansible
version: "6"
title: "community.vmware.vmware_dvs_portgroup_find module – Find portgroup(s) in a VMware environment"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_dvs_portgroup_find_module.html
fetched_at: 2026-07-27T17:21:40+00:00
---
# community.vmware.vmware_dvs_portgroup_find module – Find portgroup(s) in a VMware environment

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
> To use it in a playbook, specify: `community.vmware.vmware_dvs_portgroup_find`.

- [Synopsis](vmware_dvs_portgroup_find_module.md#synopsis)
- [Parameters](vmware_dvs_portgroup_find_module.md#parameters)
- [Notes](vmware_dvs_portgroup_find_module.md#notes)
- [Examples](vmware_dvs_portgroup_find_module.md#examples)
- [Return Values](vmware_dvs_portgroup_find_module.md#return-values)

## [Synopsis](vmware_dvs_portgroup_find_module.md#id1)

- Find portgroup(s) based on different criteria such as distributed vSwitch, VLAN id or a string in the name.

## [Parameters](vmware_dvs_portgroup_find_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dvswitch**  string | Name of a distributed vSwitch to look for. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **name**  string | string to check inside the name of the portgroup.  Basic containment check using python `in` operation. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **show_uplink**  boolean | Show or hide uplink portgroups.  Only relevant when `vlanid` is supplied.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **vlanid**  integer | VLAN id can be any number between 1 and 4094.  This search criteria will looks into VLAN ranges to find possible matches. |

## [Notes](vmware_dvs_portgroup_find_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_dvs_portgroup_find_module.md#id4)

```yaml+jinja
- name: Get all portgroups in dvswitch vDS
  community.vmware.vmware_dvs_portgroup_find:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    dvswitch: 'vDS'
  delegate_to: localhost

- name: Confirm if vlan 15 is present
  community.vmware.vmware_dvs_portgroup_find:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    vlanid: '15'
  delegate_to: localhost
```

## [Return Values](vmware_dvs_portgroup_find_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dvs_portgroups**  list / elements=string | basic details of portgroups found  Returned: on success  Sample: `[{"dvswitch": "vDS", "name": "N-51", "pvlan": true, "trunk": true, "vlan_id": "0"}]` |

### Authors

- David Martinez (@dx0xm)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
