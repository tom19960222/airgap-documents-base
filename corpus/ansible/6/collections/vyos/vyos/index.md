---
collection: ansible
version: "6"
title: "Vyos.Vyos"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/index.html
fetched_at: 2026-07-27T16:42:12+00:00
---
# Vyos.Vyos

Collection version 3.0.1

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Network Collection for VYOS devices.

**Author:**

- Ansible Network Community (ansible-network)

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)

## [Plugin Index](index.md#id2)

These are the plugins in the vyos.vyos collection:

### Modules

- [vyos_banner module](vyos_banner_module.md#ansible-collections-vyos-vyos-vyos-banner-module) – Manage multiline banners on VyOS devices
- [vyos_bgp_address_family module](vyos_bgp_address_family_module.md#ansible-collections-vyos-vyos-vyos-bgp-address-family-module) – BGP Address Family Resource Module.
- [vyos_bgp_global module](vyos_bgp_global_module.md#ansible-collections-vyos-vyos-vyos-bgp-global-module) – BGP Global Resource Module.
- [vyos_command module](vyos_command_module.md#ansible-collections-vyos-vyos-vyos-command-module) – Run one or more commands on VyOS devices
- [vyos_config module](vyos_config_module.md#ansible-collections-vyos-vyos-vyos-config-module) – Manage VyOS configuration on remote device
- [vyos_facts module](vyos_facts_module.md#ansible-collections-vyos-vyos-vyos-facts-module) – Get facts about vyos devices.
- [vyos_firewall_global module](vyos_firewall_global_module.md#ansible-collections-vyos-vyos-vyos-firewall-global-module) – FIREWALL global resource module
- [vyos_firewall_interfaces module](vyos_firewall_interfaces_module.md#ansible-collections-vyos-vyos-vyos-firewall-interfaces-module) – FIREWALL interfaces resource module
- [vyos_firewall_rules module](vyos_firewall_rules_module.md#ansible-collections-vyos-vyos-vyos-firewall-rules-module) – FIREWALL rules resource module
- [vyos_hostname module](vyos_hostname_module.md#ansible-collections-vyos-vyos-vyos-hostname-module) – Manages hostname resource module
- [vyos_interface module](vyos_interface_module.md#ansible-collections-vyos-vyos-vyos-interface-module) – (deprecated, removed after 2022-06-01) Manage Interface on VyOS network devices
- [vyos_interfaces module](vyos_interfaces_module.md#ansible-collections-vyos-vyos-vyos-interfaces-module) – Interfaces resource module
- [vyos_l3_interface module](vyos_l3_interface_module.md#ansible-collections-vyos-vyos-vyos-l3-interface-module) – (deprecated, removed after 2022-06-01) Manage L3 interfaces on VyOS network devices
- [vyos_l3_interfaces module](vyos_l3_interfaces_module.md#ansible-collections-vyos-vyos-vyos-l3-interfaces-module) – L3 interfaces resource module
- [vyos_lag_interfaces module](vyos_lag_interfaces_module.md#ansible-collections-vyos-vyos-vyos-lag-interfaces-module) – LAG interfaces resource module
- [vyos_linkagg module](vyos_linkagg_module.md#ansible-collections-vyos-vyos-vyos-linkagg-module) – (deprecated, removed after 2022-06-01) Manage link aggregation groups on VyOS network devices
- [vyos_lldp module](vyos_lldp_module.md#ansible-collections-vyos-vyos-vyos-lldp-module) – (deprecated, removed after 2022-06-01) Manage LLDP configuration on VyOS network devices
- [vyos_lldp_global module](vyos_lldp_global_module.md#ansible-collections-vyos-vyos-vyos-lldp-global-module) – LLDP global resource module
- [vyos_lldp_interface module](vyos_lldp_interface_module.md#ansible-collections-vyos-vyos-vyos-lldp-interface-module) – (deprecated, removed after 2022-06-01) Manage LLDP interfaces configuration on VyOS network devices
- [vyos_lldp_interfaces module](vyos_lldp_interfaces_module.md#ansible-collections-vyos-vyos-vyos-lldp-interfaces-module) – LLDP interfaces resource module
- [vyos_logging module](vyos_logging_module.md#ansible-collections-vyos-vyos-vyos-logging-module) – Manage logging on network devices
- [vyos_logging_global module](vyos_logging_global_module.md#ansible-collections-vyos-vyos-vyos-logging-global-module) – Logging resource module
- [vyos_ntp_global module](vyos_ntp_global_module.md#ansible-collections-vyos-vyos-vyos-ntp-global-module) – Manages ntp modules of Vyos network devices
- [vyos_ospf_interfaces module](vyos_ospf_interfaces_module.md#ansible-collections-vyos-vyos-vyos-ospf-interfaces-module) – OSPF Interfaces Resource Module.
- [vyos_ospfv2 module](vyos_ospfv2_module.md#ansible-collections-vyos-vyos-vyos-ospfv2-module) – OSPFv2 resource module
- [vyos_ospfv3 module](vyos_ospfv3_module.md#ansible-collections-vyos-vyos-vyos-ospfv3-module) – OSPFV3 resource module
- [vyos_ping module](vyos_ping_module.md#ansible-collections-vyos-vyos-vyos-ping-module) – Tests reachability using ping from VyOS network devices
- [vyos_prefix_lists module](vyos_prefix_lists_module.md#ansible-collections-vyos-vyos-vyos-prefix-lists-module) – Prefix-Lists resource module for VyOS
- [vyos_route_maps module](vyos_route_maps_module.md#ansible-collections-vyos-vyos-vyos-route-maps-module) – Route Map Resource Module.
- [vyos_snmp_server module](vyos_snmp_server_module.md#ansible-collections-vyos-vyos-vyos-snmp-server-module) – Manages snmp_server resource module
- [vyos_static_route module](vyos_static_route_module.md#ansible-collections-vyos-vyos-vyos-static-route-module) – (deprecated, removed after 2022-06-01) Manage static IP routes on Vyatta VyOS network devices
- [vyos_static_routes module](vyos_static_routes_module.md#ansible-collections-vyos-vyos-vyos-static-routes-module) – Static routes resource module
- [vyos_system module](vyos_system_module.md#ansible-collections-vyos-vyos-vyos-system-module) – Run `set system` commands on VyOS devices
- [vyos_user module](vyos_user_module.md#ansible-collections-vyos-vyos-vyos-user-module) – Manage the collection of local users on VyOS device
- [vyos_vlan module](vyos_vlan_module.md#ansible-collections-vyos-vyos-vyos-vlan-module) – Manage VLANs on VyOS network devices

### Cliconf Plugins

- [vyos cliconf](vyos_cliconf.md#ansible-collections-vyos-vyos-vyos-cliconf) – Use vyos cliconf to run command on VyOS platform

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
