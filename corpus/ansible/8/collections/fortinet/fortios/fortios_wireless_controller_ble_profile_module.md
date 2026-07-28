---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_wireless_controller_ble_profile module – Configure Bluetooth Low Energy profile in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_wireless_controller_ble_profile_module.html
fetched_at: 2026-07-28T02:31:02+00:00
---
# fortinet.fortios.fortios_wireless_controller_ble_profile module – Configure Bluetooth Low Energy profile in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_ble_profile_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-ble-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_ble_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_ble_profile_module.md#synopsis)
- [Requirements](fortios_wireless_controller_ble_profile_module.md#requirements)
- [Parameters](fortios_wireless_controller_ble_profile_module.md#parameters)
- [Notes](fortios_wireless_controller_ble_profile_module.md#notes)
- [Examples](fortios_wireless_controller_ble_profile_module.md#examples)
- [Return Values](fortios_wireless_controller_ble_profile_module.md#return-values)

## [Synopsis](fortios_wireless_controller_ble_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and ble_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_ble_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_wireless_controller_ble_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **wireless_controller_ble_profile**  dictionary | Configure Bluetooth Low Energy profile. |
| **advertising**  list / elements=string | Advertising type.  **Choices:**   - `"ibeacon"` - `"eddystone-uid"` - `"eddystone-url"` |
| **beacon_interval**  integer | Beacon interval . |
| **ble_scanning**  string | Enable/disable Bluetooth Low Energy (BLE) scanning.  **Choices:**   - `"enable"` - `"disable"` |
| **comment**  string | Comment. |
| **eddystone_instance**  string | Eddystone instance ID. |
| **eddystone_namespace**  string | Eddystone namespace ID. |
| **eddystone_url**  string | Eddystone URL. |
| **eddystone_url_encode_hex**  string | Eddystone encoded URL hexadecimal string |
| **ibeacon_uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **major_id**  integer | Major ID. |
| **minor_id**  integer | Minor ID. |
| **name**  string / required | Bluetooth Low Energy profile name. |
| **scan_interval**  integer | Scan Interval . |
| **scan_period**  integer | Scan Period . |
| **scan_threshold**  string | Minimum signal level/threshold in dBm required for the AP to report detected BLE device (-95 to -20). |
| **scan_time**  integer | Scan Time . |
| **scan_type**  string | Scan Type .  **Choices:**   - `"active"` - `"passive"` |
| **scan_window**  integer | Scan Windows . |
| **txpower**  string | Transmit power level .  **Choices:**   - `"0"` - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` - `"6"` - `"7"` - `"8"` - `"9"` - `"10"` - `"11"` - `"12"` |

## [Notes](fortios_wireless_controller_ble_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_ble_profile_module.md#id5)

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
  - name: Configure Bluetooth Low Energy profile.
    fortios_wireless_controller_ble_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_ble_profile:
        advertising: "ibeacon"
        beacon_interval: "100"
        ble_scanning: "enable"
        comment: "Comment."
        eddystone_instance: "<your_own_value>"
        eddystone_namespace: "<your_own_value>"
        eddystone_url: "<your_own_value>"
        eddystone_url_encode_hex: "<your_own_value>"
        ibeacon_uuid: "<your_own_value>"
        major_id: "1000"
        minor_id: "2000"
        name: "default_name_14"
        scan_interval: "50"
        scan_period: "4000"
        scan_threshold: "<your_own_value>"
        scan_time: "1000"
        scan_type: "active"
        scan_window: "50"
        txpower: "0"
```

## [Return Values](fortios_wireless_controller_ble_profile_module.md#id6)

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
