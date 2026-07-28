---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_fmupdate_webspam_fgdsetting module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_fmupdate_webspam_fgdsetting_module.html
fetched_at: 2026-07-27T17:32:37+00:00
---
# fortinet.fortimanager.fmgr_fmupdate_webspam_fgdsetting module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fmupdate_webspam_fgdsetting`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_fmupdate_webspam_fgdsetting_module.md#synopsis)
- [Parameters](fmgr_fmupdate_webspam_fgdsetting_module.md#parameters)
- [Notes](fmgr_fmupdate_webspam_fgdsetting_module.md#notes)
- [Examples](fmgr_fmupdate_webspam_fgdsetting_module.md#examples)
- [Return Values](fmgr_fmupdate_webspam_fgdsetting_module.md#return-values)

## [Synopsis](fmgr_fmupdate_webspam_fgdsetting_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_fmupdate_webspam_fgdsetting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **fmupdate_webspam_fgdsetting**  dictionary | the top level parameters set |
| **as-cache**  integer | no description  Default: `300` |
| **as-log**  string | no description  no description  no description  no description  Choices:   - `"disable"` - `"nospam"` ← (default) - `"all"` |
| **as-preload**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **av-cache**  integer | no description  Default: `300` |
| **av-log**  string | no description  no description  no description  no description  Choices:   - `"disable"` - `"novirus"` ← (default) - `"all"` |
| **av-preload**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **av2-cache**  integer | no description  Default: `800` |
| **av2-log**  string | no description  no description  no description  no description  Choices:   - `"disable"` - `"noav2"` ← (default) - `"all"` |
| **av2-preload**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **eventlog-query**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **fgd-pull-interval**  integer | no description  Default: `10` |
| **fq-cache**  integer | no description  Default: `300` |
| **fq-log**  string | no description  no description  no description  no description  Choices:   - `"disable"` - `"nofilequery"` ← (default) - `"all"` |
| **fq-preload**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **iot-cache**  integer | no description  Default: `300` |
| **iot-log**  string | no description  no description  no description  no description  Choices:   - `"disable"` - `"nofilequery"` ← (default) - `"all"` |
| **iot-preload**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **linkd-log**  string | no description  no description  no description  no description  no description  no description  no description  no description  no description  no description  Choices:   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warn"` - `"notice"` - `"info"` - `"debug"` ← (default) - `"disable"` |
| **max-client-worker**  integer | no description  Default: `0` |
| **max-log-quota**  integer | no description  Default: `6144` |
| **max-unrated-site**  integer | no description  Default: `500` |
| **restrict-as1-dbver**  string | no description |
| **restrict-as2-dbver**  string | no description |
| **restrict-as4-dbver**  string | no description |
| **restrict-av-dbver**  string | no description |
| **restrict-av2-dbver**  string | no description |
| **restrict-fq-dbver**  string | no description |
| **restrict-iots-dbver**  string | no description |
| **restrict-wf-dbver**  string | no description |
| **server-override**  dictionary | no description |
| **servlist**  list / elements=string | no description |
| **id**  integer | no description  Default: `0` |
| **ip**  string | no description  Default: `"0."` |
| **ip6**  string | no description  Default: `"no description"` |
| **port**  integer | no description  Default: `443` |
| **service-type**  list / elements=string | no description  Choices:   - `"fgd"` - `"fgc"` - `"fsa"` |
| **status**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **stat-log-interval**  integer | no description  Default: `60` |
| **stat-sync-interval**  integer | no description  Default: `60` |
| **update-interval**  integer | no description  Default: `6` |
| **update-log**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **wf-cache**  integer | no description  Default: `0` |
| **wf-dn-cache-expire-time**  integer | no description  Default: `30` |
| **wf-dn-cache-max-number**  integer | no description  Default: `10000` |
| **wf-log**  string | no description  no description  no description  no description  Choices:   - `"disable"` - `"nourl"` ← (default) - `"all"` |
| **wf-preload**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_fmupdate_webspam_fgdsetting_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_fmupdate_webspam_fgdsetting_module.md#id4)

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
     fmgr_fmupdate_webspam_fgdsetting:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        fmupdate_webspam_fgdsetting:
           as-cache: <value of integer>
           as-log: <value in [disable, nospam, all]>
           as-preload: <value in [disable, enable]>
           av-cache: <value of integer>
           av-log: <value in [disable, novirus, all]>
           av-preload: <value in [disable, enable]>
           av2-cache: <value of integer>
           av2-log: <value in [disable, noav2, all]>
           av2-preload: <value in [disable, enable]>
           eventlog-query: <value in [disable, enable]>
           fgd-pull-interval: <value of integer>
           fq-cache: <value of integer>
           fq-log: <value in [disable, nofilequery, all]>
           fq-preload: <value in [disable, enable]>
           linkd-log: <value in [emergency, alert, critical, ...]>
           max-client-worker: <value of integer>
           max-log-quota: <value of integer>
           max-unrated-site: <value of integer>
           restrict-as1-dbver: <value of string>
           restrict-as2-dbver: <value of string>
           restrict-as4-dbver: <value of string>
           restrict-av-dbver: <value of string>
           restrict-av2-dbver: <value of string>
           restrict-fq-dbver: <value of string>
           restrict-wf-dbver: <value of string>
           server-override:
              servlist:
                -
                    id: <value of integer>
                    ip: <value of string>
                    ip6: <value of string>
                    port: <value of integer>
                    service-type:
                      - fgd
                      - fgc
                      - fsa
              status: <value in [disable, enable]>
           stat-log-interval: <value of integer>
           stat-sync-interval: <value of integer>
           update-interval: <value of integer>
           update-log: <value in [disable, enable]>
           wf-cache: <value of integer>
           wf-dn-cache-expire-time: <value of integer>
           wf-dn-cache-max-number: <value of integer>
           wf-log: <value in [disable, nourl, all]>
           wf-preload: <value in [disable, enable]>
           iot-cache: <value of integer>
           iot-log: <value in [disable, nofilequery, all]>
           iot-preload: <value in [disable, enable]>
           restrict-iots-dbver: <value of string>
```

## [Return Values](fmgr_fmupdate_webspam_fgdsetting_module.md#id5)

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
