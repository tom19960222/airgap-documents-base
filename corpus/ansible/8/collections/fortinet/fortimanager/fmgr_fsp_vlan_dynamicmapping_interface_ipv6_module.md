---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping_interface_ipv6 module – IPv6 of interface."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.html
fetched_at: 2026-07-28T02:14:02+00:00
---
# fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping_interface_ipv6 module – IPv6 of interface.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping_interface_ipv6`.

New in fortinet.fortimanager 2.1.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **dynamic_mapping**  string / required | the parameter (dynamic_mapping) in requested url |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **fsp_vlan_dynamicmapping_interface_ipv6**  dictionary | the top level parameters set |
| **autoconf**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **cli-conn6-status**  integer | no description |
| **dhcp6-client-options**  list / elements=string | no description  **Choices:**   - `"rapid"` - `"iapd"` - `"iana"` - `"dns"` - `"dnsname"` |
| **dhcp6-information-request**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp6-prefix-delegation**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp6-prefix-hint**  string | no description |
| **dhcp6-prefix-hint-plt**  integer | no description |
| **dhcp6-prefix-hint-vlt**  integer | no description |
| **dhcp6-relay-ip**  string | no description |
| **dhcp6-relay-service**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp6-relay-source-interface**  string | Enable/disable use of address on this interface as the source address of the relay message.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp6-relay-type**  string | no description  **Choices:**   - `"regular"` |
| **icmp6-send-redirect**  string | Enable/disable sending of ICMPv6 redirects.  **Choices:**   - `"disable"` - `"enable"` |
| **interface-identifier**  string | no description |
| **ip6-address**  string | no description |
| **ip6-allowaccess**  list / elements=string | no description  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"capwap"` - `"fabric"` |
| **ip6-default-life**  integer | no description |
| **ip6-delegated-prefix-iaid**  integer | IAID of obtained delegated-prefix from the upstream interface. |
| **ip6-delegated-prefix-list**  list / elements=dictionary | no description |
| **autonomous-flag**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **delegated-prefix-iaid**  integer | IAID of obtained delegated-prefix from the upstream interface. |
| **onlink-flag**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **prefix-id**  integer | no description |
| **rdnss**  any | (list) no description |
| **rdnss-service**  string | no description  **Choices:**   - `"delegated"` - `"default"` - `"specify"` |
| **subnet**  string | no description |
| **upstream-interface**  string | no description |
| **ip6-dns-server-override**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-extra-addr**  list / elements=dictionary | no description |
| **prefix**  string | no description |
| **ip6-hop-limit**  integer | no description |
| **ip6-link-mtu**  integer | no description |
| **ip6-manage-flag**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-max-interval**  integer | no description |
| **ip6-min-interval**  integer | no description |
| **ip6-mode**  string | no description  **Choices:**   - `"static"` - `"dhcp"` - `"pppoe"` - `"delegated"` |
| **ip6-other-flag**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-prefix-list**  list / elements=dictionary | no description |
| **autonomous-flag**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dnssl**  any | (list) no description |
| **onlink-flag**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **preferred-life-time**  integer | no description |
| **prefix**  string | no description |
| **rdnss**  any | (list) no description |
| **valid-life-time**  integer | no description |
| **ip6-prefix-mode**  string | Assigning a prefix from DHCP or RA.  **Choices:**   - `"dhcp6"` - `"ra"` |
| **ip6-reachable-time**  integer | no description |
| **ip6-retrans-time**  integer | no description |
| **ip6-send-adv**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-subnet**  string | no description |
| **ip6-upstream-interface**  string | no description |
| **nd-cert**  string | no description |
| **nd-cga-modifier**  string | no description |
| **nd-mode**  string | no description  **Choices:**   - `"basic"` - `"SEND-compatible"` |
| **nd-security-level**  integer | no description |
| **nd-timestamp-delta**  integer | no description |
| **nd-timestamp-fuzz**  integer | no description |
| **ra-send-mtu**  string | Enable/disable sending link MTU in RA packet.  **Choices:**   - `"disable"` - `"enable"` |
| **unique-autoconf-addr**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **vrip6_link_local**  string | no description |
| **vrrp-virtual-mac6**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **vrrp6**  list / elements=dictionary | no description |
| **accept-mode**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **adv-interval**  integer | no description |
| **preempt**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **priority**  integer | no description |
| **start-time**  integer | no description |
| **status**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **vrdst6**  string | no description |
| **vrgrp**  integer | no description |
| **vrid**  integer | no description |
| **vrip6**  string | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **vlan**  string / required | the parameter (vlan) in requested url |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
    - name: IPv6 of interface.
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
          dhcp6-prefix-hint: <string>
          dhcp6-prefix-hint-plt: <integer>
          dhcp6-prefix-hint-vlt: <integer>
          dhcp6-relay-ip: <string>
          dhcp6-relay-service: <value in [disable, enable]>
          dhcp6-relay-type: <value in [regular]>
          ip6-address: <string>
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
          ip6-default-life: <integer>
          ip6-delegated-prefix-list:
            -
              autonomous-flag: <value in [disable, enable]>
              onlink-flag: <value in [disable, enable]>
              prefix-id: <integer>
              rdnss: <list or string>
              rdnss-service: <value in [delegated, default, specify]>
              subnet: <string>
              upstream-interface: <string>
              delegated-prefix-iaid: <integer>
          ip6-dns-server-override: <value in [disable, enable]>
          ip6-extra-addr:
            -
              prefix: <string>
          ip6-hop-limit: <integer>
          ip6-link-mtu: <integer>
          ip6-manage-flag: <value in [disable, enable]>
          ip6-max-interval: <integer>
          ip6-min-interval: <integer>
          ip6-mode: <value in [static, dhcp, pppoe, ...]>
          ip6-other-flag: <value in [disable, enable]>
          ip6-prefix-list:
            -
              autonomous-flag: <value in [disable, enable]>
              dnssl: <list or string>
              onlink-flag: <value in [disable, enable]>
              preferred-life-time: <integer>
              prefix: <string>
              rdnss: <list or string>
              valid-life-time: <integer>
          ip6-reachable-time: <integer>
          ip6-retrans-time: <integer>
          ip6-send-adv: <value in [disable, enable]>
          ip6-subnet: <string>
          ip6-upstream-interface: <string>
          nd-cert: <string>
          nd-cga-modifier: <string>
          nd-mode: <value in [basic, SEND-compatible]>
          nd-security-level: <integer>
          nd-timestamp-delta: <integer>
          nd-timestamp-fuzz: <integer>
          vrip6_link_local: <string>
          vrrp-virtual-mac6: <value in [disable, enable]>
          vrrp6:
            -
              accept-mode: <value in [disable, enable]>
              adv-interval: <integer>
              preempt: <value in [disable, enable]>
              priority: <integer>
              start-time: <integer>
              status: <value in [disable, enable]>
              vrdst6: <string>
              vrgrp: <integer>
              vrid: <integer>
              vrip6: <string>
          interface-identifier: <string>
          unique-autoconf-addr: <value in [disable, enable]>
          icmp6-send-redirect: <value in [disable, enable]>
          cli-conn6-status: <integer>
          ip6-prefix-mode: <value in [dhcp6, ra]>
          ra-send-mtu: <value in [disable, enable]>
          ip6-delegated-prefix-iaid: <integer>
          dhcp6-relay-source-interface: <value in [disable, enable]>
```

## [Return Values](fmgr_fsp_vlan_dynamicmapping_interface_ipv6_module.md#id5)

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
