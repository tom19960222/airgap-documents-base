---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_monitor_fact module – Retrieve Facts of FortiOS Monitor Objects."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_monitor_fact_module.html
fetched_at: 2026-07-27T17:42:48+00:00
---
# fortinet.fortios.fortios_monitor_fact module – Retrieve Facts of FortiOS Monitor Objects.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_monitor_fact_module.md#ansible-collections-fortinet-fortios-fortios-monitor-fact-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_monitor_fact`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_monitor_fact_module.md#synopsis)
- [Requirements](fortios_monitor_fact_module.md#requirements)
- [Parameters](fortios_monitor_fact_module.md#parameters)
- [Notes](fortios_monitor_fact_module.md#notes)
- [Examples](fortios_monitor_fact_module.md#examples)
- [Return Values](fortios_monitor_fact_module.md#return-values)

## [Synopsis](fortios_monitor_fact_module.md#id1)

- Collects monitor facts from network devices running the fortios operating system. This facts module will only collect those facts which user specified in playbook.

## [Requirements](fortios_monitor_fact_module.md#id2)

The below requirements are needed on the host that executes this module.

- install galaxy collection fortinet.fortios >= 2.0.0.

## [Parameters](fortios_monitor_fact_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **filters**  list / elements=string | A list of expressions to filter the returned results.  The items of the list are combined as LOGICAL AND with operator ampersand.  One item itself could be concatenated with a comma as LOGICAL OR. |
| **formatters**  list / elements=string | A list of fields to display for returned results. |
| **params**  dictionary | the parameter for each selector, see definition in above list. |
| **selector**  string | selector of the retrieved fortiOS facts.  Choices:   - `"endpoint-control_profile_xml"` - `"endpoint-control_record-list"` - `"endpoint-control_registration_summary"` - `"endpoint-control_installer"` - `"endpoint-control_installer_download"` - `"endpoint-control_avatar_download"` - `"firewall_health"` - `"firewall_local-in"` - `"firewall_acl"` - `"firewall_acl6"` - `"firewall_internet-service-match"` - `"firewall_internet-service-details"` - `"firewall_policy"` - `"firewall_policy6"` - `"firewall_proxy-policy"` - `"firewall_policy-lookup"` - `"firewall_session"` - `"firewall_shaper"` - `"firewall_per-ip-shaper"` - `"firewall_load-balance"` - `"firewall_address-fqdns"` - `"firewall_address-fqdns6"` - `"firewall_ippool"` - `"firewall_address-dynamic"` - `"firewall_address6-dynamic"` - `"fortiview_statistics"` - `"fortiview_sandbox-file-details"` - `"geoip_geoip-query"` - `"ips_rate-based"` - `"license_status"` - `"license_forticare-resellers"` - `"license_forticare-org-list"` - `"log_current-disk-usage"` - `"log_device_state"` - `"log_forticloud"` - `"log_fortianalyzer"` - `"log_fortianalyzer-queue"` - `"log_hourly-disk-usage"` - `"log_historic-daily-remote-logs"` - `"log_stats"` - `"log_forticloud-report_download"` - `"log_ips-archive_download"` - `"log_policy-archive_download"` - `"log_av-archive_download"` - `"log_event"` - `"registration_forticloud_disclaimer"` - `"registration_forticloud_domains"` - `"router_ipv4"` - `"router_ipv6"` - `"router_statistics"` - `"router_lookup"` - `"router_policy"` - `"router_policy6"` - `"system_config-revision"` - `"system_config-revision_file"` - `"system_config-revision_info"` - `"system_current-admins"` - `"system_time"` - `"system_global-resources"` - `"system_vdom-resource"` - `"system_dhcp"` - `"system_firmware"` - `"system_firmware_upgrade-paths"` - `"system_storage"` - `"system_csf"` - `"system_csf_pending-authorizations"` - `"system_modem"` - `"system_3g-modem"` - `"system_resource_usage"` - `"system_sniffer"` - `"system_sniffer_download"` - `"system_automation-stitch_stats"` - `"switch-controller_managed-switch"` - `"switch-controller_managed-switch_faceplate-xml"` - `"switch-controller_managed-switch_dhcp-snooping"` - `"switch-controller_fsw-firmware"` - `"switch-controller_detected-device"` - `"switch-controller_validate-switch-prefix"` - `"system_interface"` - `"system_interface_dhcp-status"` - `"system_available-interfaces"` - `"system_acquired-dns"` - `"system_resolve-fqdn"` - `"system_nat46-ippools"` - `"system_usb-log"` - `"system_ipconf"` - `"system_fortiguard_server-info"` - `"system_fortimanager_status"` - `"system_fortimanager_backup-summary"` - `"system_fortimanager_backup-details"` - `"system_available-certificates"` - `"system_certificate_download"` - `"system_debug_download"` - `"system_com-log_update"` - `"system_com-log_download"` - `"system_botnet_stat"` - `"system_botnet"` - `"system_botnet-domains"` - `"system_botnet-domains_stat"` - `"system_botnet-domains_hits"` - `"system_ha-statistics"` - `"system_ha-history"` - `"system_ha-checksums"` - `"system_ha-peer"` - `"system_link-monitor"` - `"system_config_backup"` - `"system_config_usb-filelist"` - `"system_sandbox_stats"` - `"system_sandbox_status"` - `"system_sandbox_test-connect"` - `"system_object_usage"` - `"system_object-tagging_usage"` - `"system_status"` - `"system_timezone"` - `"system_sensor-info"` - `"system_security-rating"` - `"system_security-rating_history"` - `"system_security-rating_status"` - `"system_security-rating_lang"` - `"system_fortiguard-blacklist"` - `"system_check-port-availability"` - `"system_external-resource_entry-list"` - `"extender-controller_extender"` - `"system_sdn-connector_status"` - `"user_firewall"` - `"user_banned"` - `"user_fortitoken"` - `"user_detected-device"` - `"user_device"` - `"user_device-type"` - `"user_device-category"` - `"user_fsso"` - `"utm_rating-lookup"` - `"utm_app-lookup"` - `"utm_application-categories"` - `"utm_antivirus_stats"` - `"virtual-wan_health-check"` - `"virtual-wan_members"` - `"webfilter_override"` - `"webfilter_malicious-urls"` - `"webfilter_malicious-urls_stat"` - `"webfilter_category-quota"` - `"webfilter_fortiguard-categories"` - `"webfilter_trusted-urls"` - `"vpn_ipsec"` - `"vpn_one-click_members"` - `"vpn_one-click_status"` - `"vpn_ssl"` - `"vpn_ssl_stats"` - `"wanopt_history"` - `"wanopt_webcache"` - `"wanopt_peer_stats"` - `"webproxy_pacfile_download"` - `"webcache_stats"` - `"wifi_client"` - `"wifi_managed_ap"` - `"wifi_firmware"` - `"wifi_ap_status"` - `"wifi_interfering_ap"` - `"wifi_euclid"` - `"wifi_rogue_ap"` - `"wifi_spectrum"` - `"endpoint-control_summary"` - `"endpoint-control_ems_status"` - `"firewall_consolidated-policy"` - `"firewall_security-policy"` - `"firewall_uuid-list"` - `"firewall_uuid-type-lookup"` - `"fortiguard_redirect-portal"` - `"firewall_sdn-connector-filters"` - `"fortiview_sandbox-file-list"` - `"ips_metadata"` - `"ips_anomaly"` - `"license_fortianalyzer-status"` - `"log_forticloud-report-list"` - `"log_local-report-list"` - `"log_local-report_download"` - `"network_lldp_neighbors"` - `"network_lldp_ports"` - `"network_dns_latency"` - `"network_fortiguard_live-services-latency"` - `"network_ddns_servers"` - `"network_ddns_lookup"` - `"router_lookup-policy"` - `"system_config-script"` - `"system_config-sync_status"` - `"system_vdom-link"` - `"switch-controller_managed-switch_transceivers"` - `"system_interface_poe"` - `"system_trusted-cert-authorities"` - `"system_sandbox_cloud-regions"` - `"system_interface_transceivers"` - `"system_vm-information"` - `"system_security-rating_supported-reports"` - `"nsx_service_status"` - `"nsx_instance"` - `"system_sdn-connector_nsx-security-tags"` - `"web-ui_custom-language_download"` - `"user_collected-email"` - `"user_info_query"` - `"user_info_thumbnail"` - `"utm_blacklisted-certificates"` - `"utm_blacklisted-certificates_statistics"` - `"virtual-wan_interface-log"` - `"virtual-wan_sla-log"` - `"vpn_ocvpn_members"` - `"vpn_ocvpn_status"` - `"vpn_ocvpn_meta"` - `"wifi_network_list"` - `"wifi_network_status"` - `"wifi_region-image"` - `"azure_application-list"` - `"endpoint-control_ems_cert-status"` - `"endpoint-control_ems_status-summary"` - `"fortiguard_service-communication-stats"` - `"network_reverse-ip-lookup"` - `"registration_forticloud_device-status"` - `"switch-controller_managed-switch_health"` - `"switch-controller_managed-switch_cable-status"` - `"switch-controller_mclag-icl_eligible-peer"` - `"system_interface_speed-test-status"` - `"user_fortitoken-cloud_status"` - `"wifi_vlan-probe"` - `"firewall_ippool_mapping"` - `"network_arp"` - `"system_interface-connected-admins-info"` - `"system_ntp_status"` - `"system_config-error-log_download"` - `"system_running-processes"` - `"user_device_query"` - `"ips_exceed-scan-range"` - `"firewall_multicast-policy"` - `"firewall_multicast-policy6"` - `"firewall_gtp-statistics"` - `"firewall_gtp-runtime-statistics"` - `"router_bgp_neighbors"` - `"router_bgp_neighbors6"` - `"router_bgp_paths"` - `"router_bgp_paths6"` - `"router_ospf_neighbors"` - `"system_automation-action_stats"` - `"switch-controller_matched-devices"` - `"system_ha-table-checksums"` - `"system_sandbox_connection"` - `"system_traffic-history_interface"` - `"system_traffic-history_top-applications"` - `"videofilter_fortiguard-categories"` - `"firewall_central-snat-map"` - `"firewall_dnat"` - `"ips_hold-signatures"` - `"router_bgp_paths-statistics"` - `"system_lte-modem_status"` - `"system_global-search"` - `"switch-controller_managed-switch_status"` - `"switch-controller_managed-switch_port-stats"` - `"switch-controller_managed-switch_models"` - `"system_interface_kernel-interfaces"` - `"system_config_restore-status"` - `"wifi_meta"` - `"wifi_ap_channels"` - `"wifi_ap-names"` - `"firewall_internet-service-reputation"` - `"firewall_shaper_multi-class-shaper"` - `"log_forticloud_connection"` - `"system_performance_status"` - `"system_ipam_list"` - `"system_ipam_status"` - `"system_acme-certificate-status"` - `"system_crash-log_download"` - `"user_banned_check"` - `"user_info_thumbnail-file"` - `"vpn-certificate_cert-name-available"` - `"wifi_unassociated-devices"` - `"wifi_matched-devices"` - `"firewall_proxy_sessions"` - `"firewall_gtp"` - `"fortiview_proxy-statistics"` - `"system_ha-hw-interface"` - `"user_firewall_count"` - `"firewall_internet-service-basic"` - `"firewall_vip-overlap"` - `"switch-controller_managed-switch_port-health"` - `"switch-controller_managed-switch_tx-rx"` - `"firewall_network-service-dynamic"` - `"system_ipam_utilization"` - `"system_ha-nonsync-checksums"` - `"wifi_station-capability"` |
| **selectors**  list / elements=dictionary | A list of selectors for retrieving the fortiOS facts. |
| **filters**  list / elements=string | A list of expressions to filter the returned results.  The items of the list are combined as LOGICAL AND with operator ampersand.  One item itself could be concatenated with a comma as LOGICAL OR. |
| **formatters**  list / elements=string | A list of fields to display for returned results. |
| **params**  dictionary | the parameter for each selector, see definition in above list. |
| **selector**  string / required | selector of the retrieved fortiOS facts  Choices:   - `"endpoint-control_profile_xml"` - `"endpoint-control_record-list"` - `"endpoint-control_registration_summary"` - `"endpoint-control_installer"` - `"endpoint-control_installer_download"` - `"endpoint-control_avatar_download"` - `"firewall_health"` - `"firewall_local-in"` - `"firewall_acl"` - `"firewall_acl6"` - `"firewall_internet-service-match"` - `"firewall_internet-service-details"` - `"firewall_policy"` - `"firewall_policy6"` - `"firewall_proxy-policy"` - `"firewall_policy-lookup"` - `"firewall_session"` - `"firewall_shaper"` - `"firewall_per-ip-shaper"` - `"firewall_load-balance"` - `"firewall_address-fqdns"` - `"firewall_address-fqdns6"` - `"firewall_ippool"` - `"firewall_address-dynamic"` - `"firewall_address6-dynamic"` - `"fortiview_statistics"` - `"fortiview_sandbox-file-details"` - `"geoip_geoip-query"` - `"ips_rate-based"` - `"license_status"` - `"license_forticare-resellers"` - `"license_forticare-org-list"` - `"log_current-disk-usage"` - `"log_device_state"` - `"log_forticloud"` - `"log_fortianalyzer"` - `"log_fortianalyzer-queue"` - `"log_hourly-disk-usage"` - `"log_historic-daily-remote-logs"` - `"log_stats"` - `"log_forticloud-report_download"` - `"log_ips-archive_download"` - `"log_policy-archive_download"` - `"log_av-archive_download"` - `"log_event"` - `"registration_forticloud_disclaimer"` - `"registration_forticloud_domains"` - `"router_ipv4"` - `"router_ipv6"` - `"router_statistics"` - `"router_lookup"` - `"router_policy"` - `"router_policy6"` - `"system_config-revision"` - `"system_config-revision_file"` - `"system_config-revision_info"` - `"system_current-admins"` - `"system_time"` - `"system_global-resources"` - `"system_vdom-resource"` - `"system_dhcp"` - `"system_firmware"` - `"system_firmware_upgrade-paths"` - `"system_storage"` - `"system_csf"` - `"system_csf_pending-authorizations"` - `"system_modem"` - `"system_3g-modem"` - `"system_resource_usage"` - `"system_sniffer"` - `"system_sniffer_download"` - `"system_automation-stitch_stats"` - `"switch-controller_managed-switch"` - `"switch-controller_managed-switch_faceplate-xml"` - `"switch-controller_managed-switch_dhcp-snooping"` - `"switch-controller_fsw-firmware"` - `"switch-controller_detected-device"` - `"switch-controller_validate-switch-prefix"` - `"system_interface"` - `"system_interface_dhcp-status"` - `"system_available-interfaces"` - `"system_acquired-dns"` - `"system_resolve-fqdn"` - `"system_nat46-ippools"` - `"system_usb-log"` - `"system_ipconf"` - `"system_fortiguard_server-info"` - `"system_fortimanager_status"` - `"system_fortimanager_backup-summary"` - `"system_fortimanager_backup-details"` - `"system_available-certificates"` - `"system_certificate_download"` - `"system_debug_download"` - `"system_com-log_update"` - `"system_com-log_download"` - `"system_botnet_stat"` - `"system_botnet"` - `"system_botnet-domains"` - `"system_botnet-domains_stat"` - `"system_botnet-domains_hits"` - `"system_ha-statistics"` - `"system_ha-history"` - `"system_ha-checksums"` - `"system_ha-peer"` - `"system_link-monitor"` - `"system_config_backup"` - `"system_config_usb-filelist"` - `"system_sandbox_stats"` - `"system_sandbox_status"` - `"system_sandbox_test-connect"` - `"system_object_usage"` - `"system_object-tagging_usage"` - `"system_status"` - `"system_timezone"` - `"system_sensor-info"` - `"system_security-rating"` - `"system_security-rating_history"` - `"system_security-rating_status"` - `"system_security-rating_lang"` - `"system_fortiguard-blacklist"` - `"system_check-port-availability"` - `"system_external-resource_entry-list"` - `"extender-controller_extender"` - `"system_sdn-connector_status"` - `"user_firewall"` - `"user_banned"` - `"user_fortitoken"` - `"user_detected-device"` - `"user_device"` - `"user_device-type"` - `"user_device-category"` - `"user_fsso"` - `"utm_rating-lookup"` - `"utm_app-lookup"` - `"utm_application-categories"` - `"utm_antivirus_stats"` - `"virtual-wan_health-check"` - `"virtual-wan_members"` - `"webfilter_override"` - `"webfilter_malicious-urls"` - `"webfilter_malicious-urls_stat"` - `"webfilter_category-quota"` - `"webfilter_fortiguard-categories"` - `"webfilter_trusted-urls"` - `"vpn_ipsec"` - `"vpn_one-click_members"` - `"vpn_one-click_status"` - `"vpn_ssl"` - `"vpn_ssl_stats"` - `"wanopt_history"` - `"wanopt_webcache"` - `"wanopt_peer_stats"` - `"webproxy_pacfile_download"` - `"webcache_stats"` - `"wifi_client"` - `"wifi_managed_ap"` - `"wifi_firmware"` - `"wifi_ap_status"` - `"wifi_interfering_ap"` - `"wifi_euclid"` - `"wifi_rogue_ap"` - `"wifi_spectrum"` - `"endpoint-control_summary"` - `"endpoint-control_ems_status"` - `"firewall_consolidated-policy"` - `"firewall_security-policy"` - `"firewall_uuid-list"` - `"firewall_uuid-type-lookup"` - `"fortiguard_redirect-portal"` - `"firewall_sdn-connector-filters"` - `"fortiview_sandbox-file-list"` - `"ips_metadata"` - `"ips_anomaly"` - `"license_fortianalyzer-status"` - `"log_forticloud-report-list"` - `"log_local-report-list"` - `"log_local-report_download"` - `"network_lldp_neighbors"` - `"network_lldp_ports"` - `"network_dns_latency"` - `"network_fortiguard_live-services-latency"` - `"network_ddns_servers"` - `"network_ddns_lookup"` - `"router_lookup-policy"` - `"system_config-script"` - `"system_config-sync_status"` - `"system_vdom-link"` - `"switch-controller_managed-switch_transceivers"` - `"system_interface_poe"` - `"system_trusted-cert-authorities"` - `"system_sandbox_cloud-regions"` - `"system_interface_transceivers"` - `"system_vm-information"` - `"system_security-rating_supported-reports"` - `"nsx_service_status"` - `"nsx_instance"` - `"system_sdn-connector_nsx-security-tags"` - `"web-ui_custom-language_download"` - `"user_collected-email"` - `"user_info_query"` - `"user_info_thumbnail"` - `"utm_blacklisted-certificates"` - `"utm_blacklisted-certificates_statistics"` - `"virtual-wan_interface-log"` - `"virtual-wan_sla-log"` - `"vpn_ocvpn_members"` - `"vpn_ocvpn_status"` - `"vpn_ocvpn_meta"` - `"wifi_network_list"` - `"wifi_network_status"` - `"wifi_region-image"` - `"azure_application-list"` - `"endpoint-control_ems_cert-status"` - `"endpoint-control_ems_status-summary"` - `"fortiguard_service-communication-stats"` - `"network_reverse-ip-lookup"` - `"registration_forticloud_device-status"` - `"switch-controller_managed-switch_health"` - `"switch-controller_managed-switch_cable-status"` - `"switch-controller_mclag-icl_eligible-peer"` - `"system_interface_speed-test-status"` - `"user_fortitoken-cloud_status"` - `"wifi_vlan-probe"` - `"firewall_ippool_mapping"` - `"network_arp"` - `"system_interface-connected-admins-info"` - `"system_ntp_status"` - `"system_config-error-log_download"` - `"system_running-processes"` - `"user_device_query"` - `"ips_exceed-scan-range"` - `"firewall_multicast-policy"` - `"firewall_multicast-policy6"` - `"firewall_gtp-statistics"` - `"firewall_gtp-runtime-statistics"` - `"router_bgp_neighbors"` - `"router_bgp_neighbors6"` - `"router_bgp_paths"` - `"router_bgp_paths6"` - `"router_ospf_neighbors"` - `"system_automation-action_stats"` - `"switch-controller_matched-devices"` - `"system_ha-table-checksums"` - `"system_sandbox_connection"` - `"system_traffic-history_interface"` - `"system_traffic-history_top-applications"` - `"videofilter_fortiguard-categories"` - `"firewall_central-snat-map"` - `"firewall_dnat"` - `"ips_hold-signatures"` - `"router_bgp_paths-statistics"` - `"system_lte-modem_status"` - `"system_global-search"` - `"switch-controller_managed-switch_status"` - `"switch-controller_managed-switch_port-stats"` - `"switch-controller_managed-switch_models"` - `"system_interface_kernel-interfaces"` - `"system_config_restore-status"` - `"wifi_meta"` - `"wifi_ap_channels"` - `"wifi_ap-names"` - `"firewall_internet-service-reputation"` - `"firewall_shaper_multi-class-shaper"` - `"log_forticloud_connection"` - `"system_performance_status"` - `"system_ipam_list"` - `"system_ipam_status"` - `"system_acme-certificate-status"` - `"system_crash-log_download"` - `"user_banned_check"` - `"user_info_thumbnail-file"` - `"vpn-certificate_cert-name-available"` - `"wifi_unassociated-devices"` - `"wifi_matched-devices"` - `"firewall_proxy_sessions"` - `"firewall_gtp"` - `"fortiview_proxy-statistics"` - `"system_ha-hw-interface"` - `"user_firewall_count"` - `"firewall_internet-service-basic"` - `"firewall_vip-overlap"` - `"switch-controller_managed-switch_port-health"` - `"switch-controller_managed-switch_tx-rx"` - `"firewall_network-service-dynamic"` - `"system_ipam_utilization"` - `"system_ha-nonsync-checksums"` - `"wifi_station-capability"` |
| **sorters**  list / elements=string | A list of expressions to sort the returned results.  The items of the list are in ascending order with operator ampersand.  One item itself could be in decending order with a comma inside. |
| **sorters**  list / elements=string | A list of expressions to sort the returned results.  The items of the list are in ascending order with operator ampersand.  One item itself could be in decending order with a comma inside. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_monitor_fact_module.md#id4)

> **Note:**
>
> - Different selector may have different parameters, users are expected to look up them for a specific selector.
> - For some selectors, the objects are global, no params are allowed to appear.
> - Not all parameters are required for a slector.
> - This module is exclusivly for FortiOS monitor API.
> - The result of API request is stored in results.

## [Examples](fortios_monitor_fact_module.md#id5)

```yaml+jinja
- hosts: fortigate03
  connection: httpapi
  collections:
  - fortinet.fortios
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:

  - name: Get license shizzle
    fortios_monitor_fact:
      vdom: ""
      selectors:
        - selector: license_status
        - selector: system_status
        - selector: firewall_security-policy
          params:
            policyid: '1'

  - fortios_monitor_fact:
       vdom: ""
       formatters:
            - model_name
       filters:
            - model_name==FortiGat
       selector: 'system_status'

  - name: fact gathering
    fortios_monitor_fact:
       vdom: ""
       access_token: ""
       selector: 'firewall_acl'
```

## [Return Values](fortios_monitor_fact_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"GET"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"firmware"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"system"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@fshen01)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
