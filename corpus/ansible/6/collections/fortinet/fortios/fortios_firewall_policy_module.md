---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_policy module – Configure IPv4/IPv6 policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_policy_module.html
fetched_at: 2026-07-27T17:41:18+00:00
---
# fortinet.fortios.fortios_firewall_policy module – Configure IPv4/IPv6 policies in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_policy_module.md#ansible-collections-fortinet-fortios-fortios-firewall-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_policy`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_policy_module.md#synopsis)
- [Requirements](fortios_firewall_policy_module.md#requirements)
- [Parameters](fortios_firewall_policy_module.md#parameters)
- [Notes](fortios_firewall_policy_module.md#notes)
- [Examples](fortios_firewall_policy_module.md#examples)
- [Return Values](fortios_firewall_policy_module.md#return-values)

## [Synopsis](fortios_firewall_policy_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and policy category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **action**  string | the action indiactor to move an object in the list  Choices:   - `"move"` |
| **after**  string | mkey of target identifier |
| **before**  string | mkey of target identifier |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_policy**  dictionary | Configure IPv4/IPv6 policies. |
| **action**  string | Policy action (accept/deny/ipsec).  Choices:   - `"accept"` - `"deny"` - `"ipsec"` |
| **anti_replay**  string | Enable/disable anti-replay check.  Choices:   - `"enable"` - `"disable"` |
| **app_category**  list / elements=dictionary | Application category ID list. |
| **id**  integer | Category IDs. |
| **app_group**  list / elements=dictionary | Application group names. |
| **name**  string | Application group names. Source application.group.name. |
| **application**  list / elements=dictionary | Application ID list. |
| **id**  integer | Application IDs. |
| **application_list**  string | Name of an existing Application list. Source application.list.name. |
| **auth_cert**  string | HTTPS server certificate for policy authentication. Source vpn.certificate.local.name. |
| **auth_path**  string | Enable/disable authentication-based routing.  Choices:   - `"enable"` - `"disable"` |
| **auth_redirect_addr**  string | HTTP-to-HTTPS redirect address for firewall authentication. |
| **auto_asic_offload**  string | Enable/disable policy traffic ASIC offloading.  Choices:   - `"enable"` - `"disable"` |
| **av_profile**  string | Name of an existing Antivirus profile. Source antivirus.profile.name. |
| **block_notification**  string | Enable/disable block notification.  Choices:   - `"enable"` - `"disable"` |
| **captive_portal_exempt**  string | Enable to exempt some users from the captive portal.  Choices:   - `"enable"` - `"disable"` |
| **capture_packet**  string | Enable/disable capture packets.  Choices:   - `"enable"` - `"disable"` |
| **cifs_profile**  string | Name of an existing CIFS profile. Source cifs.profile.name. |
| **comments**  string | Comment. |
| **custom_log_fields**  list / elements=dictionary | Custom fields to append to log messages for this policy. |
| **field_id**  string | Custom log field. Source log.custom-field.id. |
| **decrypted_traffic_mirror**  string | Decrypted traffic mirror. Source firewall.decrypted-traffic-mirror.name. |
| **delay_tcp_npu_session**  string | Enable TCP NPU session delay to guarantee packet order of 3-way handshake.  Choices:   - `"enable"` - `"disable"` |
| **devices**  list / elements=dictionary | Names of devices or device groups that can be matched by the policy. |
| **name**  string | Device or group name. Source user.device.alias user.device-group.name user.device-category.name. |
| **diffserv_copy**  string | Enable to copy packet”s DiffServ values from session”s original direction to its reply direction.  Choices:   - `"enable"` - `"disable"` |
| **diffserv_forward**  string | Enable to change packet”s DiffServ values to the specified diffservcode-forward value.  Choices:   - `"enable"` - `"disable"` |
| **diffserv_reverse**  string | Enable to change packet”s reverse (reply) DiffServ values to the specified diffservcode-rev value.  Choices:   - `"enable"` - `"disable"` |
| **diffservcode_forward**  string | Change packet”s DiffServ to this value. |
| **diffservcode_rev**  string | Change packet”s reverse (reply) DiffServ to this value. |
| **disclaimer**  string | Enable/disable user authentication disclaimer.  Choices:   - `"enable"` - `"disable"` |
| **dlp_profile**  string | Name of an existing DLP profile. Source dlp.profile.name. |
| **dlp_sensor**  string | Name of an existing DLP sensor. Source dlp.sensor.name. |
| **dnsfilter_profile**  string | Name of an existing DNS filter profile. Source dnsfilter.profile.name. |
| **dscp_match**  string | Enable DSCP check.  Choices:   - `"enable"` - `"disable"` |
| **dscp_negate**  string | Enable negated DSCP match.  Choices:   - `"enable"` - `"disable"` |
| **dscp_value**  string | DSCP value. |
| **dsri**  string | Enable DSRI to ignore HTTP server responses.  Choices:   - `"enable"` - `"disable"` |
| **dstaddr**  list / elements=dictionary | Destination IPv4 address and address group names. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name firewall.vip.name firewall.vipgrp.name system.external-resource .name. |
| **dstaddr6**  list / elements=dictionary | Destination IPv6 address name and address group names. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name firewall.vipgrp6.name firewall.vip6.name system .external-resource.name. |
| **dstaddr6_negate**  string | When enabled dstaddr6 specifies what the destination address must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **dstaddr_negate**  string | When enabled dstaddr specifies what the destination address must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **dstintf**  list / elements=dictionary | Outgoing (egress) interface. |
| **name**  string | Interface name. Source system.interface.name system.zone.name system.sdwan.zone.name. |
| **dynamic_shaping**  string | Enable/disable dynamic RADIUS defined traffic shaping.  Choices:   - `"enable"` - `"disable"` |
| **email_collect**  string | Enable/disable email collection.  Choices:   - `"enable"` - `"disable"` |
| **emailfilter_profile**  string | Name of an existing email filter profile. Source emailfilter.profile.name. |
| **fec**  string | Enable/disable Forward Error Correction on traffic matching this policy on a FEC device.  Choices:   - `"enable"` - `"disable"` |
| **file_filter_profile**  string | Name of an existing file-filter profile. Source file-filter.profile.name. |
| **firewall_session_dirty**  string | How to handle sessions if the configuration of this firewall policy changes.  Choices:   - `"check-all"` - `"check-new"` |
| **fixedport**  string | Enable to prevent source NAT from changing a session”s source port.  Choices:   - `"enable"` - `"disable"` |
| **fsso**  string | Enable/disable Fortinet Single Sign-On.  Choices:   - `"enable"` - `"disable"` |
| **fsso_agent_for_ntlm**  string | FSSO agent to use for NTLM authentication. Source user.fsso.name. |
| **fsso_groups**  list / elements=dictionary | Names of FSSO groups. |
| **name**  string | Names of FSSO groups. Source user.adgrp.name. |
| **geoip_anycast**  string | Enable/disable recognition of anycast IP addresses using the geography IP database.  Choices:   - `"enable"` - `"disable"` |
| **geoip_match**  string | Match geography address based either on its physical location or registered location.  Choices:   - `"physical-location"` - `"registered-location"` |
| **global_label**  string | Label for the policy that appears when the GUI is in Global View mode. |
| **groups**  list / elements=dictionary | Names of user groups that can authenticate with this policy. |
| **name**  string | Group name. Source user.group.name. |
| **gtp_profile**  string | GTP profile. Source firewall.gtp.name. |
| **http_policy_redirect**  string | Redirect HTTP(S) traffic to matching transparent web proxy policy.  Choices:   - `"enable"` - `"disable"` |
| **icap_profile**  string | Name of an existing ICAP profile. Source icap.profile.name. |
| **identity_based_route**  string | Name of identity-based routing rule. Source firewall.identity-based-route.name. |
| **inbound**  string | Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN.  Choices:   - `"enable"` - `"disable"` |
| **inspection_mode**  string | Policy inspection mode (Flow/proxy). Default is Flow mode.  Choices:   - `"proxy"` - `"flow"` |
| **internet_service**  string | Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.  Choices:   - `"enable"` - `"disable"` |
| **internet_service6**  string | Enable/disable use of IPv6 Internet Services for this policy. If enabled, destination address and service are not used.  Choices:   - `"enable"` - `"disable"` |
| **internet_service6_custom**  list / elements=dictionary | Custom IPv6 Internet Service name. |
| **name**  string | Custom Internet Service name. Source . |
| **internet_service6_custom_group**  list / elements=dictionary | Custom Internet Service6 group name. |
| **name**  string | Custom Internet Service6 group name. Source . |
| **internet_service6_group**  list / elements=dictionary | Internet Service group name. |
| **name**  string | Internet Service group name. Source . |
| **internet_service6_name**  list / elements=dictionary | IPv6 Internet Service name. |
| **name**  string | IPv6 Internet Service name. Source . |
| **internet_service6_negate**  string | When enabled internet-service6 specifies what the service must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **internet_service6_src**  string | Enable/disable use of IPv6 Internet Services in source for this policy. If enabled, source address is not used.  Choices:   - `"enable"` - `"disable"` |
| **internet_service6_src_custom**  list / elements=dictionary | Custom IPv6 Internet Service source name. |
| **name**  string | Custom Internet Service name. Source . |
| **internet_service6_src_custom_group**  list / elements=dictionary | Custom Internet Service6 source group name. |
| **name**  string | Custom Internet Service6 group name. Source . |
| **internet_service6_src_group**  list / elements=dictionary | Internet Service6 source group name. |
| **name**  string | Internet Service group name. Source . |
| **internet_service6_src_name**  list / elements=dictionary | IPv6 Internet Service source name. |
| **name**  string | Internet Service name. Source . |
| **internet_service6_src_negate**  string | When enabled internet-service6-src specifies what the service must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **internet_service_custom**  list / elements=dictionary | Custom Internet Service name. |
| **name**  string | Custom Internet Service name. Source firewall.internet-service-custom.name. |
| **internet_service_custom_group**  list / elements=dictionary | Custom Internet Service group name. |
| **name**  string | Custom Internet Service group name. Source firewall.internet-service-custom-group.name. |
| **internet_service_group**  list / elements=dictionary | Internet Service group name. |
| **name**  string | Internet Service group name. Source firewall.internet-service-group.name. |
| **internet_service_id**  list / elements=dictionary | Internet Service ID. |
| **id**  integer | Internet Service ID. Source firewall.internet-service.id. |
| **internet_service_name**  list / elements=dictionary | Internet Service name. |
| **name**  string | Internet Service name. Source firewall.internet-service-name.name. |
| **internet_service_negate**  string | When enabled internet-service specifies what the service must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **internet_service_src**  string | Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.  Choices:   - `"enable"` - `"disable"` |
| **internet_service_src_custom**  list / elements=dictionary | Custom Internet Service source name. |
| **name**  string | Custom Internet Service name. Source firewall.internet-service-custom.name. |
| **internet_service_src_custom_group**  list / elements=dictionary | Custom Internet Service source group name. |
| **name**  string | Custom Internet Service group name. Source firewall.internet-service-custom-group.name. |
| **internet_service_src_group**  list / elements=dictionary | Internet Service source group name. |
| **name**  string | Internet Service group name. Source firewall.internet-service-group.name. |
| **internet_service_src_id**  list / elements=dictionary | Internet Service source ID. |
| **id**  integer | Internet Service ID. Source firewall.internet-service.id. |
| **internet_service_src_name**  list / elements=dictionary | Internet Service source name. |
| **name**  string | Internet Service name. Source firewall.internet-service-name.name. |
| **internet_service_src_negate**  string | When enabled internet-service-src specifies what the service must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **ippool**  string | Enable to use IP Pools for source NAT.  Choices:   - `"enable"` - `"disable"` |
| **ips_sensor**  string | Name of an existing IPS sensor. Source ips.sensor.name. |
| **label**  string | Label for the policy that appears when the GUI is in Section View mode. |
| **learning_mode**  string | Enable to allow everything, but log all of the meaningful data for security information gathering. A learning report will be generated.  Choices:   - `"enable"` - `"disable"` |
| **logtraffic**  string | Enable or disable logging. Log all sessions or security profile sessions.  Choices:   - `"all"` - `"utm"` - `"disable"` |
| **logtraffic_start**  string | Record logs when a session starts.  Choices:   - `"enable"` - `"disable"` |
| **match_vip**  string | Enable to match packets that have had their destination addresses changed by a VIP.  Choices:   - `"enable"` - `"disable"` |
| **match_vip_only**  string | Enable/disable matching of only those packets that have had their destination addresses changed by a VIP.  Choices:   - `"enable"` - `"disable"` |
| **mms_profile**  string | Name of an existing MMS profile. Source firewall.mms-profile.name. |
| **name**  string | Policy name. |
| **nat**  string | Enable/disable source NAT.  Choices:   - `"enable"` - `"disable"` |
| **nat46**  string | Enable/disable NAT46.  Choices:   - `"enable"` - `"disable"` |
| **nat64**  string | Enable/disable NAT64.  Choices:   - `"enable"` - `"disable"` |
| **natinbound**  string | Policy-based IPsec VPN: apply destination NAT to inbound traffic.  Choices:   - `"enable"` - `"disable"` |
| **natip**  string | Policy-based IPsec VPN: source NAT IP address for outgoing traffic. |
| **natoutbound**  string | Policy-based IPsec VPN: apply source NAT to outbound traffic.  Choices:   - `"enable"` - `"disable"` |
| **network_service_dynamic**  list / elements=dictionary | Dynamic Network Service name. |
| **name**  string | Dynamic Network Service name. Source . |
| **network_service_src_dynamic**  list / elements=dictionary | Dynamic Network Service source name. |
| **name**  string | Dynamic Network Service name. Source . |
| **np_acceleration**  string | Enable/disable UTM Network Processor acceleration.  Choices:   - `"enable"` - `"disable"` |
| **ntlm**  string | Enable/disable NTLM authentication.  Choices:   - `"enable"` - `"disable"` |
| **ntlm_enabled_browsers**  list / elements=dictionary | HTTP-User-Agent value of supported browsers. |
| **user_agent_string**  string | User agent string. |
| **ntlm_guest**  string | Enable/disable NTLM guest user access.  Choices:   - `"enable"` - `"disable"` |
| **outbound**  string | Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN.  Choices:   - `"enable"` - `"disable"` |
| **passive_wan_health_measurement**  string | Enable/disable passive WAN health measurement. When enabled, auto-asic-offload is disabled.  Choices:   - `"enable"` - `"disable"` |
| **per_ip_shaper**  string | Per-IP traffic shaper. Source firewall.shaper.per-ip-shaper.name. |
| **permit_any_host**  string | Accept UDP packets from any host.  Choices:   - `"enable"` - `"disable"` |
| **permit_stun_host**  string | Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host.  Choices:   - `"enable"` - `"disable"` |
| **pfcp_profile**  string | PFCP profile. Source firewall.pfcp.name. |
| **policy_expiry**  string | Enable/disable policy expiry.  Choices:   - `"enable"` - `"disable"` |
| **policy_expiry_date**  string | Policy expiry date (YYYY-MM-DD HH:MM:SS). |
| **policyid**  integer / required | Policy ID (0 - 4294967294). |
| **poolname**  list / elements=dictionary | IP Pool names. |
| **name**  string | IP pool name. Source firewall.ippool.name. |
| **poolname6**  list / elements=dictionary | IPv6 pool names. |
| **name**  string | IPv6 pool name. Source firewall.ippool6.name. |
| **profile_group**  string | Name of profile group. Source firewall.profile-group.name. |
| **profile_protocol_options**  string | Name of an existing Protocol options profile. Source firewall.profile-protocol-options.name. |
| **profile_type**  string | Determine whether the firewall policy allows security profile groups or single profiles only.  Choices:   - `"single"` - `"group"` |
| **radius_mac_auth_bypass**  string | Enable MAC authentication bypass. The bypassed MAC address must be received from RADIUS server.  Choices:   - `"enable"` - `"disable"` |
| **redirect_url**  string | URL users are directed to after seeing and accepting the disclaimer or authenticating. |
| **replacemsg_override_group**  string | Override the default replacement message group for this policy. Source system.replacemsg-group.name. |
| **reputation_direction**  string | Direction of the initial traffic for reputation to take effect.  Choices:   - `"source"` - `"destination"` |
| **reputation_direction6**  string | Direction of the initial traffic for IPv6 reputation to take effect.  Choices:   - `"source"` - `"destination"` |
| **reputation_minimum**  integer | Minimum Reputation to take action. Source firewall.internet-service-reputation.id. |
| **reputation_minimum6**  integer | IPv6 Minimum Reputation to take action. Source . |
| **rsso**  string | Enable/disable RADIUS single sign-on (RSSO).  Choices:   - `"enable"` - `"disable"` |
| **rtp_addr**  list / elements=dictionary | Address names if this is an RTP NAT policy. |
| **name**  string | Address name. Source firewall.internet-service-custom-group.name firewall.addrgrp.name. |
| **rtp_nat**  string | Enable Real Time Protocol (RTP) NAT.  Choices:   - `"disable"` - `"enable"` |
| **scan_botnet_connections**  string | Block or monitor connections to Botnet servers or disable Botnet scanning.  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  string | Schedule name. Source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name. |
| **schedule_timeout**  string | Enable to force current sessions to end when the schedule object times out. Disable allows them to end from inactivity.  Choices:   - `"enable"` - `"disable"` |
| **sctp_filter_profile**  string | Name of an existing SCTP filter profile. Source sctp-filter.profile.name. |
| **send_deny_packet**  string | Enable to send a reply when a session is denied or blocked by a firewall policy.  Choices:   - `"disable"` - `"enable"` |
| **service**  list / elements=dictionary | Service and service group names. |
| **name**  string | Service and service group names. Source firewall.service.custom.name firewall.service.group.name. |
| **service_negate**  string | When enabled service specifies what the service must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **session_ttl**  string | TTL in seconds for sessions accepted by this policy (0 means use the system ). |
| **sgt**  list / elements=dictionary | Security group tags. |
| **id**  integer | Security group tag (1 - 65535). |
| **sgt_check**  string | Enable/disable security group tags (SGT) check.  Choices:   - `"enable"` - `"disable"` |
| **spamfilter_profile**  string | Name of an existing Spam filter profile. Source spamfilter.profile.name. |
| **src_vendor_mac**  list / elements=dictionary | Vendor MAC source ID. |
| **id**  integer | Vendor MAC ID. Source firewall.vendor-mac.id. |
| **srcaddr**  list / elements=dictionary | Source IPv4 address and address group names. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name system.external-resource.name. |
| **srcaddr6**  list / elements=dictionary | Source IPv6 address name and address group names. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name system.external-resource.name. |
| **srcaddr6_negate**  string | When enabled srcaddr6 specifies what the source address must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **srcaddr_negate**  string | When enabled srcaddr specifies what the source address must NOT be.  Choices:   - `"enable"` - `"disable"` |
| **srcintf**  list / elements=dictionary | Incoming (ingress) interface. |
| **name**  string | Interface name. Source system.interface.name system.zone.name system.sdwan.zone.name. |
| **ssh_filter_profile**  string | Name of an existing SSH filter profile. Source ssh-filter.profile.name. |
| **ssh_policy_redirect**  string | Redirect SSH traffic to matching transparent proxy policy.  Choices:   - `"enable"` - `"disable"` |
| **ssl_mirror**  string | Enable to copy decrypted SSL traffic to a FortiGate interface (called SSL mirroring).  Choices:   - `"enable"` - `"disable"` |
| **ssl_mirror_intf**  list / elements=dictionary | SSL mirror interface name. |
| **name**  string | Mirror Interface name. Source system.interface.name system.zone.name. |
| **ssl_ssh_profile**  string | Name of an existing SSL SSH profile. Source firewall.ssl-ssh-profile.name. |
| **status**  string | Enable or disable this policy.  Choices:   - `"enable"` - `"disable"` |
| **tcp_mss_receiver**  integer | Receiver TCP maximum segment size (MSS). |
| **tcp_mss_sender**  integer | Sender TCP maximum segment size (MSS). |
| **tcp_session_without_syn**  string | Enable/disable creation of TCP session without SYN flag.  Choices:   - `"all"` - `"data-only"` - `"disable"` |
| **timeout_send_rst**  string | Enable/disable sending RST packets when TCP sessions expire.  Choices:   - `"enable"` - `"disable"` |
| **tos**  string | ToS (Type of Service) value used for comparison. |
| **tos_mask**  string | Non-zero bit positions are used for comparison while zero bit positions are ignored. |
| **tos_negate**  string | Enable negated TOS match.  Choices:   - `"enable"` - `"disable"` |
| **traffic_shaper**  string | Traffic shaper. Source firewall.shaper.traffic-shaper.name. |
| **traffic_shaper_reverse**  string | Reverse traffic shaper. Source firewall.shaper.traffic-shaper.name. |
| **url_category**  list / elements=dictionary | URL category ID list. |
| **id**  integer | URL category ID. |
| **users**  list / elements=dictionary | Names of individual users that can authenticate with this policy. |
| **name**  string | Names of individual users that can authenticate with this policy. Source user.local.name. |
| **utm_status**  string | Enable to add one or more security profiles (AV, IPS, etc.) to the firewall policy.  Choices:   - `"enable"` - `"disable"` |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **videofilter_profile**  string | Name of an existing VideoFilter profile. Source videofilter.profile.name. |
| **vlan_cos_fwd**  integer | VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest. |
| **vlan_cos_rev**  integer | VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest. |
| **vlan_filter**  string | Set VLAN filters. |
| **voip_profile**  string | Name of an existing VoIP profile. Source voip.profile.name. |
| **vpntunnel**  string | Policy-based IPsec VPN: name of the IPsec VPN Phase 1. Source vpn.ipsec.phase1.name vpn.ipsec.manualkey.name. |
| **waf_profile**  string | Name of an existing Web application firewall profile. Source waf.profile.name. |
| **wanopt**  string | Enable/disable WAN optimization.  Choices:   - `"enable"` - `"disable"` |
| **wanopt_detection**  string | WAN optimization auto-detection mode.  Choices:   - `"active"` - `"passive"` - `"off"` |
| **wanopt_passive_opt**  string | WAN optimization passive mode options. This option decides what IP address will be used to connect server.  Choices:   - `"default"` - `"transparent"` - `"non-transparent"` |
| **wanopt_peer**  string | WAN optimization peer. Source wanopt.peer.peer-host-id. |
| **wanopt_profile**  string | WAN optimization profile. Source wanopt.profile.name. |
| **wccp**  string | Enable/disable forwarding traffic matching this policy to a configured WCCP server.  Choices:   - `"enable"` - `"disable"` |
| **webcache**  string | Enable/disable web cache.  Choices:   - `"enable"` - `"disable"` |
| **webcache_https**  string | Enable/disable web cache for HTTPS.  Choices:   - `"disable"` - `"enable"` |
| **webfilter_profile**  string | Name of an existing Web filter profile. Source webfilter.profile.name. |
| **webproxy_forward_server**  string | Webproxy forward server name. Source web-proxy.forward-server.name web-proxy.forward-server-group.name. |
| **webproxy_profile**  string | Webproxy profile name. Source web-proxy.profile.name. |
| **wsso**  string | Enable/disable WiFi Single Sign On (WSSO).  Choices:   - `"enable"` - `"disable"` |
| **ztna_ems_tag**  list / elements=dictionary | Source ztna-ems-tag names. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **ztna_geo_tag**  list / elements=dictionary | Source ztna-geo-tag names. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **ztna_status**  string | Enable/disable zero trust access.  Choices:   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **self**  string | mkey of self identifier |
| **state**  string | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_policy_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks
> - Adjust object order by moving self after(before) another.
> - Only one of [after, before] must be specified when action is moving an object.

## [Examples](fortios_firewall_policy_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure IPv4/IPv6 policies.
    fortios_firewall_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_policy:
        action: "accept"
        anti_replay: "enable"
        app_category:
         -
            id:  "6"
        app_group:
         -
            name: "default_name_8 (source application.group.name)"
        application:
         -
            id:  "10"
        application_list: "<your_own_value> (source application.list.name)"
        auth_cert: "<your_own_value> (source vpn.certificate.local.name)"
        auth_path: "enable"
        auth_redirect_addr: "<your_own_value>"
        auto_asic_offload: "enable"
        av_profile: "<your_own_value> (source antivirus.profile.name)"
        block_notification: "enable"
        captive_portal_exempt: "enable"
        capture_packet: "enable"
        cifs_profile: "<your_own_value> (source cifs.profile.name)"
        comments: "<your_own_value>"
        custom_log_fields:
         -
            field_id: "<your_own_value> (source log.custom-field.id)"
        decrypted_traffic_mirror: "<your_own_value> (source firewall.decrypted-traffic-mirror.name)"
        delay_tcp_npu_session: "enable"
        devices:
         -
            name: "default_name_27 (source user.device.alias user.device-group.name user.device-category.name)"
        diffserv_copy: "enable"
        diffserv_forward: "enable"
        diffserv_reverse: "enable"
        diffservcode_forward: "<your_own_value>"
        diffservcode_rev: "<your_own_value>"
        disclaimer: "enable"
        dlp_profile: "<your_own_value> (source dlp.profile.name)"
        dlp_sensor: "<your_own_value> (source dlp.sensor.name)"
        dnsfilter_profile: "<your_own_value> (source dnsfilter.profile.name)"
        dscp_match: "enable"
        dscp_negate: "enable"
        dscp_value: "<your_own_value>"
        dsri: "enable"
        dstaddr:
         -
            name: "default_name_42 (source firewall.address.name firewall.addrgrp.name firewall.vip.name firewall.vipgrp.name system.external-resource.name)"
        dstaddr_negate: "enable"
        dstaddr6:
         -
            name: "default_name_45 (source firewall.address6.name firewall.addrgrp6.name firewall.vipgrp6.name firewall.vip6.name system.external-resource
              .name)"
        dstaddr6_negate: "enable"
        dstintf:
         -
            name: "default_name_48 (source system.interface.name system.zone.name system.sdwan.zone.name)"
        dynamic_shaping: "enable"
        email_collect: "enable"
        emailfilter_profile: "<your_own_value> (source emailfilter.profile.name)"
        fec: "enable"
        file_filter_profile: "<your_own_value> (source file-filter.profile.name)"
        firewall_session_dirty: "check-all"
        fixedport: "enable"
        fsso: "enable"
        fsso_agent_for_ntlm: "<your_own_value> (source user.fsso.name)"
        fsso_groups:
         -
            name: "default_name_59 (source user.adgrp.name)"
        geoip_anycast: "enable"
        geoip_match: "physical-location"
        global_label: "<your_own_value>"
        groups:
         -
            name: "default_name_64 (source user.group.name)"
        gtp_profile: "<your_own_value> (source firewall.gtp.name)"
        http_policy_redirect: "enable"
        icap_profile: "<your_own_value> (source icap.profile.name)"
        identity_based_route: "<your_own_value> (source firewall.identity-based-route.name)"
        inbound: "enable"
        inspection_mode: "proxy"
        internet_service: "enable"
        internet_service_custom:
         -
            name: "default_name_73 (source firewall.internet-service-custom.name)"
        internet_service_custom_group:
         -
            name: "default_name_75 (source firewall.internet-service-custom-group.name)"
        internet_service_group:
         -
            name: "default_name_77 (source firewall.internet-service-group.name)"
        internet_service_id:
         -
            id:  "79 (source firewall.internet-service.id)"
        internet_service_name:
         -
            name: "default_name_81 (source firewall.internet-service-name.name)"
        internet_service_negate: "enable"
        internet_service_src: "enable"
        internet_service_src_custom:
         -
            name: "default_name_85 (source firewall.internet-service-custom.name)"
        internet_service_src_custom_group:
         -
            name: "default_name_87 (source firewall.internet-service-custom-group.name)"
        internet_service_src_group:
         -
            name: "default_name_89 (source firewall.internet-service-group.name)"
        internet_service_src_id:
         -
            id:  "91 (source firewall.internet-service.id)"
        internet_service_src_name:
         -
            name: "default_name_93 (source firewall.internet-service-name.name)"
        internet_service_src_negate: "enable"
        internet_service6: "enable"
        internet_service6_custom:
         -
            name: "default_name_97 (source )"
        internet_service6_custom_group:
         -
            name: "default_name_99 (source )"
        internet_service6_group:
         -
            name: "default_name_101 (source )"
        internet_service6_name:
         -
            name: "default_name_103 (source )"
        internet_service6_negate: "enable"
        internet_service6_src: "enable"
        internet_service6_src_custom:
         -
            name: "default_name_107 (source )"
        internet_service6_src_custom_group:
         -
            name: "default_name_109 (source )"
        internet_service6_src_group:
         -
            name: "default_name_111 (source )"
        internet_service6_src_name:
         -
            name: "default_name_113 (source )"
        internet_service6_src_negate: "enable"
        ippool: "enable"
        ips_sensor: "<your_own_value> (source ips.sensor.name)"
        label: "<your_own_value>"
        learning_mode: "enable"
        logtraffic: "all"
        logtraffic_start: "enable"
        match_vip: "enable"
        match_vip_only: "enable"
        mms_profile: "<your_own_value> (source firewall.mms-profile.name)"
        name: "default_name_124"
        nat: "enable"
        nat46: "enable"
        nat64: "enable"
        natinbound: "enable"
        natip: "<your_own_value>"
        natoutbound: "enable"
        network_service_dynamic:
         -
            name: "default_name_132 (source )"
        network_service_src_dynamic:
         -
            name: "default_name_134 (source )"
        np_acceleration: "enable"
        ntlm: "enable"
        ntlm_enabled_browsers:
         -
            user_agent_string: "<your_own_value>"
        ntlm_guest: "enable"
        outbound: "enable"
        passive_wan_health_measurement: "enable"
        per_ip_shaper: "<your_own_value> (source firewall.shaper.per-ip-shaper.name)"
        permit_any_host: "enable"
        permit_stun_host: "enable"
        pfcp_profile: "<your_own_value> (source firewall.pfcp.name)"
        policy_expiry: "enable"
        policy_expiry_date: "<your_own_value>"
        policyid: "0"
        poolname:
         -
            name: "default_name_150 (source firewall.ippool.name)"
        poolname6:
         -
            name: "default_name_152 (source firewall.ippool6.name)"
        profile_group: "<your_own_value> (source firewall.profile-group.name)"
        profile_protocol_options: "<your_own_value> (source firewall.profile-protocol-options.name)"
        profile_type: "single"
        radius_mac_auth_bypass: "enable"
        redirect_url: "<your_own_value>"
        replacemsg_override_group: "<your_own_value> (source system.replacemsg-group.name)"
        reputation_direction: "source"
        reputation_direction6: "source"
        reputation_minimum: "0"
        reputation_minimum6: "0"
        rsso: "enable"
        rtp_addr:
         -
            name: "default_name_165 (source firewall.internet-service-custom-group.name firewall.addrgrp.name)"
        rtp_nat: "disable"
        scan_botnet_connections: "disable"
        schedule: "<your_own_value> (source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name)"
        schedule_timeout: "enable"
        sctp_filter_profile: "<your_own_value> (source sctp-filter.profile.name)"
        send_deny_packet: "disable"
        service:
         -
            name: "default_name_173 (source firewall.service.custom.name firewall.service.group.name)"
        service_negate: "enable"
        session_ttl: "<your_own_value>"
        sgt:
         -
            id:  "177"
        sgt_check: "enable"
        spamfilter_profile: "<your_own_value> (source spamfilter.profile.name)"
        src_vendor_mac:
         -
            id:  "181 (source firewall.vendor-mac.id)"
        srcaddr:
         -
            name: "default_name_183 (source firewall.address.name firewall.addrgrp.name system.external-resource.name)"
        srcaddr_negate: "enable"
        srcaddr6:
         -
            name: "default_name_186 (source firewall.address6.name firewall.addrgrp6.name system.external-resource.name)"
        srcaddr6_negate: "enable"
        srcintf:
         -
            name: "default_name_189 (source system.interface.name system.zone.name system.sdwan.zone.name)"
        ssh_filter_profile: "<your_own_value> (source ssh-filter.profile.name)"
        ssh_policy_redirect: "enable"
        ssl_mirror: "enable"
        ssl_mirror_intf:
         -
            name: "default_name_194 (source system.interface.name system.zone.name)"
        ssl_ssh_profile: "<your_own_value> (source firewall.ssl-ssh-profile.name)"
        status: "enable"
        tcp_mss_receiver: "0"
        tcp_mss_sender: "0"
        tcp_session_without_syn: "all"
        timeout_send_rst: "enable"
        tos: "<your_own_value>"
        tos_mask: "<your_own_value>"
        tos_negate: "enable"
        traffic_shaper: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
        traffic_shaper_reverse: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
        url_category:
         -
            id:  "207"
        users:
         -
            name: "default_name_209 (source user.local.name)"
        utm_status: "enable"
        uuid: "<your_own_value>"
        videofilter_profile: "<your_own_value> (source videofilter.profile.name)"
        vlan_cos_fwd: "255"
        vlan_cos_rev: "255"
        vlan_filter: "<your_own_value>"
        voip_profile: "<your_own_value> (source voip.profile.name)"
        vpntunnel: "<your_own_value> (source vpn.ipsec.phase1.name vpn.ipsec.manualkey.name)"
        waf_profile: "<your_own_value> (source waf.profile.name)"
        wanopt: "enable"
        wanopt_detection: "active"
        wanopt_passive_opt: "default"
        wanopt_peer: "<your_own_value> (source wanopt.peer.peer-host-id)"
        wanopt_profile: "<your_own_value> (source wanopt.profile.name)"
        wccp: "enable"
        webcache: "enable"
        webcache_https: "disable"
        webfilter_profile: "<your_own_value> (source webfilter.profile.name)"
        webproxy_forward_server: "<your_own_value> (source web-proxy.forward-server.name web-proxy.forward-server-group.name)"
        webproxy_profile: "<your_own_value> (source web-proxy.profile.name)"
        wsso: "enable"
        ztna_ems_tag:
         -
            name: "default_name_232 (source firewall.address.name firewall.addrgrp.name)"
        ztna_geo_tag:
         -
            name: "default_name_234 (source firewall.address.name firewall.addrgrp.name)"
        ztna_status: "enable"

  - name: move firewall.policy
    fortios_firewall_policy:
      vdom:  "root"
      action: "move"
      self: "<mkey of self identifier>"
      after: "<mkey of target identifier>"
     #before: "<mkey of target identifier>"
```

## [Return Values](fortios_firewall_policy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
