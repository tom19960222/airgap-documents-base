---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_gtp_messageratelimit module – Message rate limiting."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_gtp_messageratelimit_module.html
fetched_at: 2026-07-28T02:11:59+00:00
---
# fortinet.fortimanager.fmgr_firewall_gtp_messageratelimit module – Message rate limiting.

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_gtp_messageratelimit`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_gtp_messageratelimit**  dictionary | the top level parameters set |
| **create-aa-pdp-request**  integer | Rate limit for create AA PDP context request |
| **create-aa-pdp-response**  integer | Rate limit for create AA PDP context response |
| **create-mbms-request**  integer | Rate limit for create MBMS context request |
| **create-mbms-response**  integer | Rate limit for create MBMS context response |
| **create-pdp-request**  integer | Rate limit for create PDP context request |
| **create-pdp-response**  integer | Rate limit for create PDP context response |
| **delete-aa-pdp-request**  integer | Rate limit for delete AA PDP context request |
| **delete-aa-pdp-response**  integer | Rate limit for delete AA PDP context response |
| **delete-mbms-request**  integer | Rate limit for delete MBMS context request |
| **delete-mbms-response**  integer | Rate limit for delete MBMS context response |
| **delete-pdp-request**  integer | Rate limit for delete PDP context request |
| **delete-pdp-response**  integer | Rate limit for delete PDP context response |
| **echo-reponse**  integer | Rate limit for echo response |
| **echo-request**  integer | Rate limit for echo requests |
| **error-indication**  integer | Rate limit for error indication |
| **failure-report-request**  integer | Rate limit for failure report request |
| **failure-report-response**  integer | Rate limit for failure report response |
| **fwd-reloc-complete-ack**  integer | Rate limit for forward relocation complete acknowledge |
| **fwd-relocation-complete**  integer | Rate limit for forward relocation complete |
| **fwd-relocation-request**  integer | Rate limit for forward relocation request |
| **fwd-relocation-response**  integer | Rate limit for forward relocation response |
| **fwd-srns-context**  integer | Rate limit for forward SRNS context |
| **fwd-srns-context-ack**  integer | Rate limit for forward SRNS context acknowledge |
| **g-pdu**  integer | Rate limit for G-PDU |
| **identification-request**  integer | Rate limit for identification request |
| **identification-response**  integer | Rate limit for identification response |
| **mbms-de-reg-request**  integer | Rate limit for MBMS de-registration request |
| **mbms-de-reg-response**  integer | Rate limit for MBMS de-registration response |
| **mbms-notify-rej-request**  integer | Rate limit for MBMS notification reject request |
| **mbms-notify-rej-response**  integer | Rate limit for MBMS notification reject response |
| **mbms-notify-request**  integer | Rate limit for MBMS notification request |
| **mbms-notify-response**  integer | Rate limit for MBMS notification response |
| **mbms-reg-request**  integer | Rate limit for MBMS registration request |
| **mbms-reg-response**  integer | Rate limit for MBMS registration response |
| **mbms-ses-start-request**  integer | Rate limit for MBMS session start request |
| **mbms-ses-start-response**  integer | Rate limit for MBMS session start response |
| **mbms-ses-stop-request**  integer | Rate limit for MBMS session stop request |
| **mbms-ses-stop-response**  integer | Rate limit for MBMS session stop response |
| **note-ms-request**  integer | Rate limit for note MS GPRS present request |
| **note-ms-response**  integer | Rate limit for note MS GPRS present response |
| **pdu-notify-rej-request**  integer | Rate limit for PDU notify reject request |
| **pdu-notify-rej-response**  integer | Rate limit for PDU notify reject response |
| **pdu-notify-request**  integer | Rate limit for PDU notify request |
| **pdu-notify-response**  integer | Rate limit for PDU notify response |
| **ran-info**  integer | Rate limit for RAN information relay |
| **relocation-cancel-request**  integer | Rate limit for relocation cancel request |
| **relocation-cancel-response**  integer | Rate limit for relocation cancel response |
| **send-route-request**  integer | Rate limit for send routing information for GPRS request |
| **send-route-response**  integer | Rate limit for send routing information for GPRS response |
| **sgsn-context-ack**  integer | Rate limit for SGSN context acknowledgement |
| **sgsn-context-request**  integer | Rate limit for SGSN context request |
| **sgsn-context-response**  integer | Rate limit for SGSN context response |
| **support-ext-hdr-notify**  integer | Rate limit for support extension headers notification |
| **update-mbms-request**  integer | Rate limit for update MBMS context request |
| **update-mbms-response**  integer | Rate limit for update MBMS context response |
| **update-pdp-request**  integer | Rate limit for update PDP context request |
| **update-pdp-response**  integer | Rate limit for update PDP context response |
| **version-not-support**  integer | Rate limit for version not supported |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **gtp**  string / required | the parameter (gtp) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
    - name: Message rate limiting.
      fmgr_firewall_gtp_messageratelimit:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        gtp: <your own value>
        firewall_gtp_messageratelimit:
          create-aa-pdp-request: <integer>
          create-aa-pdp-response: <integer>
          create-mbms-request: <integer>
          create-mbms-response: <integer>
          create-pdp-request: <integer>
          create-pdp-response: <integer>
          delete-aa-pdp-request: <integer>
          delete-aa-pdp-response: <integer>
          delete-mbms-request: <integer>
          delete-mbms-response: <integer>
          delete-pdp-request: <integer>
          delete-pdp-response: <integer>
          echo-reponse: <integer>
          echo-request: <integer>
          error-indication: <integer>
          failure-report-request: <integer>
          failure-report-response: <integer>
          fwd-reloc-complete-ack: <integer>
          fwd-relocation-complete: <integer>
          fwd-relocation-request: <integer>
          fwd-relocation-response: <integer>
          fwd-srns-context: <integer>
          fwd-srns-context-ack: <integer>
          g-pdu: <integer>
          identification-request: <integer>
          identification-response: <integer>
          mbms-de-reg-request: <integer>
          mbms-de-reg-response: <integer>
          mbms-notify-rej-request: <integer>
          mbms-notify-rej-response: <integer>
          mbms-notify-request: <integer>
          mbms-notify-response: <integer>
          mbms-reg-request: <integer>
          mbms-reg-response: <integer>
          mbms-ses-start-request: <integer>
          mbms-ses-start-response: <integer>
          mbms-ses-stop-request: <integer>
          mbms-ses-stop-response: <integer>
          note-ms-request: <integer>
          note-ms-response: <integer>
          pdu-notify-rej-request: <integer>
          pdu-notify-rej-response: <integer>
          pdu-notify-request: <integer>
          pdu-notify-response: <integer>
          ran-info: <integer>
          relocation-cancel-request: <integer>
          relocation-cancel-response: <integer>
          send-route-request: <integer>
          send-route-response: <integer>
          sgsn-context-ack: <integer>
          sgsn-context-request: <integer>
          sgsn-context-response: <integer>
          support-ext-hdr-notify: <integer>
          update-mbms-request: <integer>
          update-mbms-response: <integer>
          update-pdp-request: <integer>
          update-pdp-response: <integer>
          version-not-support: <integer>
```

## [Return Values](fmgr_firewall_gtp_messageratelimit_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
