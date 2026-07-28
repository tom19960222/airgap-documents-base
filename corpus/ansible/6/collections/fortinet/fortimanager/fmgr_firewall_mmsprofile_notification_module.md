---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_firewall_mmsprofile_notification module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_firewall_mmsprofile_notification_module.html
fetched_at: 2026-07-27T17:31:27+00:00
---
# fortinet.fortimanager.fmgr_firewall_mmsprofile_notification module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_mmsprofile_notification`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_mmsprofile_notification_module.md#synopsis)
- [Parameters](fmgr_firewall_mmsprofile_notification_module.md#parameters)
- [Notes](fmgr_firewall_mmsprofile_notification_module.md#notes)
- [Examples](fmgr_firewall_mmsprofile_notification_module.md#examples)
- [Return Values](fmgr_firewall_mmsprofile_notification_module.md#return-values)

## [Synopsis](fmgr_firewall_mmsprofile_notification_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_mmsprofile_notification_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **firewall_mmsprofile_notification**  dictionary | the top level parameters set |
| **alert-int**  integer | no description |
| **alert-int-mode**  string | no description  Choices:   - `"hours"` - `"minutes"` |
| **alert-src-msisdn**  string | no description |
| **alert-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **bword-int**  integer | no description |
| **bword-int-mode**  string | no description  Choices:   - `"hours"` - `"minutes"` |
| **bword-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **carrier-endpoint-bwl-int**  integer | no description |
| **carrier-endpoint-bwl-int-mode**  string | no description  Choices:   - `"hours"` - `"minutes"` |
| **carrier-endpoint-bwl-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **days-allowed**  list / elements=string | description  Choices:   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **detect-server**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dupe-int**  integer | no description |
| **dupe-int-mode**  string | no description  Choices:   - `"hours"` - `"minutes"` |
| **dupe-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **file-block-int**  integer | no description |
| **file-block-int-mode**  string | no description  Choices:   - `"hours"` - `"minutes"` |
| **file-block-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **flood-int**  integer | no description |
| **flood-int-mode**  string | no description  Choices:   - `"hours"` - `"minutes"` |
| **flood-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **from-in-header**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-checksum-int**  integer | no description |
| **mms-checksum-int-mode**  string | no description  Choices:   - `"hours"` - `"minutes"` |
| **mms-checksum-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mmsc-hostname**  string | no description |
| **mmsc-password**  string | description |
| **mmsc-port**  integer | no description |
| **mmsc-url**  string | no description |
| **mmsc-username**  string | no description |
| **msg-protocol**  string | no description  Choices:   - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **msg-type**  string | no description  Choices:   - `"submit-req"` - `"deliver-req"` |
| **protocol**  string | no description |
| **rate-limit**  integer | no description |
| **tod-window-duration**  string | no description |
| **tod-window-end**  string | no description |
| **tod-window-start**  string | no description |
| **user-domain**  string | no description |
| **vas-id**  string | no description |
| **vasp-id**  string | no description |
| **virus-int**  integer | no description |
| **virus-int-mode**  string | no description  Choices:   - `"hours"` - `"minutes"` |
| **virus-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mms-profile**  string / required | the parameter (mms-profile) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_firewall_mmsprofile_notification_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_mmsprofile_notification_module.md#id4)

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
     fmgr_firewall_mmsprofile_notification:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        mms-profile: <your own value>
        firewall_mmsprofile_notification:
           alert-int: <value of integer>
           alert-int-mode: <value in [hours, minutes]>
           alert-src-msisdn: <value of string>
           alert-status: <value in [disable, enable]>
           bword-int: <value of integer>
           bword-int-mode: <value in [hours, minutes]>
           bword-status: <value in [disable, enable]>
           carrier-endpoint-bwl-int: <value of integer>
           carrier-endpoint-bwl-int-mode: <value in [hours, minutes]>
           carrier-endpoint-bwl-status: <value in [disable, enable]>
           days-allowed:
             - sunday
             - monday
             - tuesday
             - wednesday
             - thursday
             - friday
             - saturday
           detect-server: <value in [disable, enable]>
           dupe-int: <value of integer>
           dupe-int-mode: <value in [hours, minutes]>
           dupe-status: <value in [disable, enable]>
           file-block-int: <value of integer>
           file-block-int-mode: <value in [hours, minutes]>
           file-block-status: <value in [disable, enable]>
           flood-int: <value of integer>
           flood-int-mode: <value in [hours, minutes]>
           flood-status: <value in [disable, enable]>
           from-in-header: <value in [disable, enable]>
           mms-checksum-int: <value of integer>
           mms-checksum-int-mode: <value in [hours, minutes]>
           mms-checksum-status: <value in [disable, enable]>
           mmsc-hostname: <value of string>
           mmsc-password: <value of string>
           mmsc-port: <value of integer>
           mmsc-url: <value of string>
           mmsc-username: <value of string>
           msg-protocol: <value in [mm1, mm3, mm4, ...]>
           msg-type: <value in [submit-req, deliver-req]>
           protocol: <value of string>
           rate-limit: <value of integer>
           tod-window-duration: <value of string>
           tod-window-end: <value of string>
           tod-window-start: <value of string>
           user-domain: <value of string>
           vas-id: <value of string>
           vasp-id: <value of string>
           virus-int: <value of integer>
           virus-int-mode: <value in [hours, minutes]>
           virus-status: <value in [disable, enable]>
```

## [Return Values](fmgr_firewall_mmsprofile_notification_module.md#id5)

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
