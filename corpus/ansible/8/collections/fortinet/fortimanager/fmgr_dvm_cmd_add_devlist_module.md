---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_dvm_cmd_add_devlist module – Add multiple devices to the Device Manager database."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_dvm_cmd_add_devlist_module.html
fetched_at: 2026-07-28T02:09:30+00:00
---
# fortinet.fortimanager.fmgr_dvm_cmd_add_devlist module – Add multiple devices to the Device Manager database.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_dvm_cmd_add_devlist`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_dvm_cmd_add_devlist_module.md#synopsis)
- [Parameters](fmgr_dvm_cmd_add_devlist_module.md#parameters)
- [Notes](fmgr_dvm_cmd_add_devlist_module.md#notes)
- [Examples](fmgr_dvm_cmd_add_devlist_module.md#examples)
- [Return Values](fmgr_dvm_cmd_add_devlist_module.md#return-values)

## [Synopsis](fmgr_dvm_cmd_add_devlist_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_dvm_cmd_add_devlist_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **dvm_cmd_add_devlist**  dictionary | the top level parameters set |
| **add-dev-list**  list / elements=dictionary | no description |
| **adm_pass**  any | (list) no description |
| **adm_usr**  string | add real and promote device. |
| **authorization template**  string | add model device only. |
| **desc**  string | available for all operations. |
| **device action**  string | Specify add device operations, or leave blank to add real device  add_model - add a model device.  promote_unreg - promote an unregistered device to be managed by FortiManager using information from database. |
| **device blueprint**  string | add model device only. |
| **faz.quota**  integer | available for all operations. |
| **ip**  string | add real device only. |
| **meta fields**  any | (dict or str) add real and model device. |
| **mgmt_mode**  string | add real and model device.  **Choices:**   - `"unreg"` - `"fmg"` - `"faz"` - `"fmgfaz"` |
| **mr**  integer | add model device only. |
| **name**  string | required for all operations. |
| **os_type**  string | add model device only.  **Choices:**   - `"unknown"` - `"fos"` - `"fsw"` - `"foc"` - `"fml"` - `"faz"` - `"fwb"` - `"fch"` - `"fct"` - `"log"` - `"fmg"` - `"fsa"` - `"fdd"` - `"fac"` - `"fpx"` - `"fna"` |
| **os_ver**  string | add model device only.  **Choices:**   - `"unknown"` - `"0.0"` - `"1.0"` - `"2.0"` - `"3.0"` - `"4.0"` - `"5.0"` - `"6.0"` - `"7.0"` - `"8.0"` |
| **patch**  integer | add model device only. |
| **platform_str**  string | add model device only. |
| **sn**  string | add model device only. |
| **adom**  string | Name or ID of the ADOM where the command is to be executed on. |
| **flags**  list / elements=string | no description  **Choices:**   - `"none"` - `"create_task"` - `"nonblocking"` - `"log_dev"` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_dvm_cmd_add_devlist_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_dvm_cmd_add_devlist_module.md#id4)

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
    - name: Add multiple devices to the Device Manager database.
      fmgr_dvm_cmd_add_devlist:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        dvm_cmd_add_devlist:
          add-dev-list:
            -
              adm_pass: <list or string>
              adm_usr: <string>
              desc: <string>
              device action: <string>
              faz.quota: <integer>
              ip: <string>
              meta fields: <dict or string>
              mgmt_mode: <value in [unreg, fmg, faz, ...]>
              mr: <integer>
              name: <string>
              os_type: <value in [unknown, fos, fsw, ...]>
              os_ver: <value in [unknown, 0.0, 1.0, ...]>
              patch: <integer>
              platform_str: <string>
              sn: <string>
              device blueprint: <string>
              authorization template: <string>
          adom: <string>
          flags:
            - none
            - create_task
            - nonblocking
            - log_dev
```

## [Return Values](fmgr_dvm_cmd_add_devlist_module.md#id5)

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
