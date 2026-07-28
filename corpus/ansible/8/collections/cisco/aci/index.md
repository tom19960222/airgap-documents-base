---
collection: ansible
version: "8"
title: "Cisco.Aci"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/aci/index.html
fetched_at: 2026-07-28T01:01:55+00:00
---
# Cisco.Aci

Collection version 2.8.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Modules for Cisco ACI

**Authors:**

- Dag Wieers (@dagwieers) <[dag@wieers.com](mailto:dag%40wieers.com)>
- Swetha Chunduri (@schunduri)
- Jacob McGill (@jmcgill298)
- Rob Huelga (@RobW3LGA)
- Bruno Calogero <[brunocalogero@hotmail.com](mailto:brunocalogero%40hotmail.com)>
- Simon Metzger <[smnmtzgr@gmail.com](mailto:smnmtzgr%40gmail.com)>
- Tim Knipper <[tim.knipper@gmail.com](mailto:tim.knipper%40gmail.com)>
- Apoorva Gururaja (@aciguru)
- Devarshi Shah (@devarshishah3)
- Ramses Smeyers (@rsmeyers)
- Lionel Hercot (@lhercot) <[lhercot@cisco.com](mailto:lhercot%40cisco.com)>

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-aci/issues)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-aci)

## [Plugin Index](index.md#id2)

These are the plugins in the cisco.aci collection:

### Modules

