---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_dlp_sensor_filter module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_dlp_sensor_filter_module.html
fetched_at: 2026-07-27T17:29:15+00:00
---
# fortinet.fortimanager.fmgr_dlp_sensor_filter module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_dlp_sensor_filter`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_dlp_sensor_filter_module.md#synopsis)
- [Parameters](fmgr_dlp_sensor_filter_module.md#parameters)
- [Notes](fmgr_dlp_sensor_filter_module.md#notes)
- [Examples](fmgr_dlp_sensor_filter_module.md#examples)
- [Return Values](fmgr_dlp_sensor_filter_module.md#return-values)

## [Synopsis](fmgr_dlp_sensor_filter_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_dlp_sensor_filter_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **dlp_sensor_filter**  dictionary | the top level parameters set |
| **action**  string | no description  Choices:   - `"log-only"` - `"block"` - `"exempt"` - `"ban"` - `"ban-sender"` - `"quarantine-ip"` - `"quarantine-port"` - `"none"` - `"allow"` |
| **archive**  string | no description  Choices:   - `"disable"` - `"enable"` - `"summary-only"` |
| **company-identifier**  string | no description |
| **expiry**  string | no description |
| **file-size**  integer | no description |
| **file-type**  string | no description |
| **filter-by**  string | no description  Choices:   - `"credit-card"` - `"ssn"` - `"regexp"` - `"file-type"` - `"file-size"` - `"fingerprint"` - `"watermark"` - `"encrypted"` |
| **fp-sensitivity**  string | no description |
| **id**  integer | no description |
| **match-percentage**  integer | no description |
| **name**  string | no description |
| **proto**  list / elements=string | description  Choices:   - `"imap"` - `"smtp"` - `"pop3"` - `"ftp"` - `"nntp"` - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` - `"mapi"` - `"aim"` - `"icq"` - `"msn"` - `"yahoo"` - `"http-get"` - `"http-post"` - `"ssh"` - `"cifs"` |
| **regexp**  string | no description |
| **sensitivity**  string | no description |
| **severity**  string | no description  Choices:   - `"info"` - `"low"` - `"medium"` - `"high"` - `"critical"` |
| **type**  string | no description  Choices:   - `"file"` - `"message"` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **sensor**  string / required | the parameter (sensor) in requested url |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_dlp_sensor_filter_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_dlp_sensor_filter_module.md#id4)

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
     fmgr_dlp_sensor_filter:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        sensor: <your own value>
        state: <value in [present, absent]>
        dlp_sensor_filter:
           action: <value in [log-only, block, exempt, ...]>
           archive: <value in [disable, enable, summary-only]>
           company-identifier: <value of string>
           expiry: <value of string>
           file-size: <value of integer>
           file-type: <value of string>
           filter-by: <value in [credit-card, ssn, regexp, ...]>
           fp-sensitivity: <value of string>
           id: <value of integer>
           match-percentage: <value of integer>
           name: <value of string>
           proto:
             - imap
             - smtp
             - pop3
             - ftp
             - nntp
             - mm1
             - mm3
             - mm4
             - mm7
             - mapi
             - aim
             - icq
             - msn
             - yahoo
             - http-get
             - http-post
             - ssh
             - cifs
           regexp: <value of string>
           severity: <value in [info, low, medium, ...]>
           type: <value in [file, message]>
           sensitivity: <value of string>
```

## [Return Values](fmgr_dlp_sensor_filter_module.md#id5)

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
