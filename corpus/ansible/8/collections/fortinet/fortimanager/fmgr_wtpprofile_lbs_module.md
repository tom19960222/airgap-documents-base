---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_wtpprofile_lbs module – Set various location based service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_wtpprofile_lbs_module.html
fetched_at: 2026-07-28T02:23:08+00:00
---
# fortinet.fortimanager.fmgr_wtpprofile_lbs module – Set various location based service

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_wtpprofile_lbs`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |
| **wtp-profile**  string / required | the parameter (wtp-profile) in requested url |
| **wtpprofile_lbs**  dictionary | the top level parameters set |
| **aeroscout**  string | Enable/disable AeroScout Real Time Location Service  **Choices:**   - `"disable"` - `"enable"` |
| **aeroscout-ap-mac**  string | Use BSSID or board MAC address as AP MAC address in the Aeroscout AP message.  **Choices:**   - `"bssid"` - `"board-mac"` |
| **aeroscout-mmu-report**  string | Enable/disable MU compounded report.  **Choices:**   - `"disable"` - `"enable"` |
| **aeroscout-mu**  string | Enable/disable AeroScout support.  **Choices:**   - `"disable"` - `"enable"` |
| **aeroscout-mu-factor**  integer | AeroScout Mobile Unit |
| **aeroscout-mu-timeout**  integer | AeroScout MU mode timeout |
| **aeroscout-server-ip**  string | IP address of AeroScout server. |
| **aeroscout-server-port**  integer | AeroScout server UDP listening port. |
| **ekahau-blink-mode**  string | Enable/disable Ekahua blink mode  **Choices:**   - `"disable"` - `"enable"` |
| **ekahau-tag**  string | WiFi frame MAC address or WiFi Tag. |
| **erc-server-ip**  string | IP address of Ekahua RTLS Controller |
| **erc-server-port**  integer | Ekahua RTLS Controller |
| **fortipresence**  string | Enable/disable FortiPresence to monitor the location and activity of WiFi clients even if they dont connect to this WiFi network  **Choices:**   - `"disable"` - `"enable"` - `"enable2"` - `"foreign"` - `"both"` |
| **fortipresence-ble**  string | Enable/disable FortiPresence finding and reporting BLE devices.  **Choices:**   - `"disable"` - `"enable"` |
| **fortipresence-frequency**  integer | FortiPresence report transmit frequency |
| **fortipresence-port**  integer | FortiPresence server UDP listening port |
| **fortipresence-project**  string | FortiPresence project name |
| **fortipresence-rogue**  string | Enable/disable FortiPresence finding and reporting rogue APs.  **Choices:**   - `"disable"` - `"enable"` |
| **fortipresence-secret**  any | (list) no description |
| **fortipresence-server**  string | FortiPresence server IP address. |
| **fortipresence-server-addr-type**  string | FortiPresence server address type  **Choices:**   - `"fqdn"` - `"ipv4"` |
| **fortipresence-server-fqdn**  string | FQDN of FortiPresence server. |
| **fortipresence-unassoc**  string | Enable/disable FortiPresence finding and reporting unassociated stations.  **Choices:**   - `"disable"` - `"enable"` |
| **polestar**  string | Enable/disable PoleStar BLE NAO Track Real Time Location Service  **Choices:**   - `"disable"` - `"enable"` |
| **polestar-accumulation-interval**  integer | Time that measurements should be accumulated in seconds |
| **polestar-asset-addrgrp-list**  string | Tags and asset addrgrp list to be reported. |
| **polestar-asset-uuid-list1**  string | Tags and asset UUID list 1 to be reported |
| **polestar-asset-uuid-list2**  string | Tags and asset UUID list 2 to be reported |
| **polestar-asset-uuid-list3**  string | Tags and asset UUID list 3 to be reported |
| **polestar-asset-uuid-list4**  string | Tags and asset UUID list 4 to be reported |
| **polestar-protocol**  string | Select the protocol to report Measurements, Advertising Data, or Location Data to NAO Cloud.  **Choices:**   - `"WSS"` |
| **polestar-reporting-interval**  integer | Time between reporting accumulated measurements in seconds |
| **polestar-server-fqdn**  string | FQDN of PoleStar Nao Track Server |
| **polestar-server-path**  string | Path of PoleStar Nao Track Server |
| **polestar-server-port**  integer | Port of PoleStar Nao Track Server |
| **polestar-server-token**  string | Access Token of PoleStar Nao Track Server. |
| **station-locate**  string | Enable/disable client station locating services for all clients, whether associated or not  **Choices:**   - `"disable"` - `"enable"` |

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
    - name: Set various location based service
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
          aeroscout-mu-factor: <integer>
          aeroscout-mu-timeout: <integer>
          aeroscout-server-ip: <string>
          aeroscout-server-port: <integer>
          ekahau-blink-mode: <value in [disable, enable]>
          ekahau-tag: <string>
          erc-server-ip: <string>
          erc-server-port: <integer>
          fortipresence: <value in [disable, enable, enable2, ...]>
          fortipresence-frequency: <integer>
          fortipresence-port: <integer>
          fortipresence-project: <string>
          fortipresence-rogue: <value in [disable, enable]>
          fortipresence-secret: <list or string>
          fortipresence-server: <string>
          fortipresence-unassoc: <value in [disable, enable]>
          station-locate: <value in [disable, enable]>
          fortipresence-ble: <value in [disable, enable]>
          fortipresence-server-addr-type: <value in [fqdn, ipv4]>
          fortipresence-server-fqdn: <string>
          polestar: <value in [disable, enable]>
          polestar-accumulation-interval: <integer>
          polestar-asset-addrgrp-list: <string>
          polestar-asset-uuid-list1: <string>
          polestar-asset-uuid-list2: <string>
          polestar-asset-uuid-list3: <string>
          polestar-asset-uuid-list4: <string>
          polestar-protocol: <value in [WSS]>
          polestar-reporting-interval: <integer>
          polestar-server-fqdn: <string>
          polestar-server-path: <string>
          polestar-server-port: <integer>
          polestar-server-token: <string>
```

## [Return Values](fmgr_wtpprofile_lbs_module.md#id5)

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
