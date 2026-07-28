---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_admin_user_dashboard module – Custom dashboard widgets."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_admin_user_dashboard_module.html
fetched_at: 2026-07-28T02:18:02+00:00
---
# fortinet.fortimanager.fmgr_system_admin_user_dashboard module – Custom dashboard widgets.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_admin_user_dashboard`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_system_admin_user_dashboard_module.md#synopsis)
- [Parameters](fmgr_system_admin_user_dashboard_module.md#parameters)
- [Notes](fmgr_system_admin_user_dashboard_module.md#notes)
- [Examples](fmgr_system_admin_user_dashboard_module.md#examples)
- [Return Values](fmgr_system_admin_user_dashboard_module.md#return-values)

## [Synopsis](fmgr_system_admin_user_dashboard_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_admin_user_dashboard_module.md#id2)

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
| **system_admin_user_dashboard**  dictionary | the top level parameters set |
| **column**  integer | Widgets column ID. |
| **diskio-content-type**  string | Disk I/O Monitor widgets chart type.  util - bandwidth utilization.  iops - the number of I/O requests.  blks - the amount of data of I/O requests.  **Choices:**   - `"util"` - `"iops"` - `"blks"` |
| **diskio-period**  string | Disk I/O Monitor widgets data period.  1hour - 1 hour.  8hour - 8 hour.  24hour - 24 hour.  **Choices:**   - `"1hour"` - `"8hour"` - `"24hour"` |
| **log-rate-period**  string | Log receive monitor widgets data period.  2min - 2 minutes.  1hour - 1 hour.  6hours - 6 hours.  **Choices:**   - `"2min"` - `"1hour"` - `"6hours"` |
| **log-rate-topn**  string | Log receive monitor widgets number of top items to display.  1 - Top 1.  2 - Top 2.  3 - Top 3.  4 - Top 4.  5 - Top 5.  **Choices:**   - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` |
| **log-rate-type**  string | Log receive monitor widgets statistics breakdown options.  log - Show log rates for each log type.  device - Show log rates for each device.  **Choices:**   - `"log"` - `"device"` |
| **moduleid**  integer / required | Widget ID. |
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
| **user**  string / required | the parameter (user) in requested url |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_admin_user_dashboard_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_admin_user_dashboard_module.md#id4)

```yaml+jinja
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
   - name: retrieve all the dashboard widgets
     fmgr_fact:
       facts:
           selector: 'system_admin_user_dashboard'
           params:
               user: 'ansible-test'
               dashboard: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Custom dashboard widgets.
     fmgr_system_admin_user_dashboard:
        bypass_validation: False
        user: ansible-test
        state: present
        system_admin_user_dashboard:
           column: 1
           diskio-content-type: util #<value in [util, iops, blks]>
           diskio-period: 1hour #<value in [1hour, 8hour, 24hour]>
           log-rate-period: 1hour #<value in [2min , 1hour, 6hours]>
           log-rate-topn: 5 #<value in [1, 2, 3, ...]>
           log-rate-type: device #<value in [log, device]>
           moduleid: 10
           name: ansible-test-dashboard
           num-entries: 10
           refresh-interval: 0
           res-cpu-display: 'each' #<value in [average , each]>
           res-period: 10min #<value in [10min , hour, day]>
           res-view-type: history #<value in [real-time , history]>
           status: open #<value in [close, open]>
           tabid: 1
           time-period: 1hour #<value in [1hour, 8hour, 24hour]>
           widget-type: sysres #<value in [top-lograte, sysres, sysinfo, ...]>
```

## [Return Values](fmgr_system_admin_user_dashboard_module.md#id5)

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
