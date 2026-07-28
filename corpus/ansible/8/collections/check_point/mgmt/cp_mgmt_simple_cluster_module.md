---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_simple_cluster module – Manages simple-cluster objects on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_simple_cluster_module.html
fetched_at: 2026-07-28T01:17:56+00:00
---
# check_point.mgmt.cp_mgmt_simple_cluster module – Manages simple-cluster objects on Checkpoint over Web Services API

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/ui/repo/published/check_point/mgmt/) (version 5.1.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_simple_cluster`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_simple_cluster_module.md#synopsis)
- [Parameters](cp_mgmt_simple_cluster_module.md#parameters)
- [Examples](cp_mgmt_simple_cluster_module.md#examples)
- [Return Values](cp_mgmt_simple_cluster_module.md#return-values)

## [Synopsis](cp_mgmt_simple_cluster_module.md#id1)

- Manages simple-cluster objects on Checkpoint devices including creating, updating and removing objects.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_simple_cluster_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **anti_bot**  boolean | Anti-Bot blade enabled.  **Choices:**   - `false` - `true` |
| **anti_virus**  boolean | Anti-Virus blade enabled.  **Choices:**   - `false` - `true` |
| **application_control**  boolean | Application Control blade enabled.  **Choices:**   - `false` - `true` |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **cluster_mode**  string | Cluster mode.  **Choices:**   - `"cluster-xl-ha"` - `"cluster-ls-multicast"` - `"cluster-ls-unicast"` - `"opsec-ha"` - `"opsec-ls"` |
| **cluster_version**  string | Cluster platform version. |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **content_awareness**  boolean | Content Awareness blade enabled.  **Choices:**   - `false` - `true` |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **firewall**  boolean | Firewall blade enabled.  **Choices:**   - `false` - `true` |
| **firewall_settings**  dictionary | N/A |
| **auto_calculate_connections_hash_table_size_and_memory_pool**  boolean | N/A  **Choices:**   - `false` - `true` |
| **auto_maximum_limit_for_concurrent_connections**  boolean | N/A  **Choices:**   - `false` - `true` |
| **connections_hash_size**  integer | N/A |
| **maximum_limit_for_concurrent_connections**  integer | N/A |
| **maximum_memory_pool_size**  integer | N/A |
| **memory_pool_size**  integer | N/A |
| **groups**  list / elements=string | Collection of group identifiers. |
| **hardware**  string | Cluster platform hardware. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **interfaces**  list / elements=dictionary | N/A |
| **anti_spoofing**  boolean | N/A  **Choices:**   - `false` - `true` |
| **anti_spoofing_settings**  dictionary | N/A |
| **action**  string | If packets will be rejected (the Prevent option) or whether the packets will be monitored (the Detect option).  **Choices:**   - `"prevent"` - `"detect"` |
| **exclude_packets**  boolean | Don’t check packets from excluded network.  **Choices:**   - `false` - `true` |
| **excluded_network_name**  string | Excluded network name. |
| **excluded_network_uid**  string | Excluded network UID. |
| **spoof_tracking**  string | Spoof tracking.  **Choices:**   - `"none"` - `"log"` - `"alert"` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **interface_type**  string | Cluster interface type.  **Choices:**   - `"cluster"` - `"sync"` - `"cluster + sync"` - `"private"` |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. |
| **ipv4_address**  string | IPv4 address. |
| **ipv4_mask_length**  string | IPv4 network mask length. |
| **ipv4_network_mask**  string | IPv4 network address. |
| **ipv6_address**  string | IPv6 address. |
| **ipv6_mask_length**  string | IPv6 network mask length. |
| **ipv6_network_mask**  string | IPv6 network address. |
| **mask_length**  string | IPv4 or IPv6 network mask length. |
| **multicast_address**  string | Multicast IP Address. |
| **multicast_address_type**  string | Multicast Address Type.  **Choices:**   - `"manual"` - `"default"` |
| **name**  string | Object name. |
| **network_mask**  string | IPv4 or IPv6 network mask. If both masks are required use ipv4-network-mask and ipv6-network-mask fields explicitly. Instead of providing mask itself it is possible to specify IPv4 or IPv6 mask length in mask-length field. If both masks length are required use ipv4-mask-length and ipv6-mask-length fields explicitly. |
| **security_zone**  boolean | N/A  **Choices:**   - `false` - `true` |
| **security_zone_settings**  dictionary | N/A |
| **auto_calculated**  boolean | Security Zone is calculated according to where the interface leads to.  **Choices:**   - `false` - `true` |
| **specific_zone**  string | Security Zone specified manually. |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **topology**  string | N/A  **Choices:**   - `"automatic"` - `"external"` - `"internal"` |
| **topology_settings**  dictionary | N/A |
| **interface_leads_to_dmz**  boolean | Whether this interface leads to demilitarized zone (perimeter network).  **Choices:**   - `false` - `true` |
| **ip_address_behind_this_interface**  string | Network settings behind this interface.  **Choices:**   - `"not defined"` - `"network defined by the interface ip and net mask"` - `"network defined by routing"` - `"specific"` |
| **specific_network**  string | Network behind this interface. |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. |
| **ips**  boolean | Intrusion Prevention System blade enabled.  **Choices:**   - `false` - `true` |
| **ipv4_address**  string | IPv4 address. |
| **ipv6_address**  string | IPv6 address. |
| **members**  list / elements=dictionary | Cluster members list. Only new cluster member can be added. Adding existing gateway is not supported. |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **interfaces**  list / elements=dictionary | Cluster Member network interfaces. |
| **anti_spoofing**  boolean | N/A  **Choices:**   - `false` - `true` |
| **anti_spoofing_settings**  dictionary | N/A |
| **action**  string | If packets will be rejected (the Prevent option) or whether the packets will be monitored (the Detect option).  **Choices:**   - `"prevent"` - `"detect"` |
| **exclude_packets**  boolean | Don’t check packets from excluded network.  **Choices:**   - `false` - `true` |
| **excluded_network_name**  string | Excluded network name. |
| **excluded_network_uid**  string | Excluded network UID. |
| **spoof_tracking**  string | Spoof tracking.  **Choices:**   - `"none"` - `"log"` - `"alert"` |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. |
| **ipv4_address**  string | IPv4 address. |
| **ipv4_mask_length**  string | IPv4 network mask length. |
| **ipv4_network_mask**  string | IPv4 network address. |
| **ipv6_address**  string | IPv6 address. |
| **ipv6_mask_length**  string | IPv6 network mask length. |
| **ipv6_network_mask**  string | IPv6 network address. |
| **mask_length**  string | IPv4 or IPv6 network mask length. |
| **name**  string | Object name. |
| **network_mask**  string | IPv4 or IPv6 network mask. If both masks are required use ipv4-network-mask and ipv6-network-mask fields explicitly. Instead of providing mask itself it is possible to specify IPv4 or IPv6 mask length in mask-length field. If both masks length are required use ipv4-mask-length and ipv6-mask-length fields explicitly. |
| **security_zone**  boolean | N/A  **Choices:**   - `false` - `true` |
| **security_zone_settings**  dictionary | N/A |
| **auto_calculated**  boolean | Security Zone is calculated according to where the interface leads to.  **Choices:**   - `false` - `true` |
| **specific_zone**  string | Security Zone specified manually. |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **topology**  string | N/A  **Choices:**   - `"automatic"` - `"external"` - `"internal"` |
| **topology_settings**  dictionary | N/A |
| **interface_leads_to_dmz**  boolean | Whether this interface leads to demilitarized zone (perimeter network).  **Choices:**   - `false` - `true` |
| **ip_address_behind_this_interface**  string | Network settings behind this interface.  **Choices:**   - `"not defined"` - `"network defined by the interface ip and net mask"` - `"network defined by routing"` - `"specific"` |
| **specific_network**  string | Network behind this interface. |
| **ip_address**  string | IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly. |
| **ipv4_address**  string | IPv4 address. |
| **ipv6_address**  string | IPv6 address. |
| **name**  string | Object name. |
| **one_time_password**  string | N/A |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **name**  string / required | Object name. |
| **os_name**  string | Cluster platform operating system. |
| **platform_portal_settings**  dictionary | Platform portal settings. |
| **accessibility**  dictionary | Configuration of the portal access settings. |
| **allow_access_from**  string | Allowed access to the web portal (based on interfaces, or security policy).  **Choices:**   - `"rule_base"` - `"internal_interfaces"` - `"all_interfaces"` |
| **internal_access_settings**  dictionary | Configuration of the additional portal access settings for internal interfaces only. |
| **dmz**  boolean | Controls portal access settings for internal interfaces, whose topology is set to ‘DMZ’.  **Choices:**   - `false` - `true` |
| **undefined**  boolean | Controls portal access settings for internal interfaces, whose topology is set to ‘Undefined’.  **Choices:**   - `false` - `true` |
| **vpn**  boolean | Controls portal access settings for interfaces that are part of a VPN Encryption Domain.  **Choices:**   - `false` - `true` |
| **certificate_settings**  dictionary | Configuration of the portal certificate settings. |
| **base64_certificate**  string | The certificate file encoded in Base64 with padding. This file must be in the \*.p12 format. |
| **base64_password**  string | Password (encoded in Base64 with padding) for the certificate file. |
| **portal_web_settings**  dictionary | Configuration of the portal web settings. |
| **aliases**  list / elements=string | List of URL aliases that are redirected to the main portal URL. |
| **ip_address**  string | Optional, IP address for the web portal to use, if your DNS server fails to resolve the main portal URL. Note, If your DNS server resolves the main portal URL, this IP address is ignored. |
| **main_url**  string | The main URL for the web portal. |
| **send_alerts_to_server**  list / elements=string | Server(s) to send alerts to. |
| **send_logs_to_backup_server**  list / elements=string | Backup server(s) to send logs to. |
| **send_logs_to_server**  list / elements=string | Server(s) to send logs to. |
| **show_portals_certificate**  boolean | Indicates whether to show the portals certificate value in the reply.  **Choices:**   - `false` - `true` |
| **state**  string | State of the access rule (present or absent). Defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Collection of tag identifiers. |
| **threat_emulation**  boolean | Threat Emulation blade enabled.  **Choices:**   - `false` - `true` |
| **threat_extraction**  boolean | Threat Extraction blade enabled.  **Choices:**   - `false` - `true` |
| **threat_prevention_mode**  string | The mode of Threat Prevention to use. When using Autonomous Threat Prevention, disabling the Threat Prevention blades is not allowed.  **Choices:**   - `"autonomous"` - `"custom"` |
| **url_filtering**  boolean | URL Filtering blade enabled.  **Choices:**   - `false` - `true` |
| **usercheck_portal_settings**  dictionary | UserCheck portal settings. |
| **accessibility**  dictionary | Configuration of the portal access settings. |
| **allow_access_from**  string | Allowed access to the web portal (based on interfaces, or security policy).  **Choices:**   - `"rule_base"` - `"internal_interfaces"` - `"all_interfaces"` |
| **internal_access_settings**  dictionary | Configuration of the additional portal access settings for internal interfaces only. |
| **dmz**  boolean | Controls portal access settings for internal interfaces, whose topology is set to ‘DMZ’.  **Choices:**   - `false` - `true` |
| **undefined**  boolean | Controls portal access settings for internal interfaces, whose topology is set to ‘Undefined’.  **Choices:**   - `false` - `true` |
| **vpn**  boolean | Controls portal access settings for interfaces that are part of a VPN Encryption Domain.  **Choices:**   - `false` - `true` |
| **certificate_settings**  dictionary | Configuration of the portal certificate settings. |
| **base64_certificate**  string | The certificate file encoded in Base64 with padding. This file must be in the \*.p12 format. |
| **base64_password**  string | Password (encoded in Base64 with padding) for the certificate file. |
| **enabled**  boolean | State of the web portal (enabled or disabled). The supported blades are, {‘Application Control’, ‘URL Filtering’, ‘Data Loss Prevention’, ‘Anti Virus’, ‘Anti Bot’, ‘Threat Emulation’, ‘Threat Extraction’, ‘Data Awareness’}.  **Choices:**   - `false` - `true` |
| **portal_web_settings**  dictionary | Configuration of the portal web settings. |
| **aliases**  list / elements=string | List of URL aliases that are redirected to the main portal URL. |
| **ip_address**  string | Optional, IP address for the web portal to use, if your DNS server fails to resolve the main portal URL. Note, If your DNS server resolves the main portal URL, this IP address is ignored. |
| **main_url**  string | The main URL for the web portal. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **vpn**  boolean | VPN blade enabled.  **Choices:**   - `false` - `true` |
| **vpn_settings**  dictionary | Gateway VPN settings. |
| **authentication**  dictionary | Authentication. |
| **authentication_clients**  list / elements=string | Collection of VPN Authentication clients identified by the name or UID. |
| **link_selection**  dictionary | Link Selection. |
| **dns_resolving_hostname**  string | DNS Resolving Hostname. Must be set when “ip-selection” was selected to be “dns-resolving-from-hostname”. |
| **ip_address**  string | IP Address. Must be set when “ip-selection” was selected to be “use-selected-address-from-topology” or “use-statically-nated-ip”. |
| **ip_selection**  string | N/A  **Choices:**   - `"use-main-address"` - `"use-selected-address-from-topology"` - `"use-statically-nated-ip"` - `"calculated-ip-based-on-topology"` - `"dns-resolving-from-hostname"` - `"dns-resolving-from-gateway-and-domain-name"` - `"use-probing-with-high-availability"` - `"use-probing-with-load-sharing"` - `"use-one-time-probing"` |
| **maximum_concurrent_ike_negotiations**  integer | N/A |
| **maximum_concurrent_tunnels**  integer | N/A |
| **office_mode**  dictionary | Office Mode. Notation Wide Impact - Office Mode apply IPSec VPN Software Blade clients and to the Mobile Access Software Blade clients. |
| **allocate_ip_address_from**  dictionary | Allocate IP address Method. Allocate IP address by sequentially trying the given methods until success. |
| **allocate_method**  string | Using either Manual (IP Pool) or Automatic (DHCP). Must be set when “use-allocate-method” is true.  **Choices:**   - `"manual"` - `"automatic"` |
| **dhcp_mac_address**  string | Calculated MAC address for DHCP allocation. Must be set when “allocate-method” was selected to be “automatic”.  **Choices:**   - `"per-machine"` - `"per-user"` |
| **dhcp_server**  string | DHCP Server. Identified by name or UID. Must be set when “allocate-method” was selected to be “automatic”. |
| **manual_network**  string | Manual Network. Identified by name or UID. Must be set when “allocate-method” was selected to be “manual”. |
| **optional_parameters**  dictionary | This configuration applies to all Office Mode methods except Automatic (using DHCP) and ipassignment.conf entries which contain this data. |
| **dns_suffixes**  string | DNS Suffixes. |
| **first_backup_dns_server**  string | First Backup DNS Server. Identified by name or UID. Must be set when “use-first-backup-dns-server” is true and can not be set when “use-first-backup-dns-server” is false. |
| **first_backup_wins_server**  string | First Backup WINS Server. Identified by name or UID. Must be set when “use-first-backup-wins-server” is true and can not be set when “use-first-backup-wins-server” is false. |
| **ip_lease_duration**  integer | IP Lease Duration in Minutes. The value must be in the range 2-32767. |
| **primary_dns_server**  string | Primary DNS Server. Identified by name or UID. Must be set when “use-primary-dns-server” is true and can not be set when “use-primary-dns-server” is false. |
| **primary_wins_server**  string | Primary WINS Server. Identified by name or UID. Must be set when “use-primary-wins-server” is true and can not be set when “use-primary-wins-server” is false. |
| **second_backup_dns_server**  string | Second Backup DNS Server. Identified by name or UID. Must be set when “use-second-backup-dns-server” is true and can not be set when “use-second-backup-dns-server” is false. |
| **second_backup_wins_server**  string | Second Backup WINS Server. Identified by name or UID. Must be set when “use-second-backup-wins-server” is true and can not be set when “use-second-backup-wins-server” is false. |
| **use_first_backup_dns_server**  boolean | Use First Backup DNS Server.  **Choices:**   - `false` - `true` |
| **use_first_backup_wins_server**  boolean | Use First Backup WINS Server.  **Choices:**   - `false` - `true` |
| **use_primary_dns_server**  boolean | Use Primary DNS Server.  **Choices:**   - `false` - `true` |
| **use_primary_wins_server**  boolean | Use Primary WINS Server.  **Choices:**   - `false` - `true` |
| **use_second_backup_dns_server**  boolean | Use Second Backup DNS Server.  **Choices:**   - `false` - `true` |
| **use_second_backup_wins_server**  boolean | Use Second Backup WINS Server.  **Choices:**   - `false` - `true` |
| **radius_server**  boolean | Radius server used to authenticate the user.  **Choices:**   - `false` - `true` |
| **use_allocate_method**  boolean | Use Allocate Method.  **Choices:**   - `false` - `true` |
| **virtual_ip_address**  string | Virtual IPV4 address for DHCP server replies. Must be set when “allocate-method” was selected to be “automatic”. |
| **anti_spoofing_additional_addresses**  string | Additional IP Addresses for Anti-Spoofing. Identified by name or UID. Must be set when “perform-anti-spoofings” is true. |
| **group**  string | Group. Identified by name or UID. Must be set when “office-mode-permissions” was selected to be “group”. |
| **mode**  string | Office Mode Permissions.When selected to be “off”, all the other definitions are irrelevant.  **Choices:**   - `"off"` - `"specific-group"` - `"all-users"` |
| **perform_anti_spoofing**  boolean | Perform Anti-Spoofing on Office Mode addresses.  **Choices:**   - `false` - `true` |
| **support_multiple_interfaces**  boolean | Support connectivity enhancement for gateways with multiple external interfaces.  **Choices:**   - `false` - `true` |
| **remote_access**  dictionary | Remote Access. |
| **allow_vpn_clients_to_route_traffic**  boolean | Allow VPN clients to route traffic.  **Choices:**   - `false` - `true` |
| **l2tp_auth_method**  string | L2TP Authentication Method. Must be set when “support-l2tp” is true.  **Choices:**   - `"certificate"` - `"md5"` |
| **l2tp_certificate**  string | L2TP Certificate. Must be set when “l2tp-auth-method” was selected to be “certificate”. Insert “defaultCert” when you want to use the default certificate. |
| **nat_traversal_service**  string | Allocated NAT traversal UDP service. Identified by name or UID. Must be set when “support-nat-traversal-mechanism” is true. |
| **support_l2tp**  boolean | Support L2TP (relevant only when office mode is active).  **Choices:**   - `false` - `true` |
| **support_nat_traversal_mechanism**  boolean | Support NAT traversal mechanism (UDP encapsulation).  **Choices:**   - `false` - `true` |
| **support_visitor_mode**  boolean | Support Visitor Mode.  **Choices:**   - `false` - `true` |
| **visitor_mode_interface**  string | Interface for Visitor Mode. Must be set when “support-visitor-mode” is true. Insert IPV4 Address of existing interface or “All IPs” when you want all interfaces. |
| **visitor_mode_service**  string | TCP Service for Visitor Mode. Identified by name or UID. Must be set when “support-visitor-mode” is true. |
| **vpn_domain**  string | Gateway VPN domain identified by the name or UID. |
| **vpn_domain_type**  string | Gateway VPN domain type.  **Choices:**   - `"manual"` - `"addresses_behind_gw"` |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_simple_cluster_module.md#id3)

```yaml+jinja
- name: add-simple-cluster
  cp_mgmt_simple_cluster:
    cluster_mode: cluster-xl-ha
    color: yellow
    firewall: true
    interfaces:
    - anti_spoofing: true
      interface_type: cluster
      ip_address: 17.23.5.1
      name: eth0
      network_mask: 255.255.255.0
      topology: EXTERNAL
    - interface_type: sync
      name: eth1
      topology: INTERNAL
      topology_settings:
        interface_leads_to_dmz: false
        ip_address_behind_this_interface: network defined by the interface ip and net
          mask
    - anti_spoofing: true
      interface_type: cluster
      ip_address: 192.168.1.1
      name: eth2
      network_mask: 255.255.255.0
      topology: INTERNAL
      topology_settings:
        interface_leads_to_dmz: false
        ip_address_behind_this_interface: network defined by the interface ip and net
          mask
    ip_address: 17.23.5.1
    members:
    - interfaces:
      - ip_address: 17.23.5.2
        name: eth0
        network_mask: 255.255.255.0
      - ip_address: 1.1.2.4
        name: eth1
        network_mask: 255.255.255.0
      - ip_address: 192.168.1.2
        name: eth2
        network_mask: 255.255.255.0
      ip_address: 17.23.5.2
      name: member1
      one_time_password: abcd
    - interfaces:
      - ip_address: 17.23.5.3
        name: eth0
        network_mask: 255.255.255.0
      - ip_address: 1.1.2.5
        name: eth1
        network_mask: 255.255.255.0
      - ip_address: 192.168.1.3
        name: eth2
        network_mask: 255.255.255.0
      ip_address: 17.23.5.3
      name: member2
      one_time_password: abcd
    name: cluster1
    os_name: Gaia
    state: present
    cluster_version: R80.30

- name: set-simple-cluster
  cp_mgmt_simple_cluster:
    name: cluster1
    state: present

- name: delete-simple-cluster
  cp_mgmt_simple_cluster:
    name: cluster1
    state: absent
```

## [Return Values](cp_mgmt_simple_cluster_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_simple_cluster**  dictionary | The checkpoint object created or updated.  **Returned:** always, except when deleting the object. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
