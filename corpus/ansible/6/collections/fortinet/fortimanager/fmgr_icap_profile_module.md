---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_icap_profile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_icap_profile_module.html
fetched_at: 2026-07-27T17:33:28+00:00
---
# fortinet.fortimanager.fmgr_icap_profile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_icap_profile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_icap_profile_module.md#synopsis)
- [Parameters](fmgr_icap_profile_module.md#parameters)
- [Notes](fmgr_icap_profile_module.md#notes)
- [Examples](fmgr_icap_profile_module.md#examples)
- [Return Values](fmgr_icap_profile_module.md#return-values)

## [Synopsis](fmgr_icap_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_icap_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **icap_profile**  dictionary | the top level parameters set |
| **204-response**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **204-size-limit**  integer | no description |
| **chunk-encap**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **extension-feature**  list / elements=string | description  Choices:   - `"scan-progress"` |
| **file-transfer**  list / elements=string | description  Choices:   - `"ssh"` - `"ftp"` |
| **file-transfer-failure**  string | no description  Choices:   - `"error"` - `"bypass"` |
| **file-transfer-path**  string | no description |
| **file-transfer-server**  string | no description |
| **icap-block-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **icap-headers**  list / elements=string | no description |
| **base64-encoding**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **content**  string | no description |
| **id**  integer | no description |
| **name**  string | no description |
| **methods**  list / elements=string | no description  Choices:   - `"delete"` - `"get"` - `"head"` - `"options"` - `"post"` - `"put"` - `"trace"` - `"other"` - `"connect"` |
| **name**  string | no description |
| **preview**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **preview-data-length**  integer | no description |
| **replacemsg-group**  string | no description |
| **request**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **request-failure**  string | no description  Choices:   - `"error"` - `"bypass"` |
| **request-path**  string | no description |
| **request-server**  string | no description |
| **respmod-default-action**  string | no description  Choices:   - `"bypass"` - `"forward"` |
| **respmod-forward-rules**  list / elements=string | no description |
| **action**  string | no description  Choices:   - `"bypass"` - `"forward"` |
| **header-group**  list / elements=string | no description |
| **case-sensitivity**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **header**  string | no description |
| **header-name**  string | no description |
| **id**  integer | no description |
| **host**  string | no description |
| **http-resp-status-code**  integer | no description |
| **name**  string | no description |
| **response**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **response-failure**  string | no description  Choices:   - `"error"` - `"bypass"` |
| **response-path**  string | no description |
| **response-req-hdr**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **response-server**  string | no description |
| **scan-progress-interval**  integer | no description |
| **streaming-content-bypass**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **timeout**  integer | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_icap_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_icap_profile_module.md#id4)

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
     fmgr_icap_profile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        icap_profile:
           methods:
             - delete
             - get
             - head
             - options
             - post
             - put
             - trace
             - other
             - connect
           name: <value of string>
           replacemsg-group: <value of string>
           request: <value in [disable, enable]>
           request-failure: <value in [error, bypass]>
           request-path: <value of string>
           request-server: <value of string>
           response: <value in [disable, enable]>
           response-failure: <value in [error, bypass]>
           response-path: <value of string>
           response-server: <value of string>
           streaming-content-bypass: <value in [disable, enable]>
           icap-headers:
             -
                 base64-encoding: <value in [disable, enable]>
                 content: <value of string>
                 id: <value of integer>
                 name: <value of string>
           preview: <value in [disable, enable]>
           preview-data-length: <value of integer>
           response-req-hdr: <value in [disable, enable]>
           respmod-default-action: <value in [bypass, forward]>
           respmod-forward-rules:
             -
                 action: <value in [bypass, forward]>
                 header-group:
                   -
                       case-sensitivity: <value in [disable, enable]>
                       header: <value of string>
                       header-name: <value of string>
                       id: <value of integer>
                 host: <value of string>
                 http-resp-status-code: <value of integer>
                 name: <value of string>
           204-response: <value in [disable, enable]>
           204-size-limit: <value of integer>
           chunk-encap: <value in [disable, enable]>
           extension-feature:
             - scan-progress
           file-transfer:
             - ssh
             - ftp
           file-transfer-failure: <value in [error, bypass]>
           file-transfer-path: <value of string>
           file-transfer-server: <value of string>
           icap-block-log: <value in [disable, enable]>
           scan-progress-interval: <value of integer>
           timeout: <value of integer>
```

## [Return Values](fmgr_icap_profile_module.md#id5)

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
