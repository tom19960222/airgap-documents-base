---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_pkg_firewall_dospolicy6 module – Configure IPv6 DoS policies."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_pkg_firewall_dospolicy6_module.html
fetched_at: 2026-07-28T02:15:18+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_dospolicy6 module – Configure IPv6 DoS policies.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_dospolicy6`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_pkg_firewall_dospolicy6_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_dospolicy6_module.md#parameters)
- [Notes](fmgr_pkg_firewall_dospolicy6_module.md#notes)
- [Examples](fmgr_pkg_firewall_dospolicy6_module.md#examples)
- [Return Values](fmgr_pkg_firewall_dospolicy6_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_dospolicy6_module.md#id8)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_dospolicy6_module.md#id9)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_dospolicy6**  dictionary | the top level parameters set |
| **anomaly**  list / elements=dictionary | Anomaly. |
| **action**  string | Action taken when the threshold is reached.  **Choices:**   - `"pass"` - `"block"` - `"proxy"` |
| **log**  string | Enable/disable logging for this anomaly.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string | Anomaly name. |
| **quarantine**  string | Quarantine method.  **Choices:**   - `"none"` - `"attacker"` - `"both"` - `"interface"` |
| **quarantine-expiry**  string | Duration of quarantine, from 1 minute to 364 days, 23 hours, and 59 minutes from now. |
| **quarantine-log**  string | Enable/disable quarantine logging.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable the active status of this anomaly sensor.  **Choices:**   - `"disable"` - `"enable"` |
| **synproxy-tcp-mss**  string | Determine TCP maximum segment size  **Choices:**   - `"0"` - `"256"` - `"512"` - `"1024"` - `"1300"` - `"1360"` - `"1460"` - `"1500"` |
| **synproxy-tcp-sack**  string | enable/disable TCP selective acknowledage  **Choices:**   - `"disable"` - `"enable"` |
| **synproxy-tcp-timestamp**  string | enable/disable TCP timestamp option for packets replied by syn proxy module.  **Choices:**   - `"disable"` - `"enable"` |
| **synproxy-tcp-window**  string | Determine TCP Window size for packets replied by syn proxy module.  **Choices:**   - `"4096"` - `"8192"` - `"16384"` - `"32768"` |
| **synproxy-tcp-windowscale**  string | Determine TCP window scale option value for packets replied by syn proxy module.  **Choices:**   - `"0"` - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` - `"6"` - `"7"` - `"8"` - `"9"` - `"10"` - `"11"` - `"12"` - `"13"` - `"14"` |
| **synproxy-tos**  string | Determine TCP differentiated services code point value  **Choices:**   - `"0"` - `"10"` - `"12"` - `"14"` - `"18"` - `"20"` - `"22"` - `"26"` - `"28"` - `"30"` - `"34"` - `"36"` - `"38"` - `"40"` - `"46"` - `"255"` |
| **synproxy-ttl**  string | Determine Time to live  **Choices:**   - `"32"` - `"64"` - `"128"` - `"255"` |
| **synproxy_tcp_mss**  string | Determine TCP maximum segment size  **Choices:**   - `"0"` - `"256"` - `"512"` - `"1024"` - `"1300"` - `"1360"` - `"1460"` - `"1500"` |
| **synproxy_tcp_sack**  string | enable/disable TCP selective acknowledage  **Choices:**   - `"disable"` - `"enable"` |
| **synproxy_tcp_timestamp**  string | enable/disable TCP timestamp option for packets replied by syn proxy module.  **Choices:**   - `"disable"` - `"enable"` |
| **synproxy_tcp_window**  string | Determine TCP Window size for packets replied by syn proxy module.  **Choices:**   - `"4096"` - `"8192"` - `"16384"` - `"32768"` |
| **synproxy_tcp_windowscale**  string | Determine TCP window scale option value for packets replied by syn proxy module.  **Choices:**   - `"0"` - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` - `"6"` - `"7"` - `"8"` - `"9"` - `"10"` - `"11"` - `"12"` - `"13"` - `"14"` |
| **synproxy_tos**  string | Determine TCP differentiated services code point value  **Choices:**   - `"0"` - `"10"` - `"12"` - `"14"` - `"18"` - `"20"` - `"22"` - `"26"` - `"28"` - `"30"` - `"34"` - `"36"` - `"38"` - `"40"` - `"46"` - `"255"` |
| **synproxy_ttl**  string | Determine Time to live  **Choices:**   - `"32"` - `"64"` - `"128"` - `"255"` |
| **threshold**  integer | Number of detected instances per minute which triggers action |
| **threshold(default)**  integer | Threshold |
| **comments**  string | Comment. |
| **dstaddr**  any | (list or str) Destination address name from available addresses. |
| **interface**  string | Incoming interface name from available interfaces. |
| **name**  string | Policy name. |
| **policyid**  integer / required | Policy ID. |
| **service**  any | (list or str) Service object from available options. |
| **srcaddr**  any | (list or str) Source address name from available addresses. |
| **status**  string | Enable/disable this policy.  **Choices:**   - `"disable"` - `"enable"` |
| **uuid**  string | Universally Unique Identifier |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_pkg_firewall_dospolicy6_module.md#id10)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_dospolicy6_module.md#id11)

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
   - name: Configure IPv6 DoS policies.
     fmgr_pkg_firewall_dospolicy6:
        bypass_validation: False
        adom: ansible
        pkg: ansible # package name
        state: present
        pkg_firewall_dospolicy6:
           comments: 'ansible-comment'
           interface: 'sslvpn_tun_intf'
           policyid: 1
           status: enable

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
   - name: retrieve all the IPv6 DoS policies
     fmgr_fact:
       facts:
           selector: 'pkg_firewall_dospolicy6'
           params:
               adom: 'ansible'
               pkg: 'ansible' # package name
               DoS-policy6: 'your_value'
```

## [Return Values](fmgr_pkg_firewall_dospolicy6_module.md#id12)

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
