---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_housekeeping module – Update Zabbix housekeeping"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_housekeeping_module.html
fetched_at: 2026-07-28T02:02:47+00:00
---
# community.zabbix.zabbix_housekeeping module – Update Zabbix housekeeping

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
> see [Requirements](zabbix_housekeeping_module.md#ansible-collections-community-zabbix-zabbix-housekeeping-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_housekeeping`.

New in community.zabbix 1.6.0

- [Synopsis](zabbix_housekeeping_module.md#synopsis)
- [Requirements](zabbix_housekeeping_module.md#requirements)
- [Parameters](zabbix_housekeeping_module.md#parameters)
- [Examples](zabbix_housekeeping_module.md#examples)
- [Return Values](zabbix_housekeeping_module.md#return-values)

## [Synopsis](zabbix_housekeeping_module.md#id1)

- This module allows you to modify Zabbix housekeeping setting.

## [Requirements](zabbix_housekeeping_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_housekeeping_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **compress_older**  string | Compress history and trends records older than this period if *compression_status=true*. |
| **compression_status**  boolean | TimescaleDB compression for history and trends will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **hk_audit**  string | Storage period of audit data (e.g. 365d). |
| **hk_audit_mode**  boolean | Internal housekeeping for audit will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **hk_events_autoreg**  string | Storage period of autoregistration data (e.g. 365d). |
| **hk_events_discovery**  string | Storage period of network discovery (e.g. 365d). |
| **hk_events_internal**  string | Storage period of internal data (e.g. 365d). |
| **hk_events_mode**  boolean | Internal housekeeping for events and alerts will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **hk_events_service**  string | Storage period of service data (e.g. 365d). |
| **hk_events_trigger**  string | Storage period of trigger data (e.g. 365d). |
| **hk_history**  string | Storage priod of history data (e.g. 365d). |
| **hk_history_global**  boolean | Overriding history period of each items will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **hk_history_mode**  boolean | Internal housekeeping for history will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **hk_services**  string | Storage period of services data (e.g. 365d). |
| **hk_services_mode**  boolean | Internal housekeeping for services will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **hk_sessions**  string | Storage period of sessions data (e.g. 365d). |
| **hk_sessions_mode**  boolean | Internal housekeeping for sessions will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **hk_trends**  string | Storage priod of trends data (e.g. 365d). |
| **hk_trends_global**  boolean | Overriding trend period of each items will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **hk_trends_mode**  boolean | Internal housekeeping for trends will be enabled if `true`.  **Choices:**   - `false` - `true` |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |

## [Examples](zabbix_housekeeping_module.md#id4)

```yaml+jinja
# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  ansible.builtin.set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  ansible.builtin.set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: Update housekeeping all parameter
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
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

## [Return Values](zabbix_housekeeping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The result of the operation  **Returned:** success  **Sample:** `"Successfully update housekeeping setting"` |

### Authors

- ONODERA Masaru(@masa-orca)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
