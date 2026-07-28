---
collection: ansible
version: "6"
title: "Cisco.Meraki"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/index.html
fetched_at: 2026-07-27T16:41:38+00:00
---
# Cisco.Meraki

Collection version 2.13.0

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

An Ansible collection for managing the Cisco Meraki Dashboard

**Author:**

- Kevin Breit

**Supported ansible-core versions:**

- 2.10 or newer

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)

## [Plugin Index](index.md#id2)

These are the plugins in the cisco.meraki collection:

### Modules

- [meraki_action_batch module](meraki_action_batch_module.md#ansible-collections-cisco-meraki-meraki-action-batch-module) – Manage Action Batch jobs within the Meraki Dashboard.
- [meraki_admin module](meraki_admin_module.md#ansible-collections-cisco-meraki-meraki-admin-module) – Manage administrators in the Meraki cloud
- [meraki_alert module](meraki_alert_module.md#ansible-collections-cisco-meraki-meraki-alert-module) – Manage alerts in the Meraki cloud
- [meraki_config_template module](meraki_config_template_module.md#ansible-collections-cisco-meraki-meraki-config-template-module) – Manage configuration templates in the Meraki cloud
- [meraki_device module](meraki_device_module.md#ansible-collections-cisco-meraki-meraki-device-module) – Manage devices in the Meraki cloud
- [meraki_firewalled_services module](meraki_firewalled_services_module.md#ansible-collections-cisco-meraki-meraki-firewalled-services-module) – Edit firewall policies for administrative network services
- [meraki_management_interface module](meraki_management_interface_module.md#ansible-collections-cisco-meraki-meraki-management-interface-module) – Configure Meraki management interfaces
- [meraki_mr_l3_firewall module](meraki_mr_l3_firewall_module.md#ansible-collections-cisco-meraki-meraki-mr-l3-firewall-module) – Manage MR access point layer 3 firewalls in the Meraki cloud
- [meraki_mr_l7_firewall module](meraki_mr_l7_firewall_module.md#ansible-collections-cisco-meraki-meraki-mr-l7-firewall-module) – Manage MR access point layer 7 firewalls in the Meraki cloud
- [meraki_mr_radio module](meraki_mr_radio_module.md#ansible-collections-cisco-meraki-meraki-mr-radio-module) – Manage device radio settings for Meraki wireless networks
- [meraki_mr_rf_profile module](meraki_mr_rf_profile_module.md#ansible-collections-cisco-meraki-meraki-mr-rf-profile-module) – Manage RF profiles for Meraki wireless networks
- [meraki_mr_settings module](meraki_mr_settings_module.md#ansible-collections-cisco-meraki-meraki-mr-settings-module) – Manage general settings for Meraki wireless networks
- [meraki_mr_ssid module](meraki_mr_ssid_module.md#ansible-collections-cisco-meraki-meraki-mr-ssid-module) – Manage wireless SSIDs in the Meraki cloud
- [meraki_ms_access_list module](meraki_ms_access_list_module.md#ansible-collections-cisco-meraki-meraki-ms-access-list-module) – Manage access lists for Meraki switches in the Meraki cloud
- [meraki_ms_access_policies module](meraki_ms_access_policies_module.md#ansible-collections-cisco-meraki-meraki-ms-access-policies-module) – Manage Switch Access Policies in the Meraki cloud
- [meraki_ms_l3_interface module](meraki_ms_l3_interface_module.md#ansible-collections-cisco-meraki-meraki-ms-l3-interface-module) – Manage routed interfaces on MS switches
- [meraki_ms_link_aggregation module](meraki_ms_link_aggregation_module.md#ansible-collections-cisco-meraki-meraki-ms-link-aggregation-module) – Manage link aggregations on MS switches
- [meraki_ms_ospf module](meraki_ms_ospf_module.md#ansible-collections-cisco-meraki-meraki-ms-ospf-module) – Manage OSPF configuration on MS switches
- [meraki_ms_stack module](meraki_ms_stack_module.md#ansible-collections-cisco-meraki-meraki-ms-stack-module) – Modify switch stacking configuration in Meraki.
- [meraki_ms_stack_l3_interface module](meraki_ms_stack_l3_interface_module.md#ansible-collections-cisco-meraki-meraki-ms-stack-l3-interface-module) – Manage routed interfaces on MS switches
- [meraki_ms_storm_control module](meraki_ms_storm_control_module.md#ansible-collections-cisco-meraki-meraki-ms-storm-control-module) – Manage storm control configuration on a switch in the Meraki cloud
- [meraki_ms_switchport module](meraki_ms_switchport_module.md#ansible-collections-cisco-meraki-meraki-ms-switchport-module) – Manage switchports on a switch in the Meraki cloud
- [meraki_mx_content_filtering module](meraki_mx_content_filtering_module.md#ansible-collections-cisco-meraki-meraki-mx-content-filtering-module) – Edit Meraki MX content filtering policies
- [meraki_mx_intrusion_prevention module](meraki_mx_intrusion_prevention_module.md#ansible-collections-cisco-meraki-meraki-mx-intrusion-prevention-module) – Manage intrustion prevention in the Meraki cloud
- [meraki_mx_l2_interface module](meraki_mx_l2_interface_module.md#ansible-collections-cisco-meraki-meraki-mx-l2-interface-module) – Configure MX layer 2 interfaces
- [meraki_mx_l3_firewall module](meraki_mx_l3_firewall_module.md#ansible-collections-cisco-meraki-meraki-mx-l3-firewall-module) – Manage MX appliance layer 3 firewalls in the Meraki cloud
- [meraki_mx_l7_firewall module](meraki_mx_l7_firewall_module.md#ansible-collections-cisco-meraki-meraki-mx-l7-firewall-module) – Manage MX appliance layer 7 firewalls in the Meraki cloud
- [meraki_mx_malware module](meraki_mx_malware_module.md#ansible-collections-cisco-meraki-meraki-mx-malware-module) – Manage Malware Protection in the Meraki cloud
- [meraki_mx_nat module](meraki_mx_nat_module.md#ansible-collections-cisco-meraki-meraki-mx-nat-module) – Manage NAT rules in Meraki cloud
- [meraki_mx_network_vlan_settings module](meraki_mx_network_vlan_settings_module.md#ansible-collections-cisco-meraki-meraki-mx-network-vlan-settings-module) – Manage VLAN settings for Meraki Networks
- [meraki_mx_site_to_site_firewall module](meraki_mx_site_to_site_firewall_module.md#ansible-collections-cisco-meraki-meraki-mx-site-to-site-firewall-module) – Manage MX appliance firewall rules for site-to-site VPNs
- [meraki_mx_site_to_site_vpn module](meraki_mx_site_to_site_vpn_module.md#ansible-collections-cisco-meraki-meraki-mx-site-to-site-vpn-module) – Manage AutoVPN connections in Meraki
- [meraki_mx_static_route module](meraki_mx_static_route_module.md#ansible-collections-cisco-meraki-meraki-mx-static-route-module) – Manage static routes in the Meraki cloud
- [meraki_mx_third_party_vpn_peers module](meraki_mx_third_party_vpn_peers_module.md#ansible-collections-cisco-meraki-meraki-mx-third-party-vpn-peers-module) – Manage third party (IPSec) VPN peers for MX devices
- [meraki_mx_uplink_bandwidth module](meraki_mx_uplink_bandwidth_module.md#ansible-collections-cisco-meraki-meraki-mx-uplink-bandwidth-module) – Manage uplinks on Meraki MX appliances
- [meraki_mx_vlan module](meraki_mx_vlan_module.md#ansible-collections-cisco-meraki-meraki-mx-vlan-module) – Manage VLANs in the Meraki cloud
- [meraki_network module](meraki_network_module.md#ansible-collections-cisco-meraki-meraki-network-module) – Manage networks in the Meraki cloud
- [meraki_organization module](meraki_organization_module.md#ansible-collections-cisco-meraki-meraki-organization-module) – Manage organizations in the Meraki cloud
- [meraki_snmp module](meraki_snmp_module.md#ansible-collections-cisco-meraki-meraki-snmp-module) – Manage organizations in the Meraki cloud
- [meraki_syslog module](meraki_syslog_module.md#ansible-collections-cisco-meraki-meraki-syslog-module) – Manage syslog server settings in the Meraki cloud.
- [meraki_webhook module](meraki_webhook_module.md#ansible-collections-cisco-meraki-meraki-webhook-module) – Manage webhooks configured in the Meraki cloud
- [meraki_webhook_payload_template module](meraki_webhook_payload_template_module.md#ansible-collections-cisco-meraki-meraki-webhook-payload-template-module) – Manage webhook payload templates for a network in the Meraki cloud

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
