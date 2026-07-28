---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_fsp_vlan_dynamicmapping_module.html
fetched_at: 2026-07-27T17:32:44+00:00
---
# fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_fsp_vlan_dynamicmapping_module.md#synopsis)
- [Parameters](fmgr_fsp_vlan_dynamicmapping_module.md#parameters)
- [Notes](fmgr_fsp_vlan_dynamicmapping_module.md#notes)
- [Examples](fmgr_fsp_vlan_dynamicmapping_module.md#examples)
- [Return Values](fmgr_fsp_vlan_dynamicmapping_module.md#return-values)

## [Synopsis](fmgr_fsp_vlan_dynamicmapping_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_fsp_vlan_dynamicmapping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **fsp_vlan_dynamicmapping**  dictionary | the top level parameters set |
| **_dhcp-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **_scope**  list / elements=string | description |
| **name**  string | no description |
| **vdom**  string | no description |
| **dhcp-server**  dictionary | no description |
| **auto-configuration**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **auto-managed-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **conflicted-ip-timeout**  integer | no description |
| **ddns-auth**  string | no description  Choices:   - `"disable"` - `"tsig"` |
| **ddns-key**  string | no description |
| **ddns-keyname**  string | no description |
| **ddns-server-ip**  string | no description |
| **ddns-ttl**  integer | no description |
| **ddns-update**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ddns-update-override**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ddns-zone**  string | no description |
| **default-gateway**  string | no description |
| **dhcp-settings-from-fortiipam**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dns-server1**  string | no description |
| **dns-server2**  string | no description |
| **dns-server3**  string | no description |
| **dns-server4**  string | no description |
| **dns-service**  string | no description  Choices:   - `"default"` - `"specify"` - `"local"` |
| **domain**  string | no description |
| **enable**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **exclude-range**  list / elements=string | description |
| **end-ip**  string | no description |
| **id**  integer | no description |
| **start-ip**  string | no description |
| **filename**  string | no description |
| **forticlient-on-net-status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **id**  integer | no description |
| **ip-mode**  string | no description  Choices:   - `"range"` - `"usrgrp"` |
| **ip-range**  list / elements=string | description |
| **end-ip**  string | no description |
| **id**  integer | no description |
| **start-ip**  string | no description |
| **ipsec-lease-hold**  integer | no description |
| **lease-time**  integer | no description |
| **mac-acl-default-action**  string | no description  Choices:   - `"assign"` - `"block"` |
| **netmask**  string | no description |
| **next-server**  string | no description |
| **ntp-server1**  string | no description |
| **ntp-server2**  string | no description |
| **ntp-server3**  string | no description |
| **ntp-service**  string | no description  Choices:   - `"default"` - `"specify"` - `"local"` |
| **option1**  string | description |
| **option2**  string | description |
| **option3**  string | description |
| **option4**  string | no description |
| **option5**  string | no description |
| **option6**  string | no description |
| **options**  list / elements=string | description |
| **code**  integer | no description |
| **id**  integer | no description |
| **ip**  string | description |
| **type**  string | no description  Choices:   - `"hex"` - `"string"` - `"ip"` - `"fqdn"` |
| **value**  string | no description |
| **reserved-address**  list / elements=string | description |
| **action**  string | no description  Choices:   - `"assign"` - `"block"` - `"reserved"` |
| **circuit-id**  string | no description |
| **circuit-id-type**  string | no description  Choices:   - `"hex"` - `"string"` |
| **description**  string | no description |
| **id**  integer | no description |
| **ip**  string | no description |
| **mac**  string | no description |
| **remote-id**  string | no description |
| **remote-id-type**  string | no description  Choices:   - `"hex"` - `"string"` |
| **type**  string | no description  Choices:   - `"mac"` - `"option82"` |
| **server-type**  string | no description  Choices:   - `"regular"` - `"ipsec"` |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **tftp-server**  string | description |
| **timezone**  string | no description  Choices:   - `"00"` - `"01"` - `"02"` - `"03"` - `"04"` - `"05"` - `"06"` - `"07"` - `"08"` - `"09"` - `"10"` - `"11"` - `"12"` - `"13"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"22"` - `"23"` - `"24"` - `"25"` - `"26"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` - `"32"` - `"33"` - `"34"` - `"35"` - `"36"` - `"37"` - `"38"` - `"39"` - `"40"` - `"41"` - `"42"` - `"43"` - `"44"` - `"45"` - `"46"` - `"47"` - `"48"` - `"49"` - `"50"` - `"51"` - `"52"` - `"53"` - `"54"` - `"55"` - `"56"` - `"57"` - `"58"` - `"59"` - `"60"` - `"61"` - `"62"` - `"63"` - `"64"` - `"65"` - `"66"` - `"67"` - `"68"` - `"69"` - `"70"` - `"71"` - `"72"` - `"73"` - `"74"` - `"75"` - `"76"` - `"77"` - `"78"` - `"79"` - `"80"` - `"81"` - `"82"` - `"83"` - `"84"` - `"85"` - `"86"` - `"87"` |
| **timezone-option**  string | no description  Choices:   - `"disable"` - `"default"` - `"specify"` |
| **vci-match**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **vci-string**  string | description |
| **wifi-ac-service**  string | no description  Choices:   - `"specify"` - `"local"` |
| **wifi-ac1**  string | no description |
| **wifi-ac2**  string | no description |
| **wifi-ac3**  string | no description |
| **wins-server1**  string | no description |
| **wins-server2**  string | no description |
| **interface**  dictionary | no description |
| **dhcp-relay-agent-option**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dhcp-relay-interface-select-method**  string | no description  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **dhcp-relay-ip**  string | description |
| **dhcp-relay-service**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dhcp-relay-type**  string | no description  Choices:   - `"regular"` - `"ipsec"` |
| **ip**  string | no description |
| **ipv6**  dictionary | no description |
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
| **secondary-IP**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **secondaryip**  list / elements=string | description |
| **allowaccess**  list / elements=string | description  Choices:   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"auto-ipsec"` - `"radius-acct"` - `"probe-response"` - `"capwap"` - `"dnp"` - `"ftm"` - `"fabric"` - `"speed-test"` |
| **detectprotocol**  list / elements=string | description  Choices:   - `"ping"` - `"tcp-echo"` - `"udp-echo"` |
| **detectserver**  string | no description |
| **gwdetect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ha-priority**  integer | no description |
| **id**  integer | no description |
| **ip**  string | no description |
| **ping-serv-status**  integer | no description |
| **seq**  integer | no description |
| **vlanid**  integer | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **vlan**  string / required | the parameter (vlan) in requested url |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

## [Notes](fmgr_fsp_vlan_dynamicmapping_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_fsp_vlan_dynamicmapping_module.md#id4)

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
     fmgr_fsp_vlan_dynamicmapping:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        vlan: <your own value>
        state: <value in [present, absent]>
        fsp_vlan_dynamicmapping:
           _dhcp-status: <value in [disable, enable]>
           _scope:
             -
                 name: <value of string>
                 vdom: <value of string>
           dhcp-server:
              auto-configuration: <value in [disable, enable]>
              auto-managed-status: <value in [disable, enable]>
              conflicted-ip-timeout: <value of integer>
              ddns-auth: <value in [disable, tsig]>
              ddns-key: <value of string>
              ddns-keyname: <value of string>
              ddns-server-ip: <value of string>
              ddns-ttl: <value of integer>
              ddns-update: <value in [disable, enable]>
              ddns-update-override: <value in [disable, enable]>
              ddns-zone: <value of string>
              default-gateway: <value of string>
              dhcp-settings-from-fortiipam: <value in [disable, enable]>
              dns-server1: <value of string>
              dns-server2: <value of string>
              dns-server3: <value of string>
              dns-server4: <value of string>
              dns-service: <value in [default, specify, local]>
              domain: <value of string>
              enable: <value in [disable, enable]>
              exclude-range:
                -
                    end-ip: <value of string>
                    id: <value of integer>
                    start-ip: <value of string>
              filename: <value of string>
              forticlient-on-net-status: <value in [disable, enable]>
              id: <value of integer>
              ip-mode: <value in [range, usrgrp]>
              ip-range:
                -
                    end-ip: <value of string>
                    id: <value of integer>
                    start-ip: <value of string>
              ipsec-lease-hold: <value of integer>
              lease-time: <value of integer>
              mac-acl-default-action: <value in [assign, block]>
              netmask: <value of string>
              next-server: <value of string>
              ntp-server1: <value of string>
              ntp-server2: <value of string>
              ntp-server3: <value of string>
              ntp-service: <value in [default, specify, local]>
              option1: <value of string>
              option2: <value of string>
              option3: <value of string>
              option4: <value of string>
              option5: <value of string>
              option6: <value of string>
              options:
                -
                    code: <value of integer>
                    id: <value of integer>
                    ip: <value of string>
                    type: <value in [hex, string, ip, ...]>
                    value: <value of string>
              reserved-address:
                -
                    action: <value in [assign, block, reserved]>
                    circuit-id: <value of string>
                    circuit-id-type: <value in [hex, string]>
                    description: <value of string>
                    id: <value of integer>
                    ip: <value of string>
                    mac: <value of string>
                    remote-id: <value of string>
                    remote-id-type: <value in [hex, string]>
                    type: <value in [mac, option82]>
              server-type: <value in [regular, ipsec]>
              status: <value in [disable, enable]>
              tftp-server: <value of string>
              timezone: <value in [00, 01, 02, ...]>
              timezone-option: <value in [disable, default, specify]>
              vci-match: <value in [disable, enable]>
              vci-string: <value of string>
              wifi-ac-service: <value in [specify, local]>
              wifi-ac1: <value of string>
              wifi-ac2: <value of string>
              wifi-ac3: <value of string>
              wins-server1: <value of string>
              wins-server2: <value of string>
           interface:
              dhcp-relay-agent-option: <value in [disable, enable]>
              dhcp-relay-ip: <value of string>
              dhcp-relay-service: <value in [disable, enable]>
              dhcp-relay-type: <value in [regular, ipsec]>
              ip: <value of string>
              ipv6:
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
                 icmp6-send-redirect: <value in [disable, enable]>
                 interface-identifier: <value of string>
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
                 unique-autoconf-addr: <value in [disable, enable]>
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
                 cli-conn6-status: <value of integer>
                 ip6-prefix-mode: <value in [dhcp6, ra]>
                 ra-send-mtu: <value in [disable, enable]>
                 ip6-delegated-prefix-iaid: <value of integer>
              secondary-IP: <value in [disable, enable]>
              secondaryip:
                -
                    allowaccess:
                      - https
                      - ping
                      - ssh
                      - snmp
                      - http
                      - telnet
                      - fgfm
                      - auto-ipsec
                      - radius-acct
                      - probe-response
                      - capwap
                      - dnp
                      - ftm
                      - fabric
                      - speed-test
                    detectprotocol:
                      - ping
                      - tcp-echo
                      - udp-echo
                    detectserver: <value of string>
                    gwdetect: <value in [disable, enable]>
                    ha-priority: <value of integer>
                    id: <value of integer>
                    ip: <value of string>
                    ping-serv-status: <value of integer>
                    seq: <value of integer>
              vlanid: <value of integer>
              dhcp-relay-interface-select-method: <value in [auto, sdwan, specify]>
```

## [Return Values](fmgr_fsp_vlan_dynamicmapping_module.md#id5)

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
