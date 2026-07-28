---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_facts module – Gathers facts about remote ESXi hostsystem"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_facts_module.html
fetched_at: 2026-07-28T02:00:37+00:00
---
# community.vmware.vmware_host_facts module – Gathers facts about remote ESXi hostsystem

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
> To use it in a playbook, specify: `community.vmware.vmware_host_facts`.

- [Synopsis](vmware_host_facts_module.md#synopsis)
- [Parameters](vmware_host_facts_module.md#parameters)
- [Notes](vmware_host_facts_module.md#notes)
- [Examples](vmware_host_facts_module.md#examples)

## [Synopsis](vmware_host_facts_module.md#id1)

- This module can be used to gathers facts like CPU, memory, datastore, network and system etc. about ESXi host system.
- Please specify hostname or IP address of ESXi host system as `hostname`.
- If hostname or IP address of vCenter is provided as `hostname` and `esxi_hostname` is not specified, then the module will throw an error.
- VSAN facts added in 2.7 version.
- SYSTEM fact uuid added in 2.10 version.
- Connection state fact added in VMware collection 2.6.0.
- Please note that when ESXi host connection state is not `connected`, facts returned from vCenter might be stale. Users are recommended to check connection state value and take appropriate decision in the playbook.

## [Parameters](vmware_host_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **esxi_hostname**  string | ESXi hostname.  Host facts about the specified ESXi server will be returned.  By specifying this option, you can select which ESXi hostsystem is returned if connecting to a vCenter. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **properties**  list / elements=string | Specify the properties to retrieve.  If not specified, all properties are retrieved (deeply).  Results are returned in a structure identical to the vsphere API.  Example:  properties: [  “hardware.memorySize”,  “hardware.cpuInfo.numCpuCores”,  “config.product.apiVersion”,  “overallStatus”  ]  Only valid when `schema` is `vsphere`. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **schema**  string | Specify the output schema desired.  The ‘summary’ output schema is the legacy output from the module  The ‘vsphere’ output schema is the vSphere API class definition which requires pyvmomi>6.7.1  **Choices:**   - `"summary"` ← (default) - `"vsphere"` |
| **show_tag**  boolean | Tags related to Host are shown if set to `true`.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_host_facts_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_facts_module.md#id4)

```yaml+jinja
- name: Gather vmware host facts
  community.vmware.vmware_host_facts:
    hostname: "{{ esxi_server }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
  register: host_facts
  delegate_to: localhost

- name: Gather vmware host facts from vCenter
  community.vmware.vmware_host_facts:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
  register: host_facts
  delegate_to: localhost

- name: Gather vmware host facts from vCenter with tag information
  community.vmware.vmware_host_facts:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    show_tag: true
  register: host_facts_tag
  delegate_to: localhost

- name: Get VSAN Cluster UUID from host facts
  community.vmware.vmware_host_facts:
    hostname: "{{ esxi_server }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
  register: host_facts
- set_fact:
    cluster_uuid: "{{ host_facts['ansible_facts']['vsan_cluster_uuid'] }}"

- name: Gather some info from a host using the vSphere API output schema
  community.vmware.vmware_host_facts:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    schema: vsphere
    properties:
      - hardware.memorySize
      - hardware.cpuInfo.numCpuCores
      - config.product.apiVersion
      - overallStatus
  register: host_facts

- name: Gather information about powerstate and connection state
  community.vmware.vmware_host_facts:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    schema: vsphere
    properties:
      - runtime.connectionState
      - runtime.powerState

- name: How to retrieve Product, Version, Build, Update info for ESXi from vCenter
  block:
    - name: Gather product version info for ESXi from vCenter
      community.vmware.vmware_host_facts:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        schema: vsphere
        properties:
          - config.product
          - config.option
      register: gather_host_facts_result

    - name: Extract update level info from option properties
      set_fact:
        update_level_info: "{{ item.value }}"
      loop: "{{ gather_host_facts_result.ansible_facts.config.option }}"
      when:
        - item.key == 'Misc.HostAgentUpdateLevel'

    - name: The output of Product, Version, Build, Update info for ESXi
      debug:
        msg:
          - "Product : {{ gather_host_facts_result.ansible_facts.config.product.name }}"
          - "Version : {{ gather_host_facts_result.ansible_facts.config.product.version }}"
          - "Build   : {{ gather_host_facts_result.ansible_facts.config.product.build }}"
          - "Update  : {{ update_level_info }}"
```

### Authors

- Wei Gao (@woshihaoren)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
