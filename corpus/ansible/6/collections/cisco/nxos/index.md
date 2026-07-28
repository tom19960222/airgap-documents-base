---
collection: ansible
version: "6"
title: "Cisco.Nxos"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/index.html
fetched_at: 2026-07-27T16:41:40+00:00
---
# Cisco.Nxos

Collection version 3.2.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Network Collection for Cisco NXOS devices.

**Author:**

- Ansible Network Community (ansible-network)

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)

## [Plugin Index](index.md#id2)

These are the plugins in the cisco.nxos collection:

### Modules

- [nxos_aaa_server module](nxos_aaa_server_module.md#ansible-collections-cisco-nxos-nxos-aaa-server-module) – Manages AAA server global configuration.
- [nxos_aaa_server_host module](nxos_aaa_server_host_module.md#ansible-collections-cisco-nxos-nxos-aaa-server-host-module) – Manages AAA server host-specific configuration.
- [nxos_acl module](nxos_acl_module.md#ansible-collections-cisco-nxos-nxos-acl-module) – (deprecated, removed after 2022-06-01) Manages access list entries for ACLs.
- [nxos_acl_interface module](nxos_acl_interface_module.md#ansible-collections-cisco-nxos-nxos-acl-interface-module) – (deprecated, removed after 2022-06-01) Manages applying ACLs to interfaces.
- [nxos_acl_interfaces module](nxos_acl_interfaces_module.md#ansible-collections-cisco-nxos-nxos-acl-interfaces-module) – ACL interfaces resource module
- [nxos_acls module](nxos_acls_module.md#ansible-collections-cisco-nxos-nxos-acls-module) – ACLs resource module
- [nxos_banner module](nxos_banner_module.md#ansible-collections-cisco-nxos-nxos-banner-module) – Manage multiline banners on Cisco NXOS devices
- [nxos_bfd_global module](nxos_bfd_global_module.md#ansible-collections-cisco-nxos-nxos-bfd-global-module) – Bidirectional Forwarding Detection (BFD) global-level configuration
- [nxos_bfd_interfaces module](nxos_bfd_interfaces_module.md#ansible-collections-cisco-nxos-nxos-bfd-interfaces-module) – BFD interfaces resource module
- [nxos_bgp module](nxos_bgp_module.md#ansible-collections-cisco-nxos-nxos-bgp-module) – (deprecated, removed after 2023-01-27) Manages BGP configuration.
- [nxos_bgp_address_family module](nxos_bgp_address_family_module.md#ansible-collections-cisco-nxos-nxos-bgp-address-family-module) – BGP Address Family resource module.
- [nxos_bgp_af module](nxos_bgp_af_module.md#ansible-collections-cisco-nxos-nxos-bgp-af-module) – (deprecated, removed after 2023-02-24) Manages BGP Address-family configuration.
- [nxos_bgp_global module](nxos_bgp_global_module.md#ansible-collections-cisco-nxos-nxos-bgp-global-module) – BGP Global resource module.
- [nxos_bgp_neighbor module](nxos_bgp_neighbor_module.md#ansible-collections-cisco-nxos-nxos-bgp-neighbor-module) – (deprecated, removed after 2023-01-27) Manages BGP neighbors configurations.
- [nxos_bgp_neighbor_address_family module](nxos_bgp_neighbor_address_family_module.md#ansible-collections-cisco-nxos-nxos-bgp-neighbor-address-family-module) – BGP Neighbor Address Family resource module.
- [nxos_bgp_neighbor_af module](nxos_bgp_neighbor_af_module.md#ansible-collections-cisco-nxos-nxos-bgp-neighbor-af-module) – (deprecated, removed after 2023-02-24) Manages BGP address-family’s neighbors configuration.
- [nxos_command module](nxos_command_module.md#ansible-collections-cisco-nxos-nxos-command-module) – Run arbitrary command on Cisco NXOS devices
- [nxos_config module](nxos_config_module.md#ansible-collections-cisco-nxos-nxos-config-module) – Manage Cisco NXOS configuration sections
- [nxos_devicealias module](nxos_devicealias_module.md#ansible-collections-cisco-nxos-nxos-devicealias-module) – Configuration of device alias for Cisco NXOS MDS Switches.
- [nxos_evpn_global module](nxos_evpn_global_module.md#ansible-collections-cisco-nxos-nxos-evpn-global-module) – Handles the EVPN control plane for VXLAN.
- [nxos_evpn_vni module](nxos_evpn_vni_module.md#ansible-collections-cisco-nxos-nxos-evpn-vni-module) – Manages Cisco EVPN VXLAN Network Identifier (VNI).
- [nxos_facts module](nxos_facts_module.md#ansible-collections-cisco-nxos-nxos-facts-module) – Gets facts about NX-OS switches
- [nxos_feature module](nxos_feature_module.md#ansible-collections-cisco-nxos-nxos-feature-module) – Manage features in NX-OS switches.
- [nxos_file_copy module](nxos_file_copy_module.md#ansible-collections-cisco-nxos-nxos-file-copy-module) – Copy a file to a remote NXOS device.
- [nxos_gir module](nxos_gir_module.md#ansible-collections-cisco-nxos-nxos-gir-module) – Trigger a graceful removal or insertion (GIR) of the switch.
- [nxos_gir_profile_management module](nxos_gir_profile_management_module.md#ansible-collections-cisco-nxos-nxos-gir-profile-management-module) – Create a maintenance-mode or normal-mode profile for GIR.
- [nxos_hostname module](nxos_hostname_module.md#ansible-collections-cisco-nxos-nxos-hostname-module) – Hostname resource module.
- [nxos_hsrp module](nxos_hsrp_module.md#ansible-collections-cisco-nxos-nxos-hsrp-module) – Manages HSRP configuration on NX-OS switches.
- [nxos_hsrp_interfaces module](nxos_hsrp_interfaces_module.md#ansible-collections-cisco-nxos-nxos-hsrp-interfaces-module) – HSRP interfaces resource module
- [nxos_igmp module](nxos_igmp_module.md#ansible-collections-cisco-nxos-nxos-igmp-module) – Manages IGMP global configuration.
- [nxos_igmp_interface module](nxos_igmp_interface_module.md#ansible-collections-cisco-nxos-nxos-igmp-interface-module) – Manages IGMP interface configuration.
- [nxos_igmp_snooping module](nxos_igmp_snooping_module.md#ansible-collections-cisco-nxos-nxos-igmp-snooping-module) – Manages IGMP snooping global configuration.
- [nxos_install_os module](nxos_install_os_module.md#ansible-collections-cisco-nxos-nxos-install-os-module) – Set boot options like boot, kickstart image and issu.
- [nxos_interface module](nxos_interface_module.md#ansible-collections-cisco-nxos-nxos-interface-module) – (deprecated, removed after 2022-06-01) Manages physical attributes of interfaces.
- [nxos_interface_ospf module](nxos_interface_ospf_module.md#ansible-collections-cisco-nxos-nxos-interface-ospf-module) – (deprecated, removed after 2022-10-26) Manages configuration of an OSPF interface instance.
- [nxos_interfaces module](nxos_interfaces_module.md#ansible-collections-cisco-nxos-nxos-interfaces-module) – Interfaces resource module
- [nxos_l2_interface module](nxos_l2_interface_module.md#ansible-collections-cisco-nxos-nxos-l2-interface-module) – (deprecated, removed after 2022-06-01) Manage Layer-2 interface on Cisco NXOS devices.
- [nxos_l2_interfaces module](nxos_l2_interfaces_module.md#ansible-collections-cisco-nxos-nxos-l2-interfaces-module) – L2 interfaces resource module
- [nxos_l3_interface module](nxos_l3_interface_module.md#ansible-collections-cisco-nxos-nxos-l3-interface-module) – (deprecated, removed after 2022-06-01) Manage L3 interfaces on Cisco NXOS network devices
- [nxos_l3_interfaces module](nxos_l3_interfaces_module.md#ansible-collections-cisco-nxos-nxos-l3-interfaces-module) – L3 interfaces resource module
- [nxos_lacp module](nxos_lacp_module.md#ansible-collections-cisco-nxos-nxos-lacp-module) – LACP resource module
- [nxos_lacp_interfaces module](nxos_lacp_interfaces_module.md#ansible-collections-cisco-nxos-nxos-lacp-interfaces-module) – LACP interfaces resource module
- [nxos_lag_interfaces module](nxos_lag_interfaces_module.md#ansible-collections-cisco-nxos-nxos-lag-interfaces-module) – LAG interfaces resource module
- [nxos_linkagg module](nxos_linkagg_module.md#ansible-collections-cisco-nxos-nxos-linkagg-module) – (deprecated, removed after 2022-06-01) Manage link aggregation groups on Cisco NXOS devices.
- [nxos_lldp module](nxos_lldp_module.md#ansible-collections-cisco-nxos-nxos-lldp-module) – (deprecated, removed after 2022-06-01) Manage LLDP configuration on Cisco NXOS network devices.
- [nxos_lldp_global module](nxos_lldp_global_module.md#ansible-collections-cisco-nxos-nxos-lldp-global-module) – LLDP resource module
- [nxos_lldp_interfaces module](nxos_lldp_interfaces_module.md#ansible-collections-cisco-nxos-nxos-lldp-interfaces-module) – LLDP interfaces resource module
- [nxos_logging module](nxos_logging_module.md#ansible-collections-cisco-nxos-nxos-logging-module) – Manage logging on network devices
- [nxos_logging_global module](nxos_logging_global_module.md#ansible-collections-cisco-nxos-nxos-logging-global-module) – Logging resource module.
- [nxos_ntp module](nxos_ntp_module.md#ansible-collections-cisco-nxos-nxos-ntp-module) – Manages core NTP configuration.
- [nxos_ntp_auth module](nxos_ntp_auth_module.md#ansible-collections-cisco-nxos-nxos-ntp-auth-module) – Manages NTP authentication.
- [nxos_ntp_global module](nxos_ntp_global_module.md#ansible-collections-cisco-nxos-nxos-ntp-global-module) – NTP Global resource module.
- [nxos_ntp_options module](nxos_ntp_options_module.md#ansible-collections-cisco-nxos-nxos-ntp-options-module) – Manages NTP options.
- [nxos_nxapi module](nxos_nxapi_module.md#ansible-collections-cisco-nxos-nxos-nxapi-module) – Manage NXAPI configuration on an NXOS device.
- [nxos_ospf module](nxos_ospf_module.md#ansible-collections-cisco-nxos-nxos-ospf-module) – (deprecated, removed after 2022-06-01) Manages configuration of an ospf instance.
- [nxos_ospf_interfaces module](nxos_ospf_interfaces_module.md#ansible-collections-cisco-nxos-nxos-ospf-interfaces-module) – OSPF Interfaces Resource Module.
- [nxos_ospf_vrf module](nxos_ospf_vrf_module.md#ansible-collections-cisco-nxos-nxos-ospf-vrf-module) – (deprecated, removed after 2022-10-01)Manages a VRF for an OSPF router.
- [nxos_ospfv2 module](nxos_ospfv2_module.md#ansible-collections-cisco-nxos-nxos-ospfv2-module) – OSPFv2 resource module
- [nxos_ospfv3 module](nxos_ospfv3_module.md#ansible-collections-cisco-nxos-nxos-ospfv3-module) – OSPFv3 resource module
- [nxos_overlay_global module](nxos_overlay_global_module.md#ansible-collections-cisco-nxos-nxos-overlay-global-module) – Configures anycast gateway MAC of the switch.
- [nxos_pim module](nxos_pim_module.md#ansible-collections-cisco-nxos-nxos-pim-module) – Manages configuration of a PIM instance.
- [nxos_pim_interface module](nxos_pim_interface_module.md#ansible-collections-cisco-nxos-nxos-pim-interface-module) – Manages PIM interface configuration.
- [nxos_pim_rp_address module](nxos_pim_rp_address_module.md#ansible-collections-cisco-nxos-nxos-pim-rp-address-module) – Manages configuration of an PIM static RP address instance.
- [nxos_ping module](nxos_ping_module.md#ansible-collections-cisco-nxos-nxos-ping-module) – Tests reachability using ping from Nexus switch.
- [nxos_prefix_lists module](nxos_prefix_lists_module.md#ansible-collections-cisco-nxos-nxos-prefix-lists-module) – Prefix-Lists resource module.
- [nxos_reboot module](nxos_reboot_module.md#ansible-collections-cisco-nxos-nxos-reboot-module) – Reboot a network device.
- [nxos_rollback module](nxos_rollback_module.md#ansible-collections-cisco-nxos-nxos-rollback-module) – Set a checkpoint or rollback to a checkpoint.
- [nxos_route_maps module](nxos_route_maps_module.md#ansible-collections-cisco-nxos-nxos-route-maps-module) – Route Maps resource module.
- [nxos_rpm module](nxos_rpm_module.md#ansible-collections-cisco-nxos-nxos-rpm-module) – Install patch or feature rpms on Cisco NX-OS devices.
- [nxos_smu module](nxos_smu_module.md#ansible-collections-cisco-nxos-nxos-smu-module) – (deprecated, removed after 2022-10-01) Perform SMUs on Cisco NX-OS devices.
- [nxos_snapshot module](nxos_snapshot_module.md#ansible-collections-cisco-nxos-nxos-snapshot-module) – Manage snapshots of the running states of selected features.
- [nxos_snmp_community module](nxos_snmp_community_module.md#ansible-collections-cisco-nxos-nxos-snmp-community-module) – (deprecated, removed after 2024-01-01) Manages SNMP community configs.
- [nxos_snmp_contact module](nxos_snmp_contact_module.md#ansible-collections-cisco-nxos-nxos-snmp-contact-module) – (deprecated, removed after 2024-01-01) Manages SNMP contact info.
- [nxos_snmp_host module](nxos_snmp_host_module.md#ansible-collections-cisco-nxos-nxos-snmp-host-module) – (deprecated, removed after 2024-01-01) Manages SNMP host configuration.
- [nxos_snmp_location module](nxos_snmp_location_module.md#ansible-collections-cisco-nxos-nxos-snmp-location-module) – (deprecated, removed after 2024-01-01) Manages SNMP location information.
- [nxos_snmp_server module](nxos_snmp_server_module.md#ansible-collections-cisco-nxos-nxos-snmp-server-module) – SNMP Server resource module.
- [nxos_snmp_traps module](nxos_snmp_traps_module.md#ansible-collections-cisco-nxos-nxos-snmp-traps-module) – (deprecated, removed after 2024-01-01) Manages SNMP traps.
- [nxos_snmp_user module](nxos_snmp_user_module.md#ansible-collections-cisco-nxos-nxos-snmp-user-module) – (deprecated, removed after 2024-01-01) Manages SNMP users for monitoring.
- [nxos_static_route module](nxos_static_route_module.md#ansible-collections-cisco-nxos-nxos-static-route-module) – (deprecated, removed after 2022-06-01) Manages static route configuration
- [nxos_static_routes module](nxos_static_routes_module.md#ansible-collections-cisco-nxos-nxos-static-routes-module) – Static routes resource module
- [nxos_system module](nxos_system_module.md#ansible-collections-cisco-nxos-nxos-system-module) – Manage the system attributes on Cisco NXOS devices
- [nxos_telemetry module](nxos_telemetry_module.md#ansible-collections-cisco-nxos-nxos-telemetry-module) – TELEMETRY resource module
- [nxos_udld module](nxos_udld_module.md#ansible-collections-cisco-nxos-nxos-udld-module) – Manages UDLD global configuration params.
- [nxos_udld_interface module](nxos_udld_interface_module.md#ansible-collections-cisco-nxos-nxos-udld-interface-module) – Manages UDLD interface configuration params.
- [nxos_user module](nxos_user_module.md#ansible-collections-cisco-nxos-nxos-user-module) – Manage the collection of local users on Nexus devices
- [nxos_vlan module](nxos_vlan_module.md#ansible-collections-cisco-nxos-nxos-vlan-module) – (deprecated, removed after 2022-06-01) Manages VLAN resources and attributes.
- [nxos_vlans module](nxos_vlans_module.md#ansible-collections-cisco-nxos-nxos-vlans-module) – VLANs resource module
- [nxos_vpc module](nxos_vpc_module.md#ansible-collections-cisco-nxos-nxos-vpc-module) – Manages global VPC configuration
- [nxos_vpc_interface module](nxos_vpc_interface_module.md#ansible-collections-cisco-nxos-nxos-vpc-interface-module) – Manages interface VPC configuration
- [nxos_vrf module](nxos_vrf_module.md#ansible-collections-cisco-nxos-nxos-vrf-module) – Manages global VRF configuration.
- [nxos_vrf_af module](nxos_vrf_af_module.md#ansible-collections-cisco-nxos-nxos-vrf-af-module) – Manages VRF AF.
- [nxos_vrf_interface module](nxos_vrf_interface_module.md#ansible-collections-cisco-nxos-nxos-vrf-interface-module) – Manages interface specific VRF configuration.
- [nxos_vrrp module](nxos_vrrp_module.md#ansible-collections-cisco-nxos-nxos-vrrp-module) – Manages VRRP configuration on NX-OS switches.
- [nxos_vsan module](nxos_vsan_module.md#ansible-collections-cisco-nxos-nxos-vsan-module) – Configuration of vsan for Cisco NXOS MDS Switches.
- [nxos_vtp_domain module](nxos_vtp_domain_module.md#ansible-collections-cisco-nxos-nxos-vtp-domain-module) – Manages VTP domain configuration.
- [nxos_vtp_password module](nxos_vtp_password_module.md#ansible-collections-cisco-nxos-nxos-vtp-password-module) – Manages VTP password configuration.
- [nxos_vtp_version module](nxos_vtp_version_module.md#ansible-collections-cisco-nxos-nxos-vtp-version-module) – Manages VTP version configuration.
- [nxos_vxlan_vtep module](nxos_vxlan_vtep_module.md#ansible-collections-cisco-nxos-nxos-vxlan-vtep-module) – Manages VXLAN Network Virtualization Endpoint (NVE).
- [nxos_vxlan_vtep_vni module](nxos_vxlan_vtep_vni_module.md#ansible-collections-cisco-nxos-nxos-vxlan-vtep-vni-module) – Creates a Virtual Network Identifier member (VNI)
- [nxos_zone_zoneset module](nxos_zone_zoneset_module.md#ansible-collections-cisco-nxos-nxos-zone-zoneset-module) – Configuration of zone/zoneset for Cisco NXOS MDS Switches.

### Cliconf Plugins

- [nxos cliconf](nxos_cliconf.md#ansible-collections-cisco-nxos-nxos-cliconf) – Use NX-OS cliconf to run commands on Cisco NX-OS platform

### Httpapi Plugins

- [nxos httpapi](nxos_httpapi.md#ansible-collections-cisco-nxos-nxos-httpapi) – Use NX-API to run commands on Cisco NX-OS platform

### Netconf Plugins

- [nxos netconf](nxos_netconf.md#ansible-collections-cisco-nxos-nxos-netconf) – Use nxos netconf plugin to run netconf commands on Cisco NX-OS platform.

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
