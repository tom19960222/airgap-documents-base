---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_user_fsso_dynamicmapping module – Configure Fortinet Single Sign On"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_user_fsso_dynamicmapping_module.html
fetched_at: 2026-07-28T02:20:51+00:00
---
# fortinet.fortimanager.fmgr_user_fsso_dynamicmapping module – Configure Fortinet Single Sign On

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_user_fsso_dynamicmapping`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_user_fsso_dynamicmapping_module.md#synopsis)
- [Parameters](fmgr_user_fsso_dynamicmapping_module.md#parameters)
- [Notes](fmgr_user_fsso_dynamicmapping_module.md#notes)
- [Examples](fmgr_user_fsso_dynamicmapping_module.md#examples)
- [Return Values](fmgr_user_fsso_dynamicmapping_module.md#return-values)

## [Synopsis](fmgr_user_fsso_dynamicmapping_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_user_fsso_dynamicmapping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **fsso**  string / required | the parameter (fsso) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **user_fsso_dynamicmapping**  dictionary | the top level parameters set |
| **_gui_meta**  string | no description |
| **_scope**  list / elements=dictionary | no description |
| **name**  string | no description |
| **vdom**  string | no description |
| **group-poll-interval**  integer | no description |
| **interface**  string | no description |
| **interface-select-method**  string | no description  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **ldap-poll**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ldap-poll-filter**  string | no description |
| **ldap-poll-interval**  integer | no description |
| **ldap-server**  string | no description |
| **logon-timeout**  integer | Interval in minutes to keep logons after FSSO server down. |
| **password**  any | (list) no description |
| **password2**  any | (list) no description |
| **password3**  any | (list) no description |
| **password4**  any | (list) no description |
| **password5**  any | (list) no description |
| **port**  integer | no description |
| **port2**  integer | no description |
| **port3**  integer | no description |
| **port4**  integer | no description |
| **port5**  integer | no description |
| **server**  string | no description |
| **server2**  string | no description |
| **server3**  string | no description |
| **server4**  string | no description |
| **server5**  string | no description |
| **sni**  string | Server Name Indication. |
| **source-ip**  string | no description |
| **source-ip6**  string | no description |
| **ssl**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-server-host-ip-check**  string | Enable/disable server host/IP verification.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-trusted-cert**  string | no description |
| **type**  string | no description  **Choices:**   - `"default"` - `"fortiems"` - `"fortinac"` - `"fortiems-cloud"` |
| **user-info-server**  any | (list or str) no description |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_user_fsso_dynamicmapping_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_user_fsso_dynamicmapping_module.md#id4)

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
   - name: retrieve all the dynamic mappings of Fortinet Single Sign On (FSSO) agent
     fmgr_fact:
       facts:
           selector: 'user_fsso_dynamicmapping'
           params:
               adom: 'ansible'
               fsso: 'ansible-test-fsso' # name
               dynamic_mapping: 'your_value'

- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure dynamic mappings of Fortinet Single Sign On (FSSO) agent
     fmgr_user_fsso_dynamicmapping:
        bypass_validation: False
        adom: ansible
        fsso: ansible-test-fsso # name
        state: present
        user_fsso_dynamicmapping:
           _scope:
             -
                 name: FGT_AWS # need a valid device name
                 vdom: root # need a valid vdom name under the device
           password: fortinet
           port: 9000
           server: ansible
```

## [Return Values](fmgr_user_fsso_dynamicmapping_module.md#id5)

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
