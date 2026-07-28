---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping_interface_ipv6 module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.html
fetched_at: 2026-07-27T17:32:49+00:00
---
# fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping_interface_ipv6 module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping_interface_ipv6`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.md#synopsis)
- [Parameters](fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.md#parameters)
- [Notes](fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.md#notes)
- [Examples](fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.md#examples)
- [Return Values](fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.md#return-values)

## [Synopsis](fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **dynamic_mapping**  string / required | the parameter (dynamic_mapping) in requested url |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **fsp_vlan_dynamicmapping_interface_ipv6**  dictionary | the top level parameters set |
| **autoconf**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **cli-conn6-status**  integer | no description |
| **dhcp6-client-options**  list / elements=string | description  Choices:   - `"rapid"` - `"iapd"` - `"iana"` - `"dns"` - `"dnsname"` |
| **dhcp6-information-request**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dhcp6-prefix-delegation**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dhcp6-prefix-hint**  string | no description |
| **dhcp6-prefix-hint-plt**  integer | no description |
| **dhcp6-prefix-hint-vlt**  integer | no description |
| **dhcp6-relay-ip**  string | no description |
| **dhcp6-relay-service**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dhcp6-relay-type**  string | no description  Choices:   - `"regular"` |
| **icmp6-send-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **interface-identifier**  string | no description |
| **ip6-address**  string | no description |
| **ip6-allowaccess**  list / elements=string | description  Choices:   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"capwap"` - `"fabric"` |
| **ip6-default-life**  integer | no description |
| **ip6-delegated-prefix-iaid**  integer | no description |
| **ip6-delegated-prefix-list**  list / elements=string | description |
| **autonomous-flag**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **delegated-prefix-iaid**  integer | no description |
| **onlink-flag**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **prefix-id**  integer | no description |
| **rdnss**  string | description |
| **rdnss-service**  string | no description  Choices:   - `"delegated"` - `"default"` - `"specify"` |
| **subnet**  string | no description |
| **upstream-interface**  string | no description |
| **ip6-dns-server-override**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ip6-extra-addr**  list / elements=string | description |
| **prefix**  string | no description |
| **ip6-hop-limit**  integer | no description |
| **ip6-link-mtu**  integer | no description |
| **ip6-manage-flag**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ip6-max-interval**  integer | no description |
| **ip6-min-interval**  integer | no description |
| **ip6-mode**  string | no description  Choices:   - `"static"` - `"dhcp"` - `"pppoe"` - `"delegated"` |
| **ip6-other-flag**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ip6-prefix-list**  list / elements=string | description |
| **autonomous-flag**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dnssl**  string | description |
| **onlink-flag**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **preferred-life-time**  integer | no description |
| **prefix**  string | no description |
| **rdnss**  string | description |
| **valid-life-time**  integer | no description |
| **ip6-prefix-mode**  string | no description  Choices:   - `"dhcp6"` - `"ra"` |
| **ip6-reachable-time**  integer | no description |
| **ip6-retrans-time**  integer | no description |
| **ip6-send-adv**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ip6-subnet**  string | no description |
| **ip6-upstream-interface**  string | no description |
| **nd-cert**  string | no description |
| **nd-cga-modifier**  string | no description |
| **nd-mode**  string | no description  Choices:   - `"basic"` - `"SEND-compatible"` |
| **nd-security-level**  integer | no description |
| **nd-timestamp-delta**  integer | no description |
| **nd-timestamp-fuzz**  integer | no description |
| **ra-send-mtu**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **unique-autoconf-addr**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **vrip6_link_local**  string | no description |
| **vrrp-virtual-mac6**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **vrrp6**  list / elements=string | description |
| **accept-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **adv-interval**  integer | no description |
| **preempt**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **priority**  integer | no description |
| **start-time**  integer | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **vrdst6**  string | no description |
| **vrgrp**  integer | no description |
| **vrid**  integer | no description |
| **vrip6**  string | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **vlan**  string / required | the parameter (vlan) in requested url |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.md#id4)

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
   - name: no description
     fmgr_fsp_vlan_dynamicmapping_interface_ipv6:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        vlan: <your own value>
        dynamic_mapping: <your own value>
        fsp_vlan_dynamicmapping_interface_ipv6:
           autoconf: <value in [disable, enable]>
           dhcp6-client-options:
             - rapid
             - iapd
             - iana
             - dns
             - dnsname
           dhcp6-information-request: <value in [disable, enable]>
           dhcp6-prefix-delegation: <value in [disable, enable]>
           dhcp6-prefix-hint: <value of string>
           dhcp6-prefix-hint-plt: <value of integer>
           dhcp6-prefix-hint-vlt: <value of integer>
           dhcp6-relay-ip: <value of string>
           dhcp6-relay-service: <value in [disable, enable]>
           dhcp6-relay-type: <value in [regular]>
           ip6-address: <value of string>
           ip6-allowaccess:
             - https
             - ping
             - ssh
             - snmp
             - http
             - telnet
             - fgfm
             - capwap
             - fabric
           ip6-default-life: <value of integer>
           ip6-delegated-prefix-list:
             -
                 autonomous-flag: <value in [disable, enable]>
                 onlink-flag: <value in [disable, enable]>
                 prefix-id: <value of integer>
                 rdnss: <value of string>
                 rdnss-service: <value in [delegated, default, specify]>
                 subnet: <value of string>
                 upstream-interface: <value of string>
                 delegated-prefix-iaid: <value of integer>
           ip6-dns-server-override: <value in [disable, enable]>
           ip6-extra-addr:
             -
                 prefix: <value of string>
           ip6-hop-limit: <value of integer>
           ip6-link-mtu: <value of integer>
           ip6-manage-flag: <value in [disable, enable]>
           ip6-max-interval: <value of integer>
           ip6-min-interval: <value of integer>
           ip6-mode: <value in [static, dhcp, pppoe, ...]>
           ip6-other-flag: <value in [disable, enable]>
           ip6-prefix-list:
             -
                 autonomous-flag: <value in [disable, enable]>
                 dnssl: <value of string>
                 onlink-flag: <value in [disable, enable]>
                 preferred-life-time: <value of integer>
                 prefix: <value of string>
                 rdnss: <value of string>
                 valid-life-time: <value of integer>
           ip6-reachable-time: <value of integer>
           ip6-retrans-time: <value of integer>
           ip6-send-adv: <value in [disable, enable]>
           ip6-subnet: <value of string>
           ip6-upstream-interface: <value of string>
           nd-cert: <value of string>
           nd-cga-modifier: <value of string>
           nd-mode: <value in [basic, SEND-compatible]>
           nd-security-level: <value of integer>
           nd-timestamp-delta: <value of integer>
           nd-timestamp-fuzz: <value of integer>
           vrip6_link_local: <value of string>
           vrrp-virtual-mac6: <value in [disable, enable]>
           vrrp6:
             -
                 accept-mode: <value in [disable, enable]>
                 adv-interval: <value of integer>
                 preempt: <value in [disable, enable]>
                 priority: <value of integer>
                 start-time: <value of integer>
                 status: <value in [disable, enable]>
                 vrdst6: <value of string>
                 vrgrp: <value of integer>
                 vrid: <value of integer>
                 vrip6: <value of string>
           interface-identifier: <value of string>
           unique-autoconf-addr: <value in [disable, enable]>
           icmp6-send-redirect: <value in [disable, enable]>
           cli-conn6-status: <value of integer>
           ip6-prefix-mode: <value in [dhcp6, ra]>
           ra-send-mtu: <value in [disable, enable]>
           ip6-delegated-prefix-iaid: <value of integer>
```

## [Return Values](fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.md#id5)

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
