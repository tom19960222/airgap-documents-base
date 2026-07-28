---
collection: ansible
version: "8"
title: "community.vmware.vmware_vm_info module – Return basic info pertaining to a VMware machine guest"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_vm_info_module.html
fetched_at: 2026-07-28T02:01:19+00:00
---
# community.vmware.vmware_vm_info module – Return basic info pertaining to a VMware machine guest

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
> To use it in a playbook, specify: `community.vmware.vmware_vm_info`.

- [Synopsis](vmware_vm_info_module.md#synopsis)
- [Parameters](vmware_vm_info_module.md#parameters)
- [Notes](vmware_vm_info_module.md#notes)
- [Examples](vmware_vm_info_module.md#examples)
- [Return Values](vmware_vm_info_module.md#return-values)

## [Synopsis](vmware_vm_info_module.md#id1)

- Return basic information pertaining to a vSphere or ESXi virtual machine guest.
- Cluster name as fact is added in version 2.7.

## [Parameters](vmware_vm_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **folder**  string | Specify a folder location of VMs to gather information from.  Examples:  folder: /ha-datacenter/vm  folder: ha-datacenter/vm  folder: /datacenter1/vm  folder: datacenter1/vm  folder: /datacenter1/vm/folder1  folder: datacenter1/vm/folder1  folder: /folder1/datacenter1/vm  folder: folder1/datacenter1/vm  folder: /folder1/datacenter1/vm/folder2 |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **show_allocated**  boolean  *added in community.vmware 2.5.0* | Allocated storage in byte and memory in MB are shown if it set to True.  **Choices:**   - `false` ← (default) - `true` |
| **show_attribute**  boolean | Attributes related to VM guest shown in information only when this is set `true`.  **Choices:**   - `false` ← (default) - `true` |
| **show_cluster**  boolean  *added in community.vmware 3.5.0* | Tags virtual machine’s cluster is shown if set to `true`.  **Choices:**   - `false` - `true` ← (default) |
| **show_datacenter**  boolean  *added in community.vmware 3.5.0* | Tags virtual machine’s datacenter is shown if set to `true`.  **Choices:**   - `false` - `true` ← (default) |
| **show_datastore**  boolean  *added in community.vmware 3.5.0* | Tags virtual machine’s datastore is shown if set to `true`.  **Choices:**   - `false` - `true` ← (default) |
| **show_esxi_hostname**  boolean  *added in community.vmware 3.5.0* | Tags virtual machine’s ESXi host is shown if set to `true`.  **Choices:**   - `false` - `true` ← (default) |
| **show_folder**  boolean  *added in community.vmware 3.7.0* | Show folders  **Choices:**   - `false` - `true` ← (default) |
| **show_mac_address**  boolean  *added in community.vmware 3.5.0* | Tags virtual machine’s mac address is shown if set to `true`.  **Choices:**   - `false` - `true` ← (default) |
| **show_net**  boolean  *added in community.vmware 3.5.0* | Tags virtual machine’s network is shown if set to `true`.  **Choices:**   - `false` - `true` ← (default) |
| **show_resource_pool**  boolean  *added in community.vmware 3.5.0* | Tags virtual machine’s resource pool is shown if set to `true`.  **Choices:**   - `false` - `true` ← (default) |
| **show_tag**  boolean | Tags related to virtual machine are shown if set to `true`.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **vm_name**  string | Name of the virtual machine to get related configurations information from. |
| **vm_type**  string | If set to `vm`, then information are gathered for virtual machines only.  If set to `template`, then information are gathered for virtual machine templates only.  If set to `all`, then information are gathered for all virtual machines and virtual machine templates.  **Choices:**   - `"all"` ← (default) - `"vm"` - `"template"` |

## [Notes](vmware_vm_info_module.md#id3)

> **Note:**
>
> - Fact about `moid` added in VMware collection 1.4.0.
> - Fact about `datastore_url` is added in VMware collection 1.18.0.
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_vm_info_module.md#id4)

```yaml+jinja
- name: Gather all registered virtual machines
  community.vmware.vmware_vm_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost
  register: vminfo

- debug:
    var: vminfo.virtual_machines

- name: Gather one specific VM
  community.vmware.vmware_vm_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    vm_name: 'vm_name_as_per_vcenter'
  delegate_to: localhost
  register: vm_info

- debug:
    var: vminfo.virtual_machines

- name: Gather only registered virtual machine templates
  community.vmware.vmware_vm_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    vm_type: template
  delegate_to: localhost
  register: template_info

- debug:
    var: template_info.virtual_machines

- name: Gather only registered virtual machines
  community.vmware.vmware_vm_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    vm_type: vm
  delegate_to: localhost
  register: vm_info

- debug:
    var: vm_info.virtual_machines

- name: Get UUID from given VM Name
  block:
    - name: Get virtual machine info
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        folder: "/datacenter/vm/folder"
      delegate_to: localhost
      register: vm_info

    - debug:
        msg: "{{ item.uuid }}"
      with_items:
        - "{{ vm_info.virtual_machines | community.general.json_query(query) }}"
      vars:
        query: "[?guest_name=='DC0_H0_VM0']"

- name: Get Tags from given VM Name
  block:
    - name: Get virtual machine info
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        folder: "/datacenter/vm/folder"
      delegate_to: localhost
      register: vm_info

    - debug:
        msg: "{{ item.tags }}"
      with_items:
        - "{{ vm_info.virtual_machines | community.general.json_query(query) }}"
      vars:
        query: "[?guest_name=='DC0_H0_VM0']"

- name: Gather all VMs from a specific folder
  community.vmware.vmware_vm_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    folder: "/Asia-Datacenter1/vm/prod"
  delegate_to: localhost
  register: vm_info

- name: Get datastore_url from given VM name
  block:
    - name: Get virtual machine info
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
      delegate_to: localhost
      register: vm_info

    - debug:
        msg: "{{ item.datastore_url }}"
      with_items:
        - "{{ vm_info.virtual_machines | community.general.json_query(query) }}"
      vars:
        query: "[?guest_name=='DC0_H0_VM0']"
```

## [Return Values](vmware_vm_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **virtual_machines**  list / elements=string | list of dictionary of virtual machines and their information  **Returned:** success  **Sample:** `[{"allocated": {"cpu": 2, "memory": 16, "storage": 500000000}, "attributes": {"job": "backup-prepare"}, "cluster": null, "datacenter": "Datacenter-1", "datastore_url": [{"name": "t880-o2g", "url": "/vmfs/volumes/e074264a-e5c82a58"}], "esxi_hostname": "10.76.33.226", "folder": "/Datacenter-1/vm", "guest_fullname": "Ubuntu Linux (64-bit)", "guest_name": "ubuntu_t", "ip_address": "", "mac_address": ["00:50:56:87:a5:9a"], "moid": "vm-24", "power_state": "poweredOff", "tags": [{"category_id": "urn:vmomi:InventoryServiceCategory:b316cc45-f1a9-4277-811d-56c7e7975203:GLOBAL", "category_name": "cat_0001", "description": "", "id": "urn:vmomi:InventoryServiceTag:43737ec0-b832-4abf-abb1-fd2448ce3b26:GLOBAL", "name": "tag_0001"}], "uuid": "4207072c-edd8-3bd5-64dc-903fd3a0db04", "vm_network": {"00:50:56:87:a5:9a": {"ipv4": ["10.76.33.228"], "ipv6": []}}}]` |

### Authors

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
- Fedor Vompe (@sumkincpp)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
