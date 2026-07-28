---
collection: ansible
version: "6"
title: "community.network.pn_port_config module – CLI command to modify port-config"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_port_config_module.html
fetched_at: 2026-07-27T17:19:25+00:00
---
# community.network.pn_port_config module – CLI command to modify port-config

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.pn_port_config`.

- [Synopsis](pn_port_config_module.md#synopsis)
- [Parameters](pn_port_config_module.md#parameters)
- [Examples](pn_port_config_module.md#examples)
- [Return Values](pn_port_config_module.md#return-values)

## [Synopsis](pn_port_config_module.md#id1)

- This module can be used to modify a port configuration.

## [Parameters](pn_port_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_allowed_tpid**  string | Allowed TPID in addition to 0x8100 on Vlan header.  Choices:   - `"vlan"` - `"q-in-q"` - `"q-in-q-old"` |
| **pn_autoneg**  boolean | physical port autonegotiation.  Choices:   - `false` - `true` |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_crc_check_enable**  boolean | CRC check on ingress and rewrite on egress.  Choices:   - `false` - `true` |
| **pn_defer_bringup**  boolean | defer port bringup.  Choices:   - `false` - `true` |
| **pn_description**  string | physical port description. |
| **pn_dscp_map**  string | DSCP map name to enable on port. |
| **pn_edge_switch**  boolean | physical port edge switch.  Choices:   - `false` - `true` |
| **pn_egress_rate_limit**  string | max egress port data rate limit. |
| **pn_enable**  boolean | physical port enable.  Choices:   - `false` - `true` |
| **pn_eth_mode**  string | physical Ethernet mode.  Choices:   - `"1000base-x"` - `"sgmii"` - `"disabled"` - `"GMII"` |
| **pn_fabric_guard**  boolean | Fabric guard configuration.  Choices:   - `false` - `true` |
| **pn_host_enable**  boolean | Host facing port control setting.  Choices:   - `false` - `true` |
| **pn_intf**  string | physical interface. |
| **pn_jumbo**  boolean | jumbo frames on physical port.  Choices:   - `false` - `true` |
| **pn_lacp_priority**  string | LACP priority from 1 to 65535. |
| **pn_local_switching**  boolean | no-local-switching port cannot bridge traffic to another no-local-switching port.  Choices:   - `false` - `true` |
| **pn_loop_vlans**  string | looping vlans. |
| **pn_loopback**  boolean | physical port loopback.  Choices:   - `false` - `true` |
| **pn_mirror_only**  boolean | physical port mirror only.  Choices:   - `false` - `true` |
| **pn_pause**  boolean | physical port pause.  Choices:   - `false` - `true` |
| **pn_port**  string | physical port. |
| **pn_port_mac_address**  string | physical port MAC Address. |
| **pn_reflect**  boolean | physical port reflection.  Choices:   - `false` - `true` |
| **pn_routing**  boolean | routing.  Choices:   - `false` - `true` |
| **pn_send_port**  string | send port. |
| **pn_speed**  string | physical port speed.  Choices:   - `"disable"` - `"10m"` - `"100m"` - `"1g"` - `"2.5g"` - `"10g"` - `"25g"` - `"40g"` - `"50g"` - `"100g"` |
| **pn_vxlan_termination**  boolean | physical port vxlan termination setting.  Choices:   - `false` - `true` |
| **state**  string / required | State the action to perform. Use `update` to modify the port-config.  Choices:   - `"update"` |

## [Examples](pn_port_config_module.md#id3)

```yaml+jinja
- name: Port config modify
  community.network.pn_port_config:
    pn_cliswitch: "sw01"
    state: "update"
    pn_port: "all"
    pn_dscp_map: "foo"

- name: Port config modify
  community.network.pn_port_config:
    pn_cliswitch: "sw01"
    state: "update"
    pn_port: "all"
    pn_host_enable: true
```

## [Return Values](pn_port_config_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the port-config command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the port-config command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
