---
collection: ansible
version: "8"
title: "Dellemc.Enterprise_Sonic"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/index.html
fetched_at: 2026-07-28T01:02:29+00:00
---
# Dellemc.Enterprise_Sonic

Collection version 2.2.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Network Collection for Enterprise SONiC Distribution by Dell Technologies

**Authors:**

- Senthil Kumar Ganesan <[Senthil_Kumar_Ganesa@Dell.com](mailto:Senthil_Kumar_Ganesa%40Dell.com)>
- Abirami <[Abirami_N@Dell.com](mailto:Abirami_N%40Dell.com)>
- Dhivya <[Dhivya_P@Dell.com](mailto:Dhivya_P%40Dell.com)>
- Mohamed Javeed <[Mohamed_Javeed_Faroo@Dell.com](mailto:Mohamed_Javeed_Faroo%40Dell.com)>
- Nirai Madai <[Niraimadaiselvam_Mar@Dell.com](mailto:Niraimadaiselvam_Mar%40Dell.com)>
- Shade Talabi <[Shade_Talabi@Dell.com](mailto:Shade_Talabi%40Dell.com)>
- Kerry Meyer <[Kerry_Meyer@Dell.com](mailto:Kerry_Meyer%40Dell.com)>
- Mingjun Zhang <[Mingjun_Zhang@Dell.com](mailto:Mingjun_Zhang%40Dell.com)>
- Arun Saravanan Balachandran ([arun_saravanan_balac@dell.com](mailto:arun_saravanan_balac%40dell.com))
- Santhosh Kumar T ([santhosh_kumar_t@dell.com](mailto:santhosh_kumar_t%40dell.com))
- Divya Balasubramanian <[Divya_Balasubramania@DELL.com](mailto:Divya_Balasubramania%40DELL.com)>
- Cypher Miller <[Cypher.Miller@Dell.com](mailto:Cypher.Miller%40Dell.com)>

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)

## [Plugin Index](index.md#id2)

These are the plugins in the dellemc.enterprise_sonic collection:

### Modules

