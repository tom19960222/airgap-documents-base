---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_vap module – Configure Virtual Access Points"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_vap_module.html
fetched_at: 2026-07-28T02:21:22+00:00
---
# fortinet.fortimanager.fmgr_vap module – Configure Virtual Access Points

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_vap`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_vap_module.md#synopsis)
- [Parameters](fmgr_vap_module.md#parameters)
- [Notes](fmgr_vap_module.md#notes)
- [Examples](fmgr_vap_module.md#examples)
- [Return Values](fmgr_vap_module.md#return-values)

## [Synopsis](fmgr_vap_module.md#id2)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_vap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **vap**  dictionary | the top level parameters set |
| **_centmgmt**  string | _Centmgmt.  **Choices:**   - `"disable"` - `"enable"` |
| **_dhcp_svr_id**  string | _Dhcp_Svr_Id. |
| **_intf_allowaccess**  list / elements=string | _Intf_Allowaccess.  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"auto-ipsec"` - `"radius-acct"` - `"probe-response"` - `"capwap"` - `"dnp"` - `"ftm"` - `"fabric"` - `"speed-test"` |
| **_intf_device-access-list**  string | _Intf_Device-Access-List. |
| **_intf_device-identification**  string | _Intf_Device-Identification.  **Choices:**   - `"disable"` - `"enable"` |
| **_intf_device-netscan**  string | _Intf_Device-Netscan.  **Choices:**   - `"disable"` - `"enable"` |
| **_intf_dhcp-relay-ip**  any | (list) _Intf_Dhcp-Relay-Ip. |
| **_intf_dhcp-relay-service**  string | _Intf_Dhcp-Relay-Service.  **Choices:**   - `"disable"` - `"enable"` |
| **_intf_dhcp-relay-type**  string | _Intf_Dhcp-Relay-Type.  **Choices:**   - `"regular"` - `"ipsec"` |
| **_intf_dhcp6-relay-ip**  string | _Intf_Dhcp6-Relay-Ip. |
| **_intf_dhcp6-relay-service**  string | _Intf_Dhcp6-Relay-Service.  **Choices:**   - `"disable"` - `"enable"` |
| **_intf_dhcp6-relay-type**  string | _Intf_Dhcp6-Relay-Type.  **Choices:**   - `"regular"` |
| **_intf_ip**  string | _Intf_Ip. |
| **_intf_ip6-address**  string | _Intf_Ip6-Address. |
| **_intf_ip6-allowaccess**  list / elements=string | _Intf_Ip6-Allowaccess.  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"any"` - `"fgfm"` - `"capwap"` |
| **_intf_listen-forticlient-connection**  string | _Intf_Listen-Forticlient-Connection.  **Choices:**   - `"disable"` - `"enable"` |
| **_is_factory_setting**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"ext"` |
| **access-control-list**  string | access-control-list profile name. |
| **acct-interim-interval**  integer | WiFi RADIUS accounting interim interval |
| **additional-akms**  list / elements=string | Additional AKMs.  **Choices:**   - `"akm6"` |
| **address-group**  string | Address group ID. |
| **address-group-policy**  string | Configure MAC address filtering policy for MAC addresses that are in the address-group.  **Choices:**   - `"disable"` - `"allow"` - `"deny"` |
| **alias**  string | Alias. |
| **antivirus-profile**  string | AntiVirus profile name. |
| **application-detection-engine**  string | Enable/disable application detection engine  **Choices:**   - `"disable"` - `"enable"` |
| **application-dscp-marking**  string | Enable/disable application attribute based DSCP marking  **Choices:**   - `"disable"` - `"enable"` |
| **application-list**  string | Application control list name. |
| **application-report-intv**  integer | Application report interval |
| **atf-weight**  integer | Airtime weight in percentage |
| **auth**  string | Authentication protocol.  **Choices:**   - `"PSK"` - `"psk"` - `"RADIUS"` - `"radius"` - `"usergroup"` |
| **auth-cert**  string | HTTPS server certificate. |
| **auth-portal-addr**  string | Address of captive portal. |
| **beacon-advertising**  list / elements=string | no description  **Choices:**   - `"name"` - `"model"` - `"serial-number"` |
| **broadcast-ssid**  string | Enable/disable broadcasting the SSID  **Choices:**   - `"disable"` - `"enable"` |
| **broadcast-suppression**  list / elements=string | Optional suppression of broadcast messages.  **Choices:**   - `"dhcp"` - `"arp"` - `"dhcp2"` - `"arp2"` - `"netbios-ns"` - `"netbios-ds"` - `"arp3"` - `"dhcp-up"` - `"dhcp-down"` - `"arp-known"` - `"arp-unknown"` - `"arp-reply"` - `"ipv6"` - `"dhcp-starvation"` - `"arp-poison"` - `"all-other-mc"` - `"all-other-bc"` - `"arp-proxy"` - `"dhcp-ucast"` |
| **bss-color-partial**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **bstm-disassociation-imminent**  string | Enable/disable forcing of disassociation after the BSTM request timer has been reached  **Choices:**   - `"disable"` - `"enable"` |
| **bstm-load-balancing-disassoc-timer**  integer | Time interval for client to voluntarily leave AP before forcing a disassociation due to AP load-balancing |
| **bstm-rssi-disassoc-timer**  integer | Time interval for client to voluntarily leave AP before forcing a disassociation due to low RSSI |
| **captive-portal-ac-name**  string | Local-bridging captive portal ac-name. |
| **captive-portal-auth-timeout**  integer | Hard timeout - AP will always clear the session after timeout regardless of traffic |
| **captive-portal-fw-accounting**  string | Enable/disable RADIUS accounting for captive portal firewall authentication session.  **Choices:**   - `"disable"` - `"enable"` |
| **captive-portal-macauth-radius-secret**  any | (list) Secret key to access the macauth RADIUS server. |
| **captive-portal-macauth-radius-server**  string | Captive portal external RADIUS server domain name or IP address. |
| **captive-portal-radius-secret**  any | (list) Secret key to access the RADIUS server. |
| **captive-portal-radius-server**  string | Captive portal RADIUS server domain name or IP address. |
| **captive-portal-session-timeout-interval**  integer | Session timeout interval |
| **dhcp-address-enforcement**  string | Enable/disable DHCP address enforcement  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-lease-time**  integer | DHCP lease time in seconds for NAT IP address. |
| **dhcp-option43-insertion**  string | Enable/disable insertion of DHCP option 43  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-option82-circuit-id-insertion**  string | Enable/disable DHCP option 82 circuit-id insert  **Choices:**   - `"disable"` - `"style-1"` - `"style-2"` - `"style-3"` |
| **dhcp-option82-insertion**  string | Enable/disable DHCP option 82 insert  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-option82-remote-id-insertion**  string | Enable/disable DHCP option 82 remote-id insert  **Choices:**   - `"disable"` - `"style-1"` |
| **dynamic-vlan**  string | Enable/disable dynamic VLAN assignment.  **Choices:**   - `"disable"` - `"enable"` |
| **dynamic_mapping**  list / elements=dictionary | Dynamic_Mapping. |
| **_centmgmt**  string | _Centmgmt.  **Choices:**   - `"disable"` - `"enable"` |
| **_dhcp_svr_id**  string | _Dhcp_Svr_Id. |
| **_intf_allowaccess**  list / elements=string | _Intf_Allowaccess.  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"auto-ipsec"` - `"radius-acct"` - `"probe-response"` - `"capwap"` - `"dnp"` - `"ftm"` - `"fabric"` - `"speed-test"` |
| **_intf_device-access-list**  string | _Intf_Device-Access-List. |
| **_intf_device-identification**  string | _Intf_Device-Identification.  **Choices:**   - `"disable"` - `"enable"` |
| **_intf_device-netscan**  string | _Intf_Device-Netscan.  **Choices:**   - `"disable"` - `"enable"` |
| **_intf_dhcp-relay-ip**  any | (list) _Intf_Dhcp-Relay-Ip. |
| **_intf_dhcp-relay-service**  string | _Intf_Dhcp-Relay-Service.  **Choices:**   - `"disable"` - `"enable"` |
| **_intf_dhcp-relay-type**  string | _Intf_Dhcp-Relay-Type.  **Choices:**   - `"regular"` - `"ipsec"` |
| **_intf_dhcp6-relay-ip**  string | _Intf_Dhcp6-Relay-Ip. |
| **_intf_dhcp6-relay-service**  string | _Intf_Dhcp6-Relay-Service.  **Choices:**   - `"disable"` - `"enable"` |
| **_intf_dhcp6-relay-type**  string | _Intf_Dhcp6-Relay-Type.  **Choices:**   - `"regular"` |
| **_intf_ip**  string | _Intf_Ip. |
| **_intf_ip6-address**  string | _Intf_Ip6-Address. |
| **_intf_ip6-allowaccess**  list / elements=string | _Intf_Ip6-Allowaccess.  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"any"` - `"fgfm"` - `"capwap"` |
| **_intf_listen-forticlient-connection**  string | _Intf_Listen-Forticlient-Connection.  **Choices:**   - `"disable"` - `"enable"` |
| **_is_factory_setting**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"ext"` |
| **_scope**  list / elements=dictionary | _Scope. |
| **name**  string | Name. |
| **vdom**  string | Vdom. |
| **access-control-list**  string | Access-Control-List. |
| **acct-interim-interval**  integer | WiFi RADIUS accounting interim interval |
| **additional-akms**  list / elements=string | Additional-Akms.  **Choices:**   - `"akm6"` |
| **address-group**  string | Address group ID. |
| **address-group-policy**  string | Configure MAC address filtering policy for MAC addresses that are in the address-group.  **Choices:**   - `"disable"` - `"allow"` - `"deny"` |
| **alias**  string | Alias. |
| **antivirus-profile**  string | AntiVirus profile name. |
| **application-detection-engine**  string | Enable/disable application detection engine  **Choices:**   - `"disable"` - `"enable"` |
| **application-dscp-marking**  string | Enable/disable application attribute based DSCP marking  **Choices:**   - `"disable"` - `"enable"` |
| **application-list**  string | Application control list name. |
| **application-report-intv**  integer | Application report interval |
| **atf-weight**  integer | Airtime weight in percentage |
| **auth**  string | Authentication protocol.  **Choices:**   - `"PSK"` - `"psk"` - `"RADIUS"` - `"radius"` - `"usergroup"` |
| **auth-cert**  string | HTTPS server certificate. |
| **auth-portal-addr**  string | Address of captive portal. |
| **beacon-advertising**  list / elements=string | no description  **Choices:**   - `"name"` - `"model"` - `"serial-number"` |
| **broadcast-ssid**  string | Enable/disable broadcasting the SSID  **Choices:**   - `"disable"` - `"enable"` |
| **broadcast-suppression**  list / elements=string | Optional suppression of broadcast messages.  **Choices:**   - `"dhcp"` - `"arp"` - `"dhcp2"` - `"arp2"` - `"netbios-ns"` - `"netbios-ds"` - `"arp3"` - `"dhcp-up"` - `"dhcp-down"` - `"arp-known"` - `"arp-unknown"` - `"arp-reply"` - `"ipv6"` - `"dhcp-starvation"` - `"arp-poison"` - `"all-other-mc"` - `"all-other-bc"` - `"arp-proxy"` - `"dhcp-ucast"` |
| **bss-color-partial**  string | Bss-Color-Partial.  **Choices:**   - `"disable"` - `"enable"` |
| **bstm-disassociation-imminent**  string | Enable/disable forcing of disassociation after the BSTM request timer has been reached  **Choices:**   - `"disable"` - `"enable"` |
| **bstm-load-balancing-disassoc-timer**  integer | Time interval for client to voluntarily leave AP before forcing a disassociation due to AP load-balancing |
| **bstm-rssi-disassoc-timer**  integer | Time interval for client to voluntarily leave AP before forcing a disassociation due to low RSSI |
| **captive-portal-ac-name**  string | Local-bridging captive portal ac-name. |
| **captive-portal-auth-timeout**  integer | Captive-Portal-Auth-Timeout. |
| **captive-portal-fw-accounting**  string | Enable/disable RADIUS accounting for captive portal firewall authentication session.  **Choices:**   - `"disable"` - `"enable"` |
| **captive-portal-macauth-radius-secret**  any | (list) Secret key to access the macauth RADIUS server. |
| **captive-portal-macauth-radius-server**  string | Captive portal external RADIUS server domain name or IP address. |
| **captive-portal-radius-secret**  any | (list) Secret key to access the RADIUS server. |
| **captive-portal-radius-server**  string | Captive portal RADIUS server domain name or IP address. |
| **captive-portal-session-timeout-interval**  integer | Session timeout interval |
| **client-count**  integer | Client-Count. |
| **dhcp-address-enforcement**  string | Enable/disable DHCP address enforcement  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-lease-time**  integer | DHCP lease time in seconds for NAT IP address. |
| **dhcp-option43-insertion**  string | Dhcp-Option43-Insertion.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-option82-circuit-id-insertion**  string | Enable/disable DHCP option 82 circuit-id insert  **Choices:**   - `"disable"` - `"style-1"` - `"style-2"` - `"style-3"` |
| **dhcp-option82-insertion**  string | Enable/disable DHCP option 82 insert  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-option82-remote-id-insertion**  string | Enable/disable DHCP option 82 remote-id insert  **Choices:**   - `"disable"` - `"style-1"` |
| **dynamic-vlan**  string | Enable/disable dynamic VLAN assignment.  **Choices:**   - `"disable"` - `"enable"` |
| **eap-reauth**  string | Enable/disable EAP re-authentication for WPA-Enterprise security.  **Choices:**   - `"disable"` - `"enable"` |
| **eap-reauth-intv**  integer | EAP re-authentication interval |
| **eapol-key-retries**  string | Enable/disable retransmission of EAPOL-Key frames  **Choices:**   - `"disable"` - `"enable"` |
| **encrypt**  string | Encryption protocol to use  **Choices:**   - `"TKIP"` - `"AES"` - `"TKIP-AES"` |
| **external-fast-roaming**  string | Enable/disable fast roaming or pre-authentication with external APs not managed by the FortiGate  **Choices:**   - `"disable"` - `"enable"` |
| **external-logout**  string | URL of external authentication logout server. |
| **external-web**  string | URL of external authentication web server. |
| **external-web-format**  string | URL query parameter detection  **Choices:**   - `"auto-detect"` - `"no-query-string"` - `"partial-query-string"` |
| **fast-bss-transition**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **fast-roaming**  string | Enable/disable fast-roaming, or pre-authentication, where supported by clients  **Choices:**   - `"disable"` - `"enable"` |
| **ft-mobility-domain**  integer | Mobility domain identifier in FT |
| **ft-over-ds**  string | Enable/disable FT over the Distribution System  **Choices:**   - `"disable"` - `"enable"` |
| **ft-r0-key-lifetime**  integer | Lifetime of the PMK-R0 key in FT, 1-65535 minutes. |
| **gas-comeback-delay**  integer | GAS comeback delay |
| **gas-fragmentation-limit**  integer | GAS fragmentation limit |
| **gtk-rekey**  string | Enable/disable GTK rekey for WPA security.  **Choices:**   - `"disable"` - `"enable"` |
| **gtk-rekey-intv**  integer | GTK rekey interval |
| **high-efficiency**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **hotspot20-profile**  string | Hotspot 2. |
| **igmp-snooping**  string | Enable/disable IGMP snooping.  **Choices:**   - `"disable"` - `"enable"` |
| **intra-vap-privacy**  string | Enable/disable blocking communication between clients on the same SSID  **Choices:**   - `"disable"` - `"enable"` |
| **ip**  string | IP address and subnet mask for the local standalone NAT subnet. |
| **ips-sensor**  string | IPS sensor name. |
| **ipv6-rules**  list / elements=string | Ipv6-Rules.  **Choices:**   - `"drop-icmp6ra"` - `"drop-icmp6rs"` - `"drop-llmnr6"` - `"drop-icmp6mld2"` - `"drop-dhcp6s"` - `"drop-dhcp6c"` - `"ndp-proxy"` - `"drop-ns-dad"` - `"drop-ns-nondad"` |
| **key**  any | (list) WEP Key. |
| **keyindex**  integer | WEP key index |
| **l3-roaming**  string | Enable/disable layer 3 roaming  **Choices:**   - `"disable"` - `"enable"` |
| **l3-roaming-mode**  string | Select the way that layer 3 roaming traffic is passed  **Choices:**   - `"direct"` - `"indirect"` |
| **ldpc**  string | VAP low-density parity-check  **Choices:**   - `"disable"` - `"tx"` - `"rx"` - `"rxtx"` |
| **local-authentication**  string | Enable/disable AP local authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **local-bridging**  string | Enable/disable bridging of wireless and Ethernet interfaces on the FortiAP  **Choices:**   - `"disable"` - `"enable"` |
| **local-lan**  string | Allow/deny traffic destined for a Class A, B, or C private IP address  **Choices:**   - `"deny"` - `"allow"` |
| **local-standalone**  string | Enable/disable AP local standalone  **Choices:**   - `"disable"` - `"enable"` |
| **local-standalone-dns**  string | Enable/disable AP local standalone DNS.  **Choices:**   - `"disable"` - `"enable"` |
| **local-standalone-dns-ip**  any | (list) no description |
| **local-standalone-nat**  string | Enable/disable AP local standalone NAT mode.  **Choices:**   - `"disable"` - `"enable"` |
| **local-switching**  string | Local-Switching.  **Choices:**   - `"disable"` - `"enable"` |
| **mac-auth-bypass**  string | Enable/disable MAC authentication bypass.  **Choices:**   - `"disable"` - `"enable"` |
| **mac-called-station-delimiter**  string | MAC called station delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac-calling-station-delimiter**  string | MAC calling station delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac-case**  string | MAC case  **Choices:**   - `"uppercase"` - `"lowercase"` |
| **mac-filter**  string | Enable/disable MAC filtering to block wireless clients by mac address.  **Choices:**   - `"disable"` - `"enable"` |
| **mac-filter-policy-other**  string | Allow or block clients with MAC addresses that are not in the filter list.  **Choices:**   - `"deny"` - `"allow"` |
| **mac-password-delimiter**  string | MAC authentication password delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac-username-delimiter**  string | MAC authentication username delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **max-clients**  integer | Maximum number of clients that can connect simultaneously to the VAP |
| **max-clients-ap**  integer | Maximum number of clients that can connect simultaneously to the VAP per AP radio |
| **mbo**  string | Enable/disable Multiband Operation  **Choices:**   - `"disable"` - `"enable"` |
| **mbo-cell-data-conn-pref**  string | MBO cell data connection preference  **Choices:**   - `"excluded"` - `"prefer-not"` - `"prefer-use"` |
| **me-disable-thresh**  integer | Disable multicast enhancement when this many clients are receiving multicast traffic. |
| **mesh-backhaul**  string | Enable/disable using this VAP as a WiFi mesh backhaul  **Choices:**   - `"disable"` - `"enable"` |
| **mpsk**  string | Enable/disable multiple PSK authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **mpsk-concurrent-clients**  integer | Maximum number of concurrent clients that connect using the same passphrase in multiple PSK authentication |
| **mpsk-profile**  string | Mpsk-Profile. |
| **mu-mimo**  string | Enable/disable Multi-user MIMO  **Choices:**   - `"disable"` - `"enable"` |
| **multicast-enhance**  string | Enable/disable converting multicast to unicast to improve performance  **Choices:**   - `"disable"` - `"enable"` |
| **multicast-rate**  string | Multicast rate  **Choices:**   - `"0"` - `"6000"` - `"12000"` - `"24000"` |
| **nac**  string | Enable/disable network access control.  **Choices:**   - `"disable"` - `"enable"` |
| **nac-profile**  string | NAC profile name. |
| **neighbor-report-dual-band**  string | Enable/disable dual-band neighbor report  **Choices:**   - `"disable"` - `"enable"` |
| **okc**  string | Enable/disable Opportunistic Key Caching  **Choices:**   - `"disable"` - `"enable"` |
| **osen**  string | Enable/disable OSEN as part of key management  **Choices:**   - `"disable"` - `"enable"` |
| **owe-groups**  list / elements=string | OWE-Groups.  **Choices:**   - `"19"` - `"20"` - `"21"` |
| **owe-transition**  string | Enable/disable OWE transition mode support.  **Choices:**   - `"disable"` - `"enable"` |
| **owe-transition-ssid**  string | OWE transition mode peer SSID. |
| **passphrase**  any | (list) WPA pre-shared key |
| **pmf**  string | Protected Management Frames  **Choices:**   - `"disable"` - `"enable"` - `"optional"` |
| **pmf-assoc-comeback-timeout**  integer | Protected Management Frames |
| **pmf-sa-query-retry-timeout**  integer | Protected Management Frames |
| **port-macauth**  string | Enable/disable LAN port MAC authentication  **Choices:**   - `"disable"` - `"radius"` - `"address-group"` |
| **port-macauth-reauth-timeout**  integer | LAN port MAC authentication re-authentication timeout value |
| **port-macauth-timeout**  integer | LAN port MAC authentication idle timeout value |
| **portal-message-override-group**  string | Replacement message group for this VAP |
| **portal-type**  string | Captive portal functionality.  **Choices:**   - `"auth"` - `"auth+disclaimer"` - `"disclaimer"` - `"email-collect"` - `"cmcc"` - `"cmcc-macauth"` - `"auth-mac"` - `"external-auth"` - `"external-macauth"` |
| **primary-wag-profile**  string | Primary wireless access gateway profile name. |
| **probe-resp-suppression**  string | Enable/disable probe response suppression  **Choices:**   - `"disable"` - `"enable"` |
| **probe-resp-threshold**  string | Minimum signal level/threshold in dBm required for the AP response to probe requests |
| **ptk-rekey**  string | Enable/disable PTK rekey for WPA-Enterprise security.  **Choices:**   - `"disable"` - `"enable"` |
| **ptk-rekey-intv**  integer | PTK rekey interval |
| **qos-profile**  string | Quality of service profile name. |
| **quarantine**  string | Enable/disable station quarantine  **Choices:**   - `"disable"` - `"enable"` |
| **radio-2g-threshold**  string | Minimum signal level/threshold in dBm required for the AP response to receive a packet in 2. |
| **radio-5g-threshold**  string | Minimum signal level/threshold in dBm required for the AP response to receive a packet in 5G band |
| **radio-sensitivity**  string | Enable/disable software radio sensitivity  **Choices:**   - `"disable"` - `"enable"` |
| **radius-mac-auth**  string | Enable/disable RADIUS-based MAC authentication of clients  **Choices:**   - `"disable"` - `"enable"` |
| **radius-mac-auth-block-interval**  integer | Dont send RADIUS MAC auth request again if the client has been rejected within specific interval |
| **radius-mac-auth-server**  string | RADIUS-based MAC authentication server. |
| **radius-mac-auth-usergroups**  any | (list) Selective user groups that are permitted for RADIUS mac authentication. |
| **radius-mac-mpsk-auth**  string | Enable/disable RADIUS-based MAC authentication of clients for MPSK authentication  **Choices:**   - `"disable"` - `"enable"` |
| **radius-mac-mpsk-timeout**  integer | RADIUS MAC MPSK cache timeout interval |
| **radius-server**  string | RADIUS server to be used to authenticate WiFi users. |
| **rates-11a**  list / elements=string | Allowed data rates for 802.  **Choices:**   - `"1"` - `"1-basic"` - `"2"` - `"2-basic"` - `"5.5"` - `"5.5-basic"` - `"6"` - `"6-basic"` - `"9"` - `"9-basic"` - `"12"` - `"12-basic"` - `"18"` - `"18-basic"` - `"24"` - `"24-basic"` - `"36"` - `"36-basic"` - `"48"` - `"48-basic"` - `"54"` - `"54-basic"` - `"11"` - `"11-basic"` |
| **rates-11ac-mcs-map**  string | Comma separated list of max supported VHT MCS for spatial streams 1 through 8. |
| **rates-11ac-ss12**  list / elements=string | Allowed data rates for 802.  **Choices:**   - `"mcs0/1"` - `"mcs1/1"` - `"mcs2/1"` - `"mcs3/1"` - `"mcs4/1"` - `"mcs5/1"` - `"mcs6/1"` - `"mcs7/1"` - `"mcs8/1"` - `"mcs9/1"` - `"mcs0/2"` - `"mcs1/2"` - `"mcs2/2"` - `"mcs3/2"` - `"mcs4/2"` - `"mcs5/2"` - `"mcs6/2"` - `"mcs7/2"` - `"mcs8/2"` - `"mcs9/2"` - `"mcs10/1"` - `"mcs11/1"` - `"mcs10/2"` - `"mcs11/2"` |
| **rates-11ac-ss34**  list / elements=string | Allowed data rates for 802.  **Choices:**   - `"mcs0/3"` - `"mcs1/3"` - `"mcs2/3"` - `"mcs3/3"` - `"mcs4/3"` - `"mcs5/3"` - `"mcs6/3"` - `"mcs7/3"` - `"mcs8/3"` - `"mcs9/3"` - `"mcs0/4"` - `"mcs1/4"` - `"mcs2/4"` - `"mcs3/4"` - `"mcs4/4"` - `"mcs5/4"` - `"mcs6/4"` - `"mcs7/4"` - `"mcs8/4"` - `"mcs9/4"` - `"mcs10/3"` - `"mcs11/3"` - `"mcs10/4"` - `"mcs11/4"` |
| **rates-11ax-mcs-map**  string | Comma separated list of max supported HE MCS for spatial streams 1 through 8. |
| **rates-11ax-ss12**  list / elements=string | no description  **Choices:**   - `"mcs0/1"` - `"mcs1/1"` - `"mcs2/1"` - `"mcs3/1"` - `"mcs4/1"` - `"mcs5/1"` - `"mcs6/1"` - `"mcs7/1"` - `"mcs8/1"` - `"mcs9/1"` - `"mcs10/1"` - `"mcs11/1"` - `"mcs0/2"` - `"mcs1/2"` - `"mcs2/2"` - `"mcs3/2"` - `"mcs4/2"` - `"mcs5/2"` - `"mcs6/2"` - `"mcs7/2"` - `"mcs8/2"` - `"mcs9/2"` - `"mcs10/2"` - `"mcs11/2"` |
| **rates-11ax-ss34**  list / elements=string | no description  **Choices:**   - `"mcs0/3"` - `"mcs1/3"` - `"mcs2/3"` - `"mcs3/3"` - `"mcs4/3"` - `"mcs5/3"` - `"mcs6/3"` - `"mcs7/3"` - `"mcs8/3"` - `"mcs9/3"` - `"mcs10/3"` - `"mcs11/3"` - `"mcs0/4"` - `"mcs1/4"` - `"mcs2/4"` - `"mcs3/4"` - `"mcs4/4"` - `"mcs5/4"` - `"mcs6/4"` - `"mcs7/4"` - `"mcs8/4"` - `"mcs9/4"` - `"mcs10/4"` - `"mcs11/4"` |
| **rates-11bg**  list / elements=string | Allowed data rates for 802.  **Choices:**   - `"1"` - `"1-basic"` - `"2"` - `"2-basic"` - `"5.5"` - `"5.5-basic"` - `"6"` - `"6-basic"` - `"9"` - `"9-basic"` - `"12"` - `"12-basic"` - `"18"` - `"18-basic"` - `"24"` - `"24-basic"` - `"36"` - `"36-basic"` - `"48"` - `"48-basic"` - `"54"` - `"54-basic"` - `"11"` - `"11-basic"` |
| **rates-11n-ss12**  list / elements=string | Allowed data rates for 802.  **Choices:**   - `"mcs0/1"` - `"mcs1/1"` - `"mcs2/1"` - `"mcs3/1"` - `"mcs4/1"` - `"mcs5/1"` - `"mcs6/1"` - `"mcs7/1"` - `"mcs8/2"` - `"mcs9/2"` - `"mcs10/2"` - `"mcs11/2"` - `"mcs12/2"` - `"mcs13/2"` - `"mcs14/2"` - `"mcs15/2"` |
| **rates-11n-ss34**  list / elements=string | Allowed data rates for 802.  **Choices:**   - `"mcs16/3"` - `"mcs17/3"` - `"mcs18/3"` - `"mcs19/3"` - `"mcs20/3"` - `"mcs21/3"` - `"mcs22/3"` - `"mcs23/3"` - `"mcs24/4"` - `"mcs25/4"` - `"mcs26/4"` - `"mcs27/4"` - `"mcs28/4"` - `"mcs29/4"` - `"mcs30/4"` - `"mcs31/4"` |
| **sae-groups**  list / elements=string | SAE-Groups.  **Choices:**   - `"1"` - `"2"` - `"5"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` |
| **sae-h2e-only**  string | Use hash-to-element-only mechanism for PWE derivation  **Choices:**   - `"disable"` - `"enable"` |
| **sae-password**  any | (list) WPA3 SAE password to be used to authenticate WiFi users. |
| **sae-pk**  string | Enable/disable WPA3 SAE-PK  **Choices:**   - `"disable"` - `"enable"` |
| **sae-private-key**  string | Private key used for WPA3 SAE-PK authentication. |
| **scan-botnet-connections**  string | Block or monitor connections to Botnet servers or disable Botnet scanning.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  any | (list or str) Firewall schedules for enabling this VAP on the FortiAP. |
| **secondary-wag-profile**  string | Secondary wireless access gateway profile name. |
| **security**  string | Security mode for the wireless interface  **Choices:**   - `"None"` - `"WEP64"` - `"wep64"` - `"WEP128"` - `"wep128"` - `"WPA_PSK"` - `"WPA_RADIUS"` - `"WPA"` - `"WPA2"` - `"WPA2_AUTO"` - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` - `"captive-portal"` - `"wpa-only-personal"` - `"wpa-only-enterprise"` - `"wpa2-only-personal"` - `"wpa2-only-enterprise"` - `"wpa-personal+captive-portal"` - `"wpa-only-personal+captive-portal"` - `"wpa2-only-personal+captive-portal"` - `"osen"` - `"wpa3-enterprise"` - `"sae"` - `"sae-transition"` - `"owe"` - `"wpa3-sae"` - `"wpa3-sae-transition"` - `"wpa3-only-enterprise"` - `"wpa3-enterprise-transition"` |
| **security-exempt-list**  string | Optional security exempt list for captive portal authentication. |
| **security-obsolete-option**  string | Enable/disable obsolete security options.  **Choices:**   - `"disable"` - `"enable"` |
| **security-redirect-url**  string | Optional URL for redirecting users after they pass captive portal authentication. |
| **selected-usergroups**  any | (list or str) Selective user groups that are permitted to authenticate. |
| **split-tunneling**  string | Enable/disable split tunneling  **Choices:**   - `"disable"` - `"enable"` |
| **ssid**  string | IEEE 802. |
| **sticky-client-remove**  string | Sticky-Client-Remove.  **Choices:**   - `"disable"` - `"enable"` |
| **sticky-client-threshold-2g**  string | Sticky-Client-Threshold-2G. |
| **sticky-client-threshold-5g**  string | Sticky-Client-Threshold-5G. |
| **sticky-client-threshold-6g**  string | Minimum signal level/threshold in dBm required for the 6G client to be serviced by the AP |
| **target-wake-time**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **tkip-counter-measure**  string | Enable/disable TKIP counter measure.  **Choices:**   - `"disable"` - `"enable"` |
| **tunnel-echo-interval**  integer | The time interval to send echo to both primary and secondary tunnel peers |
| **tunnel-fallback-interval**  integer | The time interval for secondary tunnel to fall back to primary tunnel |
| **usergroup**  any | (list or str) Firewall user group to be used to authenticate WiFi users. |
| **utm-log**  string | Enable/disable UTM logging.  **Choices:**   - `"disable"` - `"enable"` |
| **utm-profile**  string | UTM profile name. |
| **utm-status**  string | Enable to add one or more security profiles  **Choices:**   - `"disable"` - `"enable"` |
| **vdom**  any | (list or str) Vdom. |
| **vlan-auto**  string | Enable/disable automatic management of SSID VLAN interface.  **Choices:**   - `"disable"` - `"enable"` |
| **vlan-pooling**  string | Enable/disable VLAN pooling, to allow grouping of multiple wireless controller VLANs into VLAN pools  **Choices:**   - `"wtp-group"` - `"round-robin"` - `"hash"` - `"disable"` |
| **vlanid**  integer | Optional VLAN ID. |
| **voice-enterprise**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **webfilter-profile**  string | WebFilter profile name. |
| **eap-reauth**  string | Enable/disable EAP re-authentication for WPA-Enterprise security.  **Choices:**   - `"disable"` - `"enable"` |
| **eap-reauth-intv**  integer | EAP re-authentication interval |
| **eapol-key-retries**  string | Enable/disable retransmission of EAPOL-Key frames  **Choices:**   - `"disable"` - `"enable"` |
| **encrypt**  string | Encryption protocol to use  **Choices:**   - `"TKIP"` - `"AES"` - `"TKIP-AES"` |
| **external-fast-roaming**  string | Enable/disable fast roaming or pre-authentication with external APs not managed by the FortiGate  **Choices:**   - `"disable"` - `"enable"` |
| **external-logout**  string | URL of external authentication logout server. |
| **external-web**  string | URL of external authentication web server. |
| **external-web-format**  string | URL query parameter detection  **Choices:**   - `"auto-detect"` - `"no-query-string"` - `"partial-query-string"` |
| **fast-bss-transition**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **fast-roaming**  string | Enable/disable fast-roaming, or pre-authentication, where supported by clients  **Choices:**   - `"disable"` - `"enable"` |
| **ft-mobility-domain**  integer | Mobility domain identifier in FT |
| **ft-over-ds**  string | Enable/disable FT over the Distribution System  **Choices:**   - `"disable"` - `"enable"` |
| **ft-r0-key-lifetime**  integer | Lifetime of the PMK-R0 key in FT, 1-65535 minutes. |
| **gas-comeback-delay**  integer | GAS comeback delay |
| **gas-fragmentation-limit**  integer | GAS fragmentation limit |
| **gtk-rekey**  string | Enable/disable GTK rekey for WPA security.  **Choices:**   - `"disable"` - `"enable"` |
| **gtk-rekey-intv**  integer | GTK rekey interval |
| **high-efficiency**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **hotspot20-profile**  string | Hotspot 2. |
| **igmp-snooping**  string | Enable/disable IGMP snooping.  **Choices:**   - `"disable"` - `"enable"` |
| **intra-vap-privacy**  string | Enable/disable blocking communication between clients on the same SSID  **Choices:**   - `"disable"` - `"enable"` |
| **ip**  string | IP address and subnet mask for the local standalone NAT subnet. |
| **ips-sensor**  string | IPS sensor name. |
| **ipv6-rules**  list / elements=string | Optional rules of IPv6 packets.  **Choices:**   - `"drop-icmp6ra"` - `"drop-icmp6rs"` - `"drop-llmnr6"` - `"drop-icmp6mld2"` - `"drop-dhcp6s"` - `"drop-dhcp6c"` - `"ndp-proxy"` - `"drop-ns-dad"` - `"drop-ns-nondad"` |
| **key**  any | (list) WEP Key. |
| **keyindex**  integer | WEP key index |
| **l3-roaming**  string | Enable/disable layer 3 roaming  **Choices:**   - `"disable"` - `"enable"` |
| **l3-roaming-mode**  string | Select the way that layer 3 roaming traffic is passed  **Choices:**   - `"direct"` - `"indirect"` |
| **ldpc**  string | VAP low-density parity-check  **Choices:**   - `"disable"` - `"tx"` - `"rx"` - `"rxtx"` |
| **local-authentication**  string | Enable/disable AP local authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **local-bridging**  string | Enable/disable bridging of wireless and Ethernet interfaces on the FortiAP  **Choices:**   - `"disable"` - `"enable"` |
| **local-lan**  string | Allow/deny traffic destined for a Class A, B, or C private IP address  **Choices:**   - `"deny"` - `"allow"` |
| **local-standalone**  string | Enable/disable AP local standalone  **Choices:**   - `"disable"` - `"enable"` |
| **local-standalone-dns**  string | Enable/disable AP local standalone DNS.  **Choices:**   - `"disable"` - `"enable"` |
| **local-standalone-dns-ip**  any | (list) no description |
| **local-standalone-nat**  string | Enable/disable AP local standalone NAT mode.  **Choices:**   - `"disable"` - `"enable"` |
| **mac-auth-bypass**  string | Enable/disable MAC authentication bypass.  **Choices:**   - `"disable"` - `"enable"` |
| **mac-called-station-delimiter**  string | MAC called station delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac-calling-station-delimiter**  string | MAC calling station delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac-case**  string | MAC case  **Choices:**   - `"uppercase"` - `"lowercase"` |
| **mac-filter**  string | Enable/disable MAC filtering to block wireless clients by mac address.  **Choices:**   - `"disable"` - `"enable"` |
| **mac-filter-list**  list / elements=dictionary | Mac-Filter-List. |
| **id**  integer | ID. |
| **mac**  string | MAC address. |
| **mac-filter-policy**  string | Deny or allow the client with this MAC address.  **Choices:**   - `"deny"` - `"allow"` |
| **mac-filter-policy-other**  string | Allow or block clients with MAC addresses that are not in the filter list.  **Choices:**   - `"deny"` - `"allow"` |
| **mac-password-delimiter**  string | MAC authentication password delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac-username-delimiter**  string | MAC authentication username delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **max-clients**  integer | Maximum number of clients that can connect simultaneously to the VAP |
| **max-clients-ap**  integer | Maximum number of clients that can connect simultaneously to each radio |
| **mbo**  string | Enable/disable Multiband Operation  **Choices:**   - `"disable"` - `"enable"` |
| **mbo-cell-data-conn-pref**  string | MBO cell data connection preference  **Choices:**   - `"excluded"` - `"prefer-not"` - `"prefer-use"` |
| **me-disable-thresh**  integer | Disable multicast enhancement when this many clients are receiving multicast traffic. |
| **mesh-backhaul**  string | Enable/disable using this VAP as a WiFi mesh backhaul  **Choices:**   - `"disable"` - `"enable"` |
| **mpsk**  string | Enable/disable multiple pre-shared keys  **Choices:**   - `"disable"` - `"enable"` |
| **mpsk-concurrent-clients**  integer | Number of pre-shared keys |
| **mpsk-key**  list / elements=dictionary | Mpsk-Key. |
| **comment**  string | Comment. |
| **concurrent-clients**  string | Number of clients that can connect using this pre-shared key. |
| **key-name**  string | Pre-shared key name. |
| **mpsk-schedules**  any | (list or str) Firewall schedule for MPSK passphrase. |
| **passphrase**  any | (list) WPA Pre-shared key. |
| **mpsk-profile**  string | MPSK profile name. |
| **mu-mimo**  string | Enable/disable Multi-user MIMO  **Choices:**   - `"disable"` - `"enable"` |
| **multicast-enhance**  string | Enable/disable converting multicast to unicast to improve performance  **Choices:**   - `"disable"` - `"enable"` |
| **multicast-rate**  string | Multicast rate  **Choices:**   - `"0"` - `"6000"` - `"12000"` - `"24000"` |
| **nac**  string | Enable/disable network access control.  **Choices:**   - `"disable"` - `"enable"` |
| **nac-profile**  string | NAC profile name. |
| **name**  string / required | Virtual AP name. |
| **neighbor-report-dual-band**  string | Enable/disable dual-band neighbor report  **Choices:**   - `"disable"` - `"enable"` |
| **okc**  string | Enable/disable Opportunistic Key Caching  **Choices:**   - `"disable"` - `"enable"` |
| **osen**  string | Enable/disable OSEN as part of key management  **Choices:**   - `"disable"` - `"enable"` |
| **owe-groups**  list / elements=string | OWE-Groups.  **Choices:**   - `"19"` - `"20"` - `"21"` |
| **owe-transition**  string | Enable/disable OWE transition mode support.  **Choices:**   - `"disable"` - `"enable"` |
| **owe-transition-ssid**  string | OWE transition mode peer SSID. |
| **passphrase**  any | (list) WPA pre-shared key |
| **pmf**  string | Protected Management Frames  **Choices:**   - `"disable"` - `"enable"` - `"optional"` |
| **pmf-assoc-comeback-timeout**  integer | Protected Management Frames |
| **pmf-sa-query-retry-timeout**  integer | Protected Management Frames |
| **port-macauth**  string | Enable/disable LAN port MAC authentication  **Choices:**   - `"disable"` - `"radius"` - `"address-group"` |
| **port-macauth-reauth-timeout**  integer | LAN port MAC authentication re-authentication timeout value |
| **port-macauth-timeout**  integer | LAN port MAC authentication idle timeout value |
| **portal-message-override-group**  string | Replacement message group for this VAP |
| **portal-message-overrides**  dictionary | no description |
| **auth-disclaimer-page**  string | Override auth-disclaimer-page message with message from portal-message-overrides group. |
| **auth-login-failed-page**  string | Override auth-login-failed-page message with message from portal-message-overrides group. |
| **auth-login-page**  string | Override auth-login-page message with message from portal-message-overrides group. |
| **auth-reject-page**  string | Override auth-reject-page message with message from portal-message-overrides group. |
| **portal-type**  string | Captive portal functionality.  **Choices:**   - `"auth"` - `"auth+disclaimer"` - `"disclaimer"` - `"email-collect"` - `"cmcc"` - `"cmcc-macauth"` - `"auth-mac"` - `"external-auth"` - `"external-macauth"` |
| **primary-wag-profile**  string | Primary wireless access gateway profile name. |
| **probe-resp-suppression**  string | Enable/disable probe response suppression  **Choices:**   - `"disable"` - `"enable"` |
| **probe-resp-threshold**  string | Minimum signal level/threshold in dBm required for the AP response to probe requests |
| **ptk-rekey**  string | Enable/disable PTK rekey for WPA-Enterprise security.  **Choices:**   - `"disable"` - `"enable"` |
| **ptk-rekey-intv**  integer | PTK rekey interval |
| **qos-profile**  string | Quality of service profile name. |
| **quarantine**  string | Enable/disable station quarantine  **Choices:**   - `"disable"` - `"enable"` |
| **radio-2g-threshold**  string | Minimum signal level/threshold in dBm required for the AP response to receive a packet in 2. |
| **radio-5g-threshold**  string | Minimum signal level/threshold in dBm required for the AP response to receive a packet in 5G band |
| **radio-sensitivity**  string | Enable/disable software radio sensitivity  **Choices:**   - `"disable"` - `"enable"` |
| **radius-mac-auth**  string | Enable/disable RADIUS-based MAC authentication of clients  **Choices:**   - `"disable"` - `"enable"` |
| **radius-mac-auth-block-interval**  integer | Dont send RADIUS MAC auth request again if the client has been rejected within specific interval |
| **radius-mac-auth-server**  string | RADIUS-based MAC authentication server. |
| **radius-mac-auth-usergroups**  any | (list) Selective user groups that are permitted for RADIUS mac authentication. |
| **radius-mac-mpsk-auth**  string | Enable/disable RADIUS-based MAC authentication of clients for MPSK authentication  **Choices:**   - `"disable"` - `"enable"` |
| **radius-mac-mpsk-timeout**  integer | RADIUS MAC MPSK cache timeout interval |
| **radius-server**  string | RADIUS server to be used to authenticate WiFi users. |
| **rates-11a**  list / elements=string | Allowed data rates for 802.  **Choices:**   - `"1"` - `"1-basic"` - `"2"` - `"2-basic"` - `"5.5"` - `"5.5-basic"` - `"6"` - `"6-basic"` - `"9"` - `"9-basic"` - `"12"` - `"12-basic"` - `"18"` - `"18-basic"` - `"24"` - `"24-basic"` - `"36"` - `"36-basic"` - `"48"` - `"48-basic"` - `"54"` - `"54-basic"` - `"11"` - `"11-basic"` |
| **rates-11ac-mcs-map**  string | Comma separated list of max supported VHT MCS for spatial streams 1 through 8. |
| **rates-11ac-ss12**  list / elements=string | Allowed data rates for 802.  **Choices:**   - `"mcs0/1"` - `"mcs1/1"` - `"mcs2/1"` - `"mcs3/1"` - `"mcs4/1"` - `"mcs5/1"` - `"mcs6/1"` - `"mcs7/1"` - `"mcs8/1"` - `"mcs9/1"` - `"mcs0/2"` - `"mcs1/2"` - `"mcs2/2"` - `"mcs3/2"` - `"mcs4/2"` - `"mcs5/2"` - `"mcs6/2"` - `"mcs7/2"` - `"mcs8/2"` - `"mcs9/2"` - `"mcs10/1"` - `"mcs11/1"` - `"mcs10/2"` - `"mcs11/2"` |
| **rates-11ac-ss34**  list / elements=string | Allowed data rates for 802.  **Choices:**   - `"mcs0/3"` - `"mcs1/3"` - `"mcs2/3"` - `"mcs3/3"` - `"mcs4/3"` - `"mcs5/3"` - `"mcs6/3"` - `"mcs7/3"` - `"mcs8/3"` - `"mcs9/3"` - `"mcs0/4"` - `"mcs1/4"` - `"mcs2/4"` - `"mcs3/4"` - `"mcs4/4"` - `"mcs5/4"` - `"mcs6/4"` - `"mcs7/4"` - `"mcs8/4"` - `"mcs9/4"` - `"mcs10/3"` - `"mcs11/3"` - `"mcs10/4"` - `"mcs11/4"` |
| **rates-11ax-mcs-map**  string | Comma separated list of max supported HE MCS for spatial streams 1 through 8. |
| **rates-11ax-ss12**  list / elements=string | no description  **Choices:**   - `"mcs0/1"` - `"mcs1/1"` - `"mcs2/1"` - `"mcs3/1"` - `"mcs4/1"` - `"mcs5/1"` - `"mcs6/1"` - `"mcs7/1"` - `"mcs8/1"` - `"mcs9/1"` - `"mcs10/1"` - `"mcs11/1"` - `"mcs0/2"` - `"mcs1/2"` - `"mcs2/2"` - `"mcs3/2"` - `"mcs4/2"` - `"mcs5/2"` - `"mcs6/2"` - `"mcs7/2"` - `"mcs8/2"` - `"mcs9/2"` - `"mcs10/2"` - `"mcs11/2"` |
| **rates-11ax-ss34**  list / elements=string | no description  **Choices:**   - `"mcs0/3"` - `"mcs1/3"` - `"mcs2/3"` - `"mcs3/3"` - `"mcs4/3"` - `"mcs5/3"` - `"mcs6/3"` - `"mcs7/3"` - `"mcs8/3"` - `"mcs9/3"` - `"mcs10/3"` - `"mcs11/3"` - `"mcs0/4"` - `"mcs1/4"` - `"mcs2/4"` - `"mcs3/4"` - `"mcs4/4"` - `"mcs5/4"` - `"mcs6/4"` - `"mcs7/4"` - `"mcs8/4"` - `"mcs9/4"` - `"mcs10/4"` - `"mcs11/4"` |
| **rates-11bg**  list / elements=string | Allowed data rates for 802.  **Choices:**   - `"1"` - `"1-basic"` - `"2"` - `"2-basic"` - `"5.5"` - `"5.5-basic"` - `"6"` - `"6-basic"` - `"9"` - `"9-basic"` - `"12"` - `"12-basic"` - `"18"` - `"18-basic"` - `"24"` - `"24-basic"` - `"36"` - `"36-basic"` - `"48"` - `"48-basic"` - `"54"` - `"54-basic"` - `"11"` - `"11-basic"` |
| **rates-11n-ss12**  list / elements=string | Allowed data rates for 802.  **Choices:**   - `"mcs0/1"` - `"mcs1/1"` - `"mcs2/1"` - `"mcs3/1"` - `"mcs4/1"` - `"mcs5/1"` - `"mcs6/1"` - `"mcs7/1"` - `"mcs8/2"` - `"mcs9/2"` - `"mcs10/2"` - `"mcs11/2"` - `"mcs12/2"` - `"mcs13/2"` - `"mcs14/2"` - `"mcs15/2"` |
| **rates-11n-ss34**  list / elements=string | Allowed data rates for 802.  **Choices:**   - `"mcs16/3"` - `"mcs17/3"` - `"mcs18/3"` - `"mcs19/3"` - `"mcs20/3"` - `"mcs21/3"` - `"mcs22/3"` - `"mcs23/3"` - `"mcs24/4"` - `"mcs25/4"` - `"mcs26/4"` - `"mcs27/4"` - `"mcs28/4"` - `"mcs29/4"` - `"mcs30/4"` - `"mcs31/4"` |
| **sae-groups**  list / elements=string | SAE-Groups.  **Choices:**   - `"1"` - `"2"` - `"5"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` |
| **sae-h2e-only**  string | Use hash-to-element-only mechanism for PWE derivation  **Choices:**   - `"disable"` - `"enable"` |
| **sae-password**  any | (list) WPA3 SAE password to be used to authenticate WiFi users. |
| **sae-pk**  string | Enable/disable WPA3 SAE-PK  **Choices:**   - `"disable"` - `"enable"` |
| **sae-private-key**  string | Private key used for WPA3 SAE-PK authentication. |
| **scan-botnet-connections**  string | Block or monitor connections to Botnet servers or disable Botnet scanning.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  any | (list or str) VAP schedule name. |
| **secondary-wag-profile**  string | Secondary wireless access gateway profile name. |
| **security**  string | Security mode for the wireless interface  **Choices:**   - `"None"` - `"WEP64"` - `"wep64"` - `"WEP128"` - `"wep128"` - `"WPA_PSK"` - `"WPA_RADIUS"` - `"WPA"` - `"WPA2"` - `"WPA2_AUTO"` - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` - `"captive-portal"` - `"wpa-only-personal"` - `"wpa-only-enterprise"` - `"wpa2-only-personal"` - `"wpa2-only-enterprise"` - `"wpa-personal+captive-portal"` - `"wpa-only-personal+captive-portal"` - `"wpa2-only-personal+captive-portal"` - `"osen"` - `"wpa3-enterprise"` - `"sae"` - `"sae-transition"` - `"owe"` - `"wpa3-sae"` - `"wpa3-sae-transition"` - `"wpa3-only-enterprise"` - `"wpa3-enterprise-transition"` |
| **security-exempt-list**  string | Optional security exempt list for captive portal authentication. |
| **security-obsolete-option**  string | Enable/disable obsolete security options.  **Choices:**   - `"disable"` - `"enable"` |
| **security-redirect-url**  string | Optional URL for redirecting users after they pass captive portal authentication. |
| **selected-usergroups**  any | (list or str) Selective user groups that are permitted to authenticate. |
| **split-tunneling**  string | Enable/disable split tunneling  **Choices:**   - `"disable"` - `"enable"` |
| **ssid**  string | IEEE 802. |
| **sticky-client-remove**  string | Enable/disable sticky client remove to maintain good signal level clients in SSID.  **Choices:**   - `"disable"` - `"enable"` |
| **sticky-client-threshold-2g**  string | Minimum signal level/threshold in dBm required for the 2G client to be serviced by the AP |
| **sticky-client-threshold-5g**  string | Minimum signal level/threshold in dBm required for the 5G client to be serviced by the AP |
| **sticky-client-threshold-6g**  string | Minimum signal level/threshold in dBm required for the 6G client to be serviced by the AP |
| **target-wake-time**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **tkip-counter-measure**  string | Enable/disable TKIP counter measure.  **Choices:**   - `"disable"` - `"enable"` |
| **tunnel-echo-interval**  integer | The time interval to send echo to both primary and secondary tunnel peers |
| **tunnel-fallback-interval**  integer | The time interval for secondary tunnel to fall back to primary tunnel |
| **usergroup**  any | (list or str) Firewall user group to be used to authenticate WiFi users. |
| **utm-log**  string | Enable/disable UTM logging.  **Choices:**   - `"disable"` - `"enable"` |
| **utm-profile**  string | UTM profile name. |
| **utm-status**  string | Enable to add one or more security profiles  **Choices:**   - `"disable"` - `"enable"` |
| **vdom**  string | Name of the VDOM that the Virtual AP has been added to. |
| **vlan-auto**  string | Enable/disable automatic management of SSID VLAN interface.  **Choices:**   - `"disable"` - `"enable"` |
| **vlan-name**  list / elements=dictionary | no description |
| **name**  string | VLAN name. |
| **vlan-id**  integer | VLAN ID. |
| **vlan-pool**  list / elements=dictionary | Vlan-Pool. |
| **_wtp-group**  string | _Wtp-Group. |
| **id**  integer | ID. |
| **wtp-group**  string | WTP group name. |
| **vlan-pooling**  string | Enable/disable VLAN pooling, to allow grouping of multiple wireless controller VLANs into VLAN pools  **Choices:**   - `"wtp-group"` - `"round-robin"` - `"hash"` - `"disable"` |
| **vlanid**  integer | Optional VLAN ID. |
| **voice-enterprise**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **webfilter-profile**  string | WebFilter profile name. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_vap_module.md#id4)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_vap_module.md#id5)

```yaml+jinja
- hosts: fortimanager-inventory
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
    - name: Configure Virtual Access Points
      fmgr_vap:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        vap:
          _centmgmt: <value in [disable, enable]>
          _dhcp_svr_id: <string>
          _intf_allowaccess:
            - https
            - ping
            - ssh
            - snmp
            - http
            - telnet
            - fgfm
            - auto-ipsec
            - radius-acct
            - probe-response
            - capwap
            - dnp
            - ftm
            - fabric
            - speed-test
          _intf_device-identification: <value in [disable, enable]>
          _intf_device-netscan: <value in [disable, enable]>
          _intf_dhcp-relay-ip: <list or string>
          _intf_dhcp-relay-service: <value in [disable, enable]>
          _intf_dhcp-relay-type: <value in [regular, ipsec]>
          _intf_dhcp6-relay-ip: <string>
          _intf_dhcp6-relay-service: <value in [disable, enable]>
          _intf_dhcp6-relay-type: <value in [regular]>
          _intf_ip: <string>
          _intf_ip6-address: <string>
          _intf_ip6-allowaccess:
            - https
            - ping
            - ssh
            - snmp
            - http
            - telnet
            - any
            - fgfm
            - capwap
          _intf_listen-forticlient-connection: <value in [disable, enable]>
          acct-interim-interval: <integer>
          alias: <string>
          auth: <value in [PSK, psk, RADIUS, ...]>
          broadcast-ssid: <value in [disable, enable]>
          broadcast-suppression:
            - dhcp
            - arp
            - dhcp2
            - arp2
            - netbios-ns
            - netbios-ds
            - arp3
            - dhcp-up
            - dhcp-down
            - arp-known
            - arp-unknown
            - arp-reply
            - ipv6
            - dhcp-starvation
            - arp-poison
            - all-other-mc
            - all-other-bc
            - arp-proxy
            - dhcp-ucast
          captive-portal-ac-name: <string>
          captive-portal-macauth-radius-secret: <list or string>
          captive-portal-macauth-radius-server: <string>
          captive-portal-radius-secret: <list or string>
          captive-portal-radius-server: <string>
          captive-portal-session-timeout-interval: <integer>
          dhcp-lease-time: <integer>
          dhcp-option82-circuit-id-insertion: <value in [disable, style-1, style-2, ...]>
          dhcp-option82-insertion: <value in [disable, enable]>
          dhcp-option82-remote-id-insertion: <value in [disable, style-1]>
          dynamic-vlan: <value in [disable, enable]>
          dynamic_mapping:
            -
              _centmgmt: <value in [disable, enable]>
              _dhcp_svr_id: <string>
              _intf_allowaccess:
                - https
                - ping
                - ssh
                - snmp
                - http
                - telnet
                - fgfm
                - auto-ipsec
                - radius-acct
                - probe-response
                - capwap
                - dnp
                - ftm
                - fabric
                - speed-test
              _intf_device-identification: <value in [disable, enable]>
              _intf_device-netscan: <value in [disable, enable]>
              _intf_dhcp-relay-ip: <list or string>
              _intf_dhcp-relay-service: <value in [disable, enable]>
              _intf_dhcp-relay-type: <value in [regular, ipsec]>
              _intf_dhcp6-relay-ip: <string>
              _intf_dhcp6-relay-service: <value in [disable, enable]>
              _intf_dhcp6-relay-type: <value in [regular]>
              _intf_ip: <string>
              _intf_ip6-address: <string>
              _intf_ip6-allowaccess:
                - https
                - ping
                - ssh
                - snmp
                - http
                - telnet
                - any
                - fgfm
                - capwap
              _intf_listen-forticlient-connection: <value in [disable, enable]>
              _scope:
                -
                  name: <string>
                  vdom: <string>
              acct-interim-interval: <integer>
              address-group: <string>
              alias: <string>
              atf-weight: <integer>
              auth: <value in [PSK, psk, RADIUS, ...]>
              broadcast-ssid: <value in [disable, enable]>
              broadcast-suppression:
                - dhcp
                - arp
                - dhcp2
                - arp2
                - netbios-ns
                - netbios-ds
                - arp3
                - dhcp-up
                - dhcp-down
                - arp-known
                - arp-unknown
                - arp-reply
                - ipv6
                - dhcp-starvation
                - arp-poison
                - all-other-mc
                - all-other-bc
                - arp-proxy
                - dhcp-ucast
              captive-portal-ac-name: <string>
              captive-portal-macauth-radius-secret: <list or string>
              captive-portal-macauth-radius-server: <string>
              captive-portal-radius-secret: <list or string>
              captive-portal-radius-server: <string>
              captive-portal-session-timeout-interval: <integer>
              client-count: <integer>
              dhcp-lease-time: <integer>
              dhcp-option82-circuit-id-insertion: <value in [disable, style-1, style-2, ...]>
              dhcp-option82-insertion: <value in [disable, enable]>
              dhcp-option82-remote-id-insertion: <value in [disable, style-1]>
              dynamic-vlan: <value in [disable, enable]>
              eap-reauth: <value in [disable, enable]>
              eap-reauth-intv: <integer>
              eapol-key-retries: <value in [disable, enable]>
              encrypt: <value in [TKIP, AES, TKIP-AES]>
              external-fast-roaming: <value in [disable, enable]>
              external-logout: <string>
              external-web: <string>
              fast-bss-transition: <value in [disable, enable]>
              fast-roaming: <value in [disable, enable]>
              ft-mobility-domain: <integer>
              ft-over-ds: <value in [disable, enable]>
              ft-r0-key-lifetime: <integer>
              gtk-rekey: <value in [disable, enable]>
              gtk-rekey-intv: <integer>
              hotspot20-profile: <string>
              intra-vap-privacy: <value in [disable, enable]>
              ip: <string>
              key: <list or string>
              keyindex: <integer>
              ldpc: <value in [disable, tx, rx, ...]>
              local-authentication: <value in [disable, enable]>
              local-bridging: <value in [disable, enable]>
              local-lan: <value in [deny, allow]>
              local-standalone: <value in [disable, enable]>
              local-standalone-nat: <value in [disable, enable]>
              local-switching: <value in [disable, enable]>
              mac-auth-bypass: <value in [disable, enable]>
              mac-filter: <value in [disable, enable]>
              mac-filter-policy-other: <value in [deny, allow]>
              max-clients: <integer>
              max-clients-ap: <integer>
              me-disable-thresh: <integer>
              mesh-backhaul: <value in [disable, enable]>
              mpsk: <value in [disable, enable]>
              mpsk-concurrent-clients: <integer>
              multicast-enhance: <value in [disable, enable]>
              multicast-rate: <value in [0, 6000, 12000, ...]>
              okc: <value in [disable, enable]>
              owe-groups:
                - 19
                - 20
                - 21
              owe-transition: <value in [disable, enable]>
              owe-transition-ssid: <string>
              passphrase: <list or string>
              pmf: <value in [disable, enable, optional]>
              pmf-assoc-comeback-timeout: <integer>
              pmf-sa-query-retry-timeout: <integer>
              portal-message-override-group: <string>
              portal-type: <value in [auth, auth+disclaimer, disclaimer, ...]>
              probe-resp-suppression: <value in [disable, enable]>
              probe-resp-threshold: <string>
              ptk-rekey: <value in [disable, enable]>
              ptk-rekey-intv: <integer>
              qos-profile: <string>
              quarantine: <value in [disable, enable]>
              radio-2g-threshold: <string>
              radio-5g-threshold: <string>
              radio-sensitivity: <value in [disable, enable]>
              radius-mac-auth: <value in [disable, enable]>
              radius-mac-auth-server: <string>
              radius-mac-auth-usergroups: <list or string>
              radius-server: <string>
              rates-11a:
                - 1
                - 1-basic
                - 2
                - 2-basic
                - 5.5
                - 5.5-basic
                - 6
                - 6-basic
                - 9
                - 9-basic
                - 12
                - 12-basic
                - 18
                - 18-basic
                - 24
                - 24-basic
                - 36
                - 36-basic
                - 48
                - 48-basic
                - 54
                - 54-basic
                - 11
                - 11-basic
              rates-11ac-ss12:
                - mcs0/1
                - mcs1/1
                - mcs2/1
                - mcs3/1
                - mcs4/1
                - mcs5/1
                - mcs6/1
                - mcs7/1
                - mcs8/1
                - mcs9/1
                - mcs0/2
                - mcs1/2
                - mcs2/2
                - mcs3/2
                - mcs4/2
                - mcs5/2
                - mcs6/2
                - mcs7/2
                - mcs8/2
                - mcs9/2
                - mcs10/1
                - mcs11/1
                - mcs10/2
                - mcs11/2
              rates-11ac-ss34:
                - mcs0/3
                - mcs1/3
                - mcs2/3
                - mcs3/3
                - mcs4/3
                - mcs5/3
                - mcs6/3
                - mcs7/3
                - mcs8/3
                - mcs9/3
                - mcs0/4
                - mcs1/4
                - mcs2/4
                - mcs3/4
                - mcs4/4
                - mcs5/4
                - mcs6/4
                - mcs7/4
                - mcs8/4
                - mcs9/4
                - mcs10/3
                - mcs11/3
                - mcs10/4
                - mcs11/4
              rates-11bg:
                - 1
                - 1-basic
                - 2
                - 2-basic
                - 5.5
                - 5.5-basic
                - 6
                - 6-basic
                - 9
                - 9-basic
                - 12
                - 12-basic
                - 18
                - 18-basic
                - 24
                - 24-basic
                - 36
                - 36-basic
                - 48
                - 48-basic
                - 54
                - 54-basic
                - 11
                - 11-basic
              rates-11n-ss12:
                - mcs0/1
                - mcs1/1
                - mcs2/1
                - mcs3/1
                - mcs4/1
                - mcs5/1
                - mcs6/1
                - mcs7/1
                - mcs8/2
                - mcs9/2
                - mcs10/2
                - mcs11/2
                - mcs12/2
                - mcs13/2
                - mcs14/2
                - mcs15/2
              rates-11n-ss34:
                - mcs16/3
                - mcs17/3
                - mcs18/3
                - mcs19/3
                - mcs20/3
                - mcs21/3
                - mcs22/3
                - mcs23/3
                - mcs24/4
                - mcs25/4
                - mcs26/4
                - mcs27/4
                - mcs28/4
                - mcs29/4
                - mcs30/4
                - mcs31/4
              sae-groups:
                - 1
                - 2
                - 5
                - 14
                - 15
                - 16
                - 17
                - 18
                - 19
                - 20
                - 21
                - 27
                - 28
                - 29
                - 30
                - 31
              sae-password: <list or string>
              schedule: <list or string>
              security: <value in [None, WEP64, wep64, ...]>
              security-exempt-list: <string>
              security-obsolete-option: <value in [disable, enable]>
              security-redirect-url: <string>
              selected-usergroups: <list or string>
              split-tunneling: <value in [disable, enable]>
              ssid: <string>
              tkip-counter-measure: <value in [disable, enable]>
              usergroup: <list or string>
              utm-profile: <string>
              vdom: <list or string>
              vlan-auto: <value in [disable, enable]>
              vlan-pooling: <value in [wtp-group, round-robin, hash, ...]>
              vlanid: <integer>
              voice-enterprise: <value in [disable, enable]>
              mu-mimo: <value in [disable, enable]>
              _intf_device-access-list: <string>
              external-web-format: <value in [auto-detect, no-query-string, partial-query-string]>
              high-efficiency: <value in [disable, enable]>
              primary-wag-profile: <string>
              secondary-wag-profile: <string>
              target-wake-time: <value in [disable, enable]>
              tunnel-echo-interval: <integer>
              tunnel-fallback-interval: <integer>
              access-control-list: <string>
              captive-portal-auth-timeout: <integer>
              ipv6-rules:
                - drop-icmp6ra
                - drop-icmp6rs
                - drop-llmnr6
                - drop-icmp6mld2
                - drop-dhcp6s
                - drop-dhcp6c
                - ndp-proxy
                - drop-ns-dad
                - drop-ns-nondad
              sticky-client-remove: <value in [disable, enable]>
              sticky-client-threshold-2g: <string>
              sticky-client-threshold-5g: <string>
              bss-color-partial: <value in [disable, enable]>
              dhcp-option43-insertion: <value in [disable, enable]>
              mpsk-profile: <string>
              igmp-snooping: <value in [disable, enable]>
              port-macauth: <value in [disable, radius, address-group]>
              port-macauth-reauth-timeout: <integer>
              port-macauth-timeout: <integer>
              additional-akms:
                - akm6
              bstm-disassociation-imminent: <value in [disable, enable]>
              bstm-load-balancing-disassoc-timer: <integer>
              bstm-rssi-disassoc-timer: <integer>
              dhcp-address-enforcement: <value in [disable, enable]>
              gas-comeback-delay: <integer>
              gas-fragmentation-limit: <integer>
              mac-called-station-delimiter: <value in [hyphen, single-hyphen, colon, ...]>
              mac-calling-station-delimiter: <value in [hyphen, single-hyphen, colon, ...]>
              mac-case: <value in [uppercase, lowercase]>
              mac-password-delimiter: <value in [hyphen, single-hyphen, colon, ...]>
              mac-username-delimiter: <value in [hyphen, single-hyphen, colon, ...]>
              mbo: <value in [disable, enable]>
              mbo-cell-data-conn-pref: <value in [excluded, prefer-not, prefer-use]>
              nac: <value in [disable, enable]>
              nac-profile: <string>
              neighbor-report-dual-band: <value in [disable, enable]>
              address-group-policy: <value in [disable, allow, deny]>
              antivirus-profile: <string>
              application-detection-engine: <value in [disable, enable]>
              application-list: <string>
              application-report-intv: <integer>
              auth-cert: <string>
              auth-portal-addr: <string>
              beacon-advertising:
                - name
                - model
                - serial-number
              ips-sensor: <string>
              l3-roaming: <value in [disable, enable]>
              local-standalone-dns: <value in [disable, enable]>
              local-standalone-dns-ip: <list or string>
              osen: <value in [disable, enable]>
              radius-mac-mpsk-auth: <value in [disable, enable]>
              radius-mac-mpsk-timeout: <integer>
              rates-11ax-ss12:
                - mcs0/1
                - mcs1/1
                - mcs2/1
                - mcs3/1
                - mcs4/1
                - mcs5/1
                - mcs6/1
                - mcs7/1
                - mcs8/1
                - mcs9/1
                - mcs10/1
                - mcs11/1
                - mcs0/2
                - mcs1/2
                - mcs2/2
                - mcs3/2
                - mcs4/2
                - mcs5/2
                - mcs6/2
                - mcs7/2
                - mcs8/2
                - mcs9/2
                - mcs10/2
                - mcs11/2
              rates-11ax-ss34:
                - mcs0/3
                - mcs1/3
                - mcs2/3
                - mcs3/3
                - mcs4/3
                - mcs5/3
                - mcs6/3
                - mcs7/3
                - mcs8/3
                - mcs9/3
                - mcs10/3
                - mcs11/3
                - mcs0/4
                - mcs1/4
                - mcs2/4
                - mcs3/4
                - mcs4/4
                - mcs5/4
                - mcs6/4
                - mcs7/4
                - mcs8/4
                - mcs9/4
                - mcs10/4
                - mcs11/4
              scan-botnet-connections: <value in [disable, block, monitor]>
              utm-log: <value in [disable, enable]>
              utm-status: <value in [disable, enable]>
              webfilter-profile: <string>
              sae-h2e-only: <value in [disable, enable]>
              sae-pk: <value in [disable, enable]>
              sae-private-key: <string>
              sticky-client-threshold-6g: <string>
              application-dscp-marking: <value in [disable, enable]>
              l3-roaming-mode: <value in [direct, indirect]>
              rates-11ac-mcs-map: <string>
              rates-11ax-mcs-map: <string>
              captive-portal-fw-accounting: <value in [disable, enable]>
              radius-mac-auth-block-interval: <integer>
              _is_factory_setting: <value in [disable, enable, ext]>
          eap-reauth: <value in [disable, enable]>
          eap-reauth-intv: <integer>
          eapol-key-retries: <value in [disable, enable]>
          encrypt: <value in [TKIP, AES, TKIP-AES]>
          external-fast-roaming: <value in [disable, enable]>
          external-logout: <string>
          external-web: <string>
          fast-bss-transition: <value in [disable, enable]>
          fast-roaming: <value in [disable, enable]>
          ft-mobility-domain: <integer>
          ft-over-ds: <value in [disable, enable]>
          ft-r0-key-lifetime: <integer>
          gtk-rekey: <value in [disable, enable]>
          gtk-rekey-intv: <integer>
          hotspot20-profile: <string>
          intra-vap-privacy: <value in [disable, enable]>
          ip: <string>
          key: <list or string>
          keyindex: <integer>
          ldpc: <value in [disable, tx, rx, ...]>
          local-authentication: <value in [disable, enable]>
          local-bridging: <value in [disable, enable]>
          local-lan: <value in [deny, allow]>
          local-standalone: <value in [disable, enable]>
          local-standalone-nat: <value in [disable, enable]>
          mac-auth-bypass: <value in [disable, enable]>
          mac-filter: <value in [disable, enable]>
          mac-filter-list:
            -
              id: <integer>
              mac: <string>
              mac-filter-policy: <value in [deny, allow]>
          mac-filter-policy-other: <value in [deny, allow]>
          max-clients: <integer>
          max-clients-ap: <integer>
          me-disable-thresh: <integer>
          mesh-backhaul: <value in [disable, enable]>
          mpsk: <value in [disable, enable]>
          mpsk-concurrent-clients: <integer>
          mpsk-key:
            -
              comment: <string>
              concurrent-clients: <string>
              key-name: <string>
              passphrase: <list or string>
              mpsk-schedules: <list or string>
          multicast-enhance: <value in [disable, enable]>
          multicast-rate: <value in [0, 6000, 12000, ...]>
          name: <string>
          okc: <value in [disable, enable]>
          passphrase: <list or string>
          pmf: <value in [disable, enable, optional]>
          pmf-assoc-comeback-timeout: <integer>
          pmf-sa-query-retry-timeout: <integer>
          portal-message-override-group: <string>
          portal-type: <value in [auth, auth+disclaimer, disclaimer, ...]>
          probe-resp-suppression: <value in [disable, enable]>
          probe-resp-threshold: <string>
          ptk-rekey: <value in [disable, enable]>
          ptk-rekey-intv: <integer>
          qos-profile: <string>
          quarantine: <value in [disable, enable]>
          radio-2g-threshold: <string>
          radio-5g-threshold: <string>
          radio-sensitivity: <value in [disable, enable]>
          radius-mac-auth: <value in [disable, enable]>
          radius-mac-auth-server: <string>
          radius-mac-auth-usergroups: <list or string>
          radius-server: <string>
          rates-11a:
            - 1
            - 1-basic
            - 2
            - 2-basic
            - 5.5
            - 5.5-basic
            - 6
            - 6-basic
            - 9
            - 9-basic
            - 12
            - 12-basic
            - 18
            - 18-basic
            - 24
            - 24-basic
            - 36
            - 36-basic
            - 48
            - 48-basic
            - 54
            - 54-basic
            - 11
            - 11-basic
          rates-11ac-ss12:
            - mcs0/1
            - mcs1/1
            - mcs2/1
            - mcs3/1
            - mcs4/1
            - mcs5/1
            - mcs6/1
            - mcs7/1
            - mcs8/1
            - mcs9/1
            - mcs0/2
            - mcs1/2
            - mcs2/2
            - mcs3/2
            - mcs4/2
            - mcs5/2
            - mcs6/2
            - mcs7/2
            - mcs8/2
            - mcs9/2
            - mcs10/1
            - mcs11/1
            - mcs10/2
            - mcs11/2
          rates-11ac-ss34:
            - mcs0/3
            - mcs1/3
            - mcs2/3
            - mcs3/3
            - mcs4/3
            - mcs5/3
            - mcs6/3
            - mcs7/3
            - mcs8/3
            - mcs9/3
            - mcs0/4
            - mcs1/4
            - mcs2/4
            - mcs3/4
            - mcs4/4
            - mcs5/4
            - mcs6/4
            - mcs7/4
            - mcs8/4
            - mcs9/4
            - mcs10/3
            - mcs11/3
            - mcs10/4
            - mcs11/4
          rates-11bg:
            - 1
            - 1-basic
            - 2
            - 2-basic
            - 5.5
            - 5.5-basic
            - 6
            - 6-basic
            - 9
            - 9-basic
            - 12
            - 12-basic
            - 18
            - 18-basic
            - 24
            - 24-basic
            - 36
            - 36-basic
            - 48
            - 48-basic
            - 54
            - 54-basic
            - 11
            - 11-basic
          rates-11n-ss12:
            - mcs0/1
            - mcs1/1
            - mcs2/1
            - mcs3/1
            - mcs4/1
            - mcs5/1
            - mcs6/1
            - mcs7/1
            - mcs8/2
            - mcs9/2
            - mcs10/2
            - mcs11/2
            - mcs12/2
            - mcs13/2
            - mcs14/2
            - mcs15/2
          rates-11n-ss34:
            - mcs16/3
            - mcs17/3
            - mcs18/3
            - mcs19/3
            - mcs20/3
            - mcs21/3
            - mcs22/3
            - mcs23/3
            - mcs24/4
            - mcs25/4
            - mcs26/4
            - mcs27/4
            - mcs28/4
            - mcs29/4
            - mcs30/4
            - mcs31/4
          schedule: <list or string>
          security: <value in [None, WEP64, wep64, ...]>
          security-exempt-list: <string>
          security-obsolete-option: <value in [disable, enable]>
          security-redirect-url: <string>
          selected-usergroups: <list or string>
          split-tunneling: <value in [disable, enable]>
          ssid: <string>
          tkip-counter-measure: <value in [disable, enable]>
          usergroup: <list or string>
          utm-profile: <string>
          vdom: <string>
          vlan-auto: <value in [disable, enable]>
          vlan-pool:
            -
              _wtp-group: <string>
              id: <integer>
              wtp-group: <string>
          vlan-pooling: <value in [wtp-group, round-robin, hash, ...]>
          vlanid: <integer>
          voice-enterprise: <value in [disable, enable]>
          address-group: <string>
          atf-weight: <integer>
          mu-mimo: <value in [disable, enable]>
          owe-groups:
            - 19
            - 20
            - 21
          owe-transition: <value in [disable, enable]>
          owe-transition-ssid: <string>
          sae-groups:
            - 1
            - 2
            - 5
            - 14
            - 15
            - 16
            - 17
            - 18
            - 19
            - 20
            - 21
            - 27
            - 28
            - 29
            - 30
            - 31
          sae-password: <list or string>
          _intf_device-access-list: <string>
          external-web-format: <value in [auto-detect, no-query-string, partial-query-string]>
          high-efficiency: <value in [disable, enable]>
          primary-wag-profile: <string>
          secondary-wag-profile: <string>
          target-wake-time: <value in [disable, enable]>
          tunnel-echo-interval: <integer>
          tunnel-fallback-interval: <integer>
          access-control-list: <string>
          captive-portal-auth-timeout: <integer>
          ipv6-rules:
            - drop-icmp6ra
            - drop-icmp6rs
            - drop-llmnr6
            - drop-icmp6mld2
            - drop-dhcp6s
            - drop-dhcp6c
            - ndp-proxy
            - drop-ns-dad
            - drop-ns-nondad
          sticky-client-remove: <value in [disable, enable]>
          sticky-client-threshold-2g: <string>
          sticky-client-threshold-5g: <string>
          bss-color-partial: <value in [disable, enable]>
          dhcp-option43-insertion: <value in [disable, enable]>
          mpsk-profile: <string>
          igmp-snooping: <value in [disable, enable]>
          port-macauth: <value in [disable, radius, address-group]>
          port-macauth-reauth-timeout: <integer>
          port-macauth-timeout: <integer>
          portal-message-overrides:
            auth-disclaimer-page: <string>
            auth-login-failed-page: <string>
            auth-login-page: <string>
            auth-reject-page: <string>
          additional-akms:
            - akm6
          bstm-disassociation-imminent: <value in [disable, enable]>
          bstm-load-balancing-disassoc-timer: <integer>
          bstm-rssi-disassoc-timer: <integer>
          dhcp-address-enforcement: <value in [disable, enable]>
          gas-comeback-delay: <integer>
          gas-fragmentation-limit: <integer>
          mac-called-station-delimiter: <value in [hyphen, single-hyphen, colon, ...]>
          mac-calling-station-delimiter: <value in [hyphen, single-hyphen, colon, ...]>
          mac-case: <value in [uppercase, lowercase]>
          mac-password-delimiter: <value in [hyphen, single-hyphen, colon, ...]>
          mac-username-delimiter: <value in [hyphen, single-hyphen, colon, ...]>
          mbo: <value in [disable, enable]>
          mbo-cell-data-conn-pref: <value in [excluded, prefer-not, prefer-use]>
          nac: <value in [disable, enable]>
          nac-profile: <string>
          neighbor-report-dual-band: <value in [disable, enable]>
          address-group-policy: <value in [disable, allow, deny]>
          antivirus-profile: <string>
          application-detection-engine: <value in [disable, enable]>
          application-list: <string>
          application-report-intv: <integer>
          auth-cert: <string>
          auth-portal-addr: <string>
          beacon-advertising:
            - name
            - model
            - serial-number
          ips-sensor: <string>
          l3-roaming: <value in [disable, enable]>
          local-standalone-dns: <value in [disable, enable]>
          local-standalone-dns-ip: <list or string>
          osen: <value in [disable, enable]>
          radius-mac-mpsk-auth: <value in [disable, enable]>
          radius-mac-mpsk-timeout: <integer>
          rates-11ax-ss12:
            - mcs0/1
            - mcs1/1
            - mcs2/1
            - mcs3/1
            - mcs4/1
            - mcs5/1
            - mcs6/1
            - mcs7/1
            - mcs8/1
            - mcs9/1
            - mcs10/1
            - mcs11/1
            - mcs0/2
            - mcs1/2
            - mcs2/2
            - mcs3/2
            - mcs4/2
            - mcs5/2
            - mcs6/2
            - mcs7/2
            - mcs8/2
            - mcs9/2
            - mcs10/2
            - mcs11/2
          rates-11ax-ss34:
            - mcs0/3
            - mcs1/3
            - mcs2/3
            - mcs3/3
            - mcs4/3
            - mcs5/3
            - mcs6/3
            - mcs7/3
            - mcs8/3
            - mcs9/3
            - mcs10/3
            - mcs11/3
            - mcs0/4
            - mcs1/4
            - mcs2/4
            - mcs3/4
            - mcs4/4
            - mcs5/4
            - mcs6/4
            - mcs7/4
            - mcs8/4
            - mcs9/4
            - mcs10/4
            - mcs11/4
          scan-botnet-connections: <value in [disable, block, monitor]>
          utm-log: <value in [disable, enable]>
          utm-status: <value in [disable, enable]>
          vlan-name:
            -
              name: <string>
              vlan-id: <integer>
          webfilter-profile: <string>
          sae-h2e-only: <value in [disable, enable]>
          sae-pk: <value in [disable, enable]>
          sae-private-key: <string>
          sticky-client-threshold-6g: <string>
          application-dscp-marking: <value in [disable, enable]>
          l3-roaming-mode: <value in [direct, indirect]>
          rates-11ac-mcs-map: <string>
          rates-11ax-mcs-map: <string>
          captive-portal-fw-accounting: <value in [disable, enable]>
          radius-mac-auth-block-interval: <integer>
          _is_factory_setting: <value in [disable, enable, ext]>
```

## [Return Values](fmgr_vap_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
