---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_dvmdb_script_execute module – Run script."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_dvmdb_script_execute_module.html
fetched_at: 2026-07-28T02:09:47+00:00
---
# fortinet.fortimanager.fmgr_dvmdb_script_execute module – Run script.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_dvmdb_script_execute`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_dvmdb_script_execute_module.md#synopsis)
- [Parameters](fmgr_dvmdb_script_execute_module.md#parameters)
- [Notes](fmgr_dvmdb_script_execute_module.md#notes)
- [Examples](fmgr_dvmdb_script_execute_module.md#examples)
- [Return Values](fmgr_dvmdb_script_execute_module.md#return-values)

## [Synopsis](fmgr_dvmdb_script_execute_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_dvmdb_script_execute_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **dvmdb_script_execute**  dictionary | the top level parameters set |
| **adom**  string | no description |
| **package**  string | no description |
| **scope**  list / elements=dictionary | no description |
| **name**  string | no description |
| **vdom**  string | no description |
| **script**  string | Script name. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_dvmdb_script_execute_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_dvmdb_script_execute_module.md#id4)

```yaml+jinja
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Run script.
     fmgr_dvmdb_script_execute:
        bypass_validation: False
        adom: ansible
        dvmdb_script_execute:
           adom: ansible
           package: 'your_value'
           scope:
             -
                 name: ansible-test
                 vdom: root
           script: ansible-test
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

## [Return Values](fmgr_dvmdb_script_execute_module.md#id5)

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
