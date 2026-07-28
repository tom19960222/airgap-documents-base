---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_widsprofile module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_widsprofile_module.html
fetched_at: 2026-07-27T17:39:39+00:00
---
# fortinet.fortimanager.fmgr_widsprofile module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_widsprofile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_widsprofile_module.md#synopsis)
- [Parameters](fmgr_widsprofile_module.md#parameters)
- [Notes](fmgr_widsprofile_module.md#notes)
- [Examples](fmgr_widsprofile_module.md#examples)
- [Return Values](fmgr_widsprofile_module.md#return-values)

## [Synopsis](fmgr_widsprofile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_widsprofile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **widsprofile**  dictionary | the top level parameters set |
| **ap-auto-suppress**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-bgscan-disable-day**  list / elements=string | no description  Choices:   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **ap-bgscan-disable-end**  string | no description |
| **ap-bgscan-disable-schedules**  string | no description |
| **ap-bgscan-disable-start**  string | no description |
| **ap-bgscan-duration**  integer | no description |
| **ap-bgscan-idle**  integer | no description |
| **ap-bgscan-intv**  integer | no description |
| **ap-bgscan-period**  integer | no description |
| **ap-bgscan-report-intv**  integer | no description |
| **ap-fgscan-report-intv**  integer | no description |
| **ap-scan**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-scan-passive**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ap-scan-threshold**  string | no description |
| **asleap-attack**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **assoc-flood-thresh**  integer | no description |
| **assoc-flood-time**  integer | no description |
| **assoc-frame-flood**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auth-flood-thresh**  integer | no description |
| **auth-flood-time**  integer | no description |
| **auth-frame-flood**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **comment**  string | no description |
| **deauth-broadcast**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **deauth-unknown-src-thresh**  integer | no description |
| **eapol-fail-flood**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **eapol-fail-intv**  integer | no description |
| **eapol-fail-thresh**  integer | no description |
| **eapol-logoff-flood**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **eapol-logoff-intv**  integer | no description |
| **eapol-logoff-thresh**  integer | no description |
| **eapol-pre-fail-flood**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **eapol-pre-fail-intv**  integer | no description |
| **eapol-pre-fail-thresh**  integer | no description |
| **eapol-pre-succ-flood**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **eapol-pre-succ-intv**  integer | no description |
| **eapol-pre-succ-thresh**  integer | no description |
| **eapol-start-flood**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **eapol-start-intv**  integer | no description |
| **eapol-start-thresh**  integer | no description |
| **eapol-succ-flood**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **eapol-succ-intv**  integer | no description |
| **eapol-succ-thresh**  integer | no description |
| **invalid-mac-oui**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **long-duration-attack**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **long-duration-thresh**  integer | no description |
| **name**  string | no description |
| **null-ssid-probe-resp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sensor-mode**  string | no description  Choices:   - `"disable"` - `"foreign"` - `"both"` |
| **spoofed-deauth**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **weak-wep-iv**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **wireless-bridge**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_widsprofile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_widsprofile_module.md#id4)

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
     fmgr_widsprofile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        widsprofile:
           ap-auto-suppress: <value in [disable, enable]>
           ap-bgscan-disable-day:
             - sunday
             - monday
             - tuesday
             - wednesday
             - thursday
             - friday
             - saturday
           ap-bgscan-disable-end: <value of string>
           ap-bgscan-disable-start: <value of string>
           ap-bgscan-duration: <value of integer>
           ap-bgscan-idle: <value of integer>
           ap-bgscan-intv: <value of integer>
           ap-bgscan-period: <value of integer>
           ap-bgscan-report-intv: <value of integer>
           ap-fgscan-report-intv: <value of integer>
           ap-scan: <value in [disable, enable]>
           ap-scan-passive: <value in [disable, enable]>
           asleap-attack: <value in [disable, enable]>
           assoc-flood-thresh: <value of integer>
           assoc-flood-time: <value of integer>
           assoc-frame-flood: <value in [disable, enable]>
           auth-flood-thresh: <value of integer>
           auth-flood-time: <value of integer>
           auth-frame-flood: <value in [disable, enable]>
           comment: <value of string>
           deauth-broadcast: <value in [disable, enable]>
           deauth-unknown-src-thresh: <value of integer>
           eapol-fail-flood: <value in [disable, enable]>
           eapol-fail-intv: <value of integer>
           eapol-fail-thresh: <value of integer>
           eapol-logoff-flood: <value in [disable, enable]>
           eapol-logoff-intv: <value of integer>
           eapol-logoff-thresh: <value of integer>
           eapol-pre-fail-flood: <value in [disable, enable]>
           eapol-pre-fail-intv: <value of integer>
           eapol-pre-fail-thresh: <value of integer>
           eapol-pre-succ-flood: <value in [disable, enable]>
           eapol-pre-succ-intv: <value of integer>
           eapol-pre-succ-thresh: <value of integer>
           eapol-start-flood: <value in [disable, enable]>
           eapol-start-intv: <value of integer>
           eapol-start-thresh: <value of integer>
           eapol-succ-flood: <value in [disable, enable]>
           eapol-succ-intv: <value of integer>
           eapol-succ-thresh: <value of integer>
           invalid-mac-oui: <value in [disable, enable]>
           long-duration-attack: <value in [disable, enable]>
           long-duration-thresh: <value of integer>
           name: <value of string>
           null-ssid-probe-resp: <value in [disable, enable]>
           sensor-mode: <value in [disable, foreign, both]>
           spoofed-deauth: <value in [disable, enable]>
           weak-wep-iv: <value in [disable, enable]>
           wireless-bridge: <value in [disable, enable]>
           ap-bgscan-disable-schedules: <value of string>
           ap-scan-threshold: <value of string>
```

## [Return Values](fmgr_widsprofile_module.md#id5)

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
