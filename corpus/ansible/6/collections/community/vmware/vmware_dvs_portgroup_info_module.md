---
collection: ansible
version: "6"
title: "community.vmware.vmware_dvs_portgroup_info module – Gathers info DVS portgroup configurations"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/vmware/vmware_dvs_portgroup_info_module.html
fetched_at: 2026-07-27T17:21:41+00:00
---
# community.vmware.vmware_dvs_portgroup_info module – Gathers info DVS portgroup configurations

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
> To use it in a playbook, specify: `community.vmware.vmware_dvs_portgroup_info`.

- [Synopsis](vmware_dvs_portgroup_info_module.md#synopsis)
- [Parameters](vmware_dvs_portgroup_info_module.md#parameters)
- [Notes](vmware_dvs_portgroup_info_module.md#notes)
- [Examples](vmware_dvs_portgroup_info_module.md#examples)
- [Return Values](vmware_dvs_portgroup_info_module.md#return-values)

## [Synopsis](vmware_dvs_portgroup_info_module.md#id1)

- This module can be used to gather information about DVS portgroup configurations.

## [Parameters](vmware_dvs_portgroup_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **datacenter**  string / required | Name of the datacenter. |
| **dvswitch**  string | Name of a dvswitch to look for. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  Default: `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **show_mac_learning**  boolean  added in community.vmware 1.10.0 | Show or hide MAC learning information of the DVS portgroup.  Choices:   - `false` - `true` ← (default) |
| **show_network_policy**  boolean | Show or hide network policies of DVS portgroup.  Choices:   - `false` - `true` ← (default) |
| **show_port_policy**  boolean | Show or hide port policies of DVS portgroup.  Choices:   - `false` - `true` ← (default) |
| **show_teaming_policy**  boolean | Show or hide teaming policies of DVS portgroup.  Choices:   - `false` - `true` ← (default) |
| **show_uplinks**  boolean  added in community.vmware 1.10.0 | Show or hide uplinks of DVS portgroup.  Choices:   - `false` - `true` ← (default) |
| **show_vlan_info**  boolean | Show or hide vlan information of the DVS portgroup.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  Choices:   - `false` - `true` ← (default) |

## [Notes](vmware_dvs_portgroup_info_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_dvs_portgroup_info_module.md#id4)

```yaml+jinja
- name: Get info about DVPG
  community.vmware.vmware_dvs_portgroup_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
  register: dvpg_info

- name: Get number of ports for portgroup 'dvpg_001' in 'dvs_001'
  debug:
    msg: "{{ item.num_ports }}"
  with_items:
    - "{{ dvpg_info.dvs_portgroup_info['dvs_001'] | json_query(query) }}"
  vars:
    query: "[?portgroup_name=='dvpg_001']"
```

## [Return Values](vmware_dvs_portgroup_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dvs_portgroup_info**  dictionary | metadata about DVS portgroup configuration  Returned: on success  Sample: `{"dvs_0": [{"description": null, "dvswitch_name": "dvs_001", "network_policy": {"forged_transmits": false, "mac_changes": false, "promiscuous": false}, "num_ports": 8, "port_policy": {"block_override": true, "ipfix_override": false, "live_port_move": false, "network_rp_override": false, "port_config_reset_at_disconnect": true, "security_override": false, "shaping_override": false, "traffic_filter_override": false, "uplink_teaming_override": false, "vendor_config_override": false, "vlan_override": false}, "portgroup_name": "dvpg_001", "teaming_policy": {"inbound_policy": true, "notify_switches": true, "policy": "loadbalance_srcid", "rolling_order": false}, "type": "earlyBinding", "vlan_info": {"pvlan": false, "trunk": false, "vlan_id": 0}}]}` |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Homepage](https://github.com/ansible-collections/community.vmware)
[Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
