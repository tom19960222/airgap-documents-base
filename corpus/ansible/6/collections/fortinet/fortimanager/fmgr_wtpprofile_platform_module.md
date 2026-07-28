---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_wtpprofile_platform module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_wtpprofile_platform_module.html
fetched_at: 2026-07-27T17:39:43+00:00
---
# fortinet.fortimanager.fmgr_wtpprofile_platform module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_wtpprofile_platform`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_wtpprofile_platform_module.md#synopsis)
- [Parameters](fmgr_wtpprofile_platform_module.md#parameters)
- [Notes](fmgr_wtpprofile_platform_module.md#notes)
- [Examples](fmgr_wtpprofile_platform_module.md#examples)
- [Return Values](fmgr_wtpprofile_platform_module.md#return-values)

## [Synopsis](fmgr_wtpprofile_platform_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_wtpprofile_platform_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |
| **wtp-profile**  string / required | the parameter (wtp-profile) in requested url |
| **wtpprofile_platform**  dictionary | the top level parameters set |
| **_local_platform_str**  string | no description |
| **ddscan**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mode**  string | no description  Choices:   - `"dual-5G"` - `"single-5G"` |
| **type**  string | no description  Choices:   - `"30B-50B"` - `"60B"` - `"80CM-81CM"` - `"220A"` - `"220B"` - `"210B"` - `"60C"` - `"222B"` - `"112B"` - `"320B"` - `"11C"` - `"14C"` - `"223B"` - `"28C"` - `"320C"` - `"221C"` - `"25D"` - `"222C"` - `"224D"` - `"214B"` - `"21D"` - `"24D"` - `"112D"` - `"223C"` - `"321C"` - `"C220C"` - `"C225C"` - `"S321C"` - `"S323C"` - `"FWF"` - `"S311C"` - `"S313C"` - `"AP-11N"` - `"S322C"` - `"S321CR"` - `"S322CR"` - `"S323CR"` - `"S421E"` - `"S422E"` - `"S423E"` - `"421E"` - `"423E"` - `"C221E"` - `"C226E"` - `"C23JD"` - `"C24JE"` - `"C21D"` - `"U421E"` - `"U423E"` - `"221E"` - `"222E"` - `"223E"` - `"S221E"` - `"S223E"` - `"U221EV"` - `"U223EV"` - `"U321EV"` - `"U323EV"` - `"224E"` - `"U422EV"` - `"U24JEV"` - `"321E"` - `"U431F"` - `"U433F"` - `"231E"` - `"431F"` - `"433F"` - `"231F"` - `"432F"` - `"234F"` - `"23JF"` - `"U231F"` - `"831F"` - `"U234F"` - `"U432F"` |

## [Notes](fmgr_wtpprofile_platform_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_wtpprofile_platform_module.md#id4)

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
     fmgr_wtpprofile_platform:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        wtp-profile: <your own value>
        wtpprofile_platform:
           type: <value in [30B-50B, 60B, 80CM-81CM, ...]>
           mode: <value in [dual-5G, single-5G]>
           ddscan: <value in [disable, enable]>
           _local_platform_str: <value of string>
```

## [Return Values](fmgr_wtpprofile_platform_module.md#id5)

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
