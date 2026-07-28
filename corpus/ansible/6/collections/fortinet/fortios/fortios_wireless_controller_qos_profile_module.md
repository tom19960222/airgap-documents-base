---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_wireless_controller_qos_profile module – Configure WiFi quality of service (QoS) profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_wireless_controller_qos_profile_module.html
fetched_at: 2026-07-27T17:47:16+00:00
---
# fortinet.fortios.fortios_wireless_controller_qos_profile module – Configure WiFi quality of service (QoS) profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_qos_profile_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-qos-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_qos_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_qos_profile_module.md#synopsis)
- [Requirements](fortios_wireless_controller_qos_profile_module.md#requirements)
- [Parameters](fortios_wireless_controller_qos_profile_module.md#parameters)
- [Notes](fortios_wireless_controller_qos_profile_module.md#notes)
- [Examples](fortios_wireless_controller_qos_profile_module.md#examples)
- [Return Values](fortios_wireless_controller_qos_profile_module.md#return-values)

## [Synopsis](fortios_wireless_controller_qos_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and qos_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_qos_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_wireless_controller_qos_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **wireless_controller_qos_profile**  dictionary | Configure WiFi quality of service (QoS) profiles. |
| **bandwidth_admission_control**  string | Enable/disable WMM bandwidth admission control.  Choices:   - `"enable"` - `"disable"` |
| **bandwidth_capacity**  integer | Maximum bandwidth capacity allowed (1 - 600000 Kbps). |
| **burst**  string | Enable/disable client rate burst.  Choices:   - `"enable"` - `"disable"` |
| **call_admission_control**  string | Enable/disable WMM call admission control.  Choices:   - `"enable"` - `"disable"` |
| **call_capacity**  integer | Maximum number of Voice over WLAN (VoWLAN) phones allowed (0 - 60). |
| **comment**  string | Comment. |
| **downlink**  integer | Maximum downlink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps). |
| **downlink_sta**  integer | Maximum downlink bandwidth for clients (0 - 2097152 Kbps). |
| **dscp_wmm_be**  list / elements=dictionary | DSCP mapping for best effort access . |
| **id**  integer | DSCP WMM mapping numbers (0 - 63). |
| **dscp_wmm_bk**  list / elements=dictionary | DSCP mapping for background access . |
| **id**  integer | DSCP WMM mapping numbers (0 - 63). |
| **dscp_wmm_mapping**  string | Enable/disable Differentiated Services Code Point (DSCP) mapping.  Choices:   - `"enable"` - `"disable"` |
| **dscp_wmm_vi**  list / elements=dictionary | DSCP mapping for video access . |
| **id**  integer | DSCP WMM mapping numbers (0 - 63). |
| **dscp_wmm_vo**  list / elements=dictionary | DSCP mapping for voice access . |
| **id**  integer | DSCP WMM mapping numbers (0 - 63). |
| **name**  string / required | WiFi QoS profile name. |
| **uplink**  integer | Maximum uplink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps). |
| **uplink_sta**  integer | Maximum uplink bandwidth for clients (0 - 2097152 Kbps). |
| **wmm**  string | Enable/disable WiFi multi-media (WMM) control.  Choices:   - `"enable"` - `"disable"` |
| **wmm_be_dscp**  integer | DSCP marking for best effort access . |
| **wmm_bk_dscp**  integer | DSCP marking for background access . |
| **wmm_dscp_marking**  string | Enable/disable WMM Differentiated Services Code Point (DSCP) marking.  Choices:   - `"enable"` - `"disable"` |
| **wmm_uapsd**  string | Enable/disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode.  Choices:   - `"enable"` - `"disable"` |
| **wmm_vi_dscp**  integer | DSCP marking for video access . |
| **wmm_vo_dscp**  integer | DSCP marking for voice access . |

## [Notes](fortios_wireless_controller_qos_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_qos_profile_module.md#id5)

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
  - name: Configure WiFi quality of service (QoS) profiles.
    fortios_wireless_controller_qos_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_qos_profile:
        bandwidth_admission_control: "enable"
        bandwidth_capacity: "2000"
        burst: "enable"
        call_admission_control: "enable"
        call_capacity: "10"
        comment: "Comment."
        downlink: "0"
        downlink_sta: "0"
        dscp_wmm_be:
         -
            id:  "12"
        dscp_wmm_bk:
         -
            id:  "14"
        dscp_wmm_mapping: "enable"
        dscp_wmm_vi:
         -
            id:  "17"
        dscp_wmm_vo:
         -
            id:  "19"
        name: "default_name_20"
        uplink: "0"
        uplink_sta: "0"
        wmm: "enable"
        wmm_be_dscp: "0"
        wmm_bk_dscp: "8"
        wmm_dscp_marking: "enable"
        wmm_uapsd: "enable"
        wmm_vi_dscp: "32"
        wmm_vo_dscp: "48"
```

## [Return Values](fortios_wireless_controller_qos_profile_module.md#id6)

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
