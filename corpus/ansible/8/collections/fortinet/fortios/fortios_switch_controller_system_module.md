---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_switch_controller_system module – Configure system-wide switch controller settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_switch_controller_system_module.html
fetched_at: 2026-07-28T02:27:44+00:00
---
# fortinet.fortios.fortios_switch_controller_system module – Configure system-wide switch controller settings in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_switch_controller_system_module.md#ansible-collections-fortinet-fortios-fortios-switch-controller-system-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_switch_controller_system`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_switch_controller_system_module.md#synopsis)
- [Requirements](fortios_switch_controller_system_module.md#requirements)
- [Parameters](fortios_switch_controller_system_module.md#parameters)
- [Notes](fortios_switch_controller_system_module.md#notes)
- [Examples](fortios_switch_controller_system_module.md#examples)
- [Return Values](fortios_switch_controller_system_module.md#return-values)

## [Synopsis](fortios_switch_controller_system_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify switch_controller feature and system category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_switch_controller_system_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_switch_controller_system_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **switch_controller_system**  dictionary | Configure system-wide switch controller settings. |
| **caputp_echo_interval**  integer | Echo interval for the caputp echo requests from swtp. |
| **caputp_max_retransmit**  integer | Maximum retransmission count for the caputp tunnel packets. |
| **data_sync_interval**  integer | Time interval between collection of switch data (30 - 1800 sec). |
| **dynamic_periodic_interval**  integer | Periodic time interval to run Dynamic port policy engine (5 - 60 sec). |
| **iot_holdoff**  integer | MAC entry”s creation time. Time must be greater than this value for an entry to be created (0 - 10080 mins). |
| **iot_mac_idle**  integer | MAC entry”s idle time. MAC entry is removed after this value (0 - 10080 mins). |
| **iot_scan_interval**  integer | IoT scan interval (2 - 10080 mins). |
| **iot_weight_threshold**  integer | MAC entry”s confidence value. Value is re-queried when below this value . |
| **nac_periodic_interval**  integer | Periodic time interval to run NAC engine (5 - 60 sec). |
| **parallel_process**  integer | Maximum number of parallel processes. |
| **parallel_process_override**  string | Enable/disable parallel process override.  **Choices:**   - `"disable"` - `"enable"` |
| **tunnel_mode**  string | Compatible/strict tunnel mode.  **Choices:**   - `"compatible"` - `"strict"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_switch_controller_system_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_switch_controller_system_module.md#id5)

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
  - name: Configure system-wide switch controller settings.
    fortios_switch_controller_system:
      vdom:  "{{ vdom }}"
      switch_controller_system:
        caputp_echo_interval: "30"
        caputp_max_retransmit: "5"
        data_sync_interval: "60"
        dynamic_periodic_interval: "60"
        iot_holdoff: "5"
        iot_mac_idle: "1440"
        iot_scan_interval: "60"
        iot_weight_threshold: "1"
        nac_periodic_interval: "60"
        parallel_process: "1"
        parallel_process_override: "disable"
        tunnel_mode: "compatible"
```

## [Return Values](fortios_switch_controller_system_module.md#id6)

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
