---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_devprof_log_fortianalyzercloud_setting module – Global FortiAnalyzer Cloud settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_devprof_log_fortianalyzercloud_setting_module.html
fetched_at: 2026-07-28T02:08:43+00:00
---
# fortinet.fortimanager.fmgr_devprof_log_fortianalyzercloud_setting module – Global FortiAnalyzer Cloud settings.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_devprof_log_fortianalyzercloud_setting`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_devprof_log_fortianalyzercloud_setting_module.md#synopsis)
- [Parameters](fmgr_devprof_log_fortianalyzercloud_setting_module.md#parameters)
- [Notes](fmgr_devprof_log_fortianalyzercloud_setting_module.md#notes)
- [Examples](fmgr_devprof_log_fortianalyzercloud_setting_module.md#examples)
- [Return Values](fmgr_devprof_log_fortianalyzercloud_setting_module.md#return-values)

## [Synopsis](fmgr_devprof_log_fortianalyzercloud_setting_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_devprof_log_fortianalyzercloud_setting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **devprof**  string / required | the parameter (devprof) in requested url |
| **devprof_log_fortianalyzercloud_setting**  dictionary | the top level parameters set |
| **__change_ip**  integer | Hidden attribute. |
| **access-config**  string | Enable/disable FortiAnalyzer access to configuration and data.  **Choices:**   - `"disable"` - `"enable"` |
| **certificate**  string | Certificate used to communicate with FortiAnalyzer. |
| **certificate-verification**  string | Enable/disable identity verification of FortiAnalyzer by use of certificate.  **Choices:**   - `"disable"` - `"enable"` |
| **conn-timeout**  integer | FortiAnalyzer connection time-out in seconds |
| **enc-algorithm**  string | Configure the level of SSL protection for secure communication with FortiAnalyzer.  **Choices:**   - `"high"` - `"low"` - `"high-medium"` - `"low-medium"` |
| **hmac-algorithm**  string | FortiAnalyzer IPsec tunnel HMAC algorithm.  **Choices:**   - `"sha256"` - `"sha1"` |
| **interface**  string | Specify outgoing interface to reach server. |
| **interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **ips-archive**  string | Enable/disable IPS packet archive logging.  **Choices:**   - `"disable"` - `"enable"` |
| **max-log-rate**  integer | FortiAnalyzer maximum log rate in MBps |
| **monitor-failure-retry-period**  integer | Time between FortiAnalyzer connection retries in seconds |
| **monitor-keepalive-period**  integer | Time between OFTP keepalives in seconds |
| **preshared-key**  string | Preshared-key used for auto-authorization on FortiAnalyzer. |
| **priority**  string | Set log transmission priority.  **Choices:**   - `"low"` - `"default"` |
| **serial**  any | (list) no description |
| **source-ip**  string | Source IPv4 or IPv6 address used to communicate with FortiAnalyzer. |
| **ssl-min-proto-version**  string | Minimum supported protocol version for SSL/TLS connections  **Choices:**   - `"default"` - `"TLSv1-1"` - `"TLSv1-2"` - `"SSLv3"` - `"TLSv1"` - `"TLSv1-3"` |
| **status**  string | Enable/disable logging to FortiAnalyzer.  **Choices:**   - `"disable"` - `"enable"` |
| **upload-day**  string | Day of week |
| **upload-interval**  string | Frequency to upload log files to FortiAnalyzer.  **Choices:**   - `"daily"` - `"weekly"` - `"monthly"` |
| **upload-option**  string | Enable/disable logging to hard disk and then uploading to FortiAnalyzer.  **Choices:**   - `"store-and-upload"` - `"realtime"` - `"1-minute"` - `"5-minute"` |
| **upload-time**  string | Time to upload logs |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_devprof_log_fortianalyzercloud_setting_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_devprof_log_fortianalyzercloud_setting_module.md#id4)

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
    - name: Global FortiAnalyzer Cloud settings.
      fmgr_devprof_log_fortianalyzercloud_setting:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        devprof: <your own value>
        devprof_log_fortianalyzercloud_setting:
          __change_ip: <integer>
          access-config: <value in [disable, enable]>
          certificate: <string>
          conn-timeout: <integer>
          enc-algorithm: <value in [high, low, high-medium, ...]>
          hmac-algorithm: <value in [sha256, sha1]>
          ips-archive: <value in [disable, enable]>
          monitor-failure-retry-period: <integer>
          monitor-keepalive-period: <integer>
          source-ip: <string>
          ssl-min-proto-version: <value in [default, TLSv1-1, TLSv1-2, ...]>
          status: <value in [disable, enable]>
          upload-day: <string>
          upload-interval: <value in [daily, weekly, monthly]>
          upload-option: <value in [store-and-upload, realtime, 1-minute, ...]>
          upload-time: <string>
          max-log-rate: <integer>
          priority: <value in [low, default]>
          interface: <string>
          interface-select-method: <value in [auto, sdwan, specify]>
          preshared-key: <string>
          certificate-verification: <value in [disable, enable]>
          serial: <list or string>
```

## [Return Values](fmgr_devprof_log_fortianalyzercloud_setting_module.md#id5)

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
