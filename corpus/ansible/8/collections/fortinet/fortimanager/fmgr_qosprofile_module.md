---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_qosprofile module – Configure WiFi quality of service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_qosprofile_module.html
fetched_at: 2026-07-28T02:16:21+00:00
---
# fortinet.fortimanager.fmgr_qosprofile module – Configure WiFi quality of service

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_qosprofile`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_qosprofile_module.md#synopsis)
- [Parameters](fmgr_qosprofile_module.md#parameters)
- [Notes](fmgr_qosprofile_module.md#notes)
- [Examples](fmgr_qosprofile_module.md#examples)
- [Return Values](fmgr_qosprofile_module.md#return-values)

## [Synopsis](fmgr_qosprofile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_qosprofile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **qosprofile**  dictionary | the top level parameters set |
| **bandwidth-admission-control**  string | Enable/disable WMM bandwidth admission control.  **Choices:**   - `"disable"` - `"enable"` |
| **bandwidth-capacity**  integer | Maximum bandwidth capacity allowed |
| **burst**  string | Enable/disable client rate burst.  **Choices:**   - `"disable"` - `"enable"` |
| **call-admission-control**  string | Enable/disable WMM call admission control.  **Choices:**   - `"disable"` - `"enable"` |
| **call-capacity**  integer | Maximum number of Voice over WLAN |
| **comment**  string | Comment. |
| **downlink**  integer | Maximum downlink bandwidth for Virtual Access Points |
| **downlink-sta**  integer | Maximum downlink bandwidth for clients |
| **dscp-wmm-be**  any | (list) DSCP mapping for best effort access |
| **dscp-wmm-bk**  any | (list) DSCP mapping for background access |
| **dscp-wmm-mapping**  string | Enable/disable Differentiated Services Code Point  **Choices:**   - `"disable"` - `"enable"` |
| **dscp-wmm-vi**  any | (list) DSCP mapping for video access |
| **dscp-wmm-vo**  any | (list) DSCP mapping for voice access |
| **name**  string / required | WiFi QoS profile name. |
| **uplink**  integer | Maximum uplink bandwidth for Virtual Access Points |
| **uplink-sta**  integer | Maximum uplink bandwidth for clients |
| **wmm**  string | Enable/disable WiFi multi-media  **Choices:**   - `"disable"` - `"enable"` |
| **wmm-be-dscp**  integer | DSCP marking for best effort access |
| **wmm-bk-dscp**  integer | DSCP marking for background access |
| **wmm-dscp-marking**  string | Enable/disable WMM Differentiated Services Code Point  **Choices:**   - `"disable"` - `"enable"` |
| **wmm-uapsd**  string | Enable/disable WMM Unscheduled Automatic Power Save Delivery  **Choices:**   - `"disable"` - `"enable"` |
| **wmm-vi-dscp**  integer | DSCP marking for video access |
| **wmm-vo-dscp**  integer | DSCP marking for voice access |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_qosprofile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_qosprofile_module.md#id4)

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
    - name: Configure WiFi quality of service
      fmgr_qosprofile:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        qosprofile:
          bandwidth-admission-control: <value in [disable, enable]>
          bandwidth-capacity: <integer>
          burst: <value in [disable, enable]>
          call-admission-control: <value in [disable, enable]>
          call-capacity: <integer>
          comment: <string>
          downlink: <integer>
          downlink-sta: <integer>
          dscp-wmm-be: <list or integer>
          dscp-wmm-bk: <list or integer>
          dscp-wmm-mapping: <value in [disable, enable]>
          dscp-wmm-vi: <list or integer>
          dscp-wmm-vo: <list or integer>
          name: <string>
          uplink: <integer>
          uplink-sta: <integer>
          wmm: <value in [disable, enable]>
          wmm-uapsd: <value in [disable, enable]>
          wmm-be-dscp: <integer>
          wmm-bk-dscp: <integer>
          wmm-dscp-marking: <value in [disable, enable]>
          wmm-vi-dscp: <integer>
          wmm-vo-dscp: <integer>
```

## [Return Values](fmgr_qosprofile_module.md#id5)

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
