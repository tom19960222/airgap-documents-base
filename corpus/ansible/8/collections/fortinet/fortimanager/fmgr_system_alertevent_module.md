---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_alertevent module – Alert events."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_alertevent_module.html
fetched_at: 2026-07-28T02:18:08+00:00
---
# fortinet.fortimanager.fmgr_system_alertevent module – Alert events.

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_alertevent`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_alertevent_module.md#synopsis)
- [Parameters](fmgr_system_alertevent_module.md#parameters)
- [Notes](fmgr_system_alertevent_module.md#notes)
- [Examples](fmgr_system_alertevent_module.md#examples)
- [Return Values](fmgr_system_alertevent_module.md#return-values)

## [Synopsis](fmgr_system_alertevent_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_alertevent_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **system_alertevent**  dictionary | the top level parameters set |
| **alert-destination**  list / elements=dictionary | Alert-Destination. |
| **from**  string | Sender email address to use in alert emails. |
| **smtp-name**  string | SMTP server name. |
| **snmp-name**  string | SNMP trap name. |
| **syslog-name**  string | Syslog server name. |
| **to**  string | Recipient email address to use in alert emails. |
| **type**  string | Destination type.  mail - Send email alert.  snmp - Send SNMP trap.  syslog - Send syslog message.  **Choices:**   - `"mail"` - `"snmp"` - `"syslog"` |
| **enable-generic-text**  list / elements=string | Enable/disable generic text match.  enable - Enable setting.  disable - Disable setting.  **Choices:**   - `"enable"` - `"disable"` |
| **enable-severity-filter**  list / elements=string | Enable/disable alert severity filter.  enable - Enable setting.  disable - Disable setting.  **Choices:**   - `"enable"` - `"disable"` |
| **event-time-period**  string | Time period      1 - 1 hour.  3 - 3 hours.  6 - 6 hours.  12 - 12 hours.  24 - 1 day.  72 - 3 days.  168 - 1 week.  **Choices:**   - `"0.5"` - `"1"` - `"3"` - `"6"` - `"12"` - `"24"` - `"72"` - `"168"` |
| **generic-text**  string | Text that must be contained in a log to trigger alert. |
| **name**  string / required | Alert name. |
| **num-events**  string | Minimum number of events required within time period.  1 - 1 event.  5 - 5 events.  10 - 10 events.  50 - 50 events.  100 - 100 events.  **Choices:**   - `"1"` - `"5"` - `"10"` - `"50"` - `"100"` |
| **severity-filter**  string | Required log severity to trigger alert.  high - High level alert.  medium-high - Medium-high level alert.  medium - Medium level alert.  medium-low - Medium-low level alert.  low - Low level alert.  **Choices:**   - `"high"` - `"medium-high"` - `"medium"` - `"medium-low"` - `"low"` |
| **severity-level-comp**  list / elements=string | Log severity threshold comparison criterion.  **Choices:**   - `">="` - `"="` - `"<="` |
| **severity-level-logs**  list / elements=string | Log severity threshold level.  no-check - Do not check severity level for this log type.  information - Information level.  notify - Notify level.  warning - Warning level.  error - Error level.  critical - Critical level.  alert - Alert level.  emergency - Emergency level.  **Choices:**   - `"no-check"` - `"information"` - `"notify"` - `"warning"` - `"error"` - `"critical"` - `"alert"` - `"emergency"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_alertevent_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_alertevent_module.md#id4)

```yaml+jinja
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Alert events.
     fmgr_system_alertevent:
        bypass_validation: False
        state: present
        system_alertevent:
           enable-generic-text:
             - enable
             - disable
           enable-severity-filter:
             - enable
             - disable
           event-time-period: 1 #<value in [0.5, 1, 3, ...]>
           name: ansible-test-sysalert
           num-events: 1 #<value in [1, 5, 10, ...]>
           severity-filter: high #<value in [high, medium-high, medium, ...]>
           #severity-level-comp:
           #  - <=
           severity-level-logs:
             - no-check
             - information
             - notify
             - warning
             - error
             - critical
             - alert
             - emergency

- name: gathering fortimanager facts
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: retrieve all the alert events
     fmgr_fact:
       facts:
           selector: 'system_alertevent'
           params:
               alert-event: 'your_value'
```

## [Return Values](fmgr_system_alertevent_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
