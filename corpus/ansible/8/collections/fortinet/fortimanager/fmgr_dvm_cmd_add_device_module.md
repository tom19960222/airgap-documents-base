---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_dvm_cmd_add_device module – Add a device to the Device Manager database."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_dvm_cmd_add_device_module.html
fetched_at: 2026-07-28T02:09:29+00:00
---
# fortinet.fortimanager.fmgr_dvm_cmd_add_device module – Add a device to the Device Manager database.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_dvm_cmd_add_device`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_dvm_cmd_add_device_module.md#synopsis)
- [Parameters](fmgr_dvm_cmd_add_device_module.md#parameters)
- [Notes](fmgr_dvm_cmd_add_device_module.md#notes)
- [Examples](fmgr_dvm_cmd_add_device_module.md#examples)
- [Return Values](fmgr_dvm_cmd_add_device_module.md#return-values)

## [Synopsis](fmgr_dvm_cmd_add_device_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_dvm_cmd_add_device_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **dvm_cmd_add_device**  dictionary | the top level parameters set |
| **adom**  string | Name or ID of the ADOM where the command is to be executed on. |
| **device**  dictionary | no description |
| **adm_pass**  any | (list) no description |
| **adm_usr**  string | add real and promote device. |
| **authorization template**  string | add model device only. |
| **desc**  string | available for all operations. |
| **device action**  string | Specify add device operations, or leave blank to add real device  add_model - add a model device.  promote_unreg - promote an unregistered device to be managed by FortiManager using information from database. |
| **device blueprint**  string | add model device only. |
| **faz.quota**  integer | available for all operations. |
| **ip**  string | add real device only. |
| **meta fields**  any | (dict or str) no description |
| **mgmt_mode**  string | add real and model device.  **Choices:**   - `"unreg"` - `"fmg"` - `"faz"` - `"fmgfaz"` |
| **mr**  integer | add model device only. |
| **name**  string | required for all operations. |
| **os_type**  string | add model device only.  **Choices:**   - `"unknown"` - `"fos"` - `"fsw"` - `"foc"` - `"fml"` - `"faz"` - `"fwb"` - `"fch"` - `"fct"` - `"log"` - `"fmg"` - `"fsa"` - `"fdd"` - `"fac"` - `"fpx"` - `"fna"` |
| **os_ver**  string | add model device only.  **Choices:**   - `"unknown"` - `"0.0"` - `"1.0"` - `"2.0"` - `"3.0"` - `"4.0"` - `"5.0"` - `"6.0"` - `"7.0"` - `"8.0"` |
| **patch**  integer | add model device only. |
| **platform_str**  string | add model device only. |
| **sn**  string | add model device only. |
| **flags**  list / elements=string | no description  **Choices:**   - `"none"` - `"create_task"` - `"nonblocking"` - `"log_dev"` |
| **groups**  list / elements=dictionary | no description |
| **name**  string | no description |
| **vdom**  string | no description |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_dvm_cmd_add_device_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_dvm_cmd_add_device_module.md#id4)

```yaml+jinja
- name: Add a FOS device to FMG
  hosts: fortimanager01
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
    fos_user: 'admin'
    fos_pass: 'password'
    fos_ip: '192.168.190.151'
  tasks:
    - name: discover device
      fmgr_dvm_cmd_discover_device:
        bypass_validation: True
        dvm_cmd_discover_device:
            device:
                adm_pass: '{{ fos_pass }}'
                adm_usr: '{{ fos_user }}'
                ip: '{{ fos_ip }}'
      register: probed_device
    - name: add device
      fmgr_dvm_cmd_add_device:
        bypass_validation: True
        dvm_cmd_add_device:
            adom: 'root'
            flags:
              - 'create_task'
              - 'nonblocking'
            device:
                adm_usr: '{{ probed_device.meta.response_data.device.adm_usr }}'
                adm_pass: '{{ probed_device.meta.response_data.device.adm_pass }}'
                desc: 'The device is added via FortiManager Ansible'
                ip: '{{ probed_device.meta.response_data.device.ip }}'
                mgmt_mode: 'fmg'
                name: '{{ probed_device.meta.response_data.device.name }}'
                sn: '{{ probed_device.meta.response_data.device.sn }}'
      register: installing_task
    - name: poll the task
      fmgr_fact:
        facts:
            selector: 'task_task'
            params:
                task: '{{installing_task.meta.response_data.taskid}}'
      register: taskinfo
      until: taskinfo.meta.response_data.percent == 100
      retries: 30
      delay: 5
      failed_when: taskinfo.meta.response_data.state == 'error' and 'devsnexist' not in taskinfo.meta.response_data.line[0].detail

- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Add a device to the Device Manager database.
     fmgr_dvm_cmd_add_device:
        bypass_validation: False
        dvm_cmd_add_device:
           adom: ansible
           device:
              adm_pass: fortinet # device password
              adm_usr: admin # device user name
              ip: 0.0.0.0 # device ip
              mgmt_mode: fmg #<value in [unreg, fmg, faz, ...]>
              name: FGT_AWS
           flags:
             - none
             - create_task
             - nonblocking
             - log_dev
```

## [Return Values](fmgr_dvm_cmd_add_device_module.md#id5)

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
