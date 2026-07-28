---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_wtpprofile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_wtpprofile_module.html
fetched_at: 2026-07-27T17:39:40+00:00
---
# fortinet.fortimanager.fmgr_wtpprofile module – no description

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/fortinet/fortimanager) (version 2.1.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_wtpprofile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_wtpprofile_module.md#synopsis)
- [Parameters](fmgr_wtpprofile_module.md#parameters)
- [Notes](fmgr_wtpprofile_module.md#notes)
- [Examples](fmgr_wtpprofile_module.md#examples)
- [Return Values](fmgr_wtpprofile_module.md#return-values)

## [Synopsis](fmgr_wtpprofile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_wtpprofile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |
| **wtpprofile**  dictionary | the top level parameters set |
| **allowaccess**  list / elements=string | no description  Choices:   - `"https"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` |
| **ap-country**  string | no description  Choices:   - `"AL"` - `"DZ"` - `"AR"` - `"AM"` - `"AU"` - `"AT"` - `"AZ"` - `"BH"` - `"BD"` - `"BY"` - `"BE"` - `"BZ"` - `"BO"` - `"BA"` - `"BR"` - `"BN"` - `"BG"` - `"CA"` - `"CL"` - `"CN"` - `"CO"` - `"CR"` - `"HR"` - `"CY"` - `"CZ"` - `"DK"` - `"DO"` - `"EC"` - `"EG"` - `"SV"` - `"EE"` - `"FI"` - `"FR"` - `"GE"` - `"DE"` - `"GR"` - `"GT"` - `"HN"` - `"HK"` - `"HU"` - `"IS"` - `"IN"` - `"ID"` - `"IR"` - `"IE"` - `"IL"` - `"IT"` - `"JM"` - `"JP"` - `"JO"` - `"KZ"` - `"KE"` - `"KP"` - `"KR"` - `"KW"` - `"LV"` - `"LB"` - `"LI"` - `"LT"` - `"LU"` - `"MO"` - `"MK"` - `"MY"` - `"MT"` - `"MX"` - `"MC"` - `"MA"` - `"NP"` - `"NL"` - `"AN"` - `"NZ"` - `"NO"` - `"OM"` - `"PK"` - `"PA"` - `"PG"` - `"PE"` - `"PH"` - `"PL"` - `"PT"` - `"PR"` - `"QA"` - `"RO"` - `"RU"` - `"SA"` - `"SG"` - `"SK"` - `"SI"` - `"ZA"` - `"ES"` - `"LK"` - `"SE"` - `"CH"` - `"SY"` - `"TW"` - `"TH"` - `"TT"` - `"TN"` - `"TR"` - `"AE"` - `"UA"` - `"GB"` - `"US"` - `"PS"` - `"UY"` - `"UZ"` - `"VE"` - `"VN"` - `"YE"` - `"ZW"` - `"NA"` - `"KH"` - `"TZ"` - `"SD"` - `"AO"` - `"RW"` - `"MZ"` - `"RS"` - `"ME"` - `"BB"` - `"GD"` - `"GL"` - `"GU"` - `"PY"` - `"HT"` - `"AW"` - `"MM"` - `"ZB"` - `"CF"` - `"BS"` - `"VC"` - `"MV"` - `"SN"` - `"CI"` - `"GH"` - `"MW"` - `"UG"` - `"BF"` - `"KY"` - `"TC"` - `"TM"` - `"VU"` - `"FM"` - `"GY"` - `"KN"` - `"LC"` - `"CX"` - `"AF"` - `"CM"` - `"ML"` - `"BJ"` - `"MG"` - `"TD"` - `"BW"` - `"LY"` - `"LS"` - `"MU"` - `"SL"` - `"NE"` - `"TG"` - `"RE"` - `"MD"` - `"BM"` - `"VI"` - `"PM"` - `"MF"` - `"IM"` - `"FO"` - `"GI"` - `"LA"` - `"WF"` - `"MH"` - `"BT"` - `"PF"` - `"NI"` - `"GF"` - `"AS"` - `"MP"` - `"PW"` - `"GP"` - `"ET"` - `"SR"` - `"DM"` - `"MQ"` - `"YT"` - `"BL"` - `"ZM"` - `"CG"` - `"CD"` - `"MR"` - `"IQ"` - `"FJ"` - `"--"` |
| **ap-handoff**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **apcfg-profile**  string | no description |
| **ble-profile**  string | no description |
| **comment**  string | no description |
| **console-login**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **control-message-offload**  list / elements=string | no description  Choices:   - `"ebp-frame"` - `"aeroscout-tag"` - `"ap-list"` - `"sta-list"` - `"sta-cap-list"` - `"stats"` - `"aeroscout-mu"` - `"sta-health"` - `"spectral-analysis"` |
| **deny-mac-list**  list / elements=string | no description |
| **id**  integer | no description |
| **mac**  string | no description |
| **dtls-in-kernel**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dtls-policy**  list / elements=string | no description  Choices:   - `"clear-text"` - `"dtls-enabled"` - `"ipsec-vpn"` |
| **energy-efficient-ethernet**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **esl-ses-dongle**  dictionary | no description |
| **apc-addr-type**  string | no description  Choices:   - `"fqdn"` - `"ip"` |
| **apc-fqdn**  string | no description |
| **apc-ip**  string | no description |
| **apc-port**  integer | no description |
| **coex-level**  string | no description  Choices:   - `"none"` |
| **compliance-level**  string | no description  Choices:   - `"compliance-level-2"` |
| **esl-channel**  string | no description  Choices:   - `"0"` - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` - `"6"` - `"7"` - `"8"` - `"9"` - `"10"` - `"127"` - `"-1"` |
| **output-power**  string | no description  Choices:   - `"a"` - `"b"` - `"c"` - `"d"` - `"e"` - `"f"` - `"g"` - `"h"` |
| **scd-enable**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tls-cert-verification**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tls-fqdn-verification**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ext-info-enable**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **frequency-handoff**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **handoff-roaming**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **handoff-rssi**  integer | no description |
| **handoff-sta-thresh**  integer | no description |
| **indoor-outdoor-deployment**  string | no description  Choices:   - `"platform-determined"` - `"outdoor"` - `"indoor"` |
| **ip-fragment-preventing**  list / elements=string | no description  Choices:   - `"tcp-mss-adjust"` - `"icmp-unreachable"` |
| **lan**  dictionary | no description |
| **port-esl-mode**  string | no description  Choices:   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port-esl-ssid**  string | no description |
| **port-mode**  string | no description  Choices:   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port-ssid**  string | no description |
| **port1-mode**  string | no description  Choices:   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port1-ssid**  string | no description |
| **port2-mode**  string | no description  Choices:   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port2-ssid**  string | no description |
| **port3-mode**  string | no description  Choices:   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port3-ssid**  string | no description |
| **port4-mode**  string | no description  Choices:   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port4-ssid**  string | no description |
| **port5-mode**  string | no description  Choices:   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port5-ssid**  string | no description |
| **port6-mode**  string | no description  Choices:   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port6-ssid**  string | no description |
| **port7-mode**  string | no description  Choices:   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port7-ssid**  string | no description |
| **port8-mode**  string | no description  Choices:   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port8-ssid**  string | no description |
| **lbs**  dictionary | no description |
| **aeroscout**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **aeroscout-ap-mac**  string | no description  Choices:   - `"bssid"` - `"board-mac"` |
| **aeroscout-mmu-report**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **aeroscout-mu**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **aeroscout-mu-factor**  integer | no description |
| **aeroscout-mu-timeout**  integer | no description |
| **aeroscout-server-ip**  string | no description |
| **aeroscout-server-port**  integer | no description |
| **ekahau-blink-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ekahau-tag**  string | no description |
| **erc-server-ip**  string | no description |
| **erc-server-port**  integer | no description |
| **fortipresence**  string | no description  Choices:   - `"disable"` - `"enable"` - `"enable2"` - `"foreign"` - `"both"` |
| **fortipresence-ble**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fortipresence-frequency**  integer | no description |
| **fortipresence-port**  integer | no description |
| **fortipresence-project**  string | no description |
| **fortipresence-rogue**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fortipresence-secret**  string | no description |
| **fortipresence-server**  string | no description |
| **fortipresence-server-addr-type**  string | no description  Choices:   - `"fqdn"` - `"ipv4"` |
| **fortipresence-server-fqdn**  string | no description |
| **fortipresence-unassoc**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **station-locate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **led-schedules**  string | no description |
| **led-state**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **lldp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **login-passwd**  string | no description |
| **login-passwd-change**  string | no description  Choices:   - `"no"` - `"yes"` - `"default"` |
| **max-clients**  integer | no description |
| **name**  string | no description |
| **platform**  dictionary | no description |
| **_local_platform_str**  string | no description |
| **ddscan**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mode**  string | no description  Choices:   - `"dual-5G"` - `"single-5G"` |
| **type**  string | no description  Choices:   - `"30B-50B"` - `"60B"` - `"80CM-81CM"` - `"220A"` - `"220B"` - `"210B"` - `"60C"` - `"222B"` - `"112B"` - `"320B"` - `"11C"` - `"14C"` - `"223B"` - `"28C"` - `"320C"` - `"221C"` - `"25D"` - `"222C"` - `"224D"` - `"214B"` - `"21D"` - `"24D"` - `"112D"` - `"223C"` - `"321C"` - `"C220C"` - `"C225C"` - `"S321C"` - `"S323C"` - `"FWF"` - `"S311C"` - `"S313C"` - `"AP-11N"` - `"S322C"` - `"S321CR"` - `"S322CR"` - `"S323CR"` - `"S421E"` - `"S422E"` - `"S423E"` - `"421E"` - `"423E"` - `"C221E"` - `"C226E"` - `"C23JD"` - `"C24JE"` - `"C21D"` - `"U421E"` - `"U423E"` - `"221E"` - `"222E"` - `"223E"` - `"S221E"` - `"S223E"` - `"U221EV"` - `"U223EV"` - `"U321EV"` - `"U323EV"` - `"224E"` - `"U422EV"` - `"U24JEV"` - `"321E"` - `"U431F"` - `"U433F"` - `"231E"` - `"431F"` - `"433F"` - `"231F"` - `"432F"` - `"234F"` - `"23JF"` - `"U231F"` - `"831F"` - `"U234F"` - `"U432F"` |
| **poe-mode**  string | no description  Choices:   - `"auto"` - `"8023af"` - `"8023at"` - `"power-adapter"` - `"full"` - `"high"` - `"low"` |
| **radio-1**  dictionary | no description |
| **airtime-fairness**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **amsdu**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-addr**  string | no description |
| **ap-sniffer-bufsize**  integer | no description |
| **ap-sniffer-chan**  integer | no description |
| **ap-sniffer-ctl**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-data**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-beacon**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-other**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-probe**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **arrp-profile**  string | no description |
| **auto-power-high**  integer | no description |
| **auto-power-level**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auto-power-low**  integer | no description |
| **auto-power-target**  string | no description |
| **band**  string | no description  Choices:   - `"802.11b"` - `"802.11a"` - `"802.11g"` - `"802.11n"` - `"802.11ac"` - `"802.11n-5G"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n,g-only"` - `"802.11ac-only"` - `"802.11ac,n-only"` - `"802.11n-5G-only"` - `"802.11ax-5G-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` |
| **band-5g-type**  string | no description  Choices:   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth-admission-control**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **bandwidth-capacity**  integer | no description |
| **beacon-interval**  integer | no description |
| **bss-color**  integer | no description |
| **bss-color-mode**  string | no description  Choices:   - `"auto"` - `"static"` |
| **call-admission-control**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **call-capacity**  integer | no description |
| **channel**  string | no description |
| **channel-bonding**  string | no description  Choices:   - `"disable"` - `"enable"` - `"80MHz"` - `"40MHz"` - `"20MHz"` - `"160MHz"` |
| **channel-utilization**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **coexistence**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **darrp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **drma**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **drma-sensitivity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | no description |
| **frag-threshold**  integer | no description |
| **iperf-protocol**  string | no description  Choices:   - `"udp"` - `"tcp"` |
| **iperf-server-port**  integer | no description |
| **max-clients**  integer | no description |
| **max-distance**  integer | no description |
| **mode**  string | no description  Choices:   - `"disabled"` - `"ap"` - `"monitor"` - `"sniffer"` - `"sam"` |
| **power-level**  integer | no description |
| **power-mode**  string | no description  Choices:   - `"dBm"` - `"percentage"` |
| **power-value**  integer | no description |
| **powersave-optimize**  list / elements=string | no description  Choices:   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection-mode**  string | no description  Choices:   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio-id**  integer | no description |
| **rts-threshold**  integer | no description |
| **sam-bssid**  string | no description |
| **sam-captive-portal**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sam-cwp-failure-string**  string | no description |
| **sam-cwp-match-string**  string | no description |
| **sam-cwp-password**  string | description |
| **sam-cwp-success-string**  string | no description |
| **sam-cwp-test-url**  string | no description |
| **sam-cwp-username**  string | no description |
| **sam-password**  string | no description |
| **sam-report-intv**  integer | no description |
| **sam-security-type**  string | no description  Choices:   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam-server**  string | no description |
| **sam-server-fqdn**  string | no description |
| **sam-server-ip**  string | no description |
| **sam-server-type**  string | no description  Choices:   - `"ip"` - `"fqdn"` |
| **sam-ssid**  string | no description |
| **sam-test**  string | no description  Choices:   - `"ping"` - `"iperf"` |
| **sam-username**  string | no description |
| **short-guard-interval**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **spectrum-analysis**  string | no description  Choices:   - `"disable"` - `"enable"` - `"scan-only"` |
| **transmit-optimize**  list / elements=string | no description  Choices:   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap-all**  string | no description  Choices:   - `"disable"` - `"enable"` - `"tunnel"` - `"bridge"` - `"manual"` |
| **vap1**  string | no description |
| **vap2**  string | no description |
| **vap3**  string | no description |
| **vap4**  string | no description |
| **vap5**  string | no description |
| **vap6**  string | no description |
| **vap7**  string | no description |
| **vap8**  string | no description |
| **vaps**  string | no description |
| **wids-profile**  string | no description |
| **zero-wait-dfs**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **radio-2**  dictionary | no description |
| **airtime-fairness**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **amsdu**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-addr**  string | no description |
| **ap-sniffer-bufsize**  integer | no description |
| **ap-sniffer-chan**  integer | no description |
| **ap-sniffer-ctl**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-data**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-beacon**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-other**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-probe**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **arrp-profile**  string | no description |
| **auto-power-high**  integer | no description |
| **auto-power-level**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auto-power-low**  integer | no description |
| **auto-power-target**  string | no description |
| **band**  string | no description  Choices:   - `"802.11b"` - `"802.11a"` - `"802.11g"` - `"802.11n"` - `"802.11ac"` - `"802.11n-5G"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n,g-only"` - `"802.11ac-only"` - `"802.11ac,n-only"` - `"802.11n-5G-only"` - `"802.11ax-5G-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` |
| **band-5g-type**  string | no description  Choices:   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth-admission-control**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **bandwidth-capacity**  integer | no description |
| **beacon-interval**  integer | no description |
| **bss-color**  integer | no description |
| **bss-color-mode**  string | no description  Choices:   - `"auto"` - `"static"` |
| **call-admission-control**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **call-capacity**  integer | no description |
| **channel**  string | no description |
| **channel-bonding**  string | no description  Choices:   - `"disable"` - `"enable"` - `"80MHz"` - `"40MHz"` - `"20MHz"` - `"160MHz"` |
| **channel-utilization**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **coexistence**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **darrp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **drma**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **drma-sensitivity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | no description |
| **frag-threshold**  integer | no description |
| **iperf-protocol**  string | no description  Choices:   - `"udp"` - `"tcp"` |
| **iperf-server-port**  integer | no description |
| **max-clients**  integer | no description |
| **max-distance**  integer | no description |
| **mode**  string | no description  Choices:   - `"disabled"` - `"ap"` - `"monitor"` - `"sniffer"` - `"sam"` |
| **power-level**  integer | no description |
| **power-mode**  string | no description  Choices:   - `"dBm"` - `"percentage"` |
| **power-value**  integer | no description |
| **powersave-optimize**  list / elements=string | no description  Choices:   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection-mode**  string | no description  Choices:   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio-id**  integer | no description |
| **rts-threshold**  integer | no description |
| **sam-bssid**  string | no description |
| **sam-captive-portal**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sam-cwp-failure-string**  string | no description |
| **sam-cwp-match-string**  string | no description |
| **sam-cwp-password**  string | description |
| **sam-cwp-success-string**  string | no description |
| **sam-cwp-test-url**  string | no description |
| **sam-cwp-username**  string | no description |
| **sam-password**  string | no description |
| **sam-report-intv**  integer | no description |
| **sam-security-type**  string | no description  Choices:   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam-server**  string | no description |
| **sam-server-fqdn**  string | no description |
| **sam-server-ip**  string | no description |
| **sam-server-type**  string | no description  Choices:   - `"ip"` - `"fqdn"` |
| **sam-ssid**  string | no description |
| **sam-test**  string | no description  Choices:   - `"ping"` - `"iperf"` |
| **sam-username**  string | no description |
| **short-guard-interval**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **spectrum-analysis**  string | no description  Choices:   - `"disable"` - `"enable"` - `"scan-only"` |
| **transmit-optimize**  list / elements=string | no description  Choices:   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap-all**  string | no description  Choices:   - `"disable"` - `"enable"` - `"tunnel"` - `"bridge"` - `"manual"` |
| **vap1**  string | no description |
| **vap2**  string | no description |
| **vap3**  string | no description |
| **vap4**  string | no description |
| **vap5**  string | no description |
| **vap6**  string | no description |
| **vap7**  string | no description |
| **vap8**  string | no description |
| **vaps**  string | no description |
| **wids-profile**  string | no description |
| **zero-wait-dfs**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **radio-3**  dictionary | no description |
| **airtime-fairness**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **amsdu**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-addr**  string | no description |
| **ap-sniffer-bufsize**  integer | no description |
| **ap-sniffer-chan**  integer | no description |
| **ap-sniffer-ctl**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-data**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-beacon**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-other**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-probe**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **arrp-profile**  string | no description |
| **auto-power-high**  integer | no description |
| **auto-power-level**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auto-power-low**  integer | no description |
| **auto-power-target**  string | no description |
| **band**  string | no description  Choices:   - `"802.11b"` - `"802.11a"` - `"802.11g"` - `"802.11n"` - `"802.11ac"` - `"802.11n-5G"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n,g-only"` - `"802.11ac-only"` - `"802.11ac,n-only"` - `"802.11n-5G-only"` - `"802.11ax-5G-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` |
| **band-5g-type**  string | no description  Choices:   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth-admission-control**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **bandwidth-capacity**  integer | no description |
| **beacon-interval**  integer | no description |
| **bss-color**  integer | no description |
| **bss-color-mode**  string | no description  Choices:   - `"auto"` - `"static"` |
| **call-admission-control**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **call-capacity**  integer | no description |
| **channel**  string | no description |
| **channel-bonding**  string | no description  Choices:   - `"80MHz"` - `"40MHz"` - `"20MHz"` - `"160MHz"` |
| **channel-utilization**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **coexistence**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **darrp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **drma**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **drma-sensitivity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | no description |
| **frag-threshold**  integer | no description |
| **iperf-protocol**  string | no description  Choices:   - `"udp"` - `"tcp"` |
| **iperf-server-port**  integer | no description |
| **max-clients**  integer | no description |
| **max-distance**  integer | no description |
| **mode**  string | no description  Choices:   - `"disabled"` - `"ap"` - `"monitor"` - `"sniffer"` - `"sam"` |
| **power-level**  integer | no description |
| **power-mode**  string | no description  Choices:   - `"dBm"` - `"percentage"` |
| **power-value**  integer | no description |
| **powersave-optimize**  list / elements=string | no description  Choices:   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection-mode**  string | no description  Choices:   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio-id**  integer | no description |
| **rts-threshold**  integer | no description |
| **sam-bssid**  string | no description |
| **sam-captive-portal**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sam-cwp-failure-string**  string | no description |
| **sam-cwp-match-string**  string | no description |
| **sam-cwp-password**  string | description |
| **sam-cwp-success-string**  string | no description |
| **sam-cwp-test-url**  string | no description |
| **sam-cwp-username**  string | no description |
| **sam-password**  string | no description |
| **sam-report-intv**  integer | no description |
| **sam-security-type**  string | no description  Choices:   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam-server**  string | no description |
| **sam-server-fqdn**  string | no description |
| **sam-server-ip**  string | no description |
| **sam-server-type**  string | no description  Choices:   - `"ip"` - `"fqdn"` |
| **sam-ssid**  string | no description |
| **sam-test**  string | no description  Choices:   - `"ping"` - `"iperf"` |
| **sam-username**  string | no description |
| **short-guard-interval**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **spectrum-analysis**  string | no description  Choices:   - `"disable"` - `"enable"` - `"scan-only"` |
| **transmit-optimize**  list / elements=string | no description  Choices:   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap-all**  string | no description  Choices:   - `"disable"` - `"enable"` - `"tunnel"` - `"bridge"` - `"manual"` |
| **vap1**  string | no description |
| **vap2**  string | no description |
| **vap3**  string | no description |
| **vap4**  string | no description |
| **vap5**  string | no description |
| **vap6**  string | no description |
| **vap7**  string | no description |
| **vap8**  string | no description |
| **vaps**  string | no description |
| **wids-profile**  string | no description |
| **zero-wait-dfs**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **radio-4**  dictionary | no description |
| **airtime-fairness**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **amsdu**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-addr**  string | no description |
| **ap-sniffer-bufsize**  integer | no description |
| **ap-sniffer-chan**  integer | no description |
| **ap-sniffer-ctl**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-data**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-beacon**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-other**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-probe**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **arrp-profile**  string | no description |
| **auto-power-high**  integer | no description |
| **auto-power-level**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auto-power-low**  integer | no description |
| **auto-power-target**  string | no description |
| **band**  string | no description  Choices:   - `"802.11b"` - `"802.11a"` - `"802.11g"` - `"802.11n"` - `"802.11ac"` - `"802.11n-5G"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n,g-only"` - `"802.11ac-only"` - `"802.11ac,n-only"` - `"802.11n-5G-only"` - `"802.11ax-5G-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` |
| **band-5g-type**  string | no description  Choices:   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth-admission-control**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **bandwidth-capacity**  integer | no description |
| **beacon-interval**  integer | no description |
| **bss-color**  integer | no description |
| **bss-color-mode**  string | no description  Choices:   - `"auto"` - `"static"` |
| **call-admission-control**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **call-capacity**  integer | no description |
| **channel**  string | no description |
| **channel-bonding**  string | no description  Choices:   - `"80MHz"` - `"40MHz"` - `"20MHz"` - `"160MHz"` |
| **channel-utilization**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **coexistence**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **darrp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **drma**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **drma-sensitivity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | no description |
| **frag-threshold**  integer | no description |
| **iperf-protocol**  string | no description  Choices:   - `"udp"` - `"tcp"` |
| **iperf-server-port**  integer | no description |
| **max-clients**  integer | no description |
| **max-distance**  integer | no description |
| **mode**  string | no description  Choices:   - `"ap"` - `"monitor"` - `"sniffer"` - `"disabled"` - `"sam"` |
| **power-level**  integer | no description |
| **power-mode**  string | no description  Choices:   - `"dBm"` - `"percentage"` |
| **power-value**  integer | no description |
| **powersave-optimize**  list / elements=string | no description  Choices:   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection-mode**  string | no description  Choices:   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio-id**  integer | no description |
| **rts-threshold**  integer | no description |
| **sam-bssid**  string | no description |
| **sam-captive-portal**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sam-cwp-failure-string**  string | no description |
| **sam-cwp-match-string**  string | no description |
| **sam-cwp-password**  string | description |
| **sam-cwp-success-string**  string | no description |
| **sam-cwp-test-url**  string | no description |
| **sam-cwp-username**  string | no description |
| **sam-password**  string | no description |
| **sam-report-intv**  integer | no description |
| **sam-security-type**  string | no description  Choices:   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam-server**  string | no description |
| **sam-server-fqdn**  string | no description |
| **sam-server-ip**  string | no description |
| **sam-server-type**  string | no description  Choices:   - `"ip"` - `"fqdn"` |
| **sam-ssid**  string | no description |
| **sam-test**  string | no description  Choices:   - `"ping"` - `"iperf"` |
| **sam-username**  string | no description |
| **short-guard-interval**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **spectrum-analysis**  string | no description  Choices:   - `"disable"` - `"enable"` - `"scan-only"` |
| **transmit-optimize**  list / elements=string | no description  Choices:   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap-all**  string | no description  Choices:   - `"disable"` - `"enable"` - `"tunnel"` - `"bridge"` - `"manual"` |
| **vap1**  string | no description |
| **vap2**  string | no description |
| **vap3**  string | no description |
| **vap4**  string | no description |
| **vap5**  string | no description |
| **vap6**  string | no description |
| **vap7**  string | no description |
| **vap8**  string | no description |
| **vaps**  string | no description |
| **wids-profile**  string | no description |
| **zero-wait-dfs**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **snmp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **split-tunneling-acl**  list / elements=string | no description |
| **dest-ip**  string | no description |
| **id**  integer | no description |
| **split-tunneling-acl-local-ap-subnet**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **split-tunneling-acl-path**  string | no description  Choices:   - `"tunnel"` - `"local"` |
| **syslog-profile**  string | no description |
| **tun-mtu-downlink**  integer | no description |
| **tun-mtu-uplink**  integer | no description |
| **wan-port-auth**  string | no description  Choices:   - `"none"` - `"802.1x"` |
| **wan-port-auth-methods**  string | no description  Choices:   - `"all"` - `"EAP-FAST"` - `"EAP-TLS"` - `"EAP-PEAP"` |
| **wan-port-auth-password**  string | description |
| **wan-port-auth-usrname**  string | no description |
| **wan-port-mode**  string | no description  Choices:   - `"wan-lan"` - `"wan-only"` |

## [Notes](fmgr_wtpprofile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_wtpprofile_module.md#id4)

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
   - name: no description
     fmgr_wtpprofile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        wtpprofile:
           allowaccess:
             - https
             - ssh
             - snmp
             - http
             - telnet
           ap-country: <value in [AL, DZ, AR, ...]>
           ble-profile: <value of string>
           comment: <value of string>
           control-message-offload:
             - ebp-frame
             - aeroscout-tag
             - ap-list
             - sta-list
             - sta-cap-list
             - stats
             - aeroscout-mu
             - sta-health
             - spectral-analysis
           deny-mac-list:
             -
                 id: <value of integer>
                 mac: <value of string>
           dtls-in-kernel: <value in [disable, enable]>
           dtls-policy:
             - clear-text
             - dtls-enabled
             - ipsec-vpn
           energy-efficient-ethernet: <value in [disable, enable]>
           ext-info-enable: <value in [disable, enable]>
           handoff-roaming: <value in [disable, enable]>
           handoff-rssi: <value of integer>
           handoff-sta-thresh: <value of integer>
           ip-fragment-preventing:
             - tcp-mss-adjust
             - icmp-unreachable
           led-schedules: <value of string>
           led-state: <value in [disable, enable]>
           lldp: <value in [disable, enable]>
           login-passwd: <value of string>
           login-passwd-change: <value in [no, yes, default]>
           max-clients: <value of integer>
           name: <value of string>
           poe-mode: <value in [auto, 8023af, 8023at, ...]>
           split-tunneling-acl:
             -
                 dest-ip: <value of string>
                 id: <value of integer>
           split-tunneling-acl-local-ap-subnet: <value in [disable, enable]>
           split-tunneling-acl-path: <value in [tunnel, local]>
           tun-mtu-downlink: <value of integer>
           tun-mtu-uplink: <value of integer>
           wan-port-mode: <value in [wan-lan, wan-only]>
           snmp: <value in [disable, enable]>
           ap-handoff: <value in [disable, enable]>
           apcfg-profile: <value of string>
           frequency-handoff: <value in [disable, enable]>
           lan:
              port-esl-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
              port-esl-ssid: <value of string>
              port-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
              port-ssid: <value of string>
              port1-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
              port1-ssid: <value of string>
              port2-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
              port2-ssid: <value of string>
              port3-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
              port3-ssid: <value of string>
              port4-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
              port4-ssid: <value of string>
              port5-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
              port5-ssid: <value of string>
              port6-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
              port6-ssid: <value of string>
              port7-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
              port7-ssid: <value of string>
              port8-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
              port8-ssid: <value of string>
           lbs:
              aeroscout: <value in [disable, enable]>
              aeroscout-ap-mac: <value in [bssid, board-mac]>
              aeroscout-mmu-report: <value in [disable, enable]>
              aeroscout-mu: <value in [disable, enable]>
              aeroscout-mu-factor: <value of integer>
              aeroscout-mu-timeout: <value of integer>
              aeroscout-server-ip: <value of string>
              aeroscout-server-port: <value of integer>
              ekahau-blink-mode: <value in [disable, enable]>
              ekahau-tag: <value of string>
              erc-server-ip: <value of string>
              erc-server-port: <value of integer>
              fortipresence: <value in [disable, enable, enable2, ...]>
              fortipresence-ble: <value in [disable, enable]>
              fortipresence-frequency: <value of integer>
              fortipresence-port: <value of integer>
              fortipresence-project: <value of string>
              fortipresence-rogue: <value in [disable, enable]>
              fortipresence-secret: <value of string>
              fortipresence-server: <value of string>
              fortipresence-unassoc: <value in [disable, enable]>
              station-locate: <value in [disable, enable]>
              fortipresence-server-addr-type: <value in [fqdn, ipv4]>
              fortipresence-server-fqdn: <value of string>
           platform:
              ddscan: <value in [disable, enable]>
              mode: <value in [dual-5G, single-5G]>
              type: <value in [30B-50B, 60B, 80CM-81CM, ...]>
              _local_platform_str: <value of string>
           radio-1:
              airtime-fairness: <value in [disable, enable]>
              amsdu: <value in [disable, enable]>
              ap-sniffer-addr: <value of string>
              ap-sniffer-bufsize: <value of integer>
              ap-sniffer-chan: <value of integer>
              ap-sniffer-ctl: <value in [disable, enable]>
              ap-sniffer-data: <value in [disable, enable]>
              ap-sniffer-mgmt-beacon: <value in [disable, enable]>
              ap-sniffer-mgmt-other: <value in [disable, enable]>
              ap-sniffer-mgmt-probe: <value in [disable, enable]>
              auto-power-high: <value of integer>
              auto-power-level: <value in [disable, enable]>
              auto-power-low: <value of integer>
              auto-power-target: <value of string>
              band: <value in [802.11b, 802.11a, 802.11g, ...]>
              band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
              bandwidth-admission-control: <value in [disable, enable]>
              bandwidth-capacity: <value of integer>
              beacon-interval: <value of integer>
              bss-color: <value of integer>
              call-admission-control: <value in [disable, enable]>
              call-capacity: <value of integer>
              channel: <value of string>
              channel-bonding: <value in [disable, enable, 80MHz, ...]>
              channel-utilization: <value in [disable, enable]>
              coexistence: <value in [disable, enable]>
              darrp: <value in [disable, enable]>
              drma: <value in [disable, enable]>
              drma-sensitivity: <value in [low, medium, high]>
              dtim: <value of integer>
              frag-threshold: <value of integer>
              max-clients: <value of integer>
              max-distance: <value of integer>
              mode: <value in [disabled, ap, monitor, ...]>
              power-level: <value of integer>
              powersave-optimize:
                - tim
                - ac-vo
                - no-obss-scan
                - no-11b-rate
                - client-rate-follow
              protection-mode: <value in [rtscts, ctsonly, disable]>
              radio-id: <value of integer>
              rts-threshold: <value of integer>
              short-guard-interval: <value in [disable, enable]>
              spectrum-analysis: <value in [disable, enable, scan-only]>
              transmit-optimize:
                - disable
                - power-save
                - aggr-limit
                - retry-limit
                - send-bar
              vap-all: <value in [disable, enable, tunnel, ...]>
              vap1: <value of string>
              vap2: <value of string>
              vap3: <value of string>
              vap4: <value of string>
              vap5: <value of string>
              vap6: <value of string>
              vap7: <value of string>
              vap8: <value of string>
              vaps: <value of string>
              wids-profile: <value of string>
              zero-wait-dfs: <value in [disable, enable]>
              iperf-protocol: <value in [udp, tcp]>
              iperf-server-port: <value of integer>
              power-mode: <value in [dBm, percentage]>
              power-value: <value of integer>
              sam-bssid: <value of string>
              sam-captive-portal: <value in [disable, enable]>
              sam-password: <value of string>
              sam-report-intv: <value of integer>
              sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
              sam-server: <value of string>
              sam-ssid: <value of string>
              sam-test: <value in [ping, iperf]>
              sam-username: <value of string>
              arrp-profile: <value of string>
              bss-color-mode: <value in [auto, static]>
              sam-cwp-failure-string: <value of string>
              sam-cwp-match-string: <value of string>
              sam-cwp-password: <value of string>
              sam-cwp-success-string: <value of string>
              sam-cwp-test-url: <value of string>
              sam-cwp-username: <value of string>
              sam-server-fqdn: <value of string>
              sam-server-ip: <value of string>
              sam-server-type: <value in [ip, fqdn]>
           radio-2:
              airtime-fairness: <value in [disable, enable]>
              amsdu: <value in [disable, enable]>
              ap-sniffer-addr: <value of string>
              ap-sniffer-bufsize: <value of integer>
              ap-sniffer-chan: <value of integer>
              ap-sniffer-ctl: <value in [disable, enable]>
              ap-sniffer-data: <value in [disable, enable]>
              ap-sniffer-mgmt-beacon: <value in [disable, enable]>
              ap-sniffer-mgmt-other: <value in [disable, enable]>
              ap-sniffer-mgmt-probe: <value in [disable, enable]>
              auto-power-high: <value of integer>
              auto-power-level: <value in [disable, enable]>
              auto-power-low: <value of integer>
              auto-power-target: <value of string>
              band: <value in [802.11b, 802.11a, 802.11g, ...]>
              band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
              bandwidth-admission-control: <value in [disable, enable]>
              bandwidth-capacity: <value of integer>
              beacon-interval: <value of integer>
              bss-color: <value of integer>
              call-admission-control: <value in [disable, enable]>
              call-capacity: <value of integer>
              channel: <value of string>
              channel-bonding: <value in [disable, enable, 80MHz, ...]>
              channel-utilization: <value in [disable, enable]>
              coexistence: <value in [disable, enable]>
              darrp: <value in [disable, enable]>
              drma: <value in [disable, enable]>
              drma-sensitivity: <value in [low, medium, high]>
              dtim: <value of integer>
              frag-threshold: <value of integer>
              max-clients: <value of integer>
              max-distance: <value of integer>
              mode: <value in [disabled, ap, monitor, ...]>
              power-level: <value of integer>
              powersave-optimize:
                - tim
                - ac-vo
                - no-obss-scan
                - no-11b-rate
                - client-rate-follow
              protection-mode: <value in [rtscts, ctsonly, disable]>
              radio-id: <value of integer>
              rts-threshold: <value of integer>
              short-guard-interval: <value in [disable, enable]>
              spectrum-analysis: <value in [disable, enable, scan-only]>
              transmit-optimize:
                - disable
                - power-save
                - aggr-limit
                - retry-limit
                - send-bar
              vap-all: <value in [disable, enable, tunnel, ...]>
              vap1: <value of string>
              vap2: <value of string>
              vap3: <value of string>
              vap4: <value of string>
              vap5: <value of string>
              vap6: <value of string>
              vap7: <value of string>
              vap8: <value of string>
              vaps: <value of string>
              wids-profile: <value of string>
              zero-wait-dfs: <value in [disable, enable]>
              iperf-protocol: <value in [udp, tcp]>
              iperf-server-port: <value of integer>
              power-mode: <value in [dBm, percentage]>
              power-value: <value of integer>
              sam-bssid: <value of string>
              sam-captive-portal: <value in [disable, enable]>
              sam-password: <value of string>
              sam-report-intv: <value of integer>
              sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
              sam-server: <value of string>
              sam-ssid: <value of string>
              sam-test: <value in [ping, iperf]>
              sam-username: <value of string>
              arrp-profile: <value of string>
              bss-color-mode: <value in [auto, static]>
              sam-cwp-failure-string: <value of string>
              sam-cwp-match-string: <value of string>
              sam-cwp-password: <value of string>
              sam-cwp-success-string: <value of string>
              sam-cwp-test-url: <value of string>
              sam-cwp-username: <value of string>
              sam-server-fqdn: <value of string>
              sam-server-ip: <value of string>
              sam-server-type: <value in [ip, fqdn]>
           radio-3:
              airtime-fairness: <value in [disable, enable]>
              amsdu: <value in [disable, enable]>
              ap-sniffer-addr: <value of string>
              ap-sniffer-bufsize: <value of integer>
              ap-sniffer-chan: <value of integer>
              ap-sniffer-ctl: <value in [disable, enable]>
              ap-sniffer-data: <value in [disable, enable]>
              ap-sniffer-mgmt-beacon: <value in [disable, enable]>
              ap-sniffer-mgmt-other: <value in [disable, enable]>
              ap-sniffer-mgmt-probe: <value in [disable, enable]>
              auto-power-high: <value of integer>
              auto-power-level: <value in [disable, enable]>
              auto-power-low: <value of integer>
              auto-power-target: <value of string>
              band: <value in [802.11b, 802.11a, 802.11g, ...]>
              band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
              bandwidth-admission-control: <value in [disable, enable]>
              bandwidth-capacity: <value of integer>
              beacon-interval: <value of integer>
              bss-color: <value of integer>
              call-admission-control: <value in [disable, enable]>
              call-capacity: <value of integer>
              channel: <value of string>
              channel-bonding: <value in [80MHz, 40MHz, 20MHz, ...]>
              channel-utilization: <value in [disable, enable]>
              coexistence: <value in [disable, enable]>
              darrp: <value in [disable, enable]>
              drma: <value in [disable, enable]>
              drma-sensitivity: <value in [low, medium, high]>
              dtim: <value of integer>
              frag-threshold: <value of integer>
              max-clients: <value of integer>
              max-distance: <value of integer>
              mode: <value in [disabled, ap, monitor, ...]>
              power-level: <value of integer>
              powersave-optimize:
                - tim
                - ac-vo
                - no-obss-scan
                - no-11b-rate
                - client-rate-follow
              protection-mode: <value in [rtscts, ctsonly, disable]>
              radio-id: <value of integer>
              rts-threshold: <value of integer>
              short-guard-interval: <value in [disable, enable]>
              spectrum-analysis: <value in [disable, enable, scan-only]>
              transmit-optimize:
                - disable
                - power-save
                - aggr-limit
                - retry-limit
                - send-bar
              vap-all: <value in [disable, enable, tunnel, ...]>
              vap1: <value of string>
              vap2: <value of string>
              vap3: <value of string>
              vap4: <value of string>
              vap5: <value of string>
              vap6: <value of string>
              vap7: <value of string>
              vap8: <value of string>
              vaps: <value of string>
              wids-profile: <value of string>
              zero-wait-dfs: <value in [disable, enable]>
              iperf-protocol: <value in [udp, tcp]>
              iperf-server-port: <value of integer>
              power-mode: <value in [dBm, percentage]>
              power-value: <value of integer>
              sam-bssid: <value of string>
              sam-captive-portal: <value in [disable, enable]>
              sam-password: <value of string>
              sam-report-intv: <value of integer>
              sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
              sam-server: <value of string>
              sam-ssid: <value of string>
              sam-test: <value in [ping, iperf]>
              sam-username: <value of string>
              arrp-profile: <value of string>
              bss-color-mode: <value in [auto, static]>
              sam-cwp-failure-string: <value of string>
              sam-cwp-match-string: <value of string>
              sam-cwp-password: <value of string>
              sam-cwp-success-string: <value of string>
              sam-cwp-test-url: <value of string>
              sam-cwp-username: <value of string>
              sam-server-fqdn: <value of string>
              sam-server-ip: <value of string>
              sam-server-type: <value in [ip, fqdn]>
           radio-4:
              airtime-fairness: <value in [disable, enable]>
              amsdu: <value in [disable, enable]>
              ap-sniffer-addr: <value of string>
              ap-sniffer-bufsize: <value of integer>
              ap-sniffer-chan: <value of integer>
              ap-sniffer-ctl: <value in [disable, enable]>
              ap-sniffer-data: <value in [disable, enable]>
              ap-sniffer-mgmt-beacon: <value in [disable, enable]>
              ap-sniffer-mgmt-other: <value in [disable, enable]>
              ap-sniffer-mgmt-probe: <value in [disable, enable]>
              auto-power-high: <value of integer>
              auto-power-level: <value in [disable, enable]>
              auto-power-low: <value of integer>
              auto-power-target: <value of string>
              band: <value in [802.11b, 802.11a, 802.11g, ...]>
              band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
              bandwidth-admission-control: <value in [disable, enable]>
              bandwidth-capacity: <value of integer>
              beacon-interval: <value of integer>
              bss-color: <value of integer>
              call-admission-control: <value in [disable, enable]>
              call-capacity: <value of integer>
              channel: <value of string>
              channel-bonding: <value in [80MHz, 40MHz, 20MHz, ...]>
              channel-utilization: <value in [disable, enable]>
              coexistence: <value in [disable, enable]>
              darrp: <value in [disable, enable]>
              drma: <value in [disable, enable]>
              drma-sensitivity: <value in [low, medium, high]>
              dtim: <value of integer>
              frag-threshold: <value of integer>
              max-clients: <value of integer>
              max-distance: <value of integer>
              mode: <value in [ap, monitor, sniffer, ...]>
              power-level: <value of integer>
              powersave-optimize:
                - tim
                - ac-vo
                - no-obss-scan
                - no-11b-rate
                - client-rate-follow
              protection-mode: <value in [rtscts, ctsonly, disable]>
              radio-id: <value of integer>
              rts-threshold: <value of integer>
              short-guard-interval: <value in [disable, enable]>
              spectrum-analysis: <value in [disable, enable, scan-only]>
              transmit-optimize:
                - disable
                - power-save
                - aggr-limit
                - retry-limit
                - send-bar
              vap-all: <value in [disable, enable, tunnel, ...]>
              vap1: <value of string>
              vap2: <value of string>
              vap3: <value of string>
              vap4: <value of string>
              vap5: <value of string>
              vap6: <value of string>
              vap7: <value of string>
              vap8: <value of string>
              vaps: <value of string>
              wids-profile: <value of string>
              zero-wait-dfs: <value in [disable, enable]>
              iperf-protocol: <value in [udp, tcp]>
              iperf-server-port: <value of integer>
              power-mode: <value in [dBm, percentage]>
              power-value: <value of integer>
              sam-bssid: <value of string>
              sam-captive-portal: <value in [disable, enable]>
              sam-password: <value of string>
              sam-report-intv: <value of integer>
              sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
              sam-server: <value of string>
              sam-ssid: <value of string>
              sam-test: <value in [ping, iperf]>
              sam-username: <value of string>
              arrp-profile: <value of string>
              bss-color-mode: <value in [auto, static]>
              sam-cwp-failure-string: <value of string>
              sam-cwp-match-string: <value of string>
              sam-cwp-password: <value of string>
              sam-cwp-success-string: <value of string>
              sam-cwp-test-url: <value of string>
              sam-cwp-username: <value of string>
              sam-server-fqdn: <value of string>
              sam-server-ip: <value of string>
              sam-server-type: <value in [ip, fqdn]>
           console-login: <value in [disable, enable]>
           esl-ses-dongle:
              apc-addr-type: <value in [fqdn, ip]>
              apc-fqdn: <value of string>
              apc-ip: <value of string>
              apc-port: <value of integer>
              coex-level: <value in [none]>
              compliance-level: <value in [compliance-level-2]>
              esl-channel: <value in [0, 1, 2, ...]>
              output-power: <value in [a, b, c, ...]>
              scd-enable: <value in [disable, enable]>
              tls-cert-verification: <value in [disable, enable]>
              tls-fqdn-verification: <value in [disable, enable]>
           indoor-outdoor-deployment: <value in [platform-determined, outdoor, indoor]>
           syslog-profile: <value of string>
           wan-port-auth: <value in [none, 802.1x]>
           wan-port-auth-methods: <value in [all, EAP-FAST, EAP-TLS, ...]>
           wan-port-auth-password: <value of string>
           wan-port-auth-usrname: <value of string>
```

## [Return Values](fmgr_wtpprofile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **request_url**  string | The full url requested  Returned: always  Sample: `"/sys/login/user"` |
| **response_code**  integer | The status of api request  Returned: always  Sample: `0` |
| **response_message**  string | The descriptive message of the api response  Returned: always  Sample: `"OK."` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
[Homepage](https://fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/tree/galaxy/2.1.7)
