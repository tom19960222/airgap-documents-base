---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_logfetch_clientprofile module – Log-fetch client profile settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_logfetch_clientprofile_module.html
fetched_at: 2026-07-28T02:19:11+00:00
---
# fortinet.fortimanager.fmgr_system_logfetch_clientprofile module – Log-fetch client profile settings.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_logfetch_clientprofile`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_logfetch_clientprofile_module.md#synopsis)
- [Parameters](fmgr_system_logfetch_clientprofile_module.md#parameters)
- [Notes](fmgr_system_logfetch_clientprofile_module.md#notes)
- [Examples](fmgr_system_logfetch_clientprofile_module.md#examples)
- [Return Values](fmgr_system_logfetch_clientprofile_module.md#return-values)

## [Synopsis](fmgr_system_logfetch_clientprofile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_logfetch_clientprofile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **system_logfetch_clientprofile**  dictionary | the top level parameters set |
| **client-adom**  string | Log-fetch client sides adom name. |
| **data-range**  string | Data-range for fetched logs.  custom - Specify some other date and time range.  **Choices:**   - `"custom"` |
| **data-range-value**  integer | Last n days or hours. |
| **device-filter**  list / elements=dictionary | Device-Filter. |
| **adom**  string | Adom name. |
| **device**  string | Device name or Serial number. |
| **id**  integer | Add or edit a device filter. |
| **vdom**  string | Vdom filters. |
| **end-time**  any | (list) End date and time of the data-range |
| **id**  integer / required | Log-fetch client profile ID. |
| **index-fetch-logs**  string | Enable/Disable indexing logs automatically after fetching logs.  disable - Disable attribute function.  enable - Enable attribute function.  **Choices:**   - `"disable"` - `"enable"` |
| **log-filter**  list / elements=dictionary | Log-Filter. |
| **field**  string | Field name. |
| **id**  integer | Log filter ID. |
| **oper**  string | Field filter operator.  no description  no description  contain - Contain  not-contain - Not contain  match - Match  **Choices:**   - `"="` - `"!="` - `"<"` - `">"` - `"<="` - `">="` - `"contain"` - `"not-contain"` - `"match"` |
| **value**  string | Field filter operand or free-text matching expression. |
| **log-filter-logic**  string | And/Or logic for log-filters.  and - Logic And.  or - Logic Or.  **Choices:**   - `"and"` - `"or"` |
| **log-filter-status**  string | Enable/Disable log-filter.  disable - Disable attribute function.  enable - Enable attribute function.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string | Name of log-fetch client profile. |
| **password**  any | (list) Log-fetch server login password. |
| **peer-cert-cn**  string | Certificate common name of log-fetch server. |
| **secure-connection**  string | Enable/Disable protecting log-fetch connection with TLS/SSL.  disable - Disable attribute function.  enable - Enable attribute function.  **Choices:**   - `"disable"` - `"enable"` |
| **server-adom**  string | Log-fetch server sides adom name. |
| **server-ip**  string | Log-fetch server IP address. |
| **start-time**  any | (list) Start date and time of the data-range |
| **sync-adom-config**  string | Enable/Disable sync adom related config.  disable - Disable attribute function.  enable - Enable attribute function.  **Choices:**   - `"disable"` - `"enable"` |
| **user**  string | Log-fetch server login username. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_logfetch_clientprofile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_logfetch_clientprofile_module.md#id4)

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
   - name: retrieve all the Log-fetch client profile settings
     fmgr_fact:
       facts:
           selector: 'system_logfetch_clientprofile'
           params:
               client-profile: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Log-fetch client profile settings.
     fmgr_system_logfetch_clientprofile:
        bypass_validation: False
        state: present
        system_logfetch_clientprofile:
           client-adom: ansible
           data-range: custom #<value in [custom]>
           id: 1
           index-fetch-logs: enable
           name: ansible-test-clientprofile
           password: fortinet
           server-ip: '222.222.22.25'
           user: ansible
```

## [Return Values](fmgr_system_logfetch_clientprofile_module.md#id5)

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
