---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_sql_customindex module – List of SQL index fields."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_sql_customindex_module.html
fetched_at: 2026-07-28T02:20:26+00:00
---
# fortinet.fortimanager.fmgr_system_sql_customindex module – List of SQL index fields.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_sql_customindex`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_sql_customindex_module.md#synopsis)
- [Parameters](fmgr_system_sql_customindex_module.md#parameters)
- [Notes](fmgr_system_sql_customindex_module.md#notes)
- [Examples](fmgr_system_sql_customindex_module.md#examples)
- [Return Values](fmgr_system_sql_customindex_module.md#return-values)

## [Synopsis](fmgr_system_sql_customindex_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_sql_customindex_module.md#id2)

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
| **system_sql_customindex**  dictionary | the top level parameters set |
| **case-sensitive**  string | Disable/Enable case sensitive index.  disable - Build a case insensitive index.  enable - Build a case sensitive index.  **Choices:**   - `"disable"` - `"enable"` |
| **device-type**  string | Device type.  FortiGate - Device type to FortiGate.  FortiManager - Set device type to FortiManager  FortiClient - Set device type to FortiClient  FortiMail - Device type to FortiMail.  FortiWeb - Device type to FortiWeb.  FortiCache - Set device type to FortiCache  FortiSandbox - Set device type to FortiSandbox  FortiDDoS - Set device type to FortiDDoS  FortiAuthenticator - Set device type to FortiAuthenticator  FortiProxy - Set device type to FortiProxy  **Choices:**   - `"FortiGate"` - `"FortiManager"` - `"FortiClient"` - `"FortiMail"` - `"FortiWeb"` - `"FortiCache"` - `"FortiSandbox"` - `"FortiDDoS"` - `"FortiAuthenticator"` - `"FortiProxy"` |
| **id**  integer / required | Add or Edit log index fields. |
| **index-field**  string | Log field name to be indexed. |
| **log-type**  string | Log type.  none - none  app-ctrl  attack  content  dlp  emailfilter  event  generic  history  traffic  virus  voip  webfilter  netscan  fct-event  fct-traffic  fct-netscan  waf  gtp  dns  ssh  ssl  **Choices:**   - `"none"` - `"app-ctrl"` - `"attack"` - `"content"` - `"dlp"` - `"emailfilter"` - `"event"` - `"generic"` - `"history"` - `"traffic"` - `"virus"` - `"voip"` - `"webfilter"` - `"netscan"` - `"fct-event"` - `"fct-traffic"` - `"fct-netscan"` - `"waf"` - `"gtp"` - `"dns"` - `"ssh"` - `"ssl"` - `"file-filter"` - `"asset"` - `"protocol"` - `"siem"` - `"ztna"` - `"security"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_sql_customindex_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_sql_customindex_module.md#id4)

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
   - name: List of SQL index fields.
     fmgr_system_sql_customindex:
        bypass_validation: False
        state: present
        system_sql_customindex:
           case-sensitive: disable
           device-type: FortiGate #<value in [FortiGate, FortiManager, FortiClient, ...]>
           id: 1
           index-field: srcip
           log-type: attack #<value in [none, app-ctrl, attack, ...]>
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
   - name: retrieve all the SQL index fields
     fmgr_fact:
       facts:
           selector: 'system_sql_customindex'
           params:
               custom-index: 'your_value'
```

## [Return Values](fmgr_system_sql_customindex_module.md#id5)

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
