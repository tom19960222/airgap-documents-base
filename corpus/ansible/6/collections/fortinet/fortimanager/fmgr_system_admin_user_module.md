---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_admin_user module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_admin_user_module.html
fetched_at: 2026-07-27T17:35:37+00:00
---
# fortinet.fortimanager.fmgr_system_admin_user module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_admin_user`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_admin_user_module.md#synopsis)
- [Parameters](fmgr_system_admin_user_module.md#parameters)
- [Notes](fmgr_system_admin_user_module.md#notes)
- [Examples](fmgr_system_admin_user_module.md#examples)
- [Return Values](fmgr_system_admin_user_module.md#return-values)

## [Synopsis](fmgr_system_admin_user_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_admin_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_admin_user**  dictionary | the top level parameters set |
| **adom**  list / elements=string | no description |
| **adom-name**  string | no description |
| **adom-access**  string | no description  no description  no description  no description  Choices:   - `"all"` - `"specify"` ← (default) - `"exclude"` |
| **adom-exclude**  list / elements=string | no description |
| **adom-name**  string | no description |
| **app-filter**  list / elements=string | no description |
| **app-filter-name**  string | no description |
| **avatar**  string | no description |
| **ca**  string | no description |
| **change-password**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **dashboard**  list / elements=string | no description |
| **column**  integer | no description  Default: `0` |
| **diskio-content-type**  string | no description  no description  no description  no description  Choices:   - `"util"` ← (default) - `"iops"` - `"blks"` |
| **diskio-period**  string | no description  no description  no description  no description  Choices:   - `"1hour"` ← (default) - `"8hour"` - `"24hour"` |
| **log-rate-period**  string | no description  no description  no description  no description  Choices:   - `"2min "` - `"1hour"` - `"6hours"` |
| **log-rate-topn**  string | no description  no description  no description  no description  no description  no description  Choices:   - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` ← (default) |
| **log-rate-type**  string | no description  no description  no description  Choices:   - `"log"` - `"device"` ← (default) |
| **moduleid**  integer | no description  Default: `0` |
| **name**  string | no description |
| **num-entries**  integer | no description  Default: `10` |
| **refresh-interval**  integer | no description  Default: `300` |
| **res-cpu-display**  string | no description  no description  no description  Choices:   - `"average "` - `"each"`   Default: `"average"` |
| **res-period**  string | no description  no description  no description  no description  Choices:   - `"10min "` - `"hour"` - `"day"`   Default: `"10min"` |
| **res-view-type**  string | no description  no description  no description  Choices:   - `"real-time "` - `"history"` ← (default) |
| **status**  string | no description  no description  no description  Choices:   - `"close"` - `"open"` ← (default) |
| **tabid**  integer | no description  Default: `0` |
| **time-period**  string | no description  no description  no description  no description  Choices:   - `"1hour"` ← (default) - `"8hour"` - `"24hour"` |
| **widget-type**  string | no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  Choices:   - `"top-lograte"` - `"sysres"` - `"sysinfo"` - `"licinfo"` - `"jsconsole"` - `"sysop"` - `"alert"` - `"statistics"` - `"rpteng"` - `"raid"` - `"logrecv"` - `"devsummary"` - `"logdb-perf"` - `"logdb-lag"` - `"disk-io"` - `"log-rcvd-fwd"` |
| **dashboard-tabs**  list / elements=string | no description |
| **name**  string | no description |
| **tabid**  integer | no description  Default: `0` |
| **description**  string | no description |
| **dev-group**  string | no description |
| **email-address**  string | no description |
| **ext-auth-accprofile-override**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **ext-auth-adom-override**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **ext-auth-group-match**  string | no description |
| **fingerprint**  string | no description |
| **first-name**  string | no description |
| **force-password-change**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **group**  string | no description |
| **hidden**  integer | no description  Default: `0` |
| **ips-filter**  list / elements=string | no description |
| **ips-filter-name**  string | no description |
| **ipv6_trusthost1**  string | no description  Default: `"no description"` |
| **ipv6_trusthost10**  string | no description  Default: `"ffff"` |
| **ipv6_trusthost2**  string | no description  Default: `"ffff"` |
| **ipv6_trusthost3**  string | no description  Default: `"ffff"` |
| **ipv6_trusthost4**  string | no description  Default: `"ffff"` |
| **ipv6_trusthost5**  string | no description  Default: `"ffff"` |
| **ipv6_trusthost6**  string | no description  Default: `"ffff"` |
| **ipv6_trusthost7**  string | no description  Default: `"ffff"` |
| **ipv6_trusthost8**  string | no description  Default: `"ffff"` |
| **ipv6_trusthost9**  string | no description  Default: `"ffff"` |
| **last-name**  string | no description |
| **ldap-server**  string | no description |
| **login-max**  integer | no description  Default: `32` |
| **meta-data**  list / elements=string | no description |
| **fieldlength**  integer | no description  Default: `0` |
| **fieldname**  string | no description |
| **fieldvalue**  string | no description |
| **importance**  string | no description  no description  no description  Choices:   - `"optional"` ← (default) - `"required"` |
| **status**  string | no description  no description  no description  Choices:   - `"disabled"` - `"enabled"` ← (default) |
| **mobile-number**  string | no description |
| **pager-number**  string | no description |
| **password**  string | no description |
| **password-expire**  string | no description |
| **phone-number**  string | no description |
| **policy-package**  list / elements=string | no description |
| **policy-package-name**  string | no description |
| **profileid**  string | no description  Default: `"Restricted_User"` |
| **radius_server**  string | no description |
| **restrict-access**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **restrict-dev-vdom**  list / elements=string | description |
| **dev-vdom**  string | no description |
| **rpc-permit**  string | no description  no description  no description  no description  Choices:   - `"read-write"` - `"none"` ← (default) - `"read"` - `"from-profile"` |
| **ssh-public-key1**  string | no description |
| **ssh-public-key2**  string | no description |
| **ssh-public-key3**  string | no description |
| **subject**  string | no description |
| **tacacs-plus-server**  string | no description |
| **th-from-profile**  integer | no description  Default: `0` |
| **th6-from-profile**  integer | no description  Default: `0` |
| **trusthost1**  string | no description  Default: `"0."` |
| **trusthost10**  string | no description  Default: `"255."` |
| **trusthost2**  string | no description  Default: `"255."` |
| **trusthost3**  string | no description  Default: `"255."` |
| **trusthost4**  string | no description  Default: `"255."` |
| **trusthost5**  string | no description  Default: `"255."` |
| **trusthost6**  string | no description  Default: `"255."` |
| **trusthost7**  string | no description  Default: `"255."` |
| **trusthost8**  string | no description  Default: `"255."` |
| **trusthost9**  string | no description  Default: `"255."` |
| **two-factor-auth**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **use-global-theme**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **user-theme**  string | no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  Choices:   - `"blue"` ← (default) - `"green"` - `"red"` - `"melongene"` - `"spring"` - `"summer"` - `"autumn"` - `"winter"` - `"circuit-board"` - `"calla-lily"` - `"binary-tunnel"` - `"mars"` - `"blue-sea"` - `"technology"` - `"landscape"` - `"twilight"` - `"canyon"` - `"northern-light"` - `"astronomy"` - `"fish"` - `"penguin"` - `"mountain"` - `"panda"` - `"parrot"` - `"cave"` - `"zebra"` - `"contrast-dark"` |
| **user_type**  string | no description  no description  no description  no description  no description  no description  no description  Choices:   - `"local"` ← (default) - `"radius"` - `"ldap"` - `"tacacs-plus"` - `"pki-auth"` - `"group"` - `"sso"` |
| **userid**  string | no description |
| **web-filter**  list / elements=string | no description |
| **web-filter-name**  string | no description |
| **wildcard**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_system_admin_user_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_admin_user_module.md#id4)

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
   - name: Admin User
     fmgr_system_admin_user:
        state: present
        system_admin_user:
            adom:
             - adom-name: ansible
            userid: 'ansible-test'
   - name: Admin domain.
     fmgr_system_admin_user_adom:
        bypass_validation: False
        user: ansible-test # userid
        state: present
        system_admin_user_adom:
           adom-name: 'ALL ADOMS'
```

## [Return Values](fmgr_system_admin_user_module.md#id5)

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
