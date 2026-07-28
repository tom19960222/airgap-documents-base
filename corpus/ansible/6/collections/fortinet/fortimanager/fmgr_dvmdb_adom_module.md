---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_dvmdb_adom module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_dvmdb_adom_module.html
fetched_at: 2026-07-27T17:29:27+00:00
---
# fortinet.fortimanager.fmgr_dvmdb_adom module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_dvmdb_adom`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_dvmdb_adom_module.md#synopsis)
- [Parameters](fmgr_dvmdb_adom_module.md#parameters)
- [Notes](fmgr_dvmdb_adom_module.md#notes)
- [Examples](fmgr_dvmdb_adom_module.md#examples)
- [Return Values](fmgr_dvmdb_adom_module.md#return-values)

## [Synopsis](fmgr_dvmdb_adom_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_dvmdb_adom_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **dvmdb_adom**  dictionary | the top level parameters set |
| **create_time**  integer | no description |
| **desc**  string | no description |
| **flags**  list / elements=string | no description  Choices:   - `"migration"` - `"db_export"` - `"no_vpn_console"` - `"backup"` - `"other_devices"` - `"central_sdwan"` - `"is_autosync"` - `"per_device_wtp"` - `"policy_check_on_install"` - `"install_on_policy_check_fail"` - `"auto_push_cfg"` - `"per_device_fsw"` |
| **log_db_retention_hours**  integer | no description  Default: `1440` |
| **log_disk_quota**  integer | no description |
| **log_disk_quota_alert_thres**  integer | no description  Default: `90` |
| **log_disk_quota_split_ratio**  integer | no description  Default: `70` |
| **log_file_retention_hours**  integer | no description  Default: `8760` |
| **meta fields**  dictionary | no description |
| **mig_mr**  integer | no description  Default: `2` |
| **mig_os_ver**  string | no description  Choices:   - `"unknown"` - `"0.0"` - `"1.0"` - `"2.0"` - `"3.0"` - `"4.0"` - `"5.0"` - `"6.0"` - `"7.0"` - `"8.0"`   Default: `"6."` |
| **mode**  string | no description  no description  Choices:   - `"ems"` - `"gms"` ← (default) - `"provider"` |
| **mr**  integer | no description  Default: `2` |
| **name**  string | no description |
| **os_ver**  string | no description  Choices:   - `"unknown"` - `"0.0"` - `"1.0"` - `"2.0"` - `"3.0"` - `"4.0"` - `"5.0"` - `"6.0"` - `"7.0"` - `"8.0"`   Default: `"6."` |
| **restricted_prds**  list / elements=string | no description  Choices:   - `"fos"` - `"foc"` - `"fml"` - `"fch"` - `"fwb"` - `"log"` - `"fct"` - `"faz"` - `"fsa"` - `"fsw"` - `"fmg"` - `"fdd"` - `"fac"` - `"fpx"` - `"fna"` - `"fdc"` - `"ffw"` - `"fsr"` - `"fad"` - `"fap"` - `"fxt"` - `"fts"` - `"fai"` - `"fwc"` |
| **state**  integer | no description  Default: `1` |
| **uuid**  string | no description |
| **workspace_mode**  integer | no description |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_dvmdb_adom_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_dvmdb_adom_module.md#id4)

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
     fmgr_dvmdb_adom:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        state: <value in [present, absent]>
        dvmdb_adom:
           desc: <value of string>
           flags:
             - migration
             - db_export
             - no_vpn_console
             - backup
             - other_devices
             - central_sdwan
             - is_autosync
             - per_device_wtp
             - policy_check_on_install
             - install_on_policy_check_fail
             - auto_push_cfg
             - per_device_fsw
           log_db_retention_hours: <value of integer>
           log_disk_quota: <value of integer>
           log_disk_quota_alert_thres: <value of integer>
           log_disk_quota_split_ratio: <value of integer>
           log_file_retention_hours: <value of integer>
           meta fields: <value of dict>
           mig_mr: <value of integer>
           mig_os_ver: <value in [unknown, 0.0, 1.0, ...]>
           mode: <value in [ems, gms, provider]>
           mr: <value of integer>
           name: <value of string>
           os_ver: <value in [unknown, 0.0, 1.0, ...]>
           restricted_prds:
             - fos
             - foc
             - fml
             - fch
             - fwb
             - log
             - fct
             - faz
             - fsa
             - fsw
             - fmg
             - fdd
             - fac
             - fpx
             - fna
             - fdc
             - ffw
             - fsr
             - fad
             - fap
             - fxt
             - fts
             - fai
             - fwc
           state: <value of integer>
           uuid: <value of string>
           create_time: <value of integer>
           workspace_mode: <value of integer>
```

## [Return Values](fmgr_dvmdb_adom_module.md#id5)

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
