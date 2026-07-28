---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_log_setting module – Configure general log settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_log_setting_module.html
fetched_at: 2026-07-28T02:26:09+00:00
---
# fortinet.fortios.fortios_log_setting module – Configure general log settings in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_log_setting_module.md#ansible-collections-fortinet-fortios-fortios-log-setting-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_log_setting`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_log_setting_module.md#synopsis)
- [Requirements](fortios_log_setting_module.md#requirements)
- [Parameters](fortios_log_setting_module.md#parameters)
- [Notes](fortios_log_setting_module.md#notes)
- [Examples](fortios_log_setting_module.md#examples)
- [Return Values](fortios_log_setting_module.md#return-values)

## [Synopsis](fortios_log_setting_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify log feature and setting category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_log_setting_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_log_setting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **log_setting**  dictionary | Configure general log settings. |
| **anonymization_hash**  string | User name anonymization hash salt. |
| **brief_traffic_format**  string | Enable/disable brief format traffic logging.  **Choices:**   - `"enable"` - `"disable"` |
| **custom_log_fields**  list / elements=dictionary | Custom fields to append to all log messages. |
| **field_id**  string / required | Custom log field. Source log.custom-field.id. |
| **daemon_log**  string | Enable/disable daemon logging.  **Choices:**   - `"enable"` - `"disable"` |
| **expolicy_implicit_log**  string | Enable/disable explicit proxy firewall implicit policy logging.  **Choices:**   - `"enable"` - `"disable"` |
| **extended_log**  string | Enable/disable extended traffic logging.  **Choices:**   - `"enable"` - `"disable"` |
| **faz_override**  string | Enable/disable override FortiAnalyzer settings.  **Choices:**   - `"enable"` - `"disable"` |
| **fortiview_weekly_data**  string | Enable/disable FortiView weekly data.  **Choices:**   - `"enable"` - `"disable"` |
| **fwpolicy6_implicit_log**  string | Enable/disable implicit firewall policy6 logging.  **Choices:**   - `"enable"` - `"disable"` |
| **fwpolicy_implicit_log**  string | Enable/disable implicit firewall policy logging.  **Choices:**   - `"enable"` - `"disable"` |
| **local_in_allow**  string | Enable/disable local-in-allow logging.  **Choices:**   - `"enable"` - `"disable"` |
| **local_in_deny_broadcast**  string | Enable/disable local-in-deny-broadcast logging.  **Choices:**   - `"enable"` - `"disable"` |
| **local_in_deny_unicast**  string | Enable/disable local-in-deny-unicast logging.  **Choices:**   - `"enable"` - `"disable"` |
| **local_out**  string | Enable/disable local-out logging.  **Choices:**   - `"enable"` - `"disable"` |
| **local_out_ioc_detection**  string | Enable/disable local-out traffic IoC detection. Requires local-out to be enabled.  **Choices:**   - `"enable"` - `"disable"` |
| **log_invalid_packet**  string | Enable/disable invalid packet traffic logging.  **Choices:**   - `"enable"` - `"disable"` |
| **log_policy_comment**  string | Enable/disable inserting policy comments into traffic logs.  **Choices:**   - `"enable"` - `"disable"` |
| **log_policy_name**  string | Enable/disable inserting policy name into traffic logs.  **Choices:**   - `"enable"` - `"disable"` |
| **log_user_in_upper**  string | Enable/disable logs with user-in-upper.  **Choices:**   - `"enable"` - `"disable"` |
| **neighbor_event**  string | Enable/disable neighbor event logging.  **Choices:**   - `"enable"` - `"disable"` |
| **resolve_ip**  string | Enable/disable adding resolved domain names to traffic logs if possible.  **Choices:**   - `"enable"` - `"disable"` |
| **resolve_port**  string | Enable/disable adding resolved service names to traffic logs.  **Choices:**   - `"enable"` - `"disable"` |
| **rest_api_get**  string | Enable/disable REST API GET request logging.  **Choices:**   - `"enable"` - `"disable"` |
| **rest_api_set**  string | Enable/disable REST API POST/PUT/DELETE request logging.  **Choices:**   - `"enable"` - `"disable"` |
| **syslog_override**  string | Enable/disable override Syslog settings.  **Choices:**   - `"enable"` - `"disable"` |
| **user_anonymize**  string | Enable/disable anonymizing user names in log messages.  **Choices:**   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_log_setting_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_log_setting_module.md#id5)

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
  - name: Configure general log settings.
    fortios_log_setting:
      vdom:  "{{ vdom }}"
      log_setting:
        anonymization_hash: "<your_own_value>"
        brief_traffic_format: "enable"
        custom_log_fields:
         -
            field_id: "<your_own_value> (source log.custom-field.id)"
        daemon_log: "enable"
        expolicy_implicit_log: "enable"
        extended_log: "enable"
        faz_override: "enable"
        fortiview_weekly_data: "enable"
        fwpolicy_implicit_log: "enable"
        fwpolicy6_implicit_log: "enable"
        local_in_allow: "enable"
        local_in_deny_broadcast: "enable"
        local_in_deny_unicast: "enable"
        local_out: "enable"
        local_out_ioc_detection: "enable"
        log_invalid_packet: "enable"
        log_policy_comment: "enable"
        log_policy_name: "enable"
        log_user_in_upper: "enable"
        neighbor_event: "enable"
        resolve_ip: "enable"
        resolve_port: "enable"
        rest_api_get: "enable"
        rest_api_set: "enable"
        syslog_override: "enable"
        user_anonymize: "enable"
```

## [Return Values](fortios_log_setting_module.md#id6)

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
