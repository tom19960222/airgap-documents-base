---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_dvmdb_device module – Device table, most attributes are read-only and can only be changed internally."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_dvmdb_device_module.html
fetched_at: 2026-07-28T02:09:39+00:00
---
# fortinet.fortimanager.fmgr_dvmdb_device module – Device table, most attributes are read-only and can only be changed internally.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_dvmdb_device`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_dvmdb_device_module.md#synopsis)
- [Parameters](fmgr_dvmdb_device_module.md#parameters)
- [Notes](fmgr_dvmdb_device_module.md#notes)
- [Examples](fmgr_dvmdb_device_module.md#examples)
- [Return Values](fmgr_dvmdb_device_module.md#return-values)

## [Synopsis](fmgr_dvmdb_device_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_dvmdb_device_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **device**  string / required | the parameter (device) in requested url |
| **dvmdb_device**  dictionary | the top level parameters set |
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
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_dvmdb_device_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_dvmdb_device_module.md#id4)

```yaml+jinja
- name: Delete first FOS devices from FMG In a specific adom
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
    device_adom: 'root'
  tasks:
    - name: fetch all devices
      fmgr_fact:
        facts:
            selector: 'dvmdb_device'
            params:
                adom: '{{ device_adom }}'
                device: 'your_value'
      register: alldevices
    - when: alldevices.meta.response_data != []
      debug:
        msg:
         - 'We are going to delete device: {{ alldevices.meta.response_data[0].name }}'
         - 'IP of the device is: {{ alldevices.meta.response_data[0].ip }}'
    - when: alldevices.meta.response_data != [] and False
      name: Create The Task To Delete The Device
      fmgr_dvm_cmd_del_device:
        dvm_cmd_del_device:
            device: '{{ alldevices.meta.response_data[0].name }}'
            adom: '{{ device_adom }}'
            flags:
             - 'create_task'
             - 'nonblocking'
      register: uninstalling_task
    - when: alldevices.meta.response_data != [] and False
      name: poll the task
      fmgr_fact:
        facts:
            selector: 'task_task'
            params:
                task: '{{uninstalling_task.meta.response_data.taskid}}'
      register: taskinfo
      until: taskinfo.meta.response_data.percent == 100
      retries: 30
      delay: 5
      failed_when: taskinfo.meta.response_data.state == 'error'
```

## [Return Values](fmgr_dvmdb_device_module.md#id5)

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
