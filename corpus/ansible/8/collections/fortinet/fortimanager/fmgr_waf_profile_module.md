---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_waf_profile module – Web application firewall configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_waf_profile_module.html
fetched_at: 2026-07-28T02:22:00+00:00
---
# fortinet.fortimanager.fmgr_waf_profile module – Web application firewall configuration.

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **waf_profile**  dictionary | the top level parameters set |
| **address-list**  dictionary | no description |
| **blocked-address**  any | (list or str) Blocked address. |
| **blocked-log**  string | Enable/disable logging on blocked addresses.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Status.  **Choices:**   - `"disable"` - `"enable"` |
| **trusted-address**  any | (list or str) Trusted address. |
| **comment**  string | Comment. |
| **constraint**  dictionary | no description |
| **content-length**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **length**  integer | Length of HTTP content in bytes |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **exception**  list / elements=dictionary | Exception. |
| **address**  string | Host address. |
| **content-length**  string | HTTP content length in request.  **Choices:**   - `"disable"` - `"enable"` |
| **header-length**  string | HTTP header length in request.  **Choices:**   - `"disable"` - `"enable"` |
| **hostname**  string | Enable/disable hostname check.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer | Exception ID. |
| **line-length**  string | HTTP line length in request.  **Choices:**   - `"disable"` - `"enable"` |
| **malformed**  string | Enable/disable malformed HTTP request check.  **Choices:**   - `"disable"` - `"enable"` |
| **max-cookie**  string | Maximum number of cookies in HTTP request.  **Choices:**   - `"disable"` - `"enable"` |
| **max-header-line**  string | Maximum number of HTTP header line.  **Choices:**   - `"disable"` - `"enable"` |
| **max-range-segment**  string | Maximum number of range segments in HTTP range line.  **Choices:**   - `"disable"` - `"enable"` |
| **max-url-param**  string | Maximum number of parameters in URL.  **Choices:**   - `"disable"` - `"enable"` |
| **method**  string | Enable/disable HTTP method check.  **Choices:**   - `"disable"` - `"enable"` |
| **param-length**  string | Maximum length of parameter in URL, HTTP POST request or HTTP body.  **Choices:**   - `"disable"` - `"enable"` |
| **pattern**  string | URL pattern. |
| **regex**  string | Enable/disable regular expression based pattern match.  **Choices:**   - `"disable"` - `"enable"` |
| **url-param-length**  string | Maximum length of parameter in URL.  **Choices:**   - `"disable"` - `"enable"` |
| **version**  string | Enable/disable HTTP version check.  **Choices:**   - `"disable"` - `"enable"` |
| **header-length**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **length**  integer | Length of HTTP header in bytes |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **hostname**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **line-length**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **length**  integer | Length of HTTP line in bytes |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **malformed**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **max-cookie**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **max-cookie**  integer | Maximum number of cookies in HTTP request |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **max-header-line**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **max-header-line**  integer | Maximum number HTTP header lines |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **max-range-segment**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **max-range-segment**  integer | Maximum number of range segments in HTTP range line |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **max-url-param**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **max-url-param**  integer | Maximum number of parameters in URL |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **method**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **param-length**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **length**  integer | Maximum length of parameter in URL, HTTP POST request or HTTP body in bytes |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **url-param-length**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **length**  integer | Maximum length of URL parameter in bytes |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **version**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Enable/disable the constraint.  **Choices:**   - `"disable"` - `"enable"` |
| **extended-log**  string | Enable/disable extended logging.  **Choices:**   - `"disable"` - `"enable"` |
| **external**  string | Disable/Enable external HTTP Inspection.  **Choices:**   - `"disable"` - `"enable"` |
| **method**  dictionary | no description |
| **default-allowed-methods**  list / elements=string | Methods.  **Choices:**   - `"delete"` - `"get"` - `"head"` - `"options"` - `"post"` - `"put"` - `"trace"` - `"others"` - `"connect"` |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **method-policy**  list / elements=dictionary | Method-Policy. |
| **address**  string | Host address. |
| **allowed-methods**  list / elements=string | Allowed Methods.  **Choices:**   - `"delete"` - `"get"` - `"head"` - `"options"` - `"post"` - `"put"` - `"trace"` - `"others"` - `"connect"` |
| **id**  integer | HTTP method policy ID. |
| **pattern**  string | URL pattern. |
| **regex**  string | Enable/disable regular expression based pattern match.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Status.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | WAF Profile name. |
| **signature**  dictionary | no description |
| **credit-card-detection-threshold**  integer | The minimum number of Credit cards to detect violation. |
| **custom-signature**  list / elements=dictionary | Custom-Signature. |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` - `"erase"` |
| **case-sensitivity**  string | Case sensitivity in pattern.  **Choices:**   - `"disable"` - `"enable"` |
| **direction**  string | Traffic direction.  **Choices:**   - `"request"` - `"response"` |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string | Signature name. |
| **pattern**  string | Match pattern. |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Status.  **Choices:**   - `"disable"` - `"enable"` |
| **target**  list / elements=string | Match HTTP target.  **Choices:**   - `"arg"` - `"arg-name"` - `"req-body"` - `"req-cookie"` - `"req-cookie-name"` - `"req-filename"` - `"req-header"` - `"req-header-name"` - `"req-raw-uri"` - `"req-uri"` - `"resp-body"` - `"resp-hdr"` - `"resp-status"` |
| **disabled-signature**  any | (list or str) Disabled signatures |
| **disabled-sub-class**  any | (list or str) Disabled signature subclasses. |
| **main-class**  dictionary | no description |
| **action**  string | Action.  **Choices:**   - `"allow"` - `"block"` - `"erase"` |
| **id**  integer | Main signature class ID. |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **status**  string | Status.  **Choices:**   - `"disable"` - `"enable"` |
| **url-access**  list / elements=dictionary | Url-Access. |
| **access-pattern**  list / elements=dictionary | Access-Pattern. |
| **id**  integer | URL access pattern ID. |
| **negate**  string | Enable/disable match negation.  **Choices:**   - `"disable"` - `"enable"` |
| **pattern**  string | URL pattern. |
| **regex**  string | Enable/disable regular expression based pattern match.  **Choices:**   - `"disable"` - `"enable"` |
| **srcaddr**  string | Source address. |
| **action**  string | Action.  **Choices:**   - `"bypass"` - `"permit"` - `"block"` |
| **address**  string | Host address. |
| **id**  integer | URL access ID. |
| **log**  string | Enable/disable logging.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Severity.  **Choices:**   - `"low"` - `"medium"` - `"high"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
    - name: Web application firewall configuration.
      fmgr_waf_profile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        waf_profile:
          comment: <string>
          extended-log: <value in [disable, enable]>
          external: <value in [disable, enable]>
          name: <string>
          url-access:
            -
              access-pattern:
                -
                  id: <integer>
                  negate: <value in [disable, enable]>
                  pattern: <string>
                  regex: <value in [disable, enable]>
                  srcaddr: <string>
              action: <value in [bypass, permit, block]>
              address: <string>
              id: <integer>
              log: <value in [disable, enable]>
              severity: <value in [low, medium, high]>
          address-list:
            blocked-address: <list or string>
            blocked-log: <value in [disable, enable]>
            severity: <value in [low, medium, high]>
            status: <value in [disable, enable]>
            trusted-address: <list or string>
          constraint:
            content-length:
              action: <value in [allow, block]>
              length: <integer>
              log: <value in [disable, enable]>
              severity: <value in [low, medium, high]>
              status: <value in [disable, enable]>
            exception:
              -
                address: <string>
                content-length: <value in [disable, enable]>
                header-length: <value in [disable, enable]>
                hostname: <value in [disable, enable]>
                id: <integer>
                line-length: <value in [disable, enable]>
                malformed: <value in [disable, enable]>
                max-cookie: <value in [disable, enable]>
                max-header-line: <value in [disable, enable]>
                max-range-segment: <value in [disable, enable]>
                max-url-param: <value in [disable, enable]>
                method: <value in [disable, enable]>
                param-length: <value in [disable, enable]>
                pattern: <string>
                regex: <value in [disable, enable]>
                url-param-length: <value in [disable, enable]>
                version: <value in [disable, enable]>
            header-length:
              action: <value in [allow, block]>
              length: <integer>
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
              length: <integer>
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
              max-cookie: <integer>
              severity: <value in [low, medium, high]>
              status: <value in [disable, enable]>
            max-header-line:
              action: <value in [allow, block]>
              log: <value in [disable, enable]>
              max-header-line: <integer>
              severity: <value in [low, medium, high]>
              status: <value in [disable, enable]>
            max-range-segment:
              action: <value in [allow, block]>
              log: <value in [disable, enable]>
              max-range-segment: <integer>
              severity: <value in [low, medium, high]>
              status: <value in [disable, enable]>
            max-url-param:
              action: <value in [allow, block]>
              log: <value in [disable, enable]>
              max-url-param: <integer>
              severity: <value in [low, medium, high]>
              status: <value in [disable, enable]>
            method:
              action: <value in [allow, block]>
              log: <value in [disable, enable]>
              severity: <value in [low, medium, high]>
              status: <value in [disable, enable]>
            param-length:
              action: <value in [allow, block]>
              length: <integer>
              log: <value in [disable, enable]>
              severity: <value in [low, medium, high]>
              status: <value in [disable, enable]>
            url-param-length:
              action: <value in [allow, block]>
              length: <integer>
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
                address: <string>
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
                id: <integer>
                pattern: <string>
                regex: <value in [disable, enable]>
            severity: <value in [low, medium, high]>
            status: <value in [disable, enable]>
          signature:
            credit-card-detection-threshold: <integer>
            custom-signature:
              -
                action: <value in [allow, block, erase]>
                case-sensitivity: <value in [disable, enable]>
                direction: <value in [request, response]>
                log: <value in [disable, enable]>
                name: <string>
                pattern: <string>
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
            disabled-signature: <list or string>
            disabled-sub-class: <list or string>
            main-class:
              action: <value in [allow, block, erase]>
              id: <integer>
              log: <value in [disable, enable]>
              severity: <value in [low, medium, high]>
              status: <value in [disable, enable]>
```

## [Return Values](fmgr_waf_profile_module.md#id5)

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
