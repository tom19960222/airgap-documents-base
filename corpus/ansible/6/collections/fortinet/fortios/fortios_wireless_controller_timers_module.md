---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_wireless_controller_timers module – Configure CAPWAP timers in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_wireless_controller_timers_module.html
fetched_at: 2026-07-27T17:47:22+00:00
---
# fortinet.fortios.fortios_wireless_controller_timers module – Configure CAPWAP timers in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_timers_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-timers-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_timers`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_timers_module.md#synopsis)
- [Requirements](fortios_wireless_controller_timers_module.md#requirements)
- [Parameters](fortios_wireless_controller_timers_module.md#parameters)
- [Notes](fortios_wireless_controller_timers_module.md#notes)
- [Examples](fortios_wireless_controller_timers_module.md#examples)
- [Return Values](fortios_wireless_controller_timers_module.md#return-values)

## [Synopsis](fortios_wireless_controller_timers_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and timers category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_timers_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_wireless_controller_timers_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **wireless_controller_timers**  dictionary | Configure CAPWAP timers. |
| **auth_timeout**  integer | Time after which a client is considered failed in RADIUS authentication and times out (5 - 30 sec). |
| **ble_scan_report_intv**  integer | Time between running Bluetooth Low Energy (BLE) reports (10 - 3600 sec). |
| **client_idle_rehome_timeout**  integer | Time after which a client is considered idle and disconnected from the home controller (2 - 3600 sec). |
| **client_idle_timeout**  integer | Time after which a client is considered idle and times out (20 - 3600 sec). |
| **darrp_day**  string | Weekday on which to run DARRP optimization.  Choices:   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **darrp_optimize**  integer | Time for running Dynamic Automatic Radio Resource Provisioning (DARRP) optimizations (0 - 86400 sec). |
| **darrp_time**  list / elements=dictionary | Time at which DARRP optimizations run (you can add up to 8 times). |
| **time**  string | Time. |
| **discovery_interval**  integer | Time between discovery requests (2 - 180 sec). |
| **drma_interval**  integer | Dynamic radio mode assignment (DRMA) schedule interval in minutes (10 - 1440). |
| **echo_interval**  integer | Time between echo requests sent by the managed WTP, AP, or FortiAP (1 - 255 sec). |
| **fake_ap_log**  integer | Time between recording logs about fake APs if periodic fake AP logging is configured (0 - 1440 min). |
| **ipsec_intf_cleanup**  integer | Time period to keep IPsec VPN interfaces up after WTP sessions are disconnected (30 - 3600 sec). |
| **radio_stats_interval**  integer | Time between running radio reports (1 - 255 sec). |
| **rogue_ap_cleanup**  integer | Time period in minutes to keep rogue AP after it is gone . |
| **rogue_ap_log**  integer | Time between logging rogue AP messages if periodic rogue AP logging is configured (0 - 1440 min). |
| **sta_capability_interval**  integer | Time between running station capability reports (1 - 255 sec). |
| **sta_locate_timer**  integer | Time between running client presence flushes to remove clients that are listed but no longer present (0 - 86400 sec). |
| **sta_stats_interval**  integer | Time between running client (station) reports (1 - 255 sec). |
| **vap_stats_interval**  integer | Time between running Virtual Access Point (VAP) reports (1 - 255 sec). |

## [Notes](fortios_wireless_controller_timers_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_timers_module.md#id5)

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
  - name: Configure CAPWAP timers.
    fortios_wireless_controller_timers:
      vdom:  "{{ vdom }}"
      wireless_controller_timers:
        auth_timeout: "5"
        ble_scan_report_intv: "30"
        client_idle_rehome_timeout: "20"
        client_idle_timeout: "300"
        darrp_day: "sunday"
        darrp_optimize: "43200"
        darrp_time:
         -
            time: "<your_own_value>"
        discovery_interval: "5"
        drma_interval: "60"
        echo_interval: "30"
        fake_ap_log: "1"
        ipsec_intf_cleanup: "120"
        radio_stats_interval: "15"
        rogue_ap_cleanup: "0"
        rogue_ap_log: "0"
        sta_capability_interval: "30"
        sta_locate_timer: "1800"
        sta_stats_interval: "1"
        vap_stats_interval: "15"
```

## [Return Values](fortios_wireless_controller_timers_module.md#id6)

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
