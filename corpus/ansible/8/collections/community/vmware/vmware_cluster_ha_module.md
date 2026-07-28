---
collection: ansible
version: "8"
title: "community.vmware.vmware_cluster_ha module – Manage High Availability (HA) on VMware vSphere clusters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_cluster_ha_module.html
fetched_at: 2026-07-28T01:59:39+00:00
---
# community.vmware.vmware_cluster_ha module – Manage High Availability (HA) on VMware vSphere clusters

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
> To use it in a playbook, specify: `community.vmware.vmware_cluster_ha`.

- [Synopsis](vmware_cluster_ha_module.md#synopsis)
- [Parameters](vmware_cluster_ha_module.md#parameters)
- [Notes](vmware_cluster_ha_module.md#notes)
- [Examples](vmware_cluster_ha_module.md#examples)

## [Synopsis](vmware_cluster_ha_module.md#id1)

- Manages HA configuration on VMware vSphere clusters.
- All values and VMware object names are case sensitive.

## [Parameters](vmware_cluster_ha_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **advanced_settings**  dictionary | A dictionary of advanced HA settings.  **Default:** `{}` |
| **apd_delay**  integer  *added in community.vmware 2.9.0* | The response recovery delay time in sec for storage failures categorized as All Paths Down (APD).  Only set if `apd_response` is `restartConservative` or `restartAggressive`.  **Default:** `180` |
| **apd_reaction**  string  *added in community.vmware 2.9.0* | VM response recovery reaction for storage failures categorized as All Paths Down (APD).  Only set if `apd_response` is `restartConservative` or `restartAggressive`.  **Choices:**   - `"reset"` ← (default) - `"none"` |
| **apd_response**  string | VM storage protection setting for storage failures categorized as All Paths Down (APD).  **Choices:**   - `"disabled"` - `"warning"` ← (default) - `"restartConservative"` - `"restartAggressive"` |
| **cluster_name**  string / required | The name of the cluster to be managed. |
| **datacenter**  aliases: datacenter_name  string / required | The name of the datacenter. |
| **enable**  boolean | Whether to enable HA.  **Choices:**   - `false` - `true` ← (default) |
| **failover_host_admission_control**  dictionary | Configure dedicated failover hosts.  `slot_based_admission_control`, `reservation_based_admission_control` and `failover_host_admission_control` are mutually exclusive. |
| **failover_hosts**  list / elements=string / required | List of dedicated failover hosts. |
| **ha_host_monitoring**  string | Whether HA restarts virtual machines after a host fails.  If set to `enabled`, HA restarts virtual machines after a host fails.  If set to `disabled`, HA does not restart virtual machines after a host fails.  If `enable` is set to `false`, then this value is ignored.  **Choices:**   - `"enabled"` ← (default) - `"disabled"` |
| **ha_restart_priority**  string | Priority HA gives to a virtual machine if sufficient capacity is not available to power on all failed virtual machines.  Valid only if *ha_vm_monitoring* is set to either `vmAndAppMonitoring` or `vmMonitoringOnly`.  If set to `disabled`, then HA is disabled for this virtual machine.  If set to `high`, then virtual machine with this priority have a higher chance of powering on after a failure, when there is insufficient capacity on hosts to meet all virtual machine needs.  If set to `medium`, then virtual machine with this priority have an intermediate chance of powering on after a failure, when there is insufficient capacity on hosts to meet all virtual machine needs.  If set to `low`, then virtual machine with this priority have a lower chance of powering on after a failure, when there is insufficient capacity on hosts to meet all virtual machine needs.  **Choices:**   - `"disabled"` - `"high"` - `"low"` - `"medium"` ← (default) |
| **ha_vm_failure_interval**  integer | The number of seconds after which virtual machine is declared as failed if no heartbeat has been received.  This setting is only valid if `ha_vm_monitoring` is set to, either `vmAndAppMonitoring` or `vmMonitoringOnly`.  Unit is seconds.  **Default:** `30` |
| **ha_vm_max_failure_window**  integer | The number of seconds for the window during which up to `ha_vm_max_failures` resets can occur before automated responses stop.  Valid only when *ha_vm_monitoring* is set to either `vmAndAppMonitoring` or `vmMonitoringOnly`.  Unit is seconds.  Default specifies no failure window.  **Default:** `-1` |
| **ha_vm_max_failures**  integer | Maximum number of failures and automated resets allowed during the time that `ha_vm_max_failure_window` specifies.  Valid only when *ha_vm_monitoring* is set to either `vmAndAppMonitoring` or `vmMonitoringOnly`.  **Default:** `3` |
| **ha_vm_min_up_time**  integer | The number of seconds for the virtual machine’s heartbeats to stabilize after the virtual machine has been powered on.  Valid only when *ha_vm_monitoring* is set to either `vmAndAppMonitoring` or `vmMonitoringOnly`.  Unit is seconds.  **Default:** `120` |
| **ha_vm_monitoring**  string | State of virtual machine health monitoring service.  If set to `vmAndAppMonitoring`, HA response to both virtual machine and application heartbeat failure.  If set to `vmMonitoringDisabled`, virtual machine health monitoring is disabled.  If set to `vmMonitoringOnly`, HA response to virtual machine heartbeat failure.  If `enable` is set to `false`, then this value is ignored.  **Choices:**   - `"vmAndAppMonitoring"` - `"vmMonitoringOnly"` - `"vmMonitoringDisabled"` ← (default) |
| **host_isolation_response**  string | Indicates whether or VMs should be powered off if a host determines that it is isolated from the rest of the compute resource.  If set to `none`, do not power off VMs in the event of a host network isolation.  If set to `powerOff`, power off VMs in the event of a host network isolation.  If set to `shutdown`, shut down VMs guest operating system in the event of a host network isolation.  **Choices:**   - `"none"` ← (default) - `"powerOff"` - `"shutdown"` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **pdl_response**  string | VM storage protection setting for storage failures categorized as Permenant Device Loss (PDL).  **Choices:**   - `"disabled"` - `"warning"` ← (default) - `"restartAggressive"` |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **reservation_based_admission_control**  dictionary | Configure reservation based admission control policy.  `slot_based_admission_control`, `reservation_based_admission_control` and `failover_host_admission_control` are mutually exclusive. |
| **auto_compute_percentages**  boolean | By default, `failover_level` is used to calculate `cpu_failover_resources_percent` and `memory_failover_resources_percent`. If a user wants to override the percentage values, he has to set this field to false.  **Choices:**   - `false` - `true` ← (default) |
| **cpu_failover_resources_percent**  integer | Percentage of CPU resources in the cluster to reserve for failover. Ignored if `auto_compute_percentages` is not set to false.  **Default:** `50` |
| **failover_level**  integer / required | Number of host failures that should be tolerated. |
| **memory_failover_resources_percent**  integer | Percentage of memory resources in the cluster to reserve for failover. Ignored if `auto_compute_percentages` is not set to false.  **Default:** `50` |
| **slot_based_admission_control**  dictionary | Configure slot based admission control policy.  `slot_based_admission_control`, `reservation_based_admission_control` and `failover_host_admission_control` are mutually exclusive. |
| **failover_level**  integer / required | Number of host failures that should be tolerated. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_cluster_ha_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_cluster_ha_module.md#id4)

```yaml+jinja
- name: Enable HA without admission control
  community.vmware.vmware_cluster_ha:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
    enable: true
  delegate_to: localhost

- name: Enable HA and VM monitoring without admission control
  community.vmware.vmware_cluster_ha:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter_name: DC0
    cluster_name: "{{ cluster_name }}"
    enable: true
    ha_vm_monitoring: vmMonitoringOnly
  delegate_to: localhost

- name: Enable HA with admission control reserving 50% of resources for HA
  community.vmware.vmware_cluster_ha:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
    enable: true
    reservation_based_admission_control:
      auto_compute_percentages: false
      failover_level: 1
      cpu_failover_resources_percent: 50
      memory_failover_resources_percent: 50
  delegate_to: localhost
```

### Authors

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
