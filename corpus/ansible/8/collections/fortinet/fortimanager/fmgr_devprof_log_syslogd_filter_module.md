---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_devprof_log_syslogd_filter module – Filters for remote system server."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_devprof_log_syslogd_filter_module.html
fetched_at: 2026-07-28T02:08:44+00:00
---
# fortinet.fortimanager.fmgr_devprof_log_syslogd_filter module – Filters for remote system server.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_devprof_log_syslogd_filter`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_devprof_log_syslogd_filter_module.md#synopsis)
- [Parameters](fmgr_devprof_log_syslogd_filter_module.md#parameters)
- [Notes](fmgr_devprof_log_syslogd_filter_module.md#notes)
- [Examples](fmgr_devprof_log_syslogd_filter_module.md#examples)
- [Return Values](fmgr_devprof_log_syslogd_filter_module.md#return-values)

## [Synopsis](fmgr_devprof_log_syslogd_filter_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_devprof_log_syslogd_filter_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **devprof**  string / required | the parameter (devprof) in requested url |
| **devprof_log_syslogd_filter**  dictionary | the top level parameters set |
| **anomaly**  string | Enable/disable anomaly logging.  **Choices:**   - `"disable"` - `"enable"` |
| **cifs**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dns**  string | Enable/disable detailed DNS event logging.  **Choices:**   - `"disable"` - `"enable"` |
| **exclude-list**  list / elements=dictionary | no description |
| **category**  string | no description  **Choices:**   - `"app-ctrl"` - `"attack"` - `"dlp"` - `"event"` - `"traffic"` - `"virus"` - `"voip"` - `"webfilter"` - `"netscan"` - `"spam"` - `"anomaly"` - `"waf"` |
| **fields**  list / elements=dictionary | no description |
| **args**  any | (list) no description |
| **field**  string | no description |
| **negate**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer | no description |
| **filter**  string | Syslog filter. |
| **filter-type**  string | Include/exclude logs that match the filter.  **Choices:**   - `"include"` - `"exclude"` |
| **forward-traffic**  string | Enable/disable forward traffic logging.  **Choices:**   - `"disable"` - `"enable"` |
| **free-style**  list / elements=dictionary | no description |
| **category**  string | Log category.  **Choices:**   - `"traffic"` - `"event"` - `"virus"` - `"webfilter"` - `"attack"` - `"spam"` - `"voip"` - `"dlp"` - `"app-ctrl"` - `"anomaly"` - `"waf"` - `"gtp"` - `"dns"` - `"ssh"` - `"ssl"` - `"file-filter"` - `"icap"` - `"ztna"` - `"virtual-patch"` |
| **filter**  string | Free style filter string. |
| **filter-type**  string | Include/exclude logs that match the filter.  **Choices:**   - `"include"` - `"exclude"` |
| **id**  integer | Entry ID. |
| **gtp**  string | Enable/disable GTP messages logging.  **Choices:**   - `"disable"` - `"enable"` |
| **local-traffic**  string | Enable/disable local in or out traffic logging.  **Choices:**   - `"disable"` - `"enable"` |
| **multicast-traffic**  string | Enable/disable multicast traffic logging.  **Choices:**   - `"disable"` - `"enable"` |
| **netscan-discovery**  string | Enable/disable netscan discovery event logging.  **Choices:**   - `"disable"` - `"enable"` |
| **netscan-vulnerability**  string | Enable/disable netscan vulnerability event logging.  **Choices:**   - `"disable"` - `"enable"` |
| **severity**  string | Lowest severity level to log.  **Choices:**   - `"emergency"` - `"alert"` - `"critical"` - `"error"` - `"warning"` - `"notification"` - `"information"` - `"debug"` |
| **sniffer-traffic**  string | Enable/disable sniffer traffic logging.  **Choices:**   - `"disable"` - `"enable"` |
| **ssh**  string | Enable/disable SSH logging.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **voip**  string | Enable/disable VoIP logging.  **Choices:**   - `"disable"` - `"enable"` |
| **ztna-traffic**  string | Enable/disable ztna traffic logging.  **Choices:**   - `"disable"` - `"enable"` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_devprof_log_syslogd_filter_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_devprof_log_syslogd_filter_module.md#id4)

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
    - name: Filters for remote system server.
      fmgr_devprof_log_syslogd_filter:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        devprof: <your own value>
        devprof_log_syslogd_filter:
          severity: <value in [emergency, alert, critical, ...]>
          anomaly: <value in [disable, enable]>
          exclude-list:
            -
              category: <value in [app-ctrl, attack, dlp, ...]>
              fields:
                -
                  args: <list or string>
                  field: <string>
                  negate: <value in [disable, enable]>
              id: <integer>
          forward-traffic: <value in [disable, enable]>
          free-style:
            -
              category: <value in [traffic, event, virus, ...]>
              filter: <string>
              filter-type: <value in [include, exclude]>
              id: <integer>
          gtp: <value in [disable, enable]>
          local-traffic: <value in [disable, enable]>
          multicast-traffic: <value in [disable, enable]>
          sniffer-traffic: <value in [disable, enable]>
          voip: <value in [disable, enable]>
          ztna-traffic: <value in [disable, enable]>
          filter-type: <value in [include, exclude]>
          filter: <string>
          cifs: <value in [disable, enable]>
          ssl: <value in [disable, enable]>
          dns: <value in [disable, enable]>
          ssh: <value in [disable, enable]>
          netscan-discovery: <value in [disable, enable]>
          netscan-vulnerability: <value in [disable, enable]>
```

## [Return Values](fmgr_devprof_log_syslogd_filter_module.md#id5)

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
