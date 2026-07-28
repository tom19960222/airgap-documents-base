---
collection: ansible
version: "8"
title: "community.vmware.vmware_drs_rule_info module – Gathers info about DRS rule on the given cluster"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_drs_rule_info_module.html
fetched_at: 2026-07-28T01:59:54+00:00
---
# community.vmware.vmware_drs_rule_info module – Gathers info about DRS rule on the given cluster

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
> To use it in a playbook, specify: `community.vmware.vmware_drs_rule_info`.

- [Synopsis](vmware_drs_rule_info_module.md#synopsis)
- [Parameters](vmware_drs_rule_info_module.md#parameters)
- [Notes](vmware_drs_rule_info_module.md#notes)
- [Examples](vmware_drs_rule_info_module.md#examples)
- [Return Values](vmware_drs_rule_info_module.md#return-values)

## [Synopsis](vmware_drs_rule_info_module.md#id1)

- This module can be used to gather information about DRS VM-VM and VM-HOST rules from the given cluster.

## [Parameters](vmware_drs_rule_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster.  DRS information for the given cluster will be returned.  This is required parameter if `datacenter` parameter is not provided. |
| **datacenter**  string | Name of the datacenter.  DRS information for all the clusters from the given datacenter will be returned.  This is required parameter if `cluster_name` parameter is not provided. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_drs_rule_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_drs_rule_info_module.md#id4)

```yaml+jinja
- name: Gather DRS info about given Cluster
  community.vmware.vmware_drs_rule_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
  register: cluster_drs_info

- name: Gather DRS info about all Clusters in given datacenter
  community.vmware.vmware_drs_rule_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter_name }}'
  delegate_to: localhost
  register: datacenter_drs_info
```

## [Return Values](vmware_drs_rule_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **drs_rule_info**  dictionary | metadata about DRS rule from given cluster / datacenter  **Returned:** always  **Sample:** `{"DC0_C0": [{"rule_affinity": false, "rule_enabled": true, "rule_key": 1, "rule_mandatory": true, "rule_name": "drs_rule_0001", "rule_type": "vm_vm_rule", "rule_uuid": "52be5061-665a-68dc-3d25-85cd2d37e114", "rule_vms": ["VM_65", "VM_146"]}], "DC1_C1": [{"rule_affine_host_group_name": "host_group_1", "rule_affine_hosts": ["10.76.33.204"], "rule_anti_affine_host_group_name": null, "rule_anti_affine_hosts": [], "rule_enabled": true, "rule_key": 1, "rule_mandatory": false, "rule_name": "vm_host_rule_0001", "rule_type": "vm_host_rule", "rule_uuid": "52687108-4d3a-76f2-d29c-b708c40dbe40", "rule_vm_group_name": "test_vm_group_1", "rule_vms": ["VM_8916", "VM_4010"]}]}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
