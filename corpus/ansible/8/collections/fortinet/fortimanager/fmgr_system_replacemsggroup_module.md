---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_replacemsggroup module – Configure replacement message groups."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_replacemsggroup_module.html
fetched_at: 2026-07-28T02:19:41+00:00
---
# fortinet.fortimanager.fmgr_system_replacemsggroup module – Configure replacement message groups.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_replacemsggroup`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **system_replacemsggroup**  dictionary | the top level parameters set |
| **admin**  list / elements=dictionary | Admin. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **alertmail**  list / elements=dictionary | Alertmail. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **id**  integer | no description |
| **msg-type**  string | Message type. |
| **auth**  list / elements=dictionary | Auth. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **automation**  list / elements=dictionary | Automation. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **comment**  string | Comment. |
| **custom-message**  list / elements=dictionary | Custom-Message. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **device-detection-portal**  list / elements=dictionary | Device-Detection-Portal. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **ec**  list / elements=dictionary | no description |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **fortiguard-wf**  list / elements=dictionary | Fortiguard-Wf. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **ftp**  list / elements=dictionary | Ftp. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **group-type**  string | Group type.  **Choices:**   - `"default"` - `"utm"` - `"auth"` - `"ec"` - `"captive-portal"` |
| **http**  list / elements=dictionary | Http. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **icap**  list / elements=dictionary | Icap. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **mail**  list / elements=dictionary | Mail. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **mm1**  list / elements=dictionary | Mm1. |
| **add-smil**  string | add message encapsulation  **Choices:**   - `"disable"` - `"enable"` |
| **charset**  string | character encoding used for replacement message  **Choices:**   - `"us-ascii"` - `"utf-8"` |
| **class**  string | message class  **Choices:**   - `"personal"` - `"advertisement"` - `"information"` - `"automatic"` - `"not-included"` |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **from**  string | from address |
| **from-sender**  string | notification message sent from recipient  **Choices:**   - `"disable"` - `"enable"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **image**  string | Message string. |
| **message**  string | message text |
| **msg-type**  string | Message type. |
| **priority**  string | message priority  **Choices:**   - `"low"` - `"normal"` - `"high"` - `"not-included"` |
| **rsp-status**  string | response status code  **Choices:**   - `"ok"` - `"err-unspecified"` - `"err-srv-denied"` - `"err-msg-fmt-corrupt"` - `"err-snd-addr-unresolv"` - `"err-msg-not-found"` - `"err-net-prob"` - `"err-content-not-accept"` - `"err-unsupp-msg"` |
| **rsp-text**  string | response text |
| **sender-visibility**  string | sender visibility  **Choices:**   - `"hide"` - `"show"` - `"not-specified"` |
| **smil-part**  string | message encapsulation text |
| **subject**  string | subject text string |
| **mm3**  list / elements=dictionary | Mm3. |
| **add-html**  string | add message encapsulation  **Choices:**   - `"disable"` - `"enable"` |
| **charset**  string | character encoding used for replacement message  **Choices:**   - `"us-ascii"` - `"utf-8"` |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **from**  string | from address |
| **from-sender**  string | notification message sent from recipient  **Choices:**   - `"disable"` - `"enable"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **html-part**  string | message encapsulation text |
| **image**  string | Message string. |
| **message**  string | message text |
| **msg-type**  string | Message type. |
| **priority**  string | message priority  **Choices:**   - `"low"` - `"normal"` - `"high"` - `"not-included"` |
| **subject**  string | subject text string |
| **mm4**  list / elements=dictionary | Mm4. |
| **add-smil**  string | add message encapsulation  **Choices:**   - `"disable"` - `"enable"` |
| **charset**  string | character encoding used for replacement message  **Choices:**   - `"us-ascii"` - `"utf-8"` |
| **class**  string | message class  **Choices:**   - `"personal"` - `"advertisement"` - `"informational"` - `"auto"` - `"not-included"` |
| **domain**  string | from address domain |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **from**  string | from address |
| **from-sender**  string | notification message sent from recipient  **Choices:**   - `"disable"` - `"enable"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **image**  string | Message string. |
| **message**  string | message text |
| **msg-type**  string | Message type. |
| **priority**  string | message priority  **Choices:**   - `"low"` - `"normal"` - `"high"` - `"not-included"` |
| **rsp-status**  string | response status  **Choices:**   - `"ok"` - `"err-unspecified"` - `"err-srv-denied"` - `"err-msg-fmt-corrupt"` - `"err-snd-addr-unresolv"` - `"err-net-prob"` - `"err-content-not-accept"` - `"err-unsupp-msg"` |
| **smil-part**  string | message encapsulation text |
| **subject**  string | subject text string |
| **mm7**  list / elements=dictionary | Mm7. |
| **add-smil**  string | add message encapsulation  **Choices:**   - `"disable"` - `"enable"` |
| **addr-type**  string | from address type  **Choices:**   - `"rfc2822-addr"` - `"number"` - `"short-code"` |
| **allow-content-adaptation**  string | allow content adaptations  **Choices:**   - `"disable"` - `"enable"` |
| **charset**  string | character encoding used for replacement message  **Choices:**   - `"us-ascii"` - `"utf-8"` |
| **class**  string | message class  **Choices:**   - `"personal"` - `"advertisement"` - `"informational"` - `"auto"` - `"not-included"` |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **from**  string | from address |
| **from-sender**  string | notification message sent from recipient  **Choices:**   - `"disable"` - `"enable"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **image**  string | Message string. |
| **message**  string | message text |
| **msg-type**  string | Message type. |
| **priority**  string | message priority  **Choices:**   - `"low"` - `"normal"` - `"high"` - `"not-included"` |
| **rsp-status**  string | response status  **Choices:**   - `"success"` - `"partial-success"` - `"client-err"` - `"oper-restrict"` - `"addr-err"` - `"addr-not-found"` - `"content-refused"` - `"msg-id-not-found"` - `"link-id-not-found"` - `"msg-fmt-corrupt"` - `"app-id-not-found"` - `"repl-app-id-not-found"` - `"srv-err"` - `"not-possible"` - `"msg-rejected"` - `"multiple-addr-not-supp"` - `"app-addr-not-supp"` - `"gen-service-err"` - `"improper-ident"` - `"unsupp-ver"` - `"unsupp-oper"` - `"validation-err"` - `"service-err"` - `"service-unavail"` - `"service-denied"` - `"app-denied"` |
| **smil-part**  string | message encapsulation text |
| **subject**  string | subject text string |
| **mms**  list / elements=dictionary | Mms. |
| **buffer**  string | Message string. |
| **charset**  string | character encoding used for replacement message  **Choices:**   - `"us-ascii"` - `"utf-8"` |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **image**  string | Message string. |
| **msg-type**  string | Message type. |
| **nac-quar**  list / elements=dictionary | Nac-Quar. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **id**  integer | no description |
| **msg-type**  string | Message type. |
| **name**  string / required | Group name. |
| **nntp**  list / elements=dictionary | Nntp. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **spam**  list / elements=dictionary | Spam. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **sslvpn**  list / elements=dictionary | Sslvpn. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **traffic-quota**  list / elements=dictionary | Traffic-Quota. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **utm**  list / elements=dictionary | Utm. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **webproxy**  list / elements=dictionary | Webproxy. |
| **buffer**  string | Message string. |
| **format**  string | Format flag.  **Choices:**   - `"none"` - `"text"` - `"html"` - `"wml"` |
| **header**  string | Header flag.  **Choices:**   - `"none"` - `"http"` - `"8bit"` |
| **msg-type**  string | Message type. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_replacemsggroup_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_replacemsggroup_module.md#id4)

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
   - name: retrieve all the replacement message groups
     fmgr_fact:
       facts:
           selector: 'system_replacemsggroup'
           params:
               adom: 'ansible'
               replacemsg-group: 'your_value'
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
```

## [Return Values](fmgr_system_replacemsggroup_module.md#id5)

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
