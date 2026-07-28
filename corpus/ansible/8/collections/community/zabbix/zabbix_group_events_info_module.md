---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_group_events_info module – Get all triggers about a Zabbix group"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_group_events_info_module.html
fetched_at: 2026-07-28T02:02:43+00:00
---
# community.zabbix.zabbix_group_events_info module – Get all triggers about a Zabbix group

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/ui/repo/published/community/zabbix/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_group_events_info_module.md#ansible-collections-community-zabbix-zabbix-group-events-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_group_events_info`.

- [Synopsis](zabbix_group_events_info_module.md#synopsis)
- [Requirements](zabbix_group_events_info_module.md#requirements)
- [Parameters](zabbix_group_events_info_module.md#parameters)
- [Examples](zabbix_group_events_info_module.md#examples)
- [Return Values](zabbix_group_events_info_module.md#return-values)

## [Synopsis](zabbix_group_events_info_module.md#id1)

- This module allows you to check the state of triggers of all hosts in a Zabbix hostgroup.

## [Requirements](zabbix_group_events_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_group_events_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostgroup_name**  list / elements=string / required | Name of the hostgroup in Zabbix. |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **trigger_severity**  string | Zabbix severity for search filter  **Choices:**   - `"not_classified"` - `"information"` - `"warning"` - `"average"` ← (default) - `"high"` - `"disaster"` |

## [Examples](zabbix_group_events_info_module.md#id4)

```yaml+jinja
# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: Fail if alert active in hostgroup
  # set task level variables as we change ansible_connection plugin here
  vars:
      ansible_network_os: community.zabbix.zabbix
      ansible_connection: httpapi
      ansible_httpapi_port: 443
      ansible_httpapi_use_ssl: true
      ansible_httpapi_validate_certs: false
      ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
      ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_group_events_info:
      hostgroup_name: "{{ inventory_hostname }}"
  register: zbx_hostgroup
  delegate_to: localhost
- fail:
    msg: "Active alert in zabbix"
  when: zbx_hostgroup["triggers_problem"] | length > 0
```

## [Return Values](zabbix_group_events_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **triggers_ok**  complex | Zabbix Triggers in OK state  **Returned:** On success |
| **comments**  string | Additional description of the trigger  **Returned:** success |
| **description**  string | Name of the trigger  **Returned:** success |
| **error**  string | Error text if there have been any problems when updating the state of the trigger  **Returned:** success |
| **expression**  string | Reduced trigger expression  **Returned:** success |
| **flags**  integer | Origin of the trigger  **Returned:** success |
| **lastchange**  integer | Time when the trigger last changed its state (timestamp)  **Returned:** success |
| **priority**  integer | Severity of the trigger  **Returned:** success |
| **state**  integer | State of the trigger  **Returned:** success |
| **status**  integer | Whether the trigger is enabled or disabled  **Returned:** success |
| **templateid**  integer | ID of the parent template trigger  **Returned:** success |
| **triggerid**  integer | ID of the trigger  **Returned:** success |
| **type**  integer | Whether the trigger can generate multiple problem events  **Returned:** success |
| **url**  string | URL associated with the trigger  **Returned:** success |
| **value**  integer | Whether the trigger is in OK or problem state  **Returned:** success |
| **triggers_problem**  complex | Zabbix Triggers in problem state. See trigger and event objects in API documentation of your zabbix version for more  **Returned:** On success |
| **comments**  string | Additional description of the trigger  **Returned:** success |
| **description**  string | Name of the trigger  **Returned:** success |
| **error**  string | Error text if there have been any problems when updating the state of the trigger  **Returned:** success |
| **expression**  string | Reduced trigger expression  **Returned:** success |
| **flags**  integer | Origin of the trigger  **Returned:** success |
| **last_event**  complex | last event informations  **Returned:** success |
| **acknowledged**  integer | If set to true return only acknowledged events  **Returned:** success |
| **acknowledges**  complex | acknowledges informations  **Returned:** success |
| **alias**  string | Account who acknowledge  **Returned:** success |
| **clock**  integer | Time when the event was created (timestamp)  **Returned:** success |
| **message**  string | Text of the acknowledgement message  **Returned:** success |
| **clock**  integer | Time when the event was created (timestamp)  **Returned:** success |
| **eventid**  integer | ID of the event  **Returned:** success |
| **value**  integer | State of the related object  **Returned:** success |
| **lastchange**  integer | Time when the trigger last changed its state (timestamp)  **Returned:** success |
| **priority**  integer | Severity of the trigger  **Returned:** success |
| **state**  integer | State of the trigger  **Returned:** success |
| **status**  integer | Whether the trigger is enabled or disabled  **Returned:** success |
| **templateid**  integer | ID of the parent template trigger  **Returned:** success |
| **triggerid**  integer | ID of the trigger  **Returned:** success |
| **type**  integer | Whether the trigger can generate multiple problem events  **Returned:** success |
| **url**  string | URL associated with the trigger  **Returned:** success |
| **value**  integer | Whether the trigger is in OK or problem state  **Returned:** success |

### Authors

- Martin Eiswirth (@meis4h)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
