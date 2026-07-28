---
collection: ansible
version: "8"
title: "community.vmware.vmware_dvs_portgroup module – Create or remove a Distributed vSwitch portgroup."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_dvs_portgroup_module.html
fetched_at: 2026-07-28T01:59:55+00:00
---
# community.vmware.vmware_dvs_portgroup module – Create or remove a Distributed vSwitch portgroup.

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
> To use it in a playbook, specify: `community.vmware.vmware_dvs_portgroup`.

- [Synopsis](vmware_dvs_portgroup_module.md#synopsis)
- [Parameters](vmware_dvs_portgroup_module.md#parameters)
- [Notes](vmware_dvs_portgroup_module.md#notes)
- [Examples](vmware_dvs_portgroup_module.md#examples)

## [Synopsis](vmware_dvs_portgroup_module.md#id1)

- Create or remove a Distributed vSwitch portgroup.

## [Parameters](vmware_dvs_portgroup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **in_traffic_shaping**  dictionary  *added in community.vmware 2.3.0* | Dictionary which configures the ingress traffic shaping settings for the portgroup. |
| **average_bandwidth**  integer | Establishes the number of bits per second to allow across a port, averaged over time, that is, the allowed average load.  Ignored if `inherited` is true. |
| **burst_size**  integer | The maximum number of bits per second to allow across a port when it is sending/sending or receiving a burst of traffic.  Ignored if `inherited` is true. |
| **enabled**  boolean | Indicates whether ingress traffic shaping is activated or not.  Ignored if `inherited` is true.  **Choices:**   - `false` - `true` |
| **inherited**  boolean / required | Inherit the settings from the switch or not.  **Choices:**   - `false` - `true` |
| **peak_bandwidth**  integer | The maximum number of bytes to allow in a burst.  Ignored if `inherited` is true. |
| **mac_learning**  dictionary | Dictionary which configures MAC learning for portgroup. |
| **allow_unicast_flooding**  boolean | The flag to allow flooding of unlearned MAC for ingress traffic.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | The flag to indicate if source MAC address learning is allowed.  **Choices:**   - `false` - `true` |
| **limit**  integer | The maximum number of MAC addresses that can be learned. |
| **limit_policy**  string | The default switching policy after MAC limit is exceeded.  **Choices:**   - `"allow"` - `"drop"` |
| **net_flow**  string  *added in community.vmware 2.3.0* | Indicate whether or not the virtual machine IP traffic that flows through a vds gets analyzed by sending reports to a NetFlow collector.  **Choices:**   - `"true"` - `"on"` - `"yes"` - `"false"` - `"off"` - `"no"` - `"inherited"` |
| **network_policy**  dictionary | Dictionary which configures the different security values for portgroup. |
| **forged_transmits**  boolean | Indicates whether forged transmits are allowed. Ignored if `inherited` is true.  **Choices:**   - `false` - `true` |
| **inherited**  boolean / required | Inherit the settings from the switch or not.  **Choices:**   - `false` - `true` |
| **mac_changes**  boolean | Indicates whether mac changes are allowed. Ignored if `inherited` is true.  **Choices:**   - `false` - `true` |
| **promiscuous**  boolean | Indicates whether promiscuous mode is allowed. Ignored if `inherited` is true.  **Choices:**   - `false` - `true` |
| **num_ports**  integer | The number of ports the portgroup should contain. |
| **out_traffic_shaping**  dictionary  *added in community.vmware 2.3.0* | Dictionary which configures the egress traffic shaping settings for the portgroup. |
| **average_bandwidth**  integer | Establishes the number of bits per second to allow across a port, averaged over time, that is, the allowed average load.  Ignored if `inherited` is true. |
| **burst_size**  integer | The maximum number of bits per second to allow across a port when it is sending/sending or receiving a burst of traffic.  Ignored if `inherited` is true. |
| **enabled**  boolean | Indicates whether egress traffic shaping is activated or not.  Ignored if `inherited` is true.  **Choices:**   - `false` - `true` |
| **inherited**  boolean / required | Inherit the settings from the switch or not.  **Choices:**   - `false` - `true` |
| **peak_bandwidth**  integer | The maximum number of bytes to allow in a burst.  Ignored if `inherited` is true. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **port_allocation**  string | Elastic port groups automatically increase or decrease the number of ports as needed.  Only valid if *port_binding* is set to `static`.  Will be `elastic` if not specified and *port_binding* is set to `static`.  Will be `fixed` if not specified and *port_binding* is set to `ephemeral`.  **Choices:**   - `"elastic"` - `"fixed"` |
| **port_binding**  string / required | The type of port binding determines when ports in a port group are assigned to virtual machines.  See VMware KB 1022312 <https://kb.vmware.com/s/article/1022312> for more details.  **Choices:**   - `"static"` - `"ephemeral"` |
| **port_policy**  dictionary | Dictionary which configures the advanced policy settings for the portgroup.  **Default:** `{"block_override": true, "ipfix_override": false, "live_port_move": false, "mac_management_override": false, "network_rp_override": false, "port_config_reset_at_disconnect": true, "shaping_override": false, "traffic_filter_override": false, "uplink_teaming_override": false, "vendor_config_override": false, "vlan_override": false}` |
| **block_override**  boolean | Indicates if the block policy can be changed per port.  **Choices:**   - `false` - `true` ← (default) |
| **ipfix_override**  boolean | Indicates if the ipfix policy can be changed per port.  **Choices:**   - `false` ← (default) - `true` |
| **live_port_move**  boolean | Indicates if a live port can be moved in or out of the portgroup.  **Choices:**   - `false` ← (default) - `true` |
| **mac_management_override**  aliases: security_override  boolean | Indicates if the security policy can be changed per port.  **Choices:**   - `false` ← (default) - `true` |
| **network_rp_override**  boolean | Indicates if the network resource pool can be changed per port.  **Choices:**   - `false` ← (default) - `true` |
| **port_config_reset_at_disconnect**  boolean | Indicates if the configuration of a port is reset automatically after disconnect.  **Choices:**   - `false` - `true` ← (default) |
| **shaping_override**  boolean | Indicates if the shaping policy can be changed per port.  **Choices:**   - `false` ← (default) - `true` |
| **traffic_filter_override**  boolean | Indicates if the traffic filter can be changed per port.  **Choices:**   - `false` ← (default) - `true` |
| **uplink_teaming_override**  boolean | Indicates if the uplink teaming policy can be changed per port.  **Choices:**   - `false` ← (default) - `true` |
| **vendor_config_override**  boolean | Indicates if the vendor config can be changed per port.  **Choices:**   - `false` ← (default) - `true` |
| **vlan_override**  boolean | Indicates if the vlan can be changed per port.  **Choices:**   - `false` ← (default) - `true` |
| **portgroup_name**  string / required | The name of the portgroup that is to be created or deleted. |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string / required | Determines if the portgroup should be present or not.  **Choices:**   - `"present"` - `"absent"` |
| **switch_name**  string / required | The name of the distributed vSwitch the port group should be created on. |
| **teaming_policy**  dictionary | Dictionary which configures the different teaming values for portgroup.  **Default:** `{"load_balance_policy": "loadbalance_srcid", "notify_switches": true, "rolling_order": false}` |
| **active_uplinks**  list / elements=string | List of active uplinks used for load balancing. |
| **inbound_policy**  boolean | Indicate whether or not the teaming policy is applied to inbound frames as well.  **Choices:**   - `false` - `true` |
| **load_balance_policy**  string | Network adapter teaming policy.  `loadbalance_loadbased` is available from version 2.6 and onwards.  **Choices:**   - `"loadbalance_ip"` - `"loadbalance_srcmac"` - `"loadbalance_srcid"` ← (default) - `"loadbalance_loadbased"` - `"failover_explicit"` |
| **notify_switches**  boolean | Indicate whether or not to notify the physical switch if a link fails.  **Choices:**   - `false` - `true` ← (default) |
| **rolling_order**  boolean | Indicate whether or not to use a rolling policy when restoring links.  **Choices:**   - `false` ← (default) - `true` |
| **standby_uplinks**  list / elements=string | List of standby uplinks used for failover. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **vlan_id**  string / required | The VLAN ID that should be configured with the portgroup, use 0 for no VLAN.  If `vlan_trunk` is configured to be *true*, this can be a combination of multiple ranges and numbers, example: 1-200, 205, 400-4094.  The valid `vlan_id` range is from 0 to 4094. Overlapping ranges are allowed.  If `vlan_private` is configured to be *true*, the corresponding private VLAN should already be configured in the distributed vSwitch. |
| **vlan_private**  boolean | Indicates whether this is for a private VLAN or not.  Mutually exclusive with `vlan_trunk` parameter.  **Choices:**   - `false` ← (default) - `true` |
| **vlan_trunk**  boolean | Indicates whether this is a VLAN trunk or not.  Mutually exclusive with `vlan_private` parameter.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](vmware_dvs_portgroup_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_dvs_portgroup_module.md#id4)

```yaml+jinja
- name: Create vlan portgroup
  community.vmware.vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: vlan-123-portrgoup
    switch_name: dvSwitch
    vlan_id: 123
    num_ports: 120
    port_binding: static
    state: present
  delegate_to: localhost

- name: Create vlan trunk portgroup
  community.vmware.vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: vlan-trunk-portrgoup
    switch_name: dvSwitch
    vlan_id: 1-1000, 1005, 1100-1200
    vlan_trunk: true
    num_ports: 120
    port_binding: static
    state: present
  delegate_to: localhost

- name: Create private vlan portgroup
  vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: private-vlan-portrgoup
    switch_name: dvSwitch
    vlan_id: 1001
    vlan_private: true
    num_ports: 120
    port_binding: static
    state: present
  delegate_to: localhost

- name: Create no-vlan portgroup
  community.vmware.vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: no-vlan-portrgoup
    switch_name: dvSwitch
    vlan_id: 0
    num_ports: 120
    port_binding: static
    state: present
  delegate_to: localhost

- name: Create vlan portgroup with all security and port policies
  community.vmware.vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: vlan-123-portrgoup
    switch_name: dvSwitch
    vlan_id: 123
    num_ports: 120
    port_binding: static
    state: present
    network_policy:
      inherited: false
      promiscuous: true
      forged_transmits: true
      mac_changes: true
    port_policy:
      block_override: true
      ipfix_override: true
      live_port_move: true
      network_rp_override: true
      port_config_reset_at_disconnect: true
      mac_management_override: true
      shaping_override: true
      traffic_filter_override: true
      uplink_teaming_override: true
      vendor_config_override: true
      vlan_override: true
  delegate_to: localhost
```

### Authors

- Joseph Callen (@jcpowermac)
- Philippe Dellaert (@pdellaert)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
