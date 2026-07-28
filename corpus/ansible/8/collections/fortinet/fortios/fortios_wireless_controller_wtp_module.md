---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_wireless_controller_wtp module – Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_wireless_controller_wtp_module.html
fetched_at: 2026-07-28T02:31:32+00:00
---
# fortinet.fortios.fortios_wireless_controller_wtp module – Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_wtp_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-wtp-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_wtp`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_wtp_module.md#synopsis)
- [Requirements](fortios_wireless_controller_wtp_module.md#requirements)
- [Parameters](fortios_wireless_controller_wtp_module.md#parameters)
- [Notes](fortios_wireless_controller_wtp_module.md#notes)
- [Examples](fortios_wireless_controller_wtp_module.md#examples)
- [Return Values](fortios_wireless_controller_wtp_module.md#return-values)

## [Synopsis](fortios_wireless_controller_wtp_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and wtp category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_wtp_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_wireless_controller_wtp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **wireless_controller_wtp**  dictionary | Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate. |
| **admin**  string | Configure how the FortiGate operating as a wireless controller discovers and manages this WTP, AP or FortiAP.  **Choices:**   - `"discovered"` - `"disable"` - `"enable"` |
| **allowaccess**  list / elements=string | Control management access to the managed WTP, FortiAP, or AP. Separate entries with a space.  **Choices:**   - `"https"` - `"ssh"` - `"snmp"` - `"telnet"` - `"http"` |
| **apcfg_profile**  string | AP local configuration profile name. Source wireless-controller.apcfg-profile.name. |
| **ble_major_id**  integer | Override BLE Major ID. |
| **ble_minor_id**  integer | Override BLE Minor ID. |
| **bonjour_profile**  string | Bonjour profile name. Source wireless-controller.bonjour-profile.name. |
| **coordinate_enable**  string | Enable/disable WTP coordinates (X,Y axis).  **Choices:**   - `"enable"` - `"disable"` |
| **coordinate_latitude**  string | WTP latitude coordinate. |
| **coordinate_longitude**  string | WTP longitude coordinate. |
| **coordinate_x**  string | X axis coordinate. |
| **coordinate_y**  string | Y axis coordinate. |
| **firmware_provision**  string | Firmware version to provision to this FortiAP on bootup (major.minor.build, i.e. 6.2.1234). |
| **firmware_provision_latest**  string | Enable/disable one-time automatic provisioning of the latest firmware version.  **Choices:**   - `"disable"` - `"once"` |
| **image_download**  string | Enable/disable WTP image download.  **Choices:**   - `"enable"` - `"disable"` |
| **index**  integer | Index (0 - 4294967295). |
| **ip_fragment_preventing**  list / elements=string | Method(s) by which IP fragmentation is prevented for control and data packets through CAPWAP tunnel .  **Choices:**   - `"tcp-mss-adjust"` - `"icmp-unreachable"` |
| **lan**  dictionary | WTP LAN port mapping. |
| **port1_mode**  string | LAN port 1 mode.  **Choices:**   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port1_ssid**  string | Bridge LAN port 1 to SSID. Source system.interface.name. |
| **port2_mode**  string | LAN port 2 mode.  **Choices:**   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port2_ssid**  string | Bridge LAN port 2 to SSID. Source system.interface.name. |
| **port3_mode**  string | LAN port 3 mode.  **Choices:**   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port3_ssid**  string | Bridge LAN port 3 to SSID. Source system.interface.name. |
| **port4_mode**  string | LAN port 4 mode.  **Choices:**   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port4_ssid**  string | Bridge LAN port 4 to SSID. Source system.interface.name. |
| **port5_mode**  string | LAN port 5 mode.  **Choices:**   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port5_ssid**  string | Bridge LAN port 5 to SSID. Source system.interface.name. |
| **port6_mode**  string | LAN port 6 mode.  **Choices:**   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port6_ssid**  string | Bridge LAN port 6 to SSID. Source system.interface.name. |
| **port7_mode**  string | LAN port 7 mode.  **Choices:**   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port7_ssid**  string | Bridge LAN port 7 to SSID. Source system.interface.name. |
| **port8_mode**  string | LAN port 8 mode.  **Choices:**   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port8_ssid**  string | Bridge LAN port 8 to SSID. Source system.interface.name. |
| **port_esl_mode**  string | ESL port mode.  **Choices:**   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port_esl_ssid**  string | Bridge ESL port to SSID. Source system.interface.name. |
| **port_mode**  string | LAN port mode.  **Choices:**   - `"offline"` - `"nat-to-wan"` - `"bridge-to-wan"` - `"bridge-to-ssid"` |
| **port_ssid**  string | Bridge LAN port to SSID. Source system.interface.name. |
| **led_state**  string | Enable to allow the FortiAPs LEDs to light. Disable to keep the LEDs off. You may want to keep the LEDs off so they are not distracting in low light areas etc.  **Choices:**   - `"enable"` - `"disable"` |
| **location**  string | Field for describing the physical location of the WTP, AP or FortiAP. |
| **login_passwd**  string | Set the managed WTP, FortiAP, or AP”s administrator password. |
| **login_passwd_change**  string | Change or reset the administrator password of a managed WTP, FortiAP or AP (yes, default, or no).  **Choices:**   - `"yes"` - `"default"` - `"no"` |
| **mesh_bridge_enable**  string | Enable/disable mesh Ethernet bridge when WTP is configured as a mesh branch/leaf AP.  **Choices:**   - `"default"` - `"enable"` - `"disable"` |
| **name**  string | WTP, AP or FortiAP configuration name. |
| **override_allowaccess**  string | Enable to override the WTP profile management access configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **override_ip_fragment**  string | Enable/disable overriding the WTP profile IP fragment prevention setting.  **Choices:**   - `"enable"` - `"disable"` |
| **override_lan**  string | Enable to override the WTP profile LAN port setting.  **Choices:**   - `"enable"` - `"disable"` |
| **override_led_state**  string | Enable to override the profile LED state setting for this FortiAP. You must enable this option to use the led-state command to turn off the FortiAP”s LEDs.  **Choices:**   - `"enable"` - `"disable"` |
| **override_login_passwd_change**  string | Enable to override the WTP profile login-password (administrator password) setting.  **Choices:**   - `"enable"` - `"disable"` |
| **override_split_tunnel**  string | Enable/disable overriding the WTP profile split tunneling setting.  **Choices:**   - `"enable"` - `"disable"` |
| **override_wan_port_mode**  string | Enable/disable overriding the wan-port-mode in the WTP profile.  **Choices:**   - `"enable"` - `"disable"` |
| **radio_1**  dictionary | Configuration options for radio 1. |
| **auto_power_high**  integer | The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference .  **Choices:**   - `"enable"` - `"disable"` |
| **auto_power_low**  integer | The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_target**  string | Target of automatic transmit power adjustment in dBm (-95 to -20). |
| **band**  string | WiFi band that Radio 1 operates on.  **Choices:**   - `"802.11a"` - `"802.11b"` - `"802.11g"` - `"802.11n"` - `"802.11n-5G"` - `"802.11ac"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11ax-6G"` - `"802.11n,g-only"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n-5G-only"` - `"802.11ac,n-only"` - `"802.11ac-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-5G-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ax-only"` |
| **channel**  list / elements=dictionary | Selected list of wireless radio channels. |
| **chan**  string / required | Channel number. |
| **drma_manual_mode**  string | Radio mode to be used for DRMA manual mode .  **Choices:**   - `"ap"` - `"monitor"` - `"ncf"` - `"ncf-peek"` |
| **override_analysis**  string | Enable to override the WTP profile spectrum analysis configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **override_band**  string | Enable to override the WTP profile band setting.  **Choices:**   - `"enable"` - `"disable"` |
| **override_channel**  string | Enable to override WTP profile channel settings.  **Choices:**   - `"enable"` - `"disable"` |
| **override_txpower**  string | Enable to override the WTP profile power level configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **override_vaps**  string | Enable to override WTP profile Virtual Access Point (VAP) settings.  **Choices:**   - `"enable"` - `"disable"` |
| **power_level**  integer | Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100). |
| **power_mode**  string | Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP . This power takes into account both radio transmit power and antenna gain. Higher power level settings may be constrained by local regulatory requirements and AP capabilities.  **Choices:**   - `"dBm"` - `"percentage"` |
| **power_value**  integer | Radio EIRP power in dBm (1 - 33). |
| **radio_id**  integer | radio-id |
| **spectrum_analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  **Choices:**   - `"enable"` - `"scan-only"` - `"disable"` |
| **vap_all**  string | Configure method for assigning SSIDs to this FortiAP .  **Choices:**   - `"tunnel"` - `"bridge"` - `"manual"` - `"enable"` - `"disable"` |
| **vaps**  list / elements=dictionary | Manually selected list of Virtual Access Points (VAPs). |
| **name**  string / required | Virtual Access Point (VAP) name. Source wireless-controller.vap-group.name system.interface.name. |
| **radio_2**  dictionary | Configuration options for radio 2. |
| **auto_power_high**  integer | The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference .  **Choices:**   - `"enable"` - `"disable"` |
| **auto_power_low**  integer | The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_target**  string | Target of automatic transmit power adjustment in dBm (-95 to -20). |
| **band**  string | WiFi band that Radio 2 operates on.  **Choices:**   - `"802.11a"` - `"802.11b"` - `"802.11g"` - `"802.11n"` - `"802.11n-5G"` - `"802.11ac"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11ax-6G"` - `"802.11n,g-only"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n-5G-only"` - `"802.11ac,n-only"` - `"802.11ac-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-5G-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ax-only"` |
| **channel**  list / elements=dictionary | Selected list of wireless radio channels. |
| **chan**  string / required | Channel number. |
| **drma_manual_mode**  string | Radio mode to be used for DRMA manual mode .  **Choices:**   - `"ap"` - `"monitor"` - `"ncf"` - `"ncf-peek"` |
| **override_analysis**  string | Enable to override the WTP profile spectrum analysis configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **override_band**  string | Enable to override the WTP profile band setting.  **Choices:**   - `"enable"` - `"disable"` |
| **override_channel**  string | Enable to override WTP profile channel settings.  **Choices:**   - `"enable"` - `"disable"` |
| **override_txpower**  string | Enable to override the WTP profile power level configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **override_vaps**  string | Enable to override WTP profile Virtual Access Point (VAP) settings.  **Choices:**   - `"enable"` - `"disable"` |
| **power_level**  integer | Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100). |
| **power_mode**  string | Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP . This power takes into account both radio transmit power and antenna gain. Higher power level settings may be constrained by local regulatory requirements and AP capabilities.  **Choices:**   - `"dBm"` - `"percentage"` |
| **power_value**  integer | Radio EIRP power in dBm (1 - 33). |
| **radio_id**  integer | radio-id |
| **spectrum_analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  **Choices:**   - `"enable"` - `"scan-only"` - `"disable"` |
| **vap_all**  string | Configure method for assigning SSIDs to this FortiAP .  **Choices:**   - `"tunnel"` - `"bridge"` - `"manual"` - `"enable"` - `"disable"` |
| **vaps**  list / elements=dictionary | Manually selected list of Virtual Access Points (VAPs). |
| **name**  string / required | Virtual Access Point (VAP) name. Source wireless-controller.vap-group.name system.interface.name. |
| **radio_3**  dictionary | Configuration options for radio 3. |
| **auto_power_high**  integer | The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference .  **Choices:**   - `"enable"` - `"disable"` |
| **auto_power_low**  integer | The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_target**  string | Target of automatic transmit power adjustment in dBm (-95 to -20). |
| **band**  string | WiFi band that Radio 3 operates on.  **Choices:**   - `"802.11a"` - `"802.11b"` - `"802.11g"` - `"802.11n"` - `"802.11n-5G"` - `"802.11ac"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11ax-6G"` - `"802.11n,g-only"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n-5G-only"` - `"802.11ac,n-only"` - `"802.11ac-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-5G-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ax-only"` |
| **channel**  list / elements=dictionary | Selected list of wireless radio channels. |
| **chan**  string / required | Channel number. |
| **drma_manual_mode**  string | Radio mode to be used for DRMA manual mode .  **Choices:**   - `"ap"` - `"monitor"` - `"ncf"` - `"ncf-peek"` |
| **override_analysis**  string | Enable to override the WTP profile spectrum analysis configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **override_band**  string | Enable to override the WTP profile band setting.  **Choices:**   - `"enable"` - `"disable"` |
| **override_channel**  string | Enable to override WTP profile channel settings.  **Choices:**   - `"enable"` - `"disable"` |
| **override_txpower**  string | Enable to override the WTP profile power level configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **override_vaps**  string | Enable to override WTP profile Virtual Access Point (VAP) settings.  **Choices:**   - `"enable"` - `"disable"` |
| **power_level**  integer | Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100). |
| **power_mode**  string | Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP . This power takes into account both radio transmit power and antenna gain. Higher power level settings may be constrained by local regulatory requirements and AP capabilities.  **Choices:**   - `"dBm"` - `"percentage"` |
| **power_value**  integer | Radio EIRP power in dBm (1 - 33). |
| **radio_id**  integer | radio-id |
| **spectrum_analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  **Choices:**   - `"enable"` - `"scan-only"` - `"disable"` |
| **vap_all**  string | Configure method for assigning SSIDs to this FortiAP .  **Choices:**   - `"tunnel"` - `"bridge"` - `"manual"` - `"enable"` - `"disable"` |
| **vaps**  list / elements=dictionary | Manually selected list of Virtual Access Points (VAPs). |
| **name**  string / required | Virtual Access Point (VAP) name. Source wireless-controller.vap-group.name system.interface.name. |
| **radio_4**  dictionary | Configuration options for radio 4. |
| **auto_power_high**  integer | The upper bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_level**  string | Enable/disable automatic power-level adjustment to prevent co-channel interference .  **Choices:**   - `"enable"` - `"disable"` |
| **auto_power_low**  integer | The lower bound of automatic transmit power adjustment in dBm (the actual range of transmit power depends on the AP platform type). |
| **auto_power_target**  string | Target of automatic transmit power adjustment in dBm (-95 to -20). |
| **band**  string | WiFi band that Radio 4 operates on.  **Choices:**   - `"802.11a"` - `"802.11b"` - `"802.11g"` - `"802.11n"` - `"802.11n-5G"` - `"802.11ac"` - `"802.11ax-5G"` - `"802.11ax"` - `"802.11ac-2G"` - `"802.11ax-6G"` - `"802.11n,g-only"` - `"802.11g-only"` - `"802.11n-only"` - `"802.11n-5G-only"` - `"802.11ac,n-only"` - `"802.11ac-only"` - `"802.11ax,ac-only"` - `"802.11ax,ac,n-only"` - `"802.11ax-5G-only"` - `"802.11ax,n-only"` - `"802.11ax,n,g-only"` - `"802.11ax-only"` |
| **channel**  list / elements=dictionary | Selected list of wireless radio channels. |
| **chan**  string / required | Channel number. |
| **drma_manual_mode**  string | Radio mode to be used for DRMA manual mode .  **Choices:**   - `"ap"` - `"monitor"` - `"ncf"` - `"ncf-peek"` |
| **override_analysis**  string | Enable to override the WTP profile spectrum analysis configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **override_band**  string | Enable to override the WTP profile band setting.  **Choices:**   - `"enable"` - `"disable"` |
| **override_channel**  string | Enable to override WTP profile channel settings.  **Choices:**   - `"enable"` - `"disable"` |
| **override_txpower**  string | Enable to override the WTP profile power level configuration.  **Choices:**   - `"enable"` - `"disable"` |
| **override_vaps**  string | Enable to override WTP profile Virtual Access Point (VAP) settings.  **Choices:**   - `"enable"` - `"disable"` |
| **power_level**  integer | Radio EIRP power level as a percentage of the maximum EIRP power (0 - 100). |
| **power_mode**  string | Set radio effective isotropic radiated power (EIRP) in dBm or by a percentage of the maximum EIRP . This power takes into account both radio transmit power and antenna gain. Higher power level settings may be constrained by local regulatory requirements and AP capabilities.  **Choices:**   - `"dBm"` - `"percentage"` |
| **power_value**  integer | Radio EIRP power in dBm (1 - 33). |
| **spectrum_analysis**  string | Enable/disable spectrum analysis to find interference that would negatively impact wireless performance.  **Choices:**   - `"enable"` - `"scan-only"` - `"disable"` |
| **vap_all**  string | Configure method for assigning SSIDs to this FortiAP .  **Choices:**   - `"tunnel"` - `"bridge"` - `"manual"` - `"enable"` - `"disable"` |
| **vaps**  list / elements=dictionary | Manually selected list of Virtual Access Points (VAPs). |
| **name**  string / required | Virtual Access Point (VAP) name. Source wireless-controller.vap-group.name system.interface.name. |
| **region**  string | Region name WTP is associated with. Source wireless-controller.region.name. |
| **region_x**  string | Relative horizontal region coordinate (between 0 and 1). |
| **region_y**  string | Relative vertical region coordinate (between 0 and 1). |
| **split_tunneling_acl**  list / elements=dictionary | Split tunneling ACL filter list. |
| **dest_ip**  string | Destination IP and mask for the split-tunneling subnet. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **split_tunneling_acl_local_ap_subnet**  string | Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL .  **Choices:**   - `"enable"` - `"disable"` |
| **split_tunneling_acl_path**  string | Split tunneling ACL path is local/tunnel.  **Choices:**   - `"tunnel"` - `"local"` |
| **tun_mtu_downlink**  integer | The MTU of downlink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of FortiAP; ). |
| **tun_mtu_uplink**  integer | The maximum transmission unit (MTU) of uplink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of FortiAP; ). |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **wan_port_mode**  string | Enable/disable using the FortiAP WAN port as a LAN port.  **Choices:**   - `"wan-lan"` - `"wan-only"` |
| **wtp_id**  string / required | WTP ID. |
| **wtp_mode**  string | WTP, AP, or FortiAP operating mode; normal (by default) or remote. A tunnel mode SSID can be assigned to an AP in normal mode but not remote mode, while a local-bridge mode SSID can be assigned to an AP in either normal mode or remote mode.  **Choices:**   - `"normal"` - `"remote"` |
| **wtp_profile**  string | WTP profile name to apply to this WTP, AP or FortiAP. Source wireless-controller.wtp-profile.name. |

