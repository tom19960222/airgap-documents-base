---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_dvm_cmd_add_devlist module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_dvm_cmd_add_devlist_module.html
fetched_at: 2026-07-27T17:29:21+00:00
---
# fortinet.fortimanager.fmgr_dvm_cmd_add_devlist module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_dvm_cmd_add_devlist`.

New in fortinet.fortimanager 1.0.0

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
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **dvm_cmd_add_devlist**  dictionary | the top level parameters set |
| **add-dev-list**  list / elements=string | description |
| **adm_pass**  string | description |
| **adm_usr**  string | no description |
| **desc**  string | no description |
| **device action**  string | no description  no description  no description |
| **device blueprint**  string | no description |
| **faz.quota**  integer | no description |
| **ip**  string | no description |
| **meta fields**  string | no description |
| **mgmt_mode**  string | no description  Choices:   - `"unreg"` - `"fmg"` - `"faz"` - `"fmgfaz"` |
| **mr**  integer | no description |
| **name**  string | no description |
| **os_type**  string | no description  Choices:   - `"unknown"` - `"fos"` - `"fsw"` - `"foc"` - `"fml"` - `"faz"` - `"fwb"` - `"fch"` - `"fct"` - `"log"` - `"fmg"` - `"fsa"` - `"fdd"` - `"fac"` - `"fpx"` - `"fna"` |
| **os_ver**  string | no description  Choices:   - `"unknown"` - `"0.0"` - `"1.0"` - `"2.0"` - `"3.0"` - `"4.0"` - `"5.0"` - `"6.0"` - `"7.0"` - `"8.0"` |
| **patch**  integer | no description |
| **platform_str**  string | no description |
| **sn**  string | no description |
| **adom**  string | no description |
| **flags**  list / elements=string | description  Choices:   - `"none"` - `"create_task"` - `"nonblocking"` - `"log_dev"` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

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
   - name: no description
     fmgr_dvm_cmd_add_devlist:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        dvm_cmd_add_devlist:
           add-dev-list:
             -
                 adm_pass: <value of string>
                 adm_usr: <value of string>
                 desc: <value of string>
                 device action: <value of string>
                 faz.quota: <value of integer>
                 ip: <value of string>
                 meta fields: <value of string>
                 mgmt_mode: <value in [unreg, fmg, faz, ...]>
                 mr: <value of integer>
                 name: <value of string>
                 os_type: <value in [unknown, fos, fsw, ...]>
                 os_ver: <value in [unknown, 0.0, 1.0, ...]>
                 patch: <value of integer>
                 platform_str: <value of string>
                 sn: <value of string>
                 device blueprint: <value of string>
           adom: <value of string>
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
