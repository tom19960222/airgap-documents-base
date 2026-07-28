---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_fmupdate_webspam_fgdsetting module – Configure the FortiGuard run parameters."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_fmupdate_webspam_fgdsetting_module.html
fetched_at: 2026-07-28T02:13:46+00:00
---
# fortinet.fortimanager.fmgr_fmupdate_webspam_fgdsetting module – Configure the FortiGuard run parameters.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fmupdate_webspam_fgdsetting`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_fmupdate_webspam_fgdsetting_module.md#synopsis)
- [Parameters](fmgr_fmupdate_webspam_fgdsetting_module.md#parameters)
- [Notes](fmgr_fmupdate_webspam_fgdsetting_module.md#notes)
- [Examples](fmgr_fmupdate_webspam_fgdsetting_module.md#examples)
- [Return Values](fmgr_fmupdate_webspam_fgdsetting_module.md#return-values)

## [Synopsis](fmgr_fmupdate_webspam_fgdsetting_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_fmupdate_webspam_fgdsetting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **fmupdate_webspam_fgdsetting**  dictionary | the top level parameters set |
| **as-cache**  integer | Antispam service maximum memory usage in megabytes |
| **as-log**  string | Antispam log setting  disable - Disable spam log.  nospam - Log non-spam events.  all - Log all spam lookups.  **Choices:**   - `"disable"` - `"nospam"` - `"all"` |
| **as-preload**  string | Enable/disable preloading antispam database to memory  disable - Disable antispam database preload.  enable - Enable antispam database preload.  **Choices:**   - `"disable"` - `"enable"` |
| **av-cache**  integer | Antivirus service maximum memory usage, in megabytes |
| **av-log**  string | Antivirus log setting  disable - Disable virus log.  novirus - Log non-virus events.  all - Log all virus lookups.  **Choices:**   - `"disable"` - `"novirus"` - `"all"` |
| **av-preload**  string | Enable/disable preloading antivirus database to memory  disable - Disable antivirus database preload.  enable - Enable antivirus database preload.  **Choices:**   - `"disable"` - `"enable"` |
| **av2-cache**  integer | Antispam service maximum memory usage in megabytes |
| **av2-log**  string | Outbreak prevention log setting  disable - Disable av2 log.  noav2 - Log non-av2 events.  all - Log all av2 lookups.  **Choices:**   - `"disable"` - `"noav2"` - `"all"` |
| **av2-preload**  string | Enable/disable preloading outbreak prevention database to memory  disable - Disable outbreak prevention database preload.  enable - Enable outbreak prevention database preload.  **Choices:**   - `"disable"` - `"enable"` |
| **eventlog-query**  string | Enable/disable record query to event-log besides fgd-log  disable - Record query to event-log besides fgd-log.  enable - Do not log to event-log.  **Choices:**   - `"disable"` - `"enable"` |
| **fgd-pull-interval**  integer | Fgd pull interval setting, in minutes |
| **fq-cache**  integer | File query service maximum memory usage, in megabytes |
| **fq-log**  string | File query log setting  disable - Disable file query log.  nofilequery - Log non-file query events.  all - Log all file query events.  **Choices:**   - `"disable"` - `"nofilequery"` - `"all"` |
| **fq-preload**  string | Enable/disable preloading file query database to memory  disable - Disable file query db preload.  enable - Enable file query db preload.  **Choices:**   - `"disable"` - `"enable"` |
| **iot-cache**  integer | IoT service maximum memory usage, in megabytes |
| **iot-log**  string | IoT log setting  disable - Disable IoT log.  nofilequery - Log non-IoT events.  all - Log all IoT events.  **Choices:**   - `"disable"` - `"nofilequery"` - `"all"` |
| **iot-preload**  string | Enable/disable preloading IoT database to memory  disable - Disable IoT db preload.  enable - Enable IoT db preload.  **Choices:**   - `"disable"` - `"enable"` |
| **iotv-preload**  string | Enable/disable preloading IoT-Vulnerability database to memory  disable - Disable IoT-Vulnerability db preload.  enable - Enable IoT-Vulnerability db preload.  **Choices:**   - `"disable"` - `"enable"` |
| **linkd-log**  string | Linkd log setting  emergency - The unit is unusable.  alert - Immediate action is required  critical - Functionality is affected.  error - Functionality is probably affected.  warn - Functionality might be affected.  notice - Information about normal events.  info - General information.  debug - Debug information.  disable - Linkd logging is disabled.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warn"` - `"notice"` - `"info"` - `"debug"` - `"disable"` |
| **max-client-worker**  integer | max worker for tcp client connection |
| **max-log-quota**  integer | Maximum log quota setting, in megabytes |
| **max-unrated-site**  integer | Maximum number of unrated site in memory, in kilobytes |
| **restrict-as1-dbver**  string | Restrict system update to indicated antispam |
| **restrict-as2-dbver**  string | Restrict system update to indicated antispam |
| **restrict-as4-dbver**  string | Restrict system update to indicated antispam |
| **restrict-av-dbver**  string | Restrict system update to indicated antivirus database version |
| **restrict-av2-dbver**  string | Restrict system update to indicated outbreak prevention database version |
| **restrict-fq-dbver**  string | Restrict system update to indicated file query database version |
| **restrict-iots-dbver**  string | Restrict system update to indicated file query database version |
| **restrict-wf-dbver**  string | Restrict system update to indicated web filter database version |
| **server-override**  dictionary | no description |
| **servlist**  list / elements=dictionary | Servlist. |
| **id**  integer | Override server ID |
| **ip**  string | IPv4 address of the override server. |
| **ip6**  string | IPv6 address of the override server. |
| **port**  integer | Port number to use when contacting FortiGuard |
| **service-type**  any | (list or str)  Override service type.  fgd - Server override config for fgd  fgc - Server override config for fgc  fsa - Server override config for fsa  **Choices:**   - `"fgd"` - `"fgc"` - `"fsa"` |
| **status**  string | Override status.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **stat-log-interval**  integer | Statistic log interval setting, in minutes |
| **stat-sync-interval**  integer | Synchronization interval for statistic of unrated site in minutes |
| **update-interval**  integer | FortiGuard database update wait time if not enough delta files, in hours |
| **update-log**  string | Enable/disable update log setting  disable - Disable update log.  enable - Enable update log.  **Choices:**   - `"disable"` - `"enable"` |
| **wf-cache**  integer | Web filter service maximum memory usage, in megabytes |
| **wf-dn-cache-expire-time**  integer | Web filter DN cache expire time, in minutes |
| **wf-dn-cache-max-number**  integer | Maximum number of Web filter DN cache |
| **wf-log**  string | Web filter log setting  disable - Disable URL log.  nourl - Log non-URL events.  all - Log all URL lookups.  **Choices:**   - `"disable"` - `"nourl"` - `"all"` |
| **wf-preload**  string | Enable/disable preloading the web filter database into memory  disable - Disable web filter database preload.  enable - Enable web filter database preload.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_fmupdate_webspam_fgdsetting_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_fmupdate_webspam_fgdsetting_module.md#id4)

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
    - name: Configure the FortiGuard run parameters.
      fmgr_fmupdate_webspam_fgdsetting:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        fmupdate_webspam_fgdsetting:
          as-cache: <integer>
          as-log: <value in [disable, nospam, all]>
          as-preload: <value in [disable, enable]>
          av-cache: <integer>
          av-log: <value in [disable, novirus, all]>
          av-preload: <value in [disable, enable]>
          av2-cache: <integer>
          av2-log: <value in [disable, noav2, all]>
          av2-preload: <value in [disable, enable]>
          eventlog-query: <value in [disable, enable]>
          fgd-pull-interval: <integer>
          fq-cache: <integer>
          fq-log: <value in [disable, nofilequery, all]>
          fq-preload: <value in [disable, enable]>
          linkd-log: <value in [emergency, alert, critical, ...]>
          max-client-worker: <integer>
          max-log-quota: <integer>
          max-unrated-site: <integer>
          restrict-as1-dbver: <string>
          restrict-as2-dbver: <string>
          restrict-as4-dbver: <string>
          restrict-av-dbver: <string>
          restrict-av2-dbver: <string>
          restrict-fq-dbver: <string>
          restrict-wf-dbver: <string>
          server-override:
            servlist:
              -
                id: <integer>
                ip: <string>
                ip6: <string>
                port: <integer>
                service-type: # <list or string>
                  - fgd
                  - fgc
                  - fsa
            status: <value in [disable, enable]>
          stat-log-interval: <integer>
          stat-sync-interval: <integer>
          update-interval: <integer>
          update-log: <value in [disable, enable]>
          wf-cache: <integer>
          wf-dn-cache-expire-time: <integer>
          wf-dn-cache-max-number: <integer>
          wf-log: <value in [disable, nourl, all]>
          wf-preload: <value in [disable, enable]>
          iot-cache: <integer>
          iot-log: <value in [disable, nofilequery, all]>
          iot-preload: <value in [disable, enable]>
          restrict-iots-dbver: <string>
          iotv-preload: <value in [disable, enable]>
```

## [Return Values](fmgr_fmupdate_webspam_fgdsetting_module.md#id5)

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
