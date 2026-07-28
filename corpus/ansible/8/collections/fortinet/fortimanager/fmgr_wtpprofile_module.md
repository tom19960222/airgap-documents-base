---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_wtpprofile module – Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_wtpprofile_module.html
fetched_at: 2026-07-28T02:23:05+00:00
---
# fortinet.fortimanager.fmgr_wtpprofile module – Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_wtpprofile`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |
| **wtpprofile**  dictionary | the top level parameters set |
| **_is_factory_setting**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"ext"` |
| **allowaccess**  list / elements=string | Control management access to the managed WTP, FortiAP, or AP.  **Choices:**   - `"https"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` |
| **ap-country**  string | Country in which this WTP, FortiAP or AP will operate  **Choices:**   - `"AL"` - `"DZ"` - `"AR"` - `"AM"` - `"AU"` - `"AT"` - `"AZ"` - `"BH"` - `"BD"` - `"BY"` - `"BE"` - `"BZ"` - `"BO"` - `"BA"` - `"BR"` - `"BN"` - `"BG"` - `"CA"` - `"CL"` - `"CN"` - `"CO"` - `"CR"` - `"HR"` - `"CY"` - `"CZ"` - `"DK"` - `"DO"` - `"EC"` - `"EG"` - `"SV"` - `"EE"` - `"FI"` - `"FR"` - `"GE"` - `"DE"` - `"GR"` - `"GT"` - `"HN"` - `"HK"` - `"HU"` - `"IS"` - `"IN"` - `"ID"` - `"IR"` - `"IE"` - `"IL"` - `"IT"` - `"JM"` - `"JP"` - `"JO"` - `"KZ"` - `"KE"` - `"KP"` - `"KR"` - `"KW"` - `"LV"` - `"LB"` - `"LI"` - `"LT"` - `"LU"` - `"MO"` - `"MK"` - `"MY"` - `"MT"` - `"MX"` - `"MC"` - `"MA"` - `"NP"` - `"NL"` - `"AN"` - `"NZ"` - `"NO"` - `"OM"` - `"PK"` - `"PA"` - `"PG"` - `"PE"` - `"PH"` - `"PL"` - `"PT"` - `"PR"` - `"QA"` - `"RO"` - `"RU"` - `"SA"` - `"SG"` - `"SK"` - `"SI"` - `"ZA"` - `"ES"` - `"LK"` - `"SE"` - `"CH"` - `"SY"` - `"TW"` - `"TH"` - `"TT"` - `"TN"` - `"TR"` - `"AE"` - `"UA"` - `"GB"` - `"US"` - `"PS"` - `"UY"` - `"UZ"` - `"VE"` - `"VN"` - `"YE"` - `"ZW"` - `"NA"` - `"KH"` - `"TZ"` - `"SD"` - `"AO"` - `"RW"` - `"MZ"` - `"RS"` - `"ME"` - `"BB"` - `"GD"` - `"GL"` - `"GU"` - `"PY"` - `"HT"` - `"AW"` - `"MM"` - `"ZB"` - `"CF"` - `"BS"` - `"VC"` - `"MV"` - `"SN"` - `"CI"` - `"GH"` - `"MW"` - `"UG"` - `"BF"` - `"KY"` - `"TC"` - `"TM"` - `"VU"` - `"FM"` - `"GY"` - `"KN"` - `"LC"` - `"CX"` - `"AF"` - `"CM"` - `"ML"` - `"BJ"` - `"MG"` - `"TD"` - `"BW"` - `"LY"` - `"LS"` - `"MU"` - `"SL"` - `"NE"` - `"TG"` - `"RE"` - `"MD"` - `"BM"` - `"VI"` - `"PM"` - `"MF"` - `"IM"` - `"FO"` - `"GI"` - `"LA"` - `"WF"` - `"MH"` - `"BT"` - `"PF"` - `"NI"` - `"GF"` - `"AS"` - `"MP"` - `"PW"` - `"GP"` - `"ET"` - `"SR"` - `"DM"` - `"MQ"` - `"YT"` - `"BL"` - `"ZM"` - `"CG"` - `"CD"` - `"MR"` - `"IQ"` - `"FJ"` - `"--"` - `"MN"` - `"NG"` - `"GA"` - `"GM"` - `"SO"` - `"SZ"` - `"LR"` - `"DJ"` |
| **ap-handoff**  string | Enable/disable AP handoff of clients to other APs  **Choices:**   - `"disable"` - `"enable"` |
| **apcfg-profile**  string | AP local configuration profile name. |
| **ble-profile**  string | Bluetooth Low Energy profile name. |
| **comment**  string | Comment. |
| **console-login**  string | Enable/disable FortiAP console login access  **Choices:**   - `"disable"` - `"enable"` |
| **control-message-offload**  list / elements=string | Enable/disable CAPWAP control message data channel offload.  **Choices:**   - `"ebp-frame"` - `"aeroscout-tag"` - `"ap-list"` - `"sta-list"` - `"sta-cap-list"` - `"stats"` - `"aeroscout-mu"` - `"sta-health"` - `"spectral-analysis"` |
| **deny-mac-list**  list / elements=dictionary | Deny-Mac-List. |
| **id**  integer | ID. |
| **mac**  string | A WiFi device with this MAC address is denied access to this WTP, FortiAP or AP. |
| **dtls-in-kernel**  string | Enable/disable data channel DTLS in kernel.  **Choices:**   - `"disable"` - `"enable"` |
| **dtls-policy**  list / elements=string | WTP data channel DTLS policy  **Choices:**   - `"clear-text"` - `"dtls-enabled"` - `"ipsec-vpn"` - `"ipsec-sn-vpn"` |
| **energy-efficient-ethernet**  string | Enable/disable use of energy efficient Ethernet on WTP.  **Choices:**   - `"disable"` - `"enable"` |
| **esl-ses-dongle**  dictionary | no description |
| **apc-addr-type**  string | ESL SES-imagotag APC address type  **Choices:**   - `"fqdn"` - `"ip"` |
| **apc-fqdn**  string | FQDN of ESL SES-imagotag Access Point Controller |
| **apc-ip**  string | IP address of ESL SES-imagotag Access Point Controller |
| **apc-port**  integer | Port of ESL SES-imagotag Access Point Controller |
| **coex-level**  string | ESL SES-imagotag dongle coexistence level  **Choices:**   - `"none"` |
| **compliance-level**  string | Compliance levels for the ESL solution integration  **Choices:**   - `"compliance-level-2"` |
| **esl-channel**  string | ESL SES-imagotag dongle channel  **Choices:**   - `"0"` - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` - `"6"` - `"7"` - `"8"` - `"9"` - `"10"` - `"127"` - `"-1"` |
| **output-power**  string | ESL SES-imagotag dongle output power  **Choices:**   - `"a"` - `"b"` - `"c"` - `"d"` - `"e"` - `"f"` - `"g"` - `"h"` |
| **scd-enable**  string | Enable/disable ESL SES-imagotag Serial Communication Daemon  **Choices:**   - `"disable"` - `"enable"` |
| **tls-cert-verification**  string | Enable/disable TLS certificate verification  **Choices:**   - `"disable"` - `"enable"` |
| **tls-fqdn-verification**  string | Enable/disable TLS certificate verification  **Choices:**   - `"disable"` - `"enable"` |
| **ext-info-enable**  string | Enable/disable station/VAP/radio extension information.  **Choices:**   - `"disable"` - `"enable"` |
| **frequency-handoff**  string | Enable/disable frequency handoff of clients to other channels  **Choices:**   - `"disable"` - `"enable"` |
| **handoff-roaming**  string | Enable/disable client load balancing during roaming to avoid roaming delay  **Choices:**   - `"disable"` - `"enable"` |
| **handoff-rssi**  integer | Minimum received signal strength indicator |
| **handoff-sta-thresh**  integer | Threshold value for AP handoff. |
| **indoor-outdoor-deployment**  string | Set to allow indoor/outdoor-only channels under regulatory rules  **Choices:**   - `"platform-determined"` - `"outdoor"` - `"indoor"` |
| **ip-fragment-preventing**  list / elements=string | Method  **Choices:**   - `"tcp-mss-adjust"` - `"icmp-unreachable"` |
| **lan**  dictionary | no description |
| **port-esl-mode**  string | ESL port mode.  **Choices:**   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port-esl-ssid**  string | Bridge ESL port to SSID. |
| **port-mode**  string | LAN port mode.  **Choices:**   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port-ssid**  string | Bridge LAN port to SSID. |
| **port1-mode**  string | LAN port 1 mode.  **Choices:**   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port1-ssid**  string | Bridge LAN port 1 to SSID. |
| **port2-mode**  string | LAN port 2 mode.  **Choices:**   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port2-ssid**  string | Bridge LAN port 2 to SSID. |
| **port3-mode**  string | LAN port 3 mode.  **Choices:**   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port3-ssid**  string | Bridge LAN port 3 to SSID. |
| **port4-mode**  string | LAN port 4 mode.  **Choices:**   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port4-ssid**  string | Bridge LAN port 4 to SSID. |
| **port5-mode**  string | LAN port 5 mode.  **Choices:**   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port5-ssid**  string | Bridge LAN port 5 to SSID. |
| **port6-mode**  string | LAN port 6 mode.  **Choices:**   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port6-ssid**  string | Bridge LAN port 6 to SSID. |
| **port7-mode**  string | LAN port 7 mode.  **Choices:**   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port7-ssid**  string | Bridge LAN port 7 to SSID. |
| **port8-mode**  string | LAN port 8 mode.  **Choices:**   - `"offline"` - `"bridge-to-wan"` - `"bridge-to-ssid"` - `"nat-to-wan"` |
| **port8-ssid**  string | Bridge LAN port 8 to SSID. |
| **lbs**  dictionary | no description |
| **aeroscout**  string | Enable/disable AeroScout Real Time Location Service  **Choices:**   - `"disable"` - `"enable"` |
| **aeroscout-ap-mac**  string | Use BSSID or board MAC address as AP MAC address in AeroScout AP messages  **Choices:**   - `"bssid"` - `"board-mac"` |
| **aeroscout-mmu-report**  string | Enable/disable compounded AeroScout tag and MU report  **Choices:**   - `"disable"` - `"enable"` |
| **aeroscout-mu**  string | Enable/disable AeroScout Mobile Unit  **Choices:**   - `"disable"` - `"enable"` |
| **aeroscout-mu-factor**  integer | AeroScout MU mode dilution factor |
| **aeroscout-mu-timeout**  integer | AeroScout MU mode timeout |
| **aeroscout-server-ip**  string | IP address of AeroScout server. |
| **aeroscout-server-port**  integer | AeroScout server UDP listening port. |
| **ekahau-blink-mode**  string | Enable/disable Ekahau blink mode  **Choices:**   - `"disable"` - `"enable"` |
| **ekahau-tag**  string | WiFi frame MAC address or WiFi Tag. |
| **erc-server-ip**  string | IP address of Ekahau RTLS Controller |
| **erc-server-port**  integer | Ekahau RTLS Controller |
| **fortipresence**  string | Enable/disable FortiPresence to monitor the location and activity of WiFi clients even if they dont connect to this WiF…  **Choices:**   - `"disable"` - `"enable"` - `"enable2"` - `"foreign"` - `"both"` |
| **fortipresence-ble**  string | Enable/disable FortiPresence finding and reporting BLE devices.  **Choices:**   - `"disable"` - `"enable"` |
| **fortipresence-frequency**  integer | FortiPresence report transmit frequency |
| **fortipresence-port**  integer | FortiPresence server UDP listening port |
| **fortipresence-project**  string | FortiPresence project name |
| **fortipresence-rogue**  string | Enable/disable FortiPresence finding and reporting rogue APs.  **Choices:**   - `"disable"` - `"enable"` |
| **fortipresence-secret**  any | (list) FortiPresence secret password |
| **fortipresence-server**  string | FortiPresence server IP address. |
| **fortipresence-server-addr-type**  string | FortiPresence server address type  **Choices:**   - `"fqdn"` - `"ipv4"` |
| **fortipresence-server-fqdn**  string | FQDN of FortiPresence server. |
| **fortipresence-unassoc**  string | Enable/disable FortiPresence finding and reporting unassociated stations.  **Choices:**   - `"disable"` - `"enable"` |
| **polestar**  string | Enable/disable PoleStar BLE NAO Track Real Time Location Service  **Choices:**   - `"disable"` - `"enable"` |
| **polestar-accumulation-interval**  integer | Time that measurements should be accumulated in seconds |
| **polestar-asset-addrgrp-list**  string | Tags and asset addrgrp list to be reported. |
| **polestar-asset-uuid-list1**  string | Tags and asset UUID list 1 to be reported |
| **polestar-asset-uuid-list2**  string | Tags and asset UUID list 2 to be reported |
| **polestar-asset-uuid-list3**  string | Tags and asset UUID list 3 to be reported |
| **polestar-asset-uuid-list4**  string | Tags and asset UUID list 4 to be reported |
| **polestar-protocol**  string | Select the protocol to report Measurements, Advertising Data, or Location Data to NAO Cloud.  **Choices:**   - `"WSS"` |
| **polestar-reporting-interval**  integer | Time between reporting accumulated measurements in seconds |
| **polestar-server-fqdn**  string | FQDN of PoleStar Nao Track Server |
| **polestar-server-path**  string | Path of PoleStar Nao Track Server |
| **polestar-server-port**  integer | Port of PoleStar Nao Track Server |
| **polestar-server-token**  string | Access Token of PoleStar Nao Track Server. |
| **station-locate**  string | Enable/disable client station locating services for all clients, whether associated or not  **Choices:**   - `"disable"` - `"enable"` |
| **led-schedules**  any | (list or str) Recurring firewall schedules for illuminating LEDs on the FortiAP. |
| **led-state**  string | Enable/disable use of LEDs on WTP  **Choices:**   - `"disable"` - `"enable"` |
| **lldp**  string | Enable/disable Link Layer Discovery Protocol  **Choices:**   - `"disable"` - `"enable"` |
| **login-passwd**  any | (list) Set the managed WTP, FortiAP, or APs administrator password. |
| **login-passwd-change**  string | Change or reset the administrator password of a managed WTP, FortiAP or AP  **Choices:**   - `"no"` - `"yes"` - `"default"` |
| **max-clients**  integer | Maximum number of stations |
| **name**  string / required | WTP |
| **platform**  dictionary | no description |
| **_local_platform_str**  string | _Local_Platform_Str. |
| **ddscan**  string | Enable/disable use of one radio for dedicated dual-band scanning to detect RF characterization and wireless threat mana…  **Choices:**   - `"disable"` - `"enable"` |
| **mode**  string | Configure operation mode of 5G radios  **Choices:**   - `"dual-5G"` - `"single-5G"` |
| **type**  string | WTP, FortiAP or AP platform type.  **Choices:**   - `"30B-50B"` - `"60B"` - `"80CM-81CM"` - `"220A"` - `"220B"` - `"210B"` - `"60C"` - `"222B"` - `"112B"` - `"320B"` - `"11C"` - `"14C"` - `"223B"` - `"28C"` - `"320C"` - `"221C"` - `"25D"` - `"222C"` - `"224D"` - `"214B"` - `"21D"` - `"24D"` - `"112D"` - `"223C"` - `"321C"` - `"C220C"` - `"C225C"` - `"S321C"` - `"S323C"` - `"FWF"` - `"S311C"` - `"S313C"` - `"AP-11N"` - `"S322C"` - `"S321CR"` - `"S322CR"` - `"S323CR"` - `"S421E"` - `"S422E"` - `"S423E"` - `"421E"` - `"423E"` - `"C221E"` - `"C226E"` - `"C23JD"` - `"C24JE"` - `"C21D"` - `"U421E"` - `"U423E"` - `"221E"` - `"222E"` - `"223E"` - `"S221E"` - `"S223E"` - `"U221EV"` - `"U223EV"` - `"U321EV"` - `"U323EV"` - `"224E"` - `"U422EV"` - `"U24JEV"` - `"321E"` - `"U431F"` - `"U433F"` - `"231E"` - `"431F"` - `"433F"` - `"231F"` - `"432F"` - `"234F"` - `"23JF"` - `"U231F"` - `"831F"` - `"U234F"` - `"U432F"` - `"431FL"` - `"432FR"` - `"433FL"` - `"231FL"` - `"231G"` - `"233G"` - `"431G"` - `"433G"` - `"U231G"` - `"U441G"` - `"234G"` |
| **poe-mode**  string | Set the WTP, FortiAP, or APs PoE mode.  **Choices:**   - `"auto"` - `"8023af"` - `"8023at"` - `"power-adapter"` - `"full"` - `"high"` - `"low"` |
| **radio-1**  dictionary | no description |
| **80211d**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **airtime-fairness**  string | Enable/disable airtime fairness  **Choices:**   - `"disable"` - `"enable"` |
| **amsdu**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **ap-handoff**  string | Enable/disable AP handoff of clients to other APs  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-addr**  string | MAC address to monitor. |
| **ap-sniffer-bufsize**  integer | Sniffer buffer size |
| **ap-sniffer-chan**  integer | Channel on which to operate the sniffer |
| **ap-sniffer-ctl**  string | Enable/disable sniffer on WiFi control frame  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-data**  string | Enable/disable sniffer on WiFi data frame  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-beacon**  string | Enable/disable sniffer on WiFi management Beacon frames  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-other**  string | Enable/disable sniffer on WiFi management other frames  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-probe**  string | Enable/disable sniffer on WiFi management probe frames  **Choices:**   - `"disable"` - `"enable"` |
| **arrp-profile**  string | Distributed Automatic Radio Resource Provisioning |
| **auto-power-high**  integer | The upper bound of automatic transmit power adjustment in dBm |
| **auto-power-level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference  **Choices:**   - `"disable"` - `"enable"` |
| **auto-power-low**  integer | The lower bound of automatic transmit power adjustment in dBm |
| **auto-power-target**  string | The target of automatic transmit power adjustment in dBm. |
| **band**  string | WiFi band that Radio 1 operates on.  **Choices:**   - `"802.11b"` - `"802.11a"` - `"802.11g"` - `"802.11n"` - `"802.11ac"` - `"802.11n-5G"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n,g-only"` - `"802.11ac-only"` - `"802.11ac,n-only"` - `"802.11n-5G-only"` - `"802.11ax-5G-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ax-6G"` |
| **band-5g-type**  string | WiFi 5G band type.  **Choices:**   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth-admission-control**  string | Enable/disable WiFi multimedia  **Choices:**   - `"disable"` - `"enable"` |
| **bandwidth-capacity**  integer | Maximum bandwidth capacity allowed |
| **beacon-interval**  integer | Beacon interval. |
| **bss-color**  integer | BSS color value for this 11ax radio |
| **bss-color-mode**  string | BSS color mode for this 11ax radio  **Choices:**   - `"auto"` - `"static"` |
| **call-admission-control**  string | Enable/disable WiFi multimedia  **Choices:**   - `"disable"` - `"enable"` |
| **call-capacity**  integer | Maximum number of Voice over WLAN |
| **channel**  any | (list) Selected list of wireless radio channels. |
| **channel-bonding**  string | Channel bandwidth  **Choices:**   - `"disable"` - `"enable"` - `"80MHz"` - `"40MHz"` - `"20MHz"` - `"160MHz"` |
| **channel-utilization**  string | Enable/disable measuring channel utilization.  **Choices:**   - `"disable"` - `"enable"` |
| **coexistence**  string | Enable/disable allowing both HT20 and HT40 on the same radio  **Choices:**   - `"disable"` - `"enable"` |
| **darrp**  string | Enable/disable Distributed Automatic Radio Resource Provisioning  **Choices:**   - `"disable"` - `"enable"` |
| **drma**  string | Enable/disable dynamic radio mode assignment  **Choices:**   - `"disable"` - `"enable"` |
| **drma-sensitivity**  string | Network Coverage Factor  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | Delivery Traffic Indication Map |
| **frag-threshold**  integer | Maximum packet size that can be sent without fragmentation |
| **frequency-handoff**  string | Enable/disable frequency handoff of clients to other channels  **Choices:**   - `"disable"` - `"enable"` |
| **iperf-protocol**  string | Iperf test protocol  **Choices:**   - `"udp"` - `"tcp"` |
| **iperf-server-port**  integer | Iperf service port number. |
| **max-clients**  integer | Maximum number of stations |
| **max-distance**  integer | Maximum expected distance between the AP and clients |
| **mimo-mode**  string | Configure radio MIMO mode  **Choices:**   - `"default"` - `"1x1"` - `"2x2"` - `"3x3"` - `"4x4"` - `"8x8"` |
| **mode**  string | Mode of radio 1.  **Choices:**   - `"disabled"` - `"ap"` - `"monitor"` - `"sniffer"` - `"sam"` |
| **optional-antenna**  string | Optional antenna used on FAP  **Choices:**   - `"none"` - `"FANT-04ABGN-0606-O-N"` - `"FANT-04ABGN-1414-P-N"` - `"FANT-04ABGN-8065-P-N"` - `"FANT-04ABGN-0606-O-R"` - `"FANT-04ABGN-0606-P-R"` - `"FANT-10ACAX-1213-D-N"` - `"FANT-08ABGN-1213-D-R"` |
| **power-level**  integer | Radio power level as a percentage of the maximum transmit power |
| **power-mode**  string | Set radio effective isotropic radiated power  **Choices:**   - `"dBm"` - `"percentage"` |
| **power-value**  integer | Radio EIRP power in dBm |
| **powersave-optimize**  list / elements=string | Enable client power-saving features such as TIM, AC VO, and OBSS etc.  **Choices:**   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection-mode**  string | Enable/disable 802.  **Choices:**   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio-id**  integer | Radio-Id. |
| **rts-threshold**  integer | Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS |
| **sam-bssid**  string | BSSID for WiFi network. |
| **sam-captive-portal**  string | Enable/disable Captive Portal Authentication  **Choices:**   - `"disable"` - `"enable"` |
| **sam-cwp-failure-string**  string | Failure identification on the page after an incorrect login. |
| **sam-cwp-match-string**  string | Identification string from the captive portal login form. |
| **sam-cwp-password**  any | (list) no description |
| **sam-cwp-success-string**  string | Success identification on the page after a successful login. |
| **sam-cwp-test-url**  string | Website the client is trying to access. |
| **sam-cwp-username**  string | Username for captive portal authentication. |
| **sam-password**  any | (list) Passphrase for WiFi network connection. |
| **sam-report-intv**  integer | SAM report interval |
| **sam-security-type**  string | Select WiFi network security type  **Choices:**   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam-server**  string | SAM test server IP address or domain name. |
| **sam-server-fqdn**  string | SAM test server domain name. |
| **sam-server-ip**  string | SAM test server IP address. |
| **sam-server-type**  string | Select SAM server type  **Choices:**   - `"ip"` - `"fqdn"` |
| **sam-ssid**  string | SSID for WiFi network. |
| **sam-test**  string | Select SAM test type  **Choices:**   - `"ping"` - `"iperf"` |
| **sam-username**  string | Username for WiFi network connection. |
| **short-guard-interval**  string | Use either the short guard interval  **Choices:**   - `"disable"` - `"enable"` |
| **spectrum-analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  **Choices:**   - `"disable"` - `"enable"` - `"scan-only"` |
| **transmit-optimize**  list / elements=string | Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc.  **Choices:**   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap-all**  string | Configure method for assigning SSIDs to this FortiAP  **Choices:**   - `"disable"` - `"enable"` - `"tunnel"` - `"bridge"` - `"manual"` |
| **vap1**  string | Virtual Access Point |
| **vap2**  string | Virtual Access Point |
| **vap3**  string | Virtual Access Point |
| **vap4**  string | Virtual Access Point |
| **vap5**  string | Virtual Access Point |
| **vap6**  string | Virtual Access Point |
| **vap7**  string | Virtual Access Point |
| **vap8**  string | Virtual Access Point |
| **vaps**  any | (list or str) Manually selected list of Virtual Access Points |
| **wids-profile**  string | Wireless Intrusion Detection System |
| **zero-wait-dfs**  string | Enable/disable zero wait DFS on radio  **Choices:**   - `"disable"` - `"enable"` |
| **radio-2**  dictionary | no description |
| **80211d**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **airtime-fairness**  string | Enable/disable airtime fairness  **Choices:**   - `"disable"` - `"enable"` |
| **amsdu**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **ap-handoff**  string | Enable/disable AP handoff of clients to other APs  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-addr**  string | MAC address to monitor. |
| **ap-sniffer-bufsize**  integer | Sniffer buffer size |
| **ap-sniffer-chan**  integer | Channel on which to operate the sniffer |
| **ap-sniffer-ctl**  string | Enable/disable sniffer on WiFi control frame  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-data**  string | Enable/disable sniffer on WiFi data frame  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-beacon**  string | Enable/disable sniffer on WiFi management Beacon frames  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-other**  string | Enable/disable sniffer on WiFi management other frames  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-probe**  string | Enable/disable sniffer on WiFi management probe frames  **Choices:**   - `"disable"` - `"enable"` |
| **arrp-profile**  string | Distributed Automatic Radio Resource Provisioning |
| **auto-power-high**  integer | The upper bound of automatic transmit power adjustment in dBm |
| **auto-power-level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference  **Choices:**   - `"disable"` - `"enable"` |
| **auto-power-low**  integer | The lower bound of automatic transmit power adjustment in dBm |
| **auto-power-target**  string | The target of automatic transmit power adjustment in dBm. |
| **band**  string | WiFi band that Radio 2 operates on.  **Choices:**   - `"802.11b"` - `"802.11a"` - `"802.11g"` - `"802.11n"` - `"802.11ac"` - `"802.11n-5G"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n,g-only"` - `"802.11ac-only"` - `"802.11ac,n-only"` - `"802.11n-5G-only"` - `"802.11ax-5G-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ax-6G"` |
| **band-5g-type**  string | WiFi 5G band type.  **Choices:**   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth-admission-control**  string | Enable/disable WiFi multimedia  **Choices:**   - `"disable"` - `"enable"` |
| **bandwidth-capacity**  integer | Maximum bandwidth capacity allowed |
| **beacon-interval**  integer | Beacon interval. |
| **bss-color**  integer | BSS color value for this 11ax radio |
| **bss-color-mode**  string | BSS color mode for this 11ax radio  **Choices:**   - `"auto"` - `"static"` |
| **call-admission-control**  string | Enable/disable WiFi multimedia  **Choices:**   - `"disable"` - `"enable"` |
| **call-capacity**  integer | Maximum number of Voice over WLAN |
| **channel**  any | (list) Selected list of wireless radio channels. |
| **channel-bonding**  string | Channel bandwidth  **Choices:**   - `"disable"` - `"enable"` - `"80MHz"` - `"40MHz"` - `"20MHz"` - `"160MHz"` |
| **channel-utilization**  string | Enable/disable measuring channel utilization.  **Choices:**   - `"disable"` - `"enable"` |
| **coexistence**  string | Enable/disable allowing both HT20 and HT40 on the same radio  **Choices:**   - `"disable"` - `"enable"` |
| **darrp**  string | Enable/disable Distributed Automatic Radio Resource Provisioning  **Choices:**   - `"disable"` - `"enable"` |
| **drma**  string | Enable/disable dynamic radio mode assignment  **Choices:**   - `"disable"` - `"enable"` |
| **drma-sensitivity**  string | Network Coverage Factor  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | Delivery Traffic Indication Map |
| **frag-threshold**  integer | Maximum packet size that can be sent without fragmentation |
| **frequency-handoff**  string | Enable/disable frequency handoff of clients to other channels  **Choices:**   - `"disable"` - `"enable"` |
| **iperf-protocol**  string | Iperf test protocol  **Choices:**   - `"udp"` - `"tcp"` |
| **iperf-server-port**  integer | Iperf service port number. |
| **max-clients**  integer | Maximum number of stations |
| **max-distance**  integer | Maximum expected distance between the AP and clients |
| **mimo-mode**  string | Configure radio MIMO mode  **Choices:**   - `"default"` - `"1x1"` - `"2x2"` - `"3x3"` - `"4x4"` - `"8x8"` |
| **mode**  string | Mode of radio 2.  **Choices:**   - `"disabled"` - `"ap"` - `"monitor"` - `"sniffer"` - `"sam"` |
| **optional-antenna**  string | Optional antenna used on FAP  **Choices:**   - `"none"` - `"FANT-04ABGN-0606-O-N"` - `"FANT-04ABGN-1414-P-N"` - `"FANT-04ABGN-8065-P-N"` - `"FANT-04ABGN-0606-O-R"` - `"FANT-04ABGN-0606-P-R"` - `"FANT-10ACAX-1213-D-N"` - `"FANT-08ABGN-1213-D-R"` |
| **power-level**  integer | Radio power level as a percentage of the maximum transmit power |
| **power-mode**  string | Set radio effective isotropic radiated power  **Choices:**   - `"dBm"` - `"percentage"` |
| **power-value**  integer | Radio EIRP power in dBm |
| **powersave-optimize**  list / elements=string | Enable client power-saving features such as TIM, AC VO, and OBSS etc.  **Choices:**   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection-mode**  string | Enable/disable 802.  **Choices:**   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio-id**  integer | Radio-Id. |
| **rts-threshold**  integer | Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS |
| **sam-bssid**  string | BSSID for WiFi network. |
| **sam-captive-portal**  string | Enable/disable Captive Portal Authentication  **Choices:**   - `"disable"` - `"enable"` |
| **sam-cwp-failure-string**  string | Failure identification on the page after an incorrect login. |
| **sam-cwp-match-string**  string | Identification string from the captive portal login form. |
| **sam-cwp-password**  any | (list) no description |
| **sam-cwp-success-string**  string | Success identification on the page after a successful login. |
| **sam-cwp-test-url**  string | Website the client is trying to access. |
| **sam-cwp-username**  string | Username for captive portal authentication. |
| **sam-password**  any | (list) Passphrase for WiFi network connection. |
| **sam-report-intv**  integer | SAM report interval |
| **sam-security-type**  string | Select WiFi network security type  **Choices:**   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam-server**  string | SAM test server IP address or domain name. |
| **sam-server-fqdn**  string | SAM test server domain name. |
| **sam-server-ip**  string | SAM test server IP address. |
| **sam-server-type**  string | Select SAM server type  **Choices:**   - `"ip"` - `"fqdn"` |
| **sam-ssid**  string | SSID for WiFi network. |
| **sam-test**  string | Select SAM test type  **Choices:**   - `"ping"` - `"iperf"` |
| **sam-username**  string | Username for WiFi network connection. |
| **short-guard-interval**  string | Use either the short guard interval  **Choices:**   - `"disable"` - `"enable"` |
| **spectrum-analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  **Choices:**   - `"disable"` - `"enable"` - `"scan-only"` |
| **transmit-optimize**  list / elements=string | Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc.  **Choices:**   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap-all**  string | Configure method for assigning SSIDs to this FortiAP  **Choices:**   - `"disable"` - `"enable"` - `"tunnel"` - `"bridge"` - `"manual"` |
| **vap1**  string | Virtual Access Point |
| **vap2**  string | Virtual Access Point |
| **vap3**  string | Virtual Access Point |
| **vap4**  string | Virtual Access Point |
| **vap5**  string | Virtual Access Point |
| **vap6**  string | Virtual Access Point |
| **vap7**  string | Virtual Access Point |
| **vap8**  string | Virtual Access Point |
| **vaps**  any | (list or str) Manually selected list of Virtual Access Points |
| **wids-profile**  string | Wireless Intrusion Detection System |
| **zero-wait-dfs**  string | Enable/disable zero wait DFS on radio  **Choices:**   - `"disable"` - `"enable"` |
| **radio-3**  dictionary | no description |
| **80211d**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **airtime-fairness**  string | Enable/disable airtime fairness  **Choices:**   - `"disable"` - `"enable"` |
| **amsdu**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **ap-handoff**  string | Enable/disable AP handoff of clients to other APs  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-addr**  string | MAC address to monitor. |
| **ap-sniffer-bufsize**  integer | Sniffer buffer size |
| **ap-sniffer-chan**  integer | Channel on which to operate the sniffer |
| **ap-sniffer-ctl**  string | Enable/disable sniffer on WiFi control frame  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-data**  string | Enable/disable sniffer on WiFi data frame  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-beacon**  string | Enable/disable sniffer on WiFi management Beacon frames  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-other**  string | Enable/disable sniffer on WiFi management other frames  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-probe**  string | Enable/disable sniffer on WiFi management probe frames  **Choices:**   - `"disable"` - `"enable"` |
| **arrp-profile**  string | Distributed Automatic Radio Resource Provisioning |
| **auto-power-high**  integer | The upper bound of automatic transmit power adjustment in dBm |
| **auto-power-level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference  **Choices:**   - `"disable"` - `"enable"` |
| **auto-power-low**  integer | The lower bound of automatic transmit power adjustment in dBm |
| **auto-power-target**  string | The target of automatic transmit power adjustment in dBm. |
| **band**  string | WiFi band that Radio 3 operates on.  **Choices:**   - `"802.11b"` - `"802.11a"` - `"802.11g"` - `"802.11n"` - `"802.11ac"` - `"802.11n-5G"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n,g-only"` - `"802.11ac-only"` - `"802.11ac,n-only"` - `"802.11n-5G-only"` - `"802.11ax-5G-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ax-6G"` |
| **band-5g-type**  string | WiFi 5G band type.  **Choices:**   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth-admission-control**  string | Enable/disable WiFi multimedia  **Choices:**   - `"disable"` - `"enable"` |
| **bandwidth-capacity**  integer | Maximum bandwidth capacity allowed |
| **beacon-interval**  integer | Beacon interval. |
| **bss-color**  integer | BSS color value for this 11ax radio |
| **bss-color-mode**  string | BSS color mode for this 11ax radio  **Choices:**   - `"auto"` - `"static"` |
| **call-admission-control**  string | Enable/disable WiFi multimedia  **Choices:**   - `"disable"` - `"enable"` |
| **call-capacity**  integer | Maximum number of Voice over WLAN |
| **channel**  any | (list) Selected list of wireless radio channels. |
| **channel-bonding**  string | Channel bandwidth  **Choices:**   - `"80MHz"` - `"40MHz"` - `"20MHz"` - `"160MHz"` |
| **channel-utilization**  string | Enable/disable measuring channel utilization.  **Choices:**   - `"disable"` - `"enable"` |
| **coexistence**  string | Enable/disable allowing both HT20 and HT40 on the same radio  **Choices:**   - `"disable"` - `"enable"` |
| **darrp**  string | Enable/disable Distributed Automatic Radio Resource Provisioning  **Choices:**   - `"disable"` - `"enable"` |
| **drma**  string | Enable/disable dynamic radio mode assignment  **Choices:**   - `"disable"` - `"enable"` |
| **drma-sensitivity**  string | Network Coverage Factor  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | Delivery Traffic Indication Map |
| **frag-threshold**  integer | Maximum packet size that can be sent without fragmentation |
| **frequency-handoff**  string | Enable/disable frequency handoff of clients to other channels  **Choices:**   - `"disable"` - `"enable"` |
| **iperf-protocol**  string | Iperf test protocol  **Choices:**   - `"udp"` - `"tcp"` |
| **iperf-server-port**  integer | Iperf service port number. |
| **max-clients**  integer | Maximum number of stations |
| **max-distance**  integer | Maximum expected distance between the AP and clients |
| **mimo-mode**  string | Configure radio MIMO mode  **Choices:**   - `"default"` - `"1x1"` - `"2x2"` - `"3x3"` - `"4x4"` - `"8x8"` |
| **mode**  string | Mode of radio 3.  **Choices:**   - `"disabled"` - `"ap"` - `"monitor"` - `"sniffer"` - `"sam"` |
| **optional-antenna**  string | Optional antenna used on FAP  **Choices:**   - `"none"` - `"FANT-04ABGN-0606-O-N"` - `"FANT-04ABGN-1414-P-N"` - `"FANT-04ABGN-8065-P-N"` - `"FANT-04ABGN-0606-O-R"` - `"FANT-04ABGN-0606-P-R"` - `"FANT-10ACAX-1213-D-N"` - `"FANT-08ABGN-1213-D-R"` |
| **power-level**  integer | Radio power level as a percentage of the maximum transmit power |
| **power-mode**  string | Set radio effective isotropic radiated power  **Choices:**   - `"dBm"` - `"percentage"` |
| **power-value**  integer | Radio EIRP power in dBm |
| **powersave-optimize**  list / elements=string | Enable client power-saving features such as TIM, AC VO, and OBSS etc.  **Choices:**   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection-mode**  string | Enable/disable 802.  **Choices:**   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio-id**  integer | Radio-Id. |
| **rts-threshold**  integer | Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS |
| **sam-bssid**  string | BSSID for WiFi network. |
| **sam-captive-portal**  string | Enable/disable Captive Portal Authentication  **Choices:**   - `"disable"` - `"enable"` |
| **sam-cwp-failure-string**  string | Failure identification on the page after an incorrect login. |
| **sam-cwp-match-string**  string | Identification string from the captive portal login form. |
| **sam-cwp-password**  any | (list) no description |
| **sam-cwp-success-string**  string | Success identification on the page after a successful login. |
| **sam-cwp-test-url**  string | Website the client is trying to access. |
| **sam-cwp-username**  string | Username for captive portal authentication. |
| **sam-password**  any | (list) Passphrase for WiFi network connection. |
| **sam-report-intv**  integer | SAM report interval |
| **sam-security-type**  string | Select WiFi network security type  **Choices:**   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam-server**  string | SAM test server IP address or domain name. |
| **sam-server-fqdn**  string | SAM test server domain name. |
| **sam-server-ip**  string | SAM test server IP address. |
| **sam-server-type**  string | Select SAM server type  **Choices:**   - `"ip"` - `"fqdn"` |
| **sam-ssid**  string | SSID for WiFi network. |
| **sam-test**  string | Select SAM test type  **Choices:**   - `"ping"` - `"iperf"` |
| **sam-username**  string | Username for WiFi network connection. |
| **short-guard-interval**  string | Use either the short guard interval  **Choices:**   - `"disable"` - `"enable"` |
| **spectrum-analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  **Choices:**   - `"disable"` - `"enable"` - `"scan-only"` |
| **transmit-optimize**  list / elements=string | Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc.  **Choices:**   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap-all**  string | Configure method for assigning SSIDs to this FortiAP  **Choices:**   - `"disable"` - `"enable"` - `"tunnel"` - `"bridge"` - `"manual"` |
| **vap1**  string | Virtual Access Point |
| **vap2**  string | Virtual Access Point |
| **vap3**  string | Virtual Access Point |
| **vap4**  string | Virtual Access Point |
| **vap5**  string | Virtual Access Point |
| **vap6**  string | Virtual Access Point |
| **vap7**  string | Virtual Access Point |
| **vap8**  string | Virtual Access Point |
| **vaps**  any | (list or str) Manually selected list of Virtual Access Points |
| **wids-profile**  string | Wireless Intrusion Detection System |
| **zero-wait-dfs**  string | Enable/disable zero wait DFS on radio  **Choices:**   - `"disable"` - `"enable"` |
| **radio-4**  dictionary | no description |
| **80211d**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **airtime-fairness**  string | Enable/disable airtime fairness  **Choices:**   - `"disable"` - `"enable"` |
| **amsdu**  string | Enable/disable 802.  **Choices:**   - `"disable"` - `"enable"` |
| **ap-handoff**  string | Enable/disable AP handoff of clients to other APs  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-addr**  string | MAC address to monitor. |
| **ap-sniffer-bufsize**  integer | Sniffer buffer size |
| **ap-sniffer-chan**  integer | Channel on which to operate the sniffer |
| **ap-sniffer-ctl**  string | Enable/disable sniffer on WiFi control frame  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-data**  string | Enable/disable sniffer on WiFi data frame  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-beacon**  string | Enable/disable sniffer on WiFi management Beacon frames  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-other**  string | Enable/disable sniffer on WiFi management other frames  **Choices:**   - `"disable"` - `"enable"` |
| **ap-sniffer-mgmt-probe**  string | Enable/disable sniffer on WiFi management probe frames  **Choices:**   - `"disable"` - `"enable"` |
| **arrp-profile**  string | Distributed Automatic Radio Resource Provisioning |
| **auto-power-high**  integer | The upper bound of automatic transmit power adjustment in dBm |
| **auto-power-level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference  **Choices:**   - `"disable"` - `"enable"` |
| **auto-power-low**  integer | The lower bound of automatic transmit power adjustment in dBm |
| **auto-power-target**  string | The target of automatic transmit power adjustment in dBm. |
| **band**  string | WiFi band that Radio 3 operates on.  **Choices:**   - `"802.11b"` - `"802.11a"` - `"802.11g"` - `"802.11n"` - `"802.11ac"` - `"802.11n-5G"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n,g-only"` - `"802.11ac-only"` - `"802.11ac,n-only"` - `"802.11n-5G-only"` - `"802.11ax-5G-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ax-6G"` |
| **band-5g-type**  string | WiFi 5G band type.  **Choices:**   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth-admission-control**  string | Enable/disable WiFi multimedia  **Choices:**   - `"disable"` - `"enable"` |
| **bandwidth-capacity**  integer | Maximum bandwidth capacity allowed |
| **beacon-interval**  integer | Beacon interval. |
| **bss-color**  integer | BSS color value for this 11ax radio |
| **bss-color-mode**  string | BSS color mode for this 11ax radio  **Choices:**   - `"auto"` - `"static"` |
| **call-admission-control**  string | Enable/disable WiFi multimedia  **Choices:**   - `"disable"` - `"enable"` |
| **call-capacity**  integer | Maximum number of Voice over WLAN |
| **channel**  any | (list) Selected list of wireless radio channels. |
| **channel-bonding**  string | Channel bandwidth  **Choices:**   - `"80MHz"` - `"40MHz"` - `"20MHz"` - `"160MHz"` |
| **channel-utilization**  string | Enable/disable measuring channel utilization.  **Choices:**   - `"disable"` - `"enable"` |
| **coexistence**  string | Enable/disable allowing both HT20 and HT40 on the same radio  **Choices:**   - `"disable"` - `"enable"` |
| **darrp**  string | Enable/disable Distributed Automatic Radio Resource Provisioning  **Choices:**   - `"disable"` - `"enable"` |
| **drma**  string | Enable/disable dynamic radio mode assignment  **Choices:**   - `"disable"` - `"enable"` |
| **drma-sensitivity**  string | Network Coverage Factor  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | Delivery Traffic Indication Map |
| **frag-threshold**  integer | Maximum packet size that can be sent without fragmentation |
| **frequency-handoff**  string | Enable/disable frequency handoff of clients to other channels  **Choices:**   - `"disable"` - `"enable"` |
| **iperf-protocol**  string | Iperf test protocol  **Choices:**   - `"udp"` - `"tcp"` |
| **iperf-server-port**  integer | Iperf service port number. |
| **max-clients**  integer | Maximum number of stations |
| **max-distance**  integer | Maximum expected distance between the AP and clients |
| **mimo-mode**  string | Configure radio MIMO mode  **Choices:**   - `"default"` - `"1x1"` - `"2x2"` - `"3x3"` - `"4x4"` - `"8x8"` |
| **mode**  string | Mode of radio 3.  **Choices:**   - `"ap"` - `"monitor"` - `"sniffer"` - `"disabled"` - `"sam"` |
| **optional-antenna**  string | Optional antenna used on FAP  **Choices:**   - `"none"` - `"FANT-04ABGN-0606-O-N"` - `"FANT-04ABGN-1414-P-N"` - `"FANT-04ABGN-8065-P-N"` - `"FANT-04ABGN-0606-O-R"` - `"FANT-04ABGN-0606-P-R"` - `"FANT-10ACAX-1213-D-N"` - `"FANT-08ABGN-1213-D-R"` |
| **power-level**  integer | Radio power level as a percentage of the maximum transmit power |
| **power-mode**  string | Set radio effective isotropic radiated power  **Choices:**   - `"dBm"` - `"percentage"` |
| **power-value**  integer | Radio EIRP power in dBm |
| **powersave-optimize**  list / elements=string | Enable client power-saving features such as TIM, AC VO, and OBSS etc.  **Choices:**   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection-mode**  string | Enable/disable 802.  **Choices:**   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio-id**  integer | Radio-Id. |
| **rts-threshold**  integer | Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS |
| **sam-bssid**  string | BSSID for WiFi network. |
| **sam-captive-portal**  string | Enable/disable Captive Portal Authentication  **Choices:**   - `"disable"` - `"enable"` |
| **sam-cwp-failure-string**  string | Failure identification on the page after an incorrect login. |
| **sam-cwp-match-string**  string | Identification string from the captive portal login form. |
| **sam-cwp-password**  any | (list) no description |
| **sam-cwp-success-string**  string | Success identification on the page after a successful login. |
| **sam-cwp-test-url**  string | Website the client is trying to access. |
| **sam-cwp-username**  string | Username for captive portal authentication. |
| **sam-password**  any | (list) Passphrase for WiFi network connection. |
| **sam-report-intv**  integer | SAM report interval |
| **sam-security-type**  string | Select WiFi network security type  **Choices:**   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam-server**  string | SAM test server IP address or domain name. |
| **sam-server-fqdn**  string | SAM test server domain name. |
| **sam-server-ip**  string | SAM test server IP address. |
| **sam-server-type**  string | Select SAM server type  **Choices:**   - `"ip"` - `"fqdn"` |
| **sam-ssid**  string | SSID for WiFi network. |
| **sam-test**  string | Select SAM test type  **Choices:**   - `"ping"` - `"iperf"` |
| **sam-username**  string | Username for WiFi network connection. |
| **short-guard-interval**  string | Use either the short guard interval  **Choices:**   - `"disable"` - `"enable"` |
| **spectrum-analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  **Choices:**   - `"disable"` - `"enable"` - `"scan-only"` |
| **transmit-optimize**  list / elements=string | Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc.  **Choices:**   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap-all**  string | Configure method for assigning SSIDs to this FortiAP  **Choices:**   - `"disable"` - `"enable"` - `"tunnel"` - `"bridge"` - `"manual"` |
| **vap1**  string | Virtual Access Point |
| **vap2**  string | Virtual Access Point |
| **vap3**  string | Virtual Access Point |
| **vap4**  string | Virtual Access Point |
| **vap5**  string | Virtual Access Point |
| **vap6**  string | Virtual Access Point |
| **vap7**  string | Virtual Access Point |
| **vap8**  string | Virtual Access Point |
| **vaps**  any | (list or str) Manually selected list of Virtual Access Points |
| **wids-profile**  string | Wireless Intrusion Detection System |
| **zero-wait-dfs**  string | Enable/disable zero wait DFS on radio  **Choices:**   - `"disable"` - `"enable"` |
| **snmp**  string | Enable/disable SNMP for the WTP, FortiAP, or AP  **Choices:**   - `"disable"` - `"enable"` |
| **split-tunneling-acl**  list / elements=dictionary | Split-Tunneling-Acl. |
| **dest-ip**  string | Destination IP and mask for the split-tunneling subnet. |
| **id**  integer | ID. |
| **split-tunneling-acl-local-ap-subnet**  string | Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL  **Choices:**   - `"disable"` - `"enable"` |
| **split-tunneling-acl-path**  string | Split tunneling ACL path is local/tunnel.  **Choices:**   - `"tunnel"` - `"local"` |
| **syslog-profile**  string | System log server configuration profile name. |
| **tun-mtu-downlink**  integer | Downlink CAPWAP tunnel MTU |
| **tun-mtu-uplink**  integer | Uplink CAPWAP tunnel MTU |
| **unii-4-5ghz-band**  string | Enable/disable UNII-4 5Ghz band channels  **Choices:**   - `"disable"` - `"enable"` |
| **wan-port-auth**  string | Set WAN port authentication mode  **Choices:**   - `"none"` - `"802.1x"` |
| **wan-port-auth-methods**  string | WAN port 802.  **Choices:**   - `"all"` - `"EAP-FAST"` - `"EAP-TLS"` - `"EAP-PEAP"` |
| **wan-port-auth-password**  any | (list) no description |
| **wan-port-auth-usrname**  string | Set WAN port 802. |
| **wan-port-mode**  string | Enable/disable using a WAN port as a LAN port.  **Choices:**   - `"wan-lan"` - `"wan-only"` |

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
    - name: Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
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
          ble-profile: <string>
          comment: <string>
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
              id: <integer>
              mac: <string>
          dtls-in-kernel: <value in [disable, enable]>
          dtls-policy:
            - clear-text
            - dtls-enabled
            - ipsec-vpn
            - ipsec-sn-vpn
          energy-efficient-ethernet: <value in [disable, enable]>
          ext-info-enable: <value in [disable, enable]>
          handoff-roaming: <value in [disable, enable]>
          handoff-rssi: <integer>
          handoff-sta-thresh: <integer>
          ip-fragment-preventing:
            - tcp-mss-adjust
            - icmp-unreachable
          led-schedules: <list or string>
          led-state: <value in [disable, enable]>
          lldp: <value in [disable, enable]>
          login-passwd: <list or string>
          login-passwd-change: <value in [no, yes, default]>
          max-clients: <integer>
          name: <string>
          poe-mode: <value in [auto, 8023af, 8023at, ...]>
          split-tunneling-acl:
            -
              dest-ip: <string>
              id: <integer>
          split-tunneling-acl-local-ap-subnet: <value in [disable, enable]>
          split-tunneling-acl-path: <value in [tunnel, local]>
          tun-mtu-downlink: <integer>
          tun-mtu-uplink: <integer>
          wan-port-mode: <value in [wan-lan, wan-only]>
          snmp: <value in [disable, enable]>
          ap-handoff: <value in [disable, enable]>
          apcfg-profile: <string>
          frequency-handoff: <value in [disable, enable]>
          lan:
            port-esl-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port-esl-ssid: <string>
            port-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port-ssid: <string>
            port1-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port1-ssid: <string>
            port2-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port2-ssid: <string>
            port3-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port3-ssid: <string>
            port4-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port4-ssid: <string>
            port5-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port5-ssid: <string>
            port6-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port6-ssid: <string>
            port7-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port7-ssid: <string>
            port8-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
            port8-ssid: <string>
          lbs:
            aeroscout: <value in [disable, enable]>
            aeroscout-ap-mac: <value in [bssid, board-mac]>
            aeroscout-mmu-report: <value in [disable, enable]>
            aeroscout-mu: <value in [disable, enable]>
            aeroscout-mu-factor: <integer>
            aeroscout-mu-timeout: <integer>
            aeroscout-server-ip: <string>
            aeroscout-server-port: <integer>
            ekahau-blink-mode: <value in [disable, enable]>
            ekahau-tag: <string>
            erc-server-ip: <string>
            erc-server-port: <integer>
            fortipresence: <value in [disable, enable, enable2, ...]>
            fortipresence-ble: <value in [disable, enable]>
            fortipresence-frequency: <integer>
            fortipresence-port: <integer>
            fortipresence-project: <string>
            fortipresence-rogue: <value in [disable, enable]>
            fortipresence-secret: <list or string>
            fortipresence-server: <string>
            fortipresence-unassoc: <value in [disable, enable]>
            station-locate: <value in [disable, enable]>
            fortipresence-server-addr-type: <value in [fqdn, ipv4]>
            fortipresence-server-fqdn: <string>
            polestar: <value in [disable, enable]>
            polestar-accumulation-interval: <integer>
            polestar-asset-addrgrp-list: <string>
            polestar-asset-uuid-list1: <string>
            polestar-asset-uuid-list2: <string>
            polestar-asset-uuid-list3: <string>
            polestar-asset-uuid-list4: <string>
            polestar-protocol: <value in [WSS]>
            polestar-reporting-interval: <integer>
            polestar-server-fqdn: <string>
            polestar-server-path: <string>
            polestar-server-port: <integer>
            polestar-server-token: <string>
          platform:
            ddscan: <value in [disable, enable]>
            mode: <value in [dual-5G, single-5G]>
            type: <value in [30B-50B, 60B, 80CM-81CM, ...]>
            _local_platform_str: <string>
          radio-1:
            airtime-fairness: <value in [disable, enable]>
            amsdu: <value in [disable, enable]>
            ap-sniffer-addr: <string>
            ap-sniffer-bufsize: <integer>
            ap-sniffer-chan: <integer>
            ap-sniffer-ctl: <value in [disable, enable]>
            ap-sniffer-data: <value in [disable, enable]>
            ap-sniffer-mgmt-beacon: <value in [disable, enable]>
            ap-sniffer-mgmt-other: <value in [disable, enable]>
            ap-sniffer-mgmt-probe: <value in [disable, enable]>
            auto-power-high: <integer>
            auto-power-level: <value in [disable, enable]>
            auto-power-low: <integer>
            auto-power-target: <string>
            band: <value in [802.11b, 802.11a, 802.11g, ...]>
            band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
            bandwidth-admission-control: <value in [disable, enable]>
            bandwidth-capacity: <integer>
            beacon-interval: <integer>
            bss-color: <integer>
            call-admission-control: <value in [disable, enable]>
            call-capacity: <integer>
            channel: <list or string>
            channel-bonding: <value in [disable, enable, 80MHz, ...]>
            channel-utilization: <value in [disable, enable]>
            coexistence: <value in [disable, enable]>
            darrp: <value in [disable, enable]>
            drma: <value in [disable, enable]>
            drma-sensitivity: <value in [low, medium, high]>
            dtim: <integer>
            frag-threshold: <integer>
            max-clients: <integer>
            max-distance: <integer>
            mode: <value in [disabled, ap, monitor, ...]>
            power-level: <integer>
            powersave-optimize:
              - tim
              - ac-vo
              - no-obss-scan
              - no-11b-rate
              - client-rate-follow
            protection-mode: <value in [rtscts, ctsonly, disable]>
            radio-id: <integer>
            rts-threshold: <integer>
            short-guard-interval: <value in [disable, enable]>
            spectrum-analysis: <value in [disable, enable, scan-only]>
            transmit-optimize:
              - disable
              - power-save
              - aggr-limit
              - retry-limit
              - send-bar
            vap-all: <value in [disable, enable, tunnel, ...]>
            vap1: <string>
            vap2: <string>
            vap3: <string>
            vap4: <string>
            vap5: <string>
            vap6: <string>
            vap7: <string>
            vap8: <string>
            vaps: <list or string>
            wids-profile: <string>
            zero-wait-dfs: <value in [disable, enable]>
            frequency-handoff: <value in [disable, enable]>
            ap-handoff: <value in [disable, enable]>
            iperf-protocol: <value in [udp, tcp]>
            iperf-server-port: <integer>
            power-mode: <value in [dBm, percentage]>
            power-value: <integer>
            sam-bssid: <string>
            sam-captive-portal: <value in [disable, enable]>
            sam-password: <list or string>
            sam-report-intv: <integer>
            sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
            sam-server: <string>
            sam-ssid: <string>
            sam-test: <value in [ping, iperf]>
            sam-username: <string>
            arrp-profile: <string>
            bss-color-mode: <value in [auto, static]>
            sam-cwp-failure-string: <string>
            sam-cwp-match-string: <string>
            sam-cwp-password: <list or string>
            sam-cwp-success-string: <string>
            sam-cwp-test-url: <string>
            sam-cwp-username: <string>
            sam-server-fqdn: <string>
            sam-server-ip: <string>
            sam-server-type: <value in [ip, fqdn]>
            80211d: <value in [disable, enable]>
            optional-antenna: <value in [none, FANT-04ABGN-0606-O-N, FANT-04ABGN-1414-P-N, ...]>
            mimo-mode: <value in [default, 1x1, 2x2, ...]>
          radio-2:
            airtime-fairness: <value in [disable, enable]>
            amsdu: <value in [disable, enable]>
            ap-sniffer-addr: <string>
            ap-sniffer-bufsize: <integer>
            ap-sniffer-chan: <integer>
            ap-sniffer-ctl: <value in [disable, enable]>
            ap-sniffer-data: <value in [disable, enable]>
            ap-sniffer-mgmt-beacon: <value in [disable, enable]>
            ap-sniffer-mgmt-other: <value in [disable, enable]>
            ap-sniffer-mgmt-probe: <value in [disable, enable]>
            auto-power-high: <integer>
            auto-power-level: <value in [disable, enable]>
            auto-power-low: <integer>
            auto-power-target: <string>
            band: <value in [802.11b, 802.11a, 802.11g, ...]>
            band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
            bandwidth-admission-control: <value in [disable, enable]>
            bandwidth-capacity: <integer>
            beacon-interval: <integer>
            bss-color: <integer>
            call-admission-control: <value in [disable, enable]>
            call-capacity: <integer>
            channel: <list or string>
            channel-bonding: <value in [disable, enable, 80MHz, ...]>
            channel-utilization: <value in [disable, enable]>
            coexistence: <value in [disable, enable]>
            darrp: <value in [disable, enable]>
            drma: <value in [disable, enable]>
            drma-sensitivity: <value in [low, medium, high]>
            dtim: <integer>
            frag-threshold: <integer>
            max-clients: <integer>
            max-distance: <integer>
            mode: <value in [disabled, ap, monitor, ...]>
            power-level: <integer>
            powersave-optimize:
              - tim
              - ac-vo
              - no-obss-scan
              - no-11b-rate
              - client-rate-follow
            protection-mode: <value in [rtscts, ctsonly, disable]>
            radio-id: <integer>
            rts-threshold: <integer>
            short-guard-interval: <value in [disable, enable]>
            spectrum-analysis: <value in [disable, enable, scan-only]>
            transmit-optimize:
              - disable
              - power-save
              - aggr-limit
              - retry-limit
              - send-bar
            vap-all: <value in [disable, enable, tunnel, ...]>
            vap1: <string>
            vap2: <string>
            vap3: <string>
            vap4: <string>
            vap5: <string>
            vap6: <string>
            vap7: <string>
            vap8: <string>
            vaps: <list or string>
            wids-profile: <string>
            zero-wait-dfs: <value in [disable, enable]>
            frequency-handoff: <value in [disable, enable]>
            ap-handoff: <value in [disable, enable]>
            iperf-protocol: <value in [udp, tcp]>
            iperf-server-port: <integer>
            power-mode: <value in [dBm, percentage]>
            power-value: <integer>
            sam-bssid: <string>
            sam-captive-portal: <value in [disable, enable]>
            sam-password: <list or string>
            sam-report-intv: <integer>
            sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
            sam-server: <string>
            sam-ssid: <string>
            sam-test: <value in [ping, iperf]>
            sam-username: <string>
            arrp-profile: <string>
            bss-color-mode: <value in [auto, static]>
            sam-cwp-failure-string: <string>
            sam-cwp-match-string: <string>
            sam-cwp-password: <list or string>
            sam-cwp-success-string: <string>
            sam-cwp-test-url: <string>
            sam-cwp-username: <string>
            sam-server-fqdn: <string>
            sam-server-ip: <string>
            sam-server-type: <value in [ip, fqdn]>
            80211d: <value in [disable, enable]>
            optional-antenna: <value in [none, FANT-04ABGN-0606-O-N, FANT-04ABGN-1414-P-N, ...]>
            mimo-mode: <value in [default, 1x1, 2x2, ...]>
          radio-3:
            airtime-fairness: <value in [disable, enable]>
            amsdu: <value in [disable, enable]>
            ap-sniffer-addr: <string>
            ap-sniffer-bufsize: <integer>
            ap-sniffer-chan: <integer>
            ap-sniffer-ctl: <value in [disable, enable]>
            ap-sniffer-data: <value in [disable, enable]>
            ap-sniffer-mgmt-beacon: <value in [disable, enable]>
            ap-sniffer-mgmt-other: <value in [disable, enable]>
            ap-sniffer-mgmt-probe: <value in [disable, enable]>
            auto-power-high: <integer>
            auto-power-level: <value in [disable, enable]>
            auto-power-low: <integer>
            auto-power-target: <string>
            band: <value in [802.11b, 802.11a, 802.11g, ...]>
            band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
            bandwidth-admission-control: <value in [disable, enable]>
            bandwidth-capacity: <integer>
            beacon-interval: <integer>
            bss-color: <integer>
            call-admission-control: <value in [disable, enable]>
            call-capacity: <integer>
            channel: <list or string>
            channel-bonding: <value in [80MHz, 40MHz, 20MHz, ...]>
            channel-utilization: <value in [disable, enable]>
            coexistence: <value in [disable, enable]>
            darrp: <value in [disable, enable]>
            drma: <value in [disable, enable]>
            drma-sensitivity: <value in [low, medium, high]>
            dtim: <integer>
            frag-threshold: <integer>
            max-clients: <integer>
            max-distance: <integer>
            mode: <value in [disabled, ap, monitor, ...]>
            power-level: <integer>
            powersave-optimize:
              - tim
              - ac-vo
              - no-obss-scan
              - no-11b-rate
              - client-rate-follow
            protection-mode: <value in [rtscts, ctsonly, disable]>
            radio-id: <integer>
            rts-threshold: <integer>
            short-guard-interval: <value in [disable, enable]>
            spectrum-analysis: <value in [disable, enable, scan-only]>
            transmit-optimize:
              - disable
              - power-save
              - aggr-limit
              - retry-limit
              - send-bar
            vap-all: <value in [disable, enable, tunnel, ...]>
            vap1: <string>
            vap2: <string>
            vap3: <string>
            vap4: <string>
            vap5: <string>
            vap6: <string>
            vap7: <string>
            vap8: <string>
            vaps: <list or string>
            wids-profile: <string>
            zero-wait-dfs: <value in [disable, enable]>
            frequency-handoff: <value in [disable, enable]>
            ap-handoff: <value in [disable, enable]>
            iperf-protocol: <value in [udp, tcp]>
            iperf-server-port: <integer>
            power-mode: <value in [dBm, percentage]>
            power-value: <integer>
            sam-bssid: <string>
            sam-captive-portal: <value in [disable, enable]>
            sam-password: <list or string>
            sam-report-intv: <integer>
            sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
            sam-server: <string>
            sam-ssid: <string>
            sam-test: <value in [ping, iperf]>
            sam-username: <string>
            arrp-profile: <string>
            bss-color-mode: <value in [auto, static]>
            sam-cwp-failure-string: <string>
            sam-cwp-match-string: <string>
            sam-cwp-password: <list or string>
            sam-cwp-success-string: <string>
            sam-cwp-test-url: <string>
            sam-cwp-username: <string>
            sam-server-fqdn: <string>
            sam-server-ip: <string>
            sam-server-type: <value in [ip, fqdn]>
            80211d: <value in [disable, enable]>
            optional-antenna: <value in [none, FANT-04ABGN-0606-O-N, FANT-04ABGN-1414-P-N, ...]>
            mimo-mode: <value in [default, 1x1, 2x2, ...]>
          radio-4:
            airtime-fairness: <value in [disable, enable]>
            amsdu: <value in [disable, enable]>
            ap-sniffer-addr: <string>
            ap-sniffer-bufsize: <integer>
            ap-sniffer-chan: <integer>
            ap-sniffer-ctl: <value in [disable, enable]>
            ap-sniffer-data: <value in [disable, enable]>
            ap-sniffer-mgmt-beacon: <value in [disable, enable]>
            ap-sniffer-mgmt-other: <value in [disable, enable]>
            ap-sniffer-mgmt-probe: <value in [disable, enable]>
            auto-power-high: <integer>
            auto-power-level: <value in [disable, enable]>
            auto-power-low: <integer>
            auto-power-target: <string>
            band: <value in [802.11b, 802.11a, 802.11g, ...]>
            band-5g-type: <value in [5g-full, 5g-high, 5g-low]>
            bandwidth-admission-control: <value in [disable, enable]>
            bandwidth-capacity: <integer>
            beacon-interval: <integer>
            bss-color: <integer>
            call-admission-control: <value in [disable, enable]>
            call-capacity: <integer>
            channel: <list or string>
            channel-bonding: <value in [80MHz, 40MHz, 20MHz, ...]>
            channel-utilization: <value in [disable, enable]>
            coexistence: <value in [disable, enable]>
            darrp: <value in [disable, enable]>
            drma: <value in [disable, enable]>
            drma-sensitivity: <value in [low, medium, high]>
            dtim: <integer>
            frag-threshold: <integer>
            max-clients: <integer>
            max-distance: <integer>
            mode: <value in [ap, monitor, sniffer, ...]>
            power-level: <integer>
            powersave-optimize:
              - tim
              - ac-vo
              - no-obss-scan
              - no-11b-rate
              - client-rate-follow
            protection-mode: <value in [rtscts, ctsonly, disable]>
            radio-id: <integer>
            rts-threshold: <integer>
            short-guard-interval: <value in [disable, enable]>
            spectrum-analysis: <value in [disable, enable, scan-only]>
            transmit-optimize:
              - disable
              - power-save
              - aggr-limit
              - retry-limit
              - send-bar
            vap-all: <value in [disable, enable, tunnel, ...]>
            vap1: <string>
            vap2: <string>
            vap3: <string>
            vap4: <string>
            vap5: <string>
            vap6: <string>
            vap7: <string>
            vap8: <string>
            vaps: <list or string>
            wids-profile: <string>
            zero-wait-dfs: <value in [disable, enable]>
            frequency-handoff: <value in [disable, enable]>
            ap-handoff: <value in [disable, enable]>
            iperf-protocol: <value in [udp, tcp]>
            iperf-server-port: <integer>
            power-mode: <value in [dBm, percentage]>
            power-value: <integer>
            sam-bssid: <string>
            sam-captive-portal: <value in [disable, enable]>
            sam-password: <list or string>
            sam-report-intv: <integer>
            sam-security-type: <value in [open, wpa-personal, wpa-enterprise]>
            sam-server: <string>
            sam-ssid: <string>
            sam-test: <value in [ping, iperf]>
            sam-username: <string>
            arrp-profile: <string>
            bss-color-mode: <value in [auto, static]>
            sam-cwp-failure-string: <string>
            sam-cwp-match-string: <string>
            sam-cwp-password: <list or string>
            sam-cwp-success-string: <string>
            sam-cwp-test-url: <string>
            sam-cwp-username: <string>
            sam-server-fqdn: <string>
            sam-server-ip: <string>
            sam-server-type: <value in [ip, fqdn]>
            80211d: <value in [disable, enable]>
            optional-antenna: <value in [none, FANT-04ABGN-0606-O-N, FANT-04ABGN-1414-P-N, ...]>
            mimo-mode: <value in [default, 1x1, 2x2, ...]>
          console-login: <value in [disable, enable]>
          esl-ses-dongle:
            apc-addr-type: <value in [fqdn, ip]>
            apc-fqdn: <string>
            apc-ip: <string>
            apc-port: <integer>
            coex-level: <value in [none]>
            compliance-level: <value in [compliance-level-2]>
            esl-channel: <value in [0, 1, 2, ...]>
            output-power: <value in [a, b, c, ...]>
            scd-enable: <value in [disable, enable]>
            tls-cert-verification: <value in [disable, enable]>
            tls-fqdn-verification: <value in [disable, enable]>
          indoor-outdoor-deployment: <value in [platform-determined, outdoor, indoor]>
          syslog-profile: <string>
          wan-port-auth: <value in [none, 802.1x]>
          wan-port-auth-methods: <value in [all, EAP-FAST, EAP-TLS, ...]>
          wan-port-auth-password: <list or string>
          wan-port-auth-usrname: <string>
          _is_factory_setting: <value in [disable, enable, ext]>
          unii-4-5ghz-band: <value in [disable, enable]>
```

## [Return Values](fmgr_wtpprofile_module.md#id5)

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
