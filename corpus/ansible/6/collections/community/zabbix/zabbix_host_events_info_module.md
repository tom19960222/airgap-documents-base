---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_host_events_info module – Get all triggers about a Zabbix host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_host_events_info_module.html
fetched_at: 2026-07-27T17:24:12+00:00
---
# community.zabbix.zabbix_host_events_info module – Get all triggers about a Zabbix host

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/community/zabbix) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_host_events_info_module.md#ansible-collections-community-zabbix-zabbix-host-events-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_host_events_info`.

- [Synopsis](zabbix_host_events_info_module.md#synopsis)
- [Requirements](zabbix_host_events_info_module.md#requirements)
- [Parameters](zabbix_host_events_info_module.md#parameters)
- [Notes](zabbix_host_events_info_module.md#notes)
- [Examples](zabbix_host_events_info_module.md#examples)
- [Return Values](zabbix_host_events_info_module.md#return-values)

## [Synopsis](zabbix_host_events_info_module.md#id1)

- This module allows you to see if a Zabbix host have no active alert to make actions on it. For this case use module Ansible ‘fail’ to exclude host in trouble.
- Length of “triggers_ok” allow if template’s triggers exist for Zabbix Host

## [Requirements](zabbix_host_events_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](zabbix_host_events_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host_id_type**  string | Type of host_identifier  Choices:   - `"hostname"` ← (default) - `"visible_name"` - `"hostid"` |
| **host_identifier**  string / required | Identifier of Zabbix Host |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **trigger_severity**  string | Zabbix severity for search filter  Choices:   - `"not_classified"` - `"information"` - `"warning"` - `"average"` ← (default) - `"high"` - `"disaster"` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_host_events_info_module.md#id4)

> **Note:**
>
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_host_events_info_module.md#id5)

```yaml+jinja
# Set following variables for Zabbix Server host in play or inventory
- name: Set connection specific variables
  set_fact:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 80
    ansible_httpapi_use_ssl: false
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: 'zabbixeu'  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu

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

- name: exclude machine if alert active on it
  community.zabbix.zabbix_host_events_info:
      host_identifier: "{{inventory_hostname}}"
      host_id_type: "hostname"
      timeout: 120
  register: zbx_host
  delegate_to: localhost
- fail:
    msg: "machine alert in zabbix"
  when: zbx_host['triggers_problem']|length > 0
```

## [Return Values](zabbix_host_events_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **triggers_ok**  complex | Host Zabbix Triggers in OK state  Returned: On success |
| **comments**  string | Additional description of the trigger  Returned: success |
| **description**  string | Name of the trigger  Returned: success |
| **error**  string | Error text if there have been any problems when updating the state of the trigger  Returned: success |
| **expression**  string | Reduced trigger expression  Returned: success |
| **flags**  integer | Origin of the trigger  Returned: success |
| **lastchange**  integer | Time when the trigger last changed its state (timestamp)  Returned: success |
| **priority**  integer | Severity of the trigger  Returned: success |
| **state**  integer | State of the trigger  Returned: success |
| **status**  integer | Whether the trigger is enabled or disabled  Returned: success |
| **templateid**  integer | ID of the parent template trigger  Returned: success |
| **triggerid**  integer | ID of the trigger  Returned: success |
| **type**  integer | Whether the trigger can generate multiple problem events  Returned: success |
| **url**  string | URL associated with the trigger  Returned: success |
| **value**  integer | Whether the trigger is in OK or problem state  Returned: success |
| **triggers_problem**  complex | Host Zabbix Triggers in problem state. See trigger and event objects in API documentation of your zabbix version for more  Returned: On success |
| **comments**  string | Additional description of the trigger  Returned: success |
| **description**  string | Name of the trigger  Returned: success |
| **error**  string | Error text if there have been any problems when updating the state of the trigger  Returned: success |
| **expression**  string | Reduced trigger expression  Returned: success |
| **flags**  integer | Origin of the trigger  Returned: success |
| **last_event**  complex | last event informations  Returned: success |
| **acknowledged**  integer | If set to true return only acknowledged events  Returned: success |
| **acknowledges**  complex | acknowledges informations  Returned: success |
| **alias**  string | Account who acknowledge  Returned: success |
| **clock**  integer | Time when the event was created (timestamp)  Returned: success |
| **message**  string | Text of the acknowledgement message  Returned: success |
| **clock**  integer | Time when the event was created (timestamp)  Returned: success |
| **eventid**  integer | ID of the event  Returned: success |
| **value**  integer | State of the related object  Returned: success |
| **lastchange**  integer | Time when the trigger last changed its state (timestamp)  Returned: success |
| **priority**  integer | Severity of the trigger  Returned: success |
| **state**  integer | State of the trigger  Returned: success |
| **status**  integer | Whether the trigger is enabled or disabled  Returned: success |
| **templateid**  integer | ID of the parent template trigger  Returned: success |
| **triggerid**  integer | ID of the trigger  Returned: success |
| **type**  integer | Whether the trigger can generate multiple problem events  Returned: success |
| **url**  string | URL associated with the trigger  Returned: success |
| **value**  integer | Whether the trigger is in OK or problem state  Returned: success |

### Authors

- Stéphane Travassac (@stravassac)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
