---
collection: ansible
version: "8"
title: "community.vmware.vmware_dvswitch_uplink_pg module – Manage uplink portgroup configuration of a Distributed Switch"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_dvswitch_uplink_pg_module.html
fetched_at: 2026-07-28T02:00:01+00:00
---
# community.vmware.vmware_dvswitch_uplink_pg module – Manage uplink portgroup configuration of a Distributed Switch

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
> To use it in a playbook, specify: `community.vmware.vmware_dvswitch_uplink_pg`.

- [Synopsis](vmware_dvswitch_uplink_pg_module.md#synopsis)
- [Parameters](vmware_dvswitch_uplink_pg_module.md#parameters)
- [Notes](vmware_dvswitch_uplink_pg_module.md#notes)
- [Examples](vmware_dvswitch_uplink_pg_module.md#examples)
- [Return Values](vmware_dvswitch_uplink_pg_module.md#return-values)

## [Synopsis](vmware_dvswitch_uplink_pg_module.md#id1)

- This module can be used to configure the uplink portgroup of a Distributed Switch.

## [Parameters](vmware_dvswitch_uplink_pg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **advanced**  aliases: port_policy  dictionary | Dictionary which configures the advanced policy settings for the uplink portgroup.  **Default:** `{"block_override": true, "netflow_override": false, "port_config_reset_at_disconnect": true, "traffic_filter_override": false, "vendor_config_override": false, "vlan_override": false}` |
| **block_override**  boolean | Indicates if the block policy can be changed per port.  **Choices:**   - `false` - `true` ← (default) |
| **netflow_override**  boolean | Indicates if the NetFlow policy can be changed per port.  **Choices:**   - `false` ← (default) - `true` |
| **port_config_reset_at_disconnect**  boolean | Indicates if the configuration of a port is reset automatically after disconnect.  **Choices:**   - `false` - `true` ← (default) |
| **traffic_filter_override**  boolean | Indicates if the traffic filter can be changed per port.  **Choices:**   - `false` ← (default) - `true` |
| **vendor_config_override**  boolean | Indicates if the vendor config can be changed per port.  **Choices:**   - `false` ← (default) - `true` |
| **vlan_override**  boolean | Indicates if the vlan can be changed per port.  **Choices:**   - `false` ← (default) - `true` |
| **block_all_ports**  boolean | Indicates if all ports are blocked on the uplink portgroup.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | The description of the uplink portgroup. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **lacp**  dictionary | Dictionary which configures the LACP settings for the uplink portgroup.  The options are only used if the LACP support mode is set to ‘basic’.  **Default:** `{"mode": "passive", "status": "disabled"}` |
| **mode**  string | The negotiating state of the uplinks/ports.  **Choices:**   - `"active"` - `"passive"` ← (default) |
| **status**  string | Indicates if LACP is enabled.  **Choices:**   - `"enabled"` - `"disabled"` ← (default) |
| **name**  string | The name of the uplink portgroup.  The current name will be used if not specified. |
| **netflow_enabled**  boolean | Indicates if NetFlow is enabled on the uplink portgroup.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **switch**  aliases: dvswitch  string / required | The name of the Distributed Switch. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |
| **vlan_trunk_range**  list / elements=string | The VLAN trunk range that should be configured with the uplink portgroup.  This can be a combination of multiple ranges and numbers, example: [ 2-3967, 4049-4092 ].  **Default:** `["0-4094"]` |

## [Notes](vmware_dvswitch_uplink_pg_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_dvswitch_uplink_pg_module.md#id4)

```yaml+jinja
- name: Configure Uplink portgroup
  community.vmware.vmware_dvswitch_uplink_pg:
    hostname: '{{ inventory_hostname }}'
    username: '{{ vcsa_username }}'
    password: '{{ vcsa_password }}'
    switch: dvSwitch
    name: dvSwitch-DVUplinks
    advanced:
      port_config_reset_at_disconnect: true
      block_override: true
      vendor_config_override: false
      vlan_override: false
      netflow_override: false
      traffic_filter_override: false
    vlan_trunk_range:
      - '0-4094'
    netflow_enabled: false
    block_all_ports: false
  delegate_to: localhost

- name: Enabled LACP on Uplink portgroup
  community.vmware.vmware_dvswitch_uplink_pg:
    hostname: '{{ inventory_hostname }}'
    username: '{{ vcsa_username }}'
    password: '{{ vcsa_password }}'
    switch: dvSwitch
    lacp:
      status: enabled
      mode: active
  delegate_to: localhost
```

## [Return Values](vmware_dvswitch_uplink_pg_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  string | information about performed operation  **Returned:** always  **Sample:** `"{'adv_block_ports': True, 'adv_netflow': False, 'adv_reset_at_disconnect': True, 'adv_traffic_filtering': False, 'adv_vendor_conf': False, 'adv_vlan': False, 'block_all_ports': False, 'changed': False, 'description': None, 'dvswitch': 'dvSwitch', 'lacp_status': 'disabled', 'lacp_status_previous': 'enabled', 'name': 'dvSwitch-DVUplinks', 'netflow_enabled': False, 'result': 'Uplink portgroup already configured properly', 'vlan_trunk_range': ['2-3967', '4049-4092']}"` |

### Authors

- Christian Kotte (@ckotte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
