---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_widsprofile module – Configure wireless intrusion detection system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_widsprofile_module.html
fetched_at: 2026-07-28T02:22:59+00:00
---
# fortinet.fortimanager.fmgr_widsprofile module – Configure wireless intrusion detection system

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_widsprofile`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **widsprofile**  dictionary | the top level parameters set |
| **ap-auto-suppress**  string | Enable/disable on-wire rogue AP auto-suppression  **Choices:**   - `"disable"` - `"enable"` |
| **ap-bgscan-disable-day**  list / elements=string | Ap-Bgscan-Disable-Day.  **Choices:**   - `"sunday"` - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` |
| **ap-bgscan-disable-end**  string | End time, using a 24-hour clock in the format of hh |
| **ap-bgscan-disable-schedules**  any | (list or str) Firewall schedules for turning off FortiAP radio background scan. |
| **ap-bgscan-disable-start**  string | Start time, using a 24-hour clock in the format of hh |
| **ap-bgscan-duration**  integer | Listening time on a scanning channel |
| **ap-bgscan-idle**  integer | Waiting time for channel inactivity before scanning this channel |
| **ap-bgscan-intv**  integer | Period of time between scanning two channels |
| **ap-bgscan-period**  integer | Period of time between background scans |
| **ap-bgscan-report-intv**  integer | Period of time between background scan reports |
| **ap-fgscan-report-intv**  integer | Period of time between foreground scan reports |
| **ap-scan**  string | Enable/disable rogue AP detection.  **Choices:**   - `"disable"` - `"enable"` |
| **ap-scan-channel-list-2G-5G**  any | (list) no description |
| **ap-scan-channel-list-6G**  any | (list) no description |
| **ap-scan-passive**  string | Enable/disable passive scanning.  **Choices:**   - `"disable"` - `"enable"` |
| **ap-scan-threshold**  string | Minimum signal level/threshold in dBm required for the AP to report detected rogue AP |
| **asleap-attack**  string | Enable/disable asleap attack detection  **Choices:**   - `"disable"` - `"enable"` |
| **assoc-flood-thresh**  integer | The threshold value for association frame flooding. |
| **assoc-flood-time**  integer | Number of seconds after which a station is considered not connected. |
| **assoc-frame-flood**  string | Enable/disable association frame flooding detection  **Choices:**   - `"disable"` - `"enable"` |
| **auth-flood-thresh**  integer | The threshold value for authentication frame flooding. |
| **auth-flood-time**  integer | Number of seconds after which a station is considered not connected. |
| **auth-frame-flood**  string | Enable/disable authentication frame flooding detection  **Choices:**   - `"disable"` - `"enable"` |
| **comment**  string | Comment. |
| **deauth-broadcast**  string | Enable/disable broadcasting de-authentication detection  **Choices:**   - `"disable"` - `"enable"` |
| **deauth-unknown-src-thresh**  integer | Threshold value per second to deauth unknown src for DoS attack |
| **eapol-fail-flood**  string | Enable/disable EAPOL-Failure flooding  **Choices:**   - `"disable"` - `"enable"` |
| **eapol-fail-intv**  integer | The detection interval for EAPOL-Failure flooding |
| **eapol-fail-thresh**  integer | The threshold value for EAPOL-Failure flooding in specified interval. |
| **eapol-logoff-flood**  string | Enable/disable EAPOL-Logoff flooding  **Choices:**   - `"disable"` - `"enable"` |
| **eapol-logoff-intv**  integer | The detection interval for EAPOL-Logoff flooding |
| **eapol-logoff-thresh**  integer | The threshold value for EAPOL-Logoff flooding in specified interval. |
| **eapol-pre-fail-flood**  string | Enable/disable premature EAPOL-Failure flooding  **Choices:**   - `"disable"` - `"enable"` |
| **eapol-pre-fail-intv**  integer | The detection interval for premature EAPOL-Failure flooding |
| **eapol-pre-fail-thresh**  integer | The threshold value for premature EAPOL-Failure flooding in specified interval. |
| **eapol-pre-succ-flood**  string | Enable/disable premature EAPOL-Success flooding  **Choices:**   - `"disable"` - `"enable"` |
| **eapol-pre-succ-intv**  integer | The detection interval for premature EAPOL-Success flooding |
| **eapol-pre-succ-thresh**  integer | The threshold value for premature EAPOL-Success flooding in specified interval. |
| **eapol-start-flood**  string | Enable/disable EAPOL-Start flooding  **Choices:**   - `"disable"` - `"enable"` |
| **eapol-start-intv**  integer | The detection interval for EAPOL-Start flooding |
| **eapol-start-thresh**  integer | The threshold value for EAPOL-Start flooding in specified interval. |
| **eapol-succ-flood**  string | Enable/disable EAPOL-Success flooding  **Choices:**   - `"disable"` - `"enable"` |
| **eapol-succ-intv**  integer | The detection interval for EAPOL-Success flooding |
| **eapol-succ-thresh**  integer | The threshold value for EAPOL-Success flooding in specified interval. |
| **invalid-mac-oui**  string | Enable/disable invalid MAC OUI detection.  **Choices:**   - `"disable"` - `"enable"` |
| **long-duration-attack**  string | Enable/disable long duration attack detection based on user configured threshold  **Choices:**   - `"disable"` - `"enable"` |
| **long-duration-thresh**  integer | Threshold value for long duration attack detection |
| **name**  string / required | WIDS profile name. |
| **null-ssid-probe-resp**  string | Enable/disable null SSID probe response detection  **Choices:**   - `"disable"` - `"enable"` |
| **rogue-scan**  string | Enable/disable rogue AP on-wire scan.  **Choices:**   - `"disable"` - `"enable"` |
| **sensor-mode**  string | Scan WiFi nearby stations  **Choices:**   - `"disable"` - `"foreign"` - `"both"` |
| **spoofed-deauth**  string | Enable/disable spoofed de-authentication attack detection  **Choices:**   - `"disable"` - `"enable"` |
| **weak-wep-iv**  string | Enable/disable weak WEP IV  **Choices:**   - `"disable"` - `"enable"` |
| **wireless-bridge**  string | Enable/disable wireless bridge detection  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
    - name: Configure wireless intrusion detection system
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
          ap-bgscan-disable-end: <string>
          ap-bgscan-disable-start: <string>
          ap-bgscan-duration: <integer>
          ap-bgscan-idle: <integer>
          ap-bgscan-intv: <integer>
          ap-bgscan-period: <integer>
          ap-bgscan-report-intv: <integer>
          ap-fgscan-report-intv: <integer>
          ap-scan: <value in [disable, enable]>
          ap-scan-passive: <value in [disable, enable]>
          asleap-attack: <value in [disable, enable]>
          assoc-flood-thresh: <integer>
          assoc-flood-time: <integer>
          assoc-frame-flood: <value in [disable, enable]>
          auth-flood-thresh: <integer>
          auth-flood-time: <integer>
          auth-frame-flood: <value in [disable, enable]>
          comment: <string>
          deauth-broadcast: <value in [disable, enable]>
          deauth-unknown-src-thresh: <integer>
          eapol-fail-flood: <value in [disable, enable]>
          eapol-fail-intv: <integer>
          eapol-fail-thresh: <integer>
          eapol-logoff-flood: <value in [disable, enable]>
          eapol-logoff-intv: <integer>
          eapol-logoff-thresh: <integer>
          eapol-pre-fail-flood: <value in [disable, enable]>
          eapol-pre-fail-intv: <integer>
          eapol-pre-fail-thresh: <integer>
          eapol-pre-succ-flood: <value in [disable, enable]>
          eapol-pre-succ-intv: <integer>
          eapol-pre-succ-thresh: <integer>
          eapol-start-flood: <value in [disable, enable]>
          eapol-start-intv: <integer>
          eapol-start-thresh: <integer>
          eapol-succ-flood: <value in [disable, enable]>
          eapol-succ-intv: <integer>
          eapol-succ-thresh: <integer>
          invalid-mac-oui: <value in [disable, enable]>
          long-duration-attack: <value in [disable, enable]>
          long-duration-thresh: <integer>
          name: <string>
          null-ssid-probe-resp: <value in [disable, enable]>
          sensor-mode: <value in [disable, foreign, both]>
          spoofed-deauth: <value in [disable, enable]>
          weak-wep-iv: <value in [disable, enable]>
          wireless-bridge: <value in [disable, enable]>
          ap-bgscan-disable-schedules: <list or string>
          rogue-scan: <value in [disable, enable]>
          ap-scan-threshold: <string>
          ap-scan-channel-list-2G-5G: <list or string>
          ap-scan-channel-list-6G: <list or string>
```

## [Return Values](fmgr_widsprofile_module.md#id5)

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
