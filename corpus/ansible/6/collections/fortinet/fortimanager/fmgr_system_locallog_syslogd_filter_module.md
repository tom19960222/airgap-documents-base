---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_locallog_syslogd_filter module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_locallog_syslogd_filter_module.html
fetched_at: 2026-07-27T17:36:27+00:00
---
# fortinet.fortimanager.fmgr_system_locallog_syslogd_filter module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_locallog_syslogd_filter`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_locallog_syslogd_filter_module.md#synopsis)
- [Parameters](fmgr_system_locallog_syslogd_filter_module.md#parameters)
- [Notes](fmgr_system_locallog_syslogd_filter_module.md#notes)
- [Examples](fmgr_system_locallog_syslogd_filter_module.md#examples)
- [Return Values](fmgr_system_locallog_syslogd_filter_module.md#return-values)

## [Synopsis](fmgr_system_locallog_syslogd_filter_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_locallog_syslogd_filter_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_locallog_syslogd_filter**  dictionary | the top level parameters set |
| **aid**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **devcfg**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **devops**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **diskquota**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **dm**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **docker**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **dvm**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **ediscovery**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **epmgr**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **event**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **eventmgmt**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **faz**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **fazha**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **fazsys**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **fgd**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **fgfm**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **fips**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **fmgws**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **fmlmgr**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **fmwmgr**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **fortiview**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **glbcfg**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **ha**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **hcache**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **incident**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **iolog**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **logd**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **logdb**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **logdev**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **logfile**  string | no description  no description  no description  Choices:   - `"enable"` - `"disable"` |
| **logging**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **lrmgr**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **objcfg**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **report**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **rev**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **rtmon**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **scfw**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **scply**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **scrmgr**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **scvpn**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **system**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **webport**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_system_locallog_syslogd_filter_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_locallog_syslogd_filter_module.md#id4)

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
     fmgr_system_locallog_syslogd_filter:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_locallog_syslogd_filter:
           devcfg: <value in [disable, enable]>
           devops: <value in [disable, enable]>
           diskquota: <value in [disable, enable]>
           dm: <value in [disable, enable]>
           dvm: <value in [disable, enable]>
           ediscovery: <value in [disable, enable]>
           epmgr: <value in [disable, enable]>
           event: <value in [disable, enable]>
           eventmgmt: <value in [disable, enable]>
           faz: <value in [disable, enable]>
           fazha: <value in [disable, enable]>
           fazsys: <value in [disable, enable]>
           fgd: <value in [disable, enable]>
           fgfm: <value in [disable, enable]>
           fips: <value in [disable, enable]>
           fmgws: <value in [disable, enable]>
           fmlmgr: <value in [disable, enable]>
           fmwmgr: <value in [disable, enable]>
           fortiview: <value in [disable, enable]>
           glbcfg: <value in [disable, enable]>
           ha: <value in [disable, enable]>
           hcache: <value in [disable, enable]>
           iolog: <value in [disable, enable]>
           logd: <value in [disable, enable]>
           logdb: <value in [disable, enable]>
           logdev: <value in [disable, enable]>
           logfile: <value in [enable, disable]>
           logging: <value in [disable, enable]>
           lrmgr: <value in [disable, enable]>
           objcfg: <value in [disable, enable]>
           report: <value in [disable, enable]>
           rev: <value in [disable, enable]>
           rtmon: <value in [disable, enable]>
           scfw: <value in [disable, enable]>
           scply: <value in [disable, enable]>
           scrmgr: <value in [disable, enable]>
           scvpn: <value in [disable, enable]>
           system: <value in [disable, enable]>
           webport: <value in [disable, enable]>
           incident: <value in [disable, enable]>
           aid: <value in [disable, enable]>
           docker: <value in [disable, enable]>
```

## [Return Values](fmgr_system_locallog_syslogd_filter_module.md#id5)

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
