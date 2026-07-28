---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_alertemail_setting module – Configure alert email settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_alertemail_setting_module.html
fetched_at: 2026-07-27T17:39:49+00:00
---
# fortinet.fortios.fortios_alertemail_setting module – Configure alert email settings in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_alertemail_setting_module.md#ansible-collections-fortinet-fortios-fortios-alertemail-setting-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_alertemail_setting`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_alertemail_setting_module.md#synopsis)
- [Requirements](fortios_alertemail_setting_module.md#requirements)
- [Parameters](fortios_alertemail_setting_module.md#parameters)
- [Notes](fortios_alertemail_setting_module.md#notes)
- [Examples](fortios_alertemail_setting_module.md#examples)
- [Return Values](fortios_alertemail_setting_module.md#return-values)

## [Synopsis](fortios_alertemail_setting_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify alertemail feature and setting category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_alertemail_setting_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_alertemail_setting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **alertemail_setting**  dictionary | Configure alert email settings. |
| **admin_login_logs**  string | Enable/disable administrator login/logout logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **alert_interval**  integer | Alert alert interval in minutes. |
| **amc_interface_bypass_mode**  string | Enable/disable Fortinet Advanced Mezzanine Card (AMC) interface bypass mode logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **antivirus_logs**  string | Enable/disable antivirus logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **configuration_changes_logs**  string | Enable/disable configuration change logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **critical_interval**  integer | Critical alert interval in minutes. |
| **debug_interval**  integer | Debug alert interval in minutes. |
| **email_interval**  integer | Interval between sending alert emails (1 - 99999 min). |
| **emergency_interval**  integer | Emergency alert interval in minutes. |
| **error_interval**  integer | Error alert interval in minutes. |
| **FDS_license_expiring_days**  integer | Number of days to send alert email prior to FortiGuard license expiration (1 - 100 days). |
| **FDS_license_expiring_warning**  string | Enable/disable FortiGuard license expiration warnings in alert email.  Choices:   - `"enable"` - `"disable"` |
| **FDS_update_logs**  string | Enable/disable FortiGuard update logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **filter_mode**  string | How to filter log messages that are sent to alert emails.  Choices:   - `"category"` - `"threshold"` |
| **FIPS_CC_errors**  string | Enable/disable FIPS and Common Criteria error logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **firewall_authentication_failure_logs**  string | Enable/disable firewall authentication failure logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **fortiguard_log_quota_warning**  string | Enable/disable FortiCloud log quota warnings in alert email.  Choices:   - `"enable"` - `"disable"` |
| **FSSO_disconnect_logs**  string | Enable/disable logging of FSSO collector agent disconnect.  Choices:   - `"enable"` - `"disable"` |
| **HA_logs**  string | Enable/disable HA logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **information_interval**  integer | Information alert interval in minutes. |
| **IPS_logs**  string | Enable/disable IPS logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **IPsec_errors_logs**  string | Enable/disable IPsec error logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **local_disk_usage**  integer | Disk usage percentage at which to send alert email (1 - 99 percent). |
| **log_disk_usage_warning**  string | Enable/disable disk usage warnings in alert email.  Choices:   - `"enable"` - `"disable"` |
| **mailto1**  string | Email address to send alert email to (usually a system administrator) (max. 63 characters). |
| **mailto2**  string | Optional second email address to send alert email to (max. 63 characters). |
| **mailto3**  string | Optional third email address to send alert email to (max. 63 characters). |
| **notification_interval**  integer | Notification alert interval in minutes. |
| **PPP_errors_logs**  string | Enable/disable PPP error logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **severity**  string | Lowest severity level to log.  Choices:   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **ssh_logs**  string | Enable/disable SSH logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **sslvpn_authentication_errors_logs**  string | Enable/disable SSL-VPN authentication error logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **username**  string | Name that appears in the From: field of alert emails (max. 63 characters). |
| **violation_traffic_logs**  string | Enable/disable violation traffic logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **warning_interval**  integer | Warning alert interval in minutes. |
| **webfilter_logs**  string | Enable/disable web filter logs in alert email.  Choices:   - `"enable"` - `"disable"` |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_alertemail_setting_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_alertemail_setting_module.md#id5)

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
  - name: Configure alert email settings.
    fortios_alertemail_setting:
      vdom:  "{{ vdom }}"
      alertemail_setting:
        admin_login_logs: "enable"
        alert_interval: "2"
        amc_interface_bypass_mode: "enable"
        antivirus_logs: "enable"
        configuration_changes_logs: "enable"
        critical_interval: "3"
        debug_interval: "60"
        email_interval: "5"
        emergency_interval: "1"
        error_interval: "5"
        FDS_license_expiring_days: "15"
        FDS_license_expiring_warning: "enable"
        FDS_update_logs: "enable"
        filter_mode: "category"
        FIPS_CC_errors: "enable"
        firewall_authentication_failure_logs: "enable"
        fortiguard_log_quota_warning: "enable"
        FSSO_disconnect_logs: "enable"
        HA_logs: "enable"
        information_interval: "30"
        IPS_logs: "enable"
        IPsec_errors_logs: "enable"
        local_disk_usage: "75"
        log_disk_usage_warning: "enable"
        mailto1: "<your_own_value>"
        mailto2: "<your_own_value>"
        mailto3: "<your_own_value>"
        notification_interval: "20"
        PPP_errors_logs: "enable"
        severity: "emergency"
        ssh_logs: "enable"
        sslvpn_authentication_errors_logs: "enable"
        username: "<your_own_value>"
        violation_traffic_logs: "enable"
        warning_interval: "10"
        webfilter_logs: "enable"
```

## [Return Values](fortios_alertemail_setting_module.md#id6)

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
