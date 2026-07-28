---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_wireless_controller_wtp_profile module – Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_wireless_controller_wtp_profile_module.html
fetched_at: 2026-07-27T17:47:29+00:00
---
# fortinet.fortios.fortios_wireless_controller_wtp_profile module – Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_wtp_profile_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-wtp-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_wtp_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_wtp_profile_module.md#synopsis)
- [Requirements](fortios_wireless_controller_wtp_profile_module.md#requirements)
- [Parameters](fortios_wireless_controller_wtp_profile_module.md#parameters)
- [Notes](fortios_wireless_controller_wtp_profile_module.md#notes)
- [Examples](fortios_wireless_controller_wtp_profile_module.md#examples)
- [Return Values](fortios_wireless_controller_wtp_profile_module.md#return-values)

## [Synopsis](fortios_wireless_controller_wtp_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and wtp_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_wtp_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_wireless_controller_wtp_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **wireless_controller_wtp_profile**  dictionary | Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms. |
| **allowaccess**  list / elements=string | Control management access to the managed WTP, FortiAP, or AP. Separate entries with a space.  Choices:   - `"https"` - `"ssh"` - `"snmp"` - `"telnet"` - `"http"` |
| **ap_country**  string | Country in which this WTP, FortiAP, or AP will operate .  Choices:   - `"--"` - `"AF"` - `"AL"` - `"DZ"` - `"AS"` - `"AO"` - `"AR"` - `"AM"` - `"AU"` - `"AT"` - `"AZ"` - `"BS"` - `"BH"` - `"BD"` - `"BB"` - `"BY"` - `"BE"` - `"BZ"` - `"BJ"` - `"BM"` - `"BT"` - `"BO"` - `"BA"` - `"BW"` - `"BR"` - `"BN"` - `"BG"` - `"BF"` - `"KH"` - `"CM"` - `"KY"` - `"CF"` - `"TD"` - `"CL"` - `"CN"` - `"CX"` - `"CO"` - `"CG"` - `"CD"` - `"CR"` - `"HR"` - `"CY"` - `"CZ"` - `"DK"` - `"DM"` - `"DO"` - `"EC"` - `"EG"` - `"SV"` - `"ET"` - `"EE"` - `"GF"` - `"PF"` - `"FO"` - `"FJ"` - `"FI"` - `"FR"` - `"GE"` - `"DE"` - `"GH"` - `"GI"` - `"GR"` - `"GL"` - `"GD"` - `"GP"` - `"GU"` - `"GT"` - `"GY"` - `"HT"` - `"HN"` - `"HK"` - `"HU"` - `"IS"` - `"IN"` - `"ID"` - `"IQ"` - `"IE"` - `"IM"` - `"IL"` - `"IT"` - `"CI"` - `"JM"` - `"JO"` - `"KZ"` - `"KE"` - `"KR"` - `"KW"` - `"LA"` - `"LV"` - `"LB"` - `"LS"` - `"LY"` - `"LI"` - `"LT"` - `"LU"` - `"MO"` - `"MK"` - `"MG"` - `"MW"` - `"MY"` - `"MV"` - `"ML"` - `"MT"` - `"MH"` - `"MQ"` - `"MR"` - `"MU"` - `"YT"` - `"MX"` - `"FM"` - `"MD"` - `"MC"` - `"MA"` - `"MZ"` - `"MM"` - `"NA"` - `"NP"` - `"NL"` - `"AN"` - `"AW"` - `"NZ"` - `"NI"` - `"NE"` - `"NO"` - `"MP"` - `"OM"` - `"PK"` - `"PW"` - `"PA"` - `"PG"` - `"PY"` - `"PE"` - `"PH"` - `"PL"` - `"PT"` - `"PR"` - `"QA"` - `"RE"` - `"RO"` - `"RU"` - `"RW"` - `"BL"` - `"KN"` - `"LC"` - `"MF"` - `"PM"` - `"VC"` - `"SA"` - `"SN"` - `"RS"` - `"ME"` - `"SL"` - `"SG"` - `"SK"` - `"SI"` - `"ZA"` - `"ES"` - `"LK"` - `"SE"` - `"SR"` - `"CH"` - `"TW"` - `"TZ"` - `"TH"` - `"TG"` - `"TT"` - `"TN"` - `"TR"` - `"TM"` - `"AE"` - `"TC"` - `"UG"` - `"UA"` - `"GB"` - `"US"` - `"PS"` - `"UY"` - `"UZ"` - `"VU"` - `"VE"` - `"VN"` - `"VI"` - `"WF"` - `"YE"` - `"ZM"` - `"ZW"` - `"JP"` - `"CA"` - `"MN"` - `"IR"` - `"KP"` - `"SD"` - `"SY"` - `"ZB"` |
| **ap_handoff**  string | Enable/disable AP handoff of clients to other APs .  Choices:   - `"enable"` - `"disable"` |
| **apcfg_profile**  string | AP local configuration profile name. Source wireless-controller.apcfg-profile.name. |
| **ble_profile**  string | Bluetooth Low Energy profile name. Source wireless-controller.ble-profile.name. |
| **comment**  string | Comment. |
| **console_login**  string | Enable/disable FortiAP console login access .  Choices:   - `"enable"` - `"disable"` |
| **control_message_offload**  list / elements=string | Enable/disable CAPWAP control message data channel offload.  Choices:   - `"ebp-frame"` - `"aeroscout-tag"` - `"ap-list"` - `"sta-list"` - `"sta-cap-list"` - `"stats"` - `"aeroscout-mu"` - `"sta-health"` - `"spectral-analysis"` |
| **deny_mac_list**  list / elements=dictionary | List of MAC addresses that are denied access to this WTP, FortiAP, or AP. |
| **id**  integer | ID. |
| **mac**  string | A WiFi device with this MAC address is denied access to this WTP, FortiAP or AP. |
| **dtls_in_kernel**  string | Enable/disable data channel DTLS in kernel.  Choices:   - `"enable"` - `"disable"` |
| **dtls_policy**  list / elements=string | WTP data channel DTLS policy .  Choices:   - `"clear-text"` - `"dtls-enabled"` - `"ipsec-vpn"` |
| **energy_efficient_ethernet**  string | Enable/disable use of energy efficient Ethernet on WTP.  Choices:   - `"enable"` - `"disable"` |
| **esl_ses_dongle**  dictionary | ESL SES-imagotag dongle configuration. |
| **apc_addr_type**  string | ESL SES-imagotag APC address type .  Choices:   - `"fqdn"` - `"ip"` |
| **apc_fqdn**  string | FQDN of ESL SES-imagotag Access Point Controller (APC). |
| **apc_ip**  string | IP address of ESL SES-imagotag Access Point Controller (APC). |
| **apc_port**  integer | Port of ESL SES-imagotag Access Point Controller (APC). |
| **coex_level**  string | ESL SES-imagotag dongle coexistence level .  Choices:   - `"none"` |
| **compliance_level**  string | Compliance levels for the ESL solution integration .  Choices:   - `"compliance-level-2"` |
| **esl_channel**  string | ESL SES-imagotag dongle channel .  Choices:   - `"-1"` - `"0"` - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` - `"6"` - `"7"` - `"8"` - `"9"` - `"10"` - `"127"` |
| **output_power**  string | ESL SES-imagotag dongle output power .  Choices:   - `"a"` - `"b"` - `"c"` - `"d"` - `"e"` - `"f"` - `"g"` - `"h"` |
| **scd_enable**  string | Enable/disable ESL SES-imagotag Serial Communication Daemon (SCD) .  Choices:   - `"enable"` - `"disable"` |
| **tls_cert_verification**  string | Enable/disable TLS certificate verification .  Choices:   - `"enable"` - `"disable"` |
| **tls_fqdn_verification**  string | Enable/disable TLS certificate verification .  Choices:   - `"enable"` - `"disable"` |
| **ext_info_enable**  string | Enable/disable station/VAP/radio extension information.  Choices:   - `"enable"` - `"disable"` |
| **frequency_handoff**  string | Enable/disable frequency handoff of clients to other channels .  Choices:   - `"enable"` - `"disable"` |
| **handoff_roaming**  string | Enable/disable client load balancing during roaming to avoid roaming delay .  Choices:   - `"enable"` - `"disable"` |
| **handoff_rssi**  integer | Minimum received signal strength indicator (RSSI) value for handoff (20 - 30). |
| **handoff_sta_thresh**  integer | Threshold value for AP handoff. |
| **indoor_outdoor_deployment**  string | Set to allow indoor/outdoor-only channels under regulatory rules .  Choices:   - `"platform-determined"` - `"outdoor"` - `"indoor"` |
| **ip_fragment_preventing**  list / elements=string | Method(s) by which IP fragmentation is prevented for control and data packets through CAPWAP tunnel .  Choices:   - `"tcp-mss-adjust"` - `"icmp-unreachable"` |
| **lan**  dictionary | WTP LAN port mapping. |
| **port1_mode**  string | LAN port 1 mode.  Choices:   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port1_ssid**  string | Bridge LAN port 1 to SSID. Source system.interface.name. |
| **port2_mode**  string | LAN port 2 mode.  Choices:   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port2_ssid**  string | Bridge LAN port 2 to SSID. Source system.interface.name. |
| **port3_mode**  string | LAN port 3 mode.  Choices:   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port3_ssid**  string | Bridge LAN port 3 to SSID. Source system.interface.name. |
| **port4_mode**  string | LAN port 4 mode.  Choices:   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port4_ssid**  string | Bridge LAN port 4 to SSID. Source system.interface.name. |
| **port5_mode**  string | LAN port 5 mode.  Choices:   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port5_ssid**  string | Bridge LAN port 5 to SSID. Source system.interface.name. |
| **port6_mode**  string | LAN port 6 mode.  Choices:   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port6_ssid**  string | Bridge LAN port 6 to SSID. Source system.interface.name. |
| **port7_mode**  string | LAN port 7 mode.  Choices:   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port7_ssid**  string | Bridge LAN port 7 to SSID. Source system.interface.name. |
| **port8_mode**  string | LAN port 8 mode.  Choices:   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port8_ssid**  string | Bridge LAN port 8 to SSID. Source system.interface.name. |
| **port_esl_mode**  string | ESL port mode.  Choices:   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port_esl_ssid**  string | Bridge ESL port to SSID. Source system.interface.name. |
| **port_mode**  string | LAN port mode.  Choices:   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port_ssid**  string | Bridge LAN port to SSID. Source system.interface.name. |
| **lbs**  dictionary | Set various location based service (LBS) options. |
| **aeroscout**  string | Enable/disable AeroScout Real Time Location Service (RTLS) support .  Choices:   - `"enable"` - `"disable"` |
| **aeroscout_ap_mac**  string | Use BSSID or board MAC address as AP MAC address in AeroScout AP messages .  Choices:   - `"bssid"` - `"board-mac"` |
| **aeroscout_mmu_report**  string | Enable/disable compounded AeroScout tag and MU report .  Choices:   - `"enable"` - `"disable"` |
| **aeroscout_mu**  string | Enable/disable AeroScout Mobile Unit (MU) support .  Choices:   - `"enable"` - `"disable"` |
| **aeroscout_mu_factor**  integer | AeroScout MU mode dilution factor . |
| **aeroscout_mu_timeout**  integer | AeroScout MU mode timeout (0 - 65535 sec). |
| **aeroscout_server_ip**  string | IP address of AeroScout server. |
| **aeroscout_server_port**  integer | AeroScout server UDP listening port. |
| **ekahau_blink_mode**  string | Enable/disable Ekahau blink mode (now known as AiRISTA Flow) to track and locate WiFi tags .  Choices:   - `"enable"` - `"disable"` |
| **ekahau_tag**  string | WiFi frame MAC address or WiFi Tag. |
| **erc_server_ip**  string | IP address of Ekahau RTLS Controller (ERC). |
| **erc_server_port**  integer | Ekahau RTLS Controller (ERC) UDP listening port. |
| **fortipresence**  string | Enable/disable FortiPresence to monitor the location and activity of WiFi clients even if they don”t connect to this WiFi network .  Choices:   - `"foreign"` - `"both"` - `"disable"` |
| **fortipresence_ble**  string | Enable/disable FortiPresence finding and reporting BLE devices.  Choices:   - `"enable"` - `"disable"` |
| **fortipresence_frequency**  integer | FortiPresence report transmit frequency (5 - 65535 sec). |
| **fortipresence_port**  integer | UDP listening port of FortiPresence server . |
| **fortipresence_project**  string | FortiPresence project name (max. 16 characters). |
| **fortipresence_rogue**  string | Enable/disable FortiPresence finding and reporting rogue APs.  Choices:   - `"enable"` - `"disable"` |
| **fortipresence_secret**  string | FortiPresence secret password (max. 16 characters). |
| **fortipresence_server**  string | IP address of FortiPresence server. |
| **fortipresence_server_addr_type**  string | FortiPresence server address type .  Choices:   - `"ipv4"` - `"fqdn"` |
| **fortipresence_server_fqdn**  string | FQDN of FortiPresence server. |
| **fortipresence_unassoc**  string | Enable/disable FortiPresence finding and reporting unassociated stations.  Choices:   - `"enable"` - `"disable"` |
| **station_locate**  string | Enable/disable client station locating services for all clients, whether associated or not .  Choices:   - `"enable"` - `"disable"` |
| **led_schedules**  list / elements=dictionary | Recurring firewall schedules for illuminating LEDs on the FortiAP. If led-state is enabled, LEDs will be visible when at least one of the schedules is valid. Separate multiple schedule names with a space. |
| **name**  string | Schedule name. Source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name. |
| **led_state**  string | Enable/disable use of LEDs on WTP .  Choices:   - `"enable"` - `"disable"` |
| **lldp**  string | Enable/disable Link Layer Discovery Protocol (LLDP) for the WTP, FortiAP, or AP .  Choices:   - `"enable"` - `"disable"` |
| **login_passwd**  string | Set the managed WTP, FortiAP, or AP”s administrator password. |
| **login_passwd_change**  string | Change or reset the administrator password of a managed WTP, FortiAP or AP (yes, default, or no).  Choices:   - `"yes"` - `"default"` - `"no"` |
| **max_clients**  integer | Maximum number of stations (STAs) supported by the WTP . |
| **name**  string / required | WTP (or FortiAP or AP) profile name. |
| **platform**  dictionary | WTP, FortiAP, or AP platform. |
| **ddscan**  string | Enable/disable use of one radio for dedicated full-band scanning to detect RF characterization and wireless threat management.  Choices:   - `"enable"` - `"disable"` |
| **mode**  string | Configure operation mode of 5G radios .  Choices:   - `"single-5G"` - `"dual-5G"` |
| **type**  string | WTP, FortiAP or AP platform type. There are built-in WTP profiles for all supported FortiAP models. You can select a built-in profile and customize it or create a new profile.  Choices:   - `"AP-11N"` - `"220B"` - `"210B"` - `"222B"` - `"112B"` - `"320B"` - `"11C"` - `"14C"` - `"223B"` - `"28C"` - `"320C"` - `"221C"` - `"25D"` - `"222C"` - `"224D"` - `"214B"` - `"21D"` - `"24D"` - `"112D"` - `"223C"` - `"321C"` - `"C220C"` - `"C225C"` - `"C23JD"` - `"C24JE"` - `"S321C"` - `"S322C"` - `"S323C"` - `"S311C"` - `"S313C"` - `"S321CR"` - `"S322CR"` - `"S323CR"` - `"S421E"` - `"S422E"` - `"S423E"` - `"421E"` - `"423E"` - `"221E"` - `"222E"` - `"223E"` - `"224E"` - `"231E"` - `"S221E"` - `"S223E"` - `"321E"` - `"431F"` - `"431FL"` - `"432F"` - `"432FR"` - `"433F"` - `"433FL"` - `"231F"` - `"231FL"` - `"234F"` - `"23JF"` - `"831F"` - `"231G"` - `"233G"` - `"431G"` - `"433G"` - `"U421E"` - `"U422EV"` - `"U423E"` - `"U221EV"` - `"U223EV"` - `"U24JEV"` - `"U321EV"` - `"U323EV"` - `"U431F"` - `"U433F"` - `"U231F"` - `"U234F"` - `"U432F"` - `"U231G"` - `"U441G"` |
| **poe_mode**  string | Set the WTP, FortiAP, or AP”s PoE mode.  Choices:   - `"auto"` - `"8023af"` - `"8023at"` - `"power-adapter"` - `"full"` - `"high"` - `"low"` |
| **radio_1**  dictionary | Configuration options for radio 1. |
| **airtime_fairness**  string | Enable/disable airtime fairness .  Choices:   - `"enable"` - `"disable"` |
| **amsdu**  string | Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients .  Choices:   - `"enable"` - `"disable"` |
| **ap_handoff**  string | Enable/disable AP handoff of clients to other APs .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_addr**  string | MAC address to monitor. |
| **ap_sniffer_bufsize**  integer | Sniffer buffer size (1 - 32 MB). |
| **ap_sniffer_chan**  integer | Channel on which to operate the sniffer . |
| **ap_sniffer_ctl**  string | Enable/disable sniffer on WiFi control frame .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_data**  string | Enable/disable sniffer on WiFi data frame .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_mgmt_beacon**  string | Enable/disable sniffer on WiFi management Beacon frames .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_mgmt_other**  string | Enable/disable sniffer on WiFi management other frames .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_mgmt_probe**  string | Enable/disable sniffer on WiFi management probe frames .  Choices:   - `"enable"` - `"disable"` |
| **arrp_profile**  string | Distributed Automatic Radio Resource Provisioning (DARRP) profile name to assign to the radio. Source wireless-controller .arrp-profile.name. |
| **auto_power_high**  integer | The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference .  Choices:   - `"enable"` - `"disable"` |
| **auto_power_low**  integer | The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_target**  string | Target of automatic transmit power adjustment in dBm (-95 to -20). |
| **band**  string | WiFi band that Radio 1 operates on.  Choices:   - `"802.11a"` - `"802.11b"` - `"802.11g"` - `"802.11n"` - `"802.11n-5G"` - `"802.11ac"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11ax-6G"` - `"802.11n,g-only"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n-5G-only"` - `"802.11ac,n-only"` - `"802.11ac-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-5G-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ax-only"` |
| **band_5g_type**  string | WiFi 5G band type.  Choices:   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth_admission_control**  string | Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. A request to join the wireless network is only allowed if the access point has enough bandwidth to support it.  Choices:   - `"enable"` - `"disable"` |
| **bandwidth_capacity**  integer | Maximum bandwidth capacity allowed (1 - 600000 Kbps). |
| **beacon_interval**  integer | Beacon interval. The time between beacon frames in milliseconds. Actual range of beacon interval depends on the AP platform type . |
| **bss_color**  integer | BSS color value for this 11ax radio (0 - 63, disable = 0). |
| **bss_color_mode**  string | BSS color mode for this 11ax radio .  Choices:   - `"auto"` - `"static"` |
| **call_admission_control**  string | Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. New VoIP calls are only accepted if there is enough bandwidth available to support them.  Choices:   - `"enable"` - `"disable"` |
| **call_capacity**  integer | Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60). |
| **channel**  list / elements=dictionary | Selected list of wireless radio channels. |
| **chan**  string | Channel number. |
| **channel_bonding**  string | Channel bandwidth: 160,80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.  Choices:   - `"160MHz"` - `"80MHz"` - `"40MHz"` - `"20MHz"` |
| **channel_utilization**  string | Enable/disable measuring channel utilization.  Choices:   - `"enable"` - `"disable"` |
| **coexistence**  string | Enable/disable allowing both HT20 and HT40 on the same radio .  Choices:   - `"enable"` - `"disable"` |
| **darrp**  string | Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel .  Choices:   - `"enable"` - `"disable"` |
| **drma**  string | Enable/disable dynamic radio mode assignment (DRMA) .  Choices:   - `"disable"` - `"enable"` |
| **drma_sensitivity**  string | Network Coverage Factor (NCF) percentage required to consider a radio as redundant .  Choices:   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | Delivery Traffic Indication Map (DTIM) period (1 - 255). Set higher to save battery life of WiFi client in power-save mode. |
| **frag_threshold**  integer | Maximum packet size that can be sent without fragmentation (800 - 2346 bytes). |
| **frequency_handoff**  string | Enable/disable frequency handoff of clients to other channels .  Choices:   - `"enable"` - `"disable"` |
| **iperf_protocol**  string | Iperf test protocol .  Choices:   - `"udp"` - `"tcp"` |
| **iperf_server_port**  integer | Iperf service port number. |
| **max_clients**  integer | Maximum number of stations (STAs) or WiFi clients supported by the radio. Range depends on the hardware. |
| **max_distance**  integer | Maximum expected distance between the AP and clients (0 - 54000 m). |
| **mode**  string | Mode of radio 1. Radio 1 can be disabled, configured as an access point, a rogue AP monitor, a sniffer, or a station.  Choices:   - `"disabled"` - `"ap"` - `"monitor"` - `"sniffer"` - `"sam"` |
| **power_level**  integer | Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100). |
| **power_mode**  string | Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP . This power takes into account both radio transmit power and antenna gain. Higher power level settings may be constrained by local regulatory requirements and AP capabilities.  Choices:   - `"dBm"` - `"percentage"` |
| **power_value**  integer | Radio EIRP power in dBm (1 - 33). |
| **powersave_optimize**  list / elements=string | Enable client power-saving features such as TIM, AC VO, and OBSS etc.  Choices:   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection_mode**  string | Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).  Choices:   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio_id**  integer | radio-id |
| **rts_threshold**  integer | Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes). |
| **sam_bssid**  string | BSSID for WiFi network. |
| **sam_captive_portal**  string | Enable/disable Captive Portal Authentication .  Choices:   - `"enable"` - `"disable"` |
| **sam_cwp_failure_string**  string | Failure identification on the page after an incorrect login. |
| **sam_cwp_match_string**  string | Identification string from the captive portal login form. |
| **sam_cwp_password**  string | Password for captive portal authentication. |
| **sam_cwp_success_string**  string | Success identification on the page after a successful login. |
| **sam_cwp_test_url**  string | Website the client is trying to access. |
| **sam_cwp_username**  string | Username for captive portal authentication. |
| **sam_password**  string | Passphrase for WiFi network connection. |
| **sam_report_intv**  integer | SAM report interval (sec), 0 for a one-time report. |
| **sam_security_type**  string | Select WiFi network security type .  Choices:   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam_server**  string | SAM test server IP address or domain name. |
| **sam_server_fqdn**  string | SAM test server domain name. |
| **sam_server_ip**  string | SAM test server IP address. |
| **sam_server_type**  string | Select SAM server type .  Choices:   - `"ip"` - `"fqdn"` |
| **sam_ssid**  string | SSID for WiFi network. |
| **sam_test**  string | Select SAM test type .  Choices:   - `"ping"` - `"iperf"` |
| **sam_username**  string | Username for WiFi network connection. |
| **set_80211d**  string | Enable/disable 802.11d countryie.  Choices:   - `"enable"` - `"disable"` |
| **short_guard_interval**  string | Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.  Choices:   - `"enable"` - `"disable"` |
| **spectrum_analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  Choices:   - `"enable"` - `"scan-only"` - `"disable"` |
| **transmit_optimize**  list / elements=string | Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default.  Choices:   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap_all**  string | Configure method for assigning SSIDs to this FortiAP .  Choices:   - `"tunnel"` - `"bridge"` - `"manual"` - `"enable"` - `"disable"` |
| **vaps**  list / elements=dictionary | Manually selected list of Virtual Access Points (VAPs). |
| **name**  string | Virtual Access Point (VAP) name. Source wireless-controller.vap-group.name system.interface.name. |
| **wids_profile**  string | Wireless Intrusion Detection System (WIDS) profile name to assign to the radio. Source wireless-controller.wids-profile.name. |
| **zero_wait_dfs**  string | Enable/disable zero wait DFS on radio .  Choices:   - `"enable"` - `"disable"` |
| **radio_2**  dictionary | Configuration options for radio 2. |
| **airtime_fairness**  string | Enable/disable airtime fairness .  Choices:   - `"enable"` - `"disable"` |
| **amsdu**  string | Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients .  Choices:   - `"enable"` - `"disable"` |
| **ap_handoff**  string | Enable/disable AP handoff of clients to other APs .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_addr**  string | MAC address to monitor. |
| **ap_sniffer_bufsize**  integer | Sniffer buffer size (1 - 32 MB). |
| **ap_sniffer_chan**  integer | Channel on which to operate the sniffer . |
| **ap_sniffer_ctl**  string | Enable/disable sniffer on WiFi control frame .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_data**  string | Enable/disable sniffer on WiFi data frame .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_mgmt_beacon**  string | Enable/disable sniffer on WiFi management Beacon frames .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_mgmt_other**  string | Enable/disable sniffer on WiFi management other frames .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_mgmt_probe**  string | Enable/disable sniffer on WiFi management probe frames .  Choices:   - `"enable"` - `"disable"` |
| **arrp_profile**  string | Distributed Automatic Radio Resource Provisioning (DARRP) profile name to assign to the radio. Source wireless-controller .arrp-profile.name. |
| **auto_power_high**  integer | The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference .  Choices:   - `"enable"` - `"disable"` |
| **auto_power_low**  integer | The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_target**  string | Target of automatic transmit power adjustment in dBm (-95 to -20). |
| **band**  string | WiFi band that Radio 2 operates on.  Choices:   - `"802.11a"` - `"802.11b"` - `"802.11g"` - `"802.11n"` - `"802.11n-5G"` - `"802.11ac"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11ax-6G"` - `"802.11n,g-only"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n-5G-only"` - `"802.11ac,n-only"` - `"802.11ac-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-5G-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ax-only"` |
| **band_5g_type**  string | WiFi 5G band type.  Choices:   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth_admission_control**  string | Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. A request to join the wireless network is only allowed if the access point has enough bandwidth to support it.  Choices:   - `"enable"` - `"disable"` |
| **bandwidth_capacity**  integer | Maximum bandwidth capacity allowed (1 - 600000 Kbps). |
| **beacon_interval**  integer | Beacon interval. The time between beacon frames in milliseconds. Actual range of beacon interval depends on the AP platform type . |
| **bss_color**  integer | BSS color value for this 11ax radio (0 - 63, disable = 0). |
| **bss_color_mode**  string | BSS color mode for this 11ax radio .  Choices:   - `"auto"` - `"static"` |
| **call_admission_control**  string | Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. New VoIP calls are only accepted if there is enough bandwidth available to support them.  Choices:   - `"enable"` - `"disable"` |
| **call_capacity**  integer | Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60). |
| **channel**  list / elements=dictionary | Selected list of wireless radio channels. |
| **chan**  string | Channel number. |
| **channel_bonding**  string | Channel bandwidth: 160,80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.  Choices:   - `"160MHz"` - `"80MHz"` - `"40MHz"` - `"20MHz"` |
| **channel_utilization**  string | Enable/disable measuring channel utilization.  Choices:   - `"enable"` - `"disable"` |
| **coexistence**  string | Enable/disable allowing both HT20 and HT40 on the same radio .  Choices:   - `"enable"` - `"disable"` |
| **darrp**  string | Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel .  Choices:   - `"enable"` - `"disable"` |
| **drma**  string | Enable/disable dynamic radio mode assignment (DRMA) .  Choices:   - `"disable"` - `"enable"` |
| **drma_sensitivity**  string | Network Coverage Factor (NCF) percentage required to consider a radio as redundant .  Choices:   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | Delivery Traffic Indication Map (DTIM) period (1 - 255). Set higher to save battery life of WiFi client in power-save mode. |
| **frag_threshold**  integer | Maximum packet size that can be sent without fragmentation (800 - 2346 bytes). |
| **frequency_handoff**  string | Enable/disable frequency handoff of clients to other channels .  Choices:   - `"enable"` - `"disable"` |
| **iperf_protocol**  string | Iperf test protocol .  Choices:   - `"udp"` - `"tcp"` |
| **iperf_server_port**  integer | Iperf service port number. |
| **max_clients**  integer | Maximum number of stations (STAs) or WiFi clients supported by the radio. Range depends on the hardware. |
| **max_distance**  integer | Maximum expected distance between the AP and clients (0 - 54000 m). |
| **mode**  string | Mode of radio 2. Radio 2 can be disabled, configured as an access point, a rogue AP monitor, a sniffer, or a station.  Choices:   - `"disabled"` - `"ap"` - `"monitor"` - `"sniffer"` - `"sam"` |
| **power_level**  integer | Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100). |
| **power_mode**  string | Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP . This power takes into account both radio transmit power and antenna gain. Higher power level settings may be constrained by local regulatory requirements and AP capabilities.  Choices:   - `"dBm"` - `"percentage"` |
| **power_value**  integer | Radio EIRP power in dBm (1 - 33). |
| **powersave_optimize**  list / elements=string | Enable client power-saving features such as TIM, AC VO, and OBSS etc.  Choices:   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection_mode**  string | Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).  Choices:   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio_id**  integer | radio-id |
| **rts_threshold**  integer | Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes). |
| **sam_bssid**  string | BSSID for WiFi network. |
| **sam_captive_portal**  string | Enable/disable Captive Portal Authentication .  Choices:   - `"enable"` - `"disable"` |
| **sam_cwp_failure_string**  string | Failure identification on the page after an incorrect login. |
| **sam_cwp_match_string**  string | Identification string from the captive portal login form. |
| **sam_cwp_password**  string | Password for captive portal authentication. |
| **sam_cwp_success_string**  string | Success identification on the page after a successful login. |
| **sam_cwp_test_url**  string | Website the client is trying to access. |
| **sam_cwp_username**  string | Username for captive portal authentication. |
| **sam_password**  string | Passphrase for WiFi network connection. |
| **sam_report_intv**  integer | SAM report interval (sec), 0 for a one-time report. |
| **sam_security_type**  string | Select WiFi network security type .  Choices:   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam_server**  string | SAM test server IP address or domain name. |
| **sam_server_fqdn**  string | SAM test server domain name. |
| **sam_server_ip**  string | SAM test server IP address. |
| **sam_server_type**  string | Select SAM server type .  Choices:   - `"ip"` - `"fqdn"` |
| **sam_ssid**  string | SSID for WiFi network. |
| **sam_test**  string | Select SAM test type .  Choices:   - `"ping"` - `"iperf"` |
| **sam_username**  string | Username for WiFi network connection. |
| **set_80211d**  string | Enable/disable 802.11d countryie.  Choices:   - `"enable"` - `"disable"` |
| **short_guard_interval**  string | Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.  Choices:   - `"enable"` - `"disable"` |
| **spectrum_analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  Choices:   - `"enable"` - `"scan-only"` - `"disable"` |
| **transmit_optimize**  list / elements=string | Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default.  Choices:   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap_all**  string | Configure method for assigning SSIDs to this FortiAP .  Choices:   - `"tunnel"` - `"bridge"` - `"manual"` - `"enable"` - `"disable"` |
| **vaps**  list / elements=dictionary | Manually selected list of Virtual Access Points (VAPs). |
| **name**  string | Virtual Access Point (VAP) name. Source wireless-controller.vap-group.name system.interface.name. |
| **wids_profile**  string | Wireless Intrusion Detection System (WIDS) profile name to assign to the radio. Source wireless-controller.wids-profile.name. |
| **zero_wait_dfs**  string | Enable/disable zero wait DFS on radio .  Choices:   - `"enable"` - `"disable"` |
| **radio_3**  dictionary | Configuration options for radio 3. |
| **airtime_fairness**  string | Enable/disable airtime fairness .  Choices:   - `"enable"` - `"disable"` |
| **amsdu**  string | Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients .  Choices:   - `"enable"` - `"disable"` |
| **ap_handoff**  string | Enable/disable AP handoff of clients to other APs .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_addr**  string | MAC address to monitor. |
| **ap_sniffer_bufsize**  integer | Sniffer buffer size (1 - 32 MB). |
| **ap_sniffer_chan**  integer | Channel on which to operate the sniffer . |
| **ap_sniffer_ctl**  string | Enable/disable sniffer on WiFi control frame .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_data**  string | Enable/disable sniffer on WiFi data frame .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_mgmt_beacon**  string | Enable/disable sniffer on WiFi management Beacon frames .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_mgmt_other**  string | Enable/disable sniffer on WiFi management other frames .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_mgmt_probe**  string | Enable/disable sniffer on WiFi management probe frames .  Choices:   - `"enable"` - `"disable"` |
| **arrp_profile**  string | Distributed Automatic Radio Resource Provisioning (DARRP) profile name to assign to the radio. Source wireless-controller .arrp-profile.name. |
| **auto_power_high**  integer | The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference .  Choices:   - `"enable"` - `"disable"` |
| **auto_power_low**  integer | The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_target**  string | Target of automatic transmit power adjustment in dBm (-95 to -20). |
| **band**  string | WiFi band that Radio 3 operates on.  Choices:   - `"802.11a"` - `"802.11b"` - `"802.11g"` - `"802.11n"` - `"802.11n-5G"` - `"802.11ac"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11ax-6G"` - `"802.11n,g-only"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n-5G-only"` - `"802.11ac,n-only"` - `"802.11ac-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-5G-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ax-only"` |
| **band_5g_type**  string | WiFi 5G band type.  Choices:   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth_admission_control**  string | Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. A request to join the wireless network is only allowed if the access point has enough bandwidth to support it.  Choices:   - `"enable"` - `"disable"` |
| **bandwidth_capacity**  integer | Maximum bandwidth capacity allowed (1 - 600000 Kbps). |
| **beacon_interval**  integer | Beacon interval. The time between beacon frames in milliseconds. Actual range of beacon interval depends on the AP platform type . |
| **bss_color**  integer | BSS color value for this 11ax radio (0 - 63, disable = 0). |
| **bss_color_mode**  string | BSS color mode for this 11ax radio .  Choices:   - `"auto"` - `"static"` |
| **call_admission_control**  string | Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. New VoIP calls are only accepted if there is enough bandwidth available to support them.  Choices:   - `"enable"` - `"disable"` |
| **call_capacity**  integer | Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60). |
| **channel**  list / elements=dictionary | Selected list of wireless radio channels. |
| **chan**  string | Channel number. |
| **channel_bonding**  string | Channel bandwidth: 160,80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.  Choices:   - `"160MHz"` - `"80MHz"` - `"40MHz"` - `"20MHz"` |
| **channel_utilization**  string | Enable/disable measuring channel utilization.  Choices:   - `"enable"` - `"disable"` |
| **coexistence**  string | Enable/disable allowing both HT20 and HT40 on the same radio .  Choices:   - `"enable"` - `"disable"` |
| **darrp**  string | Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel .  Choices:   - `"enable"` - `"disable"` |
| **drma**  string | Enable/disable dynamic radio mode assignment (DRMA) .  Choices:   - `"disable"` - `"enable"` |
| **drma_sensitivity**  string | Network Coverage Factor (NCF) percentage required to consider a radio as redundant .  Choices:   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | Delivery Traffic Indication Map (DTIM) period (1 - 255). Set higher to save battery life of WiFi client in power-save mode. |
| **frag_threshold**  integer | Maximum packet size that can be sent without fragmentation (800 - 2346 bytes). |
| **frequency_handoff**  string | Enable/disable frequency handoff of clients to other channels .  Choices:   - `"enable"` - `"disable"` |
| **iperf_protocol**  string | Iperf test protocol .  Choices:   - `"udp"` - `"tcp"` |
| **iperf_server_port**  integer | Iperf service port number. |
| **max_clients**  integer | Maximum number of stations (STAs) or WiFi clients supported by the radio. Range depends on the hardware. |
| **max_distance**  integer | Maximum expected distance between the AP and clients (0 - 54000 m). |
| **mode**  string | Mode of radio 3. Radio 3 can be disabled, configured as an access point, a rogue AP monitor, a sniffer, or a station.  Choices:   - `"disabled"` - `"ap"` - `"monitor"` - `"sniffer"` - `"sam"` |
| **power_level**  integer | Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100). |
| **power_mode**  string | Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP . This power takes into account both radio transmit power and antenna gain. Higher power level settings may be constrained by local regulatory requirements and AP capabilities.  Choices:   - `"dBm"` - `"percentage"` |
| **power_value**  integer | Radio EIRP power in dBm (1 - 33). |
| **powersave_optimize**  list / elements=string | Enable client power-saving features such as TIM, AC VO, and OBSS etc.  Choices:   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection_mode**  string | Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).  Choices:   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **radio_id**  integer | radio-id |
| **rts_threshold**  integer | Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes). |
| **sam_bssid**  string | BSSID for WiFi network. |
| **sam_captive_portal**  string | Enable/disable Captive Portal Authentication .  Choices:   - `"enable"` - `"disable"` |
| **sam_cwp_failure_string**  string | Failure identification on the page after an incorrect login. |
| **sam_cwp_match_string**  string | Identification string from the captive portal login form. |
| **sam_cwp_password**  string | Password for captive portal authentication. |
| **sam_cwp_success_string**  string | Success identification on the page after a successful login. |
| **sam_cwp_test_url**  string | Website the client is trying to access. |
| **sam_cwp_username**  string | Username for captive portal authentication. |
| **sam_password**  string | Passphrase for WiFi network connection. |
| **sam_report_intv**  integer | SAM report interval (sec), 0 for a one-time report. |
| **sam_security_type**  string | Select WiFi network security type .  Choices:   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam_server**  string | SAM test server IP address or domain name. |
| **sam_server_fqdn**  string | SAM test server domain name. |
| **sam_server_ip**  string | SAM test server IP address. |
| **sam_server_type**  string | Select SAM server type .  Choices:   - `"ip"` - `"fqdn"` |
| **sam_ssid**  string | SSID for WiFi network. |
| **sam_test**  string | Select SAM test type .  Choices:   - `"ping"` - `"iperf"` |
| **sam_username**  string | Username for WiFi network connection. |
| **set_80211d**  string | Enable/disable 802.11d countryie.  Choices:   - `"enable"` - `"disable"` |
| **short_guard_interval**  string | Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.  Choices:   - `"enable"` - `"disable"` |
| **spectrum_analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  Choices:   - `"enable"` - `"scan-only"` - `"disable"` |
| **transmit_optimize**  list / elements=string | Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default.  Choices:   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap_all**  string | Configure method for assigning SSIDs to this FortiAP .  Choices:   - `"tunnel"` - `"bridge"` - `"manual"` - `"enable"` - `"disable"` |
| **vaps**  list / elements=dictionary | Manually selected list of Virtual Access Points (VAPs). |
| **name**  string | Virtual Access Point (VAP) name. Source wireless-controller.vap-group.name system.interface.name. |
| **wids_profile**  string | Wireless Intrusion Detection System (WIDS) profile name to assign to the radio. Source wireless-controller.wids-profile.name. |
| **zero_wait_dfs**  string | Enable/disable zero wait DFS on radio .  Choices:   - `"enable"` - `"disable"` |
| **radio_4**  dictionary | Configuration options for radio 4. |
| **airtime_fairness**  string | Enable/disable airtime fairness .  Choices:   - `"enable"` - `"disable"` |
| **amsdu**  string | Enable/disable 802.11n AMSDU support. AMSDU can improve performance if supported by your WiFi clients .  Choices:   - `"enable"` - `"disable"` |
| **ap_handoff**  string | Enable/disable AP handoff of clients to other APs .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_addr**  string | MAC address to monitor. |
| **ap_sniffer_bufsize**  integer | Sniffer buffer size (1 - 32 MB). |
| **ap_sniffer_chan**  integer | Channel on which to operate the sniffer . |
| **ap_sniffer_ctl**  string | Enable/disable sniffer on WiFi control frame .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_data**  string | Enable/disable sniffer on WiFi data frame .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_mgmt_beacon**  string | Enable/disable sniffer on WiFi management Beacon frames .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_mgmt_other**  string | Enable/disable sniffer on WiFi management other frames .  Choices:   - `"enable"` - `"disable"` |
| **ap_sniffer_mgmt_probe**  string | Enable/disable sniffer on WiFi management probe frames .  Choices:   - `"enable"` - `"disable"` |
| **arrp_profile**  string | Distributed Automatic Radio Resource Provisioning (DARRP) profile name to assign to the radio. Source wireless-controller .arrp-profile.name. |
| **auto_power_high**  integer | The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference .  Choices:   - `"enable"` - `"disable"` |
| **auto_power_low**  integer | The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_target**  string | Target of automatic transmit power adjustment in dBm (-95 to -20). |
| **band**  string | WiFi band that Radio 3 operates on.  Choices:   - `"802.11a"` - `"802.11b"` - `"802.11g"` - `"802.11n"` - `"802.11n-5G"` - `"802.11ac"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11ax-6G"` - `"802.11n,g-only"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n-5G-only"` - `"802.11ac,n-only"` - `"802.11ac-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-5G-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ax-only"` |
| **band_5g_type**  string | WiFi 5G band type.  Choices:   - `"5g-full"` - `"5g-high"` - `"5g-low"` |
| **bandwidth_admission_control**  string | Enable/disable WiFi multimedia (WMM) bandwidth admission control to optimize WiFi bandwidth use. A request to join the wireless network is only allowed if the access point has enough bandwidth to support it.  Choices:   - `"enable"` - `"disable"` |
| **bandwidth_capacity**  integer | Maximum bandwidth capacity allowed (1 - 600000 Kbps). |
| **beacon_interval**  integer | Beacon interval. The time between beacon frames in milliseconds. Actual range of beacon interval depends on the AP platform type . |
| **bss_color**  integer | BSS color value for this 11ax radio (0 - 63, disable = 0). |
| **bss_color_mode**  string | BSS color mode for this 11ax radio .  Choices:   - `"auto"` - `"static"` |
| **call_admission_control**  string | Enable/disable WiFi multimedia (WMM) call admission control to optimize WiFi bandwidth use for VoIP calls. New VoIP calls are only accepted if there is enough bandwidth available to support them.  Choices:   - `"enable"` - `"disable"` |
| **call_capacity**  integer | Maximum number of Voice over WLAN (VoWLAN) phones supported by the radio (0 - 60). |
| **channel**  list / elements=dictionary | Selected list of wireless radio channels. |
| **chan**  string | Channel number. |
| **channel_bonding**  string | Channel bandwidth: 160,80, 40, or 20MHz. Channels may use both 20 and 40 by enabling coexistence.  Choices:   - `"160MHz"` - `"80MHz"` - `"40MHz"` - `"20MHz"` |
| **channel_utilization**  string | Enable/disable measuring channel utilization.  Choices:   - `"enable"` - `"disable"` |
| **coexistence**  string | Enable/disable allowing both HT20 and HT40 on the same radio .  Choices:   - `"enable"` - `"disable"` |
| **darrp**  string | Enable/disable Distributed Automatic Radio Resource Provisioning (DARRP) to make sure the radio is always using the most optimal channel .  Choices:   - `"enable"` - `"disable"` |
| **drma**  string | Enable/disable dynamic radio mode assignment (DRMA) .  Choices:   - `"disable"` - `"enable"` |
| **drma_sensitivity**  string | Network Coverage Factor (NCF) percentage required to consider a radio as redundant .  Choices:   - `"low"` - `"medium"` - `"high"` |
| **dtim**  integer | Delivery Traffic Indication Map (DTIM) period (1 - 255). Set higher to save battery life of WiFi client in power-save mode. |
| **frag_threshold**  integer | Maximum packet size that can be sent without fragmentation (800 - 2346 bytes). |
| **frequency_handoff**  string | Enable/disable frequency handoff of clients to other channels .  Choices:   - `"enable"` - `"disable"` |
| **iperf_protocol**  string | Iperf test protocol .  Choices:   - `"udp"` - `"tcp"` |
| **iperf_server_port**  integer | Iperf service port number. |
| **max_clients**  integer | Maximum number of stations (STAs) or WiFi clients supported by the radio. Range depends on the hardware. |
| **max_distance**  integer | Maximum expected distance between the AP and clients (0 - 54000 m). |
| **mode**  string | Mode of radio 3. Radio 3 can be disabled, configured as an access point, a rogue AP monitor, a sniffer, or a station.  Choices:   - `"disabled"` - `"ap"` - `"monitor"` - `"sniffer"` - `"sam"` |
| **power_level**  integer | Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100). |
| **power_mode**  string | Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP . This power takes into account both radio transmit power and antenna gain. Higher power level settings may be constrained by local regulatory requirements and AP capabilities.  Choices:   - `"dBm"` - `"percentage"` |
| **power_value**  integer | Radio EIRP power in dBm (1 - 33). |
| **powersave_optimize**  list / elements=string | Enable client power-saving features such as TIM, AC VO, and OBSS etc.  Choices:   - `"tim"` - `"ac-vo"` - `"no-obss-scan"` - `"no-11b-rate"` - `"client-rate-follow"` |
| **protection_mode**  string | Enable/disable 802.11g protection modes to support backwards compatibility with older clients (rtscts, ctsonly, disable).  Choices:   - `"rtscts"` - `"ctsonly"` - `"disable"` |
| **rts_threshold**  integer | Maximum packet size for RTS transmissions, specifying the maximum size of a data packet before RTS/CTS (256 - 2346 bytes). |
| **sam_bssid**  string | BSSID for WiFi network. |
| **sam_captive_portal**  string | Enable/disable Captive Portal Authentication .  Choices:   - `"enable"` - `"disable"` |
| **sam_cwp_failure_string**  string | Failure identification on the page after an incorrect login. |
| **sam_cwp_match_string**  string | Identification string from the captive portal login form. |
| **sam_cwp_password**  string | Password for captive portal authentication. |
| **sam_cwp_success_string**  string | Success identification on the page after a successful login. |
| **sam_cwp_test_url**  string | Website the client is trying to access. |
| **sam_cwp_username**  string | Username for captive portal authentication. |
| **sam_password**  string | Passphrase for WiFi network connection. |
| **sam_report_intv**  integer | SAM report interval (sec), 0 for a one-time report. |
| **sam_security_type**  string | Select WiFi network security type .  Choices:   - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` |
| **sam_server**  string | SAM test server IP address or domain name. |
| **sam_server_fqdn**  string | SAM test server domain name. |
| **sam_server_ip**  string | SAM test server IP address. |
| **sam_server_type**  string | Select SAM server type .  Choices:   - `"ip"` - `"fqdn"` |
| **sam_ssid**  string | SSID for WiFi network. |
| **sam_test**  string | Select SAM test type .  Choices:   - `"ping"` - `"iperf"` |
| **sam_username**  string | Username for WiFi network connection. |
| **set_80211d**  string | Enable/disable 802.11d countryie.  Choices:   - `"enable"` - `"disable"` |
| **short_guard_interval**  string | Use either the short guard interval (Short GI) of 400 ns or the long guard interval (Long GI) of 800 ns.  Choices:   - `"enable"` - `"disable"` |
| **spectrum_analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  Choices:   - `"enable"` - `"scan-only"` - `"disable"` |
| **transmit_optimize**  list / elements=string | Packet transmission optimization options including power saving, aggregation limiting, retry limiting, etc. All are enabled by default.  Choices:   - `"disable"` - `"power-save"` - `"aggr-limit"` - `"retry-limit"` - `"send-bar"` |
| **vap_all**  string | Configure method for assigning SSIDs to this FortiAP .  Choices:   - `"tunnel"` - `"bridge"` - `"manual"` - `"enable"` - `"disable"` |
| **vaps**  list / elements=dictionary | Manually selected list of Virtual Access Points (VAPs). |
| **name**  string | Virtual Access Point (VAP) name. Source wireless-controller.vap-group.name system.interface.name. |
| **wids_profile**  string | Wireless Intrusion Detection System (WIDS) profile name to assign to the radio. Source wireless-controller.wids-profile.name. |
| **zero_wait_dfs**  string | Enable/disable zero wait DFS on radio .  Choices:   - `"enable"` - `"disable"` |
| **split_tunneling_acl**  list / elements=dictionary | Split tunneling ACL filter list. |
| **dest_ip**  string | Destination IP and mask for the split-tunneling subnet. |
| **id**  integer | ID. |
| **split_tunneling_acl_local_ap_subnet**  string | Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL .  Choices:   - `"enable"` - `"disable"` |
| **split_tunneling_acl_path**  string | Split tunneling ACL path is local/tunnel.  Choices:   - `"tunnel"` - `"local"` |
| **syslog_profile**  string | System log server configuration profile name. Source wireless-controller.syslog-profile.name. |
| **tun_mtu_downlink**  integer | The MTU of downlink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of FortiAP; ). |
| **tun_mtu_uplink**  integer | The maximum transmission unit (MTU) of uplink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of FortiAP; ). |
| **wan_port_auth**  string | Set WAN port authentication mode .  Choices:   - `"none"` - `"802.1x"` |
| **wan_port_auth_methods**  string | WAN port 802.1x supplicant EAP methods .  Choices:   - `"all"` - `"EAP-FAST"` - `"EAP-TLS"` - `"EAP-PEAP"` |
| **wan_port_auth_password**  string | Set WAN port 802.1x supplicant password. |
| **wan_port_auth_usrname**  string | Set WAN port 802.1x supplicant user name. |
| **wan_port_mode**  string | Enable/disable using a WAN port as a LAN port.  Choices:   - `"wan-lan"` - `"wan-only"` |

## [Notes](fortios_wireless_controller_wtp_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_wtp_profile_module.md#id5)

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
  - name: Configure WTP profiles or FortiAP profiles that define radio settings for manageable FortiAP platforms.
    fortios_wireless_controller_wtp_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_wtp_profile:
        allowaccess: "https"
        ap_country: "--"
        ap_handoff: "enable"
        apcfg_profile: "<your_own_value> (source wireless-controller.apcfg-profile.name)"
        ble_profile: "<your_own_value> (source wireless-controller.ble-profile.name)"
        comment: "Comment."
        console_login: "enable"
        control_message_offload: "ebp-frame"
        deny_mac_list:
         -
            id:  "12"
            mac: "<your_own_value>"
        dtls_in_kernel: "enable"
        dtls_policy: "clear-text"
        energy_efficient_ethernet: "enable"
        esl_ses_dongle:
            apc_addr_type: "fqdn"
            apc_fqdn: "<your_own_value>"
            apc_ip: "<your_own_value>"
            apc_port: "0"
            coex_level: "none"
            compliance_level: "compliance-level-2"
            esl_channel: "-1"
            output_power: "a"
            scd_enable: "enable"
            tls_cert_verification: "enable"
            tls_fqdn_verification: "enable"
        ext_info_enable: "enable"
        frequency_handoff: "enable"
        handoff_roaming: "enable"
        handoff_rssi: "25"
        handoff_sta_thresh: "0"
        indoor_outdoor_deployment: "platform-determined"
        ip_fragment_preventing: "tcp-mss-adjust"
        lan:
            port_esl_mode: "offline"
            port_esl_ssid: "<your_own_value> (source system.interface.name)"
            port_mode: "offline"
            port_ssid: "<your_own_value> (source system.interface.name)"
            port1_mode: "offline"
            port1_ssid: "<your_own_value> (source system.interface.name)"
            port2_mode: "offline"
            port2_ssid: "<your_own_value> (source system.interface.name)"
            port3_mode: "offline"
            port3_ssid: "<your_own_value> (source system.interface.name)"
            port4_mode: "offline"
            port4_ssid: "<your_own_value> (source system.interface.name)"
            port5_mode: "offline"
            port5_ssid: "<your_own_value> (source system.interface.name)"
            port6_mode: "offline"
            port6_ssid: "<your_own_value> (source system.interface.name)"
            port7_mode: "offline"
            port7_ssid: "<your_own_value> (source system.interface.name)"
            port8_mode: "offline"
            port8_ssid: "<your_own_value> (source system.interface.name)"
        lbs:
            aeroscout: "enable"
            aeroscout_ap_mac: "bssid"
            aeroscout_mmu_report: "enable"
            aeroscout_mu: "enable"
            aeroscout_mu_factor: "20"
            aeroscout_mu_timeout: "5"
            aeroscout_server_ip: "<your_own_value>"
            aeroscout_server_port: "0"
            ekahau_blink_mode: "enable"
            ekahau_tag: "<your_own_value>"
            erc_server_ip: "<your_own_value>"
            erc_server_port: "8569"
            fortipresence: "foreign"
            fortipresence_ble: "enable"
            fortipresence_frequency: "30"
            fortipresence_port: "3000"
            fortipresence_project: "<your_own_value>"
            fortipresence_rogue: "enable"
            fortipresence_secret: "<your_own_value>"
            fortipresence_server: "<your_own_value>"
            fortipresence_server_addr_type: "ipv4"
            fortipresence_server_fqdn: "<your_own_value>"
            fortipresence_unassoc: "enable"
            station_locate: "enable"
        led_schedules:
         -
            name: "default_name_83 (source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name)"
        led_state: "enable"
        lldp: "enable"
        login_passwd: "<your_own_value>"
        login_passwd_change: "yes"
        max_clients: "0"
        name: "default_name_89"
        platform:
            ddscan: "enable"
            mode: "single-5G"
            type: "AP-11N"
        poe_mode: "auto"
        radio_1:
            airtime_fairness: "enable"
            amsdu: "enable"
            ap_handoff: "enable"
            ap_sniffer_addr: "<your_own_value>"
            ap_sniffer_bufsize: "16"
            ap_sniffer_chan: "36"
            ap_sniffer_ctl: "enable"
            ap_sniffer_data: "enable"
            ap_sniffer_mgmt_beacon: "enable"
            ap_sniffer_mgmt_other: "enable"
            ap_sniffer_mgmt_probe: "enable"
            arrp_profile: "<your_own_value> (source wireless-controller.arrp-profile.name)"
            auto_power_high: "17"
            auto_power_level: "enable"
            auto_power_low: "10"
            auto_power_target: "<your_own_value>"
            band: "802.11a"
            band_5g_type: "5g-full"
            bandwidth_admission_control: "enable"
            bandwidth_capacity: "2000"
            beacon_interval: "100"
            bss_color: "0"
            bss_color_mode: "auto"
            call_admission_control: "enable"
            call_capacity: "10"
            channel:
             -
                chan: "<your_own_value>"
            channel_bonding: "160MHz"
            channel_utilization: "enable"
            coexistence: "enable"
            darrp: "enable"
            drma: "disable"
            drma_sensitivity: "low"
            dtim: "1"
            frag_threshold: "2346"
            frequency_handoff: "enable"
            iperf_protocol: "udp"
            iperf_server_port: "5001"
            max_clients: "0"
            max_distance: "0"
            mode: "disabled"
            power_level: "100"
            power_mode: "dBm"
            power_value: "27"
            powersave_optimize: "tim"
            protection_mode: "rtscts"
            radio_id: "2"
            rts_threshold: "2346"
            sam_bssid: "<your_own_value>"
            sam_captive_portal: "enable"
            sam_cwp_failure_string: "<your_own_value>"
            sam_cwp_match_string: "<your_own_value>"
            sam_cwp_password: "<your_own_value>"
            sam_cwp_success_string: "<your_own_value>"
            sam_cwp_test_url: "<your_own_value>"
            sam_cwp_username: "<your_own_value>"
            sam_password: "<your_own_value>"
            sam_report_intv: "0"
            sam_security_type: "open"
            sam_server: "<your_own_value>"
            sam_server_fqdn: "<your_own_value>"
            sam_server_ip: "<your_own_value>"
            sam_server_type: "ip"
            sam_ssid: "<your_own_value>"
            sam_test: "ping"
            sam_username: "<your_own_value>"
            set_80211d: "enable"
            short_guard_interval: "enable"
            spectrum_analysis: "enable"
            transmit_optimize: "disable"
            vap_all: "tunnel"
            vaps:
             -
                name: "default_name_168 (source wireless-controller.vap-group.name system.interface.name)"
            wids_profile: "<your_own_value> (source wireless-controller.wids-profile.name)"
            zero_wait_dfs: "enable"
        radio_2:
            airtime_fairness: "enable"
            amsdu: "enable"
            ap_handoff: "enable"
            ap_sniffer_addr: "<your_own_value>"
            ap_sniffer_bufsize: "16"
            ap_sniffer_chan: "6"
            ap_sniffer_ctl: "enable"
            ap_sniffer_data: "enable"
            ap_sniffer_mgmt_beacon: "enable"
            ap_sniffer_mgmt_other: "enable"
            ap_sniffer_mgmt_probe: "enable"
            arrp_profile: "<your_own_value> (source wireless-controller.arrp-profile.name)"
            auto_power_high: "17"
            auto_power_level: "enable"
            auto_power_low: "10"
            auto_power_target: "<your_own_value>"
            band: "802.11a"
            band_5g_type: "5g-full"
            bandwidth_admission_control: "enable"
            bandwidth_capacity: "2000"
            beacon_interval: "100"
            bss_color: "0"
            bss_color_mode: "auto"
            call_admission_control: "enable"
            call_capacity: "10"
            channel:
             -
                chan: "<your_own_value>"
            channel_bonding: "160MHz"
            channel_utilization: "enable"
            coexistence: "enable"
            darrp: "enable"
            drma: "disable"
            drma_sensitivity: "low"
            dtim: "1"
            frag_threshold: "2346"
            frequency_handoff: "enable"
            iperf_protocol: "udp"
            iperf_server_port: "5001"
            max_clients: "0"
            max_distance: "0"
            mode: "disabled"
            power_level: "100"
            power_mode: "dBm"
            power_value: "27"
            powersave_optimize: "tim"
            protection_mode: "rtscts"
            radio_id: "2"
            rts_threshold: "2346"
            sam_bssid: "<your_own_value>"
            sam_captive_portal: "enable"
            sam_cwp_failure_string: "<your_own_value>"
            sam_cwp_match_string: "<your_own_value>"
            sam_cwp_password: "<your_own_value>"
            sam_cwp_success_string: "<your_own_value>"
            sam_cwp_test_url: "<your_own_value>"
            sam_cwp_username: "<your_own_value>"
            sam_password: "<your_own_value>"
            sam_report_intv: "0"
            sam_security_type: "open"
            sam_server: "<your_own_value>"
            sam_server_fqdn: "<your_own_value>"
            sam_server_ip: "<your_own_value>"
            sam_server_type: "ip"
            sam_ssid: "<your_own_value>"
            sam_test: "ping"
            sam_username: "<your_own_value>"
            set_80211d: "enable"
            short_guard_interval: "enable"
            spectrum_analysis: "enable"
            transmit_optimize: "disable"
            vap_all: "tunnel"
            vaps:
             -
                name: "default_name_244 (source wireless-controller.vap-group.name system.interface.name)"
            wids_profile: "<your_own_value> (source wireless-controller.wids-profile.name)"
            zero_wait_dfs: "enable"
        radio_3:
            airtime_fairness: "enable"
            amsdu: "enable"
            ap_handoff: "enable"
            ap_sniffer_addr: "<your_own_value>"
            ap_sniffer_bufsize: "16"
            ap_sniffer_chan: "6"
            ap_sniffer_ctl: "enable"
            ap_sniffer_data: "enable"
            ap_sniffer_mgmt_beacon: "enable"
            ap_sniffer_mgmt_other: "enable"
            ap_sniffer_mgmt_probe: "enable"
            arrp_profile: "<your_own_value> (source wireless-controller.arrp-profile.name)"
            auto_power_high: "17"
            auto_power_level: "enable"
            auto_power_low: "10"
            auto_power_target: "<your_own_value>"
            band: "802.11a"
            band_5g_type: "5g-full"
            bandwidth_admission_control: "enable"
            bandwidth_capacity: "2000"
            beacon_interval: "100"
            bss_color: "0"
            bss_color_mode: "auto"
            call_admission_control: "enable"
            call_capacity: "10"
            channel:
             -
                chan: "<your_own_value>"
            channel_bonding: "160MHz"
            channel_utilization: "enable"
            coexistence: "enable"
            darrp: "enable"
            drma: "disable"
            drma_sensitivity: "low"
            dtim: "1"
            frag_threshold: "2346"
            frequency_handoff: "enable"
            iperf_protocol: "udp"
            iperf_server_port: "5001"
            max_clients: "0"
            max_distance: "0"
            mode: "disabled"
            power_level: "100"
            power_mode: "dBm"
            power_value: "27"
            powersave_optimize: "tim"
            protection_mode: "rtscts"
            radio_id: "2"
            rts_threshold: "2346"
            sam_bssid: "<your_own_value>"
            sam_captive_portal: "enable"
            sam_cwp_failure_string: "<your_own_value>"
            sam_cwp_match_string: "<your_own_value>"
            sam_cwp_password: "<your_own_value>"
            sam_cwp_success_string: "<your_own_value>"
            sam_cwp_test_url: "<your_own_value>"
            sam_cwp_username: "<your_own_value>"
            sam_password: "<your_own_value>"
            sam_report_intv: "0"
            sam_security_type: "open"
            sam_server: "<your_own_value>"
            sam_server_fqdn: "<your_own_value>"
            sam_server_ip: "<your_own_value>"
            sam_server_type: "ip"
            sam_ssid: "<your_own_value>"
            sam_test: "ping"
            sam_username: "<your_own_value>"
            set_80211d: "enable"
            short_guard_interval: "enable"
            spectrum_analysis: "enable"
            transmit_optimize: "disable"
            vap_all: "tunnel"
            vaps:
             -
                name: "default_name_320 (source wireless-controller.vap-group.name system.interface.name)"
            wids_profile: "<your_own_value> (source wireless-controller.wids-profile.name)"
            zero_wait_dfs: "enable"
        radio_4:
            airtime_fairness: "enable"
            amsdu: "enable"
            ap_handoff: "enable"
            ap_sniffer_addr: "<your_own_value>"
            ap_sniffer_bufsize: "16"
            ap_sniffer_chan: "6"
            ap_sniffer_ctl: "enable"
            ap_sniffer_data: "enable"
            ap_sniffer_mgmt_beacon: "enable"
            ap_sniffer_mgmt_other: "enable"
            ap_sniffer_mgmt_probe: "enable"
            arrp_profile: "<your_own_value> (source wireless-controller.arrp-profile.name)"
            auto_power_high: "17"
            auto_power_level: "enable"
            auto_power_low: "10"
            auto_power_target: "<your_own_value>"
            band: "802.11a"
            band_5g_type: "5g-full"
            bandwidth_admission_control: "enable"
            bandwidth_capacity: "2000"
            beacon_interval: "100"
            bss_color: "0"
            bss_color_mode: "auto"
            call_admission_control: "enable"
            call_capacity: "10"
            channel:
             -
                chan: "<your_own_value>"
            channel_bonding: "160MHz"
            channel_utilization: "enable"
            coexistence: "enable"
            darrp: "enable"
            drma: "disable"
            drma_sensitivity: "low"
            dtim: "1"
            frag_threshold: "2346"
            frequency_handoff: "enable"
            iperf_protocol: "udp"
            iperf_server_port: "5001"
            max_clients: "0"
            max_distance: "0"
            mode: "disabled"
            power_level: "100"
            power_mode: "dBm"
            power_value: "27"
            powersave_optimize: "tim"
            protection_mode: "rtscts"
            rts_threshold: "2346"
            sam_bssid: "<your_own_value>"
            sam_captive_portal: "enable"
            sam_cwp_failure_string: "<your_own_value>"
            sam_cwp_match_string: "<your_own_value>"
            sam_cwp_password: "<your_own_value>"
            sam_cwp_success_string: "<your_own_value>"
            sam_cwp_test_url: "<your_own_value>"
            sam_cwp_username: "<your_own_value>"
            sam_password: "<your_own_value>"
            sam_report_intv: "0"
            sam_security_type: "open"
            sam_server: "<your_own_value>"
            sam_server_fqdn: "<your_own_value>"
            sam_server_ip: "<your_own_value>"
            sam_server_type: "ip"
            sam_ssid: "<your_own_value>"
            sam_test: "ping"
            sam_username: "<your_own_value>"
            set_80211d: "enable"
            short_guard_interval: "enable"
            spectrum_analysis: "enable"
            transmit_optimize: "disable"
            vap_all: "tunnel"
            vaps:
             -
                name: "default_name_395 (source wireless-controller.vap-group.name system.interface.name)"
            wids_profile: "<your_own_value> (source wireless-controller.wids-profile.name)"
            zero_wait_dfs: "enable"
        split_tunneling_acl:
         -
            dest_ip: "<your_own_value>"
            id:  "400"
        split_tunneling_acl_local_ap_subnet: "enable"
        split_tunneling_acl_path: "tunnel"
        syslog_profile: "<your_own_value> (source wireless-controller.syslog-profile.name)"
        tun_mtu_downlink: "0"
        tun_mtu_uplink: "0"
        wan_port_auth: "none"
        wan_port_auth_methods: "all"
        wan_port_auth_password: "<your_own_value>"
        wan_port_auth_usrname: "<your_own_value>"
        wan_port_mode: "wan-lan"
```

## [Return Values](fortios_wireless_controller_wtp_profile_module.md#id6)

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
