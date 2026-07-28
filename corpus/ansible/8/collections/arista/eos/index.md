---
collection: ansible
version: "8"
title: "Arista.Eos"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/index.html
fetched_at: 2026-07-28T01:01:51+00:00
---
# Arista.Eos

Collection version 6.2.2

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Network Collection for Arista EOS devices.

**Author:**

- Ansible Network Community (ansible-network)

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)

## [Plugin Index](index.md#id2)

These are the plugins in the arista.eos collection:

### Modules

- [eos_acl_interfaces module](eos_acl_interfaces_module.md#ansible-collections-arista-eos-eos-acl-interfaces-module) – ACL interfaces resource module
- [eos_acls module](eos_acls_module.md#ansible-collections-arista-eos-eos-acls-module) – ACLs resource module
- [eos_banner module](eos_banner_module.md#ansible-collections-arista-eos-eos-banner-module) – Manage multiline banners on Arista EOS devices
- [eos_bgp module](eos_bgp_module.md#ansible-collections-arista-eos-eos-bgp-module) – (deprecated, removed after 2023-01-29) Configure global BGP protocol settings on Arista EOS.
- [eos_bgp_address_family module](eos_bgp_address_family_module.md#ansible-collections-arista-eos-eos-bgp-address-family-module) – Manages BGP address family resource module
- [eos_bgp_global module](eos_bgp_global_module.md#ansible-collections-arista-eos-eos-bgp-global-module) – Manages BGP global resource module
- [eos_command module](eos_command_module.md#ansible-collections-arista-eos-eos-command-module) – Run arbitrary commands on an Arista EOS device
- [eos_config module](eos_config_module.md#ansible-collections-arista-eos-eos-config-module) – Manage Arista EOS configuration sections
- [eos_eapi module](eos_eapi_module.md#ansible-collections-arista-eos-eos-eapi-module) – Manage and configure Arista EOS eAPI.
- [eos_facts module](eos_facts_module.md#ansible-collections-arista-eos-eos-facts-module) – Collect facts from remote devices running Arista EOS
- [eos_hostname module](eos_hostname_module.md#ansible-collections-arista-eos-eos-hostname-module) – Manages hostname resource module
- [eos_interfaces module](eos_interfaces_module.md#ansible-collections-arista-eos-eos-interfaces-module) – Interfaces resource module
- [eos_l2_interfaces module](eos_l2_interfaces_module.md#ansible-collections-arista-eos-eos-l2-interfaces-module) – L2 interfaces resource module
- [eos_l3_interfaces module](eos_l3_interfaces_module.md#ansible-collections-arista-eos-eos-l3-interfaces-module) – L3 interfaces resource module
- [eos_lacp module](eos_lacp_module.md#ansible-collections-arista-eos-eos-lacp-module) – LACP resource module
- [eos_lacp_interfaces module](eos_lacp_interfaces_module.md#ansible-collections-arista-eos-eos-lacp-interfaces-module) – LACP interfaces resource module
- [eos_lag_interfaces module](eos_lag_interfaces_module.md#ansible-collections-arista-eos-eos-lag-interfaces-module) – LAG interfaces resource module
- [eos_lldp module](eos_lldp_module.md#ansible-collections-arista-eos-eos-lldp-module) – Manage LLDP configuration on Arista EOS network devices
- [eos_lldp_global module](eos_lldp_global_module.md#ansible-collections-arista-eos-eos-lldp-global-module) – LLDP resource module
- [eos_lldp_interfaces module](eos_lldp_interfaces_module.md#ansible-collections-arista-eos-eos-lldp-interfaces-module) – LLDP interfaces resource module
- [eos_logging module](eos_logging_module.md#ansible-collections-arista-eos-eos-logging-module) – Manage logging on network devices
- [eos_logging_global module](eos_logging_global_module.md#ansible-collections-arista-eos-eos-logging-global-module) – Manages logging resource module
- [eos_ntp_global module](eos_ntp_global_module.md#ansible-collections-arista-eos-eos-ntp-global-module) – Manages ntp resource module
- [eos_ospf_interfaces module](eos_ospf_interfaces_module.md#ansible-collections-arista-eos-eos-ospf-interfaces-module) – OSPF Interfaces Resource Module.
- [eos_ospfv2 module](eos_ospfv2_module.md#ansible-collections-arista-eos-eos-ospfv2-module) – OSPFv2 resource module
- [eos_ospfv3 module](eos_ospfv3_module.md#ansible-collections-arista-eos-eos-ospfv3-module) – OSPFv3 resource module
- [eos_prefix_lists module](eos_prefix_lists_module.md#ansible-collections-arista-eos-eos-prefix-lists-module) – Manages Prefix lists resource module
- [eos_route_maps module](eos_route_maps_module.md#ansible-collections-arista-eos-eos-route-maps-module) – Manages Route Maps resource module
- [eos_snmp_server module](eos_snmp_server_module.md#ansible-collections-arista-eos-eos-snmp-server-module) – Manages snmp_server resource module
- [eos_static_routes module](eos_static_routes_module.md#ansible-collections-arista-eos-eos-static-routes-module) – Static routes resource module
- [eos_system module](eos_system_module.md#ansible-collections-arista-eos-eos-system-module) – Manage the system attributes on Arista EOS devices
- [eos_user module](eos_user_module.md#ansible-collections-arista-eos-eos-user-module) – Manage the collection of local users on EOS devices
- [eos_vlans module](eos_vlans_module.md#ansible-collections-arista-eos-eos-vlans-module) – VLANs resource module
- [eos_vrf module](eos_vrf_module.md#ansible-collections-arista-eos-eos-vrf-module) – Manage VRFs on Arista EOS network devices

### Cliconf Plugins

- [eos cliconf](eos_cliconf.md#ansible-collections-arista-eos-eos-cliconf) – Use eos cliconf to run command on Arista EOS platform

### Httpapi Plugins

- [eos httpapi](eos_httpapi.md#ansible-collections-arista-eos-eos-httpapi) – Use eAPI to run command on eos platform

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
