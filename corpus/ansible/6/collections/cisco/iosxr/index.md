---
collection: ansible
version: "6"
title: "Cisco.Iosxr"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/index.html
fetched_at: 2026-07-27T16:41:38+00:00
---
# Cisco.Iosxr

Collection version 3.3.1

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Network Collection for Cisco IOSXR devices.

**Author:**

- Ansible Network Community (ansible-network)

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)

## [Plugin Index](index.md#id2)

These are the plugins in the cisco.iosxr collection:

### Modules

- [iosxr_acl_interfaces module](iosxr_acl_interfaces_module.md#ansible-collections-cisco-iosxr-iosxr-acl-interfaces-module) – Resource module to configure ACL interfaces.
- [iosxr_acls module](iosxr_acls_module.md#ansible-collections-cisco-iosxr-iosxr-acls-module) – Resource module to configure ACLs.
- [iosxr_banner module](iosxr_banner_module.md#ansible-collections-cisco-iosxr-iosxr-banner-module) – Module to configure multiline banners.
- [iosxr_bgp module](iosxr_bgp_module.md#ansible-collections-cisco-iosxr-iosxr-bgp-module) – Module to configure BGP protocol settings.
- [iosxr_bgp_address_family module](iosxr_bgp_address_family_module.md#ansible-collections-cisco-iosxr-iosxr-bgp-address-family-module) – Resource module to configure BGP Address family.
- [iosxr_bgp_global module](iosxr_bgp_global_module.md#ansible-collections-cisco-iosxr-iosxr-bgp-global-module) – Resource module to configure BGP.
- [iosxr_bgp_neighbor_address_family module](iosxr_bgp_neighbor_address_family_module.md#ansible-collections-cisco-iosxr-iosxr-bgp-neighbor-address-family-module) – Resource module to configure BGP Neighbor Address family.
- [iosxr_command module](iosxr_command_module.md#ansible-collections-cisco-iosxr-iosxr-command-module) – Module to run commands on remote devices.
- [iosxr_config module](iosxr_config_module.md#ansible-collections-cisco-iosxr-iosxr-config-module) – Module to manage configuration sections.
- [iosxr_facts module](iosxr_facts_module.md#ansible-collections-cisco-iosxr-iosxr-facts-module) – Module to collect facts from remote devices.
- [iosxr_hostname module](iosxr_hostname_module.md#ansible-collections-cisco-iosxr-iosxr-hostname-module) – Resource module to configure hostname.
- [iosxr_interface module](iosxr_interface_module.md#ansible-collections-cisco-iosxr-iosxr-interface-module) – (deprecated, removed after 2022-06-01) Manage Interface on Cisco IOS XR network devices
- [iosxr_interfaces module](iosxr_interfaces_module.md#ansible-collections-cisco-iosxr-iosxr-interfaces-module) – Resource module to configure interfaces.
- [iosxr_l2_interfaces module](iosxr_l2_interfaces_module.md#ansible-collections-cisco-iosxr-iosxr-l2-interfaces-module) – Resource Module to configure L2 interfaces.
- [iosxr_l3_interfaces module](iosxr_l3_interfaces_module.md#ansible-collections-cisco-iosxr-iosxr-l3-interfaces-module) – Resource module to configure L3 interfaces.
- [iosxr_lacp module](iosxr_lacp_module.md#ansible-collections-cisco-iosxr-iosxr-lacp-module) – Resource module to configure LACP.
- [iosxr_lacp_interfaces module](iosxr_lacp_interfaces_module.md#ansible-collections-cisco-iosxr-iosxr-lacp-interfaces-module) – Resource module to configure LACP interfaces.
- [iosxr_lag_interfaces module](iosxr_lag_interfaces_module.md#ansible-collections-cisco-iosxr-iosxr-lag-interfaces-module) – Resource module to configure LAG interfaces.
- [iosxr_lldp_global module](iosxr_lldp_global_module.md#ansible-collections-cisco-iosxr-iosxr-lldp-global-module) – Resource module to configure LLDP.
- [iosxr_lldp_interfaces module](iosxr_lldp_interfaces_module.md#ansible-collections-cisco-iosxr-iosxr-lldp-interfaces-module) – Resource module to configure LLDP interfaces.
- [iosxr_logging module](iosxr_logging_module.md#ansible-collections-cisco-iosxr-iosxr-logging-module) – (deprecated, removed after 2023-08-01) Configuration management of system logging services on network devices
- [iosxr_logging_global module](iosxr_logging_global_module.md#ansible-collections-cisco-iosxr-iosxr-logging-global-module) – Resource module to configure logging.
- [iosxr_netconf module](iosxr_netconf_module.md#ansible-collections-cisco-iosxr-iosxr-netconf-module) – Configures NetConf sub-system service on Cisco IOS-XR devices
- [iosxr_ntp_global module](iosxr_ntp_global_module.md#ansible-collections-cisco-iosxr-iosxr-ntp-global-module) – Resource module to configure NTP.
- [iosxr_ospf_interfaces module](iosxr_ospf_interfaces_module.md#ansible-collections-cisco-iosxr-iosxr-ospf-interfaces-module) – Resource module to configure OSPF interfaces.
- [iosxr_ospfv2 module](iosxr_ospfv2_module.md#ansible-collections-cisco-iosxr-iosxr-ospfv2-module) – Resource module to configure OSPFv2.
- [iosxr_ospfv3 module](iosxr_ospfv3_module.md#ansible-collections-cisco-iosxr-iosxr-ospfv3-module) – Resource module to configure OSPFv3.
- [iosxr_ping module](iosxr_ping_module.md#ansible-collections-cisco-iosxr-iosxr-ping-module) – Tests reachability using ping from IOSXR switch.
- [iosxr_prefix_lists module](iosxr_prefix_lists_module.md#ansible-collections-cisco-iosxr-iosxr-prefix-lists-module) – Resource module to configure prefix lists.
- [iosxr_snmp_server module](iosxr_snmp_server_module.md#ansible-collections-cisco-iosxr-iosxr-snmp-server-module) – Resource module to configure snmp server.
- [iosxr_static_routes module](iosxr_static_routes_module.md#ansible-collections-cisco-iosxr-iosxr-static-routes-module) – Resource module to configure static routes.
- [iosxr_system module](iosxr_system_module.md#ansible-collections-cisco-iosxr-iosxr-system-module) – Module to manage the system attributes.
- [iosxr_user module](iosxr_user_module.md#ansible-collections-cisco-iosxr-iosxr-user-module) – Module to manage the aggregates of local users.

### Cliconf Plugins

- [iosxr cliconf](iosxr_cliconf.md#ansible-collections-cisco-iosxr-iosxr-cliconf) – Use iosxr cliconf to run command on Cisco IOS XR platform

### Netconf Plugins

- [iosxr netconf](iosxr_netconf.md#ansible-collections-cisco-iosxr-iosxr-netconf) – Use iosxr netconf plugin to run netconf commands on Cisco IOSXR platform

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
