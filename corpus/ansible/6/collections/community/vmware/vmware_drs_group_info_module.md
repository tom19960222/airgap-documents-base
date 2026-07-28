---
collection: ansible
version: "6"
title: "community.vmware.vmware_drs_group_info module – Gathers info about DRS VM/Host groups on the given cluster"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_drs_group_info_module.html
fetched_at: 2026-07-27T17:21:37+00:00
---
# community.vmware.vmware_drs_group_info module – Gathers info about DRS VM/Host groups on the given cluster

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
> To use it in a playbook, specify: `community.vmware.vmware_drs_group_info`.

- [Synopsis](vmware_drs_group_info_module.md#synopsis)
- [Parameters](vmware_drs_group_info_module.md#parameters)
- [Notes](vmware_drs_group_info_module.md#notes)
- [Examples](vmware_drs_group_info_module.md#examples)
- [Return Values](vmware_drs_group_info_module.md#return-values)

## [Synopsis](vmware_drs_group_info_module.md#id1)

- This module can be used to gather information about DRS VM/HOST groups from the given cluster.

## [Parameters](vmware_drs_group_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Cluster to search for VM/Host groups.  If set, information of DRS groups belonging this cluster will be returned.  Not needed if `datacenter` is set. |
| **datacenter**  aliases: datacenter_name  string | Datacenter to search for DRS VM/Host groups. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_drs_group_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_drs_group_info_module.md#id4)

```yaml+jinja
---
- name: "Gather DRS info about given Cluster"
  register: cluster_drs_group_info
  community.vmware.vmware_drs_group_info:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster_name: "{{ cluster_name }}"
  delegate_to: localhost

- name: "Gather DRS group info about all clusters in given datacenter"
  register: cluster_drs_group_info
  community.vmware.vmware_drs_group_info:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    datacenter: "{{ datacenter }}"
  delegate_to: localhost
```

## [Return Values](vmware_drs_group_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **drs_group_info**  dictionary | Metadata about DRS group from given cluster / datacenter  Returned: always  Sample: `{"drs_group_info": {"DC0_C0": [{"group_name": "GROUP_HOST_S01", "hosts": ["vm-01.zone", "vm-02.zone"], "type": "host"}, {"group_name": "GROUP_HOST_S02", "hosts": ["vm-03.zone", "vm-04.zone"], "type": "host"}, {"group_name": "GROUP_VM_S01", "type": "vm", "vms": ["test-node01"]}, {"group_name": "GROUP_VM_S02", "type": "vm", "vms": ["test-node02"]}], "DC0_C1": []}}` |

### Authors

- Karsten Kaj Jakobsen (@karstenjakobsen)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
