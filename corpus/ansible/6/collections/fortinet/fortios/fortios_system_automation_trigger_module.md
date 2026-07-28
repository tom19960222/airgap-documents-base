---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_system_automation_trigger module – Trigger for automation stitches in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_system_automation_trigger_module.html
fetched_at: 2026-07-27T17:44:13+00:00
---
# fortinet.fortios.fortios_system_automation_trigger module – Trigger for automation stitches in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_automation_trigger_module.md#ansible-collections-fortinet-fortios-fortios-system-automation-trigger-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_automation_trigger`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_automation_trigger_module.md#synopsis)
- [Requirements](fortios_system_automation_trigger_module.md#requirements)
- [Parameters](fortios_system_automation_trigger_module.md#parameters)
- [Notes](fortios_system_automation_trigger_module.md#notes)
- [Examples](fortios_system_automation_trigger_module.md#examples)
- [Return Values](fortios_system_automation_trigger_module.md#return-values)

## [Synopsis](fortios_system_automation_trigger_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and automation_trigger category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_automation_trigger_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_system_automation_trigger_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **system_automation_trigger**  dictionary | Trigger for automation stitches. |
| **description**  string | Description. |
| **event_type**  string | Event type.  Choices:   - `"ioc"` - `"event-log"` - `"reboot"` - `"low-memory"` - `"high-cpu"` - `"license-near-expiry"` - `"local-cert-near-expiry"` - `"ha-failover"` - `"config-change"` - `"security-rating-summary"` - `"virus-ips-db-updated"` - `"faz-event"` - `"incoming-webhook"` - `"fabric-event"` - `"ips-logs"` - `"anomaly-logs"` - `"virus-logs"` - `"ssh-logs"` - `"webfilter-violation"` - `"traffic-violation"` |
| **fabric_event_name**  string | Fabric connector event handler name. |
| **fabric_event_severity**  string | Fabric connector event severity. |
| **faz_event_name**  string | FortiAnalyzer event handler name. |
| **faz_event_severity**  string | FortiAnalyzer event severity. |
| **faz_event_tags**  string | FortiAnalyzer event tags. |
| **fields**  list / elements=dictionary | Customized trigger field settings. |
| **id**  integer | Entry ID. |
| **name**  string | Name. |
| **value**  string | Value. |
| **ioc_level**  string | IOC threat level.  Choices:   - `"medium"` - `"high"` |
| **license_type**  string | License type.  Choices:   - `"forticare-support"` - `"fortiguard-webfilter"` - `"fortiguard-antispam"` - `"fortiguard-antivirus"` - `"fortiguard-ips"` - `"fortiguard-management"` - `"forticloud"` - `"any"` |
| **logid**  list / elements=dictionary | Log IDs to trigger event. |
| **id**  integer | Log ID. |
| **name**  string / required | Name. |
| **report_type**  string | Security Rating report.  Choices:   - `"posture"` - `"coverage"` - `"optimization"` - `"any"` - `"PostureReport"` - `"CoverageReport"` - `"OptimizationReport"` |
| **serial**  string | Fabric connector serial number. |
| **trigger_datetime**  string | Trigger date and time (YYYY-MM-DD HH:MM:SS). |
| **trigger_day**  integer | Day within a month to trigger. |
| **trigger_frequency**  string | Scheduled trigger frequency .  Choices:   - `"hourly"` - `"daily"` - `"weekly"` - `"monthly"` - `"once"` |
| **trigger_hour**  integer | Hour of the day on which to trigger (0 - 23). |
| **trigger_minute**  integer | Minute of the hour on which to trigger (0 - 59). |
| **trigger_type**  string | Trigger type.  Choices:   - `"event-based"` - `"scheduled"` |
| **trigger_weekday**  string | Day of week for trigger.  Choices:   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **vdom**  list / elements=dictionary | Virtual domain(s) that this trigger is valid for. |
| **name**  string | Virtual domain name. Source system.vdom.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_system_automation_trigger_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_automation_trigger_module.md#id5)

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
  - name: Trigger for automation stitches.
    fortios_system_automation_trigger:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_automation_trigger:
        description: "<your_own_value>"
        event_type: "ioc"
        fabric_event_name: "<your_own_value>"
        fabric_event_severity: "<your_own_value>"
        faz_event_name: "<your_own_value>"
        faz_event_severity: "<your_own_value>"
        faz_event_tags: "<your_own_value>"
        fields:
         -
            id:  "11"
            name: "default_name_12"
            value: "<your_own_value>"
        ioc_level: "medium"
        license_type: "forticare-support"
        logid:
         -
            id:  "17"
        name: "default_name_18"
        report_type: "posture"
        serial: "<your_own_value>"
        trigger_datetime: "<your_own_value>"
        trigger_day: "1"
        trigger_frequency: "hourly"
        trigger_hour: "0"
        trigger_minute: "0"
        trigger_type: "event-based"
        trigger_weekday: "sunday"
        vdom:
         -
            name: "default_name_29 (source system.vdom.name)"
```

## [Return Values](fortios_system_automation_trigger_module.md#id6)

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
