---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_system_dm module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_system_dm_module.html
fetched_at: 2026-07-27T17:36:00+00:00
---
# fortinet.fortimanager.fmgr_system_dm module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_dm`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_system_dm_module.md#synopsis)
- [Parameters](fmgr_system_dm_module.md#parameters)
- [Notes](fmgr_system_dm_module.md#notes)
- [Examples](fmgr_system_dm_module.md#examples)
- [Return Values](fmgr_system_dm_module.md#return-values)

## [Synopsis](fmgr_system_dm_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_dm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **system_dm**  dictionary | the top level parameters set |
| **concurrent-install-image-limit**  integer | no description  Default: `500` |
| **concurrent-install-limit**  integer | no description  Default: `480` |
| **concurrent-install-script-limit**  integer | no description  Default: `480` |
| **conf-merge-after-script**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **discover-timeout**  integer | no description  Default: `6` |
| **dpm-logsize**  integer | no description  Default: `10000` |
| **fgfm-install-refresh-count**  integer | no description  Default: `10` |
| **fgfm-sock-timeout**  integer | no description  Default: `360` |
| **fgfm_keepalive_itvl**  integer | no description  Default: `120` |
| **force-remote-diff**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **fortiap-refresh-cnt**  integer | no description  Default: `500` |
| **fortiap-refresh-itvl**  integer | no description  Default: `10` |
| **fortiext-refresh-cnt**  integer | no description  Default: `50` |
| **install-image-timeout**  integer | no description  Default: `3600` |
| **install-tunnel-retry-itvl**  integer | no description  Default: `60` |
| **max-revs**  integer | no description  Default: `100` |
| **nr-retry**  integer | no description  Default: `1` |
| **retry**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **retry-intvl**  integer | no description  Default: `15` |
| **rollback-allow-reboot**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **script-logsize**  integer | no description  Default: `100` |
| **skip-scep-check**  string | no description  no description  no description  Choices:   - `"disable"` ← (default) - `"enable"` |
| **skip-tunnel-fcp-req**  string | no description  no description  no description  Choices:   - `"disable"` - `"enable"` ← (default) |
| **verify-install**  string | no description  no description  no description  no description  Choices:   - `"disable"` - `"optimal"` - `"enable"` ← (default) |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_system_dm_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_dm_module.md#id4)

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
     fmgr_system_dm:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_dm:
           concurrent-install-image-limit: <value of integer>
           concurrent-install-limit: <value of integer>
           concurrent-install-script-limit: <value of integer>
           discover-timeout: <value of integer>
           dpm-logsize: <value of integer>
           fgfm-sock-timeout: <value of integer>
           fgfm_keepalive_itvl: <value of integer>
           force-remote-diff: <value in [disable, enable]>
           fortiap-refresh-cnt: <value of integer>
           fortiap-refresh-itvl: <value of integer>
           fortiext-refresh-cnt: <value of integer>
           install-image-timeout: <value of integer>
           install-tunnel-retry-itvl: <value of integer>
           max-revs: <value of integer>
           nr-retry: <value of integer>
           retry: <value in [disable, enable]>
           retry-intvl: <value of integer>
           rollback-allow-reboot: <value in [disable, enable]>
           script-logsize: <value of integer>
           skip-scep-check: <value in [disable, enable]>
           skip-tunnel-fcp-req: <value in [disable, enable]>
           verify-install: <value in [disable, optimal, enable]>
           fgfm-install-refresh-count: <value of integer>
           conf-merge-after-script: <value in [disable, enable]>
```

## [Return Values](fmgr_system_dm_module.md#id5)

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
