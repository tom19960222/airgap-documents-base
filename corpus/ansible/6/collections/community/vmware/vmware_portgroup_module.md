---
collection: ansible
version: "6"
title: "community.vmware.vmware_portgroup module – Create a VMware portgroup"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_portgroup_module.html
fetched_at: 2026-07-27T17:22:44+00:00
---
# community.vmware.vmware_portgroup module – Create a VMware portgroup

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
> To use it in a playbook, specify: `community.vmware.vmware_portgroup`.

- [Synopsis](vmware_portgroup_module.md#synopsis)
- [Parameters](vmware_portgroup_module.md#parameters)
- [Notes](vmware_portgroup_module.md#notes)
- [Examples](vmware_portgroup_module.md#examples)
- [Return Values](vmware_portgroup_module.md#return-values)

## [Synopsis](vmware_portgroup_module.md#id1)

- Create a VMware Port Group on a VMware Standard Switch (vSS) for given ESXi host(s) or hosts of given cluster.

## [Parameters](vmware_portgroup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_name**  aliases: cluster  string | Name of cluster name for host membership.  Portgroup will be created on all hosts of the given cluster.  This option is required if `hosts` is not specified. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **hosts**  aliases: esxi_hostname  list / elements=string | List of name of host or hosts on which portgroup needs to be added.  This option is required if `cluster_name` is not specified. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **portgroup**  aliases: portgroup_name  string / required | Portgroup name to add. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **security**  aliases: security_policy, network_policy  dictionary | Network policy specifies layer 2 security settings for a portgroup such as promiscuous mode, where guest adapter listens to all the packets, MAC address changes and forged transmits.  Dict which configures the different security values for portgroup. |
| **forged_transmits**  boolean | Indicates whether forged transmits are allowed.  Choices:   - `false` - `true` |
| **mac_changes**  boolean | Indicates whether mac changes are allowed.  Choices:   - `false` - `true` |
| **promiscuous_mode**  boolean | Indicates whether promiscuous mode is allowed.  Choices:   - `false` - `true` |
| **state**  string | Determines if the portgroup should be present or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **switch**  aliases: switch_name, vswitch  string / required | vSwitch to modify. |
| **teaming**  aliases: teaming_policy  dictionary | Dictionary which configures the different teaming values for portgroup. |
| **active_adapters**  list / elements=string | List of active adapters used for load balancing.  All vmnics are used as active adapters if `active_adapters` and `standby_adapters` are not defined. |
| **failback**  boolean | Indicate whether or not to use a failback when restoring links.  Choices:   - `false` - `true` |
| **load_balancing**  aliases: load_balance_policy  string | Network adapter teaming policy.  Choices:   - `"loadbalance_ip"` - `"loadbalance_srcmac"` - `"loadbalance_srcid"` - `"failover_explicit"` - `"None"` |
| **network_failure_detection**  string | Network failure detection.  Choices:   - `"link_status_only"` - `"beacon_probing"` |
| **notify_switches**  boolean | Indicate whether or not to notify the physical switch if a link fails.  Choices:   - `false` - `true` |
| **standby_adapters**  list / elements=string | List of standby adapters used for failover.  All vmnics are used as active adapters if `active_adapters` and `standby_adapters` are not defined. |
| **traffic_shaping**  dictionary | Dictionary which configures traffic shaping for the switch. |
| **average_bandwidth**  integer | Average bandwidth (kbit/s). |
| **burst_size**  integer | Burst size (KB). |
| **enabled**  boolean | Status of Traffic Shaping Policy.  Choices:   - `false` - `true` |
| **peak_bandwidth**  integer | Peak bandwidth (kbit/s). |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |
| **vlan_id**  aliases: vlan  integer | VLAN ID to assign to portgroup.  Set to 0 (no VLAN tagging) by default.  Default: `0` |

## [Notes](vmware_portgroup_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_portgroup_module.md#id4)

```yaml+jinja
- name: Add Management Network VM Portgroup
  community.vmware.vmware_portgroup:
    hostname: "{{ esxi_hostname }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    switch: "{{ vswitch_name }}"
    portgroup: "{{ portgroup_name }}"
    vlan_id: "{{ vlan_id }}"
  delegate_to: localhost

- name: Add Portgroup with Promiscuous Mode Enabled
  community.vmware.vmware_portgroup:
    hostname: "{{ esxi_hostname }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    switch: "{{ vswitch_name }}"
    portgroup: "{{ portgroup_name }}"
    security:
        promiscuous_mode: True
  delegate_to: localhost

- name: Add Management Network VM Portgroup to specific hosts
  community.vmware.vmware_portgroup:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    hosts: [esxi_hostname_one]
    switch: "{{ vswitch_name }}"
    portgroup: "{{ portgroup_name }}"
    vlan_id: "{{ vlan_id }}"
  delegate_to: localhost

- name: Add Management Network VM Portgroup to all hosts in a cluster
  community.vmware.vmware_portgroup:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    cluster_name: "{{ cluster_name }}"
    switch: "{{ vswitch_name }}"
    portgroup: "{{ portgroup_name }}"
    vlan_id: "{{ vlan_id }}"
  delegate_to: localhost

- name: Remove Management Network VM Portgroup to all hosts in a cluster
  community.vmware.vmware_portgroup:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    cluster_name: "{{ cluster_name }}"
    switch: "{{ vswitch_name }}"
    portgroup: "{{ portgroup_name }}"
    vlan_id: "{{ vlan_id }}"
    state: absent
  delegate_to: localhost

- name: Add Portgroup with all settings defined
  community.vmware.vmware_portgroup:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ inventory_hostname }}"
    switch: "{{ vswitch_name }}"
    portgroup: "{{ portgroup_name }}"
    vlan_id: 10
    security:
        promiscuous_mode: False
        mac_changes: False
        forged_transmits: False
    traffic_shaping:
        enabled: True
        average_bandwidth: 100000
        peak_bandwidth: 100000
        burst_size: 102400
    teaming:
        load_balancing: failover_explicit
        network_failure_detection: link_status_only
        notify_switches: true
        failback: true
        active_adapters:
            - vmnic0
        standby_adapters:
            - vmnic1
  delegate_to: localhost
  register: teaming_result
```

## [Return Values](vmware_portgroup_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | metadata about the portgroup  Returned: always  Sample: `{"esxi01.example.com": {"changed": true, "failback": "No override", "failover_active": "No override", "failover_standby": "No override", "failure_detection": "No override", "load_balancing": "No override", "msg": "Port Group added", "notify_switches": "No override", "portgroup": "vMotion", "sec_forged_transmits": false, "sec_mac_changes": false, "sec_promiscuous_mode": false, "traffic_shaping": "No override", "vlan_id": 33, "vswitch": "vSwitch1"}}` |

### Authors

- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)
- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