- [sonic_aaa module](sonic_aaa_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-aaa-module) – Manage AAA and its parameters
- [sonic_acl_interfaces module](sonic_acl_interfaces_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-acl-interfaces-module) – Manage access control list (ACL) to interface binding on SONiC
- [sonic_api module](sonic_api_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-api-module) – Manages REST operations on devices running Enterprise SONiC
- [sonic_bfd module](sonic_bfd_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-bfd-module) – Manage BFD configuration on SONiC
- [sonic_bgp module](sonic_bgp_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-bgp-module) – Manage global BGP and its parameters
- [sonic_bgp_af module](sonic_bgp_af_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-bgp-af-module) – Manage global BGP address-family and its parameters
- [sonic_bgp_as_paths module](sonic_bgp_as_paths_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-bgp-as-paths-module) – Manage BGP autonomous system path (or as-path-list) and its parameters
- [sonic_bgp_communities module](sonic_bgp_communities_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-bgp-communities-module) – Manage BGP community and its parameters
- [sonic_bgp_ext_communities module](sonic_bgp_ext_communities_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-bgp-ext-communities-module) – Manage BGP extended community-list and its parameters
- [sonic_bgp_neighbors module](sonic_bgp_neighbors_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-bgp-neighbors-module) – Manage a BGP neighbor and its parameters
- [sonic_bgp_neighbors_af module](sonic_bgp_neighbors_af_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-bgp-neighbors-af-module) – Manage the BGP neighbor address-family and its parameters
- [sonic_command module](sonic_command_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-command-module) – Runs commands on devices running Enterprise SONiC
- [sonic_config module](sonic_config_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-config-module) – Manages configuration sections on devices running Enterprise SONiC
- [sonic_copp module](sonic_copp_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-copp-module) – Manage CoPP configuration on SONiC
- [sonic_dhcp_relay module](sonic_dhcp_relay_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-dhcp-relay-module) – Manage DHCP and DHCPv6 relay configurations on SONiC
- [sonic_facts module](sonic_facts_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-facts-module) – Collects facts on devices running Enterprise SONiC
- [sonic_interfaces module](sonic_interfaces_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-interfaces-module) – Configure Interface attributes on interfaces such as, Eth, LAG, VLAN, and loopback. (create a loopback interface if it does not exist.)
- [sonic_ip_neighbor module](sonic_ip_neighbor_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-ip-neighbor-module) – Manage IP neighbor global configuration on SONiC.
- [sonic_l2_acls module](sonic_l2_acls_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-l2-acls-module) – Manage Layer 2 access control lists (ACL) configurations on SONiC
- [sonic_l2_interfaces module](sonic_l2_interfaces_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-l2-interfaces-module) – Configure interface-to-VLAN association that is based on access or trunk mode
- [sonic_l3_acls module](sonic_l3_acls_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-l3-acls-module) – Manage Layer 3 access control lists (ACL) configurations on SONiC
- [sonic_l3_interfaces module](sonic_l3_interfaces_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-l3-interfaces-module) – Configure the IPv4 and IPv6 parameters on Interfaces such as, Eth, LAG, VLAN, and loopback
- [sonic_lag_interfaces module](sonic_lag_interfaces_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-lag-interfaces-module) – Manage link aggregation group (LAG) interface parameters
- [sonic_lldp_global module](sonic_lldp_global_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-lldp-global-module) – Manage Global LLDP configurations on SONiC
- [sonic_logging module](sonic_logging_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-logging-module) – Manage logging configuration on SONiC.
- [sonic_mac module](sonic_mac_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-mac-module) – Manage MAC configuration on SONiC
- [sonic_mclag module](sonic_mclag_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-mclag-module) – Manage multi chassis link aggregation groups domain (MCLAG) and its parameters
- [sonic_ntp module](sonic_ntp_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-ntp-module) – Manage NTP configuration on SONiC.
- [sonic_port_breakout module](sonic_port_breakout_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-port-breakout-module) – Configure port breakout settings on physical interfaces
- [sonic_port_group module](sonic_port_group_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-port-group-module) – Manages port group configuration on SONiC.
- [sonic_prefix_lists module](sonic_prefix_lists_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-prefix-lists-module) – prefix list configuration handling for SONiC
- [sonic_radius_server module](sonic_radius_server_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-radius-server-module) – Manage RADIUS server and its parameters
- [sonic_route_maps module](sonic_route_maps_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-route-maps-module) – route map configuration handling for SONiC
- [sonic_static_routes module](sonic_static_routes_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-static-routes-module) – Manage static routes configuration on SONiC
- [sonic_system module](sonic_system_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-system-module) – Configure system parameters
- [sonic_tacacs_server module](sonic_tacacs_server_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-tacacs-server-module) – Manage TACACS server and its parameters
- [sonic_users module](sonic_users_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-users-module) – Manage users and its parameters
- [sonic_vlan_mapping module](sonic_vlan_mapping_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-vlan-mapping-module) – Configure vlan mappings on SONiC.
- [sonic_vlans module](sonic_vlans_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-vlans-module) – Manage VLAN and its parameters
- [sonic_vrfs module](sonic_vrfs_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-vrfs-module) – Manage VRFs and associate VRFs to interfaces such as, Eth, LAG, VLAN, and loopback
- [sonic_vxlans module](sonic_vxlans_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-vxlans-module) – Manage VxLAN EVPN and its parameters

### Cliconf Plugins

- [sonic cliconf](sonic_cliconf.md#ansible-collections-dellemc-enterprise-sonic-sonic-cliconf) – Use sonic cliconf to run command on Dell OS10 platform

### Httpapi Plugins

- [sonic httpapi](sonic_httpapi.md#ansible-collections-dellemc-enterprise-sonic-sonic-httpapi) – HttpApi Plugin for devices supporting Restconf SONIC API

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
