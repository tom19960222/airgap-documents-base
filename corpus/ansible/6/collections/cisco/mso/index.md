---
collection: ansible
version: "6"
title: "Cisco.Mso"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/mso/index.html
fetched_at: 2026-07-27T16:41:39+00:00
---
# Cisco.Mso

Collection version 2.1.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

An Ansible collection for managing Cisco ACI Multi-Site

**Authors:**

- Dag Wieers (@dagwieers)
- Nirav Katarmal (@nkatarmal-crest)
- Lionel Hercot (@lhercot)
- Cindy Zhao (@cizhao)
- Shreyas Srish (@shrsr)

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
[Homepage](https://cisco.com/go/aci)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)

## [Plugin Index](index.md#id2)

These are the plugins in the cisco.mso collection:

### Modules

- [mso_backup module](mso_backup_module.md#ansible-collections-cisco-mso-mso-backup-module) – Manages backups
- [mso_backup_schedule module](mso_backup_schedule_module.md#ansible-collections-cisco-mso-mso-backup-schedule-module) – Manages backup schedules
- [mso_dhcp_option_policy module](mso_dhcp_option_policy_module.md#ansible-collections-cisco-mso-mso-dhcp-option-policy-module) – Manage DHCP Option policies.
- [mso_dhcp_option_policy_option module](mso_dhcp_option_policy_option_module.md#ansible-collections-cisco-mso-mso-dhcp-option-policy-option-module) – Manage DHCP options in a DHCP Option policy.
- [mso_dhcp_relay_policy module](mso_dhcp_relay_policy_module.md#ansible-collections-cisco-mso-mso-dhcp-relay-policy-module) – Manage DHCP Relay policies.
- [mso_dhcp_relay_policy_provider module](mso_dhcp_relay_policy_provider_module.md#ansible-collections-cisco-mso-mso-dhcp-relay-policy-provider-module) – Manage DHCP providers in a DHCP Relay policy.
- [mso_label module](mso_label_module.md#ansible-collections-cisco-mso-mso-label-module) – Manage labels
- [mso_remote_location module](mso_remote_location_module.md#ansible-collections-cisco-mso-mso-remote-location-module) – Manages remote locations
- [mso_rest module](mso_rest_module.md#ansible-collections-cisco-mso-mso-rest-module) – Direct access to the Cisco MSO REST API
- [mso_role module](mso_role_module.md#ansible-collections-cisco-mso-mso-role-module) – Manage roles
- [mso_schema module](mso_schema_module.md#ansible-collections-cisco-mso-mso-schema-module) – Manage schemas
- [mso_schema_clone module](mso_schema_clone_module.md#ansible-collections-cisco-mso-mso-schema-clone-module) – Clone schemas
- [mso_schema_site module](mso_schema_site_module.md#ansible-collections-cisco-mso-mso-schema-site-module) – Manage sites in schemas
- [mso_schema_site_anp module](mso_schema_site_anp_module.md#ansible-collections-cisco-mso-mso-schema-site-anp-module) – Manage site-local Application Network Profiles (ANPs) in schema template
- [mso_schema_site_anp_epg module](mso_schema_site_anp_epg_module.md#ansible-collections-cisco-mso-mso-schema-site-anp-epg-module) – Manage site-local Endpoint Groups (EPGs) in schema template
- [mso_schema_site_anp_epg_domain module](mso_schema_site_anp_epg_domain_module.md#ansible-collections-cisco-mso-mso-schema-site-anp-epg-domain-module) – Manage site-local EPG domains in schema template
- [mso_schema_site_anp_epg_selector module](mso_schema_site_anp_epg_selector_module.md#ansible-collections-cisco-mso-mso-schema-site-anp-epg-selector-module) – Manage site-local EPG selector in schema templates
- [mso_schema_site_anp_epg_staticleaf module](mso_schema_site_anp_epg_staticleaf_module.md#ansible-collections-cisco-mso-mso-schema-site-anp-epg-staticleaf-module) – Manage site-local EPG static leafs in schema template
- [mso_schema_site_anp_epg_staticport module](mso_schema_site_anp_epg_staticport_module.md#ansible-collections-cisco-mso-mso-schema-site-anp-epg-staticport-module) – Manage site-local EPG static ports in schema template
- [mso_schema_site_anp_epg_subnet module](mso_schema_site_anp_epg_subnet_module.md#ansible-collections-cisco-mso-mso-schema-site-anp-epg-subnet-module) – Manage site-local EPG subnets in schema template
- [mso_schema_site_bd module](mso_schema_site_bd_module.md#ansible-collections-cisco-mso-mso-schema-site-bd-module) – Manage site-local Bridge Domains (BDs) in schema template
- [mso_schema_site_bd_l3out module](mso_schema_site_bd_l3out_module.md#ansible-collections-cisco-mso-mso-schema-site-bd-l3out-module) – Manage site-local BD l3out’s in schema template
- [mso_schema_site_bd_subnet module](mso_schema_site_bd_subnet_module.md#ansible-collections-cisco-mso-mso-schema-site-bd-subnet-module) – Manage site-local BD subnets in schema template
- [mso_schema_site_external_epg module](mso_schema_site_external_epg_module.md#ansible-collections-cisco-mso-mso-schema-site-external-epg-module) – Manage External EPG in schema of sites
- [mso_schema_site_external_epg_selector module](mso_schema_site_external_epg_selector_module.md#ansible-collections-cisco-mso-mso-schema-site-external-epg-selector-module) – Manage External EPG selector in schema of cloud sites
- [mso_schema_site_l3out module](mso_schema_site_l3out_module.md#ansible-collections-cisco-mso-mso-schema-site-l3out-module) – Manage site-local layer3 Out (L3Outs) in schema template
- [mso_schema_site_service_graph module](mso_schema_site_service_graph_module.md#ansible-collections-cisco-mso-mso-schema-site-service-graph-module) – Manage Service Graph in schema sites
- [mso_schema_site_vrf module](mso_schema_site_vrf_module.md#ansible-collections-cisco-mso-mso-schema-site-vrf-module) – Manage site-local VRFs in schema template
- [mso_schema_site_vrf_region module](mso_schema_site_vrf_region_module.md#ansible-collections-cisco-mso-mso-schema-site-vrf-region-module) – Manage site-local VRF regions in schema template
- [mso_schema_site_vrf_region_cidr module](mso_schema_site_vrf_region_cidr_module.md#ansible-collections-cisco-mso-mso-schema-site-vrf-region-cidr-module) – Manage site-local VRF region CIDRs in schema template
- [mso_schema_site_vrf_region_cidr_subnet module](mso_schema_site_vrf_region_cidr_subnet_module.md#ansible-collections-cisco-mso-mso-schema-site-vrf-region-cidr-subnet-module) – Manage site-local VRF regions in schema template
- [mso_schema_site_vrf_region_hub_network module](mso_schema_site_vrf_region_hub_network_module.md#ansible-collections-cisco-mso-mso-schema-site-vrf-region-hub-network-module) – Manage site-local VRF region hub network in schema template
- [mso_schema_template module](mso_schema_template_module.md#ansible-collections-cisco-mso-mso-schema-template-module) – Manage templates in schemas
- [mso_schema_template_anp module](mso_schema_template_anp_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-module) – Manage Application Network Profiles (ANPs) in schema templates
- [mso_schema_template_anp_epg module](mso_schema_template_anp_epg_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-epg-module) – Manage Endpoint Groups (EPGs) in schema templates
- [mso_schema_template_anp_epg_contract module](mso_schema_template_anp_epg_contract_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-epg-contract-module) – Manage EPG contracts in schema templates
- [mso_schema_template_anp_epg_selector module](mso_schema_template_anp_epg_selector_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-epg-selector-module) – Manage EPG selector in schema templates
- [mso_schema_template_anp_epg_subnet module](mso_schema_template_anp_epg_subnet_module.md#ansible-collections-cisco-mso-mso-schema-template-anp-epg-subnet-module) – Manage EPG subnets in schema templates
- [mso_schema_template_bd module](mso_schema_template_bd_module.md#ansible-collections-cisco-mso-mso-schema-template-bd-module) – Manage Bridge Domains (BDs) in schema templates
- [mso_schema_template_bd_dhcp_policy module](mso_schema_template_bd_dhcp_policy_module.md#ansible-collections-cisco-mso-mso-schema-template-bd-dhcp-policy-module) – Manage BD DHCP Policy in schema templates
- [mso_schema_template_bd_subnet module](mso_schema_template_bd_subnet_module.md#ansible-collections-cisco-mso-mso-schema-template-bd-subnet-module) – Manage BD subnets in schema templates
- [mso_schema_template_clone module](mso_schema_template_clone_module.md#ansible-collections-cisco-mso-mso-schema-template-clone-module) – Clone templates
- [mso_schema_template_contract_filter module](mso_schema_template_contract_filter_module.md#ansible-collections-cisco-mso-mso-schema-template-contract-filter-module) – Manage contract filters in schema templates
- [mso_schema_template_contract_service_graph module](mso_schema_template_contract_service_graph_module.md#ansible-collections-cisco-mso-mso-schema-template-contract-service-graph-module) – Manage the service graph association with a contract in schema template
- [mso_schema_template_deploy module](mso_schema_template_deploy_module.md#ansible-collections-cisco-mso-mso-schema-template-deploy-module) – Deploy schema templates to sites
- [mso_schema_template_deploy_status module](mso_schema_template_deploy_status_module.md#ansible-collections-cisco-mso-mso-schema-template-deploy-status-module) – Check query of objects before deployment to site
- [mso_schema_template_external_epg module](mso_schema_template_external_epg_module.md#ansible-collections-cisco-mso-mso-schema-template-external-epg-module) – Manage external EPGs in schema templates
- [mso_schema_template_external_epg_contract module](mso_schema_template_external_epg_contract_module.md#ansible-collections-cisco-mso-mso-schema-template-external-epg-contract-module) – Manage Extrnal EPG contracts in schema templates
- [mso_schema_template_external_epg_selector module](mso_schema_template_external_epg_selector_module.md#ansible-collections-cisco-mso-mso-schema-template-external-epg-selector-module) – Manage External EPG selector in schema templates
- [mso_schema_template_external_epg_subnet module](mso_schema_template_external_epg_subnet_module.md#ansible-collections-cisco-mso-mso-schema-template-external-epg-subnet-module) – Manage External EPG subnets in schema templates
- [mso_schema_template_filter_entry module](mso_schema_template_filter_entry_module.md#ansible-collections-cisco-mso-mso-schema-template-filter-entry-module) – Manage filter entries in schema templates
- [mso_schema_template_l3out module](mso_schema_template_l3out_module.md#ansible-collections-cisco-mso-mso-schema-template-l3out-module) – Manage l3outs in schema templates
- [mso_schema_template_migrate module](mso_schema_template_migrate_module.md#ansible-collections-cisco-mso-mso-schema-template-migrate-module) – Migrate Bridge Domains (BDs) and EPGs between templates
- [mso_schema_template_service_graph module](mso_schema_template_service_graph_module.md#ansible-collections-cisco-mso-mso-schema-template-service-graph-module) – Manage Service Graph in schema templates
- [mso_schema_template_vrf module](mso_schema_template_vrf_module.md#ansible-collections-cisco-mso-mso-schema-template-vrf-module) – Manage VRFs in schema templates
- [mso_schema_template_vrf_contract module](mso_schema_template_vrf_contract_module.md#ansible-collections-cisco-mso-mso-schema-template-vrf-contract-module) – Manage vrf contracts in schema templates
- [mso_schema_validate module](mso_schema_validate_module.md#ansible-collections-cisco-mso-mso-schema-validate-module) – Validate the schema before deploying it to site
- [mso_service_node_type module](mso_service_node_type_module.md#ansible-collections-cisco-mso-mso-service-node-type-module) – Manage Service Node Types
- [mso_site module](mso_site_module.md#ansible-collections-cisco-mso-mso-site-module) – Manage sites
- [mso_tenant module](mso_tenant_module.md#ansible-collections-cisco-mso-mso-tenant-module) – Manage tenants
- [mso_tenant_site module](mso_tenant_site_module.md#ansible-collections-cisco-mso-mso-tenant-site-module) – Manage tenants with cloud sites.
- [mso_user module](mso_user_module.md#ansible-collections-cisco-mso-mso-user-module) – Manage users
- [mso_version module](mso_version_module.md#ansible-collections-cisco-mso-mso-version-module) – Get version of MSO

### Httpapi Plugins

- [mso httpapi](mso_httpapi.md#ansible-collections-cisco-mso-mso-httpapi) – MSO Ansible HTTPAPI Plugin.

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
