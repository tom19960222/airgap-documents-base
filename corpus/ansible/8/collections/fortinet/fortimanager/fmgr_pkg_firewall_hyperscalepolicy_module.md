---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pkg_firewall_hyperscalepolicy module – Configure IPv4/IPv6 policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pkg_firewall_hyperscalepolicy_module.html
fetched_at: 2026-07-28T02:15:25+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_hyperscalepolicy module – Configure IPv4/IPv6 policies.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_hyperscalepolicy`.

New in fortinet.fortimanager 2.2.0

- [Synopsis](fmgr_pkg_firewall_hyperscalepolicy_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_hyperscalepolicy_module.md#parameters)
- [Notes](fmgr_pkg_firewall_hyperscalepolicy_module.md#notes)
- [Examples](fmgr_pkg_firewall_hyperscalepolicy_module.md#examples)
- [Return Values](fmgr_pkg_firewall_hyperscalepolicy_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_hyperscalepolicy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_hyperscalepolicy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_hyperscalepolicy**  dictionary | the top level parameters set |
| **action**  string | Policy action  **Choices:**   - `"deny"` - `"accept"` |
| **auto-asic-offload**  string | Enable/disable policy traffic ASIC offloading.  **Choices:**   - `"disable"` - `"enable"` |
| **cgn-eif**  string | Enable/Disable CGN endpoint independent filtering.  **Choices:**   - `"disable"` - `"enable"` |
| **cgn-eim**  string | Enable/Disable CGN endpoint independent mapping  **Choices:**   - `"disable"` - `"enable"` |
| **cgn-log-server-grp**  string | NP log server group name |
| **cgn-resource-quota**  integer | resource quota |
| **cgn-session-quota**  integer | session quota |
| **comments**  string | Comment. |
| **delay-tcp-npu-session**  string | Enable TCP NPU session delay to guarantee packet order of 3-way handshake.  **Choices:**   - `"disable"` - `"enable"` |
| **dstaddr**  any | (list or str) no description |
| **dstaddr-negate**  string | When enabled dstaddr/dstaddr6 specifies what the destination address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **dstaddr6**  any | (list or str) no description |
| **dstintf**  any | (list or str) no description |
| **firewall-session-dirty**  string | How to handle sessions if the configuration of this firewall policy changes.  **Choices:**   - `"check-all"` - `"check-new"` |
| **global-label**  string | Label for the policy that appears when the GUI is in Global View mode. |
| **ippool**  string | Enable to use IP Pools for source NAT.  **Choices:**   - `"disable"` - `"enable"` |
| **label**  string | Label for the policy that appears when the GUI is in Section View mode. |
| **name**  string / required | Policy name. |
| **nat**  string | Enable/disable source NAT.  **Choices:**   - `"disable"` - `"enable"` |
| **policy-offload**  string | Enable/Disable hardware session setup for CGNAT.  **Choices:**   - `"disable"` - `"enable"` |
| **policyid**  integer | Policy ID |
| **poolname**  any | (list or str) no description |
| **poolname6**  any | (list or str) no description |
| **send-deny-packet**  string | Enable to send a reply when a session is denied or blocked by a firewall policy.  **Choices:**   - `"disable"` - `"enable"` |
| **service**  any | (list or str) no description |
| **service-negate**  string | When enabled service specifies what the service must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **srcaddr**  any | (list or str) no description |
| **srcaddr-negate**  string | When enabled srcaddr/srcaddr6 specifies what the source address must NOT be.  **Choices:**   - `"disable"` - `"enable"` |
| **srcaddr6**  any | (list or str) no description |
| **srcintf**  any | (list or str) no description |
| **status**  string | Enable or disable this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **tcp-timeout-pid**  string | TCP timeout profile ID |
| **traffic-shaper**  string | Traffic shaper. |
| **traffic-shaper-reverse**  string | Reverse traffic shaper. |
| **udp-timeout-pid**  string | UDP timeout profile ID |
| **uuid**  string | Universally Unique Identifier |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pkg_firewall_hyperscalepolicy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_hyperscalepolicy_module.md#id4)

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
    - name: Configure IPv4/IPv6 policies.
      fmgr_pkg_firewall_hyperscalepolicy:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        pkg: <your own value>
        state: <value in [present, absent]>
        pkg_firewall_hyperscalepolicy:
          action: <value in [deny, accept]>
          auto-asic-offload: <value in [disable, enable]>
          cgn-eif: <value in [disable, enable]>
          cgn-eim: <value in [disable, enable]>
          cgn-log-server-grp: <string>
          cgn-resource-quota: <integer>
          cgn-session-quota: <integer>
          comments: <string>
          delay-tcp-npu-session: <value in [disable, enable]>
          dstaddr: <list or string>
          dstaddr-negate: <value in [disable, enable]>
          dstaddr6: <list or string>
          dstintf: <list or string>
          firewall-session-dirty: <value in [check-all, check-new]>
          global-label: <string>
          ippool: <value in [disable, enable]>
          label: <string>
          name: <string>
          nat: <value in [disable, enable]>
          policy-offload: <value in [disable, enable]>
          policyid: <integer>
          poolname: <list or string>
          poolname6: <list or string>
          send-deny-packet: <value in [disable, enable]>
          service: <list or string>
          service-negate: <value in [disable, enable]>
          srcaddr: <list or string>
          srcaddr-negate: <value in [disable, enable]>
          srcaddr6: <list or string>
          srcintf: <list or string>
          status: <value in [disable, enable]>
          tcp-timeout-pid: <string>
          traffic-shaper: <string>
          traffic-shaper-reverse: <string>
          udp-timeout-pid: <string>
          uuid: <string>
```

## [Return Values](fmgr_pkg_firewall_hyperscalepolicy_module.md#id5)

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
