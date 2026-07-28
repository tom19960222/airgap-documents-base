---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_user_fsso module – Configure Fortinet Single Sign On"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_user_fsso_module.html
fetched_at: 2026-07-28T02:20:50+00:00
---
# fortinet.fortimanager.fmgr_user_fsso module – Configure Fortinet Single Sign On

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_user_fsso`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_user_fsso_module.md#synopsis)
- [Parameters](fmgr_user_fsso_module.md#parameters)
- [Notes](fmgr_user_fsso_module.md#notes)
- [Examples](fmgr_user_fsso_module.md#examples)
- [Return Values](fmgr_user_fsso_module.md#return-values)

## [Synopsis](fmgr_user_fsso_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_user_fsso_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **user_fsso**  dictionary | the top level parameters set |
| **_gui_meta**  string | _Gui_Meta. |
| **dynamic_mapping**  list / elements=dictionary | Dynamic_Mapping. |
| **_gui_meta**  string | _Gui_Meta. |
| **_scope**  list / elements=dictionary | _Scope. |
| **name**  string | Name. |
| **vdom**  string | Vdom. |
| **group-poll-interval**  integer | Interval in minutes within to fetch groups from FSSO server, or unset to disable. |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **ldap-poll**  string | Enable/disable automatic fetching of groups from LDAP server.  **Choices:**   - `"disable"` - `"enable"` |
| **ldap-poll-filter**  string | Filter used to fetch groups. |
| **ldap-poll-interval**  integer | Interval in minutes within to fetch groups from LDAP server. |
| **ldap-server**  string | LDAP server to get group information. |
| **logon-timeout**  integer | Interval in minutes to keep logons after FSSO server down. |
| **password**  any | (list) Password of the first FSSO collector agent. |
| **password2**  any | (list) Password of the second FSSO collector agent. |
| **password3**  any | (list) Password of the third FSSO collector agent. |
| **password4**  any | (list) Password of the fourth FSSO collector agent. |
| **password5**  any | (list) Password of the fifth FSSO collector agent. |
| **port**  integer | Port of the first FSSO collector agent. |
| **port2**  integer | Port of the second FSSO collector agent. |
| **port3**  integer | Port of the third FSSO collector agent. |
| **port4**  integer | Port of the fourth FSSO collector agent. |
| **port5**  integer | Port of the fifth FSSO collector agent. |
| **server**  string | Domain name or IP address of the first FSSO collector agent. |
| **server2**  string | Domain name or IP address of the second FSSO collector agent. |
| **server3**  string | Domain name or IP address of the third FSSO collector agent. |
| **server4**  string | Domain name or IP address of the fourth FSSO collector agent. |
| **server5**  string | Domain name or IP address of the fifth FSSO collector agent. |
| **sni**  string | Server Name Indication. |
| **source-ip**  string | Source IP for communications to FSSO agent. |
| **source-ip6**  string | IPv6 source for communications to FSSO agent. |
| **ssl**  string | Enable/disable use of SSL.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-server-host-ip-check**  string | Enable/disable server host/IP verification.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-trusted-cert**  string | Trusted server certificate or CA certificate. |
| **type**  string | Server type.  **Choices:**   - `"default"` - `"fortiems"` - `"fortinac"` - `"fortiems-cloud"` |
| **user-info-server**  any | (list or str) LDAP server to get user information. |
| **group-poll-interval**  integer | Interval in minutes within to fetch groups from FSSO server, or unset to disable. |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **ldap-poll**  string | Enable/disable automatic fetching of groups from LDAP server.  **Choices:**   - `"disable"` - `"enable"` |
| **ldap-poll-filter**  string | Filter used to fetch groups. |
| **ldap-poll-interval**  integer | Interval in minutes within to fetch groups from LDAP server. |
| **ldap-server**  string | LDAP server to get group information. |
| **logon-timeout**  integer | Interval in minutes to keep logons after FSSO server down. |
| **name**  string / required | Name. |
| **password**  any | (list) Password of the first FSSO collector agent. |
| **password2**  any | (list) Password of the second FSSO collector agent. |
| **password3**  any | (list) Password of the third FSSO collector agent. |
| **password4**  any | (list) Password of the fourth FSSO collector agent. |
| **password5**  any | (list) Password of the fifth FSSO collector agent. |
| **port**  integer | Port of the first FSSO collector agent. |
| **port2**  integer | Port of the second FSSO collector agent. |
| **port3**  integer | Port of the third FSSO collector agent. |
| **port4**  integer | Port of the fourth FSSO collector agent. |
| **port5**  integer | Port of the fifth FSSO collector agent. |
| **server**  string | Domain name or IP address of the first FSSO collector agent. |
| **server2**  string | Domain name or IP address of the second FSSO collector agent. |
| **server3**  string | Domain name or IP address of the third FSSO collector agent. |
| **server4**  string | Domain name or IP address of the fourth FSSO collector agent. |
| **server5**  string | Domain name or IP address of the fifth FSSO collector agent. |
| **sni**  string | Server Name Indication. |
| **source-ip**  string | Source IP for communications to FSSO agent. |
| **source-ip6**  string | IPv6 source for communications to FSSO agent. |
| **ssl**  string | Enable/disable use of SSL.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-server-host-ip-check**  string | Enable/disable server host/IP verification.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-trusted-cert**  string | Trusted server certificate or CA certificate. |
| **type**  string | Server type.  **Choices:**   - `"default"` - `"fortiems"` - `"fortinac"` - `"fortiems-cloud"` |
| **user-info-server**  string | LDAP server to get user information. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_user_fsso_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_user_fsso_module.md#id4)

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
   - name: retrieve all the Fortinet Single Sign On (FSSO) agents
     fmgr_fact:
       facts:
           selector: 'user_fsso'
           params:
               adom: 'ansible'
               fsso: 'your_value'

- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure Fortinet Single Sign On (FSSO) agents.
     fmgr_user_fsso:
        bypass_validation: False
        adom: ansible
        state: present
        user_fsso:
           name: ansible-test-fsso
           password: fortinet
           port: 9000
           server: ansible
```

## [Return Values](fmgr_user_fsso_module.md#id5)

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
