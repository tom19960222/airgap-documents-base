---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_vpnmgr_node module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_vpnmgr_node_module.html
fetched_at: 2026-07-27T17:38:31+00:00
---
# fortinet.fortimanager.fmgr_vpnmgr_node module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_vpnmgr_node`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_vpnmgr_node_module.md#synopsis)
- [Parameters](fmgr_vpnmgr_node_module.md#parameters)
- [Notes](fmgr_vpnmgr_node_module.md#notes)
- [Examples](fmgr_vpnmgr_node_module.md#examples)
- [Return Values](fmgr_vpnmgr_node_module.md#return-values)

## [Synopsis](fmgr_vpnmgr_node_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_vpnmgr_node_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **vpnmgr_node**  dictionary | the top level parameters set |
| **add-route**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **assign-ip**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **assign-ip-from**  string | no description  Choices:   - `"range"` - `"usrgrp"` - `"dhcp"` - `"name"` |
| **authpasswd**  string | no description |
| **authusr**  string | no description |
| **authusrgrp**  string | no description |
| **auto-configuration**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **automatic_routing**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **banner**  string | no description |
| **default-gateway**  string | no description |
| **dhcp-ra-giaddr**  string | no description |
| **dhcp-server**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dns-mode**  string | no description  Choices:   - `"auto"` - `"manual"` |
| **dns-service**  string | no description  Choices:   - `"default"` - `"specify"` - `"local"` |
| **domain**  string | no description |
| **encapsulation**  string | no description  Choices:   - `"tunnel-mode"` - `"transport-mode"` |
| **exchange-interface-ip**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **extgw**  string | no description |
| **extgw_hubip**  string | no description |
| **extgw_p2_per_net**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **extgwip**  string | no description |
| **hub-public-ip**  string | no description |
| **hub_iface**  string | no description |
| **id**  integer | no description |
| **iface**  string | no description |
| **ip-range**  list / elements=string | no description |
| **end-ip**  string | no description |
| **id**  integer | no description |
| **start-ip**  string | no description |
| **ipsec-lease-hold**  integer | no description |
| **ipv4-dns-server1**  string | no description |
| **ipv4-dns-server2**  string | no description |
| **ipv4-dns-server3**  string | no description |
| **ipv4-end-ip**  string | no description |
| **ipv4-exclude-range**  list / elements=string | no description |
| **end-ip**  string | no description |
| **id**  integer | no description |
| **start-ip**  string | no description |
| **ipv4-name**  string | no description |
| **ipv4-netmask**  string | no description |
| **ipv4-split-exclude**  string | no description |
| **ipv4-split-include**  string | no description |
| **ipv4-start-ip**  string | no description |
| **ipv4-wins-server1**  string | no description |
| **ipv4-wins-server2**  string | no description |
| **l2tp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **local-gw**  string | no description |
| **localid**  string | no description |
| **mode-cfg**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mode-cfg-ip-version**  string | no description  Choices:   - `"4"` - `"6"` |
| **net-device**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **peer**  string | no description |
| **peergrp**  string | no description |
| **peerid**  string | no description |
| **peertype**  string | no description  Choices:   - `"any"` - `"one"` - `"dialup"` - `"peer"` - `"peergrp"` |
| **protected_subnet**  list / elements=string | no description |
| **addr**  string | no description |
| **seq**  integer | no description |
| **public-ip**  string | no description |
| **role**  string | no description  Choices:   - `"hub"` - `"spoke"` |
| **route-overlap**  string | no description  Choices:   - `"use-old"` - `"use-new"` - `"allow"` |
| **scope member**  list / elements=string | description |
| **name**  string | no description |
| **vdom**  string | no description |
| **spoke-zone**  string | no description |
| **summary_addr**  list / elements=string | no description |
| **addr**  string | no description |
| **priority**  integer | no description |
| **seq**  integer | no description |
| **tunnel-search**  string | no description  Choices:   - `"selectors"` - `"nexthop"` |
| **unity-support**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **usrgrp**  string | no description |
| **vpn-interface-priority**  integer | no description |
| **vpn-zone**  string | no description |
| **vpntable**  string | no description |
| **xauthtype**  string | no description  Choices:   - `"disable"` - `"client"` - `"pap"` - `"chap"` - `"auto"` |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_vpnmgr_node_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_vpnmgr_node_module.md#id4)

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
     fmgr_vpnmgr_node:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        vpnmgr_node:
           add-route: <value in [disable, enable]>
           assign-ip: <value in [disable, enable]>
           assign-ip-from: <value in [range, usrgrp, dhcp, ...]>
           authpasswd: <value of string>
           authusr: <value of string>
           authusrgrp: <value of string>
           auto-configuration: <value in [disable, enable]>
           automatic_routing: <value in [disable, enable]>
           banner: <value of string>
           default-gateway: <value of string>
           dhcp-server: <value in [disable, enable]>
           dns-mode: <value in [auto, manual]>
           dns-service: <value in [default, specify, local]>
           domain: <value of string>
           extgw: <value of string>
           extgw_hubip: <value of string>
           extgw_p2_per_net: <value in [disable, enable]>
           extgwip: <value of string>
           hub_iface: <value of string>
           id: <value of integer>
           iface: <value of string>
           ip-range:
             -
                 end-ip: <value of string>
                 id: <value of integer>
                 start-ip: <value of string>
           ipsec-lease-hold: <value of integer>
           ipv4-dns-server1: <value of string>
           ipv4-dns-server2: <value of string>
           ipv4-dns-server3: <value of string>
           ipv4-end-ip: <value of string>
           ipv4-exclude-range:
             -
                 end-ip: <value of string>
                 id: <value of integer>
                 start-ip: <value of string>
           ipv4-netmask: <value of string>
           ipv4-split-include: <value of string>
           ipv4-start-ip: <value of string>
           ipv4-wins-server1: <value of string>
           ipv4-wins-server2: <value of string>
           local-gw: <value of string>
           localid: <value of string>
           mode-cfg: <value in [disable, enable]>
           mode-cfg-ip-version: <value in [4, 6]>
           net-device: <value in [disable, enable]>
           peer: <value of string>
           peergrp: <value of string>
           peerid: <value of string>
           peertype: <value in [any, one, dialup, ...]>
           protected_subnet:
             -
                 addr: <value of string>
                 seq: <value of integer>
           public-ip: <value of string>
           role: <value in [hub, spoke]>
           route-overlap: <value in [use-old, use-new, allow]>
           spoke-zone: <value of string>
           summary_addr:
             -
                 addr: <value of string>
                 priority: <value of integer>
                 seq: <value of integer>
           tunnel-search: <value in [selectors, nexthop]>
           unity-support: <value in [disable, enable]>
           usrgrp: <value of string>
           vpn-interface-priority: <value of integer>
           vpn-zone: <value of string>
           vpntable: <value of string>
           xauthtype: <value in [disable, client, pap, ...]>
           exchange-interface-ip: <value in [disable, enable]>
           hub-public-ip: <value of string>
           ipv4-split-exclude: <value of string>
           scope member:
             -
                 name: <value of string>
                 vdom: <value of string>
           dhcp-ra-giaddr: <value of string>
           encapsulation: <value in [tunnel-mode, transport-mode]>
           ipv4-name: <value of string>
           l2tp: <value in [disable, enable]>
```

## [Return Values](fmgr_vpnmgr_node_module.md#id5)

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
