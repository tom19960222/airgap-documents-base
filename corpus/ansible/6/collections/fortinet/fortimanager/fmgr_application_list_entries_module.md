---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_application_list_entries module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_application_list_entries_module.html
fetched_at: 2026-07-27T17:28:32+00:00
---
# fortinet.fortimanager.fmgr_application_list_entries module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_application_list_entries`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_application_list_entries_module.md#synopsis)
- [Parameters](fmgr_application_list_entries_module.md#parameters)
- [Notes](fmgr_application_list_entries_module.md#notes)
- [Examples](fmgr_application_list_entries_module.md#examples)
- [Return Values](fmgr_application_list_entries_module.md#return-values)

## [Synopsis](fmgr_application_list_entries_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_application_list_entries_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **application_list_entries**  dictionary | the top level parameters set |
| **action**  string | no description  Choices:   - `"pass"` - `"block"` - `"reset"` |
| **application**  integer | description |
| **behavior**  string | description |
| **category**  string | no description |
| **exclusion**  integer | description |
| **id**  integer | no description |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **log-packet**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **parameters**  list / elements=string | description |
| **id**  integer | no description |
| **members**  list / elements=string | description |
| **id**  integer | no description |
| **name**  string | no description |
| **value**  string | no description |
| **value**  string | no description |
| **per-ip-shaper**  string | no description |
| **popularity**  list / elements=string | description  Choices:   - `1` - `2` - `3` - `4` - `5` |
| **protocols**  string | description |
| **quarantine**  string | no description  Choices:   - `"none"` - `"attacker"` |
| **quarantine-expiry**  string | no description |
| **quarantine-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **rate-count**  integer | no description |
| **rate-duration**  integer | no description |
| **rate-mode**  string | no description  Choices:   - `"periodical"` - `"continuous"` |
| **rate-track**  string | no description  Choices:   - `"none"` - `"src-ip"` - `"dest-ip"` - `"dhcp-client-mac"` - `"dns-domain"` |
| **risk**  integer | description |
| **session-ttl**  integer | no description |
| **shaper**  string | no description |
| **shaper-reverse**  string | no description |
| **sub-category**  integer | description |
| **technology**  string | description |
| **vendor**  string | description |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **list**  string / required | the parameter (list) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_application_list_entries_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_application_list_entries_module.md#id4)

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
   - name: Application list entries.
     fmgr_application_list_entries:
        adom: ansible
        list: 'ansible-test' # name
        state: present
        application_list_entries:
           action: pass
           behavior: 'all'
           category: '2'
           id: 1
           log: enable
           log-packet: enable
           protocols: 'all'

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
   - name: retrieve all the entries in application list
     fmgr_fact:
       facts:
           selector: 'application_list_entries'
           params:
               adom: 'ansible'
               list: 'ansible-test' # name
               entries: 'your_value'
```

## [Return Values](fmgr_application_list_entries_module.md#id5)

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
