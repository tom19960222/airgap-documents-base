---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_admin_user module – Admin user."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_admin_user_module.html
fetched_at: 2026-07-28T02:17:59+00:00
---
# fortinet.fortimanager.fmgr_system_admin_user module – Admin user.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_admin_user`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_admin_user_module.md#synopsis)
- [Parameters](fmgr_system_admin_user_module.md#parameters)
- [Notes](fmgr_system_admin_user_module.md#notes)
- [Examples](fmgr_system_admin_user_module.md#examples)
- [Return Values](fmgr_system_admin_user_module.md#return-values)

## [Synopsis](fmgr_system_admin_user_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_admin_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **system_admin_user**  dictionary | the top level parameters set |
| **adom**  list / elements=dictionary | Adom. |
| **adom-name**  string | Admin domain names. |
| **adom-access**  string | set all/specify/exclude adom access mode.  all - All ADOMs access.  specify - Specify ADOMs access.  exclude - Exclude ADOMs access.  **Choices:**   - `"all"` - `"specify"` - `"exclude"` - `"per-adom-profile"` |
| **adom-exclude**  list / elements=dictionary | Adom-Exclude. |
| **adom-name**  string | Admin domain names. |
| **app-filter**  list / elements=dictionary | App-Filter. |
| **app-filter-name**  string | App filter name. |
| **avatar**  string | Image file for avatar |
| **ca**  string | PKI user certificate CA |
| **change-password**  string | Enable/disable restricted user to change self password.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **cors-allow-origin**  string | Access-Control-Allow-Origin. |
| **dashboard**  list / elements=dictionary | Dashboard. |
| **column**  integer | Widgets column ID. |
| **diskio-content-type**  string | Disk I/O Monitor widgets chart type.  util - bandwidth utilization.  iops - the number of I/O requests.  blks - the amount of data of I/O requests.  **Choices:**   - `"util"` - `"iops"` - `"blks"` |
| **diskio-period**  string | Disk I/O Monitor widgets data period.  1hour - 1 hour.  8hour - 8 hour.  24hour - 24 hour.  **Choices:**   - `"1hour"` - `"8hour"` - `"24hour"` |
| **log-rate-period**  string | Log receive monitor widgets data period.  2min - 2 minutes.  1hour - 1 hour.  6hours - 6 hours.  **Choices:**   - `"2min"` - `"1hour"` - `"6hours"` |
| **log-rate-topn**  string | Log receive monitor widgets number of top items to display.  1 - Top 1.  2 - Top 2.  3 - Top 3.  4 - Top 4.  5 - Top 5.  **Choices:**   - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` |
| **log-rate-type**  string | Log receive monitor widgets statistics breakdown options.  log - Show log rates for each log type.  device - Show log rates for each device.  **Choices:**   - `"log"` - `"device"` |
| **moduleid**  integer | Widget ID. |
| **name**  string | Widget name. |
| **num-entries**  integer | Number of entries. |
| **refresh-interval**  integer | Widgets refresh interval. |
| **res-cpu-display**  string | Widgets CPU display type.  average - Average usage of CPU.  each - Each usage of CPU.  **Choices:**   - `"average"` - `"each"` |
| **res-period**  string | Widgets data period.  10min - Last 10 minutes.  hour - Last hour.  day - Last day.  **Choices:**   - `"10min"` - `"hour"` - `"day"` |
| **res-view-type**  string | Widgets data view type.  real-time - Real-time view.  history - History view.  **Choices:**   - `"real-time"` - `"history"` |
| **status**  string | Widgets opened/closed state.  close - Widget closed.  open - Widget opened.  **Choices:**   - `"close"` - `"open"` |
| **tabid**  integer | ID of tab where widget is displayed. |
| **time-period**  string | Log Database Monitor widgets data period.  1hour - 1 hour.  8hour - 8 hour.  24hour - 24 hour.  **Choices:**   - `"1hour"` - `"8hour"` - `"24hour"` |
| **widget-type**  string | Widget type.  top-lograte - Log Receive Monitor.  sysres - System resources.  sysinfo - System Information.  licinfo - License Information.  jsconsole - CLI Console.  sysop - Unit Operation.  alert - Alert Message Console.  statistics - Statistics.  rpteng - Report Engine.  raid - Disk Monitor.  logrecv - Logs/Data Received.  devsummary - Device Summary.  logdb-perf - Log Database Performance Monitor.  logdb-lag - Log Database Lag Time.  disk-io - Disk I/O.  log-rcvd-fwd - Log receive and forwarding Monitor.  **Choices:**   - `"top-lograte"` - `"sysres"` - `"sysinfo"` - `"licinfo"` - `"jsconsole"` - `"sysop"` - `"alert"` - `"statistics"` - `"rpteng"` - `"raid"` - `"logrecv"` - `"devsummary"` - `"logdb-perf"` - `"logdb-lag"` - `"disk-io"` - `"log-rcvd-fwd"` |
| **dashboard-tabs**  list / elements=dictionary | Dashboard-Tabs. |
| **name**  string | Tab name. |
| **tabid**  integer | Tab ID. |
| **description**  string | Description. |
| **dev-group**  string | device group. |
| **email-address**  string | Email address. |
| **ext-auth-accprofile-override**  string | Allow to use the access profile provided by the remote authentication server.  disable - Disable access profile override.  enable - Enable access profile override.  **Choices:**   - `"disable"` - `"enable"` |
| **ext-auth-adom-override**  string | Allow to use the ADOM provided by the remote authentication server.  disable - Disable ADOM override.  enable - Enable ADOM override.  **Choices:**   - `"disable"` - `"enable"` |
| **ext-auth-group-match**  string | Only administrators belonging to this group can login. |
| **fingerprint**  string | PKI user certificate fingerprint |
| **first-name**  string | First name. |
| **force-password-change**  string | Enable/disable force password change on next login.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **group**  string | Group name. |
| **hidden**  integer | Hidden administrator. |
| **ips-filter**  list / elements=dictionary | Ips-Filter. |
| **ips-filter-name**  string | IPS filter name. |
| **ipv6_trusthost1**  string | Admin user trusted host IPv6, default |
| **ipv6_trusthost10**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost2**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost3**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost4**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost5**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost6**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost7**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost8**  string | Admin user trusted host IPv6, default ffff |
| **ipv6_trusthost9**  string | Admin user trusted host IPv6, default ffff |
| **last-name**  string | Last name. |
| **ldap-server**  string | LDAP server name. |
| **login-max**  integer | Max login session for this user. |
| **meta-data**  list / elements=dictionary | Meta-Data. |
| **fieldlength**  integer | Field length. |
| **fieldname**  string | Field name. |
| **fieldvalue**  string | Field value. |
| **importance**  string | Importance.  optional - This field is optional.  required - This field is required.  **Choices:**   - `"optional"` - `"required"` |
| **status**  string | Status.  disabled - This field is disabled.  enabled - This field is enabled.  **Choices:**   - `"disabled"` - `"enabled"` |
| **mobile-number**  string | Mobile number. |
| **pager-number**  string | Pager number. |
| **password**  any | (list) Password. |
| **password-expire**  any | (list or str) Password expire time in GMT. |
| **phone-number**  string | Phone number. |
| **policy-package**  list / elements=dictionary | Policy-Package. |
| **policy-package-name**  string | Policy package names. |
| **profileid**  string | Profile ID. |
| **radius_server**  string | RADIUS server name. |
| **restrict-access**  string | Enable/disable restricted access to development VDOM.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **restrict-dev-vdom**  list / elements=dictionary | no description |
| **dev-vdom**  string | Device or device VDOM. |
| **rpc-permit**  string | set none/read/read-write rpc-permission.  read-write - Read-write permission.  none - No permission.  read - Read-only permission.  **Choices:**   - `"read-write"` - `"none"` - `"read"` - `"from-profile"` |
| **ssh-public-key1**  any | (list) SSH public key 1. |
| **ssh-public-key2**  any | (list) SSH public key 2. |
| **ssh-public-key3**  any | (list) SSH public key 3. |
| **subject**  string | PKI user certificate name constraints. |
| **tacacs-plus-server**  string | TACACS+ server name. |
| **th-from-profile**  integer | Internal use only |
| **th6-from-profile**  integer | Internal use only |
| **trusthost1**  string | Admin user trusted host IP, default 0. |
| **trusthost10**  string | Admin user trusted host IP, default 255. |
| **trusthost2**  string | Admin user trusted host IP, default 255. |
| **trusthost3**  string | Admin user trusted host IP, default 255. |
| **trusthost4**  string | Admin user trusted host IP, default 255. |
| **trusthost5**  string | Admin user trusted host IP, default 255. |
| **trusthost6**  string | Admin user trusted host IP, default 255. |
| **trusthost7**  string | Admin user trusted host IP, default 255. |
| **trusthost8**  string | Admin user trusted host IP, default 255. |
| **trusthost9**  string | Admin user trusted host IP, default 255. |
| **two-factor-auth**  string | Enable 2-factor authentication  disable - Disable 2-factor authentication.  enable - Enable 2-factor authentication.  **Choices:**   - `"disable"` - `"enable"` - `"password"` - `"ftc-ftm"` - `"ftc-email"` - `"ftc-sms"` |
| **use-global-theme**  string | Enable/disble global theme for administration GUI.  disable - Disable setting.  enable - Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **user-theme**  string | Color scheme to use for the admin user GUI.  blue - Blueberry  green - Kiwi  red - Cherry  melongene - Plum  spring - Spring  summer - Summer  autumn - Autumn  winter - Winter  circuit-board - Circuit Board  calla-lily - Calla Lily  binary-tunnel - Binary Tunnel  mars - Mars  blue-sea - Blue Sea  technology - Technology  landscape - Landscape  twilight - Twilight  canyon - Canyon  northern-light - Northern Light  astronomy - Astronomy  fish - Fish  penguin - Penguin  mountain - Mountain  panda - Panda  parrot - Parrot  cave - Cave  zebra - Zebra  contrast-dark - High Contrast Dark  **Choices:**   - `"blue"` - `"green"` - `"red"` - `"melongene"` - `"spring"` - `"summer"` - `"autumn"` - `"winter"` - `"circuit-board"` - `"calla-lily"` - `"binary-tunnel"` - `"mars"` - `"blue-sea"` - `"technology"` - `"landscape"` - `"twilight"` - `"canyon"` - `"northern-light"` - `"astronomy"` - `"fish"` - `"penguin"` - `"mountain"` - `"panda"` - `"parrot"` - `"cave"` - `"zebra"` - `"contrast-dark"` - `"mariner"` - `"jade"` - `"neutrino"` - `"dark-matter"` - `"forest"` - `"cat"` - `"graphite"` |
| **user_type**  string | User type.  local - Local user.  radius - RADIUS user.  ldap - LDAP user.  tacacs-plus - TACACS+ user.  pki-auth - PKI user.  group - Group user.  **Choices:**   - `"local"` - `"radius"` - `"ldap"` - `"tacacs-plus"` - `"pki-auth"` - `"group"` - `"sso"` - `"api"` |
| **userid**  string / required | User name. |
| **web-filter**  list / elements=dictionary | Web-Filter. |
| **web-filter-name**  string | Web filter name. |
| **wildcard**  string | Enable/disable wildcard remote authentication.  disable - Disable username wildcard.  enable - Enable username wildcard.  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_admin_user_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_admin_user_module.md#id4)

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
   - name: Admin User
     fmgr_system_admin_user:
        state: present
        system_admin_user:
            adom:
             - adom-name: ansible
            userid: 'ansible-test'
   - name: Admin domain.
     fmgr_system_admin_user_adom:
        bypass_validation: False
        user: ansible-test # userid
        state: present
        system_admin_user_adom:
           adom-name: 'ALL ADOMS'
```

## [Return Values](fmgr_system_admin_user_module.md#id5)

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
