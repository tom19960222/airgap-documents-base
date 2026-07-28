---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_wireless_controller_vap module – Configure Virtual Access Points (VAPs) in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_wireless_controller_vap_module.html
fetched_at: 2026-07-27T17:47:24+00:00
---
# fortinet.fortios.fortios_wireless_controller_vap module – Configure Virtual Access Points (VAPs) in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_vap_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-vap-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_vap`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_vap_module.md#synopsis)
- [Requirements](fortios_wireless_controller_vap_module.md#requirements)
- [Parameters](fortios_wireless_controller_vap_module.md#parameters)
- [Notes](fortios_wireless_controller_vap_module.md#notes)
- [Examples](fortios_wireless_controller_vap_module.md#examples)
- [Return Values](fortios_wireless_controller_vap_module.md#return-values)

## [Synopsis](fortios_wireless_controller_vap_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and vap category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_vap_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_wireless_controller_vap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **wireless_controller_vap**  dictionary | Configure Virtual Access Points (VAPs). |
| **access_control_list**  string | Profile name for access-control-list. Source wireless-controller.access-control-list.name. |
| **acct_interim_interval**  integer | WiFi RADIUS accounting interim interval (60 - 86400 sec). |
| **additional_akms**  list / elements=string | Additional AKMs.  Choices:   - `"akm6"` |
| **address_group**  string | Firewall Address Group Name. Source firewall.addrgrp.name. |
| **address_group_policy**  string | Configure MAC address filtering policy for MAC addresses that are in the address-group.  Choices:   - `"disable"` - `"allow"` - `"deny"` |
| **alias**  string | Alias. |
| **antivirus_profile**  string | AntiVirus profile name. Source antivirus.profile.name. |
| **application_detection_engine**  string | Enable/disable application detection engine .  Choices:   - `"enable"` - `"disable"` |
| **application_dscp_marking**  string | Enable/disable application attribute based DSCP marking .  Choices:   - `"enable"` - `"disable"` |
| **application_list**  string | Application control list name. Source application.list.name. |
| **application_report_intv**  integer | Application report interval (30 - 864000 sec). |
| **atf_weight**  integer | Airtime weight in percentage . |
| **auth**  string | Authentication protocol.  Choices:   - `"psk"` - `"radius"` - `"usergroup"` |
| **auth_cert**  string | HTTPS server certificate. Source vpn.certificate.local.name. |
| **auth_portal_addr**  string | Address of captive portal. |
| **beacon_advertising**  list / elements=string | Fortinet beacon advertising IE data .  Choices:   - `"name"` - `"model"` - `"serial-number"` |
| **broadcast_ssid**  string | Enable/disable broadcasting the SSID .  Choices:   - `"enable"` - `"disable"` |
| **broadcast_suppression**  list / elements=string | Optional suppression of broadcast messages. For example, you can keep DHCP messages, ARP broadcasts, and so on off of the wireless network.  Choices:   - `"dhcp-up"` - `"dhcp-down"` - `"dhcp-starvation"` - `"dhcp-ucast"` - `"arp-known"` - `"arp-unknown"` - `"arp-reply"` - `"arp-poison"` - `"arp-proxy"` - `"netbios-ns"` - `"netbios-ds"` - `"ipv6"` - `"all-other-mc"` - `"all-other-bc"` |
| **bss_color_partial**  string | Enable/disable 802.11ax partial BSS color .  Choices:   - `"enable"` - `"disable"` |
| **bstm_disassociation_imminent**  string | Enable/disable forcing of disassociation after the BSTM request timer has been reached .  Choices:   - `"enable"` - `"disable"` |
| **bstm_load_balancing_disassoc_timer**  integer | Time interval for client to voluntarily leave AP before forcing a disassociation due to AP load-balancing (0 to 30). |
| **bstm_rssi_disassoc_timer**  integer | Time interval for client to voluntarily leave AP before forcing a disassociation due to low RSSI (0 to 2000). |
| **captive_portal_ac_name**  string | Local-bridging captive portal ac-name. |
| **captive_portal_auth_timeout**  integer | Hard timeout - AP will always clear the session after timeout regardless of traffic (0 - 864000 sec). |
| **captive_portal_macauth_radius_secret**  string | Secret key to access the macauth RADIUS server. |
| **captive_portal_macauth_radius_server**  string | Captive portal external RADIUS server domain name or IP address. |
| **captive_portal_radius_secret**  string | Secret key to access the RADIUS server. |
| **captive_portal_radius_server**  string | Captive portal RADIUS server domain name or IP address. |
| **captive_portal_session_timeout_interval**  integer | Session timeout interval (0 - 864000 sec). |
| **dhcp_address_enforcement**  string | Enable/disable DHCP address enforcement .  Choices:   - `"enable"` - `"disable"` |
| **dhcp_lease_time**  integer | DHCP lease time in seconds for NAT IP address. |
| **dhcp_option43_insertion**  string | Enable/disable insertion of DHCP option 43 .  Choices:   - `"enable"` - `"disable"` |
| **dhcp_option82_circuit_id_insertion**  string | Enable/disable DHCP option 82 circuit-id insert .  Choices:   - `"style-1"` - `"style-2"` - `"style-3"` - `"disable"` |
| **dhcp_option82_insertion**  string | Enable/disable DHCP option 82 insert .  Choices:   - `"enable"` - `"disable"` |
| **dhcp_option82_remote_id_insertion**  string | Enable/disable DHCP option 82 remote-id insert .  Choices:   - `"style-1"` - `"disable"` |
| **dynamic_vlan**  string | Enable/disable dynamic VLAN assignment.  Choices:   - `"enable"` - `"disable"` |
| **eap_reauth**  string | Enable/disable EAP re-authentication for WPA-Enterprise security.  Choices:   - `"enable"` - `"disable"` |
| **eap_reauth_intv**  integer | EAP re-authentication interval (1800 - 864000 sec). |
| **eapol_key_retries**  string | Enable/disable retransmission of EAPOL-Key frames (message 3/4 and group message 1/2) .  Choices:   - `"disable"` - `"enable"` |
| **encrypt**  string | Encryption protocol to use (only available when security is set to a WPA type).  Choices:   - `"TKIP"` - `"AES"` - `"TKIP-AES"` |
| **external_fast_roaming**  string | Enable/disable fast roaming or pre-authentication with external APs not managed by the FortiGate .  Choices:   - `"enable"` - `"disable"` |
| **external_logout**  string | URL of external authentication logout server. |
| **external_web**  string | URL of external authentication web server. |
| **external_web_format**  string | URL query parameter detection .  Choices:   - `"auto-detect"` - `"no-query-string"` - `"partial-query-string"` |
| **fast_bss_transition**  string | Enable/disable 802.11r Fast BSS Transition (FT) .  Choices:   - `"disable"` - `"enable"` |
| **fast_roaming**  string | Enable/disable fast-roaming, or pre-authentication, where supported by clients .  Choices:   - `"enable"` - `"disable"` |
| **ft_mobility_domain**  integer | Mobility domain identifier in FT (1 - 65535). |
| **ft_over_ds**  string | Enable/disable FT over the Distribution System (DS).  Choices:   - `"disable"` - `"enable"` |
| **ft_r0_key_lifetime**  integer | Lifetime of the PMK-R0 key in FT, 1-65535 minutes. |
| **gas_comeback_delay**  integer | GAS comeback delay (0 or 100 - 10000 milliseconds). |
| **gas_fragmentation_limit**  integer | GAS fragmentation limit (512 - 4096). |
| **gtk_rekey**  string | Enable/disable GTK rekey for WPA security.  Choices:   - `"enable"` - `"disable"` |
| **gtk_rekey_intv**  integer | GTK rekey interval (1800 - 864000 sec). |
| **high_efficiency**  string | Enable/disable 802.11ax high efficiency .  Choices:   - `"enable"` - `"disable"` |
| **hotspot20_profile**  string | Hotspot 2.0 profile name. Source wireless-controller.hotspot20.hs-profile.name. |
| **igmp_snooping**  string | Enable/disable IGMP snooping.  Choices:   - `"enable"` - `"disable"` |
| **intra_vap_privacy**  string | Enable/disable blocking communication between clients on the same SSID (called intra-SSID privacy) .  Choices:   - `"enable"` - `"disable"` |
| **ip**  string | IP address and subnet mask for the local standalone NAT subnet. |
| **ips_sensor**  string | IPS sensor name. Source ips.sensor.name. |
| **ipv6_rules**  list / elements=string | Optional rules of IPv6 packets. For example, you can keep RA, RS and so on off of the wireless network.  Choices:   - `"drop-icmp6ra"` - `"drop-icmp6rs"` - `"drop-llmnr6"` - `"drop-icmp6mld2"` - `"drop-dhcp6s"` - `"drop-dhcp6c"` - `"ndp-proxy"` - `"drop-ns-dad"` - `"drop-ns-nondad"` |
| **key**  string | WEP Key. |
| **keyindex**  integer | WEP key index (1 - 4). |
| **l3_roaming**  string | Enable/disable layer 3 roaming .  Choices:   - `"enable"` - `"disable"` |
| **l3_roaming_mode**  string | Select the way that layer 3 roaming traffic is passed .  Choices:   - `"direct"` - `"indirect"` |
| **ldpc**  string | VAP low-density parity-check (LDPC) coding configuration.  Choices:   - `"disable"` - `"rx"` - `"tx"` - `"rxtx"` |
| **local_authentication**  string | Enable/disable AP local authentication.  Choices:   - `"enable"` - `"disable"` |
| **local_bridging**  string | Enable/disable bridging of wireless and Ethernet interfaces on the FortiAP .  Choices:   - `"enable"` - `"disable"` |
| **local_lan**  string | Allow/deny traffic destined for a Class A, B, or C private IP address .  Choices:   - `"allow"` - `"deny"` |
| **local_standalone**  string | Enable/disable AP local standalone .  Choices:   - `"enable"` - `"disable"` |
| **local_standalone_dns**  string | Enable/disable AP local standalone DNS.  Choices:   - `"enable"` - `"disable"` |
| **local_standalone_dns_ip**  list / elements=string | IPv4 addresses for the local standalone DNS. |
| **local_standalone_nat**  string | Enable/disable AP local standalone NAT mode.  Choices:   - `"enable"` - `"disable"` |
| **mac_auth_bypass**  string | Enable/disable MAC authentication bypass.  Choices:   - `"enable"` - `"disable"` |
| **mac_called_station_delimiter**  string | MAC called station delimiter .  Choices:   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac_calling_station_delimiter**  string | MAC calling station delimiter .  Choices:   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac_case**  string | MAC case .  Choices:   - `"uppercase"` - `"lowercase"` |
| **mac_filter**  string | Enable/disable MAC filtering to block wireless clients by mac address.  Choices:   - `"enable"` - `"disable"` |
| **mac_filter_list**  list / elements=dictionary | Create a list of MAC addresses for MAC address filtering. |
| **id**  integer | ID. |
| **mac**  string | MAC address. |
| **mac_filter_policy**  string | Deny or allow the client with this MAC address.  Choices:   - `"allow"` - `"deny"` |
| **mac_filter_policy_other**  string | Allow or block clients with MAC addresses that are not in the filter list.  Choices:   - `"allow"` - `"deny"` |
| **mac_password_delimiter**  string | MAC authentication password delimiter .  Choices:   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac_username_delimiter**  string | MAC authentication username delimiter .  Choices:   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **max_clients**  integer | Maximum number of clients that can connect simultaneously to the VAP . |
| **max_clients_ap**  integer | Maximum number of clients that can connect simultaneously to the VAP per AP radio . |
| **mbo**  string | Enable/disable Multiband Operation .  Choices:   - `"disable"` - `"enable"` |
| **mbo_cell_data_conn_pref**  string | MBO cell data connection preference (0, 1, or 255).  Choices:   - `"excluded"` - `"prefer-not"` - `"prefer-use"` |
| **me_disable_thresh**  integer | Disable multicast enhancement when this many clients are receiving multicast traffic. |
| **mesh_backhaul**  string | Enable/disable using this VAP as a WiFi mesh backhaul . This entry is only available when security is set to a WPA type or open.  Choices:   - `"enable"` - `"disable"` |
| **mpsk**  string | Enable/disable multiple PSK authentication.  Choices:   - `"enable"` - `"disable"` |
| **mpsk_concurrent_clients**  integer | Maximum number of concurrent clients that connect using the same passphrase in multiple PSK authentication (0 - 65535). |
| **mpsk_key**  list / elements=dictionary | List of multiple PSK entries. |
| **comment**  string | Comment. |
| **concurrent_clients**  string | Number of clients that can connect using this pre-shared key. |
| **key_name**  string | Pre-shared key name. |
| **mpsk_schedules**  list / elements=dictionary | Firewall schedule for MPSK passphrase. The passphrase will be effective only when at least one schedule is valid. |
| **name**  string | Schedule name. Source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name. |
| **passphrase**  string | WPA Pre-shared key. |
| **mpsk_profile**  string | MPSK profile name. Source wireless-controller.mpsk-profile.name. |
| **mu_mimo**  string | Enable/disable Multi-user MIMO .  Choices:   - `"enable"` - `"disable"` |
| **multicast_enhance**  string | Enable/disable converting multicast to unicast to improve performance .  Choices:   - `"enable"` - `"disable"` |
| **multicast_rate**  string | Multicast rate (0, 6000, 12000, or 24000 kbps).  Choices:   - `"0"` - `"6000"` - `"12000"` - `"24000"` |
| **nac**  string | Enable/disable network access control.  Choices:   - `"enable"` - `"disable"` |
| **nac_profile**  string | NAC profile name. Source wireless-controller.nac-profile.name. |
| **name**  string / required | Virtual AP name. |
| **neighbor_report_dual_band**  string | Enable/disable dual-band neighbor report .  Choices:   - `"disable"` - `"enable"` |
| **okc**  string | Enable/disable Opportunistic Key Caching (OKC) .  Choices:   - `"disable"` - `"enable"` |
| **osen**  string | Enable/disable OSEN as part of key management .  Choices:   - `"enable"` - `"disable"` |
| **owe_groups**  list / elements=string | OWE-Groups.  Choices:   - `"19"` - `"20"` - `"21"` |
| **owe_transition**  string | Enable/disable OWE transition mode support.  Choices:   - `"disable"` - `"enable"` |
| **owe_transition_ssid**  string | OWE transition mode peer SSID. |
| **passphrase**  string | WPA pre-shared key (PSK) to be used to authenticate WiFi users. |
| **pmf**  string | Protected Management Frames (PMF) support .  Choices:   - `"disable"` - `"enable"` - `"optional"` |
| **pmf_assoc_comeback_timeout**  integer | Protected Management Frames (PMF) comeback maximum timeout (1-20 sec). |
| **pmf_sa_query_retry_timeout**  integer | Protected Management Frames (PMF) SA query retry timeout interval (1 - 5 100s of msec). |
| **port_macauth**  string | Enable/disable LAN port MAC authentication .  Choices:   - `"disable"` - `"radius"` - `"address-group"` |
| **port_macauth_reauth_timeout**  integer | LAN port MAC authentication re-authentication timeout value . |
| **port_macauth_timeout**  integer | LAN port MAC authentication idle timeout value . |
| **portal_message_override_group**  string | Replacement message group for this VAP (only available when security is set to a captive portal type). Source system.replacemsg-group .name. |
| **portal_message_overrides**  dictionary | Individual message overrides. |
| **auth_disclaimer_page**  string | Override auth-disclaimer-page message with message from portal-message-overrides group. |
| **auth_login_failed_page**  string | Override auth-login-failed-page message with message from portal-message-overrides group. |
| **auth_login_page**  string | Override auth-login-page message with message from portal-message-overrides group. |
| **auth_reject_page**  string | Override auth-reject-page message with message from portal-message-overrides group. |
| **portal_type**  string | Captive portal functionality. Configure how the captive portal authenticates users and whether it includes a disclaimer.  Choices:   - `"auth"` - `"auth+disclaimer"` - `"disclaimer"` - `"email-collect"` - `"cmcc"` - `"cmcc-macauth"` - `"auth-mac"` - `"external-auth"` - `"external-macauth"` |
| **primary_wag_profile**  string | Primary wireless access gateway profile name. Source wireless-controller.wag-profile.name. |
| **probe_resp_suppression**  string | Enable/disable probe response suppression (to ignore weak signals) .  Choices:   - `"enable"` - `"disable"` |
| **probe_resp_threshold**  string | Minimum signal level/threshold in dBm required for the AP response to probe requests (-95 to -20). |
| **ptk_rekey**  string | Enable/disable PTK rekey for WPA-Enterprise security.  Choices:   - `"enable"` - `"disable"` |
| **ptk_rekey_intv**  integer | PTK rekey interval (1800 - 864000 sec). |
| **qos_profile**  string | Quality of service profile name. Source wireless-controller.qos-profile.name. |
| **quarantine**  string | Enable/disable station quarantine .  Choices:   - `"enable"` - `"disable"` |
| **radio_2g_threshold**  string | Minimum signal level/threshold in dBm required for the AP response to receive a packet in 2.4G band (-95 to -20). |
| **radio_5g_threshold**  string | Minimum signal level/threshold in dBm required for the AP response to receive a packet in 5G band(-95 to -20). |
| **radio_sensitivity**  string | Enable/disable software radio sensitivity (to ignore weak signals) .  Choices:   - `"enable"` - `"disable"` |
| **radius_mac_auth**  string | Enable/disable RADIUS-based MAC authentication of clients .  Choices:   - `"enable"` - `"disable"` |
| **radius_mac_auth_server**  string | RADIUS-based MAC authentication server. Source user.radius.name. |
| **radius_mac_auth_usergroups**  list / elements=dictionary | Selective user groups that are permitted for RADIUS mac authentication. |
| **name**  string | User group name. |
| **radius_mac_mpsk_auth**  string | Enable/disable RADIUS-based MAC authentication of clients for MPSK authentication .  Choices:   - `"enable"` - `"disable"` |
| **radius_mac_mpsk_timeout**  integer | RADIUS MAC MPSK cache timeout interval (0 or 300 - 864000). |
| **radius_server**  string | RADIUS server to be used to authenticate WiFi users. Source user.radius.name. |
| **rates_11a**  list / elements=string | Allowed data rates for 802.11a.  Choices:   - `"1"` - `"1-basic"` - `"2"` - `"2-basic"` - `"5.5"` - `"5.5-basic"` - `"11"` - `"11-basic"` - `"6"` - `"6-basic"` - `"9"` - `"9-basic"` - `"12"` - `"12-basic"` - `"18"` - `"18-basic"` - `"24"` - `"24-basic"` - `"36"` - `"36-basic"` - `"48"` - `"48-basic"` - `"54"` - `"54-basic"` |
| **rates_11ac_mcs_map**  string | Comma separated list of max supported VHT MCS for spatial streams 1 through 8. |
| **rates_11ac_ss12**  list / elements=string | Allowed data rates for 802.11ac with 1 or 2 spatial streams.  Choices:   - `"mcs0/1"` - `"mcs1/1"` - `"mcs2/1"` - `"mcs3/1"` - `"mcs4/1"` - `"mcs5/1"` - `"mcs6/1"` - `"mcs7/1"` - `"mcs8/1"` - `"mcs9/1"` - `"mcs10/1"` - `"mcs11/1"` - `"mcs0/2"` - `"mcs1/2"` - `"mcs2/2"` - `"mcs3/2"` - `"mcs4/2"` - `"mcs5/2"` - `"mcs6/2"` - `"mcs7/2"` - `"mcs8/2"` - `"mcs9/2"` - `"mcs10/2"` - `"mcs11/2"` |
| **rates_11ac_ss34**  list / elements=string | Allowed data rates for 802.11ac with 3 or 4 spatial streams.  Choices:   - `"mcs0/3"` - `"mcs1/3"` - `"mcs2/3"` - `"mcs3/3"` - `"mcs4/3"` - `"mcs5/3"` - `"mcs6/3"` - `"mcs7/3"` - `"mcs8/3"` - `"mcs9/3"` - `"mcs10/3"` - `"mcs11/3"` - `"mcs0/4"` - `"mcs1/4"` - `"mcs2/4"` - `"mcs3/4"` - `"mcs4/4"` - `"mcs5/4"` - `"mcs6/4"` - `"mcs7/4"` - `"mcs8/4"` - `"mcs9/4"` - `"mcs10/4"` - `"mcs11/4"` |
| **rates_11ax_mcs_map**  string | Comma separated list of max supported HE MCS for spatial streams 1 through 8. |
| **rates_11ax_ss12**  list / elements=string | Allowed data rates for 802.11ax with 1 or 2 spatial streams.  Choices:   - `"mcs0/1"` - `"mcs1/1"` - `"mcs2/1"` - `"mcs3/1"` - `"mcs4/1"` - `"mcs5/1"` - `"mcs6/1"` - `"mcs7/1"` - `"mcs8/1"` - `"mcs9/1"` - `"mcs10/1"` - `"mcs11/1"` - `"mcs0/2"` - `"mcs1/2"` - `"mcs2/2"` - `"mcs3/2"` - `"mcs4/2"` - `"mcs5/2"` - `"mcs6/2"` - `"mcs7/2"` - `"mcs8/2"` - `"mcs9/2"` - `"mcs10/2"` - `"mcs11/2"` |
| **rates_11ax_ss34**  list / elements=string | Allowed data rates for 802.11ax with 3 or 4 spatial streams.  Choices:   - `"mcs0/3"` - `"mcs1/3"` - `"mcs2/3"` - `"mcs3/3"` - `"mcs4/3"` - `"mcs5/3"` - `"mcs6/3"` - `"mcs7/3"` - `"mcs8/3"` - `"mcs9/3"` - `"mcs10/3"` - `"mcs11/3"` - `"mcs0/4"` - `"mcs1/4"` - `"mcs2/4"` - `"mcs3/4"` - `"mcs4/4"` - `"mcs5/4"` - `"mcs6/4"` - `"mcs7/4"` - `"mcs8/4"` - `"mcs9/4"` - `"mcs10/4"` - `"mcs11/4"` |
| **rates_11bg**  list / elements=string | Allowed data rates for 802.11b/g.  Choices:   - `"1"` - `"1-basic"` - `"2"` - `"2-basic"` - `"5.5"` - `"5.5-basic"` - `"11"` - `"11-basic"` - `"6"` - `"6-basic"` - `"9"` - `"9-basic"` - `"12"` - `"12-basic"` - `"18"` - `"18-basic"` - `"24"` - `"24-basic"` - `"36"` - `"36-basic"` - `"48"` - `"48-basic"` - `"54"` - `"54-basic"` |
| **rates_11n_ss12**  list / elements=string | Allowed data rates for 802.11n with 1 or 2 spatial streams.  Choices:   - `"mcs0/1"` - `"mcs1/1"` - `"mcs2/1"` - `"mcs3/1"` - `"mcs4/1"` - `"mcs5/1"` - `"mcs6/1"` - `"mcs7/1"` - `"mcs8/2"` - `"mcs9/2"` - `"mcs10/2"` - `"mcs11/2"` - `"mcs12/2"` - `"mcs13/2"` - `"mcs14/2"` - `"mcs15/2"` |
| **rates_11n_ss34**  list / elements=string | Allowed data rates for 802.11n with 3 or 4 spatial streams.  Choices:   - `"mcs16/3"` - `"mcs17/3"` - `"mcs18/3"` - `"mcs19/3"` - `"mcs20/3"` - `"mcs21/3"` - `"mcs22/3"` - `"mcs23/3"` - `"mcs24/4"` - `"mcs25/4"` - `"mcs26/4"` - `"mcs27/4"` - `"mcs28/4"` - `"mcs29/4"` - `"mcs30/4"` - `"mcs31/4"` |
| **sae_groups**  list / elements=string | SAE-Groups.  Choices:   - `"19"` - `"20"` - `"21"` - `"1"` - `"2"` - `"5"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` |
| **sae_h2e_only**  string | Use hash-to-element-only mechanism for PWE derivation .  Choices:   - `"enable"` - `"disable"` |
| **sae_password**  string | WPA3 SAE password to be used to authenticate WiFi users. |
| **sae_pk**  string | Enable/disable WPA3 SAE-PK .  Choices:   - `"enable"` - `"disable"` |
| **sae_private_key**  string | Private key used for WPA3 SAE-PK authentication. |
| **scan_botnet_connections**  string | Block or monitor connections to Botnet servers or disable Botnet scanning.  Choices:   - `"disable"` - `"monitor"` - `"block"` |
| **schedule**  list / elements=dictionary | Firewall schedules for enabling this VAP on the FortiAP. This VAP will be enabled when at least one of the schedules is valid. Separate multiple schedule names with a space. |
| **name**  string | Schedule name. Source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name. |
| **secondary_wag_profile**  string | Secondary wireless access gateway profile name. Source wireless-controller.wag-profile.name. |
| **security**  string | Security mode for the wireless interface .  Choices:   - `"open"` - `"captive-portal"` - `"wep64"` - `"wep128"` - `"wpa-personal"` - `"wpa-personal+captive-portal"` - `"wpa-enterprise"` - `"wpa-only-personal"` - `"wpa-only-personal+captive-portal"` - `"wpa-only-enterprise"` - `"wpa2-only-personal"` - `"wpa2-only-personal+captive-portal"` - `"wpa2-only-enterprise"` - `"wpa3-enterprise"` - `"wpa3-only-enterprise"` - `"wpa3-enterprise-transition"` - `"wpa3-sae"` - `"wpa3-sae-transition"` - `"owe"` - `"osen"` |
| **security_exempt_list**  string | Optional security exempt list for captive portal authentication. Source user.security-exempt-list.name. |
| **security_obsolete_option**  string | Enable/disable obsolete security options.  Choices:   - `"enable"` - `"disable"` |
| **security_redirect_url**  string | Optional URL for redirecting users after they pass captive portal authentication. |
| **selected_usergroups**  list / elements=dictionary | Selective user groups that are permitted to authenticate. |
| **name**  string | User group name. Source user.group.name. |
| **split_tunneling**  string | Enable/disable split tunneling .  Choices:   - `"enable"` - `"disable"` |
| **ssid**  string | IEEE 802.11 service set identifier (SSID) for the wireless interface. Users who wish to use the wireless network must configure their computers to access this SSID name. |
| **sticky_client_remove**  string | Enable/disable sticky client remove to maintain good signal level clients in SSID .  Choices:   - `"enable"` - `"disable"` |
| **sticky_client_threshold_2g**  string | Minimum signal level/threshold in dBm required for the 2G client to be serviced by the AP (-95 to -20). |
| **sticky_client_threshold_5g**  string | Minimum signal level/threshold in dBm required for the 5G client to be serviced by the AP (-95 to -20). |
| **sticky_client_threshold_6g**  string | Minimum signal level/threshold in dBm required for the 6G client to be serviced by the AP (-95 to -20). |
| **target_wake_time**  string | Enable/disable 802.11ax target wake time .  Choices:   - `"enable"` - `"disable"` |
| **tkip_counter_measure**  string | Enable/disable TKIP counter measure.  Choices:   - `"enable"` - `"disable"` |
| **tunnel_echo_interval**  integer | The time interval to send echo to both primary and secondary tunnel peers (1 - 65535 sec). |
| **tunnel_fallback_interval**  integer | The time interval for secondary tunnel to fall back to primary tunnel (0 - 65535 sec). |
| **usergroup**  list / elements=dictionary | Firewall user group to be used to authenticate WiFi users. |
| **name**  string | User group name. Source user.group.name. |
| **utm_log**  string | Enable/disable UTM logging.  Choices:   - `"enable"` - `"disable"` |
| **utm_profile**  string | UTM profile name. Source wireless-controller.utm-profile.name. |
| **utm_status**  string | Enable to add one or more security profiles (AV, IPS, etc.) to the VAP.  Choices:   - `"enable"` - `"disable"` |
| **vdom**  string | Name of the VDOM that the Virtual AP has been added to. Source system.vdom.name. |
| **vlan_auto**  string | Enable/disable automatic management of SSID VLAN interface.  Choices:   - `"enable"` - `"disable"` |
| **vlan_name**  list / elements=dictionary | Table for mapping VLAN name to VLAN ID. |
| **name**  string | VLAN name. |
| **vlan_id**  integer | VLAN ID. |
| **vlan_pool**  list / elements=dictionary | VLAN pool. |
| **id**  integer | ID. |
| **wtp_group**  string | WTP group name. Source wireless-controller.wtp-group.name. |
| **vlan_pooling**  string | Enable/disable VLAN pooling, to allow grouping of multiple wireless controller VLANs into VLAN pools . When set to wtp-group, VLAN pooling occurs with VLAN assignment by wtp-group.  Choices:   - `"wtp-group"` - `"round-robin"` - `"hash"` - `"disable"` |
| **vlanid**  integer | Optional VLAN ID. |
| **voice_enterprise**  string | Enable/disable 802.11k and 802.11v assisted Voice-Enterprise roaming .  Choices:   - `"disable"` - `"enable"` |
| **webfilter_profile**  string | WebFilter profile name. Source webfilter.profile.name. |

## [Notes](fortios_wireless_controller_vap_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_vap_module.md#id5)

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
  - name: Configure Virtual Access Points (VAPs).
    fortios_wireless_controller_vap:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_vap:
        access_control_list: "<your_own_value> (source wireless-controller.access-control-list.name)"
        acct_interim_interval: "43200"
        additional_akms: "akm6"
        address_group: "<your_own_value> (source firewall.addrgrp.name)"
        address_group_policy: "disable"
        alias: "<your_own_value>"
        antivirus_profile: "<your_own_value> (source antivirus.profile.name)"
        application_detection_engine: "enable"
        application_dscp_marking: "enable"
        application_list: "<your_own_value> (source application.list.name)"
        application_report_intv: "120"
        atf_weight: "20"
        auth: "psk"
        auth_cert: "<your_own_value> (source vpn.certificate.local.name)"
        auth_portal_addr: "<your_own_value>"
        beacon_advertising: "name"
        broadcast_ssid: "enable"
        broadcast_suppression: "dhcp-up"
        bss_color_partial: "enable"
        bstm_disassociation_imminent: "enable"
        bstm_load_balancing_disassoc_timer: "10"
        bstm_rssi_disassoc_timer: "200"
        captive_portal_ac_name: "<your_own_value>"
        captive_portal_auth_timeout: "0"
        captive_portal_macauth_radius_secret: "<your_own_value>"
        captive_portal_macauth_radius_server: "<your_own_value>"
        captive_portal_radius_secret: "<your_own_value>"
        captive_portal_radius_server: "<your_own_value>"
        captive_portal_session_timeout_interval: "432000"
        dhcp_address_enforcement: "enable"
        dhcp_lease_time: "2400"
        dhcp_option43_insertion: "enable"
        dhcp_option82_circuit_id_insertion: "style-1"
        dhcp_option82_insertion: "enable"
        dhcp_option82_remote_id_insertion: "style-1"
        dynamic_vlan: "enable"
        eap_reauth: "enable"
        eap_reauth_intv: "86400"
        eapol_key_retries: "disable"
        encrypt: "TKIP"
        external_fast_roaming: "enable"
        external_logout: "<your_own_value>"
        external_web: "<your_own_value>"
        external_web_format: "auto-detect"
        fast_bss_transition: "disable"
        fast_roaming: "enable"
        ft_mobility_domain: "1000"
        ft_over_ds: "disable"
        ft_r0_key_lifetime: "480"
        gas_comeback_delay: "500"
        gas_fragmentation_limit: "1024"
        gtk_rekey: "enable"
        gtk_rekey_intv: "86400"
        high_efficiency: "enable"
        hotspot20_profile: "<your_own_value> (source wireless-controller.hotspot20.hs-profile.name)"
        igmp_snooping: "enable"
        intra_vap_privacy: "enable"
        ip: "<your_own_value>"
        ips_sensor: "<your_own_value> (source ips.sensor.name)"
        ipv6_rules: "drop-icmp6ra"
        key: "<your_own_value>"
        keyindex: "1"
        l3_roaming: "enable"
        l3_roaming_mode: "direct"
        ldpc: "disable"
        local_authentication: "enable"
        local_bridging: "enable"
        local_lan: "allow"
        local_standalone: "enable"
        local_standalone_dns: "enable"
        local_standalone_dns_ip: "<your_own_value>"
        local_standalone_nat: "enable"
        mac_auth_bypass: "enable"
        mac_called_station_delimiter: "hyphen"
        mac_calling_station_delimiter: "hyphen"
        mac_case: "uppercase"
        mac_filter: "enable"
        mac_filter_list:
         -
            id:  "81"
            mac: "<your_own_value>"
            mac_filter_policy: "allow"
        mac_filter_policy_other: "allow"
        mac_password_delimiter: "hyphen"
        mac_username_delimiter: "hyphen"
        max_clients: "0"
        max_clients_ap: "0"
        mbo: "disable"
        mbo_cell_data_conn_pref: "excluded"
        me_disable_thresh: "32"
        mesh_backhaul: "enable"
        mpsk: "enable"
        mpsk_concurrent_clients: "32767"
        mpsk_key:
         -
            comment: "Comment."
            concurrent_clients: "<your_own_value>"
            key_name: "<your_own_value>"
            mpsk_schedules:
             -
                name: "default_name_100 (source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name)"
            passphrase: "<your_own_value>"
        mpsk_profile: "<your_own_value> (source wireless-controller.mpsk-profile.name)"
        mu_mimo: "enable"
        multicast_enhance: "enable"
        multicast_rate: "0"
        nac: "enable"
        nac_profile: "<your_own_value> (source wireless-controller.nac-profile.name)"
        name: "default_name_108"
        neighbor_report_dual_band: "disable"
        okc: "disable"
        osen: "enable"
        owe_groups: "19"
        owe_transition: "disable"
        owe_transition_ssid: "<your_own_value>"
        passphrase: "<your_own_value>"
        pmf: "disable"
        pmf_assoc_comeback_timeout: "1"
        pmf_sa_query_retry_timeout: "2"
        port_macauth: "disable"
        port_macauth_reauth_timeout: "7200"
        port_macauth_timeout: "600"
        portal_message_override_group: "<your_own_value> (source system.replacemsg-group.name)"
        portal_message_overrides:
            auth_disclaimer_page: "<your_own_value>"
            auth_login_failed_page: "<your_own_value>"
            auth_login_page: "<your_own_value>"
            auth_reject_page: "<your_own_value>"
        portal_type: "auth"
        primary_wag_profile: "<your_own_value> (source wireless-controller.wag-profile.name)"
        probe_resp_suppression: "enable"
        probe_resp_threshold: "<your_own_value>"
        ptk_rekey: "enable"
        ptk_rekey_intv: "86400"
        qos_profile: "<your_own_value> (source wireless-controller.qos-profile.name)"
        quarantine: "enable"
        radio_2g_threshold: "<your_own_value>"
        radio_5g_threshold: "<your_own_value>"
        radio_sensitivity: "enable"
        radius_mac_auth: "enable"
        radius_mac_auth_server: "<your_own_value> (source user.radius.name)"
        radius_mac_auth_usergroups:
         -
            name: "default_name_142"
        radius_mac_mpsk_auth: "enable"
        radius_mac_mpsk_timeout: "86400"
        radius_server: "<your_own_value> (source user.radius.name)"
        rates_11a: "1"
        rates_11ac_mcs_map: "<your_own_value>"
        rates_11ac_ss12: "mcs0/1"
        rates_11ac_ss34: "mcs0/3"
        rates_11ax_mcs_map: "<your_own_value>"
        rates_11ax_ss12: "mcs0/1"
        rates_11ax_ss34: "mcs0/3"
        rates_11bg: "1"
        rates_11n_ss12: "mcs0/1"
        rates_11n_ss34: "mcs16/3"
        sae_groups: "19"
        sae_h2e_only: "enable"
        sae_password: "<your_own_value>"
        sae_pk: "enable"
        sae_private_key: "<your_own_value>"
        scan_botnet_connections: "disable"
        schedule:
         -
            name: "default_name_163 (source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name)"
        secondary_wag_profile: "<your_own_value> (source wireless-controller.wag-profile.name)"
        security: "open"
        security_exempt_list: "<your_own_value> (source user.security-exempt-list.name)"
        security_obsolete_option: "enable"
        security_redirect_url: "<your_own_value>"
        selected_usergroups:
         -
            name: "default_name_170 (source user.group.name)"
        split_tunneling: "enable"
        ssid: "<your_own_value>"
        sticky_client_remove: "enable"
        sticky_client_threshold_2g: "<your_own_value>"
        sticky_client_threshold_5g: "<your_own_value>"
        sticky_client_threshold_6g: "<your_own_value>"
        target_wake_time: "enable"
        tkip_counter_measure: "enable"
        tunnel_echo_interval: "300"
        tunnel_fallback_interval: "7200"
        usergroup:
         -
            name: "default_name_182 (source user.group.name)"
        utm_log: "enable"
        utm_profile: "<your_own_value> (source wireless-controller.utm-profile.name)"
        utm_status: "enable"
        vdom: "<your_own_value> (source system.vdom.name)"
        vlan_auto: "enable"
        vlan_name:
         -
            name: "default_name_189"
            vlan_id: "0"
        vlan_pool:
         -
            id:  "192"
            wtp_group: "<your_own_value> (source wireless-controller.wtp-group.name)"
        vlan_pooling: "wtp-group"
        vlanid: "0"
        voice_enterprise: "disable"
        webfilter_profile: "<your_own_value> (source webfilter.profile.name)"
```

## [Return Values](fortios_wireless_controller_vap_module.md#id6)

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
