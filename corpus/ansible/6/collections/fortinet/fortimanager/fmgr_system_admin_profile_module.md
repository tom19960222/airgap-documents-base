---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_admin_profile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_admin_profile_module.html
fetched_at: 2026-07-27T17:35:33+00:00
---
# fortinet.fortimanager.fmgr_system_admin_profile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_admin_profile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_admin_profile_module.md#synopsis)
- [Parameters](fmgr_system_admin_profile_module.md#parameters)
- [Notes](fmgr_system_admin_profile_module.md#notes)
- [Examples](fmgr_system_admin_profile_module.md#examples)
- [Return Values](fmgr_system_admin_profile_module.md#return-values)

## [Synopsis](fmgr_system_admin_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_admin_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_admin_profile**  dictionary | the top level parameters set |
| **adom-lock**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **adom-policy-packages**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **adom-switch**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **allow-to-install**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **app-filter**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **assignment**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **change-password**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **config-retrieve**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **config-revert**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **consistency-check**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **datamask**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **datamask-custom-fields**  list / elements=string | no description |
| **field-category**  list / elements=string | no description  Choices:   - `"log"` - `"fortiview"` - `"alert"` - `"ueba"` - `"all"` |
| **field-name**  string | no description |
| **field-status**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **field-type**  string | no description  no description  no description  no description  no description  no description  Choices:   - `"string"` ← (default) - `"ip"` - `"mac"` - `"email"` - `"unknown"` |
| **datamask-custom-priority**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **datamask-fields**  list / elements=string | no description  Choices:   - `"user"` - `"srcip"` - `"srcname"` - `"srcmac"` - `"dstip"` - `"dstname"` - `"email"` - `"message"` - `"domain"` |
| **datamask-key**  string | no description |
| **datamask-unmasked-time**  integer | no description  Default: `0` |
| **deploy-management**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **description**  string | no description |
| **device-ap**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **device-config**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **device-forticlient**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **device-fortiswitch**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **device-manager**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **device-op**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **device-policy-package-lock**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **device-profile**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **device-revision-deletion**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **device-wan-link-load-balance**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **event-management**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **extension-access**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **fabric-viewer**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **fgd-center-advanced**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **fgd-center-fmw-mgmt**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **fgd-center-licensing**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **fgd_center**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **global-policy-packages**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **import-policy-packages**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **intf-mapping**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **ips-filter**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **ips-objects**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
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
| **log-viewer**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **policy-objects**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **profileid**  string | no description |
| **read-passwd**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **realtime-monitor**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **report-viewer**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **rpc-permit**  string | no description  no description  no description  no description  Choices:   - `"read-write"` - `"none"` ← (default) - `"read"` |
| **run-report**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **scope**  string | no description  no description  no description  Choices:   - `"global"` ← (default) - `"adom"` |
| **script-access**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **set-install-targets**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **super-user-profile**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **system-setting**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **term-access**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **triage-events**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
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
| **type**  string | no description  no description  no description  Choices:   - `"system"` ← (default) - `"restricted"` |
| **update-incidents**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **vpn-manager**  string | no description  no description  no description  no description  Choices:   - `"none"` ← (default) - `"read"` - `"read-write"` |
| **web-filter**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_system_admin_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_admin_profile_module.md#id4)

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
   - name: retrieve all the admin profiles
     fmgr_fact:
       facts:
           selector: 'system_admin_profile'
           params:
               profile: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Admin profile.
     fmgr_system_admin_profile:
        bypass_validation: False
        state: present
        system_admin_profile:
           description: ansible-test-description
           profileid: ansible-test-profile
           scope: adom #<value in [global, adom]>
           type: system #<value in [system, restricted]>
```

## [Return Values](fmgr_system_admin_profile_module.md#id5)

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
