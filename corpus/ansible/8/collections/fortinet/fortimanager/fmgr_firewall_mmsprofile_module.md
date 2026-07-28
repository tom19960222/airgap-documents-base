---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_mmsprofile module – Configure MMS profiles."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_mmsprofile_module.html
fetched_at: 2026-07-28T02:12:21+00:00
---
# fortinet.fortimanager.fmgr_firewall_mmsprofile module – Configure MMS profiles.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_mmsprofile`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_firewall_mmsprofile_module.md#synopsis)
- [Parameters](fmgr_firewall_mmsprofile_module.md#parameters)
- [Notes](fmgr_firewall_mmsprofile_module.md#notes)
- [Examples](fmgr_firewall_mmsprofile_module.md#examples)
- [Return Values](fmgr_firewall_mmsprofile_module.md#return-values)

## [Synopsis](fmgr_firewall_mmsprofile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_mmsprofile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_mmsprofile**  dictionary | the top level parameters set |
| **avnotificationtable**  string | AntiVirus notification table ID. |
| **bwordtable**  string | MMS banned word table ID. |
| **carrier-endpoint-prefix**  string | Enable/disable prefixing of end point values.  **Choices:**   - `"disable"` - `"enable"` |
| **carrier-endpoint-prefix-range-max**  integer | Maximum length of end point value that can be prefixed |
| **carrier-endpoint-prefix-range-min**  integer | Minimum end point length to be prefixed |
| **carrier-endpoint-prefix-string**  string | String with which to prefix End point values. |
| **carrierendpointbwltable**  string | Carrier end point filter table ID. |
| **comment**  string | Comment. |
| **dupe**  dictionary | no description |
| **action1**  list / elements=string | no description  **Choices:**   - `"log"` - `"archive"` - `"intercept"` - `"block"` - `"archive-first"` - `"alert-notif"` |
| **action2**  list / elements=string | no description  **Choices:**   - `"log"` - `"archive"` - `"intercept"` - `"block"` - `"archive-first"` - `"alert-notif"` |
| **action3**  list / elements=string | no description  **Choices:**   - `"log"` - `"archive"` - `"intercept"` - `"block"` - `"archive-first"` - `"alert-notif"` |
| **block-time1**  integer | Duration for which action takes effect |
| **block-time2**  integer | Duration for which action takes effect |
| **block-time3**  integer | Duration action takes effect |
| **limit1**  integer | Maximum number of messages allowed. |
| **limit2**  integer | Maximum number of messages allowed. |
| **limit3**  integer | Maximum number of messages allowed. |
| **protocol**  string | Protocol. |
| **status1**  string | Enable/disable status1 detection.  **Choices:**   - `"disable"` - `"enable"` |
| **status2**  string | Enable/disable status2 detection.  **Choices:**   - `"disable"` - `"enable"` |
| **status3**  string | Enable/disable status3 detection.  **Choices:**   - `"disable"` - `"enable"` |
| **window1**  integer | Window to count messages over |
| **window2**  integer | Window to count messages over |
| **window3**  integer | Window to count messages over |
| **flood**  dictionary | no description |
| **action1**  list / elements=string | no description  **Choices:**   - `"log"` - `"archive"` - `"intercept"` - `"block"` - `"archive-first"` - `"alert-notif"` |
| **action2**  list / elements=string | no description  **Choices:**   - `"log"` - `"archive"` - `"intercept"` - `"block"` - `"archive-first"` - `"alert-notif"` |
| **action3**  list / elements=string | no description  **Choices:**   - `"log"` - `"archive"` - `"intercept"` - `"block"` - `"archive-first"` - `"alert-notif"` |
| **block-time1**  integer | Duration for which action takes effect |
| **block-time2**  integer | Duration for which action takes effect |
| **block-time3**  integer | Duration action takes effect |
| **limit1**  integer | Maximum number of messages allowed. |
| **limit2**  integer | Maximum number of messages allowed. |
| **limit3**  integer | Maximum number of messages allowed. |
| **protocol**  string | Protocol. |
| **status1**  string | Enable/disable status1 detection.  **Choices:**   - `"disable"` - `"enable"` |
| **status2**  string | Enable/disable status2 detection.  **Choices:**   - `"disable"` - `"enable"` |
| **status3**  string | Enable/disable status3 detection.  **Choices:**   - `"disable"` - `"enable"` |
| **window1**  integer | Window to count messages over |
| **window2**  integer | Window to count messages over |
| **window3**  integer | Window to count messages over |
| **mm1**  list / elements=string | MM1 options.  **Choices:**   - `"avmonitor"` - `"block"` - `"oversize"` - `"quarantine"` - `"scan"` - `"avquery"` - `"bannedword"` - `"no-content-summary"` - `"archive-summary"` - `"archive-full"` - `"carrier-endpoint-bwl"` - `"remove-blocked"` - `"chunkedbypass"` - `"clientcomfort"` - `"servercomfort"` - `"strict-file"` - `"mms-checksum"` |
| **mm1-addr-hdr**  string | HTTP header field |
| **mm1-addr-source**  string | Source for MM1 user address.  **Choices:**   - `"http-header"` - `"cookie"` |
| **mm1-convert-hex**  string | Enable/disable converting user address from HEX string for MM1.  **Choices:**   - `"disable"` - `"enable"` |
| **mm1-outbreak-prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **mm1-retr-dupe**  string | Enable/disable duplicate scanning of MM1 retr.  **Choices:**   - `"disable"` - `"enable"` |
| **mm1-retrieve-scan**  string | Enable/disable scanning on MM1 retrieve configuration messages.  **Choices:**   - `"disable"` - `"enable"` |
| **mm1comfortamount**  integer | MM1 comfort amount |
| **mm1comfortinterval**  integer | MM1 comfort interval |
| **mm1oversizelimit**  integer | Maximum file size to scan |
| **mm3**  list / elements=string | MM3 options.  **Choices:**   - `"avmonitor"` - `"block"` - `"oversize"` - `"quarantine"` - `"scan"` - `"avquery"` - `"bannedword"` - `"no-content-summary"` - `"archive-summary"` - `"archive-full"` - `"carrier-endpoint-bwl"` - `"remove-blocked"` - `"fragmail"` - `"splice"` - `"mms-checksum"` |
| **mm3-outbreak-prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **mm3oversizelimit**  integer | Maximum file size to scan |
| **mm4**  list / elements=string | MM4 options.  **Choices:**   - `"avmonitor"` - `"block"` - `"oversize"` - `"quarantine"` - `"scan"` - `"avquery"` - `"bannedword"` - `"no-content-summary"` - `"archive-summary"` - `"archive-full"` - `"carrier-endpoint-bwl"` - `"remove-blocked"` - `"fragmail"` - `"splice"` - `"mms-checksum"` |
| **mm4-outbreak-prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **mm4oversizelimit**  integer | Maximum file size to scan |
| **mm7**  list / elements=string | MM7 options.  **Choices:**   - `"avmonitor"` - `"block"` - `"oversize"` - `"quarantine"` - `"scan"` - `"avquery"` - `"bannedword"` - `"no-content-summary"` - `"archive-summary"` - `"archive-full"` - `"carrier-endpoint-bwl"` - `"remove-blocked"` - `"chunkedbypass"` - `"clientcomfort"` - `"servercomfort"` - `"strict-file"` - `"mms-checksum"` |
| **mm7-addr-hdr**  string | HTTP header field |
| **mm7-addr-source**  string | Source for MM7 user address.  **Choices:**   - `"http-header"` - `"cookie"` |
| **mm7-convert-hex**  string | Enable/disable conversion of user address from HEX string for MM7.  **Choices:**   - `"disable"` - `"enable"` |
| **mm7-outbreak-prevention**  string | Enable FortiGuard Virus Outbreak Prevention service.  **Choices:**   - `"disabled"` - `"files"` - `"full-archive"` |
| **mm7comfortamount**  integer | MM7 comfort amount |
| **mm7comfortinterval**  integer | MM7 comfort interval |
| **mm7oversizelimit**  integer | Maximum file size to scan |
| **mms-antispam-mass-log**  string | Enable/disable logging for MMS antispam mass.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-av-block-log**  string | Enable/disable logging for MMS antivirus file blocking.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-av-oversize-log**  string | Enable/disable logging for MMS antivirus oversize file blocking.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-av-virus-log**  string | Enable/disable logging for MMS antivirus scanning.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-carrier-endpoint-filter-log**  string | Enable/disable logging for MMS end point filter blocking.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-checksum-log**  string | Enable/disable MMS content checksum logging.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-checksum-table**  string | MMS content checksum table ID. |
| **mms-notification-log**  string | Enable/disable logging for MMS notification messages.  **Choices:**   - `"disable"` - `"enable"` |
| **mms-web-content-log**  string | Enable/disable logging for MMS web content blocking.  **Choices:**   - `"disable"` - `"enable"` |
| **mmsbwordthreshold**  integer | MMS banned word threshold. |
| **name**  string / required | Profile name. |
| **notif-msisdn**  list / elements=dictionary | Notif-Msisdn. |
| **msisdn**  string | Recipient MSISDN. |
| **threshold**  list / elements=string | Thresholds on which this MSISDN will receive an alert.  **Choices:**   - `"flood-thresh-1"` - `"flood-thresh-2"` - `"flood-thresh-3"` - `"dupe-thresh-1"` - `"dupe-thresh-2"` - `"dupe-thresh-3"` |
| **notification**  dictionary | no description |
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
| **outbreak-prevention**  dictionary | no description |
| **external-blocklist**  string | Enable/disable external malware blocklist.  **Choices:**   - `"disable"` - `"enable"` |
| **ftgd-service**  string | Enable/disable FortiGuard Virus outbreak prevention service.  **Choices:**   - `"disable"` - `"enable"` |
| **remove-blocked-const-length**  string | Enable/disable MMS replacement of blocked file constant length.  **Choices:**   - `"disable"` - `"enable"` |
| **replacemsg-group**  string | Replacement message group. |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_mmsprofile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_mmsprofile_module.md#id4)

```yaml+jinja
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure MMS profiles.
     fmgr_firewall_mmsprofile:
        bypass_validation: False
        adom: FortiCarrier # FortiCarrier only object, need a FortiCarrier adom
        state: present
        firewall_mmsprofile:
           comment: 'ansible-comment'
           #extended-utm-log: disable
           mm1:
             - avmonitor
             - block
             - oversize
             - quarantine
             - scan
             - avquery
             - bannedword
             - no-content-summary
             - archive-summary
             - archive-full
             - carrier-endpoint-bwl
             - remove-blocked
             - chunkedbypass
             - clientcomfort
             - servercomfort
             - strict-file
             - mms-checksum
           mm3:
             - avmonitor
             - block
             - oversize
             - quarantine
             - scan
             - avquery
             - bannedword
             - no-content-summary
             - archive-summary
             - archive-full
             - carrier-endpoint-bwl
             - remove-blocked
             - fragmail
             - splice
             - mms-checksum
           mm4:
             - avmonitor
             - block
             - oversize
             - quarantine
             - scan
             - avquery
             - bannedword
             - no-content-summary
             - archive-summary
             - archive-full
             - carrier-endpoint-bwl
             - remove-blocked
             - fragmail
             - splice
             - mms-checksum
           mm7:
             - avmonitor
             - block
             - oversize
             - quarantine
             - scan
             - avquery
             - bannedword
             - no-content-summary
             - archive-summary
             - archive-full
             - carrier-endpoint-bwl
             - remove-blocked
             - chunkedbypass
             - clientcomfort
             - servercomfort
             - strict-file
             - mms-checksum
           name: 'ansible-test'

- name: gathering fortimanager facts
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: retrieve all the MMS profiles
     fmgr_fact:
       facts:
           selector: 'firewall_mmsprofile'
           params:
               adom: 'FortiCarrier' # FortiCarrier only object, need a FortiCarrier adom
               mms-profile: 'your_value'
```

## [Return Values](fmgr_firewall_mmsprofile_module.md#id5)

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
