---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_settings module – Configure VDOM settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_settings_module.html
fetched_at: 2026-07-28T02:29:22+00:00
---
# fortinet.fortios.fortios_system_settings module – Configure VDOM settings in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_system_settings_module.md#ansible-collections-fortinet-fortios-fortios-system-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_settings`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_settings_module.md#synopsis)
- [Requirements](fortios_system_settings_module.md#requirements)
- [Parameters](fortios_system_settings_module.md#parameters)
- [Notes](fortios_system_settings_module.md#notes)
- [Examples](fortios_system_settings_module.md#examples)
- [Return Values](fortios_system_settings_module.md#return-values)

## [Synopsis](fortios_system_settings_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and settings category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **system_settings**  dictionary | Configure VDOM settings. |
| **allow_linkdown_path**  string | Enable/disable link down path.  **Choices:**   - `"enable"` - `"disable"` |
| **allow_subnet_overlap**  string | Enable/disable allowing interface subnets to use overlapping IP addresses.  **Choices:**   - `"enable"` - `"disable"` |
| **application_bandwidth_tracking**  string | Enable/disable application bandwidth tracking.  **Choices:**   - `"disable"` - `"enable"` |
| **asymroute**  string | Enable/disable IPv4 asymmetric routing.  **Choices:**   - `"enable"` - `"disable"` |
| **asymroute6**  string | Enable/disable asymmetric IPv6 routing.  **Choices:**   - `"enable"` - `"disable"` |
| **asymroute6_icmp**  string | Enable/disable asymmetric ICMPv6 routing.  **Choices:**   - `"enable"` - `"disable"` |
| **asymroute_icmp**  string | Enable/disable ICMP asymmetric routing.  **Choices:**   - `"enable"` - `"disable"` |
| **auxiliary_session**  string | Enable/disable auxiliary session.  **Choices:**   - `"enable"` - `"disable"` |
| **bfd**  string | Enable/disable Bi-directional Forwarding Detection (BFD) on all interfaces.  **Choices:**   - `"enable"` - `"disable"` |
| **bfd_desired_min_tx**  integer | BFD desired minimal transmit interval (1 - 100000 ms). |
| **bfd_detect_mult**  integer | BFD detection multiplier (1 - 50). |
| **bfd_dont_enforce_src_port**  string | Enable to not enforce verifying the source port of BFD Packets.  **Choices:**   - `"enable"` - `"disable"` |
| **bfd_required_min_rx**  integer | BFD required minimal receive interval (1 - 100000 ms). |
| **block_land_attack**  string | Enable/disable blocking of land attacks.  **Choices:**   - `"disable"` - `"enable"` |
| **central_nat**  string | Enable/disable central NAT.  **Choices:**   - `"enable"` - `"disable"` |
| **comments**  string | VDOM comments. |
| **compliance_check**  string | Enable/disable PCI DSS compliance checking.  **Choices:**   - `"enable"` - `"disable"` |
| **consolidated_firewall_mode**  string | Consolidated firewall mode.  **Choices:**   - `"enable"` - `"disable"` |
| **default_app_port_as_service**  string | Enable/disable policy service enforcement based on application default ports.  **Choices:**   - `"enable"` - `"disable"` |
| **default_policy_expiry_days**  integer | Default policy expiry in days (0 - 365 days). |
| **default_voip_alg_mode**  string | Configure how the FortiGate handles VoIP traffic when a policy that accepts the traffic doesn”t include a VoIP profile.  **Choices:**   - `"proxy-based"` - `"kernel-helper-based"` |
| **deny_tcp_with_icmp**  string | Enable/disable denying TCP by sending an ICMP communication prohibited packet.  **Choices:**   - `"enable"` - `"disable"` |
| **detect_unknown_esp**  string | Enable/disable detection of unknown ESP packets .  **Choices:**   - `"enable"` - `"disable"` |
| **device**  string | Interface to use for management access for NAT mode. Source system.interface.name. |
| **dhcp6_server_ip**  list / elements=string | DHCPv6 server IPv6 address. |
| **dhcp_proxy**  string | Enable/disable the DHCP Proxy.  **Choices:**   - `"enable"` - `"disable"` |
| **dhcp_proxy_interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **dhcp_proxy_interface_select_method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **dhcp_server_ip**  list / elements=string | DHCP Server IPv4 address. |
| **discovered_device_timeout**  integer | Timeout for discovered devices (1 - 365 days). |
| **dyn_addr_session_check**  string | Enable/disable dirty session check caused by dynamic address updates.  **Choices:**   - `"enable"` - `"disable"` |
| **ecmp_max_paths**  integer | Maximum number of Equal Cost Multi-Path (ECMP) next-hops. Set to 1 to disable ECMP routing (1 - 255). |
| **email_portal_check_dns**  string | Enable/disable using DNS to validate email addresses collected by a captive portal.  **Choices:**   - `"disable"` - `"enable"` |
| **ext_resource_session_check**  string | Enable/disable dirty session check caused by external resource updates.  **Choices:**   - `"enable"` - `"disable"` |
| **firewall_session_dirty**  string | Select how to manage sessions affected by firewall policy configuration changes.  **Choices:**   - `"check-all"` - `"check-new"` - `"check-policy-option"` |
| **fqdn_session_check**  string | Enable/disable dirty session check caused by FQDN updates.  **Choices:**   - `"enable"` - `"disable"` |
| **fw_session_hairpin**  string | Enable/disable checking for a matching policy each time hairpin traffic goes through the FortiGate.  **Choices:**   - `"enable"` - `"disable"` |
| **gateway**  string | Transparent mode IPv4 default gateway IP address. |
| **gateway6**  string | Transparent mode IPv6 default gateway IP address. |
| **gtp_asym_fgsp**  string | Enable/disable GTP asymmetric traffic handling on FGSP.  **Choices:**   - `"disable"` - `"enable"` |
| **gtp_monitor_mode**  string | Enable/disable GTP monitor mode (VDOM level).  **Choices:**   - `"enable"` - `"disable"` |
| **gui_advanced_policy**  string | Enable/disable advanced policy configuration on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_advanced_wireless_features**  string | Enable/disable advanced wireless features in GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_allow_unnamed_policy**  string | Enable/disable the requirement for policy naming on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_antivirus**  string | Enable/disable AntiVirus on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_ap_profile**  string | Enable/disable FortiAP profiles on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_application_control**  string | Enable/disable application control on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_casb**  string | Enable/disable Inline-CASB on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_default_policy_columns**  list / elements=dictionary | Default columns to display for policy lists on GUI. |
| **name**  string / required | Select column name. |
| **gui_dhcp_advanced**  string | Enable/disable advanced DHCP options on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_dlp**  string | Enable/disable DLP on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_dlp_profile**  string | Enable/disable Data Leak Prevention on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_dns_database**  string | Enable/disable DNS database settings on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_dnsfilter**  string | Enable/disable DNS Filtering on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_domain_ip_reputation**  string | Enable/disable Domain and IP Reputation on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_dos_policy**  string | Enable/disable DoS policies on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_dynamic_device_os_id**  string | Enable/disable Create dynamic addresses to manage known devices.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_dynamic_profile_display**  string | Enable/disable RADIUS Single Sign On (RSSO) on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_dynamic_routing**  string | Enable/disable dynamic routing on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_email_collection**  string | Enable/disable email collection on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_endpoint_control**  string | Enable/disable endpoint control on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_endpoint_control_advanced**  string | Enable/disable advanced endpoint control options on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_enforce_change_summary**  string | Enforce change summaries for select tables in the GUI.  **Choices:**   - `"disable"` - `"require"` - `"optional"` |
| **gui_explicit_proxy**  string | Enable/disable the explicit proxy on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_file_filter**  string | Enable/disable File-filter on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_fortiap_split_tunneling**  string | Enable/disable FortiAP split tunneling on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_fortiextender_controller**  string | Enable/disable FortiExtender on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_icap**  string | Enable/disable ICAP on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_implicit_policy**  string | Enable/disable implicit firewall policies on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_ips**  string | Enable/disable IPS on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_load_balance**  string | Enable/disable server load balancing on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_local_in_policy**  string | Enable/disable Local-In policies on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_local_reports**  string | Enable/disable local reports on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_multicast_policy**  string | Enable/disable multicast firewall policies on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_multiple_interface_policy**  string | Enable/disable adding multiple interfaces to a policy on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_multiple_utm_profiles**  string | Enable/disable multiple UTM profiles on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_nat46_64**  string | Enable/disable NAT46 and NAT64 settings on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_object_colors**  string | Enable/disable object colors on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_ot**  string | Enable/disable Operational technology features on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_per_policy_disclaimer**  string | Enable/disable policy disclaimer on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_policy_based_ipsec**  string | Enable/disable policy-based IPsec VPN on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_policy_disclaimer**  string | Enable/disable policy disclaimer on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_policy_learning**  string | Enable/disable firewall policy learning mode on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_proxy_inspection**  string | Enable/disable the proxy features on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_replacement_message_groups**  string | Enable/disable replacement message groups on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_route_tag_address_creation**  string | Enable/disable route-tag addresses on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_security_profile_group**  string | Enable/disable Security Profile Groups on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_spamfilter**  string | Enable/disable Antispam on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_sslvpn**  string | Enable/disable SSL-VPN settings pages on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_sslvpn_personal_bookmarks**  string | Enable/disable SSL-VPN personal bookmark management on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_sslvpn_realms**  string | Enable/disable SSL-VPN realms on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_switch_controller**  string | Enable/disable the switch controller on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_threat_weight**  string | Enable/disable threat weight on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_traffic_shaping**  string | Enable/disable traffic shaping on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_videofilter**  string | Enable/disable Video filtering on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_virtual_patch_profile**  string | Enable/disable Virtual Patching on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_voip_profile**  string | Enable/disable VoIP profiles on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_vpn**  string | Enable/disable IPsec VPN settings pages on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_waf_profile**  string | Enable/disable Web Application Firewall on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_wan_load_balancing**  string | Enable/disable SD-WAN on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_wanopt_cache**  string | Enable/disable WAN Optimization and Web Caching on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_webfilter**  string | Enable/disable Web filtering on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_webfilter_advanced**  string | Enable/disable advanced web filtering on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_wireless_controller**  string | Enable/disable the wireless controller on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **gui_ztna**  string | Enable/disable Zero Trust Network Access features on the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **h323_direct_model**  string | Enable/disable H323 direct model.  **Choices:**   - `"disable"` - `"enable"` |
| **http_external_dest**  string | Offload HTTP traffic to FortiWeb or FortiCache.  **Choices:**   - `"fortiweb"` - `"forticache"` |
| **ike_dn_format**  string | Configure IKE ASN.1 Distinguished Name format conventions.  **Choices:**   - `"with-space"` - `"no-space"` |
| **ike_policy_route**  string | Enable/disable IKE Policy Based Routing (PBR).  **Choices:**   - `"enable"` - `"disable"` |
| **ike_port**  integer | UDP port for IKE/IPsec traffic . |
| **ike_quick_crash_detect**  string | Enable/disable IKE quick crash detection (RFC 6290).  **Choices:**   - `"enable"` - `"disable"` |
| **ike_session_resume**  string | Enable/disable IKEv2 session resumption (RFC 5723).  **Choices:**   - `"enable"` - `"disable"` |
| **implicit_allow_dns**  string | Enable/disable implicitly allowing DNS traffic.  **Choices:**   - `"enable"` - `"disable"` |
| **inspection_mode**  string | Inspection mode (proxy-based or flow-based).  **Choices:**   - `"proxy"` - `"flow"` |
| **internet_service_database_cache**  string | Enable/disable Internet Service database caching.  **Choices:**   - `"disable"` - `"enable"` |
| **ip**  string | IP address and netmask. |
| **ip6**  string | IPv6 address prefix for NAT mode. |
| **lan_extension_controller_addr**  string | Controller IP address or FQDN to connect. |
| **link_down_access**  string | Enable/disable link down access traffic.  **Choices:**   - `"enable"` - `"disable"` |
| **lldp_reception**  string | Enable/disable Link Layer Discovery Protocol (LLDP) reception for this VDOM or apply global settings to this VDOM.  **Choices:**   - `"enable"` - `"disable"` - `"global"` |
| **lldp_transmission**  string | Enable/disable Link Layer Discovery Protocol (LLDP) transmission for this VDOM or apply global settings to this VDOM.  **Choices:**   - `"enable"` - `"disable"` - `"global"` |
| **location_id**  string | Local location ID in the form of an IPv4 address. |
| **mac_ttl**  integer | Duration of MAC addresses in Transparent mode (300 - 8640000 sec). |
| **manageip**  string | Transparent mode IPv4 management IP address and netmask. |
| **manageip6**  string | Transparent mode IPv6 management IP address and netmask. |
| **multicast_forward**  string | Enable/disable multicast forwarding.  **Choices:**   - `"enable"` - `"disable"` |
| **multicast_skip_policy**  string | Enable/disable allowing multicast traffic through the FortiGate without a policy check.  **Choices:**   - `"enable"` - `"disable"` |
| **multicast_ttl_notchange**  string | Enable/disable preventing the FortiGate from changing the TTL for forwarded multicast packets.  **Choices:**   - `"enable"` - `"disable"` |
| **nat46_force_ipv4_packet_forwarding**  string | Enable/disable mandatory IPv4 packet forwarding in NAT46.  **Choices:**   - `"enable"` - `"disable"` |
| **nat46_generate_ipv6_fragment_header**  string | Enable/disable NAT46 IPv6 fragment header generation.  **Choices:**   - `"enable"` - `"disable"` |
| **nat64_force_ipv6_packet_forwarding**  string | Enable/disable mandatory IPv6 packet forwarding in NAT64.  **Choices:**   - `"enable"` - `"disable"` |
| **ngfw_mode**  string | Next Generation Firewall (NGFW) mode.  **Choices:**   - `"profile-based"` - `"policy-based"` |
| **opmode**  string | Firewall operation mode (NAT or Transparent).  **Choices:**   - `"nat"` - `"transparent"` |
| **pfcp_monitor_mode**  string | Enable/disable PFCP monitor mode (VDOM level).  **Choices:**   - `"enable"` - `"disable"` |
| **prp_trailer_action**  string | Enable/disable action to take on PRP trailer.  **Choices:**   - `"enable"` - `"disable"` |
| **sccp_port**  integer | TCP port the SCCP proxy monitors for SCCP traffic (0 - 65535). |
| **sctp_session_without_init**  string | Enable/disable SCTP session creation without SCTP INIT.  **Choices:**   - `"enable"` - `"disable"` |
| **ses_denied_traffic**  string | Enable/disable including denied session in the session table.  **Choices:**   - `"enable"` - `"disable"` |
| **sip_expectation**  string | Enable/disable the SIP kernel session helper to create an expectation for port 5060.  **Choices:**   - `"enable"` - `"disable"` |
| **sip_helper**  string | Enable/disable the SIP session helper to process SIP sessions unless SIP sessions are accepted by the SIP application layer gateway (ALG).  **Choices:**   - `"enable"` - `"disable"` |
| **sip_nat_trace**  string | Enable/disable recording the original SIP source IP address when NAT is used.  **Choices:**   - `"enable"` - `"disable"` |
| **sip_ssl_port**  integer | TCP port the SIP proxy monitors for SIP SSL/TLS traffic (0 - 65535). |
| **sip_tcp_port**  list / elements=integer | TCP port the SIP proxy monitors for SIP traffic (0 - 65535). |
| **sip_udp_port**  list / elements=integer | UDP port the SIP proxy monitors for SIP traffic (0 - 65535). |
| **snat_hairpin_traffic**  string | Enable/disable source NAT (SNAT) for hairpin traffic.  **Choices:**   - `"enable"` - `"disable"` |
| **ssl_ssh_profile**  string | Profile for SSL/SSH inspection. Source firewall.ssl-ssh-profile.name. |
| **status**  string | Enable/disable this VDOM.  **Choices:**   - `"enable"` - `"disable"` |
| **strict_src_check**  string | Enable/disable strict source verification.  **Choices:**   - `"enable"` - `"disable"` |
| **tcp_session_without_syn**  string | Enable/disable allowing TCP session without SYN flags.  **Choices:**   - `"enable"` - `"disable"` |
| **utf8_spam_tagging**  string | Enable/disable converting antispam tags to UTF-8 for better non-ASCII character support.  **Choices:**   - `"enable"` - `"disable"` |
| **v4_ecmp_mode**  string | IPv4 Equal-cost multi-path (ECMP) routing and load balancing mode.  **Choices:**   - `"source-ip-based"` - `"weight-based"` - `"usage-based"` - `"source-dest-ip-based"` |
| **vdom_type**  string | Vdom type (traffic, lan-extension or admin).  **Choices:**   - `"traffic"` - `"lan-extension"` - `"admin"` |
| **vpn_stats_log**  list / elements=string | Enable/disable periodic VPN log statistics for one or more types of VPN. Separate names with a space.  **Choices:**   - `"ipsec"` - `"pptp"` - `"l2tp"` - `"ssl"` |
| **vpn_stats_period**  integer | Period to send VPN log statistics (0 or 60 - 86400 sec). |
| **wccp_cache_engine**  string | Enable/disable WCCP cache engine.  **Choices:**   - `"enable"` - `"disable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_settings_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_settings_module.md#id5)

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
  - name: Configure VDOM settings.
    fortios_system_settings:
      vdom:  "{{ vdom }}"
      system_settings:
        allow_linkdown_path: "enable"
        allow_subnet_overlap: "enable"
        application_bandwidth_tracking: "disable"
        asymroute: "enable"
        asymroute_icmp: "enable"
        asymroute6: "enable"
        asymroute6_icmp: "enable"
        auxiliary_session: "enable"
        bfd: "enable"
        bfd_desired_min_tx: "250"
        bfd_detect_mult: "3"
        bfd_dont_enforce_src_port: "enable"
        bfd_required_min_rx: "250"
        block_land_attack: "disable"
        central_nat: "enable"
        comments: "<your_own_value>"
        compliance_check: "enable"
        consolidated_firewall_mode: "enable"
        default_app_port_as_service: "enable"
        default_policy_expiry_days: "30"
        default_voip_alg_mode: "proxy-based"
        deny_tcp_with_icmp: "enable"
        detect_unknown_esp: "enable"
        device: "<your_own_value> (source system.interface.name)"
        dhcp_proxy: "enable"
        dhcp_proxy_interface: "<your_own_value> (source system.interface.name)"
        dhcp_proxy_interface_select_method: "auto"
        dhcp_server_ip: "<your_own_value>"
        dhcp6_server_ip: "<your_own_value>"
        discovered_device_timeout: "28"
        dyn_addr_session_check: "enable"
        ecmp_max_paths: "255"
        email_portal_check_dns: "disable"
        ext_resource_session_check: "enable"
        firewall_session_dirty: "check-all"
        fqdn_session_check: "enable"
        fw_session_hairpin: "enable"
        gateway: "<your_own_value>"
        gateway6: "<your_own_value>"
        gtp_asym_fgsp: "disable"
        gtp_monitor_mode: "enable"
        gui_advanced_policy: "enable"
        gui_advanced_wireless_features: "enable"
        gui_allow_unnamed_policy: "enable"
        gui_antivirus: "enable"
        gui_ap_profile: "enable"
        gui_application_control: "enable"
        gui_casb: "enable"
        gui_default_policy_columns:
         -
            name: "default_name_52"
        gui_dhcp_advanced: "enable"
        gui_dlp: "enable"
        gui_dlp_profile: "enable"
        gui_dns_database: "enable"
        gui_dnsfilter: "enable"
        gui_domain_ip_reputation: "enable"
        gui_dos_policy: "enable"
        gui_dynamic_device_os_id: "enable"
        gui_dynamic_profile_display: "enable"
        gui_dynamic_routing: "enable"
        gui_email_collection: "enable"
        gui_endpoint_control: "enable"
        gui_endpoint_control_advanced: "enable"
        gui_enforce_change_summary: "disable"
        gui_explicit_proxy: "enable"
        gui_file_filter: "enable"
        gui_fortiap_split_tunneling: "enable"
        gui_fortiextender_controller: "enable"
        gui_icap: "enable"
        gui_implicit_policy: "enable"
        gui_ips: "enable"
        gui_load_balance: "enable"
        gui_local_in_policy: "enable"
        gui_local_reports: "enable"
        gui_multicast_policy: "enable"
        gui_multiple_interface_policy: "enable"
        gui_multiple_utm_profiles: "enable"
        gui_nat46_64: "enable"
        gui_object_colors: "enable"
        gui_ot: "enable"
        gui_per_policy_disclaimer: "enable"
        gui_policy_based_ipsec: "enable"
        gui_policy_disclaimer: "enable"
        gui_policy_learning: "enable"
        gui_proxy_inspection: "enable"
        gui_replacement_message_groups: "enable"
        gui_route_tag_address_creation: "enable"
        gui_security_profile_group: "enable"
        gui_spamfilter: "enable"
        gui_sslvpn: "enable"
        gui_sslvpn_personal_bookmarks: "enable"
        gui_sslvpn_realms: "enable"
        gui_switch_controller: "enable"
        gui_threat_weight: "enable"
        gui_traffic_shaping: "enable"
        gui_videofilter: "enable"
        gui_virtual_patch_profile: "enable"
        gui_voip_profile: "enable"
        gui_vpn: "enable"
        gui_waf_profile: "enable"
        gui_wan_load_balancing: "enable"
        gui_wanopt_cache: "enable"
        gui_webfilter: "enable"
        gui_webfilter_advanced: "enable"
        gui_wireless_controller: "enable"
        gui_ztna: "enable"
        h323_direct_model: "disable"
        http_external_dest: "fortiweb"
        ike_dn_format: "with-space"
        ike_policy_route: "enable"
        ike_port: "500"
        ike_quick_crash_detect: "enable"
        ike_session_resume: "enable"
        implicit_allow_dns: "enable"
        inspection_mode: "proxy"
        internet_service_database_cache: "disable"
        ip: "<your_own_value>"
        ip6: "<your_own_value>"
        lan_extension_controller_addr: "<your_own_value>"
        link_down_access: "enable"
        lldp_reception: "enable"
        lldp_transmission: "enable"
        location_id: "<your_own_value>"
        mac_ttl: "300"
        manageip: "<your_own_value>"
        manageip6: "<your_own_value>"
        multicast_forward: "enable"
        multicast_skip_policy: "enable"
        multicast_ttl_notchange: "enable"
        nat46_force_ipv4_packet_forwarding: "enable"
        nat46_generate_ipv6_fragment_header: "enable"
        nat64_force_ipv6_packet_forwarding: "enable"
        ngfw_mode: "profile-based"
        opmode: "nat"
        pfcp_monitor_mode: "enable"
        prp_trailer_action: "enable"
        sccp_port: "2000"
        sctp_session_without_init: "enable"
        ses_denied_traffic: "enable"
        sip_expectation: "enable"
        sip_helper: "enable"
        sip_nat_trace: "enable"
        sip_ssl_port: "5061"
        sip_tcp_port: "<your_own_value>"
        sip_udp_port: "<your_own_value>"
        snat_hairpin_traffic: "enable"
        ssl_ssh_profile: "<your_own_value> (source firewall.ssl-ssh-profile.name)"
        status: "enable"
        strict_src_check: "enable"
        tcp_session_without_syn: "enable"
        utf8_spam_tagging: "enable"
        v4_ecmp_mode: "source-ip-based"
        vdom_type: "traffic"
        vpn_stats_log: "ipsec"
        vpn_stats_period: "600"
        wccp_cache_engine: "enable"
```

## [Return Values](fortios_system_settings_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
