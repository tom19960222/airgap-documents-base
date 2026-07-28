---
collection: ansible
version: "8"
title: "community.vmware.vmware_cluster_info module – Gather info about clusters available in given vCenter"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_cluster_info_module.html
fetched_at: 2026-07-28T01:59:40+00:00
---
# community.vmware.vmware_cluster_info module – Gather info about clusters available in given vCenter

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
> To use it in a playbook, specify: `community.vmware.vmware_cluster_info`.

- [Synopsis](vmware_cluster_info_module.md#synopsis)
- [Parameters](vmware_cluster_info_module.md#parameters)
- [Notes](vmware_cluster_info_module.md#notes)
- [Examples](vmware_cluster_info_module.md#examples)
- [Return Values](vmware_cluster_info_module.md#return-values)

## [Synopsis](vmware_cluster_info_module.md#id1)

- This module can be used to gather information about clusters in VMWare infrastructure.
- All values and VMware object names are case sensitive.

## [Parameters](vmware_cluster_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  string | Name of the cluster.  If set, information of this cluster will be returned.  This parameter is required, if `datacenter` is not supplied. |
| **datacenter**  string | Datacenter to search for cluster/s.  This parameter is required, if `cluster_name` is not supplied. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **properties**  list / elements=string | Specify the properties to retrieve.  Example:  properties: [  “name”,  “configuration.dasConfig.enabled”,  “summary.totalCpu”  ]  Only valid when `schema` is `vsphere`. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **schema**  string | Specify the output schema desired.  The ‘summary’ output schema is the legacy output from the module.  The ‘vsphere’ output schema is the vSphere API class definition which requires pyvmomi>6.7.1.  **Choices:**   - `"summary"` ← (default) - `"vsphere"` |
| **show_tag**  boolean | Tags related to cluster are shown if set to `true`.  **Choices:**   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_cluster_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_cluster_info_module.md#id4)

```yaml+jinja
- name: Gather cluster info from given datacenter
  community.vmware.vmware_cluster_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: ha-datacenter
  delegate_to: localhost
  register: cluster_info

- name: Gather info from datacenter about specific cluster
  community.vmware.vmware_cluster_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: DC0_C0
  delegate_to: localhost
  register: cluster_info

- name: Gather info from datacenter about specific cluster with tags
  community.vmware.vmware_cluster_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: DC0_C0
    show_tag: true
  delegate_to: localhost
  register: cluster_info

- name: Gather some info from a cluster using the vSphere API output schema
  vmware_cluster_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: DC0_C0
    schema: vsphere
    properties:
      - name
      - configuration.dasConfig.enabled
      - summary.totalCpu
  delegate_to: localhost
  register: cluster_info
```

## [Return Values](vmware_cluster_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **clusters**  dictionary | metadata about the available clusters  datacenter added in the return values from version 1.6.0  **Returned:** always  **Sample:** `{"DC0_C0": {"datacenter": "DC0", "drs_default_vm_behavior": null, "drs_enable_vm_behavior_overrides": null, "drs_vmotion_rate": null, "enable_ha": null, "enabled_drs": true, "enabled_vsan": false, "ha_admission_control_enabled": null, "ha_failover_level": null, "ha_host_monitoring": null, "ha_restart_priority": null, "ha_vm_failure_interval": null, "ha_vm_max_failure_window": null, "ha_vm_max_failures": null, "ha_vm_min_up_time": null, "ha_vm_monitoring": null, "ha_vm_tools_monitoring": null, "hosts": [{"folder": "/DC0/host/DC0_C0", "name": "esxi01.vsphere.local"}, {"folder": "/DC0/host/DC0_C0", "name": "esxi02.vsphere.local"}, {"folder": "/DC0/host/DC0_C0", "name": "esxi03.vsphere.local"}, {"folder": "/DC0/host/DC0_C0", "name": "esxi04.vsphere.local"}], "moid": "domain-c9", "resource_summary": {"cpuCapacityMHz": 4224, "cpuUsedMHz": 87, "memCapacityMB": 6139, "memUsedMB": 1254, "pMemAvailableMB": 0, "pMemCapacityMB": 0, "storageCapacityMB": 33280, "storageUsedMB": 19953}, "tags": [{"category_id": "urn:vmomi:InventoryServiceCategory:9fbf83de-7903-442e-8004-70fd3940297c:GLOBAL", "category_name": "sample_cluster_cat_0001", "description": "", "id": "urn:vmomi:InventoryServiceTag:93d680db-b3a6-4834-85ad-3e9516e8fee8:GLOBAL", "name": "sample_cluster_tag_0001"}], "vsan_auto_claim_storage": false}}` |

### Authors

- Abhijeet Kasurde (@Akasurde)
- Christian Neugum (@digifuchsi)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
