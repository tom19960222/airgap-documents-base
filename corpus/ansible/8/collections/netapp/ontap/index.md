---
collection: ansible
version: "8"
title: "Netapp.Ontap"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/index.html
fetched_at: 2026-07-28T01:02:48+00:00
---
# Netapp.Ontap

Collection version 22.8.3

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

NetApp ONTAP Collection

**Author:**

- NetApp Ansible Team <[ng-ansibleteam@netapp.com](mailto:ng-ansibleteam%40netapp.com)>

**Supported ansible-core versions:**

- 2.14 or newer

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)

## [Plugin Index](index.md#id2)

These are the plugins in the netapp.ontap collection:

### Modules

- [na_ontap_active_directory module](na_ontap_active_directory_module.md#ansible-collections-netapp-ontap-na-ontap-active-directory-module) – NetApp ONTAP configure active directory
- [na_ontap_active_directory_domain_controllers module](na_ontap_active_directory_domain_controllers_module.md#ansible-collections-netapp-ontap-na-ontap-active-directory-domain-controllers-module) – NetApp ONTAP configure active directory preferred domain controllers
- [na_ontap_aggregate module](na_ontap_aggregate_module.md#ansible-collections-netapp-ontap-na-ontap-aggregate-module) – NetApp ONTAP manage aggregates.
- [na_ontap_autosupport module](na_ontap_autosupport_module.md#ansible-collections-netapp-ontap-na-ontap-autosupport-module) – NetApp ONTAP autosupport
- [na_ontap_autosupport_invoke module](na_ontap_autosupport_invoke_module.md#ansible-collections-netapp-ontap-na-ontap-autosupport-invoke-module) – NetApp ONTAP send AutoSupport message
- [na_ontap_bgp_peer_group module](na_ontap_bgp_peer_group_module.md#ansible-collections-netapp-ontap-na-ontap-bgp-peer-group-module) – NetApp ONTAP module to create, modify or delete bgp peer group.
- [na_ontap_broadcast_domain module](na_ontap_broadcast_domain_module.md#ansible-collections-netapp-ontap-na-ontap-broadcast-domain-module) – NetApp ONTAP manage broadcast domains.
- [na_ontap_broadcast_domain_ports module](na_ontap_broadcast_domain_ports_module.md#ansible-collections-netapp-ontap-na-ontap-broadcast-domain-ports-module) – NetApp ONTAP manage broadcast domain ports
- [na_ontap_cg_snapshot module](na_ontap_cg_snapshot_module.md#ansible-collections-netapp-ontap-na-ontap-cg-snapshot-module) – NetApp ONTAP manage consistency group snapshot
- [na_ontap_cifs module](na_ontap_cifs_module.md#ansible-collections-netapp-ontap-na-ontap-cifs-module) – NetApp ONTAP Manage cifs-share
- [na_ontap_cifs_acl module](na_ontap_cifs_acl_module.md#ansible-collections-netapp-ontap-na-ontap-cifs-acl-module) – NetApp ONTAP manage cifs-share-access-control
- [na_ontap_cifs_local_group module](na_ontap_cifs_local_group_module.md#ansible-collections-netapp-ontap-na-ontap-cifs-local-group-module) – NetApp Ontap - create, delete or modify CIFS local group.
- [na_ontap_cifs_local_group_member module](na_ontap_cifs_local_group_member_module.md#ansible-collections-netapp-ontap-na-ontap-cifs-local-group-member-module) – NetApp Ontap - Add or remove CIFS local group member
- [na_ontap_cifs_local_user module](na_ontap_cifs_local_user_module.md#ansible-collections-netapp-ontap-na-ontap-cifs-local-user-module) – NetApp ONTAP local CIFS user.
- [na_ontap_cifs_local_user_modify module](na_ontap_cifs_local_user_modify_module.md#ansible-collections-netapp-ontap-na-ontap-cifs-local-user-modify-module) – NetApp ONTAP modify local CIFS user.
- [na_ontap_cifs_local_user_set_password module](na_ontap_cifs_local_user_set_password_module.md#ansible-collections-netapp-ontap-na-ontap-cifs-local-user-set-password-module) – NetApp ONTAP set local CIFS user password
- [na_ontap_cifs_server module](na_ontap_cifs_server_module.md#ansible-collections-netapp-ontap-na-ontap-cifs-server-module) – NetApp ONTAP CIFS server configuration
- [na_ontap_cluster module](na_ontap_cluster_module.md#ansible-collections-netapp-ontap-na-ontap-cluster-module) – NetApp ONTAP cluster - create a cluster and add/remove nodes.
- [na_ontap_cluster_ha module](na_ontap_cluster_ha_module.md#ansible-collections-netapp-ontap-na-ontap-cluster-ha-module) – NetApp ONTAP Manage HA status for cluster
- [na_ontap_cluster_peer module](na_ontap_cluster_peer_module.md#ansible-collections-netapp-ontap-na-ontap-cluster-peer-module) – NetApp ONTAP Manage Cluster peering
- [na_ontap_command module](na_ontap_command_module.md#ansible-collections-netapp-ontap-na-ontap-command-module) – NetApp ONTAP Run any cli command, the username provided needs to have console login permission.
- [na_ontap_debug module](na_ontap_debug_module.md#ansible-collections-netapp-ontap-na-ontap-debug-module) – NetApp ONTAP Debug netapp-lib import and connection.
- [na_ontap_disk_options module](na_ontap_disk_options_module.md#ansible-collections-netapp-ontap-na-ontap-disk-options-module) – NetApp ONTAP modify storage disk options
- [na_ontap_disks module](na_ontap_disks_module.md#ansible-collections-netapp-ontap-na-ontap-disks-module) – NetApp ONTAP Assign disks to nodes
- [na_ontap_dns module](na_ontap_dns_module.md#ansible-collections-netapp-ontap-na-ontap-dns-module) – NetApp ONTAP Create, delete, modify DNS servers.
- [na_ontap_domain_tunnel module](na_ontap_domain_tunnel_module.md#ansible-collections-netapp-ontap-na-ontap-domain-tunnel-module) – NetApp ONTAP domain tunnel
- [na_ontap_efficiency_policy module](na_ontap_efficiency_policy_module.md#ansible-collections-netapp-ontap-na-ontap-efficiency-policy-module) – NetApp ONTAP manage efficiency policies (sis policies)
- [na_ontap_ems_config module](na_ontap_ems_config_module.md#ansible-collections-netapp-ontap-na-ontap-ems-config-module) – NetApp ONTAP module to modify EMS configuration.
- [na_ontap_ems_destination module](na_ontap_ems_destination_module.md#ansible-collections-netapp-ontap-na-ontap-ems-destination-module) – NetApp ONTAP configuration for EMS event destination
- [na_ontap_ems_filter module](na_ontap_ems_filter_module.md#ansible-collections-netapp-ontap-na-ontap-ems-filter-module) – NetApp ONTAP EMS Filter
- [na_ontap_export_policy module](na_ontap_export_policy_module.md#ansible-collections-netapp-ontap-na-ontap-export-policy-module) – NetApp ONTAP manage export-policy
- [na_ontap_export_policy_rule module](na_ontap_export_policy_rule_module.md#ansible-collections-netapp-ontap-na-ontap-export-policy-rule-module) – NetApp ONTAP manage export policy rules
- [na_ontap_fcp module](na_ontap_fcp_module.md#ansible-collections-netapp-ontap-na-ontap-fcp-module) – NetApp ONTAP Start, Stop and Enable FCP services.
- [na_ontap_fdsd module](na_ontap_fdsd_module.md#ansible-collections-netapp-ontap-na-ontap-fdsd-module) – NetApp ONTAP create or remove a File Directory security descriptor.
- [na_ontap_fdsp module](na_ontap_fdsp_module.md#ansible-collections-netapp-ontap-na-ontap-fdsp-module) – NetApp ONTAP create or delete a file directory security policy
- [na_ontap_fdspt module](na_ontap_fdspt_module.md#ansible-collections-netapp-ontap-na-ontap-fdspt-module) – NetApp ONTAP create, delete or modify File Directory security policy tasks
- [na_ontap_fdss module](na_ontap_fdss_module.md#ansible-collections-netapp-ontap-na-ontap-fdss-module) – NetApp ONTAP File Directory Security Set.
- [na_ontap_file_directory_policy module](na_ontap_file_directory_policy_module.md#ansible-collections-netapp-ontap-na-ontap-file-directory-policy-module) – NetApp ONTAP create, delete, or modify vserver security file-directory policy
- [na_ontap_file_security_permissions module](na_ontap_file_security_permissions_module.md#ansible-collections-netapp-ontap-na-ontap-file-security-permissions-module) – NetApp ONTAP NTFS file security permissions
- [na_ontap_file_security_permissions_acl module](na_ontap_file_security_permissions_acl_module.md#ansible-collections-netapp-ontap-na-ontap-file-security-permissions-acl-module) – NetApp ONTAP file security permissions ACL
- [na_ontap_firewall_policy module](na_ontap_firewall_policy_module.md#ansible-collections-netapp-ontap-na-ontap-firewall-policy-module) – NetApp ONTAP Manage a firewall policy
- [na_ontap_firmware_upgrade module](na_ontap_firmware_upgrade_module.md#ansible-collections-netapp-ontap-na-ontap-firmware-upgrade-module) – NetApp ONTAP firmware upgrade for SP, shelf, ACP, and disk.
- [na_ontap_flexcache module](na_ontap_flexcache_module.md#ansible-collections-netapp-ontap-na-ontap-flexcache-module) – NetApp ONTAP FlexCache - create/delete relationship
- [na_ontap_fpolicy_event module](na_ontap_fpolicy_event_module.md#ansible-collections-netapp-ontap-na-ontap-fpolicy-event-module) – NetApp ONTAP FPolicy policy event configuration
- [na_ontap_fpolicy_ext_engine module](na_ontap_fpolicy_ext_engine_module.md#ansible-collections-netapp-ontap-na-ontap-fpolicy-ext-engine-module) – NetApp ONTAP fPolicy external engine configuration.
- [na_ontap_fpolicy_policy module](na_ontap_fpolicy_policy_module.md#ansible-collections-netapp-ontap-na-ontap-fpolicy-policy-module) – NetApp ONTAP - Create, delete or modify an FPolicy policy.
- [na_ontap_fpolicy_scope module](na_ontap_fpolicy_scope_module.md#ansible-collections-netapp-ontap-na-ontap-fpolicy-scope-module) – NetApp ONTAP - Create, delete or modify an FPolicy policy scope configuration.
- [na_ontap_fpolicy_status module](na_ontap_fpolicy_status_module.md#ansible-collections-netapp-ontap-na-ontap-fpolicy-status-module) – NetApp ONTAP - Enables or disables the specified fPolicy policy
- [na_ontap_igroup module](na_ontap_igroup_module.md#ansible-collections-netapp-ontap-na-ontap-igroup-module) – NetApp ONTAP iSCSI or FC igroup configuration
- [na_ontap_igroup_initiator module](na_ontap_igroup_initiator_module.md#ansible-collections-netapp-ontap-na-ontap-igroup-initiator-module) – NetApp ONTAP igroup initiator configuration
- [na_ontap_info module](na_ontap_info_module.md#ansible-collections-netapp-ontap-na-ontap-info-module) – NetApp information gatherer
- [na_ontap_interface module](na_ontap_interface_module.md#ansible-collections-netapp-ontap-na-ontap-interface-module) – NetApp ONTAP LIF configuration
- [na_ontap_ipspace module](na_ontap_ipspace_module.md#ansible-collections-netapp-ontap-na-ontap-ipspace-module) – NetApp ONTAP Manage an ipspace
- [na_ontap_iscsi module](na_ontap_iscsi_module.md#ansible-collections-netapp-ontap-na-ontap-iscsi-module) – NetApp ONTAP manage iSCSI service
- [na_ontap_iscsi_security module](na_ontap_iscsi_security_module.md#ansible-collections-netapp-ontap-na-ontap-iscsi-security-module) – NetApp ONTAP Manage iscsi security.
- [na_ontap_job_schedule module](na_ontap_job_schedule_module.md#ansible-collections-netapp-ontap-na-ontap-job-schedule-module) – NetApp ONTAP Job Schedule
- [na_ontap_kerberos_interface module](na_ontap_kerberos_interface_module.md#ansible-collections-netapp-ontap-na-ontap-kerberos-interface-module) – NetApp ONTAP module to modify kerberos interface.
- [na_ontap_kerberos_realm module](na_ontap_kerberos_realm_module.md#ansible-collections-netapp-ontap-na-ontap-kerberos-realm-module) – NetApp ONTAP vserver nfs kerberos realm
- [na_ontap_ldap module](na_ontap_ldap_module.md#ansible-collections-netapp-ontap-na-ontap-ldap-module) – NetApp ONTAP LDAP
- [na_ontap_ldap_client module](na_ontap_ldap_client_module.md#ansible-collections-netapp-ontap-na-ontap-ldap-client-module) – NetApp ONTAP LDAP client
- [na_ontap_license module](na_ontap_license_module.md#ansible-collections-netapp-ontap-na-ontap-license-module) – NetApp ONTAP protocol and feature license packages
- [na_ontap_local_hosts module](na_ontap_local_hosts_module.md#ansible-collections-netapp-ontap-na-ontap-local-hosts-module) – NetApp ONTAP local hosts
- [na_ontap_log_forward module](na_ontap_log_forward_module.md#ansible-collections-netapp-ontap-na-ontap-log-forward-module) – NetApp ONTAP Log Forward Configuration
- [na_ontap_login_messages module](na_ontap_login_messages_module.md#ansible-collections-netapp-ontap-na-ontap-login-messages-module) – Setup login banner and message of the day
- [na_ontap_lun module](na_ontap_lun_module.md#ansible-collections-netapp-ontap-na-ontap-lun-module) – NetApp ONTAP manage LUNs
- [na_ontap_lun_copy module](na_ontap_lun_copy_module.md#ansible-collections-netapp-ontap-na-ontap-lun-copy-module) – NetApp ONTAP copy LUNs
- [na_ontap_lun_map module](na_ontap_lun_map_module.md#ansible-collections-netapp-ontap-na-ontap-lun-map-module) – NetApp ONTAP LUN maps
- [na_ontap_lun_map_reporting_nodes module](na_ontap_lun_map_reporting_nodes_module.md#ansible-collections-netapp-ontap-na-ontap-lun-map-reporting-nodes-module) – NetApp ONTAP LUN maps reporting nodes
- [na_ontap_mcc_mediator module](na_ontap_mcc_mediator_module.md#ansible-collections-netapp-ontap-na-ontap-mcc-mediator-module) – NetApp ONTAP Add and Remove MetroCluster Mediator
- [na_ontap_metrocluster module](na_ontap_metrocluster_module.md#ansible-collections-netapp-ontap-na-ontap-metrocluster-module) – NetApp ONTAP set up a MetroCluster
- [na_ontap_metrocluster_dr_group module](na_ontap_metrocluster_dr_group_module.md#ansible-collections-netapp-ontap-na-ontap-metrocluster-dr-group-module) – NetApp ONTAP manage MetroCluster DR Group
- [na_ontap_motd module](na_ontap_motd_module.md#ansible-collections-netapp-ontap-na-ontap-motd-module) – Setup motd
- [na_ontap_name_mappings module](na_ontap_name_mappings_module.md#ansible-collections-netapp-ontap-na-ontap-name-mappings-module) – NetApp ONTAP name mappings
- [na_ontap_name_service_switch module](na_ontap_name_service_switch_module.md#ansible-collections-netapp-ontap-na-ontap-name-service-switch-module) – NetApp ONTAP Manage name service switch
- [na_ontap_ndmp module](na_ontap_ndmp_module.md#ansible-collections-netapp-ontap-na-ontap-ndmp-module) – NetApp ONTAP NDMP services configuration
- [na_ontap_net_ifgrp module](na_ontap_net_ifgrp_module.md#ansible-collections-netapp-ontap-na-ontap-net-ifgrp-module) – NetApp Ontap modify network interface group
- [na_ontap_net_port module](na_ontap_net_port_module.md#ansible-collections-netapp-ontap-na-ontap-net-port-module) – NetApp ONTAP network ports.
- [na_ontap_net_routes module](na_ontap_net_routes_module.md#ansible-collections-netapp-ontap-na-ontap-net-routes-module) – NetApp ONTAP network routes
- [na_ontap_net_subnet module](na_ontap_net_subnet_module.md#ansible-collections-netapp-ontap-na-ontap-net-subnet-module) – NetApp ONTAP Create, delete, modify network subnets.
- [na_ontap_net_vlan module](na_ontap_net_vlan_module.md#ansible-collections-netapp-ontap-na-ontap-net-vlan-module) – NetApp ONTAP network VLAN
- [na_ontap_nfs module](na_ontap_nfs_module.md#ansible-collections-netapp-ontap-na-ontap-nfs-module) – NetApp ONTAP NFS status
- [na_ontap_node module](na_ontap_node_module.md#ansible-collections-netapp-ontap-na-ontap-node-module) – NetApp ONTAP Modify or Rename a node.
- [na_ontap_ntfs_dacl module](na_ontap_ntfs_dacl_module.md#ansible-collections-netapp-ontap-na-ontap-ntfs-dacl-module) – NetApp Ontap create, delate or modify NTFS DACL (discretionary access control list)
- [na_ontap_ntfs_sd module](na_ontap_ntfs_sd_module.md#ansible-collections-netapp-ontap-na-ontap-ntfs-sd-module) – NetApp ONTAP create, delete or modify NTFS security descriptor
- [na_ontap_ntp module](na_ontap_ntp_module.md#ansible-collections-netapp-ontap-na-ontap-ntp-module) – NetApp ONTAP NTP server
- [na_ontap_ntp_key module](na_ontap_ntp_key_module.md#ansible-collections-netapp-ontap-na-ontap-ntp-key-module) – NetApp ONTAP NTP key
- [na_ontap_nvme module](na_ontap_nvme_module.md#ansible-collections-netapp-ontap-na-ontap-nvme-module) – NetApp ONTAP Manage NVMe Service
- [na_ontap_nvme_namespace module](na_ontap_nvme_namespace_module.md#ansible-collections-netapp-ontap-na-ontap-nvme-namespace-module) – NetApp ONTAP Manage NVME Namespace
- [na_ontap_nvme_subsystem module](na_ontap_nvme_subsystem_module.md#ansible-collections-netapp-ontap-na-ontap-nvme-subsystem-module) – NetApp ONTAP Manage NVME Subsystem
- [na_ontap_object_store module](na_ontap_object_store_module.md#ansible-collections-netapp-ontap-na-ontap-object-store-module) – NetApp ONTAP manage object store config.
- [na_ontap_partitions module](na_ontap_partitions_module.md#ansible-collections-netapp-ontap-na-ontap-partitions-module) – NetApp ONTAP Assign partitions and disks to nodes.
- [na_ontap_ports module](na_ontap_ports_module.md#ansible-collections-netapp-ontap-na-ontap-ports-module) – NetApp ONTAP add/remove ports
- [na_ontap_portset module](na_ontap_portset_module.md#ansible-collections-netapp-ontap-na-ontap-portset-module) – NetApp ONTAP Create/Delete portset
- [na_ontap_publickey module](na_ontap_publickey_module.md#ansible-collections-netapp-ontap-na-ontap-publickey-module) – NetApp ONTAP publickey configuration
- [na_ontap_qos_adaptive_policy_group module](na_ontap_qos_adaptive_policy_group_module.md#ansible-collections-netapp-ontap-na-ontap-qos-adaptive-policy-group-module) – NetApp ONTAP Adaptive Quality of Service policy group.
- [na_ontap_qos_policy_group module](na_ontap_qos_policy_group_module.md#ansible-collections-netapp-ontap-na-ontap-qos-policy-group-module) – NetApp ONTAP manage policy group in Quality of Service.
- [na_ontap_qtree module](na_ontap_qtree_module.md#ansible-collections-netapp-ontap-na-ontap-qtree-module) – NetApp ONTAP manage qtrees
- [na_ontap_quota_policy module](na_ontap_quota_policy_module.md#ansible-collections-netapp-ontap-na-ontap-quota-policy-module) – NetApp Ontap create, assign, rename or delete quota policy
- [na_ontap_quotas module](na_ontap_quotas_module.md#ansible-collections-netapp-ontap-na-ontap-quotas-module) – NetApp ONTAP Quotas
- [na_ontap_rest_cli module](na_ontap_rest_cli_module.md#ansible-collections-netapp-ontap-na-ontap-rest-cli-module) – NetApp ONTAP run any CLI command using REST api/private/cli/
- [na_ontap_rest_info module](na_ontap_rest_info_module.md#ansible-collections-netapp-ontap-na-ontap-rest-info-module) – NetApp ONTAP information gatherer using REST APIs
- [na_ontap_restit module](na_ontap_restit_module.md#ansible-collections-netapp-ontap-na-ontap-restit-module) – NetApp ONTAP Run any REST API on ONTAP
- [na_ontap_s3_buckets module](na_ontap_s3_buckets_module.md#ansible-collections-netapp-ontap-na-ontap-s3-buckets-module) – NetApp ONTAP S3 Buckets
- [na_ontap_s3_groups module](na_ontap_s3_groups_module.md#ansible-collections-netapp-ontap-na-ontap-s3-groups-module) – NetApp ONTAP S3 groups
- [na_ontap_s3_policies module](na_ontap_s3_policies_module.md#ansible-collections-netapp-ontap-na-ontap-s3-policies-module) – NetApp ONTAP S3 Policies
- [na_ontap_s3_services module](na_ontap_s3_services_module.md#ansible-collections-netapp-ontap-na-ontap-s3-services-module) – NetApp ONTAP S3 services
- [na_ontap_s3_users module](na_ontap_s3_users_module.md#ansible-collections-netapp-ontap-na-ontap-s3-users-module) – NetApp ONTAP S3 users
- [na_ontap_security_certificates module](na_ontap_security_certificates_module.md#ansible-collections-netapp-ontap-na-ontap-security-certificates-module) – NetApp ONTAP manage security certificates.
- [na_ontap_security_config module](na_ontap_security_config_module.md#ansible-collections-netapp-ontap-na-ontap-security-config-module) – NetApp ONTAP modify security config for SSL.
- [na_ontap_security_ipsec_ca_certificate module](na_ontap_security_ipsec_ca_certificate_module.md#ansible-collections-netapp-ontap-na-ontap-security-ipsec-ca-certificate-module) – NetApp ONTAP module to add or delete ipsec ca certificate.
- [na_ontap_security_ipsec_config module](na_ontap_security_ipsec_config_module.md#ansible-collections-netapp-ontap-na-ontap-security-ipsec-config-module) – NetApp ONTAP module to configure IPsec config.
- [na_ontap_security_ipsec_policy module](na_ontap_security_ipsec_policy_module.md#ansible-collections-netapp-ontap-na-ontap-security-ipsec-policy-module) – NetApp ONTAP module to create, modify or delete security IPsec policy.
- [na_ontap_security_key_manager module](na_ontap_security_key_manager_module.md#ansible-collections-netapp-ontap-na-ontap-security-key-manager-module) – NetApp ONTAP security key manager.
- [na_ontap_security_ssh module](na_ontap_security_ssh_module.md#ansible-collections-netapp-ontap-na-ontap-security-ssh-module) – NetApp ONTAP security ssh
- [na_ontap_service_policy module](na_ontap_service_policy_module.md#ansible-collections-netapp-ontap-na-ontap-service-policy-module) – NetApp ONTAP service policy configuration
- [na_ontap_service_processor_network module](na_ontap_service_processor_network_module.md#ansible-collections-netapp-ontap-na-ontap-service-processor-network-module) – NetApp ONTAP service processor network
- [na_ontap_snaplock_clock module](na_ontap_snaplock_clock_module.md#ansible-collections-netapp-ontap-na-ontap-snaplock-clock-module) – NetApp ONTAP Sets the snaplock compliance clock.
- [na_ontap_snapmirror module](na_ontap_snapmirror_module.md#ansible-collections-netapp-ontap-na-ontap-snapmirror-module) – NetApp ONTAP or ElementSW Manage SnapMirror
- [na_ontap_snapmirror_policy module](na_ontap_snapmirror_policy_module.md#ansible-collections-netapp-ontap-na-ontap-snapmirror-policy-module) – NetApp ONTAP create, delete or modify SnapMirror policies
- [na_ontap_snapshot module](na_ontap_snapshot_module.md#ansible-collections-netapp-ontap-na-ontap-snapshot-module) – NetApp ONTAP manage Snapshots
- [na_ontap_snapshot_policy module](na_ontap_snapshot_policy_module.md#ansible-collections-netapp-ontap-na-ontap-snapshot-policy-module) – NetApp ONTAP manage Snapshot Policy
- [na_ontap_snmp module](na_ontap_snmp_module.md#ansible-collections-netapp-ontap-na-ontap-snmp-module) – NetApp ONTAP SNMP user
- [na_ontap_snmp_traphosts module](na_ontap_snmp_traphosts_module.md#ansible-collections-netapp-ontap-na-ontap-snmp-traphosts-module) – NetApp ONTAP SNMP traphosts.
- [na_ontap_software_update module](na_ontap_software_update_module.md#ansible-collections-netapp-ontap-na-ontap-software-update-module) – NetApp ONTAP Update Software
- [na_ontap_ssh_command module](na_ontap_ssh_command_module.md#ansible-collections-netapp-ontap-na-ontap-ssh-command-module) – NetApp ONTAP Run any cli command over plain SSH using paramiko.
- [na_ontap_storage_auto_giveback module](na_ontap_storage_auto_giveback_module.md#ansible-collections-netapp-ontap-na-ontap-storage-auto-giveback-module) – Enables or disables NetApp ONTAP storage auto giveback for a specified node
- [na_ontap_storage_failover module](na_ontap_storage_failover_module.md#ansible-collections-netapp-ontap-na-ontap-storage-failover-module) – Enables or disables NetApp Ontap storage failover for a specified node
- [na_ontap_svm module](na_ontap_svm_module.md#ansible-collections-netapp-ontap-na-ontap-svm-module) – NetApp ONTAP SVM
- [na_ontap_svm_options module](na_ontap_svm_options_module.md#ansible-collections-netapp-ontap-na-ontap-svm-options-module) – NetApp ONTAP Modify SVM Options
- [na_ontap_ucadapter module](na_ontap_ucadapter_module.md#ansible-collections-netapp-ontap-na-ontap-ucadapter-module) – NetApp ONTAP UC adapter configuration
- [na_ontap_unix_group module](na_ontap_unix_group_module.md#ansible-collections-netapp-ontap-na-ontap-unix-group-module) – NetApp ONTAP UNIX Group
- [na_ontap_unix_user module](na_ontap_unix_user_module.md#ansible-collections-netapp-ontap-na-ontap-unix-user-module) – NetApp ONTAP UNIX users
- [na_ontap_user module](na_ontap_user_module.md#ansible-collections-netapp-ontap-na-ontap-user-module) – NetApp ONTAP user configuration and management
- [na_ontap_user_role module](na_ontap_user_role_module.md#ansible-collections-netapp-ontap-na-ontap-user-role-module) – NetApp ONTAP user role configuration and management
- [na_ontap_volume module](na_ontap_volume_module.md#ansible-collections-netapp-ontap-na-ontap-volume-module) – NetApp ONTAP manage volumes.
- [na_ontap_volume_autosize module](na_ontap_volume_autosize_module.md#ansible-collections-netapp-ontap-na-ontap-volume-autosize-module) – NetApp ONTAP manage volume autosize
- [na_ontap_volume_clone module](na_ontap_volume_clone_module.md#ansible-collections-netapp-ontap-na-ontap-volume-clone-module) – NetApp ONTAP manage volume clones.
- [na_ontap_volume_efficiency module](na_ontap_volume_efficiency_module.md#ansible-collections-netapp-ontap-na-ontap-volume-efficiency-module) – NetApp ONTAP enables, disables or modifies volume efficiency
- [na_ontap_volume_snaplock module](na_ontap_volume_snaplock_module.md#ansible-collections-netapp-ontap-na-ontap-volume-snaplock-module) – NetApp ONTAP manage volume snaplock retention.
- [na_ontap_vscan module](na_ontap_vscan_module.md#ansible-collections-netapp-ontap-na-ontap-vscan-module) – NetApp ONTAP Vscan enable/disable.
- [na_ontap_vscan_on_access_policy module](na_ontap_vscan_on_access_policy_module.md#ansible-collections-netapp-ontap-na-ontap-vscan-on-access-policy-module) – NetApp ONTAP Vscan on access policy configuration.
- [na_ontap_vscan_on_demand_task module](na_ontap_vscan_on_demand_task_module.md#ansible-collections-netapp-ontap-na-ontap-vscan-on-demand-task-module) – NetApp ONTAP Vscan on demand task configuration.
- [na_ontap_vscan_scanner_pool module](na_ontap_vscan_scanner_pool_module.md#ansible-collections-netapp-ontap-na-ontap-vscan-scanner-pool-module) – NetApp ONTAP Vscan Scanner Pools Configuration.
- [na_ontap_vserver_audit module](na_ontap_vserver_audit_module.md#ansible-collections-netapp-ontap-na-ontap-vserver-audit-module) – NetApp Ontap - create, delete or modify vserver audit configuration.
- [na_ontap_vserver_cifs_security module](na_ontap_vserver_cifs_security_module.md#ansible-collections-netapp-ontap-na-ontap-vserver-cifs-security-module) – NetApp ONTAP vserver CIFS security modification
- [na_ontap_vserver_peer module](na_ontap_vserver_peer_module.md#ansible-collections-netapp-ontap-na-ontap-vserver-peer-module) – NetApp ONTAP Vserver peering
- [na_ontap_vserver_peer_permissions module](na_ontap_vserver_peer_permissions_module.md#ansible-collections-netapp-ontap-na-ontap-vserver-peer-permissions-module) – NetApp Ontap - create, delete or modify vserver peer permission.
- [na_ontap_wait_for_condition module](na_ontap_wait_for_condition_module.md#ansible-collections-netapp-ontap-na-ontap-wait-for-condition-module) – NetApp ONTAP wait_for_condition. Loop over a get status request until a condition is met.
- [na_ontap_wwpn_alias module](na_ontap_wwpn_alias_module.md#ansible-collections-netapp-ontap-na-ontap-wwpn-alias-module) – NetApp ONTAP set FCP WWPN Alias
- [na_ontap_zapit module](na_ontap_zapit_module.md#ansible-collections-netapp-ontap-na-ontap-zapit-module) – NetApp ONTAP Run any ZAPI on ONTAP

### Filter Plugins

- [iso8601_duration_from_seconds filter](iso8601_duration_from_seconds_filter.md#ansible-collections-netapp-ontap-iso8601-duration-from-seconds-filter) – Encode seconds as a ISO 8601 duration string
- [iso8601_duration_to_seconds filter](iso8601_duration_to_seconds_filter.md#ansible-collections-netapp-ontap-iso8601-duration-to-seconds-filter) – Decode a ISO 8601 duration string as seconds

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
