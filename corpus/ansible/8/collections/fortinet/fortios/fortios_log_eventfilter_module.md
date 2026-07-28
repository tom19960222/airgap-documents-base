---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_log_eventfilter module – Configure log event filters in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_log_eventfilter_module.html
fetched_at: 2026-07-28T02:25:48+00:00
---
# fortinet.fortios.fortios_log_eventfilter module – Configure log event filters in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_log_eventfilter_module.md#ansible-collections-fortinet-fortios-fortios-log-eventfilter-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_log_eventfilter`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_log_eventfilter_module.md#synopsis)
- [Requirements](fortios_log_eventfilter_module.md#requirements)
- [Parameters](fortios_log_eventfilter_module.md#parameters)
- [Notes](fortios_log_eventfilter_module.md#notes)
- [Examples](fortios_log_eventfilter_module.md#examples)
- [Return Values](fortios_log_eventfilter_module.md#return-values)

## [Synopsis](fortios_log_eventfilter_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify log feature and eventfilter category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_log_eventfilter_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_log_eventfilter_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **log_eventfilter**  dictionary | Configure log event filters. |
| **cifs**  string | Enable/disable CIFS logging.  **Choices:**   - `"enable"` - `"disable"` |
| **compliance_check**  string | Enable/disable PCI DSS compliance check logging.  **Choices:**   - `"enable"` - `"disable"` |
| **connector**  string | Enable/disable SDN connector logging.  **Choices:**   - `"enable"` - `"disable"` |
| **endpoint**  string | Enable/disable endpoint event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **event**  string | Enable/disable event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **fortiextender**  string | Enable/disable FortiExtender logging.  **Choices:**   - `"enable"` - `"disable"` |
| **ha**  string | Enable/disable ha event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **rest_api**  string | Enable/disable REST API logging.  **Choices:**   - `"enable"` - `"disable"` |
| **router**  string | Enable/disable router event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **sdwan**  string | Enable/disable SD-WAN logging.  **Choices:**   - `"enable"` - `"disable"` |
| **security_rating**  string | Enable/disable Security Rating result logging.  **Choices:**   - `"enable"` - `"disable"` |
| **switch_controller**  string | Enable/disable Switch-Controller logging.  **Choices:**   - `"enable"` - `"disable"` |
| **system**  string | Enable/disable system event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **user**  string | Enable/disable user authentication event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **vpn**  string | Enable/disable VPN event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **wan_opt**  string | Enable/disable WAN optimization event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **webproxy**  string | Enable/disable web proxy event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **wireless_activity**  string | Enable/disable wireless event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_log_eventfilter_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_log_eventfilter_module.md#id5)

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
  - name: Configure log event filters.
    fortios_log_eventfilter:
      vdom:  "{{ vdom }}"
      log_eventfilter:
        cifs: "enable"
        compliance_check: "enable"
        connector: "enable"
        endpoint: "enable"
        event: "enable"
        fortiextender: "enable"
        ha: "enable"
        rest_api: "enable"
        router: "enable"
        sdwan: "enable"
        security_rating: "enable"
        switch_controller: "enable"
        system: "enable"
        user: "enable"
        vpn: "enable"
        wan_opt: "enable"
        webproxy: "enable"
        wireless_activity: "enable"
```

## [Return Values](fortios_log_eventfilter_module.md#id6)

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
