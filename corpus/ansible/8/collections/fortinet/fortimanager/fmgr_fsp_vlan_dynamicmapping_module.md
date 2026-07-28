---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping module – no description"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_fsp_vlan_dynamicmapping_module.html
fetched_at: 2026-07-28T02:13:56+00:00
---
# fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fsp_vlan_dynamicmapping`.

New in fortinet.fortimanager 2.0.0

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
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **fsp_vlan_dynamicmapping**  dictionary | the top level parameters set |
| **_dhcp-status**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **_scope**  list / elements=dictionary | no description |
| **name**  string | no description |
| **vdom**  string | no description |
| **dhcp-server**  dictionary | no description |
| **auto-configuration**  string | Enable/disable auto configuration.  **Choices:**   - `"disable"` - `"enable"` |
| **auto-managed-status**  string | Enable/disable use of this DHCP server once this interface has been assigned an IP address from FortiIPAM.  **Choices:**   - `"disable"` - `"enable"` |
| **conflicted-ip-timeout**  integer | Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused. |
| **ddns-auth**  string | DDNS authentication mode.  **Choices:**   - `"disable"` - `"tsig"` |
| **ddns-key**  any | (list or str) DDNS update key |
| **ddns-keyname**  string | DDNS update key name. |
| **ddns-server-ip**  string | DDNS server IP. |
| **ddns-ttl**  integer | TTL. |
| **ddns-update**  string | Enable/disable DDNS update for DHCP.  **Choices:**   - `"disable"` - `"enable"` |
| **ddns-update-override**  string | Enable/disable DDNS update override for DHCP.  **Choices:**   - `"disable"` - `"enable"` |
| **ddns-zone**  string | Zone of your domain name |
| **default-gateway**  string | Default gateway IP address assigned by the DHCP server. |
| **dhcp-settings-from-fortiipam**  string | Enable/disable populating of DHCP server settings from FortiIPAM.  **Choices:**   - `"disable"` - `"enable"` |
| **dns-server1**  string | DNS server 1. |
| **dns-server2**  string | DNS server 2. |
| **dns-server3**  string | DNS server 3. |
| **dns-server4**  string | DNS server 4. |
| **dns-service**  string | Options for assigning DNS servers to DHCP clients.  **Choices:**   - `"default"` - `"specify"` - `"local"` |
| **domain**  string | Domain name suffix for the IP addresses that the DHCP server assigns to clients. |
| **enable**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **exclude-range**  list / elements=dictionary | no description |
| **end-ip**  string | End of IP range. |
| **id**  integer | ID. |
| **lease-time**  integer | Lease time in seconds, 0 means default lease time. |
| **start-ip**  string | Start of IP range. |
| **uci-match**  string | Enable/disable user class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **uci-string**  any | (list) no description |
| **vci-match**  string | Enable/disable vendor class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **vci-string**  any | (list) no description |
| **filename**  string | Name of the boot file on the TFTP server. |
| **forticlient-on-net-status**  string | Enable/disable FortiClient-On-Net service for this DHCP server.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer | ID. |
| **ip-mode**  string | Method used to assign client IP.  **Choices:**   - `"range"` - `"usrgrp"` |
| **ip-range**  list / elements=dictionary | no description |
| **end-ip**  string | End of IP range. |
| **id**  integer | ID. |
| **lease-time**  integer | Lease time in seconds, 0 means default lease time. |
| **start-ip**  string | Start of IP range. |
| **uci-match**  string | Enable/disable user class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **uci-string**  any | (list) no description |
| **vci-match**  string | Enable/disable vendor class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **vci-string**  any | (list) no description |
| **ipsec-lease-hold**  integer | DHCP over IPsec leases expire this many seconds after tunnel down |
| **lease-time**  integer | Lease time in seconds, 0 means unlimited. |
| **mac-acl-default-action**  string | MAC access control default action  **Choices:**   - `"assign"` - `"block"` |
| **netmask**  string | Netmask assigned by the DHCP server. |
| **next-server**  string | IP address of a server |
| **ntp-server1**  string | NTP server 1. |
| **ntp-server2**  string | NTP server 2. |
| **ntp-server3**  string | NTP server 3. |
| **ntp-service**  string | Options for assigning Network Time Protocol  **Choices:**   - `"default"` - `"specify"` - `"local"` |
| **option1**  any | (list) no description |
| **option2**  any | (list) no description |
| **option3**  any | (list) no description |
| **option4**  string | no description |
| **option5**  string | no description |
| **option6**  string | no description |
| **options**  list / elements=dictionary | no description |
| **code**  integer | DHCP option code. |
| **id**  integer | ID. |
| **ip**  any | (list) no description |
| **type**  string | DHCP option type.  **Choices:**   - `"hex"` - `"string"` - `"ip"` - `"fqdn"` |
| **uci-match**  string | Enable/disable user class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **uci-string**  any | (list) no description |
| **value**  string | DHCP option value. |
| **vci-match**  string | Enable/disable vendor class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **vci-string**  any | (list) no description |
| **relay-agent**  string | Relay agent IP. |
| **reserved-address**  list / elements=dictionary | no description |
| **action**  string | Options for the DHCP server to configure the client with the reserved MAC address.  **Choices:**   - `"assign"` - `"block"` - `"reserved"` |
| **circuit-id**  string | Option 82 circuit-ID of the client that will get the reserved IP address. |
| **circuit-id-type**  string | DHCP option type.  **Choices:**   - `"hex"` - `"string"` |
| **description**  string | Description. |
| **id**  integer | ID. |
| **ip**  string | IP address to be reserved for the MAC address. |
| **mac**  string | MAC address of the client that will get the reserved IP address. |
| **remote-id**  string | Option 82 remote-ID of the client that will get the reserved IP address. |
| **remote-id-type**  string | DHCP option type.  **Choices:**   - `"hex"` - `"string"` |
| **type**  string | DHCP reserved-address type.  **Choices:**   - `"mac"` - `"option82"` |
| **server-type**  string | DHCP server can be a normal DHCP server or an IPsec DHCP server.  **Choices:**   - `"regular"` - `"ipsec"` |
| **shared-subnet**  string | Enable/disable shared subnet.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable this DHCP configuration.  **Choices:**   - `"disable"` - `"enable"` |
| **tftp-server**  any | (list) no description |
| **timezone**  string | Select the time zone to be assigned to DHCP clients.  **Choices:**   - `"00"` - `"01"` - `"02"` - `"03"` - `"04"` - `"05"` - `"06"` - `"07"` - `"08"` - `"09"` - `"10"` - `"11"` - `"12"` - `"13"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"22"` - `"23"` - `"24"` - `"25"` - `"26"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` - `"32"` - `"33"` - `"34"` - `"35"` - `"36"` - `"37"` - `"38"` - `"39"` - `"40"` - `"41"` - `"42"` - `"43"` - `"44"` - `"45"` - `"46"` - `"47"` - `"48"` - `"49"` - `"50"` - `"51"` - `"52"` - `"53"` - `"54"` - `"55"` - `"56"` - `"57"` - `"58"` - `"59"` - `"60"` - `"61"` - `"62"` - `"63"` - `"64"` - `"65"` - `"66"` - `"67"` - `"68"` - `"69"` - `"70"` - `"71"` - `"72"` - `"73"` - `"74"` - `"75"` - `"76"` - `"77"` - `"78"` - `"79"` - `"80"` - `"81"` - `"82"` - `"83"` - `"84"` - `"85"` - `"86"` - `"87"` |
| **timezone-option**  string | Options for the DHCP server to set the clients time zone.  **Choices:**   - `"disable"` - `"default"` - `"specify"` |
| **vci-match**  string | Enable/disable vendor class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **vci-string**  any | (list) no description |
| **wifi-ac-service**  string | Options for assigning WiFi Access Controllers to DHCP clients  **Choices:**   - `"specify"` - `"local"` |
| **wifi-ac1**  string | WiFi Access Controller 1 IP address |
| **wifi-ac2**  string | WiFi Access Controller 2 IP address |
| **wifi-ac3**  string | WiFi Access Controller 3 IP address |
| **wins-server1**  string | WINS server 1. |
| **wins-server2**  string | WINS server 2. |
| **interface**  dictionary | no description |
| **dhcp-relay-agent-option**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-relay-interface-select-method**  string | no description  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **dhcp-relay-ip**  any | (list) no description |
| **dhcp-relay-service**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-relay-type**  string | no description  **Choices:**   - `"regular"` - `"ipsec"` |
| **ip**  string | no description |
| **ipv6**  dictionary | no description |
| **autoconf**  string | Enable/disable address auto config.  **Choices:**   - `"disable"` - `"enable"` |
| **cli-conn6-status**  integer | no description |
| **dhcp6-client-options**  list / elements=string | no description  **Choices:**   - `"rapid"` - `"iapd"` - `"iana"` - `"dns"` - `"dnsname"` |
| **dhcp6-information-request**  string | Enable/disable DHCPv6 information request.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp6-prefix-delegation**  string | Enable/disable DHCPv6 prefix delegation.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp6-prefix-hint**  string | DHCPv6 prefix that will be used as a hint to the upstream DHCPv6 server. |
| **dhcp6-prefix-hint-plt**  integer | DHCPv6 prefix hint preferred life time |
| **dhcp6-prefix-hint-vlt**  integer | DHCPv6 prefix hint valid life time |
| **dhcp6-relay-interface-id**  string | DHCP6 relay interface ID. |
| **dhcp6-relay-ip**  string | DHCPv6 relay IP address. |
| **dhcp6-relay-service**  string | Enable/disable DHCPv6 relay.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp6-relay-source-interface**  string | Enable/disable use of address on this interface as the source address of the relay message.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp6-relay-source-ip**  string | IPv6 address used by the DHCP6 relay as its source IP. |
| **dhcp6-relay-type**  string | DHCPv6 relay type.  **Choices:**   - `"regular"` |
| **icmp6-send-redirect**  string | Enable/disable sending of ICMPv6 redirects.  **Choices:**   - `"disable"` - `"enable"` |
| **interface-identifier**  string | IPv6 interface identifier. |
| **ip6-address**  string | Primary IPv6 address prefix, syntax |
| **ip6-allowaccess**  list / elements=string | no description  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"capwap"` - `"fabric"` |
| **ip6-default-life**  integer | Default life |
| **ip6-delegated-prefix-iaid**  integer | IAID of obtained delegated-prefix from the upstream interface. |
| **ip6-delegated-prefix-list**  list / elements=dictionary | no description |
| **autonomous-flag**  string | Enable/disable the autonomous flag.  **Choices:**   - `"disable"` - `"enable"` |
| **delegated-prefix-iaid**  integer | IAID of obtained delegated-prefix from the upstream interface. |
| **onlink-flag**  string | Enable/disable the onlink flag.  **Choices:**   - `"disable"` - `"enable"` |
| **prefix-id**  integer | Prefix ID. |
| **rdnss**  any | (list) no description |
| **rdnss-service**  string | Recursive DNS service option.  **Choices:**   - `"delegated"` - `"default"` - `"specify"` |
| **subnet**  string | Add subnet ID to routing prefix. |
| **upstream-interface**  string | Name of the interface that provides delegated information. |
| **ip6-dns-server-override**  string | Enable/disable using the DNS server acquired by DHCP.  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-extra-addr**  list / elements=dictionary | no description |
| **prefix**  string | IPv6 address prefix. |
| **ip6-hop-limit**  integer | Hop limit |
| **ip6-link-mtu**  integer | IPv6 link MTU. |
| **ip6-manage-flag**  string | Enable/disable the managed flag.  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-max-interval**  integer | IPv6 maximum interval |
| **ip6-min-interval**  integer | IPv6 minimum interval |
| **ip6-mode**  string | Addressing mode  **Choices:**   - `"static"` - `"dhcp"` - `"pppoe"` - `"delegated"` |
| **ip6-other-flag**  string | Enable/disable the other IPv6 flag.  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-prefix-list**  list / elements=dictionary | no description |
| **autonomous-flag**  string | Enable/disable the autonomous flag.  **Choices:**   - `"disable"` - `"enable"` |
| **dnssl**  any | (list) no description |
| **onlink-flag**  string | Enable/disable the onlink flag.  **Choices:**   - `"disable"` - `"enable"` |
| **preferred-life-time**  integer | Preferred life time |
| **prefix**  string | IPv6 prefix. |
| **rdnss**  any | (list) no description |
| **valid-life-time**  integer | Valid life time |
| **ip6-prefix-mode**  string | Assigning a prefix from DHCP or RA.  **Choices:**   - `"dhcp6"` - `"ra"` |
| **ip6-reachable-time**  integer | IPv6 reachable time |
| **ip6-retrans-time**  integer | IPv6 retransmit time |
| **ip6-send-adv**  string | Enable/disable sending advertisements about the interface.  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-subnet**  string | Subnet to routing prefix, syntax |
| **ip6-upstream-interface**  string | Interface name providing delegated information. |
| **nd-cert**  string | Neighbor discovery certificate. |
| **nd-cga-modifier**  string | Neighbor discovery CGA modifier. |
| **nd-mode**  string | Neighbor discovery mode.  **Choices:**   - `"basic"` - `"SEND-compatible"` |
| **nd-security-level**  integer | Neighbor discovery security level |
| **nd-timestamp-delta**  integer | Neighbor discovery timestamp delta value |
| **nd-timestamp-fuzz**  integer | Neighbor discovery timestamp fuzz factor |
| **ra-send-mtu**  string | Enable/disable sending link MTU in RA packet.  **Choices:**   - `"disable"` - `"enable"` |
| **unique-autoconf-addr**  string | Enable/disable unique auto config address.  **Choices:**   - `"disable"` - `"enable"` |
| **vrip6_link_local**  string | Link-local IPv6 address of virtual router. |
| **vrrp-virtual-mac6**  string | Enable/disable virtual MAC for VRRP.  **Choices:**   - `"disable"` - `"enable"` |
| **vrrp6**  list / elements=dictionary | no description |
| **accept-mode**  string | Enable/disable accept mode.  **Choices:**   - `"disable"` - `"enable"` |
| **adv-interval**  integer | Advertisement interval |
| **preempt**  string | Enable/disable preempt mode.  **Choices:**   - `"disable"` - `"enable"` |
| **priority**  integer | Priority of the virtual router |
| **start-time**  integer | Startup time |
| **status**  string | Enable/disable VRRP.  **Choices:**   - `"disable"` - `"enable"` |
| **vrdst6**  string | Monitor the route to this destination. |
| **vrgrp**  integer | VRRP group ID |
| **vrid**  integer | Virtual router identifier |
| **vrip6**  string | IPv6 address of the virtual router. |
| **secondary-IP**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **secondaryip**  list / elements=dictionary | no description |
| **allowaccess**  list / elements=string | no description  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"auto-ipsec"` - `"radius-acct"` - `"probe-response"` - `"capwap"` - `"dnp"` - `"ftm"` - `"fabric"` - `"speed-test"` |
| **detectprotocol**  list / elements=string | no description  **Choices:**   - `"ping"` - `"tcp-echo"` - `"udp-echo"` |
| **detectserver**  string | Gateways ping server for this IP. |
| **gwdetect**  string | Enable/disable detect gateway alive for first.  **Choices:**   - `"disable"` - `"enable"` |
| **ha-priority**  integer | HA election priority for the PING server. |
| **id**  integer | ID. |
| **ip**  string | Secondary IP address of the interface. |
| **ping-serv-status**  integer | no description |
| **secip-relay-ip**  string | DHCP relay IP address. |
| **seq**  integer | no description |
| **vlanid**  integer | no description |
| **vrrp**  list / elements=dictionary | no description |
| **accept-mode**  string | Enable/disable accept mode.  **Choices:**   - `"disable"` - `"enable"` |
| **adv-interval**  integer | Advertisement interval |
| **ignore-default-route**  string | Enable/disable ignoring of default route when checking destination.  **Choices:**   - `"disable"` - `"enable"` |
| **preempt**  string | Enable/disable preempt mode.  **Choices:**   - `"disable"` - `"enable"` |
| **priority**  integer | Priority of the virtual router |
| **proxy-arp**  list / elements=dictionary | no description |
| **id**  integer | ID. |
| **ip**  string | Set IP addresses of proxy ARP. |
| **start-time**  integer | Startup time |
| **status**  string | Enable/disable this VRRP configuration.  **Choices:**   - `"disable"` - `"enable"` |
| **version**  string | VRRP version.  **Choices:**   - `"2"` - `"3"` |
| **vrdst**  any | (list) no description |
| **vrdst-priority**  integer | Priority of the virtual router when the virtual router destination becomes unreachable |
| **vrgrp**  integer | VRRP group ID |
| **vrid**  integer | Virtual router identifier |
| **vrip**  string | IP address of the virtual router. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **vlan**  string / required | the parameter (vlan) in requested url |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

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
              name: <string>
              vdom: <string>
          dhcp-server:
            auto-configuration: <value in [disable, enable]>
            auto-managed-status: <value in [disable, enable]>
            conflicted-ip-timeout: <integer>
            ddns-auth: <value in [disable, tsig]>
            ddns-key: <list or string>
            ddns-keyname: <string>
            ddns-server-ip: <string>
            ddns-ttl: <integer>
            ddns-update: <value in [disable, enable]>
            ddns-update-override: <value in [disable, enable]>
            ddns-zone: <string>
            default-gateway: <string>
            dhcp-settings-from-fortiipam: <value in [disable, enable]>
            dns-server1: <string>
            dns-server2: <string>
            dns-server3: <string>
            dns-server4: <string>
            dns-service: <value in [default, specify, local]>
            domain: <string>
            enable: <value in [disable, enable]>
            exclude-range:
              -
                end-ip: <string>
                id: <integer>
                start-ip: <string>
                vci-match: <value in [disable, enable]>
                vci-string: <list or string>
                lease-time: <integer>
                uci-match: <value in [disable, enable]>
                uci-string: <list or string>
            filename: <string>
            forticlient-on-net-status: <value in [disable, enable]>
            id: <integer>
            ip-mode: <value in [range, usrgrp]>
            ip-range:
              -
                end-ip: <string>
                id: <integer>
                start-ip: <string>
                vci-match: <value in [disable, enable]>
                vci-string: <list or string>
                lease-time: <integer>
                uci-match: <value in [disable, enable]>
                uci-string: <list or string>
            ipsec-lease-hold: <integer>
            lease-time: <integer>
            mac-acl-default-action: <value in [assign, block]>
            netmask: <string>
            next-server: <string>
            ntp-server1: <string>
            ntp-server2: <string>
            ntp-server3: <string>
            ntp-service: <value in [default, specify, local]>
            option1: <list or string>
            option2: <list or string>
            option3: <list or string>
            option4: <string>
            option5: <string>
            option6: <string>
            options:
              -
                code: <integer>
                id: <integer>
                ip: <list or string>
                type: <value in [hex, string, ip, ...]>
                value: <string>
                vci-match: <value in [disable, enable]>
                vci-string: <list or string>
                uci-match: <value in [disable, enable]>
                uci-string: <list or string>
            reserved-address:
              -
                action: <value in [assign, block, reserved]>
                circuit-id: <string>
                circuit-id-type: <value in [hex, string]>
                description: <string>
                id: <integer>
                ip: <string>
                mac: <string>
                remote-id: <string>
                remote-id-type: <value in [hex, string]>
                type: <value in [mac, option82]>
            server-type: <value in [regular, ipsec]>
            status: <value in [disable, enable]>
            tftp-server: <list or string>
            timezone: <value in [00, 01, 02, ...]>
            timezone-option: <value in [disable, default, specify]>
            vci-match: <value in [disable, enable]>
            vci-string: <list or string>
            wifi-ac-service: <value in [specify, local]>
            wifi-ac1: <string>
            wifi-ac2: <string>
            wifi-ac3: <string>
            wins-server1: <string>
            wins-server2: <string>
            relay-agent: <string>
            shared-subnet: <value in [disable, enable]>
          interface:
            dhcp-relay-agent-option: <value in [disable, enable]>
            dhcp-relay-ip: <list or string>
            dhcp-relay-service: <value in [disable, enable]>
            dhcp-relay-type: <value in [regular, ipsec]>
            ip: <string>
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
              dhcp6-prefix-hint: <string>
              dhcp6-prefix-hint-plt: <integer>
              dhcp6-prefix-hint-vlt: <integer>
              dhcp6-relay-ip: <string>
              dhcp6-relay-service: <value in [disable, enable]>
              dhcp6-relay-type: <value in [regular]>
              icmp6-send-redirect: <value in [disable, enable]>
              interface-identifier: <string>
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
              unique-autoconf-addr: <value in [disable, enable]>
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
              cli-conn6-status: <integer>
              ip6-prefix-mode: <value in [dhcp6, ra]>
              ra-send-mtu: <value in [disable, enable]>
              ip6-delegated-prefix-iaid: <integer>
              dhcp6-relay-source-interface: <value in [disable, enable]>
              dhcp6-relay-interface-id: <string>
              dhcp6-relay-source-ip: <string>
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
                detectserver: <string>
                gwdetect: <value in [disable, enable]>
                ha-priority: <integer>
                id: <integer>
                ip: <string>
                ping-serv-status: <integer>
                seq: <integer>
                secip-relay-ip: <string>
            vlanid: <integer>
            dhcp-relay-interface-select-method: <value in [auto, sdwan, specify]>
            vrrp:
              -
                accept-mode: <value in [disable, enable]>
                adv-interval: <integer>
                ignore-default-route: <value in [disable, enable]>
                preempt: <value in [disable, enable]>
                priority: <integer>
                proxy-arp:
                  -
                    id: <integer>
                    ip: <string>
                start-time: <integer>
                status: <value in [disable, enable]>
                version: <value in [2, 3]>
                vrdst: <list or string>
                vrdst-priority: <integer>
                vrgrp: <integer>
                vrid: <integer>
                vrip: <string>
```

## [Return Values](fmgr_fsp_vlan_dynamicmapping_module.md#id5)

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
