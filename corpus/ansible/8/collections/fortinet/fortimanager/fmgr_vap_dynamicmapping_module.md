---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_vap_dynamicmapping module – Configure Virtual Access Points"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_vap_dynamicmapping_module.html
fetched_at: 2026-07-28T02:21:23+00:00
---
# fortinet.fortimanager.fmgr_vap_dynamicmapping module – Configure Virtual Access Points

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_vap_dynamicmapping`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_vap_dynamicmapping_module.md#synopsis)
- [Parameters](fmgr_vap_dynamicmapping_module.md#parameters)
- [Notes](fmgr_vap_dynamicmapping_module.md#notes)
- [Examples](fmgr_vap_dynamicmapping_module.md#examples)
- [Return Values](fmgr_vap_dynamicmapping_module.md#return-values)

## [Synopsis](fmgr_vap_dynamicmapping_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_vap_dynamicmapping_module.md#id2)

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
| **vap**  string / required | the parameter (vap) in requested url |
| **vap_dynamicmapping**  dictionary | the top level parameters set |
| **_centmgmt**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **_dhcp_svr_id**  string | no description |
| **_intf_allowaccess**  list / elements=string | no description  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"auto-ipsec"` - `"radius-acct"` - `"probe-response"` - `"capwap"` - `"dnp"` - `"ftm"` - `"fabric"` - `"speed-test"` |
| **_intf_device-access-list**  string | no description |
| **_intf_device-identification**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **_intf_device-netscan**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **_intf_dhcp-relay-ip**  any | (list) no description |
| **_intf_dhcp-relay-service**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **_intf_dhcp-relay-type**  string | no description  **Choices:**   - `"regular"` - `"ipsec"` |
| **_intf_dhcp6-relay-ip**  string | no description |
| **_intf_dhcp6-relay-service**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **_intf_dhcp6-relay-type**  string | no description  **Choices:**   - `"regular"` |
| **_intf_ip**  string | no description |
| **_intf_ip6-address**  string | no description |
| **_intf_ip6-allowaccess**  list / elements=string | no description  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"any"` - `"fgfm"` - `"capwap"` |
| **_intf_listen-forticlient-connection**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **_is_factory_setting**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"ext"` |
| **_scope**  list / elements=dictionary | no description |
| **name**  string | no description |
| **vdom**  string | no description |
| **access-control-list**  string | no description |
| **acct-interim-interval**  integer | no description |
| **additional-akms**  list / elements=string | no description  **Choices:**   - `"akm6"` |
| **address-group**  string | no description |
| **address-group-policy**  string | Configure MAC address filtering policy for MAC addresses that are in the address-group.  **Choices:**   - `"disable"` - `"allow"` - `"deny"` |
| **alias**  string | no description |
| **antivirus-profile**  string | AntiVirus profile name. |
| **application-detection-engine**  string | Enable/disable application detection engine  **Choices:**   - `"disable"` - `"enable"` |
| **application-dscp-marking**  string | Enable/disable application attribute based DSCP marking  **Choices:**   - `"disable"` - `"enable"` |
| **application-list**  string | Application control list name. |
| **application-report-intv**  integer | Application report interval |
| **atf-weight**  integer | no description |
| **auth**  string | no description  **Choices:**   - `"PSK"` - `"psk"` - `"RADIUS"` - `"radius"` - `"usergroup"` |
| **auth-cert**  string | HTTPS server certificate. |
| **auth-portal-addr**  string | Address of captive portal. |
| **beacon-advertising**  list / elements=string | no description  **Choices:**   - `"name"` - `"model"` - `"serial-number"` |
| **broadcast-ssid**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **broadcast-suppression**  list / elements=string | no description  **Choices:**   - `"dhcp"` - `"arp"` - `"dhcp2"` - `"arp2"` - `"netbios-ns"` - `"netbios-ds"` - `"arp3"` - `"dhcp-up"` - `"dhcp-down"` - `"arp-known"` - `"arp-unknown"` - `"arp-reply"` - `"ipv6"` - `"dhcp-starvation"` - `"arp-poison"` - `"all-other-mc"` - `"all-other-bc"` - `"arp-proxy"` - `"dhcp-ucast"` |
| **bss-color-partial**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **bstm-disassociation-imminent**  string | Enable/disable forcing of disassociation after the BSTM request timer has been reached  **Choices:**   - `"disable"` - `"enable"` |
| **bstm-load-balancing-disassoc-timer**  integer | Time interval for client to voluntarily leave AP before forcing a disassociation due to AP load-balancing |
| **bstm-rssi-disassoc-timer**  integer | Time interval for client to voluntarily leave AP before forcing a disassociation due to low RSSI |
| **captive-portal-ac-name**  string | no description |
| **captive-portal-auth-timeout**  integer | no description |
| **captive-portal-fw-accounting**  string | Enable/disable RADIUS accounting for captive portal firewall authentication session.  **Choices:**   - `"disable"` - `"enable"` |
| **captive-portal-macauth-radius-secret**  any | (list) no description |
| **captive-portal-macauth-radius-server**  string | no description |
| **captive-portal-radius-secret**  any | (list) no description |
| **captive-portal-radius-server**  string | no description |
| **captive-portal-session-timeout-interval**  integer | no description |
| **client-count**  integer | no description |
| **dhcp-address-enforcement**  string | Enable/disable DHCP address enforcement  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-lease-time**  integer | no description |
| **dhcp-option43-insertion**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-option82-circuit-id-insertion**  string | no description  **Choices:**   - `"disable"` - `"style-1"` - `"style-2"` - `"style-3"` |
| **dhcp-option82-insertion**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-option82-remote-id-insertion**  string | no description  **Choices:**   - `"disable"` - `"style-1"` |
| **dynamic-vlan**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **eap-reauth**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **eap-reauth-intv**  integer | no description |
| **eapol-key-retries**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **encrypt**  string | no description  **Choices:**   - `"TKIP"` - `"AES"` - `"TKIP-AES"` |
| **external-fast-roaming**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **external-logout**  string | no description |
| **external-web**  string | no description |
| **external-web-format**  string | no description  **Choices:**   - `"auto-detect"` - `"no-query-string"` - `"partial-query-string"` |
| **fast-bss-transition**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **fast-roaming**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ft-mobility-domain**  integer | no description |
| **ft-over-ds**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ft-r0-key-lifetime**  integer | no description |
| **gas-comeback-delay**  integer | GAS comeback delay |
| **gas-fragmentation-limit**  integer | GAS fragmentation limit |
| **gtk-rekey**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **gtk-rekey-intv**  integer | no description |
| **high-efficiency**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **hotspot20-profile**  string | no description |
| **igmp-snooping**  string | Enable/disable IGMP snooping.  **Choices:**   - `"disable"` - `"enable"` |
| **intra-vap-privacy**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ip**  string | no description |
| **ips-sensor**  string | IPS sensor name. |
| **ipv6-rules**  list / elements=string | no description  **Choices:**   - `"drop-icmp6ra"` - `"drop-icmp6rs"` - `"drop-llmnr6"` - `"drop-icmp6mld2"` - `"drop-dhcp6s"` - `"drop-dhcp6c"` - `"ndp-proxy"` - `"drop-ns-dad"` - `"drop-ns-nondad"` |
| **key**  any | (list) no description |
| **keyindex**  integer | no description |
| **l3-roaming**  string | Enable/disable layer 3 roaming  **Choices:**   - `"disable"` - `"enable"` |
| **l3-roaming-mode**  string | Select the way that layer 3 roaming traffic is passed  **Choices:**   - `"direct"` - `"indirect"` |
| **ldpc**  string | no description  **Choices:**   - `"disable"` - `"tx"` - `"rx"` - `"rxtx"` |
| **local-authentication**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **local-bridging**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **local-lan**  string | no description  **Choices:**   - `"deny"` - `"allow"` |
| **local-standalone**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **local-standalone-dns**  string | Enable/disable AP local standalone DNS.  **Choices:**   - `"disable"` - `"enable"` |
| **local-standalone-dns-ip**  any | (list) no description |
| **local-standalone-nat**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **local-switching**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **mac-auth-bypass**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **mac-called-station-delimiter**  string | MAC called station delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac-calling-station-delimiter**  string | MAC calling station delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac-case**  string | MAC case  **Choices:**   - `"uppercase"` - `"lowercase"` |
| **mac-filter**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **mac-filter-policy-other**  string | no description  **Choices:**   - `"deny"` - `"allow"` |
| **mac-password-delimiter**  string | MAC authentication password delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **mac-username-delimiter**  string | MAC authentication username delimiter  **Choices:**   - `"hyphen"` - `"single-hyphen"` - `"colon"` - `"none"` |
| **max-clients**  integer | no description |
| **max-clients-ap**  integer | no description |
| **mbo**  string | Enable/disable Multiband Operation  **Choices:**   - `"disable"` - `"enable"` |
| **mbo-cell-data-conn-pref**  string | MBO cell data connection preference  **Choices:**   - `"excluded"` - `"prefer-not"` - `"prefer-use"` |
| **me-disable-thresh**  integer | no description |
| **mesh-backhaul**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **mpsk**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **mpsk-concurrent-clients**  integer | no description |
| **mpsk-profile**  string | no description |
| **mu-mimo**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **multicast-enhance**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **multicast-rate**  string | no description  **Choices:**   - `"0"` - `"6000"` - `"12000"` - `"24000"` |
| **nac**  string | Enable/disable network access control.  **Choices:**   - `"disable"` - `"enable"` |
| **nac-profile**  string | NAC profile name. |
| **neighbor-report-dual-band**  string | Enable/disable dual-band neighbor report  **Choices:**   - `"disable"` - `"enable"` |
| **okc**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **osen**  string | Enable/disable OSEN as part of key management  **Choices:**   - `"disable"` - `"enable"` |
| **owe-groups**  list / elements=string | no description  **Choices:**   - `"19"` - `"20"` - `"21"` |
| **owe-transition**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **owe-transition-ssid**  string | no description |
| **passphrase**  any | (list) no description |
| **pmf**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"optional"` |
| **pmf-assoc-comeback-timeout**  integer | no description |
| **pmf-sa-query-retry-timeout**  integer | no description |
| **port-macauth**  string | Enable/disable LAN port MAC authentication  **Choices:**   - `"disable"` - `"radius"` - `"address-group"` |
| **port-macauth-reauth-timeout**  integer | LAN port MAC authentication re-authentication timeout value |
| **port-macauth-timeout**  integer | LAN port MAC authentication idle timeout value |
| **portal-message-override-group**  string | no description |
| **portal-type**  string | no description  **Choices:**   - `"auth"` - `"auth+disclaimer"` - `"disclaimer"` - `"email-collect"` - `"cmcc"` - `"cmcc-macauth"` - `"auth-mac"` - `"external-auth"` - `"external-macauth"` |
| **primary-wag-profile**  string | no description |
| **probe-resp-suppression**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **probe-resp-threshold**  string | no description |
| **ptk-rekey**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ptk-rekey-intv**  integer | no description |
| **qos-profile**  string | no description |
| **quarantine**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **radio-2g-threshold**  string | no description |
| **radio-5g-threshold**  string | no description |
| **radio-sensitivity**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **radius-mac-auth**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **radius-mac-auth-block-interval**  integer | Dont send RADIUS MAC auth request again if the client has been rejected within specific interval |
| **radius-mac-auth-server**  string | no description |
| **radius-mac-auth-usergroups**  any | (list) no description |
| **radius-mac-mpsk-auth**  string | Enable/disable RADIUS-based MAC authentication of clients for MPSK authentication  **Choices:**   - `"disable"` - `"enable"` |
| **radius-mac-mpsk-timeout**  integer | RADIUS MAC MPSK cache timeout interval |
| **radius-server**  string | no description |
| **rates-11a**  list / elements=string | no description  **Choices:**   - `"1"` - `"1-basic"` - `"2"` - `"2-basic"` - `"5.5"` - `"5.5-basic"` - `"6"` - `"6-basic"` - `"9"` - `"9-basic"` - `"12"` - `"12-basic"` - `"18"` - `"18-basic"` - `"24"` - `"24-basic"` - `"36"` - `"36-basic"` - `"48"` - `"48-basic"` - `"54"` - `"54-basic"` - `"11"` - `"11-basic"` |
| **rates-11ac-mcs-map**  string | Comma separated list of max supported VHT MCS for spatial streams 1 through 8. |
| **rates-11ac-ss12**  list / elements=string | no description  **Choices:**   - `"mcs0/1"` - `"mcs1/1"` - `"mcs2/1"` - `"mcs3/1"` - `"mcs4/1"` - `"mcs5/1"` - `"mcs6/1"` - `"mcs7/1"` - `"mcs8/1"` - `"mcs9/1"` - `"mcs0/2"` - `"mcs1/2"` - `"mcs2/2"` - `"mcs3/2"` - `"mcs4/2"` - `"mcs5/2"` - `"mcs6/2"` - `"mcs7/2"` - `"mcs8/2"` - `"mcs9/2"` - `"mcs10/1"` - `"mcs11/1"` - `"mcs10/2"` - `"mcs11/2"` |
| **rates-11ac-ss34**  list / elements=string | no description  **Choices:**   - `"mcs0/3"` - `"mcs1/3"` - `"mcs2/3"` - `"mcs3/3"` - `"mcs4/3"` - `"mcs5/3"` - `"mcs6/3"` - `"mcs7/3"` - `"mcs8/3"` - `"mcs9/3"` - `"mcs0/4"` - `"mcs1/4"` - `"mcs2/4"` - `"mcs3/4"` - `"mcs4/4"` - `"mcs5/4"` - `"mcs6/4"` - `"mcs7/4"` - `"mcs8/4"` - `"mcs9/4"` - `"mcs10/3"` - `"mcs11/3"` - `"mcs10/4"` - `"mcs11/4"` |
| **rates-11ax-mcs-map**  string | Comma separated list of max supported HE MCS for spatial streams 1 through 8. |
| **rates-11ax-ss12**  list / elements=string | no description  **Choices:**   - `"mcs0/1"` - `"mcs1/1"` - `"mcs2/1"` - `"mcs3/1"` - `"mcs4/1"` - `"mcs5/1"` - `"mcs6/1"` - `"mcs7/1"` - `"mcs8/1"` - `"mcs9/1"` - `"mcs10/1"` - `"mcs11/1"` - `"mcs0/2"` - `"mcs1/2"` - `"mcs2/2"` - `"mcs3/2"` - `"mcs4/2"` - `"mcs5/2"` - `"mcs6/2"` - `"mcs7/2"` - `"mcs8/2"` - `"mcs9/2"` - `"mcs10/2"` - `"mcs11/2"` |
| **rates-11ax-ss34**  list / elements=string | no description  **Choices:**   - `"mcs0/3"` - `"mcs1/3"` - `"mcs2/3"` - `"mcs3/3"` - `"mcs4/3"` - `"mcs5/3"` - `"mcs6/3"` - `"mcs7/3"` - `"mcs8/3"` - `"mcs9/3"` - `"mcs10/3"` - `"mcs11/3"` - `"mcs0/4"` - `"mcs1/4"` - `"mcs2/4"` - `"mcs3/4"` - `"mcs4/4"` - `"mcs5/4"` - `"mcs6/4"` - `"mcs7/4"` - `"mcs8/4"` - `"mcs9/4"` - `"mcs10/4"` - `"mcs11/4"` |
| **rates-11bg**  list / elements=string | no description  **Choices:**   - `"1"` - `"1-basic"` - `"2"` - `"2-basic"` - `"5.5"` - `"5.5-basic"` - `"6"` - `"6-basic"` - `"9"` - `"9-basic"` - `"12"` - `"12-basic"` - `"18"` - `"18-basic"` - `"24"` - `"24-basic"` - `"36"` - `"36-basic"` - `"48"` - `"48-basic"` - `"54"` - `"54-basic"` - `"11"` - `"11-basic"` |
| **rates-11n-ss12**  list / elements=string | no description  **Choices:**   - `"mcs0/1"` - `"mcs1/1"` - `"mcs2/1"` - `"mcs3/1"` - `"mcs4/1"` - `"mcs5/1"` - `"mcs6/1"` - `"mcs7/1"` - `"mcs8/2"` - `"mcs9/2"` - `"mcs10/2"` - `"mcs11/2"` - `"mcs12/2"` - `"mcs13/2"` - `"mcs14/2"` - `"mcs15/2"` |
| **rates-11n-ss34**  list / elements=string | no description  **Choices:**   - `"mcs16/3"` - `"mcs17/3"` - `"mcs18/3"` - `"mcs19/3"` - `"mcs20/3"` - `"mcs21/3"` - `"mcs22/3"` - `"mcs23/3"` - `"mcs24/4"` - `"mcs25/4"` - `"mcs26/4"` - `"mcs27/4"` - `"mcs28/4"` - `"mcs29/4"` - `"mcs30/4"` - `"mcs31/4"` |
| **sae-groups**  list / elements=string | no description  **Choices:**   - `"1"` - `"2"` - `"5"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` |
| **sae-h2e-only**  string | Use hash-to-element-only mechanism for PWE derivation  **Choices:**   - `"disable"` - `"enable"` |
| **sae-password**  any | (list) no description |
| **sae-pk**  string | Enable/disable WPA3 SAE-PK  **Choices:**   - `"disable"` - `"enable"` |
| **sae-private-key**  string | Private key used for WPA3 SAE-PK authentication. |
| **scan-botnet-connections**  string | Block or monitor connections to Botnet servers or disable Botnet scanning.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **schedule**  any | (list or str) no description |
| **secondary-wag-profile**  string | no description |
| **security**  string | no description  **Choices:**   - `"None"` - `"WEP64"` - `"wep64"` - `"WEP128"` - `"wep128"` - `"WPA_PSK"` - `"WPA_RADIUS"` - `"WPA"` - `"WPA2"` - `"WPA2_AUTO"` - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` - `"captive-portal"` - `"wpa-only-personal"` - `"wpa-only-enterprise"` - `"wpa2-only-personal"` - `"wpa2-only-enterprise"` - `"wpa-personal+captive-portal"` - `"wpa-only-personal+captive-portal"` - `"wpa2-only-personal+captive-portal"` - `"osen"` - `"wpa3-enterprise"` - `"sae"` - `"sae-transition"` - `"owe"` - `"wpa3-sae"` - `"wpa3-sae-transition"` - `"wpa3-only-enterprise"` - `"wpa3-enterprise-transition"` |
| **security-exempt-list**  string | no description |
| **security-obsolete-option**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **security-redirect-url**  string | no description |
| **selected-usergroups**  any | (list or str) no description |
| **split-tunneling**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ssid**  string | no description |
| **sticky-client-remove**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sticky-client-threshold-2g**  string | no description |
| **sticky-client-threshold-5g**  string | no description |
| **sticky-client-threshold-6g**  string | Minimum signal level/threshold in dBm required for the 6G client to be serviced by the AP |
| **target-wake-time**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **tkip-counter-measure**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **tunnel-echo-interval**  integer | no description |
| **tunnel-fallback-interval**  integer | no description |
| **usergroup**  any | (list or str) no description |
| **utm-log**  string | Enable/disable UTM logging.  **Choices:**   - `"disable"` - `"enable"` |
| **utm-profile**  string | no description |
| **utm-status**  string | Enable to add one or more security profiles  **Choices:**   - `"disable"` - `"enable"` |
| **vdom**  any | (list or str) no description |
| **vlan-auto**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **vlan-pooling**  string | no description  **Choices:**   - `"wtp-group"` - `"round-robin"` - `"hash"` - `"disable"` |
| **vlanid**  integer | no description |
| **voice-enterprise**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **webfilter-profile**  string | WebFilter profile name. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_vap_dynamicmapping_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_vap_dynamicmapping_module.md#id4)

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
      fmgr_vap_dynamicmapping:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        vap: <your own value>
        state: <value in [present, absent]>
        vap_dynamicmapping:
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
```

## [Return Values](fmgr_vap_dynamicmapping_module.md#id5)

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
