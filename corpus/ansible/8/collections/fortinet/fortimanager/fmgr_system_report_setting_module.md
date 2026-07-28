---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_report_setting module – Report settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_report_setting_module.html
fetched_at: 2026-07-28T02:20:06+00:00
---
# fortinet.fortimanager.fmgr_system_report_setting module – Report settings.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_report_setting`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_report_setting_module.md#synopsis)
- [Parameters](fmgr_system_report_setting_module.md#parameters)
- [Notes](fmgr_system_report_setting_module.md#notes)
- [Examples](fmgr_system_report_setting_module.md#examples)
- [Return Values](fmgr_system_report_setting_module.md#return-values)

## [Synopsis](fmgr_system_report_setting_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_report_setting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **system_report_setting**  dictionary | the top level parameters set |
| **aggregate-report**  string | Enable/disable including a group report along with the per-device reports.  disable - Exclude a group report along with the per-device reports.  enable - Include a group report along with the per-device reports.  **Choices:**   - `"disable"` - `"enable"` |
| **capwap-port**  integer | Exclude capwap traffic by port. |
| **capwap-service**  string | Exclude capwap traffic by service. |
| **exclude-capwap**  string | Exclude capwap traffic.  disable - Disable.  by-port - By port.  by-service - By service.  **Choices:**   - `"disable"` - `"by-port"` - `"by-service"` |
| **hcache-lossless**  string | Usableness of ready-with-loss hcaches.  disable - Use ready-with-loss hcaches.  enable - Do not use ready-with-loss hcaches.  **Choices:**   - `"disable"` - `"enable"` |
| **ldap-cache-timeout**  integer | LDAP cache timeout in minutes, default 60, 0 means not use cache. |
| **max-rpt-pdf-rows**  integer | Maximum number of rows can be generated in a single pdf. |
| **max-table-rows**  integer | Maximum number of rows can be generated in a single table. |
| **report-priority**  string | Priority of sql report.  high - High  low - Low  auto - Auto  **Choices:**   - `"high"` - `"low"` - `"auto"` |
| **template-auto-install**  string | The language used for new ADOMs  default - Default.  english - English.  **Choices:**   - `"default"` - `"english"` |
| **week-start**  string | Day of the week on which the week starts.  sun - Sunday.  mon - Monday.  **Choices:**   - `"sun"` - `"mon"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_report_setting_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_report_setting_module.md#id4)

```yaml+jinja
- hosts: fortimanager-inventory
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
    - name: Report settings.
      fmgr_system_report_setting:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_report_setting:
          aggregate-report: <value in [disable, enable]>
          hcache-lossless: <value in [disable, enable]>
          ldap-cache-timeout: <integer>
          max-table-rows: <integer>
          report-priority: <value in [high, low, auto]>
          template-auto-install: <value in [default, english]>
          week-start: <value in [sun, mon]>
          capwap-port: <integer>
          capwap-service: <string>
          exclude-capwap: <value in [disable, by-port, by-service]>
          max-rpt-pdf-rows: <integer>
```

## [Return Values](fmgr_system_report_setting_module.md#id5)

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
