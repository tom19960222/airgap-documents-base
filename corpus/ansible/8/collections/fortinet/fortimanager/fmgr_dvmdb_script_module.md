---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_dvmdb_script module – Script table."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_dvmdb_script_module.html
fetched_at: 2026-07-28T02:09:46+00:00
---
# fortinet.fortimanager.fmgr_dvmdb_script module – Script table.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_dvmdb_script`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_dvmdb_script_module.md#synopsis)
- [Parameters](fmgr_dvmdb_script_module.md#parameters)
- [Notes](fmgr_dvmdb_script_module.md#notes)
- [Examples](fmgr_dvmdb_script_module.md#examples)
- [Return Values](fmgr_dvmdb_script_module.md#return-values)

## [Synopsis](fmgr_dvmdb_script_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_dvmdb_script_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **dvmdb_script**  dictionary | the top level parameters set |
| **content**  string | The full content of the script result log. |
| **desc**  string | Desc. |
| **filter_build**  integer | The value will be ignored in add/set/update requests if filter_ostype is not set. |
| **filter_device**  integer | Name or id of an existing device in the database. |
| **filter_hostname**  string | The value has no effect if target is adom_database. |
| **filter_ostype**  string | The value has no effect if target is adom_database.  **Choices:**   - `"unknown"` - `"fos"` |
| **filter_osver**  string | The value will be ignored in add/set/update requests if filter_ostype is not set.  **Choices:**   - `"unknown"` - `"4.00"` - `"5.00"` - `"6.00"` |
| **filter_platform**  string | The value will be ignored in add/set/update requests if filter_ostype is not set. |
| **filter_serial**  string | The value has no effect if target is adom_database. |
| **modification_time**  string | It is a read-only attribute indicating the time when the script was created or modified. |
| **name**  string / required | Name. |
| **script_schedule**  list / elements=dictionary | Script_Schedule. |
| **datetime**  string | Indicates the date and time of the schedule.  onetime  daily  weekly  monthly |
| **day_of_week**  string | Day_Of_Week.  **Choices:**   - `"unknown"` - `"sun"` - `"mon"` - `"tue"` - `"wed"` - `"thu"` - `"fri"` - `"sat"` |
| **device**  integer | Name or id of an existing device in the database. |
| **name**  string | Name. |
| **run_on_db**  string | Indicates if the scheduled script should be executed on device database.  **Choices:**   - `"disable"` - `"enable"` |
| **type**  string | Type.  **Choices:**   - `"auto"` - `"onetime"` - `"daily"` - `"weekly"` - `"monthly"` |
| **target**  string | Target.  **Choices:**   - `"device_database"` - `"remote_device"` - `"adom_database"` |
| **type**  string | Type.  **Choices:**   - `"cli"` - `"tcl"` - `"cligrp"` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_dvmdb_script_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_dvmdb_script_module.md#id4)

```yaml+jinja
- name: gathering fortimanager facts
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: retrieve all the scripts in the device
     fmgr_fact:
       facts:
           selector: 'dvmdb_script'
           params:
               adom: 'ansible'
               script: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: enable workspace mode
     fmgr_system_global:
        system_global:
             adom-status: enable
             workspace-mode: normal

   - name: Script table.
     fmgr_dvmdb_script:
        bypass_validation: False
        adom: root
        state: present
        workspace_locking_adom: 'root'
        dvmdb_script:
           content: 'ansiblt-test'
           name: 'fooscript000'
           target: device_database
           type: cli

   - name: verify script table
     fmgr_fact:
        facts:
           selector: 'dvmdb_script'
           params:
               adom: 'root'
               script: 'fooscript000'
     register: info
     failed_when: info.meta.response_code != 0

   - name: restore workspace mode
     fmgr_system_global:
        system_global:
            adom-status: enable
            workspace-mode: disabled

- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Script table.
     fmgr_dvmdb_script:
        bypass_validation: False
        adom: ansible
        state: present
        dvmdb_script:
           content: 'ansiblt-test'
           name: 'ansible-test'
           target: device_database
           type: cli
- name: Apply a script to device
  hosts: fortimanager01
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
    device_adom: 'root'
    script_name: 'FooScript'
    device_name: 'CustomHostName'
    device_vdom: 'root'
  tasks:
    - name: Create a Script to later execute
      fmgr_dvmdb_script:
        adom: '{{ device_adom }}'
        state: 'present'
        dvmdb_script:
            name: '{{ script_name }}'
            desc: 'A script created via Ansible'
            content: |
                        config system global
                            set remoteauthtimeout 80
                        end
            type: 'cli'
    - name: Run the Script
      fmgr_dvmdb_script_execute:
        adom: '{{ device_adom }}'
        dvmdb_script_execute:
            adom: '{{ device_adom }}'
            script: '{{ script_name }}'
            scope:
               - name: '{{ device_name }}'
                 vdom: '{{ device_vdom }}'
      register: running_task
    - name: Inspect the Task Status
      fmgr_fact:
        facts:
            selector: 'task_task'
            params:
                task: '{{running_task.meta.response_data.task}}'
      register: taskinfo
      until: taskinfo.meta.response_data.percent == 100
      retries: 30
      delay: 3
      failed_when: taskinfo.meta.response_data.state == 'error'
```

## [Return Values](fmgr_dvmdb_script_module.md#id5)

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
