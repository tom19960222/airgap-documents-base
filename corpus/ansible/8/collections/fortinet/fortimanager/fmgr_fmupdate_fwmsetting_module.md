---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_fmupdate_fwmsetting module – Configure firmware management settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_fmupdate_fwmsetting_module.html
fetched_at: 2026-07-28T02:13:39+00:00
---
# fortinet.fortimanager.fmgr_fmupdate_fwmsetting module – Configure firmware management settings.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fmupdate_fwmsetting`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_fmupdate_fwmsetting_module.md#synopsis)
- [Parameters](fmgr_fmupdate_fwmsetting_module.md#parameters)
- [Notes](fmgr_fmupdate_fwmsetting_module.md#notes)
- [Examples](fmgr_fmupdate_fwmsetting_module.md#examples)
- [Return Values](fmgr_fmupdate_fwmsetting_module.md#return-values)

## [Synopsis](fmgr_fmupdate_fwmsetting_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_fmupdate_fwmsetting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **fmupdate_fwmsetting**  dictionary | the top level parameters set |
| **auto-scan-fgt-disk**  string | auto scan fgt disk if needed.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **check-fgt-disk**  string | check fgt disk before upgrade image.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fds-failover-fmg**  string | using fmg local image file is download from fds fails.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fds-image-timeout**  integer | timer for fgt download image from fortiguard |
| **immx-source**  string | Configure which of IMMX file to be used for choosing upgrade pach.  fmg - Use IMMX file for FortiManager  fgt - Use IMMX file for FortiGate  cloud - Use IMMX file for FortiCloud  **Choices:**   - `"fmg"` - `"fgt"` - `"cloud"` |
| **log**  string | Configure log setting for fwm daemon  fwm - FWM daemon log  fwm_dm - FWM and Deployment service log  fwm_dm_json - FWM and Deployment service log with JSON data between FMG-FGT  **Choices:**   - `"fwm"` - `"fwm_dm"` - `"fwm_dm_json"` |
| **max-fds-retry**  integer | The retries when fgt download from fds fail |
| **multiple-steps-interval**  integer | waiting time between multiple steps upgrade |
| **skip-disk-check**  string | skip disk check when upgrade image.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **upgrade-timeout**  dictionary | no description |
| **check-status-timeout**  integer | timeout for checking status after tunnnel is up. |
| **ctrl-check-status-timeout**  integer | timeout for checking fap/fsw/fext status after request upgrade. |
| **ctrl-put-image-by-fds-timeout**  integer | timeout for waiting device get fap/fsw/fext image from fortiguard. |
| **ha-sync-timeout**  integer | timeout for waiting HA sync. |
| **license-check-timeout**  integer | timeout for waiting fortigate check license. |
| **prepare-image-timeout**  integer | timeout for preparing image. |
| **put-image-by-fds-timeout**  integer | timeout for waiting device get image from fortiguard. |
| **put-image-timeout**  integer | timeout for waiting send image over tunnel. |
| **reboot-of-fsck-timeout**  integer | timeout for waiting fortigate reboot. |
| **reboot-of-upgrade-timeout**  integer | timeout for waiting fortigate reboot after image upgrade. |
| **retrieve-timeout**  integer | timeout for waiting retrieve. |
| **rpc-timeout**  integer | timeout for waiting fortigate rpc response. |
| **total-timeout**  integer | timeout for the whole fortigate upgrade |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_fmupdate_fwmsetting_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_fmupdate_fwmsetting_module.md#id4)

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
    - name: Configure firmware management settings.
      fmgr_fmupdate_fwmsetting:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        fmupdate_fwmsetting:
          fds-image-timeout: <integer>
          max-fds-retry: <integer>
          multiple-steps-interval: <integer>
          skip-disk-check: <value in [disable, enable]>
          auto-scan-fgt-disk: <value in [disable, enable]>
          check-fgt-disk: <value in [disable, enable]>
          fds-failover-fmg: <value in [disable, enable]>
          immx-source: <value in [fmg, fgt, cloud]>
          log: <value in [fwm, fwm_dm, fwm_dm_json]>
          upgrade-timeout:
            check-status-timeout: <integer>
            ctrl-check-status-timeout: <integer>
            ctrl-put-image-by-fds-timeout: <integer>
            ha-sync-timeout: <integer>
            license-check-timeout: <integer>
            prepare-image-timeout: <integer>
            put-image-by-fds-timeout: <integer>
            put-image-timeout: <integer>
            reboot-of-fsck-timeout: <integer>
            reboot-of-upgrade-timeout: <integer>
            retrieve-timeout: <integer>
            rpc-timeout: <integer>
            total-timeout: <integer>
```

## [Return Values](fmgr_fmupdate_fwmsetting_module.md#id5)

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
