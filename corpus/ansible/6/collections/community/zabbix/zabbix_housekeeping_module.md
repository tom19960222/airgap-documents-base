---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_housekeeping module – Update Zabbix housekeeping"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_housekeeping_module.html
fetched_at: 2026-07-27T17:24:14+00:00
---
# community.zabbix.zabbix_housekeeping module – Update Zabbix housekeeping

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
> see [Requirements](zabbix_housekeeping_module.md#ansible-collections-community-zabbix-zabbix-housekeeping-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_housekeeping`.

New in community.zabbix 1.6.0

- [Synopsis](zabbix_housekeeping_module.md#synopsis)
- [Requirements](zabbix_housekeeping_module.md#requirements)
- [Parameters](zabbix_housekeeping_module.md#parameters)
- [Notes](zabbix_housekeeping_module.md#notes)
- [Examples](zabbix_housekeeping_module.md#examples)
- [Return Values](zabbix_housekeeping_module.md#return-values)

## [Synopsis](zabbix_housekeeping_module.md#id1)

- This module allows you to modify Zabbix housekeeping setting.

## [Requirements](zabbix_housekeeping_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](zabbix_housekeeping_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **compress_older**  string | Compress history and trends records older than this period if *compression_status=true*. |
| **compression_status**  boolean | TimescaleDB compression for history and trends will be enabled if `true`.  Choices:   - `false` - `true` |
| **hk_audit**  string | Storage period of audit data (e.g. 365d). |
| **hk_audit_mode**  boolean | Internal housekeeping for audit will be enabled if `true`.  Choices:   - `false` - `true` |
| **hk_events_autoreg**  string | Storage period of autoregistration data (e.g. 365d). |
| **hk_events_discovery**  string | Storage period of network discovery (e.g. 365d). |
| **hk_events_internal**  string | Storage period of internal data (e.g. 365d). |
| **hk_events_mode**  boolean | Internal housekeeping for events and alerts will be enabled if `true`.  Choices:   - `false` - `true` |
| **hk_events_service**  string | Storage period of service data (e.g. 365d).  This parameter is available since Zabbix 6.0. |
| **hk_events_trigger**  string | Storage period of trigger data (e.g. 365d). |
| **hk_history**  string | Storage priod of history data (e.g. 365d). |
| **hk_history_global**  boolean | Overriding history period of each items will be enabled if `true`.  Choices:   - `false` - `true` |
| **hk_history_mode**  boolean | Internal housekeeping for history will be enabled if `true`.  Choices:   - `false` - `true` |
| **hk_services**  string | Storage period of services data (e.g. 365d). |
| **hk_services_mode**  boolean | Internal housekeeping for services will be enabled if `true`.  Choices:   - `false` - `true` |
| **hk_sessions**  string | Storage period of sessions data (e.g. 365d). |
| **hk_sessions_mode**  boolean | Internal housekeeping for sessions will be enabled if `true`.  Choices:   - `false` - `true` |
| **hk_trends**  string | Storage priod of trends data (e.g. 365d). |
| **hk_trends_global**  boolean | Overriding trend period of each items will be enabled if `true`.  Choices:   - `false` - `true` |
| **hk_trends_mode**  boolean | Internal housekeeping for trends will be enabled if `true`.  Choices:   - `false` - `true` |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |

## [Notes](zabbix_housekeeping_module.md#id4)

> **Note:**
>
> - Zabbix 5.2 version and higher are supported.
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_housekeeping_module.md#id5)

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

- name: Update housekeeping all parameter
  community.zabbix.zabbix_housekeeping:
    login_user: Admin
    login_password: secret
    hk_events_mode: yes
    hk_events_trigger: 365d
    hk_events_service: 365d
    hk_events_internal: 365d
    hk_events_discovery: 365d
    hk_events_autoreg: 365d
    hk_services_mode: yes
    hk_services: 365d
    hk_audit_mode: yes
    hk_audit: 365d
    hk_sessions_mode: yes
    hk_sessions: 365d
    hk_history_mode: yes
    hk_history_global: yes
    hk_history: 365d
    hk_trends_mode: yes
    hk_trends_global: yes
    hk_trends: 365d
    compression_status: off
    compress_older: 7d
```

## [Return Values](zabbix_housekeeping_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The result of the operation  Returned: success  Sample: `"Successfully update housekeeping setting"` |

### Authors

- ONODERA Masaru(@masa-orca)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
