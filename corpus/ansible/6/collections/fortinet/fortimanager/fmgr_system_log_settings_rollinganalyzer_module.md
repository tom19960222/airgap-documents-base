---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_log_settings_rollinganalyzer module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_log_settings_rollinganalyzer_module.html
fetched_at: 2026-07-27T17:36:35+00:00
---
# fortinet.fortimanager.fmgr_system_log_settings_rollinganalyzer module – no description

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/fortinet/fortimanager) (version 2.1.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_log_settings_rollinganalyzer`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_log_settings_rollinganalyzer_module.md#synopsis)
- [Parameters](fmgr_system_log_settings_rollinganalyzer_module.md#parameters)
- [Notes](fmgr_system_log_settings_rollinganalyzer_module.md#notes)
- [Examples](fmgr_system_log_settings_rollinganalyzer_module.md#examples)
- [Return Values](fmgr_system_log_settings_rollinganalyzer_module.md#return-values)

## [Synopsis](fmgr_system_log_settings_rollinganalyzer_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_log_settings_rollinganalyzer_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_log_settings_rollinganalyzer**  dictionary | the top level parameters set |
| **days**  list / elements=string | no description  Choices:   - `"sun"` - `"mon"` - `"tue"` - `"wed"` - `"thu"` - `"fri"` - `"sat"` |
| **del-files**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **directory**  string | no description |
| **file-size**  integer | no description  Default: `200` |
| **gzip-format**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **hour**  integer | no description  Default: `0` |
| **ip**  string | no description  Default: `"0."` |
| **ip2**  string | no description  Default: `"0."` |
| **ip3**  string | no description  Default: `"0."` |
| **log-format**  string | no description  no description  no description  no description  Choices:   - `"native"` ← (default) - `"text"` - `"csv"` |
| **min**  integer | no description  Default: `0` |
| **password**  string | no description |
| **password2**  string | no description |
| **password3**  string | no description |
| **port**  integer | no description  Default: `0` |
| **port2**  integer | no description  Default: `0` |
| **port3**  integer | no description  Default: `0` |
| **rolling-upgrade-status**  integer | no description  Default: `0` |
| **server**  string | no description |
| **server-type**  string | no description  no description  no description  no description  Choices:   - `"ftp"` ← (default) - `"sftp"` - `"scp"` |
| **server2**  string | no description |
| **server3**  string | no description |
| **upload**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **upload-hour**  integer | no description  Default: `0` |
| **upload-mode**  string | no description  no description  no description  Choices:   - `"backup"` ← (default) - `"mirror"` |
| **upload-trigger**  string | no description  no description  no description  Choices:   - `"on-roll"` ← (default) - `"on-schedule"` |
| **username**  string | no description |
| **username2**  string | no description |
| **username3**  string | no description |
| **when**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"daily"` - `"weekly"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_system_log_settings_rollinganalyzer_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_log_settings_rollinganalyzer_module.md#id4)

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
   - name: no description
     fmgr_system_log_settings_rollinganalyzer:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_log_settings_rollinganalyzer:
           days:
             - sun
             - mon
             - tue
             - wed
             - thu
             - fri
             - sat
           del-files: <value in [disable, enable]>
           directory: <value of string>
           file-size: <value of integer>
           gzip-format: <value in [disable, enable]>
           hour: <value of integer>
           ip: <value of string>
           ip2: <value of string>
           ip3: <value of string>
           log-format: <value in [native, text, csv]>
           min: <value of integer>
           password: <value of string>
           password2: <value of string>
           password3: <value of string>
           server-type: <value in [ftp, sftp, scp]>
           upload: <value in [disable, enable]>
           upload-hour: <value of integer>
           upload-mode: <value in [backup, mirror]>
           upload-trigger: <value in [on-roll, on-schedule]>
           username: <value of string>
           username2: <value of string>
           username3: <value of string>
           when: <value in [none, daily, weekly]>
           port: <value of integer>
           port2: <value of integer>
           port3: <value of integer>
           rolling-upgrade-status: <value of integer>
           server: <value of string>
           server2: <value of string>
           server3: <value of string>
```

## [Return Values](fmgr_system_log_settings_rollinganalyzer_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **request_url**  string | The full url requested  Returned: always  Sample: `"/sys/login/user"` |
| **response_code**  integer | The status of api request  Returned: always  Sample: `0` |
| **response_message**  string | The descriptive message of the api response  Returned: always  Sample: `"OK."` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
[Homepage](https://fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/tree/galaxy/2.1.7)
