---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_vpnmgr_node module – VPN node for VPN Manager."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_vpnmgr_node_module.html
fetched_at: 2026-07-28T02:21:42+00:00
---
# fortinet.fortimanager.fmgr_vpnmgr_node module – VPN node for VPN Manager.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_vpnmgr_node`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **vpnmgr_node**  dictionary | the top level parameters set |
| **add-route**  string | Add-Route.  **Choices:**   - `"disable"` - `"enable"` |
| **assign-ip**  string | Assign-Ip.  **Choices:**   - `"disable"` - `"enable"` |
| **assign-ip-from**  string | Assign-Ip-From.  **Choices:**   - `"range"` - `"usrgrp"` - `"dhcp"` - `"name"` |
| **authpasswd**  any | (list) Authpasswd. |
| **authusr**  string | Authusr. |
| **authusrgrp**  string | Authusrgrp. |
| **auto-configuration**  string | Auto-Configuration.  **Choices:**   - `"disable"` - `"enable"` |
| **auto-discovery-receiver**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **auto-discovery-sender**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **automatic_routing**  string | Automatic_Routing.  **Choices:**   - `"disable"` - `"enable"` |
| **banner**  string | Banner. |
| **default-gateway**  string | Default-Gateway. |
| **dhcp-ra-giaddr**  string | no description |
| **dhcp-server**  string | Dhcp-Server.  **Choices:**   - `"disable"` - `"enable"` |
| **dns-mode**  string | Dns-Mode.  **Choices:**   - `"auto"` - `"manual"` |
| **dns-service**  string | Dns-Service.  **Choices:**   - `"default"` - `"specify"` - `"local"` |
| **domain**  string | Domain. |
| **encapsulation**  string | no description  **Choices:**   - `"tunnel-mode"` - `"transport-mode"` |
| **exchange-interface-ip**  string | Exchange-Interface-Ip.  **Choices:**   - `"disable"` - `"enable"` |
| **extgw**  string | Extgw. |
| **extgw_hubip**  string | Extgw_Hubip. |
| **extgw_p2_per_net**  string | Extgw_P2_Per_Net.  **Choices:**   - `"disable"` - `"enable"` |
| **extgwip**  string | Extgwip. |
| **hub-public-ip**  string | Hub-Public-Ip. |
| **hub_iface**  any | (list or str) Hub_Iface. |
| **id**  integer / required | Id. |
| **iface**  any | (list or str) Iface. |
| **ip-range**  list / elements=dictionary | Ip-Range. |
| **end-ip**  string | End-Ip. |
| **id**  integer | Id. |
| **start-ip**  string | Start-Ip. |
| **ipsec-lease-hold**  integer | Ipsec-Lease-Hold. |
| **ipv4-dns-server1**  string | Ipv4-Dns-Server1. |
| **ipv4-dns-server2**  string | Ipv4-Dns-Server2. |
| **ipv4-dns-server3**  string | Ipv4-Dns-Server3. |
| **ipv4-end-ip**  string | Ipv4-End-Ip. |
| **ipv4-exclude-range**  list / elements=dictionary | Ipv4-Exclude-Range. |
| **end-ip**  string | End-Ip. |
| **id**  integer | Id. |
| **start-ip**  string | Start-Ip. |
| **ipv4-name**  string | no description |
| **ipv4-netmask**  string | Ipv4-Netmask. |
| **ipv4-split-exclude**  string | Ipv4-Split-Exclude. |
| **ipv4-split-include**  string | Ipv4-Split-Include. |
| **ipv4-start-ip**  string | Ipv4-Start-Ip. |
| **ipv4-wins-server1**  string | Ipv4-Wins-Server1. |
| **ipv4-wins-server2**  string | Ipv4-Wins-Server2. |
| **l2tp**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **local-gw**  string | Local-Gw. |
| **localid**  string | Localid. |
| **mode-cfg**  string | Mode-Cfg.  **Choices:**   - `"disable"` - `"enable"` |
| **mode-cfg-ip-version**  string | Mode-Cfg-Ip-Version.  **Choices:**   - `"4"` - `"6"` |
| **net-device**  string | Net-Device.  **Choices:**   - `"disable"` - `"enable"` |
| **network-id**  integer | no description |
| **network-overlay**  string | no description  **Choices:**   - `"enable"` - `"disable"` |
| **peer**  any | (list or str) Peer. |
| **peergrp**  string | Peergrp. |
| **peerid**  string | Peerid. |
| **peertype**  string | Peertype.  **Choices:**   - `"any"` - `"one"` - `"dialup"` - `"peer"` - `"peergrp"` |
| **protected_subnet**  list / elements=dictionary | Protected_Subnet. |
| **addr**  any | (list or str) Addr. |
| **seq**  integer | Seq. |
| **protocol**  integer | no description |
| **public-ip**  string | Public-Ip. |
| **role**  string | Role.  **Choices:**   - `"hub"` - `"spoke"` |
| **route-overlap**  string | Route-Overlap.  **Choices:**   - `"use-old"` - `"use-new"` - `"allow"` |
| **scope member**  list / elements=dictionary | no description |
| **name**  string | no description |
| **vdom**  string | no description |
| **spoke-zone**  any | (list or str) Spoke-Zone. |
| **summary_addr**  list / elements=dictionary | Summary_Addr. |
| **addr**  string | Addr. |
| **priority**  integer | Priority. |
| **seq**  integer | Seq. |
| **tunnel-search**  string | Tunnel-Search.  **Choices:**   - `"selectors"` - `"nexthop"` |
| **unity-support**  string | Unity-Support.  **Choices:**   - `"disable"` - `"enable"` |
| **usrgrp**  string | Usrgrp. |
| **vpn-interface-priority**  integer | Vpn-Interface-Priority. |
| **vpn-zone**  any | (list or str) Vpn-Zone. |
| **vpntable**  any | (list or str) Vpntable. |
| **xauthtype**  string | Xauthtype.  **Choices:**   - `"disable"` - `"client"` - `"pap"` - `"chap"` - `"auto"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
    - name: VPN node for VPN Manager.
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
          authpasswd: <list or string>
          authusr: <string>
          authusrgrp: <string>
          auto-configuration: <value in [disable, enable]>
          automatic_routing: <value in [disable, enable]>
          banner: <string>
          default-gateway: <string>
          dhcp-server: <value in [disable, enable]>
          dns-mode: <value in [auto, manual]>
          dns-service: <value in [default, specify, local]>
          domain: <string>
          extgw: <string>
          extgw_hubip: <string>
          extgw_p2_per_net: <value in [disable, enable]>
          extgwip: <string>
          hub_iface: <list or string>
          id: <integer>
          iface: <list or string>
          ip-range:
            -
              end-ip: <string>
              id: <integer>
              start-ip: <string>
          ipsec-lease-hold: <integer>
          ipv4-dns-server1: <string>
          ipv4-dns-server2: <string>
          ipv4-dns-server3: <string>
          ipv4-end-ip: <string>
          ipv4-exclude-range:
            -
              end-ip: <string>
              id: <integer>
              start-ip: <string>
          ipv4-netmask: <string>
          ipv4-split-include: <string>
          ipv4-start-ip: <string>
          ipv4-wins-server1: <string>
          ipv4-wins-server2: <string>
          local-gw: <string>
          localid: <string>
          mode-cfg: <value in [disable, enable]>
          mode-cfg-ip-version: <value in [4, 6]>
          net-device: <value in [disable, enable]>
          peer: <list or string>
          peergrp: <string>
          peerid: <string>
          peertype: <value in [any, one, dialup, ...]>
          protected_subnet:
            -
              addr: <list or string>
              seq: <integer>
          public-ip: <string>
          role: <value in [hub, spoke]>
          route-overlap: <value in [use-old, use-new, allow]>
          spoke-zone: <list or string>
          summary_addr:
            -
              addr: <string>
              priority: <integer>
              seq: <integer>
          tunnel-search: <value in [selectors, nexthop]>
          unity-support: <value in [disable, enable]>
          usrgrp: <string>
          vpn-interface-priority: <integer>
          vpn-zone: <list or string>
          vpntable: <list or string>
          xauthtype: <value in [disable, client, pap, ...]>
          exchange-interface-ip: <value in [disable, enable]>
          hub-public-ip: <string>
          ipv4-split-exclude: <string>
          scope member:
            -
              name: <string>
              vdom: <string>
          dhcp-ra-giaddr: <string>
          encapsulation: <value in [tunnel-mode, transport-mode]>
          ipv4-name: <string>
          l2tp: <value in [disable, enable]>
          auto-discovery-receiver: <value in [disable, enable]>
          auto-discovery-sender: <value in [disable, enable]>
          network-id: <integer>
          network-overlay: <value in [enable, disable]>
          protocol: <integer>
```

## [Return Values](fmgr_vpnmgr_node_module.md#id5)

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
