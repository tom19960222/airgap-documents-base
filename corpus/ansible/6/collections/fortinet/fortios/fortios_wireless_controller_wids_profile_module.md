---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_wireless_controller_wids_profile module – Configure wireless intrusion detection system (WIDS) profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_wireless_controller_wids_profile_module.html
fetched_at: 2026-07-27T17:47:27+00:00
---
# fortinet.fortios.fortios_wireless_controller_wids_profile module – Configure wireless intrusion detection system (WIDS) profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_wids_profile_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-wids-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_wids_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_wids_profile_module.md#synopsis)
- [Requirements](fortios_wireless_controller_wids_profile_module.md#requirements)
- [Parameters](fortios_wireless_controller_wids_profile_module.md#parameters)
- [Notes](fortios_wireless_controller_wids_profile_module.md#notes)
- [Examples](fortios_wireless_controller_wids_profile_module.md#examples)
- [Return Values](fortios_wireless_controller_wids_profile_module.md#return-values)

## [Synopsis](fortios_wireless_controller_wids_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and wids_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_wids_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_wireless_controller_wids_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **wireless_controller_wids_profile**  dictionary | Configure wireless intrusion detection system (WIDS) profiles. |
| **ap_auto_suppress**  string | Enable/disable on-wire rogue AP auto-suppression .  Choices:   - `"enable"` - `"disable"` |
| **ap_bgscan_disable_day**  string | Optionally turn off scanning for one or more days of the week. Separate the days with a space. By default, no days are set.  Choices:   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **ap_bgscan_disable_end**  string | End time, using a 24-hour clock in the format of hh:mm, for disabling background scanning . |
| **ap_bgscan_disable_schedules**  list / elements=dictionary | Firewall schedules for turning off FortiAP radio background scan. Background scan will be disabled when at least one of the schedules is valid. Separate multiple schedule names with a space. |
| **name**  string | Schedule name. Source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name. |
| **ap_bgscan_disable_start**  string | Start time, using a 24-hour clock in the format of hh:mm, for disabling background scanning . |
| **ap_bgscan_duration**  integer | Listen time on scanning a channel (10 - 1000 msec). |
| **ap_bgscan_idle**  integer | Wait time for channel inactivity before scanning this channel (0 - 1000 msec). |
| **ap_bgscan_intv**  integer | Period between successive channel scans (1 - 600 sec). |
| **ap_bgscan_period**  integer | Period between background scans (10 - 3600 sec). |
| **ap_bgscan_report_intv**  integer | Period between background scan reports (15 - 600 sec). |
| **ap_fgscan_report_intv**  integer | Period between foreground scan reports (15 - 600 sec). |
| **ap_scan**  string | Enable/disable rogue AP detection.  Choices:   - `"disable"` - `"enable"` |
| **ap_scan_passive**  string | Enable/disable passive scanning. Enable means do not send probe request on any channels .  Choices:   - `"enable"` - `"disable"` |
| **ap_scan_threshold**  string | Minimum signal level/threshold in dBm required for the AP to report detected rogue AP (-95 to -20). |
| **asleap_attack**  string | Enable/disable asleap attack detection .  Choices:   - `"enable"` - `"disable"` |
| **assoc_flood_thresh**  integer | The threshold value for association frame flooding. |
| **assoc_flood_time**  integer | Number of seconds after which a station is considered not connected. |
| **assoc_frame_flood**  string | Enable/disable association frame flooding detection .  Choices:   - `"enable"` - `"disable"` |
| **auth_flood_thresh**  integer | The threshold value for authentication frame flooding. |
| **auth_flood_time**  integer | Number of seconds after which a station is considered not connected. |
| **auth_frame_flood**  string | Enable/disable authentication frame flooding detection .  Choices:   - `"enable"` - `"disable"` |
| **comment**  string | Comment. |
| **deauth_broadcast**  string | Enable/disable broadcasting de-authentication detection .  Choices:   - `"enable"` - `"disable"` |
| **deauth_unknown_src_thresh**  integer | Threshold value per second to deauth unknown src for DoS attack (0: no limit). |
| **eapol_fail_flood**  string | Enable/disable EAPOL-Failure flooding (to AP) detection .  Choices:   - `"enable"` - `"disable"` |
| **eapol_fail_intv**  integer | The detection interval for EAPOL-Failure flooding (1 - 3600 sec). |
| **eapol_fail_thresh**  integer | The threshold value for EAPOL-Failure flooding in specified interval. |
| **eapol_logoff_flood**  string | Enable/disable EAPOL-Logoff flooding (to AP) detection .  Choices:   - `"enable"` - `"disable"` |
| **eapol_logoff_intv**  integer | The detection interval for EAPOL-Logoff flooding (1 - 3600 sec). |
| **eapol_logoff_thresh**  integer | The threshold value for EAPOL-Logoff flooding in specified interval. |
| **eapol_pre_fail_flood**  string | Enable/disable premature EAPOL-Failure flooding (to STA) detection .  Choices:   - `"enable"` - `"disable"` |
| **eapol_pre_fail_intv**  integer | The detection interval for premature EAPOL-Failure flooding (1 - 3600 sec). |
| **eapol_pre_fail_thresh**  integer | The threshold value for premature EAPOL-Failure flooding in specified interval. |
| **eapol_pre_succ_flood**  string | Enable/disable premature EAPOL-Success flooding (to STA) detection .  Choices:   - `"enable"` - `"disable"` |
| **eapol_pre_succ_intv**  integer | The detection interval for premature EAPOL-Success flooding (1 - 3600 sec). |
| **eapol_pre_succ_thresh**  integer | The threshold value for premature EAPOL-Success flooding in specified interval. |
| **eapol_start_flood**  string | Enable/disable EAPOL-Start flooding (to AP) detection .  Choices:   - `"enable"` - `"disable"` |
| **eapol_start_intv**  integer | The detection interval for EAPOL-Start flooding (1 - 3600 sec). |
| **eapol_start_thresh**  integer | The threshold value for EAPOL-Start flooding in specified interval. |
| **eapol_succ_flood**  string | Enable/disable EAPOL-Success flooding (to AP) detection .  Choices:   - `"enable"` - `"disable"` |
| **eapol_succ_intv**  integer | The detection interval for EAPOL-Success flooding (1 - 3600 sec). |
| **eapol_succ_thresh**  integer | The threshold value for EAPOL-Success flooding in specified interval. |
| **invalid_mac_oui**  string | Enable/disable invalid MAC OUI detection.  Choices:   - `"enable"` - `"disable"` |
| **long_duration_attack**  string | Enable/disable long duration attack detection based on user configured threshold .  Choices:   - `"enable"` - `"disable"` |
| **long_duration_thresh**  integer | Threshold value for long duration attack detection (1000 - 32767 usec). |
| **name**  string / required | WIDS profile name. |
| **null_ssid_probe_resp**  string | Enable/disable null SSID probe response detection .  Choices:   - `"enable"` - `"disable"` |
| **sensor_mode**  string | Scan nearby WiFi stations .  Choices:   - `"disable"` - `"foreign"` - `"both"` |
| **spoofed_deauth**  string | Enable/disable spoofed de-authentication attack detection .  Choices:   - `"enable"` - `"disable"` |
| **weak_wep_iv**  string | Enable/disable weak WEP IV (Initialization Vector) detection .  Choices:   - `"enable"` - `"disable"` |
| **wireless_bridge**  string | Enable/disable wireless bridge detection .  Choices:   - `"enable"` - `"disable"` |

## [Notes](fortios_wireless_controller_wids_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_wids_profile_module.md#id5)

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
  - name: Configure wireless intrusion detection system (WIDS) profiles.
    fortios_wireless_controller_wids_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_wids_profile:
        ap_auto_suppress: "enable"
        ap_bgscan_disable_day: "sunday"
        ap_bgscan_disable_end: "<your_own_value>"
        ap_bgscan_disable_schedules:
         -
            name: "default_name_7 (source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name)"
        ap_bgscan_disable_start: "<your_own_value>"
        ap_bgscan_duration: "30"
        ap_bgscan_idle: "20"
        ap_bgscan_intv: "3"
        ap_bgscan_period: "600"
        ap_bgscan_report_intv: "30"
        ap_fgscan_report_intv: "15"
        ap_scan: "disable"
        ap_scan_passive: "enable"
        ap_scan_threshold: "<your_own_value>"
        asleap_attack: "enable"
        assoc_flood_thresh: "30"
        assoc_flood_time: "10"
        assoc_frame_flood: "enable"
        auth_flood_thresh: "30"
        auth_flood_time: "10"
        auth_frame_flood: "enable"
        comment: "Comment."
        deauth_broadcast: "enable"
        deauth_unknown_src_thresh: "10"
        eapol_fail_flood: "enable"
        eapol_fail_intv: "1"
        eapol_fail_thresh: "10"
        eapol_logoff_flood: "enable"
        eapol_logoff_intv: "1"
        eapol_logoff_thresh: "10"
        eapol_pre_fail_flood: "enable"
        eapol_pre_fail_intv: "1"
        eapol_pre_fail_thresh: "10"
        eapol_pre_succ_flood: "enable"
        eapol_pre_succ_intv: "1"
        eapol_pre_succ_thresh: "10"
        eapol_start_flood: "enable"
        eapol_start_intv: "1"
        eapol_start_thresh: "10"
        eapol_succ_flood: "enable"
        eapol_succ_intv: "1"
        eapol_succ_thresh: "10"
        invalid_mac_oui: "enable"
        long_duration_attack: "enable"
        long_duration_thresh: "8200"
        name: "default_name_49"
        null_ssid_probe_resp: "enable"
        sensor_mode: "disable"
        spoofed_deauth: "enable"
        weak_wep_iv: "enable"
        wireless_bridge: "enable"
```

## [Return Values](fortios_wireless_controller_wids_profile_module.md#id6)

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
