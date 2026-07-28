---
collection: ansible
version: "8"
title: "community.vmware.vmware_drs_group_manager module – Manage VMs and Hosts in DRS group."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_drs_group_manager_module.html
fetched_at: 2026-07-28T01:59:53+00:00
---
# community.vmware.vmware_drs_group_manager module – Manage VMs and Hosts in DRS group.

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
> To use it in a playbook, specify: `community.vmware.vmware_drs_group_manager`.

- [Synopsis](vmware_drs_group_manager_module.md#synopsis)
- [Parameters](vmware_drs_group_manager_module.md#parameters)
- [Notes](vmware_drs_group_manager_module.md#notes)
- [Examples](vmware_drs_group_manager_module.md#examples)
- [Return Values](vmware_drs_group_manager_module.md#return-values)

## [Synopsis](vmware_drs_group_manager_module.md#id1)

- The module can be used to add VMs / Hosts to or remove them from a DRS group.

## [Parameters](vmware_drs_group_manager_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster**  aliases: cluster_name  string / required | Cluster to which DRS group associated with. |
| **datacenter**  aliases: datacenter_name  string | Name of the datacenter. |
| **group_name**  string / required | The name of the group to manage. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **hosts**  list / elements=string | A List of hosts to add / remove in the group.  Required only if *vms* is not set. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If set to `present`, VMs/hosts will be added to the given DRS group.  If set to `absent`, VMs/hosts will be removed from the given DRS group.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **vms**  list / elements=string | A List of vms to add / remove in the group.  Required only if *hosts* is not set. |

## [Notes](vmware_drs_group_manager_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_drs_group_manager_module.md#id4)

```yaml+jinja
---
- name: Add VMs in an existing DRS VM group
  delegate_to: localhost
  community.vmware.vmware_drs_group_manager:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster: DC0_C0
    datacenter: DC0
    group_name: TEST_VM_01
    vms:
      - DC0_C0_RP0_VM0
      - DC0_C0_RP0_VM1
    state: present

- name: Add Hosts in an existing DRS Host group
  delegate_to: localhost
  community.vmware.vmware_drs_group_manager:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster: DC0_C0
    datacenter: DC0
    group_name: TEST_HOST_01
    hosts:
      - DC0_C0_H0
      - DC0_C0_H1
      - DC0_C0_H2
    state: present

- name: Remove VM from an existing DRS VM group
  delegate_to: localhost
  community.vmware.vmware_drs_group_manager:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster: DC0_C0
    datacenter: DC0
    group_name: TEST_VM_01
    vms:
      - DC0_C0_RP0_VM0
    state: absent

- name: Remove host from an existing DRS Host group
  delegate_to: localhost
  community.vmware.vmware_drs_group_manager:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster: DC0_C0
    datacenter: DC0
    group_name: TEST_HOST_01
    hosts:
      - DC0_C0_H0
    state: absent
```

## [Return Values](vmware_drs_group_manager_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **drs_group_member_info**  dictionary | Metadata about DRS group  **Returned:** always  **Sample:** `{"Asia-Cluster1": [{"group_name": "vm_group_002", "type": "vm", "vms": ["dev-1"]}]}` |
| **msg**  string | Info message  **Returned:** always  **Sample:** `"Updated host group TEST_HOST_01 successfully"` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
