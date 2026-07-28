---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_admin_setting module – Admin setting."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_admin_setting_module.html
fetched_at: 2026-07-28T02:17:58+00:00
---
# fortinet.fortimanager.fmgr_system_admin_setting module – Admin setting.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_admin_setting`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_admin_setting_module.md#synopsis)
- [Parameters](fmgr_system_admin_setting_module.md#parameters)
- [Notes](fmgr_system_admin_setting_module.md#notes)
- [Examples](fmgr_system_admin_setting_module.md#examples)
- [Return Values](fmgr_system_admin_setting_module.md#return-values)

## [Synopsis](fmgr_system_admin_setting_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_admin_setting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **system_admin_setting**  dictionary | the top level parameters set |
| **access-banner**  string | Enable/disable access banner.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **admin-https-redirect**  string | Enable/disable redirection of HTTP admin traffic to HTTPS.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **admin-login-max**  integer | Maximum number admin users logged in at one time |
| **admin_server_cert**  string | HTTPS & Web Service server certificate. |
| **allow_register**  string | Enable/disable allowance of register an unregistered device.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **auth-addr**  string | IP which is used by FGT to authorize FMG. |
| **auth-port**  integer | Port which is used by FGT to authorize FMG. |
| **auto-update**  string | Enable/disable FortiGate automatic update.  disable - Disable device automatic update.  enable - Enable device automatic update.  **Choices:**   - `"disable"` - `"enable"` |
| **banner-message**  string | Banner message. |
| **central-ftgd-local-cat-id**  string | Central FortiGuard local category id management, and do not auto assign id during installation.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **chassis-mgmt**  string | Enable or disable chassis management.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **chassis-update-interval**  integer | Chassis background update interval |
| **device_sync_status**  string | Enable/disable device synchronization status indication.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **firmware-upgrade-check**  string | Enable/disable firmware upgrade check.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fsw-ignore-platform-check**  string | Enable/disable FortiSwitch Manager switch platform support check.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **gui-theme**  string | Color scheme to use for the administration GUI.  blue - Blueberry  green - Kiwi  red - Cherry  melongene - Plum  spring - Spring  summer - Summer  autumn - Autumn  winter - Winter  space - Space  calla-lily - Calla Lily  binary-tunnel - Binary Tunnel  diving - Diving  dreamy - Dreamy  technology - Technology  landscape - Landscape  twilight - Twilight  canyon - Canyon  northern-light - Northern Light  astronomy - Astronomy  fish - Fish  penguin - Penguin  panda - Panda  polar-bear - Polar Bear  parrot - Parrot  cave - Cave  **Choices:**   - `"blue"` - `"green"` - `"red"` - `"melongene"` - `"spring"` - `"summer"` - `"autumn"` - `"winter"` - `"space"` - `"calla-lily"` - `"binary-tunnel"` - `"diving"` - `"dreamy"` - `"technology"` - `"landscape"` - `"twilight"` - `"canyon"` - `"northern-light"` - `"astronomy"` - `"fish"` - `"penguin"` - `"panda"` - `"polar-bear"` - `"parrot"` - `"cave"` - `"mountain"` - `"zebra"` - `"contrast-dark"` - `"circuit-board"` - `"mars"` - `"blue-sea"` - `"mariner"` - `"jade"` - `"neutrino"` - `"dark-matter"` - `"forest"` - `"cat"` - `"graphite"` |
| **http_port**  integer | HTTP port. |
| **https_port**  integer | HTTPS port. |
| **idle_timeout**  integer | Idle timeout |
| **idle_timeout_api**  integer | Idle timeout for API sessions |
| **idle_timeout_gui**  integer | Idle timeout for GUI sessions |
| **idle_timeout_sso**  integer | Idle timeout for SSO sessions |
| **install-ifpolicy-only**  string | Allow install interface policy only.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **mgmt-addr**  string | IP of FortiManager used by FGFM. |
| **mgmt-fqdn**  string | FQDN of FortiManager used by FGFM. |
| **objects-force-deletion**  string | Enable/disable used objects force deletion.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **offline_mode**  string | Enable/disable offline mode.  disable - Disable offline mode.  enable - Enable offline mode.  **Choices:**   - `"disable"` - `"enable"` |
| **preferred-fgfm-intf**  string | Preferred interface for FGFM connection. |
| **register_passwd**  any | (list) Password for register a device. |
| **rtm-max-monitor-by-days**  integer | Maximum rtm monitor |
| **rtm-temp-file-limit**  integer | Set rtm monitor temp file limit by hours. |
| **sdwan-monitor-history**  string | Enable/disable hostname display in the GUI login page.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **sdwan-skip-unmapped-input-device**  string | Skip unmapped interface for sdwan/rule/input-device instead of report mapping error.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **shell-access**  string | Enable/disable shell access.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **shell-password**  any | (list) Password for shell access. |
| **show-add-multiple**  string | Show add multiple button.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **show-adom-devman**  string | Show ADOM device manager tools on GUI.  disable - Hide device manager tools on GUI.  enable - Show device manager tools on GUI.  **Choices:**   - `"disable"` - `"enable"` |
| **show-checkbox-in-table**  string | Show checkboxs in tables on GUI.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **show-device-import-export**  string | Enable/disable import/export of ADOM, device, and group lists.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **show-fct-manager**  string | Enable/disable FCT manager.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **show-hostname**  string | Enable/disable hostname display in the GUI login page.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **show_automatic_script**  string | Enable/disable automatic script.  disable - Disable script option.  enable - Enable script option.  **Choices:**   - `"disable"` - `"enable"` |
| **show_grouping_script**  string | Enable/disable grouping script.  disable - Disable script option.  enable - Enable script option.  **Choices:**   - `"disable"` - `"enable"` |
| **show_schedule_script**  string | Enable or disable schedule script.  disable - Disable script option.  enable - Enable script option.  **Choices:**   - `"disable"` - `"enable"` |
| **show_tcl_script**  string | Enable/disable TCL script.  disable - Disable script option.  enable - Enable script option.  **Choices:**   - `"disable"` - `"enable"` |
| **traffic-shaping-history**  string | Enable/disable traffic-shaping-history.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **unreg_dev_opt**  string | Action to take when unregistered device connects to FortiManager.  add_no_service - Add unregistered devices but deny service requests.  ignore - Ignore unregistered devices.  add_allow_service - Add unregistered devices and allow service requests.  **Choices:**   - `"add_no_service"` - `"ignore"` - `"add_allow_service"` |
| **webadmin_language**  string | Web admin language.  auto_detect - Automatically detect language.  english - English.  simplified_chinese - Simplified Chinese.  traditional_chinese - Traditional Chinese.  japanese - Japanese.  korean - Korean.  spanish - Spanish.  **Choices:**   - `"auto_detect"` - `"english"` - `"simplified_chinese"` - `"traditional_chinese"` - `"japanese"` - `"korean"` - `"spanish"` - `"french"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_admin_setting_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_admin_setting_module.md#id4)

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
    - name: Admin setting.
      fmgr_system_admin_setting:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_admin_setting:
          access-banner: <value in [disable, enable]>
          admin-https-redirect: <value in [disable, enable]>
          admin-login-max: <integer>
          admin_server_cert: <string>
          allow_register: <value in [disable, enable]>
          auto-update: <value in [disable, enable]>
          banner-message: <string>
          chassis-mgmt: <value in [disable, enable]>
          chassis-update-interval: <integer>
          device_sync_status: <value in [disable, enable]>
          gui-theme: <value in [blue, green, red, ...]>
          http_port: <integer>
          https_port: <integer>
          idle_timeout: <integer>
          install-ifpolicy-only: <value in [disable, enable]>
          mgmt-addr: <string>
          mgmt-fqdn: <string>
          objects-force-deletion: <value in [disable, enable]>
          offline_mode: <value in [disable, enable]>
          register_passwd: <list or string>
          sdwan-monitor-history: <value in [disable, enable]>
          shell-access: <value in [disable, enable]>
          shell-password: <list or string>
          show-add-multiple: <value in [disable, enable]>
          show-adom-devman: <value in [disable, enable]>
          show-checkbox-in-table: <value in [disable, enable]>
          show-device-import-export: <value in [disable, enable]>
          show-hostname: <value in [disable, enable]>
          show_automatic_script: <value in [disable, enable]>
          show_grouping_script: <value in [disable, enable]>
          show_schedule_script: <value in [disable, enable]>
          show_tcl_script: <value in [disable, enable]>
          unreg_dev_opt: <value in [add_no_service, ignore, add_allow_service]>
          webadmin_language: <value in [auto_detect, english, simplified_chinese, ...]>
          show-fct-manager: <value in [disable, enable]>
          sdwan-skip-unmapped-input-device: <value in [disable, enable]>
          auth-addr: <string>
          auth-port: <integer>
          idle_timeout_api: <integer>
          idle_timeout_gui: <integer>
          central-ftgd-local-cat-id: <value in [disable, enable]>
          idle_timeout_sso: <integer>
          preferred-fgfm-intf: <string>
          traffic-shaping-history: <value in [disable, enable]>
          fsw-ignore-platform-check: <value in [disable, enable]>
          rtm-max-monitor-by-days: <integer>
          rtm-temp-file-limit: <integer>
          firmware-upgrade-check: <value in [disable, enable]>
```

## [Return Values](fmgr_system_admin_setting_module.md#id5)

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
