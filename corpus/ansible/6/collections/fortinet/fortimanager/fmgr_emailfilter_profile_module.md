---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_emailfilter_profile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_emailfilter_profile_module.html
fetched_at: 2026-07-27T17:30:17+00:00
---
# fortinet.fortimanager.fmgr_emailfilter_profile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_emailfilter_profile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_emailfilter_profile_module.md#synopsis)
- [Parameters](fmgr_emailfilter_profile_module.md#parameters)
- [Notes](fmgr_emailfilter_profile_module.md#notes)
- [Examples](fmgr_emailfilter_profile_module.md#examples)
- [Return Values](fmgr_emailfilter_profile_module.md#return-values)

## [Synopsis](fmgr_emailfilter_profile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_emailfilter_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **emailfilter_profile**  dictionary | the top level parameters set |
| **comment**  string | no description |
| **external**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **feature-set**  string | no description  Choices:   - `"proxy"` - `"flow"` |
| **gmail**  dictionary | no description |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **log-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **imap**  dictionary | no description |
| **action**  string | no description  Choices:   - `"pass"` - `"tag"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **log-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tag-msg**  string | no description |
| **tag-type**  list / elements=string | no description  Choices:   - `"subject"` - `"header"` - `"spaminfo"` |
| **mapi**  dictionary | no description |
| **action**  string | no description  Choices:   - `"pass"` - `"discard"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **log-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **msn-hotmail**  dictionary | no description |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **log-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **name**  string | no description |
| **options**  list / elements=string | no description  Choices:   - `"bannedword"` - `"spambwl"` - `"spamfsip"` - `"spamfssubmit"` - `"spamfschksum"` - `"spamfsurl"` - `"spamhelodns"` - `"spamraddrdns"` - `"spamrbl"` - `"spamhdrcheck"` - `"spamfsphish"` - `"spambal"` - `"spamfgip"` - `"spamfgsubmit"` - `"spamfgchksum"` - `"spamfgurl"` - `"spamfgphish"` |
| **other-webmails**  dictionary | no description |
| **log-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pop3**  dictionary | no description |
| **action**  string | no description  Choices:   - `"pass"` - `"tag"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **log-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tag-msg**  string | no description |
| **tag-type**  list / elements=string | no description  Choices:   - `"subject"` - `"header"` - `"spaminfo"` |
| **replacemsg-group**  string | no description |
| **smtp**  dictionary | no description |
| **action**  string | no description  Choices:   - `"pass"` - `"tag"` - `"discard"` |
| **hdrip**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **local-override**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **log-all**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tag-msg**  string | no description |
| **tag-type**  list / elements=string | no description  Choices:   - `"subject"` - `"header"` - `"spaminfo"` |
| **spam-bal-table**  string | no description |
| **spam-bwl-table**  string | no description |
| **spam-bword-table**  string | no description |
| **spam-bword-threshold**  integer | no description |
| **spam-filtering**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **spam-iptrust-table**  string | no description |
| **spam-log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **spam-log-fortiguard-response**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **spam-mheader-table**  string | no description |
| **spam-rbl-table**  string | no description |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_emailfilter_profile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_emailfilter_profile_module.md#id4)

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
     fmgr_emailfilter_profile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        emailfilter_profile:
           comment: <value of string>
           external: <value in [disable, enable]>
           name: <value of string>
           options:
             - bannedword
             - spambwl
             - spamfsip
             - spamfssubmit
             - spamfschksum
             - spamfsurl
             - spamhelodns
             - spamraddrdns
             - spamrbl
             - spamhdrcheck
             - spamfsphish
             - spambal
             - spamfgip
             - spamfgsubmit
             - spamfgchksum
             - spamfgurl
             - spamfgphish
           replacemsg-group: <value of string>
           spam-bwl-table: <value of string>
           spam-bword-table: <value of string>
           spam-bword-threshold: <value of integer>
           spam-filtering: <value in [disable, enable]>
           spam-iptrust-table: <value of string>
           spam-log: <value in [disable, enable]>
           spam-log-fortiguard-response: <value in [disable, enable]>
           spam-mheader-table: <value of string>
           spam-rbl-table: <value of string>
           feature-set: <value in [proxy, flow]>
           gmail:
              log: <value in [disable, enable]>
              log-all: <value in [disable, enable]>
           imap:
              action: <value in [pass, tag]>
              log: <value in [disable, enable]>
              log-all: <value in [disable, enable]>
              tag-msg: <value of string>
              tag-type:
                - subject
                - header
                - spaminfo
           mapi:
              action: <value in [pass, discard]>
              log: <value in [disable, enable]>
              log-all: <value in [disable, enable]>
           msn-hotmail:
              log: <value in [disable, enable]>
              log-all: <value in [disable, enable]>
           other-webmails:
              log-all: <value in [disable, enable]>
           pop3:
              action: <value in [pass, tag]>
              log: <value in [disable, enable]>
              log-all: <value in [disable, enable]>
              tag-msg: <value of string>
              tag-type:
                - subject
                - header
                - spaminfo
           smtp:
              action: <value in [pass, tag, discard]>
              hdrip: <value in [disable, enable]>
              local-override: <value in [disable, enable]>
              log: <value in [disable, enable]>
              log-all: <value in [disable, enable]>
              tag-msg: <value of string>
              tag-type:
                - subject
                - header
                - spaminfo
           spam-bal-table: <value of string>
```

## [Return Values](fmgr_emailfilter_profile_module.md#id5)

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
