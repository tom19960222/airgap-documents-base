---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_firewall_gtp_messageratelimit module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_firewall_gtp_messageratelimit_module.html
fetched_at: 2026-07-27T17:31:06+00:00
---
# fortinet.fortimanager.fmgr_firewall_gtp_messageratelimit module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_gtp_messageratelimit`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_gtp_messageratelimit_module.md#synopsis)
- [Parameters](fmgr_firewall_gtp_messageratelimit_module.md#parameters)
- [Notes](fmgr_firewall_gtp_messageratelimit_module.md#notes)
- [Examples](fmgr_firewall_gtp_messageratelimit_module.md#examples)
- [Return Values](fmgr_firewall_gtp_messageratelimit_module.md#return-values)

## [Synopsis](fmgr_firewall_gtp_messageratelimit_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_gtp_messageratelimit_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **firewall_gtp_messageratelimit**  dictionary | the top level parameters set |
| **create-aa-pdp-request**  integer | no description |
| **create-aa-pdp-response**  integer | no description |
| **create-mbms-request**  integer | no description |
| **create-mbms-response**  integer | no description |
| **create-pdp-request**  integer | no description |
| **create-pdp-response**  integer | no description |
| **delete-aa-pdp-request**  integer | no description |
| **delete-aa-pdp-response**  integer | no description |
| **delete-mbms-request**  integer | no description |
| **delete-mbms-response**  integer | no description |
| **delete-pdp-request**  integer | no description |
| **delete-pdp-response**  integer | no description |
| **echo-reponse**  integer | no description |
| **echo-request**  integer | no description |
| **error-indication**  integer | no description |
| **failure-report-request**  integer | no description |
| **failure-report-response**  integer | no description |
| **fwd-reloc-complete-ack**  integer | no description |
| **fwd-relocation-complete**  integer | no description |
| **fwd-relocation-request**  integer | no description |
| **fwd-relocation-response**  integer | no description |
| **fwd-srns-context**  integer | no description |
| **fwd-srns-context-ack**  integer | no description |
| **g-pdu**  integer | no description |
| **identification-request**  integer | no description |
| **identification-response**  integer | no description |
| **mbms-de-reg-request**  integer | no description |
| **mbms-de-reg-response**  integer | no description |
| **mbms-notify-rej-request**  integer | no description |
| **mbms-notify-rej-response**  integer | no description |
| **mbms-notify-request**  integer | no description |
| **mbms-notify-response**  integer | no description |
| **mbms-reg-request**  integer | no description |
| **mbms-reg-response**  integer | no description |
| **mbms-ses-start-request**  integer | no description |
| **mbms-ses-start-response**  integer | no description |
| **mbms-ses-stop-request**  integer | no description |
| **mbms-ses-stop-response**  integer | no description |
| **note-ms-request**  integer | no description |
| **note-ms-response**  integer | no description |
| **pdu-notify-rej-request**  integer | no description |
| **pdu-notify-rej-response**  integer | no description |
| **pdu-notify-request**  integer | no description |
| **pdu-notify-response**  integer | no description |
| **ran-info**  integer | no description |
| **relocation-cancel-request**  integer | no description |
| **relocation-cancel-response**  integer | no description |
| **send-route-request**  integer | no description |
| **send-route-response**  integer | no description |
| **sgsn-context-ack**  integer | no description |
| **sgsn-context-request**  integer | no description |
| **sgsn-context-response**  integer | no description |
| **support-ext-hdr-notify**  integer | no description |
| **update-mbms-request**  integer | no description |
| **update-mbms-response**  integer | no description |
| **update-pdp-request**  integer | no description |
| **update-pdp-response**  integer | no description |
| **version-not-support**  integer | no description |
| **gtp**  string / required | the parameter (gtp) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_firewall_gtp_messageratelimit_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_gtp_messageratelimit_module.md#id4)

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
     fmgr_firewall_gtp_messageratelimit:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        gtp: <your own value>
        firewall_gtp_messageratelimit:
           create-aa-pdp-request: <value of integer>
           create-aa-pdp-response: <value of integer>
           create-mbms-request: <value of integer>
           create-mbms-response: <value of integer>
           create-pdp-request: <value of integer>
           create-pdp-response: <value of integer>
           delete-aa-pdp-request: <value of integer>
           delete-aa-pdp-response: <value of integer>
           delete-mbms-request: <value of integer>
           delete-mbms-response: <value of integer>
           delete-pdp-request: <value of integer>
           delete-pdp-response: <value of integer>
           echo-reponse: <value of integer>
           echo-request: <value of integer>
           error-indication: <value of integer>
           failure-report-request: <value of integer>
           failure-report-response: <value of integer>
           fwd-reloc-complete-ack: <value of integer>
           fwd-relocation-complete: <value of integer>
           fwd-relocation-request: <value of integer>
           fwd-relocation-response: <value of integer>
           fwd-srns-context: <value of integer>
           fwd-srns-context-ack: <value of integer>
           g-pdu: <value of integer>
           identification-request: <value of integer>
           identification-response: <value of integer>
           mbms-de-reg-request: <value of integer>
           mbms-de-reg-response: <value of integer>
           mbms-notify-rej-request: <value of integer>
           mbms-notify-rej-response: <value of integer>
           mbms-notify-request: <value of integer>
           mbms-notify-response: <value of integer>
           mbms-reg-request: <value of integer>
           mbms-reg-response: <value of integer>
           mbms-ses-start-request: <value of integer>
           mbms-ses-start-response: <value of integer>
           mbms-ses-stop-request: <value of integer>
           mbms-ses-stop-response: <value of integer>
           note-ms-request: <value of integer>
           note-ms-response: <value of integer>
           pdu-notify-rej-request: <value of integer>
           pdu-notify-rej-response: <value of integer>
           pdu-notify-request: <value of integer>
           pdu-notify-response: <value of integer>
           ran-info: <value of integer>
           relocation-cancel-request: <value of integer>
           relocation-cancel-response: <value of integer>
           send-route-request: <value of integer>
           send-route-response: <value of integer>
           sgsn-context-ack: <value of integer>
           sgsn-context-request: <value of integer>
           sgsn-context-response: <value of integer>
           support-ext-hdr-notify: <value of integer>
           update-mbms-request: <value of integer>
           update-mbms-response: <value of integer>
           update-pdp-request: <value of integer>
           update-pdp-response: <value of integer>
           version-not-support: <value of integer>
```

## [Return Values](fmgr_firewall_gtp_messageratelimit_module.md#id5)

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
