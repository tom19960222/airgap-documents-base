---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_mmsprofile_notification module – Notification configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_mmsprofile_notification_module.html
fetched_at: 2026-07-28T02:12:23+00:00
---
# fortinet.fortimanager.fmgr_firewall_mmsprofile_notification module – Notification configuration.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_mmsprofile_notification`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_mmsprofile_notification**  dictionary | the top level parameters set |
| **alert-int**  integer | Alert notification send interval. |
| **alert-int-mode**  string | Alert notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **alert-src-msisdn**  string | Specify from address for alert messages. |
| **alert-status**  string | Alert notification status.  **Choices:**   - `"disable"` - `"enable"` |
| **bword-int**  integer | Banned word notification send interval. |
| **bword-int-mode**  string | Banned word notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **bword-status**  string | Banned word notification status.  **Choices:**   - `"disable"` - `"enable"` |
| **carrier-endpoint-bwl-int**  integer | Carrier end point black/white list notification send interval. |
| **carrier-endpoint-bwl-int-mode**  string | Carrier end point black/white list notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **carrier-endpoint-bwl-status**  string | Carrier end point black/white list notification status.  **Choices:**   - `"disable"` - `"enable"` |
| **days-allowed**  list / elements=string | no description  **Choices:**   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **detect-server**  string | Enable/disable automatic server address determination.  **Choices:**   - `"disable"` - `"enable"` |
| **dupe-int**  integer | Duplicate notification send interval. |
| **dupe-int-mode**  string | Duplicate notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **dupe-status**  string | Duplicate notification status.  **Choices:**   - `"disable"` - `"enable"` |
| **file-block-int**  integer | File block notification send interval. |
| **file-block-int-mode**  string | File block notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **file-block-status**  string | File block notification status.  **Choices:**   - `"disable"` - `"enable"` |
| **flood-int**  integer | Flood notification send interval. |
| **flood-int-mode**  string | Flood notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **flood-status**  string | Flood notification status.  **Choices:**   - `"disable"` - `"enable"` |
| **from-in-header**  string | Enable/disable insertion of from address in HTTP header.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-checksum-int**  integer | MMS checksum notification send interval. |
| **mms-checksum-int-mode**  string | MMS checksum notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **mms-checksum-status**  string | MMS checksum notification status.  **Choices:**   - `"disable"` - `"enable"` |
| **mmsc-hostname**  string | Host name or IP address of the MMSC. |
| **mmsc-password**  any | (list) no description |
| **mmsc-port**  integer | Port used on the MMSC for sending MMS messages |
| **mmsc-url**  string | URL used on the MMSC for sending MMS messages. |
| **mmsc-username**  string | User name required for authentication with the MMSC. |
| **msg-protocol**  string | Protocol to use for sending notification messages.  **Choices:**   - `"mm1"` - `"mm3"` - `"mm4"` - `"mm7"` |
| **msg-type**  string | MM7 message type.  **Choices:**   - `"submit-req"` - `"deliver-req"` |
| **protocol**  string | Protocol. |
| **rate-limit**  integer | Rate limit for sending notification messages |
| **tod-window-duration**  string | Time of day window duration. |
| **tod-window-end**  string | Obsolete. |
| **tod-window-start**  string | Time of day window start. |
| **user-domain**  string | Domain name to which the user addresses belong. |
| **vas-id**  string | VAS identifier. |
| **vasp-id**  string | VASP identifier. |
| **virus-int**  integer | Virus notification send interval. |
| **virus-int-mode**  string | Virus notification interval mode.  **Choices:**   - `"hours"` - `"minutes"` |
| **virus-status**  string | Virus notification status.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **mms-profile**  string / required | the parameter (mms-profile) in requested url |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
    - name: Notification configuration.
      fmgr_firewall_mmsprofile_notification:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        mms-profile: <your own value>
        firewall_mmsprofile_notification:
          alert-int: <integer>
          alert-int-mode: <value in [hours, minutes]>
          alert-src-msisdn: <string>
          alert-status: <value in [disable, enable]>
          bword-int: <integer>
          bword-int-mode: <value in [hours, minutes]>
          bword-status: <value in [disable, enable]>
          carrier-endpoint-bwl-int: <integer>
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
          dupe-int: <integer>
          dupe-int-mode: <value in [hours, minutes]>
          dupe-status: <value in [disable, enable]>
          file-block-int: <integer>
          file-block-int-mode: <value in [hours, minutes]>
          file-block-status: <value in [disable, enable]>
          flood-int: <integer>
          flood-int-mode: <value in [hours, minutes]>
          flood-status: <value in [disable, enable]>
          from-in-header: <value in [disable, enable]>
          mms-checksum-int: <integer>
          mms-checksum-int-mode: <value in [hours, minutes]>
          mms-checksum-status: <value in [disable, enable]>
          mmsc-hostname: <string>
          mmsc-password: <list or string>
          mmsc-port: <integer>
          mmsc-url: <string>
          mmsc-username: <string>
          msg-protocol: <value in [mm1, mm3, mm4, ...]>
          msg-type: <value in [submit-req, deliver-req]>
          protocol: <string>
          rate-limit: <integer>
          tod-window-duration: <string>
          tod-window-end: <string>
          tod-window-start: <string>
          user-domain: <string>
          vas-id: <string>
          vasp-id: <string>
          virus-int: <integer>
          virus-int-mode: <value in [hours, minutes]>
          virus-status: <value in [disable, enable]>
```

## [Return Values](fmgr_firewall_mmsprofile_notification_module.md#id5)

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
