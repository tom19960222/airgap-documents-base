---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_devprof_log_fortianalyzer_setting module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_devprof_log_fortianalyzer_setting_module.html
fetched_at: 2026-07-27T17:28:45+00:00
---
# fortinet.fortimanager.fmgr_devprof_log_fortianalyzer_setting module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_devprof_log_fortianalyzer_setting`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_devprof_log_fortianalyzer_setting_module.md#synopsis)
- [Parameters](fmgr_devprof_log_fortianalyzer_setting_module.md#parameters)
- [Notes](fmgr_devprof_log_fortianalyzer_setting_module.md#notes)
- [Examples](fmgr_devprof_log_fortianalyzer_setting_module.md#examples)
- [Return Values](fmgr_devprof_log_fortianalyzer_setting_module.md#return-values)

## [Synopsis](fmgr_devprof_log_fortianalyzer_setting_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_devprof_log_fortianalyzer_setting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **devprof**  string / required | the parameter (devprof) in requested url |
| **devprof_log_fortianalyzer_setting**  dictionary | the top level parameters set |
| **access-config**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **certificate**  string | no description |
| **certificate-verification**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **conn-timeout**  integer | no description |
| **enc-algorithm**  string | no description  Choices:   - `"default"` - `"high"` - `"low"` - `"disable"` - `"high-medium"` - `"low-medium"` |
| **hmac-algorithm**  string | no description  Choices:   - `"sha256"` - `"sha1"` |
| **interface**  string | no description |
| **interface-select-method**  string | no description  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **ips-archive**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **max-log-rate**  integer | no description |
| **monitor-failure-retry-period**  integer | no description |
| **monitor-keepalive-period**  integer | no description |
| **preshared-key**  string | no description |
| **priority**  string | no description  Choices:   - `"low"` - `"default"` |
| **reliable**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ssl-min-proto-version**  string | no description  Choices:   - `"default"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"SSLv3"` - `"TLSv1-3"` |
| **upload-day**  string | no description |
| **upload-interval**  string | no description  Choices:   - `"daily"` - `"weekly"` - `"monthly"` |
| **upload-option**  string | no description  Choices:   - `"store-and-upload"` - `"realtime"` - `"1-minute"` - `"5-minute"` |
| **upload-time**  string | no description |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_devprof_log_fortianalyzer_setting_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_devprof_log_fortianalyzer_setting_module.md#id4)

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
     fmgr_devprof_log_fortianalyzer_setting:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        devprof: <your own value>
        devprof_log_fortianalyzer_setting:
           certificate: <value of string>
           conn-timeout: <value of integer>
           enc-algorithm: <value in [default, high, low, ...]>
           hmac-algorithm: <value in [sha256, sha1]>
           ips-archive: <value in [disable, enable]>
           monitor-failure-retry-period: <value of integer>
           monitor-keepalive-period: <value of integer>
           reliable: <value in [disable, enable]>
           ssl-min-proto-version: <value in [default, TLSv1, TLSv1-1, ...]>
           upload-day: <value of string>
           upload-interval: <value in [daily, weekly, monthly]>
           upload-option: <value in [store-and-upload, realtime, 1-minute, ...]>
           upload-time: <value of string>
           access-config: <value in [disable, enable]>
           certificate-verification: <value in [disable, enable]>
           max-log-rate: <value of integer>
           priority: <value in [low, default]>
           interface: <value of string>
           interface-select-method: <value in [auto, sdwan, specify]>
           preshared-key: <value of string>
```

## [Return Values](fmgr_devprof_log_fortianalyzer_setting_module.md#id5)

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