- [aci_aaa_custom_privilege module](aci_aaa_custom_privilege_module.md#ansible-collections-cisco-aci-aci-aaa-custom-privilege-module) – Manage AAA RBAC Custom Privileges (aaa:RbacClassPriv)
- [aci_aaa_domain module](aci_aaa_domain_module.md#ansible-collections-cisco-aci-aci-aaa-domain-module) – Manage AAA domains (aaa:Domain)
- [aci_aaa_role module](aci_aaa_role_module.md#ansible-collections-cisco-aci-aci-aaa-role-module) – Manage AAA roles (aaa:Role)
- [aci_aaa_ssh_auth module](aci_aaa_ssh_auth_module.md#ansible-collections-cisco-aci-aci-aaa-ssh-auth-module) – Manage AAA SSH auth (aaaSshAuth) objects.
- [aci_aaa_user module](aci_aaa_user_module.md#ansible-collections-cisco-aci-aci-aaa-user-module) – Manage AAA users (aaa:User)
- [aci_aaa_user_certificate module](aci_aaa_user_certificate_module.md#ansible-collections-cisco-aci-aci-aaa-user-certificate-module) – Manage AAA user certificates (aaa:UserCert)
- [aci_aaa_user_domain module](aci_aaa_user_domain_module.md#ansible-collections-cisco-aci-aci-aaa-user-domain-module) – Manage AAA user domains (aaa:UserDomain)
- [aci_aaa_user_role module](aci_aaa_user_role_module.md#ansible-collections-cisco-aci-aci-aaa-user-role-module) – Manage AAA user roles (aaa:UserRole)
- [aci_access_port_block_to_access_port module](aci_access_port_block_to_access_port_module.md#ansible-collections-cisco-aci-aci-access-port-block-to-access-port-module) – Manage port blocks of Fabric interface policy leaf profile interface selectors (infra:HPortS, infra:PortBlk)
- [aci_access_port_to_interface_policy_leaf_profile module](aci_access_port_to_interface_policy_leaf_profile_module.md#ansible-collections-cisco-aci-aci-access-port-to-interface-policy-leaf-profile-module) – Manage Fabric interface policy leaf profile interface selectors (infra:HPortS, infra:RsAccBaseGrp, infra:PortBlk)
- [aci_access_span_dst_group module](aci_access_span_dst_group_module.md#ansible-collections-cisco-aci-aci-access-span-dst-group-module) – Manage Access SPAN destination groups (span:DestGrp)
- [aci_access_span_filter_group module](aci_access_span_filter_group_module.md#ansible-collections-cisco-aci-aci-access-span-filter-group-module) – Manage Access SPAN filter groups (span:FilterGrp)
- [aci_access_span_filter_group_entry module](aci_access_span_filter_group_entry_module.md#ansible-collections-cisco-aci-aci-access-span-filter-group-entry-module) – Manage Access SPAN filter group entries (span:FilterEntry)
- [aci_access_span_src_group module](aci_access_span_src_group_module.md#ansible-collections-cisco-aci-aci-access-span-src-group-module) – Manage Access SPAN source groups (span:SrcGrp)
- [aci_access_span_src_group_src module](aci_access_span_src_group_src_module.md#ansible-collections-cisco-aci-aci-access-span-src-group-src-module) – Manage Access SPAN sources (span:Src)
- [aci_access_span_src_group_src_path module](aci_access_span_src_group_src_path_module.md#ansible-collections-cisco-aci-aci-access-span-src-group-src-path-module) – Manage Access SPAN source paths (span:RsSrcToPathEp)
- [aci_access_sub_port_block_to_access_port module](aci_access_sub_port_block_to_access_port_module.md#ansible-collections-cisco-aci-aci-access-sub-port-block-to-access-port-module) – Manage sub port blocks of Fabric interface policy leaf profile interface selectors (infra:HPortS, infra:SubPortBlk)
- [aci_aep module](aci_aep_module.md#ansible-collections-cisco-aci-aci-aep-module) – Manage attachable Access Entity Profile (AEP) objects (infra:AttEntityP, infra:ProvAcc)
- [aci_aep_to_domain module](aci_aep_to_domain_module.md#ansible-collections-cisco-aci-aci-aep-to-domain-module) – Bind AEPs to Physical or Virtual Domains (infra:RsDomP)
- [aci_aep_to_epg module](aci_aep_to_epg_module.md#ansible-collections-cisco-aci-aci-aep-to-epg-module) – Bind EPG to AEP (infra:RsFuncToEpg).
- [aci_ap module](aci_ap_module.md#ansible-collections-cisco-aci-aci-ap-module) – Manage top level Application Profile (AP) objects (fv:Ap)
- [aci_bd module](aci_bd_module.md#ansible-collections-cisco-aci-aci-bd-module) – Manage Bridge Domains (BD) objects (fv:BD)
- [aci_bd_dhcp_label module](aci_bd_dhcp_label_module.md#ansible-collections-cisco-aci-aci-bd-dhcp-label-module) – Manage DHCP Labels (dhcp:Lbl)
- [aci_bd_subnet module](aci_bd_subnet_module.md#ansible-collections-cisco-aci-aci-bd-subnet-module) – Manage Subnets (fv:Subnet)
- [aci_bd_to_l3out module](aci_bd_to_l3out_module.md#ansible-collections-cisco-aci-aci-bd-to-l3out-module) – Bind Bridge Domain to L3 Out (fv:RsBDToOut)
- [aci_bgp_best_path_policy module](aci_bgp_best_path_policy_module.md#ansible-collections-cisco-aci-aci-bgp-best-path-policy-module) – Manage BGP Best Path policy (bgp:BestPathCtrlPol)
- [aci_bgp_rr_asn module](aci_bgp_rr_asn_module.md#ansible-collections-cisco-aci-aci-bgp-rr-asn-module) – Manage BGP Route Reflector ASN.
- [aci_bgp_rr_node module](aci_bgp_rr_node_module.md#ansible-collections-cisco-aci-aci-bgp-rr-node-module) – Manage BGP Route Reflector objects.
- [aci_bgp_timers_policy module](aci_bgp_timers_policy_module.md#ansible-collections-cisco-aci-aci-bgp-timers-policy-module) – Manage BGP timers policy (bgp:CtxPol)
- [aci_bulk_static_binding_to_epg module](aci_bulk_static_binding_to_epg_module.md#ansible-collections-cisco-aci-aci-bulk-static-binding-to-epg-module) – Bind static paths to EPGs (fv:RsPathAtt)
- [aci_cloud_ap module](aci_cloud_ap_module.md#ansible-collections-cisco-aci-aci-cloud-ap-module) – Manage Cloud Application Profile (AP) (cloud:App)
- [aci_cloud_aws_provider module](aci_cloud_aws_provider_module.md#ansible-collections-cisco-aci-aci-cloud-aws-provider-module) – Manage Cloud AWS Provider (cloud:AwsProvider)
- [aci_cloud_bgp_asn module](aci_cloud_bgp_asn_module.md#ansible-collections-cisco-aci-aci-cloud-bgp-asn-module) – Manage Cloud APIC BGP Autonomous System Profile (cloud:BgpAsP)
- [aci_cloud_cidr module](aci_cloud_cidr_module.md#ansible-collections-cisco-aci-aci-cloud-cidr-module) – Manage CIDR under Cloud Context Profile (cloud:Cidr)
- [aci_cloud_ctx_profile module](aci_cloud_ctx_profile_module.md#ansible-collections-cisco-aci-aci-cloud-ctx-profile-module) – Manage Cloud Context Profile (cloud:CtxProfile)
- [aci_cloud_epg module](aci_cloud_epg_module.md#ansible-collections-cisco-aci-aci-cloud-epg-module) – Manage Cloud EPG (cloud:EPg)
- [aci_cloud_epg_selector module](aci_cloud_epg_selector_module.md#ansible-collections-cisco-aci-aci-cloud-epg-selector-module) – Manage Cloud Endpoint Selector (cloud:EPSelector)
- [aci_cloud_external_epg module](aci_cloud_external_epg_module.md#ansible-collections-cisco-aci-aci-cloud-external-epg-module) – Manage Cloud External EPG (cloud:ExtEPg)
- [aci_cloud_external_epg_selector module](aci_cloud_external_epg_selector_module.md#ansible-collections-cisco-aci-aci-cloud-external-epg-selector-module) – Manage Cloud Endpoint Selector for External EPGs (cloud:ExtEPSelector)
- [aci_cloud_provider module](aci_cloud_provider_module.md#ansible-collections-cisco-aci-aci-cloud-provider-module) – Query Cloud Provider information (cloud:ProvP)
- [aci_cloud_region module](aci_cloud_region_module.md#ansible-collections-cisco-aci-aci-cloud-region-module) – Manage Cloud Providers Region (cloud:Region)
- [aci_cloud_subnet module](aci_cloud_subnet_module.md#ansible-collections-cisco-aci-aci-cloud-subnet-module) – Manage Cloud Subnet (cloud:Subnet)
- [aci_cloud_vpn_gateway module](aci_cloud_vpn_gateway_module.md#ansible-collections-cisco-aci-aci-cloud-vpn-gateway-module) – Manage cloudRouterP in Cloud Context Profile (cloud:cloudRouterP)
- [aci_cloud_zone module](aci_cloud_zone_module.md#ansible-collections-cisco-aci-aci-cloud-zone-module) – Manage Cloud Availability Zone (cloud:Zone)
- [aci_config_export_policy module](aci_config_export_policy_module.md#ansible-collections-cisco-aci-aci-config-export-policy-module) – Manage Configuration Export Policy (config:ExportP)
- [aci_config_rollback module](aci_config_rollback_module.md#ansible-collections-cisco-aci-aci-config-rollback-module) – Provides rollback and rollback preview functionality (config:ImportP)
- [aci_config_snapshot module](aci_config_snapshot_module.md#ansible-collections-cisco-aci-aci-config-snapshot-module) – Manage Config Snapshots (config:Snapshot, config:ExportP)
- [aci_contract module](aci_contract_module.md#ansible-collections-cisco-aci-aci-contract-module) – Manage contract resources (vz:BrCP)
- [aci_contract_export module](aci_contract_export_module.md#ansible-collections-cisco-aci-aci-contract-export-module) – Manage contract interfaces (vz:CPIf)
- [aci_contract_subject module](aci_contract_subject_module.md#ansible-collections-cisco-aci-aci-contract-subject-module) – Manage initial Contract Subjects (vz:Subj)
- [aci_contract_subject_to_filter module](aci_contract_subject_to_filter_module.md#ansible-collections-cisco-aci-aci-contract-subject-to-filter-module) – Bind Contract Subjects to Filters (vz:RsSubjFiltAtt)
- [aci_contract_subject_to_service_graph module](aci_contract_subject_to_service_graph_module.md#ansible-collections-cisco-aci-aci-contract-subject-to-service-graph-module) – Bind contract subject to service graph (vz:RsSubjGraphAtt).
- [aci_dhcp_relay module](aci_dhcp_relay_module.md#ansible-collections-cisco-aci-aci-dhcp-relay-module) – Manage DHCP relay policies.
- [aci_dhcp_relay_provider module](aci_dhcp_relay_provider_module.md#ansible-collections-cisco-aci-aci-dhcp-relay-provider-module) – Manage DHCP relay policy providers.
- [aci_dns_domain module](aci_dns_domain_module.md#ansible-collections-cisco-aci-aci-dns-domain-module) – Manage DNS Provider (dnsDomain) objects.
- [aci_dns_profile module](aci_dns_profile_module.md#ansible-collections-cisco-aci-aci-dns-profile-module) – Manage DNS Profile (dnsProfile) objects.
- [aci_dns_provider module](aci_dns_provider_module.md#ansible-collections-cisco-aci-aci-dns-provider-module) – Manage DNS Provider (dnsProv) objects.
- [aci_domain module](aci_domain_module.md#ansible-collections-cisco-aci-aci-domain-module) – Manage physical, virtual, bridged, routed or FC domain profiles (phys:DomP, vmm:DomP, l2ext:DomP, l3ext:DomP, fc:DomP)
- [aci_domain_to_encap_pool module](aci_domain_to_encap_pool_module.md#ansible-collections-cisco-aci-aci-domain-to-encap-pool-module) – Bind Domain to Encap Pools (infra:RsVlanNs)
- [aci_domain_to_vlan_pool module](aci_domain_to_vlan_pool_module.md#ansible-collections-cisco-aci-aci-domain-to-vlan-pool-module) – Bind Domain to VLAN Pools (infra:RsVlanNs)
- [aci_encap_pool module](aci_encap_pool_module.md#ansible-collections-cisco-aci-aci-encap-pool-module) – Manage encap pools (fvns:VlanInstP, fvns:VxlanInstP, fvns:VsanInstP)
- [aci_encap_pool_range module](aci_encap_pool_range_module.md#ansible-collections-cisco-aci-aci-encap-pool-range-module) – Manage encap ranges assigned to pools (fvns:EncapBlk, fvns:VsanEncapBlk)
- [aci_epg module](aci_epg_module.md#ansible-collections-cisco-aci-aci-epg-module) – Manage End Point Groups (EPG) objects (fv:AEPg)
- [aci_epg_monitoring_policy module](aci_epg_monitoring_policy_module.md#ansible-collections-cisco-aci-aci-epg-monitoring-policy-module) – Manage monitoring policies (mon:EPGPol)
- [aci_epg_subnet module](aci_epg_subnet_module.md#ansible-collections-cisco-aci-aci-epg-subnet-module) – Manage EPG Subnets (fv:Subnet)
- [aci_epg_to_contract module](aci_epg_to_contract_module.md#ansible-collections-cisco-aci-aci-epg-to-contract-module) – Bind EPGs to Contracts (fv:RsCons, fv:RsProv)
- [aci_epg_to_contract_interface module](aci_epg_to_contract_interface_module.md#ansible-collections-cisco-aci-aci-epg-to-contract-interface-module) – Bind EPGs to Consumed Contracts Interface (fv:RsConsIf).
- [aci_epg_to_contract_master module](aci_epg_to_contract_master_module.md#ansible-collections-cisco-aci-aci-epg-to-contract-master-module) – Manage End Point Group (EPG) contract master relationships (fv:RsSecInherited)
- [aci_epg_to_domain module](aci_epg_to_domain_module.md#ansible-collections-cisco-aci-aci-epg-to-domain-module) – Bind EPGs to Domains (fv:RsDomAtt)
- [aci_esg module](aci_esg_module.md#ansible-collections-cisco-aci-aci-esg-module) – Manage Endpoint Security Groups (ESGs) objects (fv:ESg)
- [aci_esg_contract_master module](aci_esg_contract_master_module.md#ansible-collections-cisco-aci-aci-esg-contract-master-module) – Manage ESG contract master relationships (fv:RsSecInherited)
- [aci_esg_epg_selector module](aci_esg_epg_selector_module.md#ansible-collections-cisco-aci-aci-esg-epg-selector-module) – Manage ESG - EPG Selectors (fv:fvEPgSelector)
- [aci_esg_ip_subnet_selector module](aci_esg_ip_subnet_selector_module.md#ansible-collections-cisco-aci-aci-esg-ip-subnet-selector-module) – Manage ESG IP Subnet selector(fv:EPSelector)
- [aci_esg_tag_selector module](aci_esg_tag_selector_module.md#ansible-collections-cisco-aci-aci-esg-tag-selector-module) – Manage ESG Tag Selectors (fv:TagSelector)
- [aci_fabric_interface_policy_group module](aci_fabric_interface_policy_group_module.md#ansible-collections-cisco-aci-aci-fabric-interface-policy-group-module) – Manage Fabric Interface Policy Groups (fabric:LePortPGrp, fabric:SpPortPGrp)
- [aci_fabric_leaf_profile module](aci_fabric_leaf_profile_module.md#ansible-collections-cisco-aci-aci-fabric-leaf-profile-module) – Manage fabric leaf profiles (fabric:LeafP).
- [aci_fabric_leaf_switch_assoc module](aci_fabric_leaf_switch_assoc_module.md#ansible-collections-cisco-aci-aci-fabric-leaf-switch-assoc-module) – Manage leaf switch bindings to profiles and policy groups (fabric:LeafS and fabric:RsLeNodePGrp).
- [aci_fabric_node module](aci_fabric_node_module.md#ansible-collections-cisco-aci-aci-fabric-node-module) – Manage Fabric Node Members (fabric:NodeIdentP)
- [aci_fabric_node_control module](aci_fabric_node_control_module.md#ansible-collections-cisco-aci-aci-fabric-node-control-module) – Manage Fabric Node Controls (fabric:NodeControl)
- [aci_fabric_pod_policy_group module](aci_fabric_pod_policy_group_module.md#ansible-collections-cisco-aci-aci-fabric-pod-policy-group-module) – Manage Fabric Pod Policy Groups (fabric:PodPGrp)
- [aci_fabric_pod_selector module](aci_fabric_pod_selector_module.md#ansible-collections-cisco-aci-aci-fabric-pod-selector-module) – Manage Fabric Pod Selectors (fabric:PodS)
- [aci_fabric_scheduler module](aci_fabric_scheduler_module.md#ansible-collections-cisco-aci-aci-fabric-scheduler-module) – This module creates ACI schedulers (trig:SchedP)
- [aci_fabric_span_dst_group module](aci_fabric_span_dst_group_module.md#ansible-collections-cisco-aci-aci-fabric-span-dst-group-module) – Manage Fabric SPAN destination groups (span:DestGrp)
- [aci_fabric_span_src_group module](aci_fabric_span_src_group_module.md#ansible-collections-cisco-aci-aci-fabric-span-src-group-module) – Manage Fabric SPAN source groups (span:SrcGrp)
- [aci_fabric_span_src_group_src module](aci_fabric_span_src_group_src_module.md#ansible-collections-cisco-aci-aci-fabric-span-src-group-src-module) – Manage Fabric SPAN sources (span:Src)
- [aci_fabric_span_src_group_src_node module](aci_fabric_span_src_group_src_node_module.md#ansible-collections-cisco-aci-aci-fabric-span-src-group-src-node-module) – Manage Fabric SPAN source nodes (span:RsSrcToNode)
- [aci_fabric_span_src_group_src_path module](aci_fabric_span_src_group_src_path_module.md#ansible-collections-cisco-aci-aci-fabric-span-src-group-src-path-module) – Manage Fabric SPAN source paths (span:RsSrcToPathEp)
- [aci_fabric_spine_profile module](aci_fabric_spine_profile_module.md#ansible-collections-cisco-aci-aci-fabric-spine-profile-module) – Manage fabric spine profiles (fabric:SpineP).
- [aci_fabric_spine_switch_assoc module](aci_fabric_spine_switch_assoc_module.md#ansible-collections-cisco-aci-aci-fabric-spine-switch-assoc-module) – Manage spine switch bindings to profiles and policy groups (fabric:SpineS and fabric:RsSpNodePGrp).
- [aci_fabric_switch_block module](aci_fabric_switch_block_module.md#ansible-collections-cisco-aci-aci-fabric-switch-block-module) – Manage switch blocks (fabric:NodeBlk).
- [aci_fabric_switch_policy_group module](aci_fabric_switch_policy_group_module.md#ansible-collections-cisco-aci-aci-fabric-switch-policy-group-module) – Manage Fabric Switch Policy Group objects.
- [aci_fabric_wide_settings module](aci_fabric_wide_settings_module.md#ansible-collections-cisco-aci-aci-fabric-wide-settings-module) – Manage Fabric Wide Settings (infra:SetPol)
- [aci_file_remote_path module](aci_file_remote_path_module.md#ansible-collections-cisco-aci-aci-file-remote-path-module) – Manage Import/Export File Remote Paths (<file:RemotePath>)
- [aci_filter module](aci_filter_module.md#ansible-collections-cisco-aci-aci-filter-module) – Manages top level filter objects (vz:Filter)
- [aci_filter_entry module](aci_filter_entry_module.md#ansible-collections-cisco-aci-aci-filter-entry-module) – Manage filter entries (vz:Entry)
- [aci_firmware_group module](aci_firmware_group_module.md#ansible-collections-cisco-aci-aci-firmware-group-module) – Manage firmware groups (firmware:FwGrp)
- [aci_firmware_group_node module](aci_firmware_group_node_module.md#ansible-collections-cisco-aci-aci-firmware-group-node-module) – Manage firmware group nodes (fabric:NodeBlk)
- [aci_firmware_policy module](aci_firmware_policy_module.md#ansible-collections-cisco-aci-aci-firmware-policy-module) – Manage firmware policies (firmware:FwP)
- [aci_firmware_source module](aci_firmware_source_module.md#ansible-collections-cisco-aci-aci-firmware-source-module) – Manage firmware image sources (firmware:OSource)
- [aci_igmp_interface_policy module](aci_igmp_interface_policy_module.md#ansible-collections-cisco-aci-aci-igmp-interface-policy-module) – Manage IGMP Interface Policies (igmp:IfPol)
- [aci_interface_blacklist module](aci_interface_blacklist_module.md#ansible-collections-cisco-aci-aci-interface-blacklist-module) – Enabling or Disabling physical interfaces.
- [aci_interface_config module](aci_interface_config_module.md#ansible-collections-cisco-aci-aci-interface-config-module) – Manage Interface Configuration of Access (infra:PortConfig) and Fabric (fabric:PortConfig) Ports is only supported for ACI 5.2(7)+
- [aci_interface_description module](aci_interface_description_module.md#ansible-collections-cisco-aci-aci-interface-description-module) – Setting and removing description on physical interfaces.
- [aci_interface_policy_cdp module](aci_interface_policy_cdp_module.md#ansible-collections-cisco-aci-aci-interface-policy-cdp-module) – Manage CDP interface policies (cdp:IfPol)
- [aci_interface_policy_fc module](aci_interface_policy_fc_module.md#ansible-collections-cisco-aci-aci-interface-policy-fc-module) – Manage Fibre Channel interface policies (fc:IfPol)
- [aci_interface_policy_l2 module](aci_interface_policy_l2_module.md#ansible-collections-cisco-aci-aci-interface-policy-l2-module) – Manage Layer 2 interface policies (l2:IfPol)
- [aci_interface_policy_leaf_breakout_port_group module](aci_interface_policy_leaf_breakout_port_group_module.md#ansible-collections-cisco-aci-aci-interface-policy-leaf-breakout-port-group-module) – Manage fabric interface policy leaf breakout port group (infra:BrkoutPortGrp)
- [aci_interface_policy_leaf_fc_policy_group module](aci_interface_policy_leaf_fc_policy_group_module.md#ansible-collections-cisco-aci-aci-interface-policy-leaf-fc-policy-group-module) – Manage Fibre Channel (FC) interface policy groups (infra:FcAccBndlGrp, infra:FcAccPortGrp)
- [aci_interface_policy_leaf_policy_group module](aci_interface_policy_leaf_policy_group_module.md#ansible-collections-cisco-aci-aci-interface-policy-leaf-policy-group-module) – Manage fabric interface policy leaf policy groups (infra:AccBndlGrp, infra:AccPortGrp)
- [aci_interface_policy_leaf_profile module](aci_interface_policy_leaf_profile_module.md#ansible-collections-cisco-aci-aci-interface-policy-leaf-profile-module) – Manage fabric interface policy leaf profiles (infra:AccPortP)
- [aci_interface_policy_leaf_profile_fex_policy_group module](aci_interface_policy_leaf_profile_fex_policy_group_module.md#ansible-collections-cisco-aci-aci-interface-policy-leaf-profile-fex-policy-group-module) – Manage leaf interface profiles fex policy group (infra:FexBndlGrp)
- [aci_interface_policy_link_level module](aci_interface_policy_link_level_module.md#ansible-collections-cisco-aci-aci-interface-policy-link-level-module) – Manage Link Level interface policies (fabric:HIfPol)
- [aci_interface_policy_lldp module](aci_interface_policy_lldp_module.md#ansible-collections-cisco-aci-aci-interface-policy-lldp-module) – Manage LLDP interface policies (lldp:IfPol)
- [aci_interface_policy_mcp module](aci_interface_policy_mcp_module.md#ansible-collections-cisco-aci-aci-interface-policy-mcp-module) – Manage MCP interface policies (mcp:IfPol)
- [aci_interface_policy_ospf module](aci_interface_policy_ospf_module.md#ansible-collections-cisco-aci-aci-interface-policy-ospf-module) – Manage OSPF interface policies (ospf:IfPol)
- [aci_interface_policy_port_channel module](aci_interface_policy_port_channel_module.md#ansible-collections-cisco-aci-aci-interface-policy-port-channel-module) – Manage port channel interface policies (lacp:LagPol)
- [aci_interface_policy_port_security module](aci_interface_policy_port_security_module.md#ansible-collections-cisco-aci-aci-interface-policy-port-security-module) – Manage port security (l2:PortSecurityPol)
- [aci_interface_policy_spanning_tree module](aci_interface_policy_spanning_tree_module.md#ansible-collections-cisco-aci-aci-interface-policy-spanning-tree-module) – Manage spanning tree interface policies (stp:IfPol)
- [aci_interface_policy_spine_policy_group module](aci_interface_policy_spine_policy_group_module.md#ansible-collections-cisco-aci-aci-interface-policy-spine-policy-group-module) – Manage spine access interface policy groups (infra:SpAccPortGrp)
- [aci_interface_selector_to_switch_policy_leaf_profile module](aci_interface_selector_to_switch_policy_leaf_profile_module.md#ansible-collections-cisco-aci-aci-interface-selector-to-switch-policy-leaf-profile-module) – Bind interface selector profiles to switch policy leaf profiles (infra:RsAccPortP)
- [aci_l2out module](aci_l2out_module.md#ansible-collections-cisco-aci-aci-l2out-module) – Manage Layer2 Out (L2Out) objects.
- [aci_l2out_extepg module](aci_l2out_extepg_module.md#ansible-collections-cisco-aci-aci-l2out-extepg-module) – Manage External Network Instance (L2Out External EPG) objects (l2extInstP).
- [aci_l2out_extepg_to_contract module](aci_l2out_extepg_to_contract_module.md#ansible-collections-cisco-aci-aci-l2out-extepg-to-contract-module) – Bind Contracts to L2 External End Point Groups (EPGs)
- [aci_l2out_logical_interface_path module](aci_l2out_logical_interface_path_module.md#ansible-collections-cisco-aci-aci-l2out-logical-interface-path-module) – Manage Layer 2 Outside (L2Out) logical interface path (l2extRsPathL2OutAtt)
- [aci_l2out_logical_interface_profile module](aci_l2out_logical_interface_profile_module.md#ansible-collections-cisco-aci-aci-l2out-logical-interface-profile-module) – Manage Layer 2 Outside (L2Out) interface profiles (l2ext:LIfP)
- [aci_l2out_logical_node_profile module](aci_l2out_logical_node_profile_module.md#ansible-collections-cisco-aci-aci-l2out-logical-node-profile-module) – Manage Layer 2 Outside (L2Out) logical node profiles (l2ext:LNodeP)
- [aci_l3out module](aci_l3out_module.md#ansible-collections-cisco-aci-aci-l3out-module) – Manage Layer 3 Outside (L3Out) objects (l3ext:Out)
- [aci_l3out_bgp_peer module](aci_l3out_bgp_peer_module.md#ansible-collections-cisco-aci-aci-l3out-bgp-peer-module) – Manage Layer 3 Outside (L3Out) BGP Peers (bgp:PeerP)
- [aci_l3out_bgp_protocol_profile module](aci_l3out_bgp_protocol_profile_module.md#ansible-collections-cisco-aci-aci-l3out-bgp-protocol-profile-module) – Manage BGP Protocol Profile (bgp:ProtP)
- [aci_l3out_extepg module](aci_l3out_extepg_module.md#ansible-collections-cisco-aci-aci-l3out-extepg-module) – Manage External Network Instance Profile (ExtEpg) objects (l3extInstP:instP)
- [aci_l3out_extepg_to_contract module](aci_l3out_extepg_to_contract_module.md#ansible-collections-cisco-aci-aci-l3out-extepg-to-contract-module) – Bind Contracts to External End Point Groups (EPGs)
- [aci_l3out_extsubnet module](aci_l3out_extsubnet_module.md#ansible-collections-cisco-aci-aci-l3out-extsubnet-module) – Manage External Subnet objects (l3extSubnet:extsubnet)
- [aci_l3out_interface module](aci_l3out_interface_module.md#ansible-collections-cisco-aci-aci-l3out-interface-module) – Manage Layer 3 Outside (L3Out) interfaces (l3ext:RsPathL3OutAtt)
- [aci_l3out_interface_secondary_ip module](aci_l3out_interface_secondary_ip_module.md#ansible-collections-cisco-aci-aci-l3out-interface-secondary-ip-module) – Manage Layer 3 Outside (L3Out) interface secondary IP addresses (l3ext:Ip).
- [aci_l3out_logical_interface_profile module](aci_l3out_logical_interface_profile_module.md#ansible-collections-cisco-aci-aci-l3out-logical-interface-profile-module) – Manage Layer 3 Outside (L3Out) logical interface profiles (l3ext:LIfP)
- [aci_l3out_logical_interface_profile_ospf_policy module](aci_l3out_logical_interface_profile_ospf_policy_module.md#ansible-collections-cisco-aci-aci-l3out-logical-interface-profile-ospf-policy-module) – Manage Layer 3 Outside (L3Out) logical interface profile (l3ext:LIfP) OSPF policy (ospfIfP)
- [aci_l3out_logical_interface_vpc_member module](aci_l3out_logical_interface_vpc_member_module.md#ansible-collections-cisco-aci-aci-l3out-logical-interface-vpc-member-module) – Manage Member Node objects (l3ext:Member)
- [aci_l3out_logical_node module](aci_l3out_logical_node_module.md#ansible-collections-cisco-aci-aci-l3out-logical-node-module) – Manage Layer 3 Outside (L3Out) logical node profile nodes (l3ext:RsNodeL3OutAtt)
- [aci_l3out_logical_node_profile module](aci_l3out_logical_node_profile_module.md#ansible-collections-cisco-aci-aci-l3out-logical-node-profile-module) – Manage Layer 3 Outside (L3Out) logical node profiles (l3ext:LNodeP)
- [aci_l3out_route_tag_policy module](aci_l3out_route_tag_policy_module.md#ansible-collections-cisco-aci-aci-l3out-route-tag-policy-module) – Manage route tag policies (l3ext:RouteTagPol)
- [aci_l3out_static_routes module](aci_l3out_static_routes_module.md#ansible-collections-cisco-aci-aci-l3out-static-routes-module) – Manage Static routes object (l3ext:ipRouteP)
- [aci_l3out_static_routes_nexthop module](aci_l3out_static_routes_nexthop_module.md#ansible-collections-cisco-aci-aci-l3out-static-routes-nexthop-module) – Manage nexthops for static routes (ip:NexthopP)
- [aci_maintenance_group module](aci_maintenance_group_module.md#ansible-collections-cisco-aci-aci-maintenance-group-module) – This creates an ACI maintenance group (maint:MaintGrp)
- [aci_maintenance_group_node module](aci_maintenance_group_node_module.md#ansible-collections-cisco-aci-aci-maintenance-group-node-module) – Manage maintenance group nodes (fabric:NodeBlk)
- [aci_maintenance_policy module](aci_maintenance_policy_module.md#ansible-collections-cisco-aci-aci-maintenance-policy-module) – Manage firmware maintenance policies (maint:MaintP)
- [aci_match_as_path_regex_term module](aci_match_as_path_regex_term_module.md#ansible-collections-cisco-aci-aci-match-as-path-regex-term-module) – Manage Match Regular Expression AS-Path Term (rtctrl:MatchAsPathRegexTerm)
- [aci_match_community_factor module](aci_match_community_factor_module.md#ansible-collections-cisco-aci-aci-match-community-factor-module) – Manage Match Community Factor (rtctrl:MatchCommFactor)
- [aci_match_community_regex_term module](aci_match_community_regex_term_module.md#ansible-collections-cisco-aci-aci-match-community-regex-term-module) – Manage Match Regular Expression Community Term (rtctrl:MatchCommRegexTerm)
- [aci_match_community_term module](aci_match_community_term_module.md#ansible-collections-cisco-aci-aci-match-community-term-module) – Manage Match Community Term (rtctrl:MatchCommTerm)
- [aci_match_route_destination module](aci_match_route_destination_module.md#ansible-collections-cisco-aci-aci-match-route-destination-module) – Manage Match action rule term based on the Route Destination. (rtctrl:MatchRtDest)
- [aci_match_rule module](aci_match_rule_module.md#ansible-collections-cisco-aci-aci-match-rule-module) – Manage Match Rule (rtcrtl:SubjP)
- [aci_node_mgmt_epg module](aci_node_mgmt_epg_module.md#ansible-collections-cisco-aci-aci-node-mgmt-epg-module) – In band or Out of band management EPGs
- [aci_ntp_policy module](aci_ntp_policy_module.md#ansible-collections-cisco-aci-aci-ntp-policy-module) – Manage NTP policies.
- [aci_ntp_server module](aci_ntp_server_module.md#ansible-collections-cisco-aci-aci-ntp-server-module) – Manage NTP servers.
- [aci_rest module](aci_rest_module.md#ansible-collections-cisco-aci-aci-rest-module) – Direct access to the Cisco APIC REST API
- [aci_route_control_context module](aci_route_control_context_module.md#ansible-collections-cisco-aci-aci-route-control-context-module) – Manage Route Control Context (rtcrtl:CtxP)
- [aci_route_control_profile module](aci_route_control_profile_module.md#ansible-collections-cisco-aci-aci-route-control-profile-module) – Manage Route Control Profile (rtcrtl:Profile)
- [aci_snmp_client module](aci_snmp_client_module.md#ansible-collections-cisco-aci-aci-snmp-client-module) – Manage SNMP clients (<snmp:ClientP>).
- [aci_snmp_client_group module](aci_snmp_client_group_module.md#ansible-collections-cisco-aci-aci-snmp-client-group-module) – Manage SNMP client groups (<snmp:ClientGrpP>).
- [aci_snmp_community_policy module](aci_snmp_community_policy_module.md#ansible-collections-cisco-aci-aci-snmp-community-policy-module) – Manage SNMP community policies (<snmp:CommunityP>).
- [aci_snmp_policy module](aci_snmp_policy_module.md#ansible-collections-cisco-aci-aci-snmp-policy-module) – Manage Syslog groups (<snmp:Pol>).
- [aci_snmp_user module](aci_snmp_user_module.md#ansible-collections-cisco-aci-aci-snmp-user-module) – Manage SNMP v3 Users (<snmp:UserP>).
- [aci_static_binding_to_epg module](aci_static_binding_to_epg_module.md#ansible-collections-cisco-aci-aci-static-binding-to-epg-module) – Bind static paths to EPGs (fv:RsPathAtt)
- [aci_static_node_mgmt_address module](aci_static_node_mgmt_address_module.md#ansible-collections-cisco-aci-aci-static-node-mgmt-address-module) – In band or Out of band management IP address
- [aci_switch_leaf_selector module](aci_switch_leaf_selector_module.md#ansible-collections-cisco-aci-aci-switch-leaf-selector-module) – Bind leaf selectors to switch policy leaf profiles (infra:LeafS, infra:NodeBlk, infra:RsAccNodePGrep)
- [aci_switch_policy_leaf_profile module](aci_switch_policy_leaf_profile_module.md#ansible-collections-cisco-aci-aci-switch-policy-leaf-profile-module) – Manage switch policy leaf profiles (infra:NodeP)
- [aci_switch_policy_vpc_protection_group module](aci_switch_policy_vpc_protection_group_module.md#ansible-collections-cisco-aci-aci-switch-policy-vpc-protection-group-module) – Manage switch policy explicit vPC protection groups (fabric:ExplicitGEp, fabric:NodePEp).
- [aci_syslog_group module](aci_syslog_group_module.md#ansible-collections-cisco-aci-aci-syslog-group-module) – Manage Syslog groups (syslog:Group, syslog:Console, syslog:File and syslog:Prof).
- [aci_syslog_remote_dest module](aci_syslog_remote_dest_module.md#ansible-collections-cisco-aci-aci-syslog-remote-dest-module) – Manage Syslog Remote Destinations (syslog:RemoteDest).
- [aci_syslog_source module](aci_syslog_source_module.md#ansible-collections-cisco-aci-aci-syslog-source-module) – Manage Syslog Source objects (syslog:Src)
- [aci_system module](aci_system_module.md#ansible-collections-cisco-aci-aci-system-module) – Query the ACI system information (top:System)
- [aci_system_banner module](aci_system_banner_module.md#ansible-collections-cisco-aci-aci-system-banner-module) – Manages Alias and Banners (aaa:PreLoginBanner)
- [aci_system_endpoint_controls module](aci_system_endpoint_controls_module.md#ansible-collections-cisco-aci-aci-system-endpoint-controls-module) – Manage System Endpoint Controls (ep:IpAgingP, ep:ControlP, and ep:LoopProtectP)
- [aci_system_global_aes_passphrase_encryption module](aci_system_global_aes_passphrase_encryption_module.md#ansible-collections-cisco-aci-aci-system-global-aes-passphrase-encryption-module) – Manage Global AES Passphrase Encryption Settings (pki:ExportEncryptionKey)
- [aci_taboo_contract module](aci_taboo_contract_module.md#ansible-collections-cisco-aci-aci-taboo-contract-module) – Manage taboo contracts (vz:BrCP)
- [aci_tag module](aci_tag_module.md#ansible-collections-cisco-aci-aci-tag-module) – Tagging of ACI objects
- [aci_tenant module](aci_tenant_module.md#ansible-collections-cisco-aci-aci-tenant-module) – Manage tenants (fv:Tenant)
- [aci_tenant_action_rule_profile module](aci_tenant_action_rule_profile_module.md#ansible-collections-cisco-aci-aci-tenant-action-rule-profile-module) – Manage action rule profiles (rtctrl:AttrP)
- [aci_tenant_ep_retention_policy module](aci_tenant_ep_retention_policy_module.md#ansible-collections-cisco-aci-aci-tenant-ep-retention-policy-module) – Manage End Point (EP) retention protocol policies (fv:EpRetPol)
- [aci_tenant_span_dst_group module](aci_tenant_span_dst_group_module.md#ansible-collections-cisco-aci-aci-tenant-span-dst-group-module) – Manage SPAN destination groups (span:DestGrp)
- [aci_tenant_span_src_group module](aci_tenant_span_src_group_module.md#ansible-collections-cisco-aci-aci-tenant-span-src-group-module) – Manage SPAN source groups (span:SrcGrp)
- [aci_tenant_span_src_group_src module](aci_tenant_span_src_group_src_module.md#ansible-collections-cisco-aci-aci-tenant-span-src-group-src-module) – Manage SPAN source group sources (span:Src)
- [aci_tenant_span_src_group_to_dst_group module](aci_tenant_span_src_group_to_dst_group_module.md#ansible-collections-cisco-aci-aci-tenant-span-src-group-to-dst-group-module) – Bind SPAN source groups to destination groups (span:SpanLbl)
- [aci_vlan_pool module](aci_vlan_pool_module.md#ansible-collections-cisco-aci-aci-vlan-pool-module) – Manage VLAN pools (fvns:VlanInstP)
- [aci_vlan_pool_encap_block module](aci_vlan_pool_encap_block_module.md#ansible-collections-cisco-aci-aci-vlan-pool-encap-block-module) – Manage encap blocks assigned to VLAN pools (fvns:EncapBlk)
- [aci_vmm_controller module](aci_vmm_controller_module.md#ansible-collections-cisco-aci-aci-vmm-controller-module) – Manage VMM Controller for virtual domains profiles (vmm:CtrlrP)
- [aci_vmm_credential module](aci_vmm_credential_module.md#ansible-collections-cisco-aci-aci-vmm-credential-module) – Manage virtual domain credential profiles (vmm:UsrAccP)
- [aci_vmm_uplink module](aci_vmm_uplink_module.md#ansible-collections-cisco-aci-aci-vmm-uplink-module) – Manage VMM uplinks (vmm:UplinkP)
- [aci_vmm_uplink_container module](aci_vmm_uplink_container_module.md#ansible-collections-cisco-aci-aci-vmm-uplink-container-module) – Manage VMM uplink containers (vmm:UplinkPCont)
- [aci_vmm_vswitch_policy module](aci_vmm_vswitch_policy_module.md#ansible-collections-cisco-aci-aci-vmm-vswitch-policy-module) – Manage vSwitch policy for VMware virtual domains profiles (vmm:DomP)
- [aci_vrf module](aci_vrf_module.md#ansible-collections-cisco-aci-aci-vrf-module) – Manage contexts or VRFs (fv:Ctx)
- [aci_vrf_leak_internal_subnet module](aci_vrf_leak_internal_subnet_module.md#ansible-collections-cisco-aci-aci-vrf-leak-internal-subnet-module) – Manage VRF leaking of subnets (fv:leakInternalSubnet)
- [aci_vzany_to_contract module](aci_vzany_to_contract_module.md#ansible-collections-cisco-aci-aci-vzany-to-contract-module) – Attach contracts to vzAny (vz:RsAnyToProv, vz:RsAnyToCons, vz:RsAnyToConsIf)

### Httpapi Plugins

- [aci httpapi](aci_httpapi.md#ansible-collections-cisco-aci-aci-httpapi) – Ansible ACI HTTPAPI Plugin.

### Lookup Plugins

- [interface_range lookup](interface_range_lookup.md#ansible-collections-cisco-aci-interface-range-lookup) – query interfaces from a range or comma separated list of ranges

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
