---
collection: ansible
version: "6"
title: "F5Networks.F5_Modules"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/index.html
fetched_at: 2026-07-27T16:41:55+00:00
---
# F5Networks.F5_Modules

Collection version 1.21.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

F5 BIG-IP Imperative Collection for Ansible

**Author:**

- Wojciech Wypior (@wojtek0806)

**Supported ansible-core versions:**

- 2.9 or newer

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)

## [Plugin Index](index.md#id2)

These are the plugins in the f5networks.f5_modules collection:

### Modules

- [bigip_apm_acl module](bigip_apm_acl_module.md#ansible-collections-f5networks-f5-modules-bigip-apm-acl-module) – Manage user-defined APM ACLs
- [bigip_apm_network_access module](bigip_apm_network_access_module.md#ansible-collections-f5networks-f5-modules-bigip-apm-network-access-module) – Manage APM Network Access resource
- [bigip_apm_policy_fetch module](bigip_apm_policy_fetch_module.md#ansible-collections-f5networks-f5-modules-bigip-apm-policy-fetch-module) – Exports the APM policy or APM access profile from remote nodes.
- [bigip_apm_policy_import module](bigip_apm_policy_import_module.md#ansible-collections-f5networks-f5-modules-bigip-apm-policy-import-module) – Manage BIG-IP APM policy or APM access profile imports
- [bigip_asm_advanced_settings module](bigip_asm_advanced_settings_module.md#ansible-collections-f5networks-f5-modules-bigip-asm-advanced-settings-module) – Manage BIG-IP system ASM advanced settings
- [bigip_asm_dos_application module](bigip_asm_dos_application_module.md#ansible-collections-f5networks-f5-modules-bigip-asm-dos-application-module) – Manage application settings for a DOS profile
- [bigip_asm_policy_fetch module](bigip_asm_policy_fetch_module.md#ansible-collections-f5networks-f5-modules-bigip-asm-policy-fetch-module) – Exports the ASM policy from remote nodes.
- [bigip_asm_policy_import module](bigip_asm_policy_import_module.md#ansible-collections-f5networks-f5-modules-bigip-asm-policy-import-module) – Manage BIG-IP ASM policy imports
- [bigip_asm_policy_manage module](bigip_asm_policy_manage_module.md#ansible-collections-f5networks-f5-modules-bigip-asm-policy-manage-module) – Manage BIG-IP ASM policies
- [bigip_asm_policy_server_technology module](bigip_asm_policy_server_technology_module.md#ansible-collections-f5networks-f5-modules-bigip-asm-policy-server-technology-module) – Manages Server Technology on an ASM policy
- [bigip_asm_policy_signature_set module](bigip_asm_policy_signature_set_module.md#ansible-collections-f5networks-f5-modules-bigip-asm-policy-signature-set-module) – Manages Signature Sets on an ASM policy
- [bigip_cgnat_lsn_pool module](bigip_cgnat_lsn_pool_module.md#ansible-collections-f5networks-f5-modules-bigip-cgnat-lsn-pool-module) – Manage CGNAT LSN Pools
- [bigip_cli_alias module](bigip_cli_alias_module.md#ansible-collections-f5networks-f5-modules-bigip-cli-alias-module) – Manage CLI aliases on a BIG-IP
- [bigip_cli_script module](bigip_cli_script_module.md#ansible-collections-f5networks-f5-modules-bigip-cli-script-module) – Manage CLI scripts on a BIG-IP
- [bigip_command module](bigip_command_module.md#ansible-collections-f5networks-f5-modules-bigip-command-module) – Run TMSH and BASH commands on F5 devices
- [bigip_config module](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) – Manage BIG-IP configuration sections
- [bigip_configsync_action module](bigip_configsync_action_module.md#ansible-collections-f5networks-f5-modules-bigip-configsync-action-module) – Perform different actions related to config-sync
- [bigip_data_group module](bigip_data_group_module.md#ansible-collections-f5networks-f5-modules-bigip-data-group-module) – Manage data groups on a BIG-IP
- [bigip_device_auth module](bigip_device_auth_module.md#ansible-collections-f5networks-f5-modules-bigip-device-auth-module) – Manage system authentication on a BIG-IP
- [bigip_device_auth_ldap module](bigip_device_auth_ldap_module.md#ansible-collections-f5networks-f5-modules-bigip-device-auth-ldap-module) – Manage LDAP device authentication settings on BIG-IP
- [bigip_device_auth_radius module](bigip_device_auth_radius_module.md#ansible-collections-f5networks-f5-modules-bigip-device-auth-radius-module) – Manages RADIUS auth configuration on a BIG-IP device
- [bigip_device_auth_radius_server module](bigip_device_auth_radius_server_module.md#ansible-collections-f5networks-f5-modules-bigip-device-auth-radius-server-module) – Manages the RADIUS server configuration of the device
- [bigip_device_certificate module](bigip_device_certificate_module.md#ansible-collections-f5networks-f5-modules-bigip-device-certificate-module) – Manage self-signed device certificates
- [bigip_device_connectivity module](bigip_device_connectivity_module.md#ansible-collections-f5networks-f5-modules-bigip-device-connectivity-module) – Manages device IP configuration settings for HA on a BIG-IP.
- [bigip_device_dns module](bigip_device_dns_module.md#ansible-collections-f5networks-f5-modules-bigip-device-dns-module) – Manage DNS settings on a BIG-IP
- [bigip_device_group module](bigip_device_group_module.md#ansible-collections-f5networks-f5-modules-bigip-device-group-module) – Manage device groups on a BIG-IP
- [bigip_device_group_member module](bigip_device_group_member_module.md#ansible-collections-f5networks-f5-modules-bigip-device-group-member-module) – Manages members in a device group
- [bigip_device_ha_group module](bigip_device_ha_group_module.md#ansible-collections-f5networks-f5-modules-bigip-device-ha-group-module) – Manage HA group settings on a BIG-IP system
- [bigip_device_httpd module](bigip_device_httpd_module.md#ansible-collections-f5networks-f5-modules-bigip-device-httpd-module) – Manage HTTPD related settings on a BIG-IP system
- [bigip_device_info module](bigip_device_info_module.md#ansible-collections-f5networks-f5-modules-bigip-device-info-module) – Collect information from F5 BIG-IP devices
- [bigip_device_license module](bigip_device_license_module.md#ansible-collections-f5networks-f5-modules-bigip-device-license-module) – Manage license installation and activation on BIG-IP devices
- [bigip_device_ntp module](bigip_device_ntp_module.md#ansible-collections-f5networks-f5-modules-bigip-device-ntp-module) – Manage NTP servers on a BIG-IP
- [bigip_device_sshd module](bigip_device_sshd_module.md#ansible-collections-f5networks-f5-modules-bigip-device-sshd-module) – Manage the SSHD settings of a BIG-IP
- [bigip_device_syslog module](bigip_device_syslog_module.md#ansible-collections-f5networks-f5-modules-bigip-device-syslog-module) – Manage system-level syslog settings on BIG-IP
- [bigip_device_traffic_group module](bigip_device_traffic_group_module.md#ansible-collections-f5networks-f5-modules-bigip-device-traffic-group-module) – Manages traffic groups on BIG-IP
- [bigip_device_trust module](bigip_device_trust_module.md#ansible-collections-f5networks-f5-modules-bigip-device-trust-module) – Manage the trust relationships between BIG-IPs
- [bigip_dns_cache_resolver module](bigip_dns_cache_resolver_module.md#ansible-collections-f5networks-f5-modules-bigip-dns-cache-resolver-module) – Manage DNS resolver cache configuration on a BIG-IP
- [bigip_dns_nameserver module](bigip_dns_nameserver_module.md#ansible-collections-f5networks-f5-modules-bigip-dns-nameserver-module) – Manage LTM DNS nameservers on a BIG-IP
- [bigip_dns_resolver module](bigip_dns_resolver_module.md#ansible-collections-f5networks-f5-modules-bigip-dns-resolver-module) – Manage DNS resolvers on a BIG-IP
- [bigip_dns_zone module](bigip_dns_zone_module.md#ansible-collections-f5networks-f5-modules-bigip-dns-zone-module) – Manage DNS zones on BIG-IP
- [bigip_file_copy module](bigip_file_copy_module.md#ansible-collections-f5networks-f5-modules-bigip-file-copy-module) – Manage files in datastores on a BIG-IP
- [bigip_firewall_address_list module](bigip_firewall_address_list_module.md#ansible-collections-f5networks-f5-modules-bigip-firewall-address-list-module) – Manage address lists on BIG-IP AFM
- [bigip_firewall_dos_profile module](bigip_firewall_dos_profile_module.md#ansible-collections-f5networks-f5-modules-bigip-firewall-dos-profile-module) – Manage AFM DoS profiles on a BIG-IP
- [bigip_firewall_dos_vector module](bigip_firewall_dos_vector_module.md#ansible-collections-f5networks-f5-modules-bigip-firewall-dos-vector-module) – Manage attack vector configuration in an AFM DoS profile
- [bigip_firewall_global_rules module](bigip_firewall_global_rules_module.md#ansible-collections-f5networks-f5-modules-bigip-firewall-global-rules-module) – Manage AFM global rule settings on BIG-IP
- [bigip_firewall_log_profile module](bigip_firewall_log_profile_module.md#ansible-collections-f5networks-f5-modules-bigip-firewall-log-profile-module) – Manages AFM logging profiles configured in the system
- [bigip_firewall_log_profile_network module](bigip_firewall_log_profile_network_module.md#ansible-collections-f5networks-f5-modules-bigip-firewall-log-profile-network-module) – Configures Network Firewall related settings of the log profile
- [bigip_firewall_policy module](bigip_firewall_policy_module.md#ansible-collections-f5networks-f5-modules-bigip-firewall-policy-module) – Manage AFM security firewall policies on a BIG-IP
- [bigip_firewall_port_list module](bigip_firewall_port_list_module.md#ansible-collections-f5networks-f5-modules-bigip-firewall-port-list-module) – Manage port lists on BIG-IP AFM
- [bigip_firewall_rule module](bigip_firewall_rule_module.md#ansible-collections-f5networks-f5-modules-bigip-firewall-rule-module) – Manage AFM Firewall rules
- [bigip_firewall_rule_list module](bigip_firewall_rule_list_module.md#ansible-collections-f5networks-f5-modules-bigip-firewall-rule-list-module) – Manage AFM security firewall policies on a BIG-IP
- [bigip_firewall_schedule module](bigip_firewall_schedule_module.md#ansible-collections-f5networks-f5-modules-bigip-firewall-schedule-module) – Manage BIG-IP AFM schedule configurations
- [bigip_gtm_datacenter module](bigip_gtm_datacenter_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-datacenter-module) – Manage Datacenter configuration in BIG-IP
- [bigip_gtm_dns_listener module](bigip_gtm_dns_listener_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-dns-listener-module) – Configures the BIG-IP DNS system to answer TCP or UDP DNS requests
- [bigip_gtm_global module](bigip_gtm_global_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-global-module) – Manages global GTM settings
- [bigip_gtm_monitor_bigip module](bigip_gtm_monitor_bigip_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-monitor-bigip-module) – Manages F5 BIG-IP GTM BIG-IP monitors
- [bigip_gtm_monitor_external module](bigip_gtm_monitor_external_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-monitor-external-module) – Manages external GTM monitors on a BIG-IP
- [bigip_gtm_monitor_firepass module](bigip_gtm_monitor_firepass_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-monitor-firepass-module) – Manages F5 BIG-IP GTM FirePass monitors
- [bigip_gtm_monitor_http module](bigip_gtm_monitor_http_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-monitor-http-module) – Manages F5 BIG-IP GTM HTTP monitors
- [bigip_gtm_monitor_https module](bigip_gtm_monitor_https_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-monitor-https-module) – Manages F5 BIG-IP GTM HTTPS monitors
- [bigip_gtm_monitor_tcp module](bigip_gtm_monitor_tcp_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-monitor-tcp-module) – Manages F5 BIG-IP GTM TCP monitors
- [bigip_gtm_monitor_tcp_half_open module](bigip_gtm_monitor_tcp_half_open_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-monitor-tcp-half-open-module) – Manages F5 BIG-IP GTM TCP half-open monitors
- [bigip_gtm_pool module](bigip_gtm_pool_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-pool-module) – Manages F5 BIG-IP GTM pools
- [bigip_gtm_pool_member module](bigip_gtm_pool_member_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-pool-member-module) – Manage GTM pool member settings
- [bigip_gtm_server module](bigip_gtm_server_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-server-module) – Manages F5 BIG-IP GTM servers
- [bigip_gtm_topology_record module](bigip_gtm_topology_record_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-topology-record-module) – Manages GTM Topology Records
- [bigip_gtm_topology_region module](bigip_gtm_topology_region_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-topology-region-module) – Manages GTM Topology Regions
- [bigip_gtm_virtual_server module](bigip_gtm_virtual_server_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-virtual-server-module) – Manages F5 BIG-IP GTM virtual servers
- [bigip_gtm_wide_ip module](bigip_gtm_wide_ip_module.md#ansible-collections-f5networks-f5-modules-bigip-gtm-wide-ip-module) – Manages F5 BIG-IP GTM Wide IP
- [bigip_hostname module](bigip_hostname_module.md#ansible-collections-f5networks-f5-modules-bigip-hostname-module) – Manage the hostname of a BIG-IP
- [bigip_iapp_service module](bigip_iapp_service_module.md#ansible-collections-f5networks-f5-modules-bigip-iapp-service-module) – Manages TCL iApp services on a BIG-IP
- [bigip_iapp_template module](bigip_iapp_template_module.md#ansible-collections-f5networks-f5-modules-bigip-iapp-template-module) – Manages TCL iApp templates on a BIG-IP.
- [bigip_ike_peer module](bigip_ike_peer_module.md#ansible-collections-f5networks-f5-modules-bigip-ike-peer-module) – Manage IPSec IKE Peer configuration on BIG-IP
- [bigip_imish_config module](bigip_imish_config_module.md#ansible-collections-f5networks-f5-modules-bigip-imish-config-module) – Manage BIG-IP advanced routing configuration sections
- [bigip_interface module](bigip_interface_module.md#ansible-collections-f5networks-f5-modules-bigip-interface-module) – Module to manage BIG-IP physical interfaces.
- [bigip_ipsec_policy module](bigip_ipsec_policy_module.md#ansible-collections-f5networks-f5-modules-bigip-ipsec-policy-module) – Manage IPSec policies on a BIG-IP
- [bigip_irule module](bigip_irule_module.md#ansible-collections-f5networks-f5-modules-bigip-irule-module) – Manage iRules across different modules on a BIG-IP
- [bigip_log_destination module](bigip_log_destination_module.md#ansible-collections-f5networks-f5-modules-bigip-log-destination-module) – Manages log destinations on a BIG-IP.
- [bigip_log_publisher module](bigip_log_publisher_module.md#ansible-collections-f5networks-f5-modules-bigip-log-publisher-module) – Manages log publishers on a BIG-IP
- [bigip_ltm_global module](bigip_ltm_global_module.md#ansible-collections-f5networks-f5-modules-bigip-ltm-global-module) – Manages global LTM settings
- [bigip_lx_package module](bigip_lx_package_module.md#ansible-collections-f5networks-f5-modules-bigip-lx-package-module) – Manages Javascript LX packages on a BIG-IP
- [bigip_management_route module](bigip_management_route_module.md#ansible-collections-f5networks-f5-modules-bigip-management-route-module) – Manage system management routes on a BIG-IP
- [bigip_message_routing_peer module](bigip_message_routing_peer_module.md#ansible-collections-f5networks-f5-modules-bigip-message-routing-peer-module) – Manage peers for routing generic message protocol messages
- [bigip_message_routing_protocol module](bigip_message_routing_protocol_module.md#ansible-collections-f5networks-f5-modules-bigip-message-routing-protocol-module) – Manage the generic message parser profile.
- [bigip_message_routing_route module](bigip_message_routing_route_module.md#ansible-collections-f5networks-f5-modules-bigip-message-routing-route-module) – Manages static routes for routing message protocol messages
- [bigip_message_routing_router module](bigip_message_routing_router_module.md#ansible-collections-f5networks-f5-modules-bigip-message-routing-router-module) – Manages router profiles for message-routing protocols
- [bigip_message_routing_transport_config module](bigip_message_routing_transport_config_module.md#ansible-collections-f5networks-f5-modules-bigip-message-routing-transport-config-module) – Manages configuration for an outgoing connection
- [bigip_monitor_dns module](bigip_monitor_dns_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-dns-module) – Manage DNS monitors on a BIG-IP
- [bigip_monitor_external module](bigip_monitor_external_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-external-module) – Manages external LTM monitors on a BIG-IP
- [bigip_monitor_ftp module](bigip_monitor_ftp_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-ftp-module) – Manage FTP monitors on a BIG-IP
- [bigip_monitor_gateway_icmp module](bigip_monitor_gateway_icmp_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-gateway-icmp-module) – Manages F5 BIG-IP LTM gateway ICMP monitors
- [bigip_monitor_http module](bigip_monitor_http_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-http-module) – Manages F5 BIG-IP LTM HTTP monitors
- [bigip_monitor_https module](bigip_monitor_https_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-https-module) – Manages F5 BIG-IP LTM HTTPS monitors
- [bigip_monitor_icmp module](bigip_monitor_icmp_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-icmp-module) – Manages F5 BIG-IP LTM ICMP monitors
- [bigip_monitor_ldap module](bigip_monitor_ldap_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-ldap-module) – Manages BIG-IP LDAP monitors
- [bigip_monitor_mysql module](bigip_monitor_mysql_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-mysql-module) – Manages BIG-IP MySQL monitors
- [bigip_monitor_oracle module](bigip_monitor_oracle_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-oracle-module) – Manages BIG-IP Oracle monitors
- [bigip_monitor_smtp module](bigip_monitor_smtp_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-smtp-module) – Manage SMTP monitors on a BIG-IP
- [bigip_monitor_snmp_dca module](bigip_monitor_snmp_dca_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-snmp-dca-module) – Manages BIG-IP SNMP data collecting agent (DCA) monitors
- [bigip_monitor_tcp module](bigip_monitor_tcp_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-tcp-module) – Manages F5 BIG-IP LTM TCP monitors
- [bigip_monitor_tcp_echo module](bigip_monitor_tcp_echo_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-tcp-echo-module) – Manages F5 BIG-IP LTM TCP echo monitors
- [bigip_monitor_tcp_half_open module](bigip_monitor_tcp_half_open_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-tcp-half-open-module) – Manages F5 BIG-IP LTM TCP half-open monitors
- [bigip_monitor_udp module](bigip_monitor_udp_module.md#ansible-collections-f5networks-f5-modules-bigip-monitor-udp-module) – Manages F5 BIG-IP LTM UDP monitors
- [bigip_network_globals module](bigip_network_globals_module.md#ansible-collections-f5networks-f5-modules-bigip-network-globals-module) – Manage network global settings on BIG-IP
- [bigip_node module](bigip_node_module.md#ansible-collections-f5networks-f5-modules-bigip-node-module) – Manages F5 BIG-IP LTM nodes
- [bigip_partition module](bigip_partition_module.md#ansible-collections-f5networks-f5-modules-bigip-partition-module) – Manage BIG-IP partitions
- [bigip_password_policy module](bigip_password_policy_module.md#ansible-collections-f5networks-f5-modules-bigip-password-policy-module) – Manages the authentication password policy on a BIG-IP
- [bigip_policy module](bigip_policy_module.md#ansible-collections-f5networks-f5-modules-bigip-policy-module) – Manage general policy configuration on a BIG-IP
- [bigip_policy_rule module](bigip_policy_rule_module.md#ansible-collections-f5networks-f5-modules-bigip-policy-rule-module) – Manage LTM policy rules on a BIG-IP
- [bigip_pool module](bigip_pool_module.md#ansible-collections-f5networks-f5-modules-bigip-pool-module) – Manages F5 BIG-IP LTM pools
- [bigip_pool_member module](bigip_pool_member_module.md#ansible-collections-f5networks-f5-modules-bigip-pool-member-module) – Manages F5 BIG-IP LTM pool members
- [bigip_profile_analytics module](bigip_profile_analytics_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-analytics-module) – Manage HTTP analytics profiles on a BIG-IP
- [bigip_profile_client_ssl module](bigip_profile_client_ssl_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-client-ssl-module) – Manages client SSL profiles on a BIG-IP
- [bigip_profile_dns module](bigip_profile_dns_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-dns-module) – Manage DNS profiles on a BIG-IP
- [bigip_profile_fastl4 module](bigip_profile_fastl4_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-fastl4-module) – Manages Fast L4 profiles
- [bigip_profile_ftp module](bigip_profile_ftp_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-ftp-module) – Manages FTP profiles
- [bigip_profile_http module](bigip_profile_http_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-http-module) – Manage HTTP profiles on a BIG-IP
- [bigip_profile_http2 module](bigip_profile_http2_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-http2-module) – Manage HTTP2 profiles on a BIG-IP
- [bigip_profile_http_compression module](bigip_profile_http_compression_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-http-compression-module) – Manage HTTP compression profiles on a BIG-IP
- [bigip_profile_oneconnect module](bigip_profile_oneconnect_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-oneconnect-module) – Manage OneConnect profiles on a BIG-IP
- [bigip_profile_persistence_cookie module](bigip_profile_persistence_cookie_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-persistence-cookie-module) – Manage cookie persistence profiles on BIG-IP
- [bigip_profile_persistence_src_addr module](bigip_profile_persistence_src_addr_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-persistence-src-addr-module) – Manage source address persistence profiles
- [bigip_profile_persistence_universal module](bigip_profile_persistence_universal_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-persistence-universal-module) – Manage universal persistence profiles
- [bigip_profile_server_ssl module](bigip_profile_server_ssl_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-server-ssl-module) – Manages server SSL profiles on a BIG-IP
- [bigip_profile_sip module](bigip_profile_sip_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-sip-module) – Manage SIP profiles on a BIG-IP
- [bigip_profile_tcp module](bigip_profile_tcp_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-tcp-module) – Manage TCP profiles on a BIG-IP
- [bigip_profile_udp module](bigip_profile_udp_module.md#ansible-collections-f5networks-f5-modules-bigip-profile-udp-module) – Manage UDP profiles on a BIG-IP
- [bigip_provision module](bigip_provision_module.md#ansible-collections-f5networks-f5-modules-bigip-provision-module) – Manage BIG-IP module provisioning
- [bigip_qkview module](bigip_qkview_module.md#ansible-collections-f5networks-f5-modules-bigip-qkview-module) – Manage QKviews on the device
- [bigip_remote_role module](bigip_remote_role_module.md#ansible-collections-f5networks-f5-modules-bigip-remote-role-module) – Manage remote roles on a BIG-IP
- [bigip_remote_syslog module](bigip_remote_syslog_module.md#ansible-collections-f5networks-f5-modules-bigip-remote-syslog-module) – Manipulate remote syslog settings on a BIG-IP
- [bigip_remote_user module](bigip_remote_user_module.md#ansible-collections-f5networks-f5-modules-bigip-remote-user-module) – Manages default settings for remote user accounts on a BIG-IP
- [bigip_routedomain module](bigip_routedomain_module.md#ansible-collections-f5networks-f5-modules-bigip-routedomain-module) – Manage route domains on a BIG-IP
- [bigip_selfip module](bigip_selfip_module.md#ansible-collections-f5networks-f5-modules-bigip-selfip-module) – Manage Self-IPs on a BIG-IP system
- [bigip_service_policy module](bigip_service_policy_module.md#ansible-collections-f5networks-f5-modules-bigip-service-policy-module) – Manages service policies on a BIG-IP.
- [bigip_smtp module](bigip_smtp_module.md#ansible-collections-f5networks-f5-modules-bigip-smtp-module) – Manages SMTP settings on the BIG-IP
- [bigip_snat_pool module](bigip_snat_pool_module.md#ansible-collections-f5networks-f5-modules-bigip-snat-pool-module) – Manage SNAT pools on a BIG-IP
- [bigip_snat_translation module](bigip_snat_translation_module.md#ansible-collections-f5networks-f5-modules-bigip-snat-translation-module) – Manage SNAT translations on a BIG-IP
- [bigip_snmp module](bigip_snmp_module.md#ansible-collections-f5networks-f5-modules-bigip-snmp-module) – Manipulate general SNMP settings on a BIG-IP
- [bigip_snmp_community module](bigip_snmp_community_module.md#ansible-collections-f5networks-f5-modules-bigip-snmp-community-module) – Manages SNMP communities on a BIG-IP.
- [bigip_snmp_trap module](bigip_snmp_trap_module.md#ansible-collections-f5networks-f5-modules-bigip-snmp-trap-module) – Manipulate SNMP trap information on a BIG-IP
- [bigip_software_image module](bigip_software_image_module.md#ansible-collections-f5networks-f5-modules-bigip-software-image-module) – Manage software images on a BIG-IP
- [bigip_software_install module](bigip_software_install_module.md#ansible-collections-f5networks-f5-modules-bigip-software-install-module) – Install software images on a BIG-IP
- [bigip_software_update module](bigip_software_update_module.md#ansible-collections-f5networks-f5-modules-bigip-software-update-module) – Manage the software update settings of a BIG-IP
- [bigip_ssl_certificate module](bigip_ssl_certificate_module.md#ansible-collections-f5networks-f5-modules-bigip-ssl-certificate-module) – Import/Delete certificates from BIG-IP
- [bigip_ssl_csr module](bigip_ssl_csr_module.md#ansible-collections-f5networks-f5-modules-bigip-ssl-csr-module) – Create SSL CSR files on the BIG-IP
- [bigip_ssl_key module](bigip_ssl_key_module.md#ansible-collections-f5networks-f5-modules-bigip-ssl-key-module) – Import/Delete SSL keys from BIG-IP
- [bigip_ssl_key_cert module](bigip_ssl_key_cert_module.md#ansible-collections-f5networks-f5-modules-bigip-ssl-key-cert-module) – Import/Delete SSL keys and certs from BIG-IP
- [bigip_ssl_ocsp module](bigip_ssl_ocsp_module.md#ansible-collections-f5networks-f5-modules-bigip-ssl-ocsp-module) – Manage OCSP configurations on BIG-IP
- [bigip_static_route module](bigip_static_route_module.md#ansible-collections-f5networks-f5-modules-bigip-static-route-module) – Manipulate static routes on a BIG-IP
- [bigip_sys_daemon_log_tmm module](bigip_sys_daemon_log_tmm_module.md#ansible-collections-f5networks-f5-modules-bigip-sys-daemon-log-tmm-module) – Manage BIG-IP tmm daemon log settings
- [bigip_sys_db module](bigip_sys_db_module.md#ansible-collections-f5networks-f5-modules-bigip-sys-db-module) – Manage BIG-IP system database variables
- [bigip_sys_global module](bigip_sys_global_module.md#ansible-collections-f5networks-f5-modules-bigip-sys-global-module) – Manage BIG-IP global settings
- [bigip_timer_policy module](bigip_timer_policy_module.md#ansible-collections-f5networks-f5-modules-bigip-timer-policy-module) – Manage timer policies on a BIG-IP
- [bigip_traffic_selector module](bigip_traffic_selector_module.md#ansible-collections-f5networks-f5-modules-bigip-traffic-selector-module) – Manage IPSec Traffic Selectors on BIG-IP
- [bigip_trunk module](bigip_trunk_module.md#ansible-collections-f5networks-f5-modules-bigip-trunk-module) – Manage trunks on a BIG-IP
- [bigip_tunnel module](bigip_tunnel_module.md#ansible-collections-f5networks-f5-modules-bigip-tunnel-module) – Manage tunnels on a BIG-IP
- [bigip_ucs module](bigip_ucs_module.md#ansible-collections-f5networks-f5-modules-bigip-ucs-module) – Manage upload, installation, and removal of UCS files
- [bigip_ucs_fetch module](bigip_ucs_fetch_module.md#ansible-collections-f5networks-f5-modules-bigip-ucs-fetch-module) – Fetches a UCS file from remote nodes
- [bigip_user module](bigip_user_module.md#ansible-collections-f5networks-f5-modules-bigip-user-module) – Manage user accounts and user attributes on a BIG-IP
- [bigip_vcmp_guest module](bigip_vcmp_guest_module.md#ansible-collections-f5networks-f5-modules-bigip-vcmp-guest-module) – Manages vCMP guests on a BIG-IP
- [bigip_virtual_address module](bigip_virtual_address_module.md#ansible-collections-f5networks-f5-modules-bigip-virtual-address-module) – Manage LTM virtual addresses on a BIG-IP
- [bigip_virtual_server module](bigip_virtual_server_module.md#ansible-collections-f5networks-f5-modules-bigip-virtual-server-module) – Manage LTM virtual servers on a BIG-IP
- [bigip_vlan module](bigip_vlan_module.md#ansible-collections-f5networks-f5-modules-bigip-vlan-module) – Manage VLANs on a BIG-IP system
- [bigip_wait module](bigip_wait_module.md#ansible-collections-f5networks-f5-modules-bigip-wait-module) – Wait for a BIG-IP condition before continuing
- [bigiq_application_fasthttp module](bigiq_application_fasthttp_module.md#ansible-collections-f5networks-f5-modules-bigiq-application-fasthttp-module) – Manages BIG-IQ FastHTTP applications
- [bigiq_application_fastl4_tcp module](bigiq_application_fastl4_tcp_module.md#ansible-collections-f5networks-f5-modules-bigiq-application-fastl4-tcp-module) – Manages BIG-IQ FastL4 TCP applications
- [bigiq_application_fastl4_udp module](bigiq_application_fastl4_udp_module.md#ansible-collections-f5networks-f5-modules-bigiq-application-fastl4-udp-module) – Manages BIG-IQ FastL4 UDP applications
- [bigiq_application_http module](bigiq_application_http_module.md#ansible-collections-f5networks-f5-modules-bigiq-application-http-module) – Manages BIG-IQ HTTP applications
- [bigiq_application_https_offload module](bigiq_application_https_offload_module.md#ansible-collections-f5networks-f5-modules-bigiq-application-https-offload-module) – Manages BIG-IQ HTTPS offload applications
- [bigiq_application_https_waf module](bigiq_application_https_waf_module.md#ansible-collections-f5networks-f5-modules-bigiq-application-https-waf-module) – Manages BIG-IQ HTTPS WAF applications
- [bigiq_device_discovery module](bigiq_device_discovery_module.md#ansible-collections-f5networks-f5-modules-bigiq-device-discovery-module) – Manage BIG-IP devices through BIG-IQ
- [bigiq_device_info module](bigiq_device_info_module.md#ansible-collections-f5networks-f5-modules-bigiq-device-info-module) – Collect information from F5 BIG-IQ devices
- [bigiq_regkey_license module](bigiq_regkey_license_module.md#ansible-collections-f5networks-f5-modules-bigiq-regkey-license-module) – Manages licenses in a BIG-IQ registration key pool
- [bigiq_regkey_license_assignment module](bigiq_regkey_license_assignment_module.md#ansible-collections-f5networks-f5-modules-bigiq-regkey-license-assignment-module) – Manage regkey license assignment on BIG-IPs from a BIG-IQ
- [bigiq_regkey_pool module](bigiq_regkey_pool_module.md#ansible-collections-f5networks-f5-modules-bigiq-regkey-pool-module) – Manages registration key pools on BIG-IQ
- [bigiq_utility_license module](bigiq_utility_license_module.md#ansible-collections-f5networks-f5-modules-bigiq-utility-license-module) – Manage utility licenses on a BIG-IQ
- [bigiq_utility_license_assignment module](bigiq_utility_license_assignment_module.md#ansible-collections-f5networks-f5-modules-bigiq-utility-license-assignment-module) – Manage utility license assignment on BIG-IPs from a BIG-IQ

### Lookup Plugins

- [bigiq_license lookup](bigiq_license_lookup.md#ansible-collections-f5networks-f5-modules-bigiq-license-lookup) – Select a random license key from a pool of biqiq available licenses
- [license_hopper lookup](license_hopper_lookup.md#ansible-collections-f5networks-f5-modules-license-hopper-lookup) – Return random license from list

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
