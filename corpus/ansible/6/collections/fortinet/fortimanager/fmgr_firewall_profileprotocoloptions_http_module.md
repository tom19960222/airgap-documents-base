---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_firewall_profileprotocoloptions_http module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_firewall_profileprotocoloptions_http_module.html
fetched_at: 2026-07-27T17:31:37+00:00
---
# fortinet.fortimanager.fmgr_firewall_profileprotocoloptions_http module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_profileprotocoloptions_http`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_profileprotocoloptions_http_module.md#synopsis)
- [Parameters](fmgr_firewall_profileprotocoloptions_http_module.md#parameters)
- [Notes](fmgr_firewall_profileprotocoloptions_http_module.md#notes)
- [Examples](fmgr_firewall_profileprotocoloptions_http_module.md#examples)
- [Return Values](fmgr_firewall_profileprotocoloptions_http_module.md#return-values)

## [Synopsis](fmgr_firewall_profileprotocoloptions_http_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_profileprotocoloptions_http_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **firewall_profileprotocoloptions_http**  dictionary | the top level parameters set |
| **address-ip-rating**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **block-page-status-code**  integer | no description |
| **comfort-amount**  integer | no description |
| **comfort-interval**  integer | no description |
| **fortinet-bar**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fortinet-bar-port**  integer | no description |
| **h2c**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **http-policy**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **inspect-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **options**  list / elements=string | description  Choices:   - `"oversize"` - `"chunkedbypass"` - `"clientcomfort"` - `"no-content-summary"` - `"servercomfort"` |
| **oversize-limit**  integer | no description |
| **ports**  integer | description |
| **post-lang**  list / elements=string | description  Choices:   - `"jisx0201"` - `"jisx0208"` - `"jisx0212"` - `"gb2312"` - `"ksc5601-ex"` - `"euc-jp"` - `"sjis"` - `"iso2022-jp"` - `"iso2022-jp-1"` - `"iso2022-jp-2"` - `"euc-cn"` - `"ces-gbk"` - `"hz"` - `"ces-big5"` - `"euc-kr"` - `"iso2022-jp-3"` - `"iso8859-1"` - `"tis620"` - `"cp874"` - `"cp1252"` - `"cp1251"` |
| **proxy-after-tcp-handshake**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **range-block**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **retry-count**  integer | no description |
| **scan-bzip2**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-offloaded**  string | no description  Choices:   - `"no"` - `"yes"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **stream-based-uncompressed-limit**  integer | no description |
| **streaming-content-bypass**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **strip-x-forwarded-for**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switching-protocols**  string | no description  Choices:   - `"bypass"` - `"block"` |
| **tcp-window-maximum**  integer | no description |
| **tcp-window-minimum**  integer | no description |
| **tcp-window-size**  integer | no description |
| **tcp-window-type**  string | no description  Choices:   - `"system"` - `"static"` - `"dynamic"` - `"auto-tuning"` |
| **tunnel-non-http**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **uncompressed-nest-limit**  integer | no description |
| **uncompressed-oversize-limit**  integer | no description |
| **unknown-http-version**  string | no description  Choices:   - `"best-effort"` - `"reject"` - `"tunnel"` |
| **profile-protocol-options**  string / required | the parameter (profile-protocol-options) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_firewall_profileprotocoloptions_http_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_profileprotocoloptions_http_module.md#id4)

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
     fmgr_firewall_profileprotocoloptions_http:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        profile-protocol-options: <your own value>
        firewall_profileprotocoloptions_http:
           block-page-status-code: <value of integer>
           comfort-amount: <value of integer>
           comfort-interval: <value of integer>
           fortinet-bar: <value in [disable, enable]>
           fortinet-bar-port: <value of integer>
           http-policy: <value in [disable, enable]>
           inspect-all: <value in [disable, enable]>
           options:
             - oversize
             - chunkedbypass
             - clientcomfort
             - no-content-summary
             - servercomfort
           oversize-limit: <value of integer>
           ports: <value of integer>
           post-lang:
             - jisx0201
             - jisx0208
             - jisx0212
             - gb2312
             - ksc5601-ex
             - euc-jp
             - sjis
             - iso2022-jp
             - iso2022-jp-1
             - iso2022-jp-2
             - euc-cn
             - ces-gbk
             - hz
             - ces-big5
             - euc-kr
             - iso2022-jp-3
             - iso8859-1
             - tis620
             - cp874
             - cp1252
             - cp1251
           range-block: <value in [disable, enable]>
           retry-count: <value of integer>
           scan-bzip2: <value in [disable, enable]>
           status: <value in [disable, enable]>
           streaming-content-bypass: <value in [disable, enable]>
           strip-x-forwarded-for: <value in [disable, enable]>
           switching-protocols: <value in [bypass, block]>
           uncompressed-nest-limit: <value of integer>
           uncompressed-oversize-limit: <value of integer>
           tcp-window-maximum: <value of integer>
           tcp-window-minimum: <value of integer>
           tcp-window-size: <value of integer>
           tcp-window-type: <value in [system, static, dynamic, ...]>
           ssl-offloaded: <value in [no, yes]>
           stream-based-uncompressed-limit: <value of integer>
           proxy-after-tcp-handshake: <value in [disable, enable]>
           tunnel-non-http: <value in [disable, enable]>
           unknown-http-version: <value in [best-effort, reject, tunnel]>
           address-ip-rating: <value in [disable, enable]>
           h2c: <value in [disable, enable]>
```

## [Return Values](fmgr_firewall_profileprotocoloptions_http_module.md#id5)

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
