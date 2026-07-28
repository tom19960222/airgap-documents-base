---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_arrpprofile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_arrpprofile_module.html
fetched_at: 2026-07-27T17:28:34+00:00
---
# fortinet.fortimanager.fmgr_arrpprofile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_arrpprofile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_arrpprofile_module.md#synopsis)
- [Parameters](fmgr_arrpprofile_module.md#parameters)
- [Notes](fmgr_arrpprofile_module.md#notes)
- [Examples](fmgr_arrpprofile_module.md#examples)
- [Return Values](fmgr_arrpprofile_module.md#return-values)

## [Synopsis](fmgr_arrpprofile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_arrpprofile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **arrpprofile**  dictionary | the top level parameters set |
| **comment**  string | no description |
| **darrp-optimize**  integer | no description |
| **darrp-optimize-schedules**  string | description |
| **include-dfs-channel**  string | no description  Choices:   - `"no"` - `"disable"` - `"yes"` - `"enable"` |
| **include-weather-channel**  string | no description  Choices:   - `"no"` - `"disable"` - `"yes"` - `"enable"` |
| **monitor-period**  integer | no description |
| **name**  string | no description |
| **override-darrp-optimize**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **selection-period**  integer | no description |
| **threshold-ap**  integer | no description |
| **threshold-channel-load**  integer | no description |
| **threshold-noise-floor**  string | no description |
| **threshold-rx-errors**  integer | no description |
| **threshold-spectral-rssi**  string | no description |
| **threshold-tx-retries**  integer | no description |
| **weight-channel-load**  integer | no description |
| **weight-dfs-channel**  integer | no description |
| **weight-managed-ap**  integer | no description |
| **weight-noise-floor**  integer | no description |
| **weight-rogue-ap**  integer | no description |
| **weight-spectral-rssi**  integer | no description |
| **weight-weather-channel**  integer | no description |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_arrpprofile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_arrpprofile_module.md#id4)

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
     fmgr_arrpprofile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        arrpprofile:
           comment: <value of string>
           darrp-optimize: <value of integer>
           darrp-optimize-schedules: <value of string>
           include-dfs-channel: <value in [no, disable, yes, ...]>
           include-weather-channel: <value in [no, disable, yes, ...]>
           monitor-period: <value of integer>
           name: <value of string>
           override-darrp-optimize: <value in [disable, enable]>
           selection-period: <value of integer>
           threshold-ap: <value of integer>
           threshold-channel-load: <value of integer>
           threshold-noise-floor: <value of string>
           threshold-rx-errors: <value of integer>
           threshold-spectral-rssi: <value of string>
           threshold-tx-retries: <value of integer>
           weight-channel-load: <value of integer>
           weight-dfs-channel: <value of integer>
           weight-managed-ap: <value of integer>
           weight-noise-floor: <value of integer>
           weight-rogue-ap: <value of integer>
           weight-spectral-rssi: <value of integer>
           weight-weather-channel: <value of integer>
```

## [Return Values](fmgr_arrpprofile_module.md#id5)

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
