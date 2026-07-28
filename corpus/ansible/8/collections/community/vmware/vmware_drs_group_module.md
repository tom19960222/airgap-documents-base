---
collection: ansible
version: "8"
title: "community.vmware.vmware_drs_group module – Creates vm/host group in a given cluster."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_drs_group_module.html
fetched_at: 2026-07-28T01:59:52+00:00
---
# community.vmware.vmware_drs_group module – Creates vm/host group in a given cluster.

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
> To use it in a playbook, specify: `community.vmware.vmware_drs_group`.

- [Synopsis](vmware_drs_group_module.md#synopsis)
- [Parameters](vmware_drs_group_module.md#parameters)
- [Notes](vmware_drs_group_module.md#notes)
- [Examples](vmware_drs_group_module.md#examples)
- [Return Values](vmware_drs_group_module.md#return-values)

## [Synopsis](vmware_drs_group_module.md#id1)

- This module can be used to create VM/Host groups in a given cluster. Creates a vm group if `vms` is set. Creates a host group if `hosts` is set.

## [Parameters](vmware_drs_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string / required | Cluster to create vm/host group. |
| **datacenter**  aliases: datacenter_name  string | Datacenter to search for given cluster. If not set, we use first cluster we encounter with `cluster_name`. |
| **group_name**  string / required | The name of the group to create or remove. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **hosts**  list / elements=string | List of hosts to create in group.  Required only if `vms` is not set. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If set to `present` and the group doesn’t exists then the group will be created.  If set to `absent` and the group exists then the group will be deleted.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **vms**  list / elements=string | List of vms to create in group.  Required only if `hosts` is not set. |

## [Notes](vmware_drs_group_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_drs_group_module.md#id4)

```yaml+jinja
---
- name: "Create DRS VM group"
  delegate_to: localhost
  community.vmware.vmware_drs_group:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster_name: DC0_C0
    datacenter_name: DC0
    group_name: TEST_VM_01
    vms:
      - DC0_C0_RP0_VM0
      - DC0_C0_RP0_VM1
    state: present

- name: "Create DRS Host group"
  delegate_to: localhost
  community.vmware.vmware_drs_group:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster_name: DC0_C0
    datacenter_name: DC0
    group_name: TEST_HOST_01
    hosts:
      - DC0_C0_H0
      - DC0_C0_H1
      - DC0_C0_H2
    state: present

- name: "Delete DRS Host group"
  delegate_to: localhost
  community.vmware.vmware_drs_group:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster_name: DC0_C0
    datacenter_name: DC0
    group_name: TEST_HOST_01
    state: absent
```

## [Return Values](vmware_drs_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **drs_group_facts**  dictionary | Metadata about DRS group created  **Returned:** always  **Sample:** `{"drs_group_facts": {"changed": true, "failed": false, "msg": "Created host group TEST_HOST_01 successfully", "result": {"DC0_C0": [{"group_name": "TEST_HOST_01", "hosts": ["DC0_C0_H0", "DC0_C0_H1", "DC0_C0_H2"], "type": "host"}]}}}` |

### Authors

- Karsten Kaj Jakobsen (@karstenjakobsen)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
