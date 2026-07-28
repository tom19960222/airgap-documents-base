---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_settings module – Update Zabbix global settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_settings_module.html
fetched_at: 2026-07-28T02:02:54+00:00
---
# community.zabbix.zabbix_settings module – Update Zabbix global settings.

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
> see [Requirements](zabbix_settings_module.md#ansible-collections-community-zabbix-zabbix-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_settings`.

New in community.zabbix 2.1.0

- [Synopsis](zabbix_settings_module.md#synopsis)
- [Requirements](zabbix_settings_module.md#requirements)
- [Parameters](zabbix_settings_module.md#parameters)
- [Notes](zabbix_settings_module.md#notes)
- [Examples](zabbix_settings_module.md#examples)
- [Return Values](zabbix_settings_module.md#return-values)

## [Synopsis](zabbix_settings_module.md#id1)

- This module allows you to update Zabbix global settings.

## [Requirements](zabbix_settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alert_usrgrp**  string | A name of user group which user belongs to receive an alerm message when database down. |
| **auditlog_enabled**  boolean | Enable audit logging if `true`.  **Choices:**   - `false` - `true` |
| **blink_period**  string | A time of period for blinking status changed triggers.  Accepts seconds and time unit with suffix (e.g. 5m). |
| **connect_timeout**  string | A time of connection timeout with Zabbix server. |
| **custom_color**  boolean | Custom event color settings will be activated if `true`.  **Choices:**   - `false` - `true` |
| **default_inventory_mode**  string | A default value for host inventory mode.  **Choices:**   - `"disabled"` - `"manual"` - `"automatic"` |
| **default_lang**  string | Default language for users. |
| **default_theme**  string | Default theme for users.  **Choices:**   - `"blue-theme"` - `"dark-theme"` - `"hc-light"` - `"hc-dark"` |
| **default_timezone**  string | Default time zone for users.  Please set `system` if you want to use system time zone. |
| **discovery_group**  string | A hostgroup which discovered hosts will belong to. |
| **frontend_url**  string | A URL of frontend.  This parameter is used for url parameter of settings API. |
| **geomaps_attribution**  string | A text of Geomap attribution. |
| **geomaps_max_zoom**  string | Max zoom level of geomap. |
| **geomaps_tile_provider**  string | A provider of Geomap tile.  Please set `another` if you want use non default provider  **Choices:**   - `"OpenStreetMap.Mapnik"` - `"OpenTopoMap"` - `"Stamen.TonerLite"` - `"Stamen.Terrain"` - `"USGS.USTopo"` - `"USGS.USImagery"` - `"another"` |
| **geomaps_tile_url**  string | A URL of geomap tile. |
| **history_period**  string | Max period of displaying history data.  Accepts seconds and time unit with suffix (e.g. 24h). |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **iframe_sandboxing_enabled**  boolean | The Zabbix uses iframe sandboxing if `true`.  **Choices:**   - `false` - `true` |
| **iframe_sandboxing_exceptions**  string | A text of iframe sandboxing exceptions. |
| **item_test_timeout**  string | A time of network timeout for item tests. |
| **login_attempts**  integer | A number of login attempts you can try with non blocked. |
| **login_block**  string | A time of interval to reset login attempts when the user is blocked.  Accepts seconds and time unit with suffix (e.g. 5m). |
| **max_in_table**  integer | Max count of elements to show inside table cell |
| **max_overview_table_size**  integer | Max number of columns and rows in overview tables |
| **max_period**  string | Max period for time filter.  Accepts seconds and time unit with suffix (e.g. 1y). |
| **media_type_test_timeout**  string | A time of network timeout for media type test. |
| **ok_ack_color**  string | A custom color for acknowledged RESOLVED events.  This setting will be activated if *custom_color=true*.  Please set hexadecimal color code (e.g. 00FF00). |
| **ok_ack_style**  boolean | Acknowledged RESOLVED events blink if `true`.  **Choices:**   - `false` - `true` |
| **ok_period**  string | A time of period for displaying OK triggers.  Accepts seconds and time unit with suffix (e.g. 5m). |
| **ok_unack_color**  string | A custom color for unacknowledged RESOLVED events.  This setting will be activated if *custom_color=true*.  Please set hexadecimal color code (e.g. 00FF00). |
| **ok_unack_style**  boolean | Unacknowledged RESOLVED events blink if `true`.  **Choices:**   - `false` - `true` |
| **period_default**  string | Default period value for time filter.  Accepts seconds and time unit with suffix (e.g. 1h). |
| **problem_ack_color**  string | A custom color for acknowledged PROBLEM events.  This setting will be activated if *custom_color=true*.  Please set hexadecimal color code (e.g. 00FF00). |
| **problem_ack_style**  boolean | Acknowledged PROBLEM events blink if `true`.  **Choices:**   - `false` - `true` |
| **problem_unack_color**  string | A custom color for unacknowledged PROBLEM events.  This setting will be activated if *custom_color=true*.  Please set hexadecimal color code (e.g. 00FF00). |
| **problem_unack_style**  boolean | Unacknowledged PROBLEM events blink if `true`.  **Choices:**   - `false` - `true` |
| **report_test_timeout**  string | A time of network timeout for scheduled report test. |
| **script_timeout**  string | A time of network timeout for script execution. |
| **search_limit**  integer | A number of search and filter results limit. |
| **server_check_interval**  boolean | The Zabbix shows “Zabbix server is down” warning if `true`.  **Choices:**   - `false` - `true` |
| **severity_color_0**  string | A custom color for not classified severity.  Please set hexadecimal color code (e.g. 00FF00). |
| **severity_color_1**  string | A custom color for information severity.  Please set hexadecimal color code (e.g. 00FF00). |
| **severity_color_2**  string | A custom color for warning severity.  Please set hexadecimal color code (e.g. 00FF00). |
| **severity_color_3**  string | A custom color for average severity.  Please set hexadecimal color code (e.g. 00FF00). |
| **severity_color_4**  string | A custom color for high severity.  Please set hexadecimal color code (e.g. 00FF00). |
| **severity_color_5**  string | A custom color for disaster severity.  Please set hexadecimal color code (e.g. 00FF00). |
| **severity_name_0**  string | A custom name for not classified severity. |
| **severity_name_1**  string | A custom name for information severity. |
| **severity_name_2**  string | A custom name for warning severity. |
| **severity_name_3**  string | A custom name for average severity. |
| **severity_name_4**  string | A custom name for high severity. |
| **severity_name_5**  string | A custom name for disaster severity. |
| **show_technical_errors**  boolean | The Zabbix shows PHP and SQL technical errors to users who are non-Super admin or belong to user groups with debug mode not enabled if `true`.  **Choices:**   - `false` - `true` |
| **snmptrap_logging**  boolean | Logging unmatched SNMP traps will be ebabled if `true`.  **Choices:**   - `false` - `true` |
| **socket_timeout**  string | A time of network default timeout. |
| **uri_valid_schemes**  list / elements=string | A list of valid URI scheme. |
| **validate_uri_schemes**  boolean | Validate URI schemes if `true`.  **Choices:**   - `false` - `true` |
| **vault_provider**  string | A name of vault provider.  This parameter is available since Zabbix 6.2.  **Choices:**   - `"HashiCorp_Vault"` - `"CyberArk_Vault"` |
| **work_period**  string | Working time setting.  <https://www.zabbix.com/documentation/current/en/manual/appendix/time_period> |
| **x_frame_options**  string | A text of X-Frame-Options of HTTP header. |

## [Notes](zabbix_settings_module.md#id4)

> **Note:**
>
> - This module manages settings related with settings api except ha_failover_delay.

## [Examples](zabbix_settings_module.md#id5)

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

- name: Update settings
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_settings:
    alert_usrgrp: "0"
    auditlog_enabled: false
    blink_period: "10m"
    connect_timeout: "30s"
    custom_color: false
    default_inventory_mode: automatic
```

## [Return Values](zabbix_settings_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The result of the operation  **Returned:** success  **Sample:** `"Successfully update global settings"` |

### Authors

- ONODERA Masaru(@masa-orca)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
