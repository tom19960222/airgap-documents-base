---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_dvmdb_adom module – ADOM table, most attributes are read-only and can only be changed internally."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_dvmdb_adom_module.html
fetched_at: 2026-07-28T02:09:37+00:00
---
# fortinet.fortimanager.fmgr_dvmdb_adom module – ADOM table, most attributes are read-only and can only be changed internally.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_dvmdb_adom`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **dvmdb_adom**  dictionary | the top level parameters set |
| **create_time**  integer | Create_Time. |
| **desc**  string | Desc. |
| **flags**  list / elements=string | Flags.  **Choices:**   - `"migration"` - `"db_export"` - `"no_vpn_console"` - `"backup"` - `"other_devices"` - `"central_sdwan"` - `"is_autosync"` - `"per_device_wtp"` - `"policy_check_on_install"` - `"install_on_policy_check_fail"` - `"auto_push_cfg"` - `"per_device_fsw"` - `"install_deselect_all"` |
| **lock_override**  integer | no description |
| **log_db_retention_hours**  integer | Log_Db_Retention_Hours. |
| **log_disk_quota**  integer | Log_Disk_Quota. |
| **log_disk_quota_alert_thres**  integer | Log_Disk_Quota_Alert_Thres. |
| **log_disk_quota_split_ratio**  integer | Log_Disk_Quota_Split_Ratio. |
| **log_file_retention_hours**  integer | Log_File_Retention_Hours. |
| **meta fields**  dictionary | Default metafields |
| **mig_mr**  integer | Mig_Mr. |
| **mig_os_ver**  string | Mig_Os_Ver.  **Choices:**   - `"unknown"` - `"0.0"` - `"1.0"` - `"2.0"` - `"3.0"` - `"4.0"` - `"5.0"` - `"6.0"` - `"7.0"` - `"8.0"` - `"9.0"` |
| **mode**  string | ems -  provider - Global database.  **Choices:**   - `"ems"` - `"gms"` - `"provider"` |
| **mr**  integer | Mr. |
| **name**  string / required | Name. |
| **os_ver**  string | Os_Ver.  **Choices:**   - `"unknown"` - `"0.0"` - `"1.0"` - `"2.0"` - `"3.0"` - `"4.0"` - `"5.0"` - `"6.0"` - `"7.0"` - `"8.0"` - `"9.0"` |
| **restricted_prds**  any | (list or str) Restricted_Prds.  **Choices:**   - `"fos"` - `"foc"` - `"fml"` - `"fch"` - `"fwb"` - `"log"` - `"fct"` - `"faz"` - `"fsa"` - `"fsw"` - `"fmg"` - `"fdd"` - `"fac"` - `"fpx"` - `"fna"` - `"fdc"` - `"ffw"` - `"fsr"` - `"fad"` - `"fap"` - `"fxt"` - `"fts"` - `"fai"` - `"fwc"` |
| **state**  integer | State. |
| **tz**  integer | no description |
| **uuid**  string | Uuid. |
| **workspace_mode**  integer | Workspace_Mode. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
    - name: ADOM table, most attributes are read-only and can only be changed internally.
      fmgr_dvmdb_adom:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        state: <value in [present, absent]>
        dvmdb_adom:
          desc: <string>
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
            - install_deselect_all
          log_db_retention_hours: <integer>
          log_disk_quota: <integer>
          log_disk_quota_alert_thres: <integer>
          log_disk_quota_split_ratio: <integer>
          log_file_retention_hours: <integer>
          meta fields: <dict>
          mig_mr: <integer>
          mig_os_ver: <value in [unknown, 0.0, 1.0, ...]>
          mode: <value in [ems, gms, provider]>
          mr: <integer>
          name: <string>
          os_ver: <value in [unknown, 0.0, 1.0, ...]>
          restricted_prds: # <list or string>
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
          state: <integer>
          uuid: <string>
          create_time: <integer>
          workspace_mode: <integer>
          tz: <integer>
          lock_override: <integer>
```

## [Return Values](fmgr_dvmdb_adom_module.md#id5)

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
