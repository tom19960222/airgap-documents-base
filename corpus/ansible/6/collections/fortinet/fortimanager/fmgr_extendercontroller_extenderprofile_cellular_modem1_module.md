---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_extendercontroller_extenderprofile_cellular_modem1 module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_extendercontroller_extenderprofile_cellular_modem1_module.html
fetched_at: 2026-07-27T17:30:29+00:00
---
# fortinet.fortimanager.fmgr_extendercontroller_extenderprofile_cellular_modem1 module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_extendercontroller_extenderprofile_cellular_modem1`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_extendercontroller_extenderprofile_cellular_modem1_module.md#synopsis)
- [Parameters](fmgr_extendercontroller_extenderprofile_cellular_modem1_module.md#parameters)
- [Notes](fmgr_extendercontroller_extenderprofile_cellular_modem1_module.md#notes)
- [Examples](fmgr_extendercontroller_extenderprofile_cellular_modem1_module.md#examples)
- [Return Values](fmgr_extendercontroller_extenderprofile_cellular_modem1_module.md#return-values)

## [Synopsis](fmgr_extendercontroller_extenderprofile_cellular_modem1_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_extendercontroller_extenderprofile_cellular_modem1_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **extender-profile**  string / required | the parameter (extender-profile) in requested url |
| **extendercontroller_extenderprofile_cellular_modem1**  dictionary | the top level parameters set |
| **auto-switch**  dictionary | no description |
| **dataplan**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **disconnect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **disconnect-period**  integer | no description |
| **disconnect-threshold**  integer | no description |
| **signal**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switch-back**  list / elements=string | description  Choices:   - `"time"` - `"timer"` |
| **switch-back-time**  string | no description |
| **switch-back-timer**  integer | no description |
| **conn-status**  integer | no description |
| **default-sim**  string | no description  Choices:   - `"sim1"` - `"sim2"` - `"carrier"` - `"cost"` |
| **gps**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **modem-id**  integer | no description |
| **preferred-carrier**  string | no description |
| **redundant-intf**  string | no description |
| **redundant-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sim1-pin**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sim1-pin-code**  string | description |
| **sim2-pin**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sim2-pin-code**  string | description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_extendercontroller_extenderprofile_cellular_modem1_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_extendercontroller_extenderprofile_cellular_modem1_module.md#id4)

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
     fmgr_extendercontroller_extenderprofile_cellular_modem1:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        extender-profile: <your own value>
        extendercontroller_extenderprofile_cellular_modem1:
           auto-switch:
              dataplan: <value in [disable, enable]>
              disconnect: <value in [disable, enable]>
              disconnect-period: <value of integer>
              disconnect-threshold: <value of integer>
              signal: <value in [disable, enable]>
              switch-back:
                - time
                - timer
              switch-back-time: <value of string>
              switch-back-timer: <value of integer>
           conn-status: <value of integer>
           default-sim: <value in [sim1, sim2, carrier, ...]>
           gps: <value in [disable, enable]>
           modem-id: <value of integer>
           preferred-carrier: <value of string>
           redundant-intf: <value of string>
           redundant-mode: <value in [disable, enable]>
           sim1-pin: <value in [disable, enable]>
           sim1-pin-code: <value of string>
           sim2-pin: <value in [disable, enable]>
           sim2-pin-code: <value of string>
```

## [Return Values](fmgr_extendercontroller_extenderprofile_cellular_modem1_module.md#id5)

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
