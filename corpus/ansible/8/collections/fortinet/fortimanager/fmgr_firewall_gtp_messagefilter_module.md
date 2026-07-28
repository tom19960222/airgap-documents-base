---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_gtp_messagefilter module – Message filter."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_gtp_messagefilter_module.html
fetched_at: 2026-07-28T02:11:58+00:00
---
# fortinet.fortimanager.fmgr_firewall_gtp_messagefilter module – Message filter.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_gtp_messagefilter`.

New in fortinet.fortimanager 2.2.0

- [Synopsis](fmgr_firewall_gtp_messagefilter_module.md#synopsis)
- [Parameters](fmgr_firewall_gtp_messagefilter_module.md#parameters)
- [Notes](fmgr_firewall_gtp_messagefilter_module.md#notes)
- [Examples](fmgr_firewall_gtp_messagefilter_module.md#examples)
- [Return Values](fmgr_firewall_gtp_messagefilter_module.md#return-values)

## [Synopsis](fmgr_firewall_gtp_messagefilter_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_gtp_messagefilter_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_gtp_messagefilter**  dictionary | the top level parameters set |
| **create-aa-pdp**  string | Create AA PDP.  **Choices:**   - `"allow"` - `"deny"` |
| **create-mbms**  string | Create MBMS.  **Choices:**   - `"allow"` - `"deny"` |
| **create-pdp**  string | Create PDP.  **Choices:**   - `"allow"` - `"deny"` |
| **data-record**  string | Data record.  **Choices:**   - `"allow"` - `"deny"` |
| **delete-aa-pdp**  string | Delete AA PDP.  **Choices:**   - `"allow"` - `"deny"` |
| **delete-mbms**  string | Delete MBMS.  **Choices:**   - `"allow"` - `"deny"` |
| **delete-pdp**  string | Delete PDP.  **Choices:**   - `"allow"` - `"deny"` |
| **echo**  string | Echo.  **Choices:**   - `"allow"` - `"deny"` |
| **error-indication**  string | Error indication.  **Choices:**   - `"allow"` - `"deny"` |
| **failure-report**  string | Failure report.  **Choices:**   - `"allow"` - `"deny"` |
| **fwd-relocation**  string | Forward relocation.  **Choices:**   - `"allow"` - `"deny"` |
| **fwd-srns-context**  string | Forward SRNS context.  **Choices:**   - `"allow"` - `"deny"` |
| **gtp-pdu**  string | GTP PDU.  **Choices:**   - `"allow"` - `"deny"` |
| **identification**  string | Identification.  **Choices:**   - `"allow"` - `"deny"` |
| **mbms-notification**  string | MBMS notification.  **Choices:**   - `"allow"` - `"deny"` |
| **node-alive**  string | Node alive.  **Choices:**   - `"allow"` - `"deny"` |
| **note-ms-present**  string | Note MS present.  **Choices:**   - `"allow"` - `"deny"` |
| **pdu-notification**  string | PDU notification.  **Choices:**   - `"allow"` - `"deny"` |
| **ran-info**  string | Ran info.  **Choices:**   - `"allow"` - `"deny"` |
| **redirection**  string | Redirection.  **Choices:**   - `"allow"` - `"deny"` |
| **relocation-cancel**  string | Relocation cancel.  **Choices:**   - `"allow"` - `"deny"` |
| **send-route**  string | Send route.  **Choices:**   - `"allow"` - `"deny"` |
| **sgsn-context**  string | SGSN context.  **Choices:**   - `"allow"` - `"deny"` |
| **support-extension**  string | Support extension.  **Choices:**   - `"allow"` - `"deny"` |
| **unknown-message-action**  string | Unknown message action.  **Choices:**   - `"allow"` - `"deny"` |
| **update-mbms**  string | Update MBMS.  **Choices:**   - `"allow"` - `"deny"` |
| **update-pdp**  string | Update PDP.  **Choices:**   - `"allow"` - `"deny"` |
| **version-not-support**  string | Version not supported.  **Choices:**   - `"allow"` - `"deny"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **gtp**  string / required | the parameter (gtp) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_gtp_messagefilter_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_gtp_messagefilter_module.md#id4)

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
    - name: Message filter.
      fmgr_firewall_gtp_messagefilter:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        gtp: <your own value>
        firewall_gtp_messagefilter:
          create-aa-pdp: <value in [allow, deny]>
          create-mbms: <value in [allow, deny]>
          create-pdp: <value in [allow, deny]>
          data-record: <value in [allow, deny]>
          delete-aa-pdp: <value in [allow, deny]>
          delete-mbms: <value in [allow, deny]>
          delete-pdp: <value in [allow, deny]>
          echo: <value in [allow, deny]>
          error-indication: <value in [allow, deny]>
          failure-report: <value in [allow, deny]>
          fwd-relocation: <value in [allow, deny]>
          fwd-srns-context: <value in [allow, deny]>
          gtp-pdu: <value in [allow, deny]>
          identification: <value in [allow, deny]>
          mbms-notification: <value in [allow, deny]>
          node-alive: <value in [allow, deny]>
          note-ms-present: <value in [allow, deny]>
          pdu-notification: <value in [allow, deny]>
          ran-info: <value in [allow, deny]>
          redirection: <value in [allow, deny]>
          relocation-cancel: <value in [allow, deny]>
          send-route: <value in [allow, deny]>
          sgsn-context: <value in [allow, deny]>
          support-extension: <value in [allow, deny]>
          unknown-message-action: <value in [allow, deny]>
          update-mbms: <value in [allow, deny]>
          update-pdp: <value in [allow, deny]>
          version-not-support: <value in [allow, deny]>
```

## [Return Values](fmgr_firewall_gtp_messagefilter_module.md#id5)

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
