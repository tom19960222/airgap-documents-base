---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_fmupdate_fdssetting module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_fmupdate_fdssetting_module.html
fetched_at: 2026-07-27T17:32:27+00:00
---
# fortinet.fortimanager.fmgr_fmupdate_fdssetting module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fmupdate_fdssetting`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_fmupdate_fdssetting_module.md#synopsis)
- [Parameters](fmgr_fmupdate_fdssetting_module.md#parameters)
- [Notes](fmgr_fmupdate_fdssetting_module.md#notes)
- [Examples](fmgr_fmupdate_fdssetting_module.md#examples)
- [Return Values](fmgr_fmupdate_fdssetting_module.md#return-values)

## [Synopsis](fmgr_fmupdate_fdssetting_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_fmupdate_fdssetting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **fmupdate_fdssetting**  dictionary | the top level parameters set |
| **fds-clt-ssl-protocol**  string | no description  no description  no description  no description  no description  Choices:   - `"sslv3"` - `"tlsv1.0"` - `"tlsv1.1"` - `"tlsv1.2"` - `"tlsv1.3"`   Default: `"tlsv1."` |
| **fds-ssl-protocol**  string | no description  no description  no description  no description  no description  Choices:   - `"sslv3"` - `"tlsv1.0"` - `"tlsv1.1"` - `"tlsv1.2"` - `"tlsv1.3"`   Default: `"tlsv1."` |
| **fmtr-log**  string | no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  Choices:   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warn"` - `"notice"` - `"info"` ← (default) - `"debug"` - `"disable"` |
| **fortiguard-anycast**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **fortiguard-anycast-source**  string | no description  no description  no description  Choices:   - `"fortinet"` ← (default) - `"aws"` |
| **linkd-log**  string | no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  Choices:   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warn"` - `"notice"` - `"info"` ← (default) - `"debug"` - `"disable"` |
| **max-av-ips-version**  integer | no description  Default: `20` |
| **max-work**  integer | no description  Default: `1` |
| **push-override**  dictionary | no description |
| **ip**  string | no description  Default: `"0."` |
| **port**  integer | no description  Default: `9443` |
| **status**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **push-override-to-client**  dictionary | no description |
| **announce-ip**  list / elements=string | no description |
| **id**  integer | no description  Default: `0` |
| **ip**  string | no description  Default: `"0."` |
| **port**  integer | no description  Default: `8890` |
| **status**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **send_report**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **send_setup**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **server-override**  dictionary | no description |
| **servlist**  list / elements=string | no description |
| **id**  integer | no description  Default: `0` |
| **ip**  string | no description  Default: `"0."` |
| **ip6**  string | no description  Default: `"no description"` |
| **port**  integer | no description  Default: `443` |
| **service-type**  list / elements=string | no description  Choices:   - `"fds"` - `"fct"` |
| **status**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **system-support-fct**  list / elements=string | no description  Choices:   - `"4.x"` - `5.0` - `5.2` - `5.4` - `5.6` - `6.0` - `6.2` - `6.4` - `7.0` |
| **system-support-fdc**  list / elements=string | description  Choices:   - `"3.x"` - `"4.x"` |
| **system-support-fgt**  list / elements=string | no description  Choices:   - `5.4` - `5.6` - `6.0` - `6.2` - `6.4` - `7.0` - `7.2` |
| **system-support-fml**  list / elements=string | no description  Choices:   - `"4.x"` - `"5.x"` - `"6.x"` - `6.0` - `6.2` - `6.4` - `7.0` |
| **system-support-fsa**  list / elements=string | no description  Choices:   - `"1.x"` - `"2.x"` - `"3.x"` - `"4.x"` - `3.0` - `3.1` - `3.2` |
| **system-support-fsw**  list / elements=string | no description  Choices:   - `5.4` - `5.6` - `6.0` - `6.2` - `"4.x"` - `5.0` - `5.2` - `6.4` |
| **system-support-fts**  list / elements=string | description  Choices:   - `"3.x"` - `"4.x"` - `"7.x"` |
| **umsvc-log**  string | no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  Choices:   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warn"` - `"notice"` - `"info"` ← (default) - `"debug"` - `"disable"` |
| **unreg-dev-option**  string | no description  no description  no description  no description  Choices:   - `"ignore"` - `"svc-only"` - `"add-service"` ← (default) |
| **update-schedule**  dictionary | no description |
| **day**  string | no description  no description  no description  no description  no description  no description  no description  no description  Choices:   - `"Sunday"` - `"Monday"` ← (default) - `"Tuesday"` - `"Wednesday"` - `"Thursday"` - `"Friday"` - `"Saturday"` |
| **frequency**  string | no description  no description  no description  no description  Choices:   - `"every"` ← (default) - `"daily"` - `"weekly"` |
| **status**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **time**  string | no description |
| **User-Agent**  string | no description  Default: `"Mozilla/5."` |
| **wanip-query-mode**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"ipify"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_fmupdate_fdssetting_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_fmupdate_fdssetting_module.md#id4)

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
     fmgr_fmupdate_fdssetting:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        fmupdate_fdssetting:
           User-Agent: <value of string>
           fds-clt-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...]>
           fds-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...]>
           fmtr-log: <value in [emergency, alert, critical, ...]>
           linkd-log: <value in [emergency, alert, critical, ...]>
           max-av-ips-version: <value of integer>
           max-work: <value of integer>
           push-override:
              ip: <value of string>
              port: <value of integer>
              status: <value in [disable, enable]>
           push-override-to-client:
              announce-ip:
                -
                    id: <value of integer>
                    ip: <value of string>
                    port: <value of integer>
              status: <value in [disable, enable]>
           send_report: <value in [disable, enable]>
           send_setup: <value in [disable, enable]>
           server-override:
              servlist:
                -
                    id: <value of integer>
                    ip: <value of string>
                    ip6: <value of string>
                    port: <value of integer>
                    service-type:
                      - fds
                      - fct
              status: <value in [disable, enable]>
           system-support-fct:
             - 4.x
             - 5.0
             - 5.2
             - 5.4
             - 5.6
             - 6.0
             - 6.2
             - 6.4
             - 7.0
           system-support-fgt:
             - 5.4
             - 5.6
             - 6.0
             - 6.2
             - 6.4
             - 7.0
             - 7.2
           system-support-fml:
             - 4.x
             - 5.x
             - 6.x
             - 6.0
             - 6.2
             - 6.4
             - 7.0
           system-support-fsa:
             - 1.x
             - 2.x
             - 3.x
             - 4.x
             - 3.0
             - 3.1
             - 3.2
           system-support-fsw:
             - 5.4
             - 5.6
             - 6.0
             - 6.2
             - 4.x
             - 5.0
             - 5.2
             - 6.4
           umsvc-log: <value in [emergency, alert, critical, ...]>
           unreg-dev-option: <value in [ignore, svc-only, add-service]>
           update-schedule:
              day: <value in [Sunday, Monday, Tuesday, ...]>
              frequency: <value in [every, daily, weekly]>
              status: <value in [disable, enable]>
              time: <value of string>
           wanip-query-mode: <value in [disable, ipify]>
           fortiguard-anycast: <value in [disable, enable]>
           fortiguard-anycast-source: <value in [fortinet, aws]>
           system-support-fdc:
             - 3.x
             - 4.x
           system-support-fts:
             - 3.x
             - 4.x
             - 7.x
```

## [Return Values](fmgr_fmupdate_fdssetting_module.md#id5)

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
