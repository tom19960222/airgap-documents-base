---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_internetservice module – Show Internet Service application."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_internetservice_module.html
fetched_at: 2026-07-28T02:12:06+00:00
---
# fortinet.fortimanager.fmgr_firewall_internetservice module – Show Internet Service application.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_internetservice`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_firewall_internetservice_module.md#synopsis)
- [Parameters](fmgr_firewall_internetservice_module.md#parameters)
- [Notes](fmgr_firewall_internetservice_module.md#notes)
- [Examples](fmgr_firewall_internetservice_module.md#examples)
- [Return Values](fmgr_firewall_internetservice_module.md#return-values)

## [Synopsis](fmgr_firewall_internetservice_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_internetservice_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_internetservice**  dictionary | the top level parameters set |
| **city**  any | (list) City sequence number list. |
| **city6**  any | (list) no description |
| **country**  any | (list) Country sequence number list. |
| **country6**  any | (list) no description |
| **database**  string | Database.  **Choices:**   - `"isdb"` - `"irdb"` |
| **direction**  string | Direction.  **Choices:**   - `"src"` - `"dst"` - `"both"` |
| **entry**  list / elements=dictionary | no description |
| **id**  integer | Entry ID. |
| **ip-number**  integer | Total number of IP addresses. |
| **ip-range-number**  integer | Total number of IP ranges. |
| **port**  any | (list) no description |
| **protocol**  integer | Integer value for the protocol type as defined by IANA |
| **extra-ip-range-number**  integer | Extra-Ip-Range-Number. |
| **extra-ip6-range-number**  integer | no description |
| **icon-id**  integer | Icon-Id. |
| **id**  integer | Id. |
| **ip-number**  integer | Ip-Number. |
| **ip-range-number**  integer | Ip-Range-Number. |
| **ip6-range-number**  integer | no description |
| **jitter-threshold**  integer | Jitter-Threshold. |
| **latency-threshold**  integer | Latency-Threshold. |
| **name**  string | Name. |
| **obsolete**  integer | Obsolete. |
| **offset**  integer | no description |
| **packetloss-threshold**  integer | Packetloss-Threshold. |
| **region**  any | (list) Region sequence number list. |
| **region6**  any | (list) no description |
| **reputation**  integer | Reputation. |
| **singularity**  integer | Singularity. |
| **sld-id**  integer | Sld-Id. |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_internetservice_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_internetservice_module.md#id4)

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
    - name: Show Internet Service application.
      fmgr_firewall_internetservice:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        firewall_internetservice:
          database: <value in [isdb, irdb]>
          direction: <value in [src, dst, both]>
          entry:
            -
              id: <integer>
              ip-number: <integer>
              ip-range-number: <integer>
              port: <list or integer>
              protocol: <integer>
          icon-id: <integer>
          id: <integer>
          name: <string>
          offset: <integer>
          reputation: <integer>
          sld-id: <integer>
          extra-ip-range-number: <integer>
          ip-number: <integer>
          ip-range-number: <integer>
          jitter-threshold: <integer>
          latency-threshold: <integer>
          obsolete: <integer>
          packetloss-threshold: <integer>
          singularity: <integer>
          city: <list or integer>
          country: <list or integer>
          region: <list or integer>
          city6: <list or integer>
          country6: <list or integer>
          extra-ip6-range-number: <integer>
          ip6-range-number: <integer>
          region6: <list or integer>
```

## [Return Values](fmgr_firewall_internetservice_module.md#id5)

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
