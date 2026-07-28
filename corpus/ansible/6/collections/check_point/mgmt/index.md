---
collection: ansible
version: "6"
title: "Check_Point.Mgmt"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/index.html
fetched_at: 2026-07-27T16:41:35+00:00
---
# Check_Point.Mgmt

Collection version 2.3.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Check Point collection for the Management Server

**Author:**

- Shiran Golzar <[shirango@checkpoint.com](mailto:shirango%40checkpoint.com)>

**Supported ansible-core versions:**

- 2.11 or newer

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)

## [Plugin Index](index.md#id2)

These are the plugins in the check_point.mgmt collection:

### Modules

- [checkpoint_access_layer_facts module](checkpoint_access_layer_facts_module.md#ansible-collections-check-point-mgmt-checkpoint-access-layer-facts-module) – Get access layer facts on Check Point over Web Services API
- [checkpoint_access_rule module](checkpoint_access_rule_module.md#ansible-collections-check-point-mgmt-checkpoint-access-rule-module) – Manages access rules on Check Point over Web Services API
- [checkpoint_access_rule_facts module](checkpoint_access_rule_facts_module.md#ansible-collections-check-point-mgmt-checkpoint-access-rule-facts-module) – Get access rules objects facts on Check Point over Web Services API
- [checkpoint_host module](checkpoint_host_module.md#ansible-collections-check-point-mgmt-checkpoint-host-module) – Manages host objects on Check Point over Web Services API
- [checkpoint_host_facts module](checkpoint_host_facts_module.md#ansible-collections-check-point-mgmt-checkpoint-host-facts-module) – Get host objects facts on Check Point over Web Services API
- [checkpoint_object_facts module](checkpoint_object_facts_module.md#ansible-collections-check-point-mgmt-checkpoint-object-facts-module) – Get object facts on Check Point over Web Services API
- [checkpoint_run_script module](checkpoint_run_script_module.md#ansible-collections-check-point-mgmt-checkpoint-run-script-module) – Run scripts on Check Point devices over Web Services API
- [checkpoint_session module](checkpoint_session_module.md#ansible-collections-check-point-mgmt-checkpoint-session-module) – Manages session objects on Check Point over Web Services API
- [checkpoint_task_facts module](checkpoint_task_facts_module.md#ansible-collections-check-point-mgmt-checkpoint-task-facts-module) – Get task objects facts on Check Point over Web Services API
- [cp_mgmt_access_layer module](cp_mgmt_access_layer_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-layer-module) – Manages access-layer objects on Check Point over Web Services API
- [cp_mgmt_access_layer_facts module](cp_mgmt_access_layer_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-access-layer-facts-module) – Get access-layer objects facts on Check Point over Web Services API
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
- [cp_mgmt_assign_global_assignment module](cp_mgmt_assign_global_assignment_module.md#ansible-collections-check-point-mgmt-cp-mgmt-assign-global-assignment-module) – assign global assignment on Check Point over Web Services API
- [cp_mgmt_data_center_object_facts module](cp_mgmt_data_center_object_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-data-center-object-facts-module) – Get data-center-object objects facts on Checkpoint over Web Services API
- [cp_mgmt_delete_api_key module](cp_mgmt_delete_api_key_module.md#ansible-collections-check-point-mgmt-cp-mgmt-delete-api-key-module) – Delete the API key. For the key to be invalid publish is needed.
- [cp_mgmt_delete_data_center_object module](cp_mgmt_delete_data_center_object_module.md#ansible-collections-check-point-mgmt-cp-mgmt-delete-data-center-object-module) – Delete existing object using object name or uid.
- [cp_mgmt_delete_domain module](cp_mgmt_delete_domain_module.md#ansible-collections-check-point-mgmt-cp-mgmt-delete-domain-module) – Delete existing object using object name or uid.
- [cp_mgmt_delete_nat_rule module](cp_mgmt_delete_nat_rule_module.md#ansible-collections-check-point-mgmt-cp-mgmt-delete-nat-rule-module) – Delete existing object using object name or uid.
- [cp_mgmt_discard module](cp_mgmt_discard_module.md#ansible-collections-check-point-mgmt-cp-mgmt-discard-module) – All changes done by user are discarded and removed from database.
- [cp_mgmt_dns_domain module](cp_mgmt_dns_domain_module.md#ansible-collections-check-point-mgmt-cp-mgmt-dns-domain-module) – Manages dns-domain objects on Check Point over Web Services API
- [cp_mgmt_dns_domain_facts module](cp_mgmt_dns_domain_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-dns-domain-facts-module) – Get dns-domain objects facts on Check Point over Web Services API
- [cp_mgmt_domain_facts module](cp_mgmt_domain_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-domain-facts-module) – Get domain objects facts on Checkpoint over Web Services API
- [cp_mgmt_dynamic_object module](cp_mgmt_dynamic_object_module.md#ansible-collections-check-point-mgmt-cp-mgmt-dynamic-object-module) – Manages dynamic-object objects on Check Point over Web Services API
- [cp_mgmt_dynamic_object_facts module](cp_mgmt_dynamic_object_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-dynamic-object-facts-module) – Get dynamic-object objects facts on Check Point over Web Services API
- [cp_mgmt_exception_group module](cp_mgmt_exception_group_module.md#ansible-collections-check-point-mgmt-cp-mgmt-exception-group-module) – Manages exception-group objects on Check Point over Web Services API
- [cp_mgmt_exception_group_facts module](cp_mgmt_exception_group_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-exception-group-facts-module) – Get exception-group objects facts on Check Point over Web Services API
- [cp_mgmt_global_assignment module](cp_mgmt_global_assignment_module.md#ansible-collections-check-point-mgmt-cp-mgmt-global-assignment-module) – Manages global-assignment objects on Check Point over Web Services API
- [cp_mgmt_global_assignment_facts module](cp_mgmt_global_assignment_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-global-assignment-facts-module) – Get global-assignment objects facts on Check Point over Web Services API
- [cp_mgmt_group module](cp_mgmt_group_module.md#ansible-collections-check-point-mgmt-cp-mgmt-group-module) – Manages group objects on Check Point over Web Services API
- [cp_mgmt_group_facts module](cp_mgmt_group_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-group-facts-module) – Get group objects facts on Check Point over Web Services API
- [cp_mgmt_group_with_exclusion module](cp_mgmt_group_with_exclusion_module.md#ansible-collections-check-point-mgmt-cp-mgmt-group-with-exclusion-module) – Manages group-with-exclusion objects on Check Point over Web Services API
- [cp_mgmt_group_with_exclusion_facts module](cp_mgmt_group_with_exclusion_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-group-with-exclusion-facts-module) – Get group-with-exclusion objects facts on Check Point over Web Services API
- [cp_mgmt_host module](cp_mgmt_host_module.md#ansible-collections-check-point-mgmt-cp-mgmt-host-module) – Manages host objects on Check Point over Web Services API
- [cp_mgmt_host_facts module](cp_mgmt_host_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-host-facts-module) – Get host objects facts on Check Point over Web Services API
- [cp_mgmt_https_section module](cp_mgmt_https_section_module.md#ansible-collections-check-point-mgmt-cp-mgmt-https-section-module) – Manages https-section objects on Checkpoint over Web Services API
- [cp_mgmt_identity_tag module](cp_mgmt_identity_tag_module.md#ansible-collections-check-point-mgmt-cp-mgmt-identity-tag-module) – Manages identity-tag objects on Checkpoint over Web Services API
- [cp_mgmt_identity_tag_facts module](cp_mgmt_identity_tag_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-identity-tag-facts-module) – Get identity-tag objects facts on Checkpoint over Web Services API
- [cp_mgmt_install_database module](cp_mgmt_install_database_module.md#ansible-collections-check-point-mgmt-cp-mgmt-install-database-module) – Copies the user database and network objects information to specified targets.
- [cp_mgmt_install_policy module](cp_mgmt_install_policy_module.md#ansible-collections-check-point-mgmt-cp-mgmt-install-policy-module) – install policy on Check Point over Web Services API
- [cp_mgmt_install_software_package module](cp_mgmt_install_software_package_module.md#ansible-collections-check-point-mgmt-cp-mgmt-install-software-package-module) – Installs the software package on target machines.
- [cp_mgmt_lsm_cluster module](cp_mgmt_lsm_cluster_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsm-cluster-module) – Manages lsm-cluster objects on Checkpoint over Web Services API
- [cp_mgmt_lsm_cluster_facts module](cp_mgmt_lsm_cluster_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsm-cluster-facts-module) – Get lsm-cluster objects facts on Checkpoint over Web Services API
- [cp_mgmt_lsm_gateway module](cp_mgmt_lsm_gateway_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsm-gateway-module) – Manages lsm-gateway objects on Checkpoint over Web Services API
- [cp_mgmt_lsm_gateway_facts module](cp_mgmt_lsm_gateway_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-lsm-gateway-facts-module) – Get lsm-gateway objects facts on Checkpoint over Web Services API
- [cp_mgmt_mds module](cp_mgmt_mds_module.md#ansible-collections-check-point-mgmt-cp-mgmt-mds-module) – Manages mds objects on Checkpoint over Web Services API
- [cp_mgmt_mds_facts module](cp_mgmt_mds_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-mds-facts-module) – Get Multi-Domain Server (mds) objects facts on Check Point over Web Services API
- [cp_mgmt_multicast_address_range module](cp_mgmt_multicast_address_range_module.md#ansible-collections-check-point-mgmt-cp-mgmt-multicast-address-range-module) – Manages multicast-address-range objects on Check Point over Web Services API
- [cp_mgmt_multicast_address_range_facts module](cp_mgmt_multicast_address_range_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-multicast-address-range-facts-module) – Get multicast-address-range objects facts on Check Point over Web Services API
- [cp_mgmt_nat_rule_facts module](cp_mgmt_nat_rule_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-nat-rule-facts-module) – Get nat-rule objects facts on Checkpoint over Web Services API
- [cp_mgmt_nat_section module](cp_mgmt_nat_section_module.md#ansible-collections-check-point-mgmt-cp-mgmt-nat-section-module) – Manages nat-section objects on Checkpoint over Web Services API
- [cp_mgmt_network module](cp_mgmt_network_module.md#ansible-collections-check-point-mgmt-cp-mgmt-network-module) – Manages network objects on Check Point over Web Services API
- [cp_mgmt_network_facts module](cp_mgmt_network_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-network-facts-module) – Get network objects facts on Check Point over Web Services API
- [cp_mgmt_package module](cp_mgmt_package_module.md#ansible-collections-check-point-mgmt-cp-mgmt-package-module) – Manages package objects on Check Point over Web Services API
- [cp_mgmt_package_facts module](cp_mgmt_package_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-package-facts-module) – Get package objects facts on Check Point over Web Services API
- [cp_mgmt_publish module](cp_mgmt_publish_module.md#ansible-collections-check-point-mgmt-cp-mgmt-publish-module) – All the changes done by this user will be seen by all users only after publish is called.
- [cp_mgmt_put_file module](cp_mgmt_put_file_module.md#ansible-collections-check-point-mgmt-cp-mgmt-put-file-module) – put file on Check Point over Web Services API
- [cp_mgmt_run_ips_update module](cp_mgmt_run_ips_update_module.md#ansible-collections-check-point-mgmt-cp-mgmt-run-ips-update-module) – Runs IPS database update. If “package-path” is not provided server will try to get the latest package from the User Center.
- [cp_mgmt_run_script module](cp_mgmt_run_script_module.md#ansible-collections-check-point-mgmt-cp-mgmt-run-script-module) – Executes the script on a given list of targets.
- [cp_mgmt_security_zone module](cp_mgmt_security_zone_module.md#ansible-collections-check-point-mgmt-cp-mgmt-security-zone-module) – Manages security-zone objects on Check Point over Web Services API
- [cp_mgmt_security_zone_facts module](cp_mgmt_security_zone_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-security-zone-facts-module) – Get security-zone objects facts on Check Point over Web Services API
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
- [cp_mgmt_set_domain module](cp_mgmt_set_domain_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-domain-module) – Edit existing object using object name or uid.
- [cp_mgmt_set_nat_rule module](cp_mgmt_set_nat_rule_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-nat-rule-module) – Edit existing object using object name or uid.
- [cp_mgmt_set_session module](cp_mgmt_set_session_module.md#ansible-collections-check-point-mgmt-cp-mgmt-set-session-module) – Edit user’s current session.
- [cp_mgmt_show_access_section module](cp_mgmt_show_access_section_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-access-section-module) – Retrieve existing object using object name or uid.
- [cp_mgmt_show_https_section module](cp_mgmt_show_https_section_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-https-section-module) – Retrieve existing HTTPS Inspection section using section name or uid and layer name.
- [cp_mgmt_show_logs module](cp_mgmt_show_logs_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-logs-module) – Showing logs according to the given filter.
- [cp_mgmt_show_nat_section module](cp_mgmt_show_nat_section_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-nat-section-module) – Retrieve existing object using object name or uid.
- [cp_mgmt_show_software_package_details module](cp_mgmt_show_software_package_details_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-software-package-details-module) – Gets the software package information from the cloud.
- [cp_mgmt_show_task module](cp_mgmt_show_task_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-task-module) – Show task progress and details.
- [cp_mgmt_show_tasks module](cp_mgmt_show_tasks_module.md#ansible-collections-check-point-mgmt-cp-mgmt-show-tasks-module) – Retrieve all tasks and show their progress and details.
- [cp_mgmt_simple_gateway module](cp_mgmt_simple_gateway_module.md#ansible-collections-check-point-mgmt-cp-mgmt-simple-gateway-module) – Manages simple-gateway objects on Check Point over Web Services API
- [cp_mgmt_simple_gateway_facts module](cp_mgmt_simple_gateway_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-simple-gateway-facts-module) – Get simple-gateway objects facts on Check Point over Web Services API
- [cp_mgmt_tag module](cp_mgmt_tag_module.md#ansible-collections-check-point-mgmt-cp-mgmt-tag-module) – Manages tag objects on Check Point over Web Services API
- [cp_mgmt_tag_facts module](cp_mgmt_tag_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-tag-facts-module) – Get tag objects facts on Check Point over Web Services API
- [cp_mgmt_threat_exception module](cp_mgmt_threat_exception_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-exception-module) – Manages threat-exception objects on Check Point over Web Services API
- [cp_mgmt_threat_exception_facts module](cp_mgmt_threat_exception_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-exception-facts-module) – Get threat-exception objects facts on Check Point over Web Services API
- [cp_mgmt_threat_indicator module](cp_mgmt_threat_indicator_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-indicator-module) – Manages threat-indicator objects on Check Point over Web Services API
- [cp_mgmt_threat_indicator_facts module](cp_mgmt_threat_indicator_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-indicator-facts-module) – Get threat-indicator objects facts on Check Point over Web Services API
- [cp_mgmt_threat_layer module](cp_mgmt_threat_layer_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-layer-module) – Manages threat-layer objects on Check Point over Web Services API
- [cp_mgmt_threat_layer_facts module](cp_mgmt_threat_layer_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-layer-facts-module) – Get threat-layer objects facts on Check Point over Web Services API
- [cp_mgmt_threat_profile module](cp_mgmt_threat_profile_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-profile-module) – Manages threat-profile objects on Check Point over Web Services API
- [cp_mgmt_threat_profile_facts module](cp_mgmt_threat_profile_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-profile-facts-module) – Get threat-profile objects facts on Check Point over Web Services API
- [cp_mgmt_threat_protection_override module](cp_mgmt_threat_protection_override_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-protection-override-module) – Edit existing object using object name or uid.
- [cp_mgmt_threat_rule module](cp_mgmt_threat_rule_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-rule-module) – Manages threat-rule objects on Check Point over Web Services API
- [cp_mgmt_threat_rule_facts module](cp_mgmt_threat_rule_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-threat-rule-facts-module) – Get threat-rule objects facts on Check Point over Web Services API
- [cp_mgmt_time module](cp_mgmt_time_module.md#ansible-collections-check-point-mgmt-cp-mgmt-time-module) – Manages time objects on Check Point over Web Services API
- [cp_mgmt_time_facts module](cp_mgmt_time_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-time-facts-module) – Get time objects facts on Check Point over Web Services API
- [cp_mgmt_trusted_client module](cp_mgmt_trusted_client_module.md#ansible-collections-check-point-mgmt-cp-mgmt-trusted-client-module) – Manages trusted-client objects on Checkpoint over Web Services API
- [cp_mgmt_trusted_client_facts module](cp_mgmt_trusted_client_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-trusted-client-facts-module) – Get trusted-client objects facts on Checkpoint over Web Services API
- [cp_mgmt_uninstall_software_package module](cp_mgmt_uninstall_software_package_module.md#ansible-collections-check-point-mgmt-cp-mgmt-uninstall-software-package-module) – Uninstalls the software package from target machines.
- [cp_mgmt_verify_policy module](cp_mgmt_verify_policy_module.md#ansible-collections-check-point-mgmt-cp-mgmt-verify-policy-module) – Verifies the policy of the selected package.
- [cp_mgmt_verify_software_package module](cp_mgmt_verify_software_package_module.md#ansible-collections-check-point-mgmt-cp-mgmt-verify-software-package-module) – Verifies the software package on target machines.
- [cp_mgmt_vpn_community_meshed module](cp_mgmt_vpn_community_meshed_module.md#ansible-collections-check-point-mgmt-cp-mgmt-vpn-community-meshed-module) – Manages vpn-community-meshed objects on Check Point over Web Services API
- [cp_mgmt_vpn_community_meshed_facts module](cp_mgmt_vpn_community_meshed_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-vpn-community-meshed-facts-module) – Get vpn-community-meshed objects facts on Check Point over Web Services API
- [cp_mgmt_vpn_community_star module](cp_mgmt_vpn_community_star_module.md#ansible-collections-check-point-mgmt-cp-mgmt-vpn-community-star-module) – Manages vpn-community-star objects on Check Point over Web Services API
- [cp_mgmt_vpn_community_star_facts module](cp_mgmt_vpn_community_star_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-vpn-community-star-facts-module) – Get vpn-community-star objects facts on Check Point over Web Services API
- [cp_mgmt_wildcard module](cp_mgmt_wildcard_module.md#ansible-collections-check-point-mgmt-cp-mgmt-wildcard-module) – Manages wildcard objects on Check Point over Web Services API
- [cp_mgmt_wildcard_facts module](cp_mgmt_wildcard_facts_module.md#ansible-collections-check-point-mgmt-cp-mgmt-wildcard-facts-module) – Get wildcard objects facts on Check Point over Web Services API

### Httpapi Plugins

- [checkpoint httpapi](checkpoint_httpapi.md#ansible-collections-check-point-mgmt-checkpoint-httpapi) – HttpApi Plugin for Checkpoint devices

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
