---
collection: ansible
version: "8"
title: "community.vmware.vmware_dvswitch module – Create or remove a Distributed Switch"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_dvswitch_module.html
fetched_at: 2026-07-28T01:59:58+00:00
---
# community.vmware.vmware_dvswitch module – Create or remove a Distributed Switch

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
> To use it in a playbook, specify: `community.vmware.vmware_dvswitch`.

- [Synopsis](vmware_dvswitch_module.md#synopsis)
- [Parameters](vmware_dvswitch_module.md#parameters)
- [Notes](vmware_dvswitch_module.md#notes)
- [Examples](vmware_dvswitch_module.md#examples)
- [Return Values](vmware_dvswitch_module.md#return-values)

## [Synopsis](vmware_dvswitch_module.md#id1)

- This module can be used to create, remove a Distributed Switch.

## [Parameters](vmware_dvswitch_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **contact**  dictionary | Dictionary which configures administrator contact name and description for the Distributed Switch. |
| **description**  string | Description or other details. |
| **name**  string | Administrator name. |
| **datacenter_name**  aliases: datacenter  string | The name of the datacenter that will contain the Distributed Switch.  This parameter is optional, if `folder` is provided.  Mutually exclusive with `folder` parameter. |
| **description**  string | Description of the Distributed Switch. |
| **discovery_operation**  string | Select the discovery operation.  Required parameter for `state` both `present` and `absent`, before Ansible 2.6 version.  Required only if `state` is set to `present`, for Ansible 2.6 and onwards.  **Choices:**   - `"both"` - `"advertise"` - `"listen"` ← (default) |
| **discovery_proto**  aliases: discovery_protocol  string | Link discovery protocol between Cisco and Link Layer discovery.  Required parameter for `state` both `present` and `absent`, before Ansible 2.6 version.  Required only if `state` is set to `present`, for Ansible 2.6 and onwards.  `cdp`: Use Cisco Discovery Protocol (CDP).  `lldp`: Use Link Layer Discovery Protocol (LLDP).  `disabled`: Do not use a discovery protocol.  **Choices:**   - `"cdp"` ← (default) - `"lldp"` - `"disabled"` |
| **folder**  string | Destination folder, absolute path to place dvswitch in.  The folder should include the datacenter.  This parameter is case sensitive.  This parameter is optional, if `datacenter` is provided.  Examples:  folder: /datacenter1/network  folder: datacenter1/network  folder: /datacenter1/network/folder1  folder: datacenter1/network/folder1  folder: /folder1/datacenter1/network  folder: folder1/datacenter1/network  folder: /folder1/datacenter1/network/folder2 |
| **health_check**  dictionary | Dictionary which configures Health Check for the Distributed Switch.  **Default:** `{"teaming_failover": false, "teaming_failover_interval": 0, "vlan_mtu": false, "vlan_mtu_interval": 0}` |
| **teaming_failover**  boolean | Teaming and failover health check.  **Choices:**   - `false` ← (default) - `true` |
| **teaming_failover_interval**  integer | Teaming and failover health check interval (minutes).  The default value is 1 in the vSphere Client if the Teaming and failover health check is enabled.  **Default:** `0` |
| **vlan_mtu**  boolean | VLAN and MTU health check.  **Choices:**   - `false` ← (default) - `true` |
| **vlan_mtu_interval**  integer | VLAN and MTU health check interval (minutes).  The default value is 1 in the vSphere Client if the VLAN and MTU health check is enabled.  **Default:** `0` |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **mtu**  integer | The switch maximum transmission unit.  Required parameter for `state` both `present` and `absent`, before Ansible 2.6 version.  Required only if `state` is set to `present`, for Ansible 2.6 and onwards.  Accepts value between 1280 to 9000 (both inclusive).  **Default:** `1500` |
| **multicast_filtering_mode**  string | The multicast filtering mode.  `basic` mode: multicast traffic for virtual machines is forwarded according to the destination MAC address of the multicast group.  `snooping` mode: the Distributed Switch provides IGMP and MLD snooping according to RFC 4541.  **Choices:**   - `"basic"` ← (default) - `"snooping"` |
| **net_flow**  dictionary  *added in community.vmware 2.7.0* | Dictionary which configures the Net Flow for the Distributed Switch.  **Default:** `{"active_flow_timeout": 60, "collector_port": 0, "idle_flow_timeout": 15, "internal_flows_only": false, "observation_domain_id": 0, "sampling_rate": 4096}` |
| **active_flow_timeout**  integer | The time, in seconds, to wait before sending information after the flow is initiated.  **Default:** `60` |
| **collector_ip**  string | The IP Address (IPv4 or IPv6) of the NetFlow collector. |
| **collector_port**  integer | The Port of the NetFlow collector.  **Default:** `0` |
| **idle_flow_timeout**  integer | The time, in seconds, to wait before sending information after the flow is initiated.  **Default:** `15` |
| **internal_flows_only**  boolean | If True, data on network activity between vms on the same host will be collected only.  **Choices:**   - `false` ← (default) - `true` |
| **observation_domain_id**  integer | Identifies the information related to the switch.  **Default:** `0` |
| **sampling_rate**  integer | The portion of data that the switch collects.  The sampling rate represents the number of packets that NetFlow drops after every collected packet.  If the rate is 0, NetFlow samples every packet, that is, collect one packet and drop none.  If the rate is 1, NetFlow samples a packet and drops the next one, and so on.  **Default:** `4096` |
| **network_policy**  dictionary | Dictionary which configures the different default security values for portgroups.  If set, these options are inherited by the portgroups of the DVS. |
| **forged_transmits**  boolean | Indicates whether forged transmits are allowed.  **Choices:**   - `false` ← (default) - `true` |
| **mac_changes**  boolean | Indicates whether mac changes are allowed.  **Choices:**   - `false` ← (default) - `true` |
| **promiscuous**  boolean | Indicates whether promiscuous mode is allowed.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If set to `present` and the Distributed Switch does not exist, the Distributed Switch will be created.  If set to `absent` and the Distributed Switch exists, the Distributed Switch will be deleted.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **switch_name**  aliases: switch, dvswitch  string / required | The name of the distribute vSwitch to create or remove. |
| **switch_version**  aliases: version  string | The version of the Distributed Switch to create.  The version must match the version of the ESXi hosts you want to connect.  The version of the vCenter server is used if not specified.  Required only if `state` is set to `present`. |
| **uplink_prefix**  string | The prefix used for the naming of the uplinks.  Only valid if the Distributed Switch will be created. Not used if the Distributed Switch is already present.  Uplinks are created as Uplink 1, Uplink 2, etc. pp. by default.  **Default:** `"Uplink "` |
| **uplink_quantity**  integer | Quantity of uplink per ESXi host added to the Distributed Switch.  The uplink quantity can be increased or decreased, but a decrease will only be successfull if the uplink isn’t used by a portgroup.  Required parameter for `state` both `present` and `absent`, before Ansible 2.6 version.  Required only if `state` is set to `present`, for Ansible 2.6 and onwards. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_dvswitch_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_dvswitch_module.md#id4)

```yaml+jinja
- name: Create dvSwitch
  community.vmware.vmware_dvswitch:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter }}'
    switch: dvSwitch
    version: 6.0.0
    mtu: 9000
    uplink_quantity: 2
    discovery_protocol: lldp
    discovery_operation: both
    state: present
  delegate_to: localhost

- name: Create dvSwitch with all options
  community.vmware.vmware_dvswitch:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter }}'
    switch: dvSwitch
    version: 6.5.0
    mtu: 9000
    uplink_quantity: 2
    uplink_prefix: 'Uplink_'
    discovery_protocol: cdp
    discovery_operation: both
    multicast_filtering_mode: snooping
    health_check:
      vlan_mtu: true
      vlan_mtu_interval: 1
      teaming_failover: true
      teaming_failover_interval: 1
    net_flow:
        collector_ip: 192.168.10.50
        collector_port: 50034
        observation_domain_id: 0
        active_flow_timeout: 60
        idle_flow_timeout: 15
        sampling_rate: 4096
        internal_flows_only: false
    state: present
  delegate_to: localhost

- name: Delete dvSwitch
  community.vmware.vmware_dvswitch:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter }}'
    switch: dvSwitch
    state: absent
  delegate_to: localhost
```

## [Return Values](vmware_dvswitch_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | information about performed operation  **Returned:** always  **Sample:** `"{'changed': False, 'contact': None, 'contact_details': None, 'description': None, 'discovery_operation': 'both', 'discovery_protocol': 'cdp', 'dvswitch': 'test', 'health_check_teaming': False, 'health_check_teaming_interval': 0, 'health_check_vlan': False, 'health_check_vlan_interval': 0, 'mtu': 9000, 'multicast_filtering_mode': 'basic', 'net_flow_active_flow_timeout': 60, 'net_flow_collector_ip': '192.168.10.50', 'net_flow_collector_port': 50034, 'net_flow_idle_flow_timeout': 15, 'net_flow_internal_flows_only': False, 'net_flow_observation_domain_id': 0, 'net_flow_sampling_rate': 4096, 'result': 'DVS already configured properly', 'uplink_quantity': 2, 'uplinks': ['Uplink_1', 'Uplink_2'], 'version': '6.6.0'}"` |

### Authors

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
