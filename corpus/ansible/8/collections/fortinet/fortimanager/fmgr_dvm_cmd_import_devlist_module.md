---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_dvm_cmd_import_devlist module – Import a list of ADOMs and devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_dvm_cmd_import_devlist_module.html
fetched_at: 2026-07-28T02:09:34+00:00
---
# fortinet.fortimanager.fmgr_dvm_cmd_import_devlist module – Import a list of ADOMs and devices.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_dvm_cmd_import_devlist`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_dvm_cmd_import_devlist_module.md#synopsis)
- [Parameters](fmgr_dvm_cmd_import_devlist_module.md#parameters)
- [Notes](fmgr_dvm_cmd_import_devlist_module.md#notes)
- [Examples](fmgr_dvm_cmd_import_devlist_module.md#examples)
- [Return Values](fmgr_dvm_cmd_import_devlist_module.md#return-values)

## [Synopsis](fmgr_dvm_cmd_import_devlist_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_dvm_cmd_import_devlist_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **dvm_cmd_import_devlist**  dictionary | the top level parameters set |
| **adom**  string | Name or ID of the ADOM where the command is to be executed on. |
| **flags**  list / elements=string | no description  **Choices:**   - `"none"` - `"create_task"` - `"nonblocking"` - `"log_dev"` |
| **import-adom-members**  list / elements=dictionary | no description |
| **adom**  string | Target ADOM to associate device VDOM with. |
| **dev**  string | no description |
| **vdom**  string | no description |
| **import-adoms**  list / elements=dictionary | no description |
| **create_time**  integer | no description |
| **desc**  string | no description |
| **flags**  list / elements=string | no description  **Choices:**   - `"migration"` - `"db_export"` - `"no_vpn_console"` - `"backup"` - `"other_devices"` - `"central_sdwan"` - `"is_autosync"` - `"per_device_wtp"` - `"policy_check_on_install"` - `"install_on_policy_check_fail"` - `"auto_push_cfg"` - `"per_device_fsw"` - `"install_deselect_all"` |
| **lock_override**  integer | no description |
| **log_db_retention_hours**  integer | no description |
| **log_disk_quota**  integer | no description |
| **log_disk_quota_alert_thres**  integer | no description |
| **log_disk_quota_split_ratio**  integer | no description |
| **log_file_retention_hours**  integer | no description |
| **meta fields**  dictionary | no description |
| **mig_mr**  integer | no description |
| **mig_os_ver**  string | no description  **Choices:**   - `"unknown"` - `"0.0"` - `"1.0"` - `"2.0"` - `"3.0"` - `"4.0"` - `"5.0"` - `"6.0"` - `"7.0"` - `"8.0"` - `"9.0"` |
| **mode**  string | ems -  provider - Global database.  **Choices:**   - `"ems"` - `"gms"` - `"provider"` |
| **mr**  integer | no description |
| **name**  string | no description |
| **os_ver**  string | no description  **Choices:**   - `"unknown"` - `"0.0"` - `"1.0"` - `"2.0"` - `"3.0"` - `"4.0"` - `"5.0"` - `"6.0"` - `"7.0"` - `"8.0"` - `"9.0"` |
| **restricted_prds**  any | (list or str) no description  **Choices:**   - `"fos"` - `"foc"` - `"fml"` - `"fch"` - `"fwb"` - `"log"` - `"fct"` - `"faz"` - `"fsa"` - `"fsw"` - `"fmg"` - `"fdd"` - `"fac"` - `"fpx"` - `"fna"` - `"fdc"` - `"ffw"` - `"fsr"` - `"fad"` - `"fap"` - `"fxt"` - `"fts"` - `"fai"` - `"fwc"` |
| **state**  integer | no description |
| **tz**  integer | no description |
| **uuid**  string | no description |
| **workspace_mode**  integer | no description |
| **import-devices**  list / elements=dictionary | no description |
| **adm_pass**  any | (list) no description |
| **adm_usr**  string | no description |
| **app_ver**  string | no description |
| **av_ver**  string | no description |
| **beta**  integer | no description |
| **branch_pt**  integer | no description |
| **build**  integer | no description |
| **checksum**  string | no description |
| **conf_status**  string | no description  **Choices:**   - `"unknown"` - `"insync"` - `"outofsync"` |
| **conn_mode**  string | no description  **Choices:**   - `"active"` - `"passive"` |
| **conn_status**  string | no description  **Choices:**   - `"UNKNOWN"` - `"up"` - `"down"` |
| **db_status**  string | no description  **Choices:**   - `"unknown"` - `"nomod"` - `"mod"` |
| **desc**  string | no description |
| **dev_status**  string | no description  **Choices:**   - `"none"` - `"unknown"` - `"checkedin"` - `"inprogress"` - `"installed"` - `"aborted"` - `"sched"` - `"retry"` - `"canceled"` - `"pending"` - `"retrieved"` - `"changed_conf"` - `"sync_fail"` - `"timeout"` - `"rev_revert"` - `"auto_updated"` |
| **eip**  string | no description |
| **fap_cnt**  integer | no description |
| **faz.full_act**  integer | no description |
| **faz.perm**  integer | no description |
| **faz.quota**  integer | no description |
| **faz.used**  integer | no description |
| **fex_cnt**  integer | no description |
| **first_tunnel_up**  integer | no description |
| **flags**  list / elements=string | no description  **Choices:**   - `"has_hdd"` - `"vdom_enabled"` - `"discover"` - `"reload"` - `"interim_build"` - `"offline_mode"` - `"is_model"` - `"fips_mode"` - `"linked_to_model"` - `"ip-conflict"` - `"faz-autosync"` - `"need_reset"` - `"backup_mode"` - `"azure_vwan_nva"` - `"fgsp_configured"` - `"cnf_mode"` - `"sase_managed"` |
| **foslic_cpu**  integer | VM Meter vCPU count. |
| **foslic_dr_site**  string | VM Meter DR Site status.  **Choices:**   - `"disable"` - `"enable"` |
| **foslic_inst_time**  integer | VM Meter first deployment time |
| **foslic_last_sync**  integer | VM Meter last synchronized time |
| **foslic_ram**  integer | VM Meter device RAM size |
| **foslic_type**  string | VM Meter license type.  **Choices:**   - `"temporary"` - `"trial"` - `"regular"` - `"trial_expired"` |
| **foslic_utm**  list / elements=string | no description  **Choices:**   - `"fw"` - `"av"` - `"ips"` - `"app"` - `"url"` - `"utm"` - `"fwb"` |
| **fsw_cnt**  integer | no description |
| **ha_group_id**  integer | no description |
| **ha_group_name**  string | no description |
| **ha_mode**  string | enabled - Value reserved for non-FOS HA devices.  **Choices:**   - `"standalone"` - `"AP"` - `"AA"` - `"ELBC"` - `"DUAL"` - `"enabled"` - `"unknown"` - `"fmg-enabled"` - `"autoscale"` |
| **ha_slave**  list / elements=dictionary | no description |
| **conf_status**  integer | no description |
| **idx**  integer | no description |
| **name**  string | no description |
| **prio**  integer | no description |
| **role**  string | no description  **Choices:**   - `"slave"` - `"master"` |
| **sn**  string | no description |
| **status**  integer | no description |
| **hdisk_size**  integer | no description |
| **hostname**  string | no description |
| **hw_generation**  integer | no description |
| **hw_rev_major**  integer | no description |
| **hw_rev_minor**  integer | no description |
| **hyperscale**  integer | no description |
| **ip**  string | no description |
| **ips_ext**  integer | no description |
| **ips_ver**  string | no description |
| **last_checked**  integer | no description |
| **last_resync**  integer | no description |
| **latitude**  string | no description |
| **lic_flags**  integer | no description |
| **lic_region**  string | no description |
| **location_from**  string | no description |
| **logdisk_size**  integer | no description |
| **longitude**  string | no description |
| **maxvdom**  integer | no description |
| **meta fields**  dictionary | no description |
| **mgmt_id**  integer | no description |
| **mgmt_if**  string | no description |
| **mgmt_mode**  string | no description  **Choices:**   - `"unreg"` - `"fmg"` - `"faz"` - `"fmgfaz"` |
| **mgmt_uuid**  string | no description |
| **mgt_vdom**  string | no description |
| **module_sn**  string | no description |
| **mr**  integer | no description |
| **name**  string | Unique name for the device. |
| **nsxt_service_name**  string | no description |
| **os_type**  string | no description  **Choices:**   - `"unknown"` - `"fos"` - `"fsw"` - `"foc"` - `"fml"` - `"faz"` - `"fwb"` - `"fch"` - `"fct"` - `"log"` - `"fmg"` - `"fsa"` - `"fdd"` - `"fac"` - `"fpx"` - `"fna"` - `"fdc"` - `"ffw"` - `"fsr"` - `"fad"` - `"fap"` - `"fxt"` - `"fts"` - `"fai"` - `"fwc"` - `"fis"` - `"fed"` - `"fpa"` - `"fca"` - `"ftc"` |
| **os_ver**  string | no description  **Choices:**   - `"unknown"` - `"0.0"` - `"1.0"` - `"2.0"` - `"3.0"` - `"4.0"` - `"5.0"` - `"6.0"` - `"7.0"` - `"8.0"` - `"9.0"` |
| **patch**  integer | no description |
| **platform_str**  string | no description |
| **prefer_img_ver**  string | no description |
| **prio**  integer | no description |
| **private_key**  string | no description |
| **private_key_status**  integer | no description |
| **psk**  string | no description |
| **role**  string | no description  **Choices:**   - `"master"` - `"ha-slave"` - `"autoscale-slave"` |
| **sn**  string | Unique value for each device. |
| **vdom**  list / elements=dictionary | no description |
| **comments**  string | no description |
| **meta fields**  dictionary | no description |
| **name**  string | no description |
| **opmode**  string | no description  **Choices:**   - `"nat"` - `"transparent"` |
| **rtm_prof_id**  integer | no description |
| **status**  string | no description |
| **vdom_type**  string | no description  **Choices:**   - `"traffic"` - `"admin"` |
| **vpn_id**  integer | no description |
| **version**  integer | no description |
| **vm_cpu**  integer | no description |
| **vm_cpu_limit**  integer | no description |
| **vm_lic_expire**  integer | no description |
| **vm_lic_overdue_since**  integer | no description |
| **vm_mem**  integer | no description |
| **vm_mem_limit**  integer | no description |
| **vm_status**  any | (int or str) no description |
| **import-group-members**  list / elements=dictionary | no description |
| **adom**  string | ADOM where the device group is located. |
| **dev**  string | no description |
| **grp**  string | Target device group to associate device VDOM with. |
| **vdom**  string | no description |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_dvm_cmd_import_devlist_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_dvm_cmd_import_devlist_module.md#id4)

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
    - name: Import a list of ADOMs and devices.
      fmgr_dvm_cmd_import_devlist:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        dvm_cmd_import_devlist:
          adom: <string>
          flags:
            - none
            - create_task
            - nonblocking
            - log_dev
          import-adom-members:
            -
              adom: <string>
              dev: <string>
              vdom: <string>
          import-adoms:
            -
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
          import-devices:
            -
              adm_pass: <list or string>
              adm_usr: <string>
              app_ver: <string>
              av_ver: <string>
              beta: <integer>
              branch_pt: <integer>
              build: <integer>
              checksum: <string>
              conf_status: <value in [unknown, insync, outofsync]>
              conn_mode: <value in [active, passive]>
              conn_status: <value in [UNKNOWN, up, down]>
              db_status: <value in [unknown, nomod, mod]>
              desc: <string>
              dev_status: <value in [none, unknown, checkedin, ...]>
              fap_cnt: <integer>
              faz.full_act: <integer>
              faz.perm: <integer>
              faz.quota: <integer>
              faz.used: <integer>
              fex_cnt: <integer>
              flags:
                - has_hdd
                - vdom_enabled
                - discover
                - reload
                - interim_build
                - offline_mode
                - is_model
                - fips_mode
                - linked_to_model
                - ip-conflict
                - faz-autosync
                - need_reset
                - backup_mode
                - azure_vwan_nva
                - fgsp_configured
                - cnf_mode
                - sase_managed
              foslic_cpu: <integer>
              foslic_dr_site: <value in [disable, enable]>
              foslic_inst_time: <integer>
              foslic_last_sync: <integer>
              foslic_ram: <integer>
              foslic_type: <value in [temporary, trial, regular, ...]>
              foslic_utm:
                - fw
                - av
                - ips
                - app
                - url
                - utm
                - fwb
              fsw_cnt: <integer>
              ha_group_id: <integer>
              ha_group_name: <string>
              ha_mode: <value in [standalone, AP, AA, ...]>
              ha_slave:
                -
                  idx: <integer>
                  name: <string>
                  prio: <integer>
                  role: <value in [slave, master]>
                  sn: <string>
                  status: <integer>
                  conf_status: <integer>
              hdisk_size: <integer>
              hostname: <string>
              hw_rev_major: <integer>
              hw_rev_minor: <integer>
              ip: <string>
              ips_ext: <integer>
              ips_ver: <string>
              last_checked: <integer>
              last_resync: <integer>
              latitude: <string>
              lic_flags: <integer>
              lic_region: <string>
              location_from: <string>
              logdisk_size: <integer>
              longitude: <string>
              maxvdom: <integer>
              meta fields: <dict>
              mgmt_id: <integer>
              mgmt_if: <string>
              mgmt_mode: <value in [unreg, fmg, faz, ...]>
              mgt_vdom: <string>
              mr: <integer>
              name: <string>
              os_type: <value in [unknown, fos, fsw, ...]>
              os_ver: <value in [unknown, 0.0, 1.0, ...]>
              patch: <integer>
              platform_str: <string>
              psk: <string>
              sn: <string>
              vdom:
                -
                  comments: <string>
                  name: <string>
                  opmode: <value in [nat, transparent]>
                  rtm_prof_id: <integer>
                  status: <string>
                  vpn_id: <integer>
                  meta fields: <dict>
                  vdom_type: <value in [traffic, admin]>
              version: <integer>
              vm_cpu: <integer>
              vm_cpu_limit: <integer>
              vm_lic_expire: <integer>
              vm_mem: <integer>
              vm_mem_limit: <integer>
              vm_status: <integer or string> <value in [N/A, No License, Startup, ...]>
              module_sn: <string>
              prefer_img_ver: <string>
              prio: <integer>
              role: <value in [master, ha-slave, autoscale-slave]>
              hyperscale: <integer>
              nsxt_service_name: <string>
              private_key: <string>
              private_key_status: <integer>
              vm_lic_overdue_since: <integer>
              first_tunnel_up: <integer>
              eip: <string>
              mgmt_uuid: <string>
              hw_generation: <integer>
          import-group-members:
            -
              adom: <string>
              dev: <string>
              grp: <string>
              vdom: <string>
```

## [Return Values](fmgr_dvm_cmd_import_devlist_module.md#id5)

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
