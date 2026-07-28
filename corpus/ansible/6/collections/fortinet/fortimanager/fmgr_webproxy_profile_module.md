---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_webproxy_profile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_webproxy_profile_module.html
fetched_at: 2026-07-27T17:39:37+00:00
---
# fortinet.fortimanager.fmgr_webproxy_profile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_webproxy_profile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_webproxy_profile_module.md#synopsis)
- [Parameters](fmgr_webproxy_profile_module.md#parameters)
- [Notes](fmgr_webproxy_profile_module.md#notes)
- [Examples](fmgr_webproxy_profile_module.md#examples)
- [Return Values](fmgr_webproxy_profile_module.md#return-values)

## [Synopsis](fmgr_webproxy_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_webproxy_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **webproxy_profile**  dictionary | the top level parameters set |
| **header-client-ip**  string | no description  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header-front-end-https**  string | no description  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header-via-request**  string | no description  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header-via-response**  string | no description  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header-x-authenticated-groups**  string | no description  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header-x-authenticated-user**  string | no description  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header-x-forwarded-client-cert**  string | no description  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **header-x-forwarded-for**  string | no description  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **headers**  list / elements=string | no description |
| **action**  string | no description  Choices:   - `"add-to-request"` - `"add-to-response"` - `"remove-from-request"` - `"remove-from-response"` |
| **add-option**  string | no description  Choices:   - `"append"` - `"new-on-not-found"` - `"new"` |
| **base64-encoding**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **content**  string | no description |
| **dstaddr**  string | no description |
| **dstaddr6**  string | no description |
| **id**  integer | no description |
| **name**  string | no description |
| **protocol**  list / elements=string | no description  Choices:   - `"https"` - `"http"` |
| **log-header-change**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **name**  string | no description |
| **strip-encoding**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_webproxy_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_webproxy_profile_module.md#id4)

```yaml+jinja
- hosts: fortimanager-inventory
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: no description
     fmgr_webproxy_profile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        webproxy_profile:
           header-client-ip: <value in [pass, add, remove]>
           header-front-end-https: <value in [pass, add, remove]>
           header-via-request: <value in [pass, add, remove]>
           header-via-response: <value in [pass, add, remove]>
           header-x-authenticated-groups: <value in [pass, add, remove]>
           header-x-authenticated-user: <value in [pass, add, remove]>
           header-x-forwarded-for: <value in [pass, add, remove]>
           headers:
             -
                 action: <value in [add-to-request, add-to-response, remove-from-request, ...]>
                 content: <value of string>
                 id: <value of integer>
                 name: <value of string>
                 add-option: <value in [append, new-on-not-found, new]>
                 base64-encoding: <value in [disable, enable]>
                 dstaddr: <value of string>
                 dstaddr6: <value of string>
                 protocol:
                   - https
                   - http
           log-header-change: <value in [disable, enable]>
           name: <value of string>
           strip-encoding: <value in [disable, enable]>
           header-x-forwarded-client-cert: <value in [pass, add, remove]>
```

## [Return Values](fmgr_webproxy_profile_module.md#id5)

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
