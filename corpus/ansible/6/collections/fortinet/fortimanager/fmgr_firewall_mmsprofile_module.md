---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_firewall_mmsprofile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_firewall_mmsprofile_module.html
fetched_at: 2026-07-27T17:31:25+00:00
---
# fortinet.fortimanager.fmgr_firewall_mmsprofile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_mmsprofile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_mmsprofile_module.md#synopsis)
- [Parameters](fmgr_firewall_mmsprofile_module.md#parameters)
- [Notes](fmgr_firewall_mmsprofile_module.md#notes)
- [Examples](fmgr_firewall_mmsprofile_module.md#examples)
- [Return Values](fmgr_firewall_mmsprofile_module.md#return-values)

## [Synopsis](fmgr_firewall_mmsprofile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_mmsprofile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **firewall_mmsprofile**  dictionary | the top level parameters set |
| **avnotificationtable**  string | no description |
| **bwordtable**  string | no description |
| **carrier-endpoint-prefix**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **carrier-endpoint-prefix-range-max**  integer | no description |
| **carrier-endpoint-prefix-range-min**  integer | no description |
| **carrier-endpoint-prefix-string**  string | no description |
| **carrierendpointbwltable**  string | no description |
| **comment**  string | no description |
| **mm1**  list / elements=string | no description  Choices:   - `"avmonitor"` - `"block"` - `"oversize"` - `"quarantine"` - `"scan"` - `"avquery"` - `"bannedword"` - `"no-content-summary"` - `"archive-summary"` - `"archive-full"` - `"carrier-endpoint-bwl"` - `"remove-blocked"` - `"chunkedbypass"` - `"clientcomfort"` - `"servercomfort"` - `"strict-file"` - `"mms-checksum"` |
| **mm1-addr-hdr**  string | no description |
| **mm1-addr-source**  string | no description  Choices:   - `"http-header"` - `"cookie"` |
| **mm1-convert-hex**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mm1-outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` |
| **mm1-retr-dupe**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mm1-retrieve-scan**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mm1comfortamount**  integer | no description |
| **mm1comfortinterval**  integer | no description |
| **mm1oversizelimit**  integer | no description |
| **mm3**  list / elements=string | no description  Choices:   - `"avmonitor"` - `"block"` - `"oversize"` - `"quarantine"` - `"scan"` - `"avquery"` - `"bannedword"` - `"no-content-summary"` - `"archive-summary"` - `"archive-full"` - `"carrier-endpoint-bwl"` - `"remove-blocked"` - `"fragmail"` - `"splice"` - `"mms-checksum"` |
| **mm3-outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` |
| **mm3oversizelimit**  integer | no description |
| **mm4**  list / elements=string | no description  Choices:   - `"avmonitor"` - `"block"` - `"oversize"` - `"quarantine"` - `"scan"` - `"avquery"` - `"bannedword"` - `"no-content-summary"` - `"archive-summary"` - `"archive-full"` - `"carrier-endpoint-bwl"` - `"remove-blocked"` - `"fragmail"` - `"splice"` - `"mms-checksum"` |
| **mm4-outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` |
| **mm4oversizelimit**  integer | no description |
| **mm7**  list / elements=string | no description  Choices:   - `"avmonitor"` - `"block"` - `"oversize"` - `"quarantine"` - `"scan"` - `"avquery"` - `"bannedword"` - `"no-content-summary"` - `"archive-summary"` - `"archive-full"` - `"carrier-endpoint-bwl"` - `"remove-blocked"` - `"chunkedbypass"` - `"clientcomfort"` - `"servercomfort"` - `"strict-file"` - `"mms-checksum"` |
| **mm7-addr-hdr**  string | no description |
| **mm7-addr-source**  string | no description  Choices:   - `"http-header"` - `"cookie"` |
| **mm7-convert-hex**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mm7-outbreak-prevention**  string | no description  Choices:   - `"disabled"` - `"files"` - `"full-archive"` |
| **mm7comfortamount**  integer | no description |
| **mm7comfortinterval**  integer | no description |
| **mm7oversizelimit**  integer | no description |
| **mms-antispam-mass-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-av-block-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-av-oversize-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-av-virus-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-carrier-endpoint-filter-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-checksum-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-checksum-table**  string | no description |
| **mms-notification-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-web-content-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mmsbwordthreshold**  integer | no description |
| **name**  string | no description |
| **notif-msisdn**  list / elements=string | no description |
| **msisdn**  string | no description |
| **threshold**  list / elements=string | no description  Choices:   - `"flood-thresh-1"` - `"flood-thresh-2"` - `"flood-thresh-3"` - `"dupe-thresh-1"` - `"dupe-thresh-2"` - `"dupe-thresh-3"` |
| **remove-blocked-const-length**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **replacemsg-group**  string | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_firewall_mmsprofile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_mmsprofile_module.md#id4)

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
   - name: retrieve all the MMS profiles
     fmgr_fact:
       facts:
           selector: 'firewall_mmsprofile'
           params:
               adom: 'FortiCarrier' # FortiCarrier only object, need a FortiCarrier adom
               mms-profile: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure MMS profiles.
     fmgr_firewall_mmsprofile:
        bypass_validation: False
        adom: FortiCarrier # FortiCarrier only object, need a FortiCarrier adom
        state: present
        firewall_mmsprofile:
           comment: 'ansible-comment'
           #extended-utm-log: disable
           mm1:
             - avmonitor
             - block
             - oversize
             - quarantine
             - scan
             - avquery
             - bannedword
             - no-content-summary
             - archive-summary
             - archive-full
             - carrier-endpoint-bwl
             - remove-blocked
             - chunkedbypass
             - clientcomfort
             - servercomfort
             - strict-file
             - mms-checksum
           mm3:
             - avmonitor
             - block
             - oversize
             - quarantine
             - scan
             - avquery
             - bannedword
             - no-content-summary
             - archive-summary
             - archive-full
             - carrier-endpoint-bwl
             - remove-blocked
             - fragmail
             - splice
             - mms-checksum
           mm4:
             - avmonitor
             - block
             - oversize
             - quarantine
             - scan
             - avquery
             - bannedword
             - no-content-summary
             - archive-summary
             - archive-full
             - carrier-endpoint-bwl
             - remove-blocked
             - fragmail
             - splice
             - mms-checksum
           mm7:
             - avmonitor
             - block
             - oversize
             - quarantine
             - scan
             - avquery
             - bannedword
             - no-content-summary
             - archive-summary
             - archive-full
             - carrier-endpoint-bwl
             - remove-blocked
             - chunkedbypass
             - clientcomfort
             - servercomfort
             - strict-file
             - mms-checksum
           name: 'ansible-test'
```

## [Return Values](fmgr_firewall_mmsprofile_module.md#id5)

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
