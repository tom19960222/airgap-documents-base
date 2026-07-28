---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_fmupdate_fdssetting module – Configure FortiGuard settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_fmupdate_fdssetting_module.html
fetched_at: 2026-07-28T02:13:34+00:00
---
# fortinet.fortimanager.fmgr_fmupdate_fdssetting module – Configure FortiGuard settings.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fmupdate_fdssetting`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_fmupdate_fdssetting_module.md#synopsis)
- [Parameters](fmgr_fmupdate_fdssetting_module.md#parameters)
- [Notes](fmgr_fmupdate_fdssetting_module.md#notes)
- [Examples](fmgr_fmupdate_fdssetting_module.md#examples)
- [Return Values](fmgr_fmupdate_fdssetting_module.md#return-values)

## [Synopsis](fmgr_fmupdate_fdssetting_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_fmupdate_fdssetting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **fmupdate_fdssetting**  dictionary | the top level parameters set |
| **fds-clt-ssl-protocol**  string | The SSL protocols version for connecting fds server  sslv3 - set SSLv3 as the client version.  tlsv1.  tlsv1.  tlsv1.  **Choices:**   - `"sslv3"` - `"tlsv1.0"` - `"tlsv1.1"` - `"tlsv1.2"` - `"tlsv1.3"` |
| **fds-ssl-protocol**  string | The SSL protocols version for receiving fgt connection  sslv3 - set SSLv3 as the lowest version.  tlsv1.  tlsv1.  tlsv1.  **Choices:**   - `"sslv3"` - `"tlsv1.0"` - `"tlsv1.1"` - `"tlsv1.2"` - `"tlsv1.3"` |
| **fmtr-log**  string | fmtr log level  emergency - Log level - emergency  alert - Log level - alert  critical - Log level - critical  error - Log level - error  warn - Log level - warn  notice - Log level - notice  info - Log level - info  debug - Log level - debug  disable - Disable linkd log  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warn"` - `"notice"` - `"info"` - `"debug"` - `"disable"` |
| **fortiguard-anycast**  string | Enable/disable use of FortiGuards anycast network  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **fortiguard-anycast-source**  string | Configure which of Fortinets servers to provide FortiGuard services in FortiGuards anycast network.  fortinet - Use Fortinets servers to provide FortiGuard services in FortiGuards anycast network.  aws - Use Fortinets AWS servers to provide FortiGuard services in FortiGuards anycast network.  **Choices:**   - `"fortinet"` - `"aws"` |
| **linkd-log**  string | The linkd log level  emergency - Log level - emergency  alert - Log level - alert  critical - Log level - critical  error - Log level - error  warn - Log level - warn  notice - Log level - notice  info - Log level - info  debug - Log level - debug  disable - Disable linkd log  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warn"` - `"notice"` - `"info"` - `"debug"` - `"disable"` |
| **max-av-ips-version**  integer | The maximum number of downloadable, full version AV/IPS packages |
| **max-work**  integer | The maximum number of worker processing download requests |
| **push-override**  dictionary | no description |
| **ip**  string | External or virtual IP address of the NAT device that will forward push messages to the FortiManager unit. |
| **port**  integer | Receiving port number on the NAT device |
| **status**  string | Enable/disable push updates for clients  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **push-override-to-client**  dictionary | no description |
| **announce-ip**  list / elements=dictionary | Announce-Ip. |
| **id**  integer | ID of the announce IP address |
| **ip**  string | Announce IPv4 address. |
| **port**  integer | Announce IP port |
| **status**  string | Enable/disable push updates  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **send_report**  string | send report/fssi to fds server.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **send_setup**  string | forward setup to fds server.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **server-override**  dictionary | no description |
| **servlist**  list / elements=dictionary | Servlist. |
| **id**  integer | Override server ID |
| **ip**  string | IPv4 address of the override server. |
| **ip6**  string | IPv6 address of the override server. |
| **port**  integer | Port number to use when contacting FortiGuard |
| **service-type**  any | (list or str)  Override service type.  fct - Server override config for fct  fds - Server override config for fds  **Choices:**   - `"fds"` - `"fct"` |
| **status**  string | Override status.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **system-support-faz**  list / elements=string | no description  **Choices:**   - `"6.x"` - `"7.x"` |
| **system-support-fct**  list / elements=string | Supported FortiClient versions.                       **Choices:**   - `"4.x"` - `"5.0"` - `"5.2"` - `"5.4"` - `"5.6"` - `"6.0"` - `"6.2"` - `"6.4"` - `"7.0"` |
| **system-support-fdc**  list / elements=string | no description  **Choices:**   - `"3.x"` - `"4.x"` |
| **system-support-fgt**  list / elements=string | Supported FortiOS versions.                **Choices:**   - `"5.4"` - `"5.6"` - `"6.0"` - `"6.2"` - `"6.4"` - `"7.0"` - `"7.2"` - `"7.4"` |
| **system-support-fis**  list / elements=string | no description  **Choices:**   - `"1.x"` - `"2.x"` |
| **system-support-fml**  list / elements=string | Supported FortiMail versions.        **Choices:**   - `"4.x"` - `"5.x"` - `"6.x"` - `"6.0"` - `"6.2"` - `"6.4"` - `"7.0"` - `"7.2"` |
| **system-support-fsa**  list / elements=string | Supported FortiSandbox versions.        **Choices:**   - `"1.x"` - `"2.x"` - `"3.x"` - `"4.x"` - `"3.0"` - `"3.1"` - `"3.2"` |
| **system-support-fsw**  list / elements=string | Supported FortiSwitch versions.                       **Choices:**   - `"5.4"` - `"5.6"` - `"6.0"` - `"6.2"` - `"4.x"` - `"5.0"` - `"5.2"` - `"6.4"` |
| **system-support-fts**  list / elements=string | no description  **Choices:**   - `"3.x"` - `"4.x"` - `"7.x"` |
| **umsvc-log**  string | The um_service log level  emergency - Log level - emergency  alert - Log level - alert  critical - Log level - critical  error - Log level - error  warn - Log level - warn  notice - Log level - notice  info - Log level - info  debug - Log level - debug  disable - Disable linkd log  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warn"` - `"notice"` - `"info"` - `"debug"` - `"disable"` |
| **unreg-dev-option**  string | set the option for unregister devices  ignore - Ignore all unregistered devices.  svc-only - Allow update requests without adding the device.  add-service - Add unregistered devices and allow update request.  **Choices:**   - `"ignore"` - `"svc-only"` - `"add-service"` |
| **update-schedule**  dictionary | no description |
| **day**  string | Configure the day the update will occur, if the freqnecy is weekly  Sunday - Update every Sunday.  Monday - Update every Monday.  Tuesday - Update every Tuesday.  Wednesday - Update every Wednesday.  Thursday - Update every Thursday.  Friday - Update every Friday.  Saturday - Update every Saturday.  **Choices:**   - `"Sunday"` - `"Monday"` - `"Tuesday"` - `"Wednesday"` - `"Thursday"` - `"Friday"` - `"Saturday"` |
| **frequency**  string | Configure update frequency  every - Time interval.  daily - Every day.  weekly - Every week.  **Choices:**   - `"every"` - `"daily"` - `"weekly"` |
| **status**  string | Enable/disable scheduled updates.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **time**  any | (list) Time interval between updates, or the hour and minute when the update occurs |
| **User-Agent**  string | Configure the user agent string. |
| **wanip-query-mode**  string | public ip query mode  disable - Do not query public ip  ipify - Get public IP through https  **Choices:**   - `"disable"` - `"ipify"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_fmupdate_fdssetting_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_fmupdate_fdssetting_module.md#id4)

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
    - name: Configure FortiGuard settings.
      fmgr_fmupdate_fdssetting:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        fmupdate_fdssetting:
          User-Agent: <string>
          fds-clt-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...]>
          fds-ssl-protocol: <value in [sslv3, tlsv1.0, tlsv1.1, ...]>
          fmtr-log: <value in [emergency, alert, critical, ...]>
          linkd-log: <value in [emergency, alert, critical, ...]>
          max-av-ips-version: <integer>
          max-work: <integer>
          push-override:
            ip: <string>
            port: <integer>
            status: <value in [disable, enable]>
          push-override-to-client:
            announce-ip:
              -
                id: <integer>
                ip: <string>
                port: <integer>
            status: <value in [disable, enable]>
          send_report: <value in [disable, enable]>
          send_setup: <value in [disable, enable]>
          server-override:
            servlist:
              -
                id: <integer>
                ip: <string>
                ip6: <string>
                port: <integer>
                service-type: # <list or string>
                  - fds
                  - fct
            status: <value in [disable, enable]>
          system-support-fct:
            - 4.x
            - 5.0
            - 5.2
            - 5.4
            - 5.6
            - 6.0
            - 6.2
            - 6.4
            - 7.0
          system-support-fgt:
            - 5.4
            - 5.6
            - 6.0
            - 6.2
            - 6.4
            - 7.0
            - 7.2
            - 7.4
          system-support-fml:
            - 4.x
            - 5.x
            - 6.x
            - 6.0
            - 6.2
            - 6.4
            - 7.0
            - 7.2
          system-support-fsa:
            - 1.x
            - 2.x
            - 3.x
            - 4.x
            - 3.0
            - 3.1
            - 3.2
          system-support-fsw:
            - 5.4
            - 5.6
            - 6.0
            - 6.2
            - 4.x
            - 5.0
            - 5.2
            - 6.4
          umsvc-log: <value in [emergency, alert, critical, ...]>
          unreg-dev-option: <value in [ignore, svc-only, add-service]>
          update-schedule:
            day: <value in [Sunday, Monday, Tuesday, ...]>
            frequency: <value in [every, daily, weekly]>
            status: <value in [disable, enable]>
            time: <list or string>
          wanip-query-mode: <value in [disable, ipify]>
          fortiguard-anycast: <value in [disable, enable]>
          fortiguard-anycast-source: <value in [fortinet, aws]>
          system-support-fdc:
            - 3.x
            - 4.x
          system-support-fts:
            - 3.x
            - 4.x
            - 7.x
          system-support-faz:
            - 6.x
            - 7.x
          system-support-fis:
            - 1.x
            - 2.x
```

## [Return Values](fmgr_fmupdate_fdssetting_module.md#id5)

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
