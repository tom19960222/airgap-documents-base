---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_wireless_controller_arrp_profile module – Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_wireless_controller_arrp_profile_module.html
fetched_at: 2026-07-28T02:31:01+00:00
---
# fortinet.fortios.fortios_wireless_controller_arrp_profile module – Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_arrp_profile_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-arrp-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_arrp_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_arrp_profile_module.md#synopsis)
- [Requirements](fortios_wireless_controller_arrp_profile_module.md#requirements)
- [Parameters](fortios_wireless_controller_arrp_profile_module.md#parameters)
- [Notes](fortios_wireless_controller_arrp_profile_module.md#notes)
- [Examples](fortios_wireless_controller_arrp_profile_module.md#examples)
- [Return Values](fortios_wireless_controller_arrp_profile_module.md#return-values)

## [Synopsis](fortios_wireless_controller_arrp_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and arrp_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_arrp_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_wireless_controller_arrp_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **wireless_controller_arrp_profile**  dictionary | Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles. |
| **comment**  string | Comment. |
| **darrp_optimize**  integer | Time for running Dynamic Automatic Radio Resource Provisioning (DARRP) optimizations (0 - 86400 sec). |
| **darrp_optimize_schedules**  list / elements=dictionary | Firewall schedules for DARRP running time. DARRP will run periodically based on darrp-optimize within the schedules. Separate multiple schedule names with a space. |
| **name**  string / required | Schedule name. Source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name. |
| **include_dfs_channel**  string | Enable/disable use of DFS channel in DARRP channel selection phase 1 .  **Choices:**   - `"enable"` - `"disable"` - `"yes"` - `"no"` |
| **include_weather_channel**  string | Enable/disable use of weather channel in DARRP channel selection phase 1 .  **Choices:**   - `"enable"` - `"disable"` - `"yes"` - `"no"` |
| **monitor_period**  integer | Period in seconds to measure average transmit retries and receive errors . |
| **name**  string / required | WiFi ARRP profile name. |
| **override_darrp_optimize**  string | Enable to override setting darrp-optimize and darrp-optimize-schedules .  **Choices:**   - `"enable"` - `"disable"` |
| **selection_period**  integer | Period in seconds to measure average channel load, noise floor, spectral RSSI . |
| **threshold_ap**  integer | Threshold to reject channel in DARRP channel selection phase 1 due to surrounding APs (0 - 500). |
| **threshold_channel_load**  integer | Threshold in percentage to reject channel in DARRP channel selection phase 1 due to channel load (0 - 100). |
| **threshold_noise_floor**  string | Threshold in dBm to reject channel in DARRP channel selection phase 1 due to noise floor (-95 to -20). |
| **threshold_rx_errors**  integer | Threshold in percentage for receive errors to trigger channel reselection in DARRP monitor stage (0 - 100). |
| **threshold_spectral_rssi**  string | Threshold in dBm to reject channel in DARRP channel selection phase 1 due to spectral RSSI (-95 to -20). |
| **threshold_tx_retries**  integer | Threshold in percentage for transmit retries to trigger channel reselection in DARRP monitor stage (0 - 1000). |
| **weight_channel_load**  integer | Weight in DARRP channel score calculation for channel load (0 - 2000). |
| **weight_dfs_channel**  integer | Weight in DARRP channel score calculation for DFS channel (0 - 2000). |
| **weight_managed_ap**  integer | Weight in DARRP channel score calculation for managed APs (0 - 2000). |
| **weight_noise_floor**  integer | Weight in DARRP channel score calculation for noise floor (0 - 2000). |
| **weight_rogue_ap**  integer | Weight in DARRP channel score calculation for rogue APs (0 - 2000). |
| **weight_spectral_rssi**  integer | Weight in DARRP channel score calculation for spectral RSSI (0 - 2000). |
| **weight_weather_channel**  integer | Weight in DARRP channel score calculation for weather channel (0 - 2000). |

## [Notes](fortios_wireless_controller_arrp_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_arrp_profile_module.md#id5)

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
  - name: Configure WiFi Automatic Radio Resource Provisioning (ARRP) profiles.
    fortios_wireless_controller_arrp_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_arrp_profile:
        comment: "Comment."
        darrp_optimize: "86400"
        darrp_optimize_schedules:
         -
            name: "default_name_6 (source firewall.schedule.group.name firewall.schedule.recurring.name firewall.schedule.onetime.name)"
        include_dfs_channel: "enable"
        include_weather_channel: "enable"
        monitor_period: "300"
        name: "default_name_10"
        override_darrp_optimize: "enable"
        selection_period: "3600"
        threshold_ap: "250"
        threshold_channel_load: "60"
        threshold_noise_floor: "<your_own_value>"
        threshold_rx_errors: "50"
        threshold_spectral_rssi: "<your_own_value>"
        threshold_tx_retries: "300"
        weight_channel_load: "20"
        weight_dfs_channel: "500"
        weight_managed_ap: "50"
        weight_noise_floor: "40"
        weight_rogue_ap: "10"
        weight_spectral_rssi: "40"
        weight_weather_channel: "1000"
```

## [Return Values](fortios_wireless_controller_arrp_profile_module.md#id6)

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
