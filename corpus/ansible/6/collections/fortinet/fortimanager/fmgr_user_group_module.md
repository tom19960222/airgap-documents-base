---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_user_group module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_user_group_module.html
fetched_at: 2026-07-27T17:37:52+00:00
---
# fortinet.fortimanager.fmgr_user_group module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_user_group`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_user_group_module.md#synopsis)
- [Parameters](fmgr_user_group_module.md#parameters)
- [Notes](fmgr_user_group_module.md#notes)
- [Examples](fmgr_user_group_module.md#examples)
- [Return Values](fmgr_user_group_module.md#return-values)

## [Synopsis](fmgr_user_group_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_user_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **user_group**  dictionary | the top level parameters set |
| **auth-concurrent-override**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auth-concurrent-value**  integer | no description |
| **authtimeout**  integer | no description |
| **company**  string | no description  Choices:   - `"optional"` - `"mandatory"` - `"disabled"` |
| **dynamic_mapping**  list / elements=string | description |
| **_scope**  list / elements=string | description |
| **name**  string | no description |
| **vdom**  string | no description |
| **auth-concurrent-override**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auth-concurrent-value**  integer | no description |
| **authtimeout**  integer | no description |
| **company**  string | no description  Choices:   - `"optional"` - `"mandatory"` - `"disabled"` |
| **email**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **expire**  integer | no description |
| **expire-type**  string | no description  Choices:   - `"immediately"` - `"first-successful-login"` |
| **group-type**  string | no description  Choices:   - `"firewall"` - `"directory-service"` - `"fsso-service"` - `"guest"` - `"rsso"` |
| **guest**  list / elements=string | description |
| **comment**  string | no description |
| **company**  string | no description |
| **email**  string | no description |
| **expiration**  string | no description |
| **group**  string | no description |
| **id**  integer | no description |
| **mobile-phone**  string | no description |
| **name**  string | no description |
| **password**  string | description |
| **sponsor**  string | no description |
| **user-id**  string | no description |
| **http-digest-realm**  string | no description |
| **id**  integer | no description |
| **ldap-memberof**  string | no description |
| **logic-type**  string | no description  Choices:   - `"or"` - `"and"` |
| **match**  list / elements=string | description |
| **_gui_meta**  string | no description |
| **group-name**  string | no description |
| **id**  integer | no description |
| **server-name**  string | no description |
| **max-accounts**  integer | no description |
| **member**  string | description |
| **mobile-phone**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **multiple-guest-add**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **password**  string | no description  Choices:   - `"auto-generate"` - `"specify"` - `"disable"` |
| **redir-url**  string | no description |
| **sms-custom-server**  string | no description |
| **sms-server**  string | no description  Choices:   - `"fortiguard"` - `"custom"` |
| **sponsor**  string | no description  Choices:   - `"optional"` - `"mandatory"` - `"disabled"` |
| **sslvpn-bookmarks-group**  string | description |
| **sslvpn-cache-cleaner**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sslvpn-client-check**  list / elements=string | description  Choices:   - `"forticlient"` - `"forticlient-av"` - `"forticlient-fw"` - `"3rdAV"` - `"3rdFW"` |
| **sslvpn-ftp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sslvpn-http**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sslvpn-os-check**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sslvpn-os-check-list**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"check-up-to-date"` - `"deny"` |
| **latest-patch-level**  string | no description |
| **name**  string | no description |
| **tolerance**  integer | no description |
| **sslvpn-portal**  string | description |
| **sslvpn-portal-heading**  string | no description |
| **sslvpn-rdp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sslvpn-samba**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sslvpn-split-tunneling**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sslvpn-ssh**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sslvpn-telnet**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sslvpn-tunnel**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sslvpn-tunnel-endip**  string | no description |
| **sslvpn-tunnel-ip-mode**  string | no description  Choices:   - `"range"` - `"usrgrp"` |
| **sslvpn-tunnel-startip**  string | no description |
| **sslvpn-virtual-desktop**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sslvpn-vnc**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sslvpn-webapp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sso-attribute-value**  string | no description |
| **user-id**  string | no description  Choices:   - `"email"` - `"auto-generate"` - `"specify"` |
| **user-name**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **email**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **expire**  integer | no description |
| **expire-type**  string | no description  Choices:   - `"immediately"` - `"first-successful-login"` |
| **group-type**  string | no description  Choices:   - `"firewall"` - `"directory-service"` - `"fsso-service"` - `"guest"` - `"rsso"` |
| **guest**  list / elements=string | no description |
| **comment**  string | no description |
| **company**  string | no description |
| **email**  string | no description |
| **expiration**  string | no description |
| **id**  integer | no description |
| **mobile-phone**  string | no description |
| **name**  string | no description |
| **password**  string | no description |
| **sponsor**  string | no description |
| **user-id**  string | no description |
| **http-digest-realm**  string | no description |
| **id**  integer | no description |
| **match**  list / elements=string | no description |
| **_gui_meta**  string | no description |
| **group-name**  string | no description |
| **id**  integer | no description |
| **server-name**  string | no description |
| **max-accounts**  integer | no description |
| **member**  list / elements=string | no description |
| **mobile-phone**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **multiple-guest-add**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **name**  string | no description |
| **password**  string | no description  Choices:   - `"auto-generate"` - `"specify"` - `"disable"` |
| **sms-custom-server**  string | no description |
| **sms-server**  string | no description  Choices:   - `"fortiguard"` - `"custom"` |
| **sponsor**  string | no description  Choices:   - `"optional"` - `"mandatory"` - `"disabled"` |
| **sso-attribute-value**  string | no description |
| **user-id**  string | no description  Choices:   - `"email"` - `"auto-generate"` - `"specify"` |
| **user-name**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_user_group_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_user_group_module.md#id4)

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
   - name: retrieve all the user groups
     fmgr_fact:
       facts:
           selector: 'user_group'
           params:
               adom: 'ansible'
               group: 'your_value'

- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure user groups.
     fmgr_user_group:
        bypass_validation: False
        adom: FortiCarrier
        state: present
        user_group:
           id: 1
           name: ansible-test-group
           password: specify #<value in [auto-generate, specify, disable]>
           user-id: email #<value in [email, auto-generate, specify]>
```

## [Return Values](fmgr_user_group_module.md#id5)

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
