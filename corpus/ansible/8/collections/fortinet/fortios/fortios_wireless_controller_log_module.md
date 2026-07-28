---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_wireless_controller_log module – Configure wireless controller event log filters in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_wireless_controller_log_module.html
fetched_at: 2026-07-28T02:31:17+00:00
---
# fortinet.fortios.fortios_wireless_controller_log module – Configure wireless controller event log filters in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_log_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-log-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_log`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_log_module.md#synopsis)
- [Requirements](fortios_wireless_controller_log_module.md#requirements)
- [Parameters](fortios_wireless_controller_log_module.md#parameters)
- [Notes](fortios_wireless_controller_log_module.md#notes)
- [Examples](fortios_wireless_controller_log_module.md#examples)
- [Return Values](fortios_wireless_controller_log_module.md#return-values)

## [Synopsis](fortios_wireless_controller_log_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and log category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_log_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_wireless_controller_log_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **wireless_controller_log**  dictionary | Configure wireless controller event log filters. |
| **addrgrp_log**  string | Lowest severity level to log address group message.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **ble_log**  string | Lowest severity level to log BLE detection message.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **clb_log**  string | Lowest severity level to log client load balancing message.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **dhcp_starv_log**  string | Lowest severity level to log DHCP starvation event message.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **led_sched_log**  string | Lowest severity level to log LED schedule event message.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **radio_event_log**  string | Lowest severity level to log radio event message.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **rogue_event_log**  string | Lowest severity level to log rogue AP event message.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **sta_event_log**  string | Lowest severity level to log station event message.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **sta_locate_log**  string | Lowest severity level to log station locate message.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **status**  string | Enable/disable wireless event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **wids_log**  string | Lowest severity level to log WIDS message.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **wtp_event_log**  string | Lowest severity level to log WTP event message.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |

## [Notes](fortios_wireless_controller_log_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_log_module.md#id5)

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
  - name: Configure wireless controller event log filters.
    fortios_wireless_controller_log:
      vdom:  "{{ vdom }}"
      wireless_controller_log:
        addrgrp_log: "emergency"
        ble_log: "emergency"
        clb_log: "emergency"
        dhcp_starv_log: "emergency"
        led_sched_log: "emergency"
        radio_event_log: "emergency"
        rogue_event_log: "emergency"
        sta_event_log: "emergency"
        sta_locate_log: "emergency"
        status: "enable"
        wids_log: "emergency"
        wtp_event_log: "emergency"
```

## [Return Values](fortios_wireless_controller_log_module.md#id6)

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
