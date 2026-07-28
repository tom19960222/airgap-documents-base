---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_locallog_fortianalyzer3_filter module – Filter for FortiAnalyzer3 logging."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_locallog_fortianalyzer3_filter_module.html
fetched_at: 2026-07-28T02:18:49+00:00
---
# fortinet.fortimanager.fmgr_system_locallog_fortianalyzer3_filter module – Filter for FortiAnalyzer3 logging.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_locallog_fortianalyzer3_filter`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_locallog_fortianalyzer3_filter_module.md#synopsis)
- [Parameters](fmgr_system_locallog_fortianalyzer3_filter_module.md#parameters)
- [Notes](fmgr_system_locallog_fortianalyzer3_filter_module.md#notes)
- [Examples](fmgr_system_locallog_fortianalyzer3_filter_module.md#examples)
- [Return Values](fmgr_system_locallog_fortianalyzer3_filter_module.md#return-values)

## [Synopsis](fmgr_system_locallog_fortianalyzer3_filter_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_locallog_fortianalyzer3_filter_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **system_locallog_fortianalyzer3_filter**  dictionary | the top level parameters set |
| **aid**  string | Log aid messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **controller**  string | Controller application generic messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **devcfg**  string | Log device configuration message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **devops**  string | Managered devices operations messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **diskquota**  string | Log Fortianalyzer disk quota messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **dm**  string | Log deployment manager message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **docker**  string | Docker application generic messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **dvm**  string | Log device manager messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **ediscovery**  string | Log Fortianalyzer ediscovery messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **epmgr**  string | Log endpoint manager message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **event**  string | Log event messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **eventmgmt**  string | Log Fortianalyzer event handler messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **faz**  string | Log Fortianalyzer messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fazha**  string | Log Fortianalyzer HA messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fazsys**  string | Log Fortianalyzer system messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fgd**  string | Log FortiGuard service message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fgfm**  string | Log FGFM protocol message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fips**  string | Whether to log fips messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fmgws**  string | Log web service messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fmlmgr**  string | Log FortiMail manager message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fmwmgr**  string | Log firmware manager message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fortiview**  string | Log Fortianalyzer FortiView messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **glbcfg**  string | Log global database message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **ha**  string | Log HA message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **hcache**  string | Log Fortianalyzer hcache messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **incident**  string | Log Fortianalyzer incident messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **iolog**  string | Log debug IO log message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **logd**  string | Log the status of log daemon.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **logdb**  string | Log Fortianalyzer log DB messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **logdev**  string | Log Fortianalyzer log device messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **logfile**  string | Log Fortianalyzer log file messages.  enable - Enable setting.  disable - Disable setting.  **Choices:**   - `"enable"` - `"disable"` |
| **logging**  string | Log Fortianalyzer logging messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **lrmgr**  string | Log log and report manager message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **objcfg**  string | Log object configuration change message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **report**  string | Log Fortianalyzer report messages.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **rev**  string | Log revision history message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **rtmon**  string | Log real-time monitor message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **scfw**  string | Log firewall objects message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **scply**  string | Log policy console message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **scrmgr**  string | Log script manager message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **scvpn**  string | Log VPN console message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **system**  string | Log system manager message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **webport**  string | Log web portal message.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_locallog_fortianalyzer3_filter_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_locallog_fortianalyzer3_filter_module.md#id4)

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
    - name: Filter for FortiAnalyzer3 logging.
      fmgr_system_locallog_fortianalyzer3_filter:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_locallog_fortianalyzer3_filter:
          devcfg: <value in [disable, enable]>
          devops: <value in [disable, enable]>
          diskquota: <value in [disable, enable]>
          dm: <value in [disable, enable]>
          dvm: <value in [disable, enable]>
          ediscovery: <value in [disable, enable]>
          epmgr: <value in [disable, enable]>
          event: <value in [disable, enable]>
          eventmgmt: <value in [disable, enable]>
          faz: <value in [disable, enable]>
          fazha: <value in [disable, enable]>
          fazsys: <value in [disable, enable]>
          fgd: <value in [disable, enable]>
          fgfm: <value in [disable, enable]>
          fips: <value in [disable, enable]>
          fmgws: <value in [disable, enable]>
          fmlmgr: <value in [disable, enable]>
          fmwmgr: <value in [disable, enable]>
          fortiview: <value in [disable, enable]>
          glbcfg: <value in [disable, enable]>
          ha: <value in [disable, enable]>
          hcache: <value in [disable, enable]>
          iolog: <value in [disable, enable]>
          logd: <value in [disable, enable]>
          logdb: <value in [disable, enable]>
          logdev: <value in [disable, enable]>
          logfile: <value in [enable, disable]>
          logging: <value in [disable, enable]>
          lrmgr: <value in [disable, enable]>
          objcfg: <value in [disable, enable]>
          report: <value in [disable, enable]>
          rev: <value in [disable, enable]>
          rtmon: <value in [disable, enable]>
          scfw: <value in [disable, enable]>
          scply: <value in [disable, enable]>
          scrmgr: <value in [disable, enable]>
          scvpn: <value in [disable, enable]>
          system: <value in [disable, enable]>
          webport: <value in [disable, enable]>
          incident: <value in [disable, enable]>
          aid: <value in [disable, enable]>
          docker: <value in [disable, enable]>
          controller: <value in [disable, enable]>
```

## [Return Values](fmgr_system_locallog_fortianalyzer3_filter_module.md#id5)

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