## [Notes](fortios_wireless_controller_wtp_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_wtp_module.md#id5)

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
  - name: Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.
    fortios_wireless_controller_wtp:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_wtp:
        admin: "discovered"
        allowaccess: "https"
        apcfg_profile: "<your_own_value> (source wireless-controller.apcfg-profile.name)"
        ble_major_id: "0"
        ble_minor_id: "0"
        bonjour_profile: "<your_own_value> (source wireless-controller.bonjour-profile.name)"
        coordinate_enable: "enable"
        coordinate_latitude: "<your_own_value>"
        coordinate_longitude: "<your_own_value>"
        coordinate_x: "<your_own_value>"
        coordinate_y: "<your_own_value>"
        firmware_provision: "<your_own_value>"
        firmware_provision_latest: "disable"
        image_download: "enable"
        index: "0"
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
        led_state: "enable"
        location: "<your_own_value>"
        login_passwd: "<your_own_value>"
        login_passwd_change: "yes"
        mesh_bridge_enable: "default"
        name: "default_name_45"
        override_allowaccess: "enable"
        override_ip_fragment: "enable"
        override_lan: "enable"
        override_led_state: "enable"
        override_login_passwd_change: "enable"
        override_split_tunnel: "enable"
        override_wan_port_mode: "enable"
        radio_1:
            auto_power_high: "17"
            auto_power_level: "enable"
            auto_power_low: "10"
            auto_power_target: "<your_own_value>"
            band: "802.11a"
            channel:
             -
                chan: "<your_own_value>"
            drma_manual_mode: "ap"
            override_analysis: "enable"
            override_band: "enable"
            override_channel: "enable"
            override_txpower: "enable"
            override_vaps: "enable"
            power_level: "100"
            power_mode: "dBm"
            power_value: "27"
            radio_id: "2"
            spectrum_analysis: "enable"
            vap_all: "tunnel"
            vaps:
             -
                name: "default_name_74 (source wireless-controller.vap-group.name system.interface.name)"
        radio_2:
            auto_power_high: "17"
            auto_power_level: "enable"
            auto_power_low: "10"
            auto_power_target: "<your_own_value>"
            band: "802.11a"
            channel:
             -
                chan: "<your_own_value>"
            drma_manual_mode: "ap"
            override_analysis: "enable"
            override_band: "enable"
            override_channel: "enable"
            override_txpower: "enable"
            override_vaps: "enable"
            power_level: "100"
            power_mode: "dBm"
            power_value: "27"
            radio_id: "2"
            spectrum_analysis: "enable"
            vap_all: "tunnel"
            vaps:
             -
                name: "default_name_96 (source wireless-controller.vap-group.name system.interface.name)"
        radio_3:
            auto_power_high: "17"
            auto_power_level: "enable"
            auto_power_low: "10"
            auto_power_target: "<your_own_value>"
            band: "802.11a"
            channel:
             -
                chan: "<your_own_value>"
            drma_manual_mode: "ap"
            override_analysis: "enable"
            override_band: "enable"
            override_channel: "enable"
            override_txpower: "enable"
            override_vaps: "enable"
            power_level: "100"
            power_mode: "dBm"
            power_value: "27"
            radio_id: "2"
            spectrum_analysis: "enable"
            vap_all: "tunnel"
            vaps:
             -
                name: "default_name_118 (source wireless-controller.vap-group.name system.interface.name)"
        radio_4:
            auto_power_high: "17"
            auto_power_level: "enable"
            auto_power_low: "10"
            auto_power_target: "<your_own_value>"
            band: "802.11a"
            channel:
             -
                chan: "<your_own_value>"
            drma_manual_mode: "ap"
            override_analysis: "enable"
            override_band: "enable"
            override_channel: "enable"
            override_txpower: "enable"
            override_vaps: "enable"
            power_level: "100"
            power_mode: "dBm"
            power_value: "27"
            spectrum_analysis: "enable"
            vap_all: "tunnel"
            vaps:
             -
                name: "default_name_139 (source wireless-controller.vap-group.name system.interface.name)"
        region: "<your_own_value> (source wireless-controller.region.name)"
        region_x: "<your_own_value>"
        region_y: "<your_own_value>"
        split_tunneling_acl:
         -
            dest_ip: "<your_own_value>"
            id:  "145"
        split_tunneling_acl_local_ap_subnet: "enable"
        split_tunneling_acl_path: "tunnel"
        tun_mtu_downlink: "0"
        tun_mtu_uplink: "0"
        uuid: "<your_own_value>"
        wan_port_mode: "wan-lan"
        wtp_id: "<your_own_value>"
        wtp_mode: "normal"
        wtp_profile: "<your_own_value> (source wireless-controller.wtp-profile.name)"
```

## [Return Values](fortios_wireless_controller_wtp_module.md#id6)

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
