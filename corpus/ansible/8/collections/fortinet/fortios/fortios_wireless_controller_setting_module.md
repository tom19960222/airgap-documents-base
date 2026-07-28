---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_wireless_controller_setting module – VDOM wireless controller configuration in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_wireless_controller_setting_module.html
fetched_at: 2026-07-28T02:31:22+00:00
---
# fortinet.fortios.fortios_wireless_controller_setting module – VDOM wireless controller configuration in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_setting_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-setting-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_setting`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_setting_module.md#synopsis)
- [Requirements](fortios_wireless_controller_setting_module.md#requirements)
- [Parameters](fortios_wireless_controller_setting_module.md#parameters)
- [Notes](fortios_wireless_controller_setting_module.md#notes)
- [Examples](fortios_wireless_controller_setting_module.md#examples)
- [Return Values](fortios_wireless_controller_setting_module.md#return-values)

## [Synopsis](fortios_wireless_controller_setting_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and setting category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_setting_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_wireless_controller_setting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **wireless_controller_setting**  dictionary | VDOM wireless controller configuration. |
| **account_id**  string | FortiCloud customer account ID. |
| **country**  string | Country or region in which the FortiGate is located. The country determines the 802.11 bands and channels that are available.  **Choices:**   - `"--"` - `"AF"` - `"AL"` - `"DZ"` - `"AS"` - `"AO"` - `"AR"` - `"AM"` - `"AU"` - `"AT"` - `"AZ"` - `"BS"` - `"BH"` - `"BD"` - `"BB"` - `"BY"` - `"BE"` - `"BZ"` - `"BJ"` - `"BM"` - `"BT"` - `"BO"` - `"BA"` - `"BW"` - `"BR"` - `"BN"` - `"BG"` - `"BF"` - `"KH"` - `"CM"` - `"KY"` - `"CF"` - `"TD"` - `"CL"` - `"CN"` - `"CX"` - `"CO"` - `"CG"` - `"CD"` - `"CR"` - `"HR"` - `"CY"` - `"CZ"` - `"DK"` - `"DJ"` - `"DM"` - `"DO"` - `"EC"` - `"EG"` - `"SV"` - `"ET"` - `"EE"` - `"GF"` - `"PF"` - `"FO"` - `"FJ"` - `"FI"` - `"FR"` - `"GA"` - `"GE"` - `"GM"` - `"DE"` - `"GH"` - `"GI"` - `"GR"` - `"GL"` - `"GD"` - `"GP"` - `"GU"` - `"GT"` - `"GY"` - `"HT"` - `"HN"` - `"HK"` - `"HU"` - `"IS"` - `"IN"` - `"ID"` - `"IQ"` - `"IE"` - `"IM"` - `"IL"` - `"IT"` - `"CI"` - `"JM"` - `"JO"` - `"KZ"` - `"KE"` - `"KR"` - `"KW"` - `"LA"` - `"LV"` - `"LB"` - `"LS"` - `"LR"` - `"LY"` - `"LI"` - `"LT"` - `"LU"` - `"MO"` - `"MK"` - `"MG"` - `"MW"` - `"MY"` - `"MV"` - `"ML"` - `"MT"` - `"MH"` - `"MQ"` - `"MR"` - `"MU"` - `"YT"` - `"MX"` - `"FM"` - `"MD"` - `"MC"` - `"MN"` - `"MA"` - `"MZ"` - `"MM"` - `"NA"` - `"NP"` - `"NL"` - `"AN"` - `"AW"` - `"NZ"` - `"NI"` - `"NE"` - `"NG"` - `"NO"` - `"MP"` - `"OM"` - `"PK"` - `"PW"` - `"PA"` - `"PG"` - `"PY"` - `"PE"` - `"PH"` - `"PL"` - `"PT"` - `"PR"` - `"QA"` - `"RE"` - `"RO"` - `"RU"` - `"RW"` - `"BL"` - `"KN"` - `"LC"` - `"MF"` - `"PM"` - `"VC"` - `"SA"` - `"SN"` - `"RS"` - `"ME"` - `"SL"` - `"SG"` - `"SK"` - `"SI"` - `"SO"` - `"ZA"` - `"ES"` - `"LK"` - `"SR"` - `"SZ"` - `"SE"` - `"CH"` - `"TW"` - `"TZ"` - `"TH"` - `"TG"` - `"TT"` - `"TN"` - `"TR"` - `"TM"` - `"AE"` - `"TC"` - `"UG"` - `"UA"` - `"GB"` - `"US"` - `"PS"` - `"UY"` - `"UZ"` - `"VU"` - `"VE"` - `"VN"` - `"VI"` - `"WF"` - `"YE"` - `"ZM"` - `"ZW"` - `"JP"` - `"CA"` - `"IR"` - `"KP"` - `"SD"` - `"SY"` - `"ZB"` |
| **darrp_optimize**  integer | Time for running Dynamic Automatic Radio Resource Provisioning (DARRP) optimizations (0 - 86400 sec). |
| **darrp_optimize_schedules**  list / elements=dictionary | Firewall schedules for DARRP running time. DARRP will run periodically based on darrp-optimize within the schedules. Separate multiple schedule names with a space. |
| **name**  string / required | Schedule name. Source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name. |
| **device_holdoff**  integer | Lower limit of creation time of device for identification in minutes (0 - 60). |
| **device_idle**  integer | Upper limit of idle time of device for identification in minutes (0 - 14400). |
| **device_weight**  integer | Upper limit of confidence of device for identification (0 - 255). |
| **duplicate_ssid**  string | Enable/disable allowing Virtual Access Points (VAPs) to use the same SSID name in the same VDOM.  **Choices:**   - `"enable"` - `"disable"` |
| **fake_ssid_action**  list / elements=string | Actions taken for detected fake SSID.  **Choices:**   - `"log"` - `"suppress"` |
| **fapc_compatibility**  string | Enable/disable FAP-C series compatibility.  **Choices:**   - `"enable"` - `"disable"` |
| **firmware_provision_on_authorization**  string | Enable/disable automatic provisioning of latest firmware on authorization.  **Choices:**   - `"enable"` - `"disable"` |
| **offending_ssid**  list / elements=dictionary | Configure offending SSID. |
| **action**  list / elements=string | Actions taken for detected offending SSID.  **Choices:**   - `"log"` - `"suppress"` |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **ssid_pattern**  string | Define offending SSID pattern (case insensitive). For example, word, word\*, \*word, wo\*rd. |
| **phishing_ssid_detect**  string | Enable/disable phishing SSID detection.  **Choices:**   - `"enable"` - `"disable"` |
| **wfa_compatibility**  string | Enable/disable WFA compatibility.  **Choices:**   - `"enable"` - `"disable"` |

## [Notes](fortios_wireless_controller_setting_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_setting_module.md#id5)

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
  - name: VDOM wireless controller configuration.
    fortios_wireless_controller_setting:
      vdom:  "{{ vdom }}"
      wireless_controller_setting:
        account_id: "<your_own_value>"
        country: "--"
        darrp_optimize: "86400"
        darrp_optimize_schedules:
         -
            name: "default_name_7 (source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name)"
        device_holdoff: "5"
        device_idle: "1440"
        device_weight: "1"
        duplicate_ssid: "enable"
        fake_ssid_action: "log"
        fapc_compatibility: "enable"
        firmware_provision_on_authorization: "enable"
        offending_ssid:
         -
            action: "log"
            id:  "17"
            ssid_pattern: "<your_own_value>"
        phishing_ssid_detect: "enable"
        wfa_compatibility: "enable"
```

## [Return Values](fortios_wireless_controller_setting_module.md#id6)

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
