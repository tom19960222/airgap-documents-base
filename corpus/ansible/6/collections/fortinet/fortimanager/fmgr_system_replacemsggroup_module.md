---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_replacemsggroup module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_replacemsggroup_module.html
fetched_at: 2026-07-27T17:36:52+00:00
---
# fortinet.fortimanager.fmgr_system_replacemsggroup module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_replacemsggroup`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_replacemsggroup_module.md#synopsis)
- [Parameters](fmgr_system_replacemsggroup_module.md#parameters)
- [Notes](fmgr_system_replacemsggroup_module.md#notes)
- [Examples](fmgr_system_replacemsggroup_module.md#examples)
- [Return Values](fmgr_system_replacemsggroup_module.md#return-values)

## [Synopsis](fmgr_system_replacemsggroup_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_replacemsggroup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_replacemsggroup**  dictionary | the top level parameters set |
| **admin**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **alertmail**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **auth**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **automation**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **comment**  string | no description |
| **custom-message**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **device-detection-portal**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **ec**  list / elements=string | description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **fortiguard-wf**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **ftp**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **group-type**  string | no description  Choices:   - `"default"` - `"utm"` - `"auth"` - `"ec"` - `"captive-portal"` |
| **http**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **icap**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **mail**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **mm1**  list / elements=string | no description |
| **add-smil**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **charset**  string | no description  Choices:   - `"us-ascii"` - `"utf-8"` |
| **class**  string | no description  Choices:   - `"personal"` - `"advertisement"` - `"information"` - `"automatic"` - `"not-included"` |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **from**  string | no description |
| **from-sender**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **image**  string | no description |
| **message**  string | no description |
| **msg-type**  string | no description |
| **priority**  string | no description  Choices:   - `"low"` - `"normal"` - `"high"` - `"not-included"` |
| **rsp-status**  string | no description  Choices:   - `"ok"` - `"err-unspecified"` - `"err-srv-denied"` - `"err-msg-fmt-corrupt"` - `"err-snd-addr-unresolv"` - `"err-msg-not-found"` - `"err-net-prob"` - `"err-content-not-accept"` - `"err-unsupp-msg"` |
| **rsp-text**  string | no description |
| **sender-visibility**  string | no description  Choices:   - `"hide"` - `"show"` - `"not-specified"` |
| **smil-part**  string | no description |
| **subject**  string | no description |
| **mm3**  list / elements=string | no description |
| **add-html**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **charset**  string | no description  Choices:   - `"us-ascii"` - `"utf-8"` |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **from**  string | no description |
| **from-sender**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **html-part**  string | no description |
| **image**  string | no description |
| **message**  string | no description |
| **msg-type**  string | no description |
| **priority**  string | no description  Choices:   - `"low"` - `"normal"` - `"high"` - `"not-included"` |
| **subject**  string | no description |
| **mm4**  list / elements=string | no description |
| **add-smil**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **charset**  string | no description  Choices:   - `"us-ascii"` - `"utf-8"` |
| **class**  string | no description  Choices:   - `"personal"` - `"advertisement"` - `"informational"` - `"auto"` - `"not-included"` |
| **domain**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **from**  string | no description |
| **from-sender**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **image**  string | no description |
| **message**  string | no description |
| **msg-type**  string | no description |
| **priority**  string | no description  Choices:   - `"low"` - `"normal"` - `"high"` - `"not-included"` |
| **rsp-status**  string | no description  Choices:   - `"ok"` - `"err-unspecified"` - `"err-srv-denied"` - `"err-msg-fmt-corrupt"` - `"err-snd-addr-unresolv"` - `"err-net-prob"` - `"err-content-not-accept"` - `"err-unsupp-msg"` |
| **smil-part**  string | no description |
| **subject**  string | no description |
| **mm7**  list / elements=string | no description |
| **add-smil**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **addr-type**  string | no description  Choices:   - `"rfc2822-addr"` - `"number"` - `"short-code"` |
| **allow-content-adaptation**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **charset**  string | no description  Choices:   - `"us-ascii"` - `"utf-8"` |
| **class**  string | no description  Choices:   - `"personal"` - `"advertisement"` - `"informational"` - `"auto"` - `"not-included"` |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **from**  string | no description |
| **from-sender**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **image**  string | no description |
| **message**  string | no description |
| **msg-type**  string | no description |
| **priority**  string | no description  Choices:   - `"low"` - `"normal"` - `"high"` - `"not-included"` |
| **rsp-status**  string | no description  Choices:   - `"success"` - `"partial-success"` - `"client-err"` - `"oper-restrict"` - `"addr-err"` - `"addr-not-found"` - `"content-refused"` - `"msg-id-not-found"` - `"link-id-not-found"` - `"msg-fmt-corrupt"` - `"app-id-not-found"` - `"repl-app-id-not-found"` - `"srv-err"` - `"not-possible"` - `"msg-rejected"` - `"multiple-addr-not-supp"` - `"app-addr-not-supp"` - `"gen-service-err"` - `"improper-ident"` - `"unsupp-ver"` - `"unsupp-oper"` - `"validation-err"` - `"service-err"` - `"service-unavail"` - `"service-denied"` - `"app-denied"` |
| **smil-part**  string | no description |
| **subject**  string | no description |
| **mms**  list / elements=string | no description |
| **buffer**  string | no description |
| **charset**  string | no description  Choices:   - `"us-ascii"` - `"utf-8"` |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **image**  string | no description |
| **msg-type**  string | no description |
| **nac-quar**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **name**  string | no description |
| **nntp**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **spam**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **sslvpn**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **traffic-quota**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **utm**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **webproxy**  list / elements=string | no description |
| **buffer**  string | no description |
| **format**  string | no description  Choices:   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | no description  Choices:   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | no description |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_system_replacemsggroup_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_replacemsggroup_module.md#id4)

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
   - name: Configure replacement message groups.
     fmgr_system_replacemsggroup:
        bypass_validation: False
        adom: ansible
        state: present
        system_replacemsggroup:
           comment: ansible-comment
           name: ansible-test

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
   - name: retrieve all the replacement message groups
     fmgr_fact:
       facts:
           selector: 'system_replacemsggroup'
           params:
               adom: 'ansible'
               replacemsg-group: 'your_value'
```

## [Return Values](fmgr_system_replacemsggroup_module.md#id5)

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
