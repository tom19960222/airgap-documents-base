---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_webfilter_profile_ftgdwf module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_webfilter_profile_ftgdwf_module.html
fetched_at: 2026-07-27T17:39:29+00:00
---
# fortinet.fortimanager.fmgr_webfilter_profile_ftgdwf module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_webfilter_profile_ftgdwf`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_webfilter_profile_ftgdwf_module.md#synopsis)
- [Parameters](fmgr_webfilter_profile_ftgdwf_module.md#parameters)
- [Notes](fmgr_webfilter_profile_ftgdwf_module.md#notes)
- [Examples](fmgr_webfilter_profile_ftgdwf_module.md#examples)
- [Return Values](fmgr_webfilter_profile_ftgdwf_module.md#return-values)

## [Synopsis](fmgr_webfilter_profile_ftgdwf_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_webfilter_profile_ftgdwf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **profile**  string / required | the parameter (profile) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **webfilter_profile_ftgdwf**  dictionary | the top level parameters set |
| **exempt-quota**  string | no description |
| **filters**  list / elements=string | description |
| **action**  string | no description  Choices:   - `"block"` - `"monitor"` - `"warning"` - `"authenticate"` |
| **auth-usr-grp**  string | no description |
| **category**  string | no description |
| **id**  integer | no description |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **override-replacemsg**  string | no description |
| **warn-duration**  string | no description |
| **warning-duration-type**  string | no description  Choices:   - `"session"` - `"timeout"` |
| **warning-prompt**  string | no description  Choices:   - `"per-domain"` - `"per-category"` |
| **max-quota-timeout**  integer | no description |
| **options**  list / elements=string | description  Choices:   - `"error-allow"` - `"http-err-detail"` - `"rate-image-urls"` - `"strict-blocking"` - `"rate-server-ip"` - `"redir-block"` - `"connect-request-bypass"` - `"log-all-url"` - `"ftgd-disable"` |
| **ovrd**  string | no description |
| **quota**  list / elements=string | description |
| **category**  string | no description |
| **duration**  string | no description |
| **id**  integer | no description |
| **override-replacemsg**  string | no description |
| **type**  string | no description  Choices:   - `"time"` - `"traffic"` |
| **unit**  string | no description  Choices:   - `"B"` - `"KB"` - `"MB"` - `"GB"` |
| **value**  integer | no description |
| **rate-crl-urls**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **rate-css-urls**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **rate-image-urls**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **rate-javascript-urls**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_webfilter_profile_ftgdwf_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_webfilter_profile_ftgdwf_module.md#id4)

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
     fmgr_webfilter_profile_ftgdwf:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        profile: <your own value>
        webfilter_profile_ftgdwf:
           exempt-quota: <value of string>
           filters:
             -
                 action: <value in [block, monitor, warning, ...]>
                 auth-usr-grp: <value of string>
                 category: <value of string>
                 id: <value of integer>
                 log: <value in [disable, enable]>
                 override-replacemsg: <value of string>
                 warn-duration: <value of string>
                 warning-duration-type: <value in [session, timeout]>
                 warning-prompt: <value in [per-domain, per-category]>
           max-quota-timeout: <value of integer>
           options:
             - error-allow
             - http-err-detail
             - rate-image-urls
             - strict-blocking
             - rate-server-ip
             - redir-block
             - connect-request-bypass
             - log-all-url
             - ftgd-disable
           ovrd: <value of string>
           quota:
             -
                 category: <value of string>
                 duration: <value of string>
                 id: <value of integer>
                 override-replacemsg: <value of string>
                 type: <value in [time, traffic]>
                 unit: <value in [B, KB, MB, ...]>
                 value: <value of integer>
           rate-crl-urls: <value in [disable, enable]>
           rate-css-urls: <value in [disable, enable]>
           rate-image-urls: <value in [disable, enable]>
           rate-javascript-urls: <value in [disable, enable]>
```

## [Return Values](fmgr_webfilter_profile_ftgdwf_module.md#id5)

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
