---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_waf_profile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_waf_profile_module.html
fetched_at: 2026-07-27T17:38:44+00:00
---
# fortinet.fortimanager.fmgr_waf_profile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_waf_profile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_waf_profile_module.md#synopsis)
- [Parameters](fmgr_waf_profile_module.md#parameters)
- [Notes](fmgr_waf_profile_module.md#notes)
- [Examples](fmgr_waf_profile_module.md#examples)
- [Return Values](fmgr_waf_profile_module.md#return-values)

## [Synopsis](fmgr_waf_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_waf_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **waf_profile**  dictionary | the top level parameters set |
| **address-list**  dictionary | no description |
| **blocked-address**  string | no description |
| **blocked-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **trusted-address**  string | no description |
| **comment**  string | no description |
| **constraint**  dictionary | no description |
| **content-length**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **length**  integer | no description |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **exception**  list / elements=string | no description |
| **address**  string | no description |
| **content-length**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **header-length**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **hostname**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **id**  integer | no description |
| **line-length**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **malformed**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-cookie**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-header-line**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-range-segment**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-url-param**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **method**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **param-length**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pattern**  string | no description |
| **regex**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **url-param-length**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **version**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **header-length**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **length**  integer | no description |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **hostname**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **line-length**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **length**  integer | no description |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **malformed**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-cookie**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-cookie**  integer | no description |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-header-line**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-header-line**  integer | no description |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-range-segment**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-range-segment**  integer | no description |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-url-param**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-url-param**  integer | no description |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **method**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **param-length**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **length**  integer | no description |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **url-param-length**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **length**  integer | no description |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **version**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **extended-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **external**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **method**  dictionary | no description |
| **default-allowed-methods**  list / elements=string | no description  Choices:   - `"delete"` - `"get"` - `"head"` - `"options"` - `"post"` - `"put"` - `"trace"` - `"others"` - `"connect"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **method-policy**  list / elements=string | no description |
| **address**  string | no description |
| **allowed-methods**  list / elements=string | no description  Choices:   - `"delete"` - `"get"` - `"head"` - `"options"` - `"post"` - `"put"` - `"trace"` - `"others"` - `"connect"` |
| **id**  integer | no description |
| **pattern**  string | no description |
| **regex**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **name**  string | no description |
| **signature**  dictionary | no description |
| **credit-card-detection-threshold**  integer | no description |
| **custom-signature**  list / elements=string | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` - `"erase"` |
| **case-sensitivity**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **direction**  string | no description  Choices:   - `"request"` - `"response"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **name**  string | no description |
| **pattern**  string | no description |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **target**  list / elements=string | no description  Choices:   - `"arg"` - `"arg-name"` - `"req-body"` - `"req-cookie"` - `"req-cookie-name"` - `"req-filename"` - `"req-header"` - `"req-header-name"` - `"req-raw-uri"` - `"req-uri"` - `"resp-body"` - `"resp-hdr"` - `"resp-status"` |
| **disabled-signature**  string | no description |
| **disabled-sub-class**  string | no description |
| **main-class**  dictionary | no description |
| **action**  string | no description  Choices:   - `"allow"` - `"block"` - `"erase"` |
| **id**  integer | no description |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **url-access**  list / elements=string | no description |
| **access-pattern**  list / elements=string | no description |
| **id**  integer | no description |
| **negate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pattern**  string | no description |
| **regex**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **srcaddr**  string | no description |
| **action**  string | no description  Choices:   - `"bypass"` - `"permit"` - `"block"` |
| **address**  string | no description |
| **id**  integer | no description |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **severity**  string | no description  Choices:   - `"low"` - `"medium"` - `"high"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_waf_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_waf_profile_module.md#id4)

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
     fmgr_waf_profile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        waf_profile:
           comment: <value of string>
           extended-log: <value in [disable, enable]>
           external: <value in [disable, enable]>
           name: <value of string>
           url-access:
             -
                 access-pattern:
                   -
                       id: <value of integer>
                       negate: <value in [disable, enable]>
                       pattern: <value of string>
                       regex: <value in [disable, enable]>
                       srcaddr: <value of string>
                 action: <value in [bypass, permit, block]>
                 address: <value of string>
                 id: <value of integer>
                 log: <value in [disable, enable]>
                 severity: <value in [low, medium, high]>
           address-list:
              blocked-address: <value of string>
              blocked-log: <value in [disable, enable]>
              severity: <value in [low, medium, high]>
              status: <value in [disable, enable]>
              trusted-address: <value of string>
           constraint:
              content-length:
                 action: <value in [allow, block]>
                 length: <value of integer>
                 log: <value in [disable, enable]>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
              exception:
                -
                    address: <value of string>
                    content-length: <value in [disable, enable]>
                    header-length: <value in [disable, enable]>
                    hostname: <value in [disable, enable]>
                    id: <value of integer>
                    line-length: <value in [disable, enable]>
                    malformed: <value in [disable, enable]>
                    max-cookie: <value in [disable, enable]>
                    max-header-line: <value in [disable, enable]>
                    max-range-segment: <value in [disable, enable]>
                    max-url-param: <value in [disable, enable]>
                    method: <value in [disable, enable]>
                    param-length: <value in [disable, enable]>
                    pattern: <value of string>
                    regex: <value in [disable, enable]>
                    url-param-length: <value in [disable, enable]>
                    version: <value in [disable, enable]>
              header-length:
                 action: <value in [allow, block]>
                 length: <value of integer>
                 log: <value in [disable, enable]>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
              hostname:
                 action: <value in [allow, block]>
                 log: <value in [disable, enable]>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
              line-length:
                 action: <value in [allow, block]>
                 length: <value of integer>
                 log: <value in [disable, enable]>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
              malformed:
                 action: <value in [allow, block]>
                 log: <value in [disable, enable]>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
              max-cookie:
                 action: <value in [allow, block]>
                 log: <value in [disable, enable]>
                 max-cookie: <value of integer>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
              max-header-line:
                 action: <value in [allow, block]>
                 log: <value in [disable, enable]>
                 max-header-line: <value of integer>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
              max-range-segment:
                 action: <value in [allow, block]>
                 log: <value in [disable, enable]>
                 max-range-segment: <value of integer>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
              max-url-param:
                 action: <value in [allow, block]>
                 log: <value in [disable, enable]>
                 max-url-param: <value of integer>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
              method:
                 action: <value in [allow, block]>
                 log: <value in [disable, enable]>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
              param-length:
                 action: <value in [allow, block]>
                 length: <value of integer>
                 log: <value in [disable, enable]>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
              url-param-length:
                 action: <value in [allow, block]>
                 length: <value of integer>
                 log: <value in [disable, enable]>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
              version:
                 action: <value in [allow, block]>
                 log: <value in [disable, enable]>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
           method:
              default-allowed-methods:
                - delete
                - get
                - head
                - options
                - post
                - put
                - trace
                - others
                - connect
              log: <value in [disable, enable]>
              method-policy:
                -
                    address: <value of string>
                    allowed-methods:
                      - delete
                      - get
                      - head
                      - options
                      - post
                      - put
                      - trace
                      - others
                      - connect
                    id: <value of integer>
                    pattern: <value of string>
                    regex: <value in [disable, enable]>
              severity: <value in [low, medium, high]>
              status: <value in [disable, enable]>
           signature:
              credit-card-detection-threshold: <value of integer>
              custom-signature:
                -
                    action: <value in [allow, block, erase]>
                    case-sensitivity: <value in [disable, enable]>
                    direction: <value in [request, response]>
                    log: <value in [disable, enable]>
                    name: <value of string>
                    pattern: <value of string>
                    severity: <value in [low, medium, high]>
                    status: <value in [disable, enable]>
                    target:
                      - arg
                      - arg-name
                      - req-body
                      - req-cookie
                      - req-cookie-name
                      - req-filename
                      - req-header
                      - req-header-name
                      - req-raw-uri
                      - req-uri
                      - resp-body
                      - resp-hdr
                      - resp-status
              disabled-signature: <value of string>
              disabled-sub-class: <value of string>
              main-class:
                 action: <value in [allow, block, erase]>
                 id: <value of integer>
                 log: <value in [disable, enable]>
                 severity: <value in [low, medium, high]>
                 status: <value in [disable, enable]>
```

## [Return Values](fmgr_waf_profile_module.md#id5)

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
