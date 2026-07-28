---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_wtpprofile_lbs module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_wtpprofile_lbs_module.html
fetched_at: 2026-07-27T17:39:43+00:00
---
# fortinet.fortimanager.fmgr_wtpprofile_lbs module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_wtpprofile_lbs`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_wtpprofile_lbs_module.md#synopsis)
- [Parameters](fmgr_wtpprofile_lbs_module.md#parameters)
- [Notes](fmgr_wtpprofile_lbs_module.md#notes)
- [Examples](fmgr_wtpprofile_lbs_module.md#examples)
- [Return Values](fmgr_wtpprofile_lbs_module.md#return-values)

## [Synopsis](fmgr_wtpprofile_lbs_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_wtpprofile_lbs_module.md#id2)

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
| **wtpprofile_lbs**  dictionary | the top level parameters set |
| **aeroscout**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **aeroscout-ap-mac**  string | no description  Choices:   - `"bssid"` - `"board-mac"` |
| **aeroscout-mmu-report**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **aeroscout-mu**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **aeroscout-mu-factor**  integer | no description |
| **aeroscout-mu-timeout**  integer | no description |
| **aeroscout-server-ip**  string | no description |
| **aeroscout-server-port**  integer | no description |
| **ekahau-blink-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ekahau-tag**  string | no description |
| **erc-server-ip**  string | no description |
| **erc-server-port**  integer | no description |
| **fortipresence**  string | no description  Choices:   - `"disable"` - `"enable"` - `"enable2"` - `"foreign"` - `"both"` |
| **fortipresence-ble**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fortipresence-frequency**  integer | no description |
| **fortipresence-port**  integer | no description |
| **fortipresence-project**  string | no description |
| **fortipresence-rogue**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fortipresence-secret**  string | description |
| **fortipresence-server**  string | no description |
| **fortipresence-server-addr-type**  string | no description  Choices:   - `"fqdn"` - `"ipv4"` |
| **fortipresence-server-fqdn**  string | no description |
| **fortipresence-unassoc**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **station-locate**  string | no description  Choices:   - `"disable"` - `"enable"` |

## [Notes](fmgr_wtpprofile_lbs_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_wtpprofile_lbs_module.md#id4)

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
     fmgr_wtpprofile_lbs:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        wtp-profile: <your own value>
        wtpprofile_lbs:
           aeroscout: <value in [disable, enable]>
           aeroscout-ap-mac: <value in [bssid, board-mac]>
           aeroscout-mmu-report: <value in [disable, enable]>
           aeroscout-mu: <value in [disable, enable]>
           aeroscout-mu-factor: <value of integer>
           aeroscout-mu-timeout: <value of integer>
           aeroscout-server-ip: <value of string>
           aeroscout-server-port: <value of integer>
           ekahau-blink-mode: <value in [disable, enable]>
           ekahau-tag: <value of string>
           erc-server-ip: <value of string>
           erc-server-port: <value of integer>
           fortipresence: <value in [disable, enable, enable2, ...]>
           fortipresence-frequency: <value of integer>
           fortipresence-port: <value of integer>
           fortipresence-project: <value of string>
           fortipresence-rogue: <value in [disable, enable]>
           fortipresence-secret: <value of string>
           fortipresence-server: <value of string>
           fortipresence-unassoc: <value in [disable, enable]>
           station-locate: <value in [disable, enable]>
           fortipresence-ble: <value in [disable, enable]>
           fortipresence-server-addr-type: <value in [fqdn, ipv4]>
           fortipresence-server-fqdn: <value of string>
```

## [Return Values](fmgr_wtpprofile_lbs_module.md#id5)

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
