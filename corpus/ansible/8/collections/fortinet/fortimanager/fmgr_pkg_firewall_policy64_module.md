---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pkg_firewall_policy64 module – Configure IPv6 to IPv4 policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pkg_firewall_policy64_module.html
fetched_at: 2026-07-28T02:15:38+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_policy64 module – Configure IPv6 to IPv4 policies.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_policy64`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_pkg_firewall_policy64_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_policy64_module.md#parameters)
- [Notes](fmgr_pkg_firewall_policy64_module.md#notes)
- [Examples](fmgr_pkg_firewall_policy64_module.md#examples)
- [Return Values](fmgr_pkg_firewall_policy64_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_policy64_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_policy64_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_policy64**  dictionary | the top level parameters set |
| **action**  string | Policy action.  **Choices:**   - `"deny"` - `"accept"` |
| **cgn-eif**  string | Enable/disable CGN endpoint independent filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **cgn-eim**  string | Enable/disable CGN endpoint independent mapping.  **Choices:**   - `"disable"` - `"enable"` |
| **cgn-log-server-grp**  string | NP log server group name |
| **cgn-resource-quota**  integer | resource quota |
| **cgn-session-quota**  integer | session quota |
| **comments**  string | Comment. |
| **dstaddr**  any | (list or str) Destination address name. |
| **dstintf**  string | Destination interface name. |
| **fixedport**  string | Enable/disable policy fixed port.  **Choices:**   - `"disable"` - `"enable"` |
| **ippool**  string | Enable/disable policy64 IP pool.  **Choices:**   - `"disable"` - `"enable"` |
| **logtraffic**  string | Enable/disable policy log traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **logtraffic-start**  string | Record logs when a session starts and ends.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string | Policy name. |
| **per-ip-shaper**  string | Per-IP traffic shaper. |
| **permit-any-host**  string | Enable/disable permit any host in.  **Choices:**   - `"disable"` - `"enable"` |
| **policy-offload**  string | Enable/disable hardware session setup for CGNAT.  **Choices:**   - `"disable"` - `"enable"` |
| **policyid**  integer / required | Policy ID. |
| **poolname**  any | (list or str) Policy IP pool names. |
| **schedule**  string | Schedule name. |
| **service**  any | (list or str) Service name. |
| **srcaddr**  any | (list or str) Source address name. |
| **srcintf**  string | Source interface name. |
| **status**  string | Enable/disable policy status.  **Choices:**   - `"disable"` - `"enable"` |
| **tags**  string | Applied object tags. |
| **tcp-mss-receiver**  integer | TCP MSS value of receiver. |
| **tcp-mss-sender**  integer | TCP MSS value of sender. |
| **traffic-shaper**  string | Traffic shaper. |
| **traffic-shaper-reverse**  string | Reverse traffic shaper. |
| **uuid**  string | Universally Unique Identifier |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pkg_firewall_policy64_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_policy64_module.md#id4)

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
   - name: retrieve all the IPv6 to IPv4 policies
     fmgr_fact:
       facts:
           selector: 'pkg_firewall_policy64'
           params:
               adom: 'ansible'
               pkg: 'ansible' # package name
               policy64: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure IPv6 to IPv4 policies.
     fmgr_pkg_firewall_policy64:
        bypass_validation: False
        adom: ansible
        pkg: ansible # package name
        state: present
        pkg_firewall_policy64:
           action: accept #<value in [deny, accept]>
           comments: ansible-comment
           dstaddr: all
           dstintf: any
           policyid: 1
           schedule: always
           service: ALL
           srcaddr: all
           srcintf: any
           status: disable
```

## [Return Values](fmgr_pkg_firewall_policy64_module.md#id5)

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
