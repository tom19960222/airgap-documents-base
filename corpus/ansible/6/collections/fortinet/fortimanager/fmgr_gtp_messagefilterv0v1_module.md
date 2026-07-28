---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_gtp_messagefilterv0v1 module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_gtp_messagefilterv0v1_module.html
fetched_at: 2026-07-27T17:33:03+00:00
---
# fortinet.fortimanager.fmgr_gtp_messagefilterv0v1 module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_gtp_messagefilterv0v1`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_gtp_messagefilterv0v1_module.md#synopsis)
- [Parameters](fmgr_gtp_messagefilterv0v1_module.md#parameters)
- [Notes](fmgr_gtp_messagefilterv0v1_module.md#notes)
- [Examples](fmgr_gtp_messagefilterv0v1_module.md#examples)
- [Return Values](fmgr_gtp_messagefilterv0v1_module.md#return-values)

## [Synopsis](fmgr_gtp_messagefilterv0v1_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_gtp_messagefilterv0v1_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **gtp_messagefilterv0v1**  dictionary | the top level parameters set |
| **create-mbms**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **create-pdp**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **data-record**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **delete-aa-pdp**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **delete-mbms**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **delete-pdp**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **echo**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **end-marker**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **error-indication**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **failure-report**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **fwd-relocation**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **fwd-srns-context**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **gtp-pdu**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **identification**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **mbms-de-registration**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **mbms-notification**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **mbms-registration**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **mbms-session-start**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **mbms-session-stop**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **mbms-session-update**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **ms-info-change-notif**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **name**  string | no description |
| **node-alive**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **note-ms-present**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **pdu-notification**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **ran-info**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **redirection**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **relocation-cancel**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **send-route**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **sgsn-context**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **support-extension**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **unknown-message**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **unknown-message-white-list**  integer | no description |
| **update-mbms**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **update-pdp**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **v0-create-aa-pdp–v1-init-pdp-ctx**  string | no description  Choices:   - `"deny"` - `"allow"` |
| **version-not-support**  string | no description  Choices:   - `"allow"` - `"deny"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_gtp_messagefilterv0v1_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_gtp_messagefilterv0v1_module.md#id4)

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
     fmgr_gtp_messagefilterv0v1:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        gtp_messagefilterv0v1:
           create-mbms: <value in [allow, deny]>
           create-pdp: <value in [allow, deny]>
           data-record: <value in [allow, deny]>
           delete-aa-pdp: <value in [allow, deny]>
           delete-mbms: <value in [allow, deny]>
           delete-pdp: <value in [allow, deny]>
           echo: <value in [allow, deny]>
           end-marker: <value in [allow, deny]>
           error-indication: <value in [allow, deny]>
           failure-report: <value in [allow, deny]>
           fwd-relocation: <value in [allow, deny]>
           fwd-srns-context: <value in [allow, deny]>
           gtp-pdu: <value in [allow, deny]>
           identification: <value in [allow, deny]>
           mbms-de-registration: <value in [allow, deny]>
           mbms-notification: <value in [allow, deny]>
           mbms-registration: <value in [allow, deny]>
           mbms-session-start: <value in [allow, deny]>
           mbms-session-stop: <value in [allow, deny]>
           mbms-session-update: <value in [allow, deny]>
           ms-info-change-notif: <value in [allow, deny]>
           name: <value of string>
           node-alive: <value in [allow, deny]>
           note-ms-present: <value in [allow, deny]>
           pdu-notification: <value in [allow, deny]>
           ran-info: <value in [allow, deny]>
           redirection: <value in [allow, deny]>
           relocation-cancel: <value in [allow, deny]>
           send-route: <value in [allow, deny]>
           sgsn-context: <value in [allow, deny]>
           support-extension: <value in [allow, deny]>
           unknown-message: <value in [allow, deny]>
           unknown-message-white-list: <value of integer>
           update-mbms: <value in [allow, deny]>
           update-pdp: <value in [allow, deny]>
           v0-create-aa-pdp--v1-init-pdp-ctx: <value in [deny, allow]>
           version-not-support: <value in [allow, deny]>
```

## [Return Values](fmgr_gtp_messagefilterv0v1_module.md#id5)

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
