---
collection: ansible
version: "8"
title: "Check_Point.Mgmt"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/index.html
fetched_at: 2026-07-28T01:01:54+00:00
---
# Check_Point.Mgmt

Collection version 5.1.1

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Check Point collection for the Management Server

**Authors:**

- Or Soffer <[orso@checkpoint.com](mailto:orso%40checkpoint.com)>
- Shiran Golzar <[shirango@checkpoint.com](mailto:shirango%40checkpoint.com)>
- Eden Brillant <[edenbr@checkpoint.com](mailto:edenbr%40checkpoint.com)>

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)

## [Plugin Index](index.md#id2)

These are the plugins in the check_point.mgmt collection:

### Modules

- [cp_mgmt_abort_get_interfaces module](cp_mgmt_abort_get_interfaces_module.md#ansible-collections-check-point-mgmt-cp-mgmt-abort-get-interfaces-module) – Attempt to abort an on-going “get-interfaces” operation.
- [cp_mgmt_access_layer module](cp_mgmt_access_layer_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-layer-module) – Manages access-layer objects on Check Point over Web Services API
- [cp_mgmt_access_layer_facts module](cp_mgmt_access_layer_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-layer-facts-module) – Get access-layer objects facts on Check Point over Web Services API
- [cp_mgmt_access_layers module](cp_mgmt_access_layers_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-layers-module) – Manages ACCESS LAYERS resource module
- [cp_mgmt_access_point_name module](cp_mgmt_access_point_name_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-point-name-module) – Manages access-point-name objects on Checkpoint over Web Services API
- [cp_mgmt_access_point_name_facts module](cp_mgmt_access_point_name_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-point-name-facts-module) – Get access-point-name objects facts on Checkpoint over Web Services API
- [cp_mgmt_access_role module](cp_mgmt_access_role_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-role-module) – Manages access-role objects on Check Point over Web Services API
- [cp_mgmt_access_role_facts module](cp_mgmt_access_role_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-role-facts-module) – Get access-role objects facts on Check Point over Web Services API
- [cp_mgmt_access_rule module](cp_mgmt_access_rule_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-rule-module) – Manages access-rule objects on Check Point over Web Services API
- [cp_mgmt_access_rule_facts module](cp_mgmt_access_rule_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-rule-facts-module) – Get access-rule objects facts on Check Point over Web Services API
- [cp_mgmt_access_rules module](cp_mgmt_access_rules_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-rules-module) – Manages access-rules objects on Check Point over Web Services API
- [cp_mgmt_access_section module](cp_mgmt_access_section_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-section-module) – Manages access-section objects on Checkpoint over Web Services API
- [cp_mgmt_add_api_key module](cp_mgmt_add_api_key_module.md#ansible-collections-check-point-mgmt-cp-mgmt-add-api-key-module) – Add API key for administrator, to enable login with it. For the key to be valid publish is needed.
- [cp_mgmt_add_data_center_object module](cp_mgmt_add_data_center_object_module.md#ansible-collections-check-point-mgmt-cp-mgmt-add-data-center-object-module) – Imports a Data Center Object from a Data Center Server.<br> Data Center Object represents an object in the cloud environment.
- [cp_mgmt_add_domain module](cp_mgmt_add_domain_module.md#ansible-collections-check-point-mgmt-cp-mgmt-add-domain-module) – Create new object
- [cp_mgmt_add_nat_rule module](cp_mgmt_add_nat_rule_module.md#ansible-collections-check-point-mgmt-cp-mgmt-add-nat-rule-module) – Create new object.
- [cp_mgmt_add_repository_package module](cp_mgmt_add_repository_package_module.md#ansible-collections-check-point-mgmt-cp-mgmt-add-repository-package-module) – Add the software package to the central repository.
- [cp_mgmt_add_rules_batch module](cp_mgmt_add_rules_batch_module.md#ansible-collections-check-point-mgmt-cp-mgmt-add-rules-batch-module) – Creates new rules in batch. Use this API to achieve optimum performance when adding more than one rule.
- [cp_mgmt_add_updatable_object module](cp_mgmt_add_updatable_object_module.md#ansible-collections-check-point-mgmt-cp-mgmt-add-updatable-object-module) – Import an updatable object from the repository to the management server.
- [cp_mgmt_address_range module](cp_mgmt_address_range_module.md#ansible-collections-check-point-mgmt-cp-mgmt-address-range-module) – Manages address-range objects on Check Point over Web Services API
- [cp_mgmt_address_range_facts module](cp_mgmt_address_range_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-address-range-facts-module) – Get address-range objects facts on Check Point over Web Services API
- [cp_mgmt_administrator module](cp_mgmt_administrator_module.md#ansible-collections-check-point-mgmt-cp-mgmt-administrator-module) – Manages administrator objects on Checkpoint over Web Services API
- [cp_mgmt_administrator_facts module](cp_mgmt_administrator_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-administrator-facts-module) – Get administrator objects facts on Checkpoint over Web Services API
- [cp_mgmt_application_site module](cp_mgmt_application_site_module.md#ansible-collections-check-point-mgmt-cp-mgmt-application-site-module) – Manages application-site objects on Check Point over Web Services API
- [cp_mgmt_application_site_category module](cp_mgmt_application_site_category_module.md#ansible-collections-check-point-mgmt-cp-mgmt-application-site-category-module) – Manages application-site-category objects on Check Point over Web Services API
- [cp_mgmt_application_site_category_facts module](cp_mgmt_application_site_category_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-application-site-category-facts-module) – Get application-site-category objects facts on Check Point over Web Services API
- [cp_mgmt_application_site_facts module](cp_mgmt_application_site_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-application-site-facts-module) – Get application-site objects facts on Check Point over Web Services API
- [cp_mgmt_application_site_group module](cp_mgmt_application_site_group_module.md#ansible-collections-check-point-mgmt-cp-mgmt-application-site-group-module) – Manages application-site-group objects on Check Point over Web Services API
- [cp_mgmt_application_site_group_facts module](cp_mgmt_application_site_group_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-application-site-group-facts-module) – Get application-site-group objects facts on Check Point over Web Services API
- [cp_mgmt_approve_session module](cp_mgmt_approve_session_module.md#ansible-collections-check-point-mgmt-cp-mgmt-approve-session-module) – Workflow feature - Approve and Publish the session.
- [cp_mgmt_assign_global_assignment module](cp_mgmt_assign_global_assignment_module.md#ansible-collections-check-point-mgmt-cp-mgmt-assign-global-assignment-module) – assign global assignment on Check Point over Web Services API
- [cp_mgmt_check_network_feed module](cp_mgmt_check_network_feed_module.md#ansible-collections-check-point-mgmt-cp-mgmt-check-network-feed-module) – Check if a target can reach or parse a network feed; can work with an existing feed object or with a new one (by providing all relevant feed parameters).
- [cp_mgmt_check_threat_ioc_feed module](cp_mgmt_check_threat_ioc_feed_module.md#ansible-collections-check-point-mgmt-cp-mgmt-check-threat-ioc-feed-module) – Check if a target can reach or parse a threat IOC feed; can work with an existing feed object or with a new one (by providing all relevant feed parameters).
- [cp_mgmt_checkpoint_host module](cp_mgmt_checkpoint_host_module.md#ansible-collections-check-point-mgmt-cp-mgmt-checkpoint-host-module) – Manages checkpoint-host objects on Checkpoint over Web Services API
- [cp_mgmt_checkpoint_host_facts module](cp_mgmt_checkpoint_host_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-checkpoint-host-facts-module) – Get checkpoint-host objects facts on Checkpoint over Web Services API
- [cp_mgmt_cluster_members_facts module](cp_mgmt_cluster_members_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-cluster-members-facts-module) – Retrieve all existing cluster members in domain.
- [cp_mgmt_connect_cloud_services module](cp_mgmt_connect_cloud_services_module.md#ansible-collections-check-point-mgmt-cp-mgmt-connect-cloud-services-module) – Securely connect the Management Server to Check Point’s Infinity Portal. <br>This is a preliminary operation so that the management server can use various Check Point cloud-based security services hosted in the Infinity Portal.
- [cp_mgmt_data_center_object_facts module](cp_mgmt_data_center_object_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-data-center-object-facts-module) – Get data-center-object objects facts on Checkpoint over Web Services API
- [cp_mgmt_delete_api_key module](cp_mgmt_delete_api_key_module.md#ansible-collections-check-point-mgmt-cp-mgmt-delete-api-key-module) – Delete the API key. For the key to be invalid publish is needed.
- [cp_mgmt_delete_data_center_object module](cp_mgmt_delete_data_center_object_module.md#ansible-collections-check-point-mgmt-cp-mgmt-delete-data-center-object-module) – Delete existing object using object name or uid.
- [cp_mgmt_delete_domain module](cp_mgmt_delete_domain_module.md#ansible-collections-check-point-mgmt-cp-mgmt-delete-domain-module) – Delete existing object using object name or uid.
- [cp_mgmt_delete_nat_rule module](cp_mgmt_delete_nat_rule_module.md#ansible-collections-check-point-mgmt-cp-mgmt-delete-nat-rule-module) – Delete existing object using object name or uid.
- [cp_mgmt_delete_repository_package module](cp_mgmt_delete_repository_package_module.md#ansible-collections-check-point-mgmt-cp-mgmt-delete-repository-package-module) – Delete the repository software package from the central repository.
- [cp_mgmt_delete_rules_batch module](cp_mgmt_delete_rules_batch_module.md#ansible-collections-check-point-mgmt-cp-mgmt-delete-rules-batch-module) – Delete rules in batch from the same layer. Use this API to achieve optimum performance when removing more than one rule.
- [cp_mgmt_delete_updatable_object module](cp_mgmt_delete_updatable_object_module.md#ansible-collections-check-point-mgmt-cp-mgmt-delete-updatable-object-module) – Delete existing object using object name or uid.
- [cp_mgmt_discard module](cp_mgmt_discard_module.md#ansible-collections-check-point-mgmt-cp-mgmt-discard-module) – All changes done by user are discarded and removed from database.
- [cp_mgmt_disconnect_cloud_services module](cp_mgmt_disconnect_cloud_services_module.md#ansible-collections-check-point-mgmt-cp-mgmt-disconnect-cloud-services-module) – Disconnect the Management Server from Check Point’s Infinity Portal.
- [cp_mgmt_dns_domain module](cp_mgmt_dns_domain_module.md#ansible-collections-check-point-mgmt-cp-mgmt-dns-domain-module) – Manages dns-domain objects on Check Point over Web Services API
- [cp_mgmt_dns_domain_facts module](cp_mgmt_dns_domain_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-dns-domain-facts-module) – Get dns-domain objects facts on Check Point over Web Services API
- [cp_mgmt_domain_facts module](cp_mgmt_domain_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-domain-facts-module) – Get domain objects facts on Checkpoint over Web Services API
- [cp_mgmt_domain_permissions_profile module](cp_mgmt_domain_permissions_profile_module.md#ansible-collections-check-point-mgmt-cp-mgmt-domain-permissions-profile-module) – Manages domain-permissions-profile objects on Checkpoint over Web Services API
- [cp_mgmt_domain_permissions_profile_facts module](cp_mgmt_domain_permissions_profile_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-domain-permissions-profile-facts-module) – Get domain-permissions-profile objects facts on Checkpoint over Web Services API
- [cp_mgmt_dynamic_global_network_object module](cp_mgmt_dynamic_global_network_object_module.md#ansible-collections-check-point-mgmt-cp-mgmt-dynamic-global-network-object-module) – Manages dynamic-global-network-object objects on Checkpoint over Web Services API
- [cp_mgmt_dynamic_global_network_object_facts module](cp_mgmt_dynamic_global_network_object_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-dynamic-global-network-object-facts-module) – Get dynamic-global-network-object objects facts on Checkpoint over Web Services API
- [cp_mgmt_dynamic_object module](cp_mgmt_dynamic_object_module.md#ansible-collections-check-point-mgmt-cp-mgmt-dynamic-object-module) – Manages dynamic-object objects on Check Point over Web Services API
- [cp_mgmt_dynamic_object_facts module](cp_mgmt_dynamic_object_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-dynamic-object-facts-module) – Get dynamic-object objects facts on Check Point over Web Services API
- [cp_mgmt_exception_group module](cp_mgmt_exception_group_module.md#ansible-collections-check-point-mgmt-cp-mgmt-exception-group-module) – Manages exception-group objects on Check Point over Web Services API
- [cp_mgmt_exception_group_facts module](cp_mgmt_exception_group_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-exception-group-facts-module) – Get exception-group objects facts on Check Point over Web Services API
- [cp_mgmt_export_management module](cp_mgmt_export_management_module.md#ansible-collections-check-point-mgmt-cp-mgmt-export-management-module) – Export the primary Security Management Server database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point configuration.
- [cp_mgmt_export_smart_task module](cp_mgmt_export_smart_task_module.md#ansible-collections-check-point-mgmt-cp-mgmt-export-smart-task-module) – Export SmartTask to a file.
- [cp_mgmt_get_attachment module](cp_mgmt_get_attachment_module.md#ansible-collections-check-point-mgmt-cp-mgmt-get-attachment-module) – Retrieves a packet capture or blob data, according to the attributes of a log record.
- [cp_mgmt_get_interfaces module](cp_mgmt_get_interfaces_module.md#ansible-collections-check-point-mgmt-cp-mgmt-get-interfaces-module) –
- [cp_mgmt_get_platform module](cp_mgmt_get_platform_module.md#ansible-collections-check-point-mgmt-cp-mgmt-get-platform-module) – Get actual platform (Hardware, Version, OS) from gateway, cluster or Check Point host.
- [cp_mgmt_global_assignment module](cp_mgmt_global_assignment_module.md#ansible-collections-check-point-mgmt-cp-mgmt-global-assignment-module) – Manages global-assignment objects on Check Point over Web Services API
- [cp_mgmt_global_assignment_facts module](cp_mgmt_global_assignment_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-global-assignment-facts-module) – Get global-assignment objects facts on Check Point over Web Services API
- [cp_mgmt_group module](cp_mgmt_group_module.md#ansible-collections-check-point-mgmt-cp-mgmt-group-module) – Manages group objects on Check Point over Web Services API
- [cp_mgmt_group_facts module](cp_mgmt_group_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-group-facts-module) – Get group objects facts on Check Point over Web Services API
- [cp_mgmt_group_with_exclusion module](cp_mgmt_group_with_exclusion_module.md#ansible-collections-check-point-mgmt-cp-mgmt-group-with-exclusion-module) – Manages group-with-exclusion objects on Check Point over Web Services API
- [cp_mgmt_group_with_exclusion_facts module](cp_mgmt_group_with_exclusion_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-group-with-exclusion-facts-module) – Get group-with-exclusion objects facts on Check Point over Web Services API
- [cp_mgmt_gsn_handover_group module](cp_mgmt_gsn_handover_group_module.md#ansible-collections-check-point-mgmt-cp-mgmt-gsn-handover-group-module) – Manages gsn-handover-group objects on Checkpoint over Web Services API
- [cp_mgmt_gsn_handover_group_facts module](cp_mgmt_gsn_handover_group_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-gsn-handover-group-facts-module) – Get gsn-handover-group objects facts on Checkpoint over Web Services API
- [cp_mgmt_ha_full_sync module](cp_mgmt_ha_full_sync_module.md#ansible-collections-check-point-mgmt-cp-mgmt-ha-full-sync-module) – Perform full sync from active server to standby peer.
- [cp_mgmt_host module](cp_mgmt_host_module.md#ansible-collections-check-point-mgmt-cp-mgmt-host-module) – Manages host objects on Check Point over Web Services API
- [cp_mgmt_host_facts module](cp_mgmt_host_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-host-facts-module) – Get host objects facts on Check Point over Web Services API
- [cp_mgmt_hosts module](cp_mgmt_hosts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-hosts-module) – Manages HOSTS resource module
- [cp_mgmt_https_layer module](cp_mgmt_https_layer_module.md#ansible-collections-check-point-mgmt-cp-mgmt-https-layer-module) – Manages https-layer objects on Checkpoint over Web Services API
- [cp_mgmt_https_layer_facts module](cp_mgmt_https_layer_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-https-layer-facts-module) – Get https-layer objects facts on Checkpoint over Web Services API
- [cp_mgmt_https_section module](cp_mgmt_https_section_module.md#ansible-collections-check-point-mgmt-cp-mgmt-https-section-module) – Manages https-section objects on Checkpoint over Web Services API
- [cp_mgmt_identity_tag module](cp_mgmt_identity_tag_module.md#ansible-collections-check-point-mgmt-cp-mgmt-identity-tag-module) – Manages identity-tag objects on Checkpoint over Web Services API
- [cp_mgmt_identity_tag_facts module](cp_mgmt_identity_tag_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-identity-tag-facts-module) – Get identity-tag objects facts on Checkpoint over Web Services API
- [cp_mgmt_idp_administrator_group module](cp_mgmt_idp_administrator_group_module.md#ansible-collections-check-point-mgmt-cp-mgmt-idp-administrator-group-module) – Manages idp-administrator-group objects on Checkpoint over Web Services API
- [cp_mgmt_idp_administrator_group_facts module](cp_mgmt_idp_administrator_group_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-idp-administrator-group-facts-module) – Get idp-administrator-group objects facts on Checkpoint over Web Services API
- [cp_mgmt_idp_to_domain_assignment_facts module](cp_mgmt_idp_to_domain_assignment_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-idp-to-domain-assignment-facts-module) – Get idp-to-domain-assignment objects facts on Checkpoint over Web Services API
- [cp_mgmt_import_management module](cp_mgmt_import_management_module.md#ansible-collections-check-point-mgmt-cp-mgmt-import-management-module) – Import the primary Security Management Server database or the primary Multi-Domain Server database or the single Domain database and the applicable Check Point configuration.
- [cp_mgmt_import_smart_task module](cp_mgmt_import_smart_task_module.md#ansible-collections-check-point-mgmt-cp-mgmt-import-smart-task-module) – Import SmartTask from a file.
- [cp_mgmt_install_database module](cp_mgmt_install_database_module.md#ansible-collections-check-point-mgmt-cp-mgmt-install-database-module) – Copies the user database and network objects information to specified targets.
- [cp_mgmt_install_lsm_policy module](cp_mgmt_install_lsm_policy_module.md#ansible-collections-check-point-mgmt-cp-mgmt-install-lsm-policy-module) – Executes the lsm-install-policy on a given list of targets. Install the LSM policy that defined on the attached LSM profile on the targets devices.
- [cp_mgmt_install_lsm_settings module](cp_mgmt_install_lsm_settings_module.md#ansible-collections-check-point-mgmt-cp-mgmt-install-lsm-settings-module) – Executes the lsm-install-settings on a given list of targets. Install the provisioning settings that defined on the object on the targets devices.
- [cp_mgmt_install_policy module](cp_mgmt_install_policy_module.md#ansible-collections-check-point-mgmt-cp-mgmt-install-policy-module) – install policy on Check Point over Web Services API
- [cp_mgmt_install_software_package module](cp_mgmt_install_software_package_module.md#ansible-collections-check-point-mgmt-cp-mgmt-install-software-package-module) – Installs the software package on target machines.
- [cp_mgmt_interoperable_device module](cp_mgmt_interoperable_device_module.md#ansible-collections-check-point-mgmt-cp-mgmt-interoperable-device-module) – Manages interoperable-device objects on Checkpoint over Web Services API
- [cp_mgmt_interoperable_device_facts module](cp_mgmt_interoperable_device_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-interoperable-device-facts-module) – Get interoperable-device objects facts on Checkpoint over Web Services API
- [cp_mgmt_ips_protection_extended_attribute_facts module](cp_mgmt_ips_protection_extended_attribute_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-ips-protection-extended-attribute-facts-module) – Get ips-protection-extended-attribute objects facts on Checkpoint over Web Services API
- [cp_mgmt_lock_object module](cp_mgmt_lock_object_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lock-object-module) –
- [cp_mgmt_lsm_cluster module](cp_mgmt_lsm_cluster_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsm-cluster-module) – Manages lsm-cluster objects on Checkpoint over Web Services API
- [cp_mgmt_lsm_cluster_facts module](cp_mgmt_lsm_cluster_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsm-cluster-facts-module) – Get lsm-cluster objects facts on Checkpoint over Web Services API
- [cp_mgmt_lsm_cluster_profile_facts module](cp_mgmt_lsm_cluster_profile_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsm-cluster-profile-facts-module) – Get lsm-cluster-profile objects facts on Checkpoint over Web Services API
- [cp_mgmt_lsm_gateway module](cp_mgmt_lsm_gateway_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsm-gateway-module) – Manages lsm-gateway objects on Checkpoint over Web Services API
- [cp_mgmt_lsm_gateway_facts module](cp_mgmt_lsm_gateway_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsm-gateway-facts-module) – Get lsm-gateway objects facts on Checkpoint over Web Services API
- [cp_mgmt_lsm_gateway_profile_facts module](cp_mgmt_lsm_gateway_profile_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsm-gateway-profile-facts-module) – Get lsm-gateway-profile objects facts on Checkpoint over Web Services API
- [cp_mgmt_lsm_run_script module](cp_mgmt_lsm_run_script_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsm-run-script-module) – Executes the lsm-run-script on a given list of targets. Run the given script on the targets devices.
- [cp_mgmt_lsv_profile module](cp_mgmt_lsv_profile_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsv-profile-module) –
- [cp_mgmt_lsv_profile_facts module](cp_mgmt_lsv_profile_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsv-profile-facts-module) – Get lsv-profile objects facts on Checkpoint over Web Services API
- [cp_mgmt_md_permissions_profile module](cp_mgmt_md_permissions_profile_module.md#ansible-collections-check-point-mgmt-cp-mgmt-md-permissions-profile-module) – Manages md-permissions-profile objects on Checkpoint over Web Services API
- [cp_mgmt_md_permissions_profile_facts module](cp_mgmt_md_permissions_profile_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-md-permissions-profile-facts-module) – Get md-permissions-profile objects facts on Checkpoint over Web Services API
- [cp_mgmt_mds module](cp_mgmt_mds_module.md#ansible-collections-check-point-mgmt-cp-mgmt-mds-module) – Manages mds objects on Checkpoint over Web Services API
- [cp_mgmt_mds_facts module](cp_mgmt_mds_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-mds-facts-module) – Get Multi-Domain Server (mds) objects facts on Check Point over Web Services API
- [cp_mgmt_multicast_address_range module](cp_mgmt_multicast_address_range_module.md#ansible-collections-check-point-mgmt-cp-mgmt-multicast-address-range-module) – Manages multicast-address-range objects on Check Point over Web Services API
- [cp_mgmt_multicast_address_range_facts module](cp_mgmt_multicast_address_range_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-multicast-address-range-facts-module) – Get multicast-address-range objects facts on Check Point over Web Services API
- [cp_mgmt_nat_rule module](cp_mgmt_nat_rule_module.md#ansible-collections-check-point-mgmt-cp-mgmt-nat-rule-module) – Manages nat-rule objects on Checkpoint over Web Services API.
- [cp_mgmt_nat_rule_facts module](cp_mgmt_nat_rule_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-nat-rule-facts-module) – Get nat-rule objects facts on Checkpoint over Web Services API
- [cp_mgmt_nat_section module](cp_mgmt_nat_section_module.md#ansible-collections-check-point-mgmt-cp-mgmt-nat-section-module) – Manages nat-section objects on Checkpoint over Web Services API
- [cp_mgmt_network module](cp_mgmt_network_module.md#ansible-collections-check-point-mgmt-cp-mgmt-network-module) – Manages network objects on Check Point over Web Services API
- [cp_mgmt_network_facts module](cp_mgmt_network_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-network-facts-module) – Get network objects facts on Check Point over Web Services API
- [cp_mgmt_network_feed module](cp_mgmt_network_feed_module.md#ansible-collections-check-point-mgmt-cp-mgmt-network-feed-module) – Manages network-feed objects on Checkpoint over Web Services API
- [cp_mgmt_network_feed_facts module](cp_mgmt_network_feed_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-network-feed-facts-module) – Get network-feed objects facts on Checkpoint over Web Services API
- [cp_mgmt_objects_facts module](cp_mgmt_objects_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-objects-facts-module) – Get objects objects facts on Checkpoint over Web Services API
- [cp_mgmt_package module](cp_mgmt_package_module.md#ansible-collections-check-point-mgmt-cp-mgmt-package-module) – Manages package objects on Check Point over Web Services API
- [cp_mgmt_package_facts module](cp_mgmt_package_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-package-facts-module) – Get package objects facts on Check Point over Web Services API
- [cp_mgmt_provisioning_profile_facts module](cp_mgmt_provisioning_profile_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-provisioning-profile-facts-module) – Get provisioning-profile objects facts on Checkpoint over Web Services API
- [cp_mgmt_publish module](cp_mgmt_publish_module.md#ansible-collections-check-point-mgmt-cp-mgmt-publish-module) – All the changes done by this user will be seen by all users only after publish is called.
- [cp_mgmt_put_file module](cp_mgmt_put_file_module.md#ansible-collections-check-point-mgmt-cp-mgmt-put-file-module) – put file on Check Point over Web Services API
- [cp_mgmt_radius_group module](cp_mgmt_radius_group_module.md#ansible-collections-check-point-mgmt-cp-mgmt-radius-group-module) – Manages radius-group objects on Checkpoint over Web Services API
- [cp_mgmt_radius_group_facts module](cp_mgmt_radius_group_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-radius-group-facts-module) – Get radius-group objects facts on Checkpoint over Web Services API
- [cp_mgmt_radius_server module](cp_mgmt_radius_server_module.md#ansible-collections-check-point-mgmt-cp-mgmt-radius-server-module) – Manages radius-server objects on Checkpoint over Web Services API
- [cp_mgmt_radius_server_facts module](cp_mgmt_radius_server_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-radius-server-facts-module) – Get radius-server objects facts on Checkpoint over Web Services API
- [cp_mgmt_reject_session module](cp_mgmt_reject_session_module.md#ansible-collections-check-point-mgmt-cp-mgmt-reject-session-module) – Workflow feature - Return the session to the submitter administrator.
- [cp_mgmt_repository_package_facts module](cp_mgmt_repository_package_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-repository-package-facts-module) – Get repository-package objects facts on Checkpoint over Web Services API
- [cp_mgmt_repository_script module](cp_mgmt_repository_script_module.md#ansible-collections-check-point-mgmt-cp-mgmt-repository-script-module) – Manages repository-script objects on Checkpoint over Web Services API
- [cp_mgmt_repository_script_facts module](cp_mgmt_repository_script_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-repository-script-facts-module) – Get repository-script objects facts on Checkpoint over Web Services API
- [cp_mgmt_reset_sic module](cp_mgmt_reset_sic_module.md#ansible-collections-check-point-mgmt-cp-mgmt-reset-sic-module) – Reset Secure Internal Communication (SIC). To complete the reset operation need also to reset the device in the Check Point Configuration Tool (by running cpconfig in Clish or Expert mode). Communication will not be possible until you reset and re-initialize the device properly.
- [cp_mgmt_run_ips_update module](cp_mgmt_run_ips_update_module.md#ansible-collections-check-point-mgmt-cp-mgmt-run-ips-update-module) – Runs IPS database update. If “package-path” is not provided server will try to get the latest package from the User Center.
- [cp_mgmt_run_script module](cp_mgmt_run_script_module.md#ansible-collections-check-point-mgmt-cp-mgmt-run-script-module) – Executes the script on a given list of targets.
- [cp_mgmt_security_zone module](cp_mgmt_security_zone_module.md#ansible-collections-check-point-mgmt-cp-mgmt-security-zone-module) – Manages security-zone objects on Check Point over Web Services API
- [cp_mgmt_security_zone_facts module](cp_mgmt_security_zone_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-security-zone-facts-module) – Get security-zone objects facts on Check Point over Web Services API
- [cp_mgmt_service_citrix_tcp module](cp_mgmt_service_citrix_tcp_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-citrix-tcp-module) – Manages service-citrix-tcp objects on Checkpoint over Web Services API
- [cp_mgmt_service_citrix_tcp_facts module](cp_mgmt_service_citrix_tcp_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-citrix-tcp-facts-module) – Get service-citrix-tcp objects facts on Checkpoint over Web Services API
- [cp_mgmt_service_compound_tcp module](cp_mgmt_service_compound_tcp_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-compound-tcp-module) – Manages service-compound-tcp objects on Checkpoint over Web Services API
- [cp_mgmt_service_compound_tcp_facts module](cp_mgmt_service_compound_tcp_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-compound-tcp-facts-module) – Get service-compound-tcp objects facts on Checkpoint over Web Services API
- [cp_mgmt_service_dce_rpc module](cp_mgmt_service_dce_rpc_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-dce-rpc-module) – Manages service-dce-rpc objects on Check Point over Web Services API
- [cp_mgmt_service_dce_rpc_facts module](cp_mgmt_service_dce_rpc_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-dce-rpc-facts-module) – Get service-dce-rpc objects facts on Check Point over Web Services API
- [cp_mgmt_service_group module](cp_mgmt_service_group_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-group-module) – Manages service-group objects on Check Point over Web Services API
- [cp_mgmt_service_group_facts module](cp_mgmt_service_group_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-group-facts-module) – Get service-group objects facts on Check Point over Web Services API
- [cp_mgmt_service_icmp module](cp_mgmt_service_icmp_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-icmp-module) – Manages service-icmp objects on Check Point over Web Services API
- [cp_mgmt_service_icmp6 module](cp_mgmt_service_icmp6_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-icmp6-module) – Manages service-icmp6 objects on Check Point over Web Services API
- [cp_mgmt_service_icmp6_facts module](cp_mgmt_service_icmp6_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-icmp6-facts-module) – Get service-icmp6 objects facts on Check Point over Web Services API
- [cp_mgmt_service_icmp_facts module](cp_mgmt_service_icmp_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-icmp-facts-module) – Get service-icmp objects facts on Check Point over Web Services API
- [cp_mgmt_service_other module](cp_mgmt_service_other_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-other-module) – Manages service-other objects on Check Point over Web Services API
- [cp_mgmt_service_other_facts module](cp_mgmt_service_other_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-other-facts-module) – Get service-other objects facts on Check Point over Web Services API
- [cp_mgmt_service_rpc module](cp_mgmt_service_rpc_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-rpc-module) – Manages service-rpc objects on Check Point over Web Services API
- [cp_mgmt_service_rpc_facts module](cp_mgmt_service_rpc_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-rpc-facts-module) – Get service-rpc objects facts on Check Point over Web Services API
- [cp_mgmt_service_sctp module](cp_mgmt_service_sctp_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-sctp-module) – Manages service-sctp objects on Check Point over Web Services API
- [cp_mgmt_service_sctp_facts module](cp_mgmt_service_sctp_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-sctp-facts-module) – Get service-sctp objects facts on Check Point over Web Services API
- [cp_mgmt_service_tcp module](cp_mgmt_service_tcp_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-tcp-module) – Manages service-tcp objects on Check Point over Web Services API
- [cp_mgmt_service_tcp_facts module](cp_mgmt_service_tcp_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-tcp-facts-module) – Get service-tcp objects facts on Check Point over Web Services API
- [cp_mgmt_service_udp module](cp_mgmt_service_udp_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-udp-module) – Manages service-udp objects on Check Point over Web Services API
- [cp_mgmt_service_udp_facts module](cp_mgmt_service_udp_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-service-udp-facts-module) – Get service-udp objects facts on Check Point over Web Services API
- [cp_mgmt_session_facts module](cp_mgmt_session_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-session-facts-module) – Get session objects facts on Check Point over Web Services API
- [cp_mgmt_set_api_settings module](cp_mgmt_set_api_settings_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-api-settings-module) – Edit API settings, the changes will be applied after publish followed by running ‘api restart’ command.
- [cp_mgmt_set_cloud_services module](cp_mgmt_set_cloud_services_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-cloud-services-module) – Set the connection settings between the Management Server and Check Point’s Infinity Portal.
- [cp_mgmt_set_domain module](cp_mgmt_set_domain_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-domain-module) – Edit existing object using object name or uid.
- [cp_mgmt_set_global_domain module](cp_mgmt_set_global_domain_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-global-domain-module) – Edit Global domain object using domain name or UID.
- [cp_mgmt_set_global_properties module](cp_mgmt_set_global_properties_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-global-properties-module) – Edit Global Properties.
- [cp_mgmt_set_ha_state module](cp_mgmt_set_ha_state_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-ha-state-module) – Switch domain server high availability state.
- [cp_mgmt_set_idp_default_assignment module](cp_mgmt_set_idp_default_assignment_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-idp-default-assignment-module) – Set default Identity Provider assignment to be use for Management server administrator access.
- [cp_mgmt_set_idp_to_domain_assignment module](cp_mgmt_set_idp_to_domain_assignment_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-idp-to-domain-assignment-module) – Set Identity Provider assignment to domain, to allow administrator login to that domain using that identity provider, if there is no Identity Provider assigned to the domain the ‘idp-default-assignment’ will be used. This command only available for Multi-Domain server.
- [cp_mgmt_set_ips_update_schedule module](cp_mgmt_set_ips_update_schedule_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-ips-update-schedule-module) – Edit IPS Update Schedule.
- [cp_mgmt_set_login_message module](cp_mgmt_set_login_message_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-login-message-module) – Edit Login message.
- [cp_mgmt_set_nat_rule module](cp_mgmt_set_nat_rule_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-nat-rule-module) – Edit existing object using object name or uid.
- [cp_mgmt_set_policy_settings module](cp_mgmt_set_policy_settings_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-policy-settings-module) – Edit Policy settings, the changes will be applied after publish.
- [cp_mgmt_set_session module](cp_mgmt_set_session_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-session-module) – Edit user’s current session.
- [cp_mgmt_set_threat_advanced_settings module](cp_mgmt_set_threat_advanced_settings_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-threat-advanced-settings-module) – Edit Threat Prevention’s Blades’ Settings.
- [cp_mgmt_set_vpn_community_remote_access module](cp_mgmt_set_vpn_community_remote_access_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-vpn-community-remote-access-module) – Edit existing Remote Access object. Using object name or uid is optional.
- [cp_mgmt_show_access_section module](cp_mgmt_show_access_section_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-access-section-module) – Retrieve existing object using object name or uid.
- [cp_mgmt_show_api_settings module](cp_mgmt_show_api_settings_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-api-settings-module) – Retrieve API Settings.
- [cp_mgmt_show_api_versions module](cp_mgmt_show_api_versions_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-api-versions-module) – Shows all supported API versions and current API version (the latest one).
- [cp_mgmt_show_azure_ad_content module](cp_mgmt_show_azure_ad_content_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-azure-ad-content-module) – Retrieve AzureAD Objects from Azure AD Server.
- [cp_mgmt_show_changes module](cp_mgmt_show_changes_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-changes-module) – Show changes between two sessions.
- [cp_mgmt_show_cloud_services module](cp_mgmt_show_cloud_services_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-cloud-services-module) – Show the connection status of the Management Server to Check Point’s Infinity Portal.
- [cp_mgmt_show_commands module](cp_mgmt_show_commands_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-commands-module) – Retrieve all of the supported Management API commands with their description.
- [cp_mgmt_show_gateways_and_servers module](cp_mgmt_show_gateways_and_servers_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-gateways-and-servers-module) – Shows list of Gateways & Servers sorted by name.
- [cp_mgmt_show_global_domain module](cp_mgmt_show_global_domain_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-global-domain-module) – Retrieve existing object using object name or uid.
- [cp_mgmt_show_global_properties module](cp_mgmt_show_global_properties_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-global-properties-module) – Retrieve Global Properties.
- [cp_mgmt_show_ha_state module](cp_mgmt_show_ha_state_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-ha-state-module) – Retrieve domain high availability state.
- [cp_mgmt_show_https_section module](cp_mgmt_show_https_section_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-https-section-module) – Retrieve existing HTTPS Inspection section using section name or uid and layer name.
- [cp_mgmt_show_idp_default_assignment module](cp_mgmt_show_idp_default_assignment_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-idp-default-assignment-module) – Retrieve default Identity Provider assignment that used for Management server administrator access.
- [cp_mgmt_show_ips_status module](cp_mgmt_show_ips_status_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-ips-status-module) – show ips status on Checkpoint over Web Services API
- [cp_mgmt_show_ips_update_schedule module](cp_mgmt_show_ips_update_schedule_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-ips-update-schedule-module) – Retrieve IPS Update Schedule.
- [cp_mgmt_show_layer_structure module](cp_mgmt_show_layer_structure_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-layer-structure-module) –
- [cp_mgmt_show_login_message module](cp_mgmt_show_login_message_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-login-message-module) – Retrieve Login message.
- [cp_mgmt_show_logs module](cp_mgmt_show_logs_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-logs-module) – Showing logs according to the given filter.
- [cp_mgmt_show_nat_section module](cp_mgmt_show_nat_section_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-nat-section-module) – Retrieve existing object using object name or uid.
- [cp_mgmt_show_place_holder module](cp_mgmt_show_place_holder_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-place-holder-module) – Retrieve existing object using object uid.
- [cp_mgmt_show_policy_settings module](cp_mgmt_show_policy_settings_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-policy-settings-module) – Show Policy settings.
- [cp_mgmt_show_servers_and_processes module](cp_mgmt_show_servers_and_processes_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-servers-and-processes-module) – Shows the status of all processes in the current machine (Multi-Domain Server and all Domain Management / Log Servers). <br>This command is available only on Multi-Domain Server.
- [cp_mgmt_show_software_package_details module](cp_mgmt_show_software_package_details_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-software-package-details-module) – Gets the software package information from the cloud.
- [cp_mgmt_show_software_packages_per_targets module](cp_mgmt_show_software_packages_per_targets_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-software-packages-per-targets-module) – Shows software packages on targets.
- [cp_mgmt_show_task module](cp_mgmt_show_task_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-task-module) – Show task progress and details.
- [cp_mgmt_show_tasks module](cp_mgmt_show_tasks_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-tasks-module) – Retrieve all tasks and show their progress and details.
- [cp_mgmt_show_threat_advanced_settings module](cp_mgmt_show_threat_advanced_settings_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-threat-advanced-settings-module) – Show Threat Prevention’s Blades’ Settings.
- [cp_mgmt_show_unused_objects module](cp_mgmt_show_unused_objects_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-unused-objects-module) – Retrieve all unused objects.
- [cp_mgmt_show_updatable_objects_repository_content module](cp_mgmt_show_updatable_objects_repository_content_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-updatable-objects-repository-content-module) – Shows the content of the available updatable objects from the Check Point User Center.
- [cp_mgmt_show_validations module](cp_mgmt_show_validations_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-validations-module) – Show all validation incidents limited to 500.
- [cp_mgmt_simple_cluster module](cp_mgmt_simple_cluster_module.md#ansible-collections-check-point-mgmt-cp-mgmt-simple-cluster-module) – Manages simple-cluster objects on Checkpoint over Web Services API
- [cp_mgmt_simple_cluster_facts module](cp_mgmt_simple_cluster_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-simple-cluster-facts-module) – Get simple-cluster objects facts on Checkpoint over Web Services API
- [cp_mgmt_simple_gateway module](cp_mgmt_simple_gateway_module.md#ansible-collections-check-point-mgmt-cp-mgmt-simple-gateway-module) – Manages simple-gateway objects on Check Point over Web Services API
- [cp_mgmt_simple_gateway_facts module](cp_mgmt_simple_gateway_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-simple-gateway-facts-module) – Get simple-gateway objects facts on Check Point over Web Services API
- [cp_mgmt_smart_task module](cp_mgmt_smart_task_module.md#ansible-collections-check-point-mgmt-cp-mgmt-smart-task-module) – Manages smart-task objects on Checkpoint over Web Services API
- [cp_mgmt_smart_task_facts module](cp_mgmt_smart_task_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-smart-task-facts-module) – Get smart-task objects facts on Checkpoint over Web Services API
- [cp_mgmt_smart_task_trigger_facts module](cp_mgmt_smart_task_trigger_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-smart-task-trigger-facts-module) – Get smart-task-trigger objects facts on Checkpoint over Web Services API
- [cp_mgmt_smtp_server module](cp_mgmt_smtp_server_module.md#ansible-collections-check-point-mgmt-cp-mgmt-smtp-server-module) – Manages smtp-server objects on Checkpoint over Web Services API
- [cp_mgmt_smtp_server_facts module](cp_mgmt_smtp_server_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-smtp-server-facts-module) – Get smtp-server objects facts on Checkpoint over Web Services API
- [cp_mgmt_submit_session module](cp_mgmt_submit_session_module.md#ansible-collections-check-point-mgmt-cp-mgmt-submit-session-module) – Workflow feature - Submit the session for approval.
- [cp_mgmt_tacacs_group module](cp_mgmt_tacacs_group_module.md#ansible-collections-check-point-mgmt-cp-mgmt-tacacs-group-module) – Manages tacacs-group objects on Checkpoint over Web Services API
- [cp_mgmt_tacacs_group_facts module](cp_mgmt_tacacs_group_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-tacacs-group-facts-module) – Get tacacs-group objects facts on Checkpoint over Web Services API
- [cp_mgmt_tacacs_server module](cp_mgmt_tacacs_server_module.md#ansible-collections-check-point-mgmt-cp-mgmt-tacacs-server-module) – Manages tacacs-server objects on Checkpoint over Web Services API
- [cp_mgmt_tacacs_server_facts module](cp_mgmt_tacacs_server_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-tacacs-server-facts-module) – Get tacacs-server objects facts on Checkpoint over Web Services API
- [cp_mgmt_tag module](cp_mgmt_tag_module.md#ansible-collections-check-point-mgmt-cp-mgmt-tag-module) – Manages tag objects on Check Point over Web Services API
- [cp_mgmt_tag_facts module](cp_mgmt_tag_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-tag-facts-module) – Get tag objects facts on Check Point over Web Services API
- [cp_mgmt_task_facts module](cp_mgmt_task_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-task-facts-module) – Get task objects facts on Checkpoint over Web Services API
- [cp_mgmt_test_sic_status module](cp_mgmt_test_sic_status_module.md#ansible-collections-check-point-mgmt-cp-mgmt-test-sic-status-module) – Test SIC Status reflects the state of the gateway after it has received the certificate issued by the ICA. If the SIC status is Unknown then there is no connection between the gateway and the Security Management Server. If the SIC status is No Communication, an error message will appear. It may contain specific instructions on how to fix the situation.
- [cp_mgmt_threat_exception module](cp_mgmt_threat_exception_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-exception-module) – Manages threat-exception objects on Check Point over Web Services API
- [cp_mgmt_threat_exception_facts module](cp_mgmt_threat_exception_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-exception-facts-module) – Get threat-exception objects facts on Check Point over Web Services API
- [cp_mgmt_threat_indicator module](cp_mgmt_threat_indicator_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-indicator-module) – Manages threat-indicator objects on Check Point over Web Services API
- [cp_mgmt_threat_indicator_facts module](cp_mgmt_threat_indicator_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-indicator-facts-module) – Get threat-indicator objects facts on Check Point over Web Services API
- [cp_mgmt_threat_layer module](cp_mgmt_threat_layer_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-layer-module) – Manages threat-layer objects on Check Point over Web Services API
- [cp_mgmt_threat_layer_facts module](cp_mgmt_threat_layer_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-layer-facts-module) – Get threat-layer objects facts on Check Point over Web Services API
- [cp_mgmt_threat_layers module](cp_mgmt_threat_layers_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-layers-module) – Manages THREAT LAYERS resource module
- [cp_mgmt_threat_profile module](cp_mgmt_threat_profile_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-profile-module) – Manages threat-profile objects on Check Point over Web Services API
- [cp_mgmt_threat_profile_facts module](cp_mgmt_threat_profile_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-profile-facts-module) – Get threat-profile objects facts on Check Point over Web Services API
- [cp_mgmt_threat_protection_override module](cp_mgmt_threat_protection_override_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-protection-override-module) – Edit existing object using object name or uid.
- [cp_mgmt_threat_rule module](cp_mgmt_threat_rule_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-rule-module) – Manages threat-rule objects on Check Point over Web Services API
- [cp_mgmt_threat_rule_facts module](cp_mgmt_threat_rule_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-rule-facts-module) – Get threat-rule objects facts on Check Point over Web Services API
- [cp_mgmt_threat_rules module](cp_mgmt_threat_rules_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-rules-module) – Manages THREAT RULES resource module
- [cp_mgmt_time module](cp_mgmt_time_module.md#ansible-collections-check-point-mgmt-cp-mgmt-time-module) – Manages time objects on Check Point over Web Services API
- [cp_mgmt_time_facts module](cp_mgmt_time_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-time-facts-module) – Get time objects facts on Check Point over Web Services API
- [cp_mgmt_time_group module](cp_mgmt_time_group_module.md#ansible-collections-check-point-mgmt-cp-mgmt-time-group-module) – Manages time-group objects on Checkpoint over Web Services API
- [cp_mgmt_time_group_facts module](cp_mgmt_time_group_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-time-group-facts-module) – Get time-group objects facts on Checkpoint over Web Services API
- [cp_mgmt_trusted_client module](cp_mgmt_trusted_client_module.md#ansible-collections-check-point-mgmt-cp-mgmt-trusted-client-module) – Manages trusted-client objects on Checkpoint over Web Services API
- [cp_mgmt_trusted_client_facts module](cp_mgmt_trusted_client_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-trusted-client-facts-module) – Get trusted-client objects facts on Checkpoint over Web Services API
- [cp_mgmt_uninstall_software_package module](cp_mgmt_uninstall_software_package_module.md#ansible-collections-check-point-mgmt-cp-mgmt-uninstall-software-package-module) – Uninstalls the software package from target machines.
- [cp_mgmt_unlock_administrator module](cp_mgmt_unlock_administrator_module.md#ansible-collections-check-point-mgmt-cp-mgmt-unlock-administrator-module) – Unlock administrator.
- [cp_mgmt_unlock_object module](cp_mgmt_unlock_object_module.md#ansible-collections-check-point-mgmt-cp-mgmt-unlock-object-module) – Unlock object using uid or {name and type}.
- [cp_mgmt_updatable_object_facts module](cp_mgmt_updatable_object_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-updatable-object-facts-module) – Get updatable-object objects facts on Checkpoint over Web Services API
- [cp_mgmt_update_provisioned_satellites module](cp_mgmt_update_provisioned_satellites_module.md#ansible-collections-check-point-mgmt-cp-mgmt-update-provisioned-satellites-module) – Executes the update-provisioned-satellites on center gateways of VPN communities.
- [cp_mgmt_update_updatable_objects_repository_content module](cp_mgmt_update_updatable_objects_repository_content_module.md#ansible-collections-check-point-mgmt-cp-mgmt-update-updatable-objects-repository-content-module) – Updates the content of the Updatable Objects repository from the Check Point User Center.
- [cp_mgmt_user_group module](cp_mgmt_user_group_module.md#ansible-collections-check-point-mgmt-cp-mgmt-user-group-module) – Manages user-group objects on Checkpoint over Web Services API
- [cp_mgmt_user_group_facts module](cp_mgmt_user_group_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-user-group-facts-module) – Get user-group objects facts on Checkpoint over Web Services API
- [cp_mgmt_verify_policy module](cp_mgmt_verify_policy_module.md#ansible-collections-check-point-mgmt-cp-mgmt-verify-policy-module) – Verifies the policy of the selected package.
- [cp_mgmt_verify_software_package module](cp_mgmt_verify_software_package_module.md#ansible-collections-check-point-mgmt-cp-mgmt-verify-software-package-module) – Verifies the software package on target machines.
- [cp_mgmt_vpn_community_meshed module](cp_mgmt_vpn_community_meshed_module.md#ansible-collections-check-point-mgmt-cp-mgmt-vpn-community-meshed-module) – Manages vpn-community-meshed objects on Check Point over Web Services API
- [cp_mgmt_vpn_community_meshed_facts module](cp_mgmt_vpn_community_meshed_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-vpn-community-meshed-facts-module) – Get vpn-community-meshed objects facts on Check Point over Web Services API
- [cp_mgmt_vpn_community_remote_access_facts module](cp_mgmt_vpn_community_remote_access_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-vpn-community-remote-access-facts-module) – Get vpn-community-remote-access objects facts on Checkpoint over Web Services API
- [cp_mgmt_vpn_community_star module](cp_mgmt_vpn_community_star_module.md#ansible-collections-check-point-mgmt-cp-mgmt-vpn-community-star-module) – Manages vpn-community-star objects on Check Point over Web Services API
- [cp_mgmt_vpn_community_star_facts module](cp_mgmt_vpn_community_star_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-vpn-community-star-facts-module) – Get vpn-community-star objects facts on Check Point over Web Services API
- [cp_mgmt_vsx_run_operation module](cp_mgmt_vsx_run_operation_module.md#ansible-collections-check-point-mgmt-cp-mgmt-vsx-run-operation-module) – Run the VSX operation by its name and parameters.
- [cp_mgmt_where_used module](cp_mgmt_where_used_module.md#ansible-collections-check-point-mgmt-cp-mgmt-where-used-module) – Searches for usage of the target object in other objects and rules.
- [cp_mgmt_wildcard module](cp_mgmt_wildcard_module.md#ansible-collections-check-point-mgmt-cp-mgmt-wildcard-module) – Manages wildcard objects on Check Point over Web Services API
- [cp_mgmt_wildcard_facts module](cp_mgmt_wildcard_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-wildcard-facts-module) – Get wildcard objects facts on Check Point over Web Services API

### Httpapi Plugins

- [checkpoint httpapi](checkpoint_httpapi.md#ansible-collections-check-point-mgmt-checkpoint-httpapi) – HttpApi Plugin for Checkpoint devices

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
