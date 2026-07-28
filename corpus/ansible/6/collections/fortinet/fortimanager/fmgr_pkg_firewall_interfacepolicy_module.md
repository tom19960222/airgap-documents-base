---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_pkg_firewall_interfacepolicy module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_pkg_firewall_interfacepolicy_module.html
fetched_at: 2026-07-27T17:33:49+00:00
---
# fortinet.fortimanager.fmgr_pkg_firewall_interfacepolicy module – no description

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/fortinet/fortimanager) (version 2.1.7).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_pkg_firewall_interfacepolicy`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_pkg_firewall_interfacepolicy_module.md#synopsis)
- [Parameters](fmgr_pkg_firewall_interfacepolicy_module.md#parameters)
- [Notes](fmgr_pkg_firewall_interfacepolicy_module.md#notes)
- [Examples](fmgr_pkg_firewall_interfacepolicy_module.md#examples)
- [Return Values](fmgr_pkg_firewall_interfacepolicy_module.md#return-values)

## [Synopsis](fmgr_pkg_firewall_interfacepolicy_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_pkg_firewall_interfacepolicy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **pkg**  string / required | the parameter (pkg) in requested url |
| **pkg_firewall_interfacepolicy**  dictionary | the top level parameters set |
| **address-type**  string | no description  Choices:   - `"ipv4"` - `"ipv6"` |
| **application-list**  string | no description |
| **application-list-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **av-profile**  string | no description |
| **av-profile-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **comments**  string | no description |
| **dlp-profile**  string | no description |
| **dlp-profile-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dlp-sensor**  string | no description |
| **dlp-sensor-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dsri**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dstaddr**  string | no description |
| **emailfilter-profile**  string | no description |
| **emailfilter-profile-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **interface**  string | no description |
| **ips-sensor**  string | no description |
| **ips-sensor-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **label**  string | no description |
| **logtraffic**  string | no description  Choices:   - `"disable"` - `"all"` - `"utm"` |
| **policyid**  integer | no description |
| **scan-botnet-connections**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
| **service**  string | no description |
| **spamfilter-profile**  string | no description |
| **spamfilter-profile-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **srcaddr**  string | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **webfilter-profile**  string | no description |
| **webfilter-profile-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_pkg_firewall_interfacepolicy_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_pkg_firewall_interfacepolicy_module.md#id4)

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
   - name: retrieve all the IPv4 interface policies
     fmgr_fact:
       facts:
           selector: 'pkg_firewall_interfacepolicy'
           params:
               adom: 'ansible'
               pkg: 'ansible' # package name
               interface-policy: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure IPv4 interface policies.
     fmgr_pkg_firewall_interfacepolicy:
        bypass_validation: False
        adom: ansible
        pkg: ansible # package name
        state: present
        pkg_firewall_interfacepolicy:
           address-type: ipv4 #<value in [ipv4, ipv6]>
           comments: 'ansible-comment'
           interface: sslvpn_tun_intf
           policyid: 1
           status: enable
```

## [Return Values](fmgr_pkg_firewall_interfacepolicy_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **request_url**  string | The full url requested  Returned: always  Sample: `"/sys/login/user"` |
| **response_code**  integer | The status of api request  Returned: always  Sample: `0` |
| **response_message**  string | The descriptive message of the api response  Returned: always  Sample: `"OK."` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
[Homepage](https://fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/tree/galaxy/2.1.7)
