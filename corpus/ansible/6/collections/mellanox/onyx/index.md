---
collection: ansible
version: "6"
title: "Mellanox.Onyx"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/index.html
fetched_at: 2026-07-27T16:42:02+00:00
---
# Mellanox.Onyx

Collection version 1.0.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Collection for managing Mellanox onyx devices

**Author:**

- Samer Deeb (@samerd)

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)

## [Plugin Index](index.md#id2)

These are the plugins in the mellanox.onyx collection:

### Modules

- [onyx_aaa module](onyx_aaa_module.md#ansible-collections-mellanox-onyx-onyx-aaa-module) – Configures AAA parameters
- [onyx_bfd module](onyx_bfd_module.md#ansible-collections-mellanox-onyx-onyx-bfd-module) – Configures BFD parameters
- [onyx_bgp module](onyx_bgp_module.md#ansible-collections-mellanox-onyx-onyx-bgp-module) – Configures BGP on Mellanox ONYX network devices
- [onyx_buffer_pool module](onyx_buffer_pool_module.md#ansible-collections-mellanox-onyx-onyx-buffer-pool-module) – Configures Buffer Pool
- [onyx_command module](onyx_command_module.md#ansible-collections-mellanox-onyx-onyx-command-module) – Run commands on remote devices running Mellanox ONYX
- [onyx_config module](onyx_config_module.md#ansible-collections-mellanox-onyx-onyx-config-module) – Manage Mellanox ONYX configuration sections
- [onyx_facts module](onyx_facts_module.md#ansible-collections-mellanox-onyx-onyx-facts-module) – Collect facts from Mellanox ONYX network devices
- [onyx_igmp module](onyx_igmp_module.md#ansible-collections-mellanox-onyx-onyx-igmp-module) – Configures IGMP global parameters
- [onyx_igmp_interface module](onyx_igmp_interface_module.md#ansible-collections-mellanox-onyx-onyx-igmp-interface-module) – Configures IGMP interface parameters
- [onyx_igmp_vlan module](onyx_igmp_vlan_module.md#ansible-collections-mellanox-onyx-onyx-igmp-vlan-module) – Configures IGMP Vlan parameters
- [onyx_interface module](onyx_interface_module.md#ansible-collections-mellanox-onyx-onyx-interface-module) – Manage Interfaces on Mellanox ONYX network devices
- [onyx_l2_interface module](onyx_l2_interface_module.md#ansible-collections-mellanox-onyx-onyx-l2-interface-module) – Manage Layer-2 interface on Mellanox ONYX network devices
- [onyx_l3_interface module](onyx_l3_interface_module.md#ansible-collections-mellanox-onyx-onyx-l3-interface-module) – Manage L3 interfaces on Mellanox ONYX network devices
- [onyx_linkagg module](onyx_linkagg_module.md#ansible-collections-mellanox-onyx-onyx-linkagg-module) – Manage link aggregation groups on Mellanox ONYX network devices
- [onyx_lldp module](onyx_lldp_module.md#ansible-collections-mellanox-onyx-onyx-lldp-module) – Manage LLDP configuration on Mellanox ONYX network devices
- [onyx_lldp_interface module](onyx_lldp_interface_module.md#ansible-collections-mellanox-onyx-onyx-lldp-interface-module) – Manage LLDP interfaces configuration on Mellanox ONYX network devices
- [onyx_magp module](onyx_magp_module.md#ansible-collections-mellanox-onyx-onyx-magp-module) – Manage MAGP protocol on Mellanox ONYX network devices
- [onyx_mlag_ipl module](onyx_mlag_ipl_module.md#ansible-collections-mellanox-onyx-onyx-mlag-ipl-module) – Manage IPL (inter-peer link) on Mellanox ONYX network devices
- [onyx_mlag_vip module](onyx_mlag_vip_module.md#ansible-collections-mellanox-onyx-onyx-mlag-vip-module) – Configures MLAG VIP on Mellanox ONYX network devices
- [onyx_ntp module](onyx_ntp_module.md#ansible-collections-mellanox-onyx-onyx-ntp-module) – Manage NTP general configurations and ntp keys configurations on Mellanox ONYX network devices
- [onyx_ntp_servers_peers module](onyx_ntp_servers_peers_module.md#ansible-collections-mellanox-onyx-onyx-ntp-servers-peers-module) – Configures NTP peers and servers parameters
- [onyx_ospf module](onyx_ospf_module.md#ansible-collections-mellanox-onyx-onyx-ospf-module) – Manage OSPF protocol on Mellanox ONYX network devices
- [onyx_pfc_interface module](onyx_pfc_interface_module.md#ansible-collections-mellanox-onyx-onyx-pfc-interface-module) – Manage priority flow control on ONYX network devices
- [onyx_protocol module](onyx_protocol_module.md#ansible-collections-mellanox-onyx-onyx-protocol-module) – Enables/Disables protocols on Mellanox ONYX network devices
- [onyx_ptp_global module](onyx_ptp_global_module.md#ansible-collections-mellanox-onyx-onyx-ptp-global-module) – Configures PTP Global parameters
- [onyx_ptp_interface module](onyx_ptp_interface_module.md#ansible-collections-mellanox-onyx-onyx-ptp-interface-module) – Configures PTP on interface
- [onyx_qos module](onyx_qos_module.md#ansible-collections-mellanox-onyx-onyx-qos-module) – Configures QoS
- [onyx_snmp module](onyx_snmp_module.md#ansible-collections-mellanox-onyx-onyx-snmp-module) – Manages SNMP general configurations on Mellanox ONYX network devices
- [onyx_snmp_hosts module](onyx_snmp_hosts_module.md#ansible-collections-mellanox-onyx-onyx-snmp-hosts-module) – Configures SNMP host parameters
- [onyx_snmp_users module](onyx_snmp_users_module.md#ansible-collections-mellanox-onyx-onyx-snmp-users-module) – Configures SNMP User parameters
- [onyx_syslog_files module](onyx_syslog_files_module.md#ansible-collections-mellanox-onyx-onyx-syslog-files-module) – Configure file management syslog module
- [onyx_syslog_remote module](onyx_syslog_remote_module.md#ansible-collections-mellanox-onyx-onyx-syslog-remote-module) – Configure remote syslog module
- [onyx_traffic_class module](onyx_traffic_class_module.md#ansible-collections-mellanox-onyx-onyx-traffic-class-module) – Configures Traffic Class
- [onyx_username module](onyx_username_module.md#ansible-collections-mellanox-onyx-onyx-username-module) – Configure username module
- [onyx_vlan module](onyx_vlan_module.md#ansible-collections-mellanox-onyx-onyx-vlan-module) – Manage VLANs on Mellanox ONYX network devices
- [onyx_vxlan module](onyx_vxlan_module.md#ansible-collections-mellanox-onyx-onyx-vxlan-module) – Configures Vxlan
- [onyx_wjh module](onyx_wjh_module.md#ansible-collections-mellanox-onyx-onyx-wjh-module) – Configure what-just-happend module

### Cliconf Plugins

- [onyx cliconf](onyx_cliconf.md#ansible-collections-mellanox-onyx-onyx-cliconf) – Use onyx cliconf to run command on Mellanox ONYX platform

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
