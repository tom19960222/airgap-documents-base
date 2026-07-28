---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_fsp_vlan module – no description"
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_fsp_vlan_module.html
fetched_at: 2026-07-28T02:13:49+00:00
---
# fortinet.fortimanager.fmgr_fsp_vlan module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fsp_vlan`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_fsp_vlan_module.md#synopsis)
- [Parameters](fmgr_fsp_vlan_module.md#parameters)
- [Notes](fmgr_fsp_vlan_module.md#notes)
- [Examples](fmgr_fsp_vlan_module.md#examples)
- [Return Values](fmgr_fsp_vlan_module.md#return-values)

## [Synopsis](fmgr_fsp_vlan_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_fsp_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **fsp_vlan**  dictionary | the top level parameters set |
| **_dhcp-status**  string | _Dhcp-Status.  **Choices:**   - `"disable"` - `"enable"` |
| **auth**  string | no description  **Choices:**   - `"radius"` - `"usergroup"` |
| **color**  integer | Color. |
| **comments**  string | no description |
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
| **enable**  string | Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **exclude-range**  list / elements=dictionary | Exclude-Range. |
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
| **ip-range**  list / elements=dictionary | Ip-Range. |
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
| **option1**  any | (list) Option1. |
| **option2**  any | (list) Option2. |
| **option3**  any | (list) Option3. |
| **option4**  string | Option4. |
| **option5**  string | Option5. |
| **option6**  string | Option6. |
| **options**  list / elements=dictionary | Options. |
| **code**  integer | DHCP option code. |
| **id**  integer | ID. |
| **ip**  any | (list) DHCP option IPs. |
| **type**  string | DHCP option type.  **Choices:**   - `"hex"` - `"string"` - `"ip"` - `"fqdn"` |
| **uci-match**  string | Enable/disable user class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **uci-string**  any | (list) no description |
| **value**  string | DHCP option value. |
| **vci-match**  string | Enable/disable vendor class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **vci-string**  any | (list) no description |
| **relay-agent**  string | Relay agent IP. |
| **reserved-address**  list / elements=dictionary | Reserved-Address. |
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
| **tftp-server**  any | (list) One or more hostnames or IP addresses of the TFTP servers in quotes separated by spaces. |
| **timezone**  string | Select the time zone to be assigned to DHCP clients.  **Choices:**   - `"00"` - `"01"` - `"02"` - `"03"` - `"04"` - `"05"` - `"06"` - `"07"` - `"08"` - `"09"` - `"10"` - `"11"` - `"12"` - `"13"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"22"` - `"23"` - `"24"` - `"25"` - `"26"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` - `"32"` - `"33"` - `"34"` - `"35"` - `"36"` - `"37"` - `"38"` - `"39"` - `"40"` - `"41"` - `"42"` - `"43"` - `"44"` - `"45"` - `"46"` - `"47"` - `"48"` - `"49"` - `"50"` - `"51"` - `"52"` - `"53"` - `"54"` - `"55"` - `"56"` - `"57"` - `"58"` - `"59"` - `"60"` - `"61"` - `"62"` - `"63"` - `"64"` - `"65"` - `"66"` - `"67"` - `"68"` - `"69"` - `"70"` - `"71"` - `"72"` - `"73"` - `"74"` - `"75"` - `"76"` - `"77"` - `"78"` - `"79"` - `"80"` - `"81"` - `"82"` - `"83"` - `"84"` - `"85"` - `"86"` - `"87"` |
| **timezone-option**  string | Options for the DHCP server to set the clients time zone.  **Choices:**   - `"disable"` - `"default"` - `"specify"` |
| **vci-match**  string | Enable/disable vendor class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **vci-string**  any | (list) One or more VCI strings in quotes separated by spaces. |
| **wifi-ac-service**  string | Options for assigning WiFi Access Controllers to DHCP clients  **Choices:**   - `"specify"` - `"local"` |
| **wifi-ac1**  string | WiFi Access Controller 1 IP address |
| **wifi-ac2**  string | WiFi Access Controller 2 IP address |
| **wifi-ac3**  string | WiFi Access Controller 3 IP address |
| **wins-server1**  string | WINS server 1. |
| **wins-server2**  string | WINS server 2. |
| **dynamic_mapping**  list / elements=dictionary | Dynamic_Mapping. |
| **_dhcp-status**  string | _Dhcp-Status.  **Choices:**   - `"disable"` - `"enable"` |
| **_scope**  list / elements=dictionary | _Scope. |
| **name**  string | Name. |
| **vdom**  string | Vdom. |
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
| **enable**  string | Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **exclude-range**  list / elements=dictionary | Exclude-Range. |
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
| **ip-range**  list / elements=dictionary | Ip-Range. |
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
| **option1**  any | (list) Option1. |
| **option2**  any | (list) Option2. |
| **option3**  any | (list) Option3. |
| **option4**  string | Option4. |
| **option5**  string | Option5. |
| **option6**  string | Option6. |
| **options**  list / elements=dictionary | Options. |
| **code**  integer | DHCP option code. |
| **id**  integer | ID. |
| **ip**  any | (list) DHCP option IPs. |
| **type**  string | DHCP option type.  **Choices:**   - `"hex"` - `"string"` - `"ip"` - `"fqdn"` |
| **uci-match**  string | Enable/disable user class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **uci-string**  any | (list) no description |
| **value**  string | DHCP option value. |
| **vci-match**  string | Enable/disable vendor class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **vci-string**  any | (list) no description |
| **relay-agent**  string | Relay agent IP. |
| **reserved-address**  list / elements=dictionary | Reserved-Address. |
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
| **tftp-server**  any | (list) One or more hostnames or IP addresses of the TFTP servers in quotes separated by spaces. |
| **timezone**  string | Select the time zone to be assigned to DHCP clients.  **Choices:**   - `"00"` - `"01"` - `"02"` - `"03"` - `"04"` - `"05"` - `"06"` - `"07"` - `"08"` - `"09"` - `"10"` - `"11"` - `"12"` - `"13"` - `"14"` - `"15"` - `"16"` - `"17"` - `"18"` - `"19"` - `"20"` - `"21"` - `"22"` - `"23"` - `"24"` - `"25"` - `"26"` - `"27"` - `"28"` - `"29"` - `"30"` - `"31"` - `"32"` - `"33"` - `"34"` - `"35"` - `"36"` - `"37"` - `"38"` - `"39"` - `"40"` - `"41"` - `"42"` - `"43"` - `"44"` - `"45"` - `"46"` - `"47"` - `"48"` - `"49"` - `"50"` - `"51"` - `"52"` - `"53"` - `"54"` - `"55"` - `"56"` - `"57"` - `"58"` - `"59"` - `"60"` - `"61"` - `"62"` - `"63"` - `"64"` - `"65"` - `"66"` - `"67"` - `"68"` - `"69"` - `"70"` - `"71"` - `"72"` - `"73"` - `"74"` - `"75"` - `"76"` - `"77"` - `"78"` - `"79"` - `"80"` - `"81"` - `"82"` - `"83"` - `"84"` - `"85"` - `"86"` - `"87"` |
| **timezone-option**  string | Options for the DHCP server to set the clients time zone.  **Choices:**   - `"disable"` - `"default"` - `"specify"` |
| **vci-match**  string | Enable/disable vendor class identifier  **Choices:**   - `"disable"` - `"enable"` |
| **vci-string**  any | (list) One or more VCI strings in quotes separated by spaces. |
| **wifi-ac-service**  string | Options for assigning WiFi Access Controllers to DHCP clients  **Choices:**   - `"specify"` - `"local"` |
| **wifi-ac1**  string | WiFi Access Controller 1 IP address |
| **wifi-ac2**  string | WiFi Access Controller 2 IP address |
| **wifi-ac3**  string | WiFi Access Controller 3 IP address |
| **wins-server1**  string | WINS server 1. |
| **wins-server2**  string | WINS server 2. |
| **interface**  dictionary | no description |
| **dhcp-relay-agent-option**  string | Dhcp-Relay-Agent-Option.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-relay-interface-select-method**  string | no description  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **dhcp-relay-ip**  any | (list) Dhcp-Relay-Ip. |
| **dhcp-relay-service**  string | Dhcp-Relay-Service.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-relay-type**  string | Dhcp-Relay-Type.  **Choices:**   - `"regular"` - `"ipsec"` |
| **ip**  string | Ip. |
| **ipv6**  dictionary | no description |
| **autoconf**  string | Enable/disable address auto config.  **Choices:**   - `"disable"` - `"enable"` |
| **cli-conn6-status**  integer | Cli-Conn6-Status. |
| **dhcp6-client-options**  list / elements=string | Dhcp6-Client-Options.  **Choices:**   - `"rapid"` - `"iapd"` - `"iana"` - `"dns"` - `"dnsname"` |
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
| **ip6-allowaccess**  list / elements=string | Allow management access to the interface.  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"capwap"` - `"fabric"` |
| **ip6-default-life**  integer | Default life |
| **ip6-delegated-prefix-iaid**  integer | IAID of obtained delegated-prefix from the upstream interface. |
| **ip6-delegated-prefix-list**  list / elements=dictionary | Ip6-Delegated-Prefix-List. |
| **autonomous-flag**  string | Enable/disable the autonomous flag.  **Choices:**   - `"disable"` - `"enable"` |
| **delegated-prefix-iaid**  integer | IAID of obtained delegated-prefix from the upstream interface. |
| **onlink-flag**  string | Enable/disable the onlink flag.  **Choices:**   - `"disable"` - `"enable"` |
| **prefix-id**  integer | Prefix ID. |
| **rdnss**  any | (list) Recursive DNS server option. |
| **rdnss-service**  string | Recursive DNS service option.  **Choices:**   - `"delegated"` - `"default"` - `"specify"` |
| **subnet**  string | Add subnet ID to routing prefix. |
| **upstream-interface**  string | Name of the interface that provides delegated information. |
| **ip6-dns-server-override**  string | Enable/disable using the DNS server acquired by DHCP.  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-extra-addr**  list / elements=dictionary | Ip6-Extra-Addr. |
| **prefix**  string | IPv6 address prefix. |
| **ip6-hop-limit**  integer | Hop limit |
| **ip6-link-mtu**  integer | IPv6 link MTU. |
| **ip6-manage-flag**  string | Enable/disable the managed flag.  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-max-interval**  integer | IPv6 maximum interval |
| **ip6-min-interval**  integer | IPv6 minimum interval |
| **ip6-mode**  string | Addressing mode  **Choices:**   - `"static"` - `"dhcp"` - `"pppoe"` - `"delegated"` |
| **ip6-other-flag**  string | Enable/disable the other IPv6 flag.  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-prefix-list**  list / elements=dictionary | Ip6-Prefix-List. |
| **autonomous-flag**  string | Enable/disable the autonomous flag.  **Choices:**   - `"disable"` - `"enable"` |
| **dnssl**  any | (list) DNS search list option. |
| **onlink-flag**  string | Enable/disable the onlink flag.  **Choices:**   - `"disable"` - `"enable"` |
| **preferred-life-time**  integer | Preferred life time |
| **prefix**  string | IPv6 prefix. |
| **rdnss**  any | (list) Recursive DNS server option. |
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
| **vrrp6**  list / elements=dictionary | Vrrp6. |
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
| **secondary-IP**  string | Secondary-Ip.  **Choices:**   - `"disable"` - `"enable"` |
| **secondaryip**  list / elements=dictionary | Secondaryip. |
| **allowaccess**  list / elements=string | Management access settings for the secondary IP address.  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"auto-ipsec"` - `"radius-acct"` - `"probe-response"` - `"capwap"` - `"dnp"` - `"ftm"` - `"fabric"` - `"speed-test"` |
| **detectprotocol**  list / elements=string | Protocols used to detect the server.  **Choices:**   - `"ping"` - `"tcp-echo"` - `"udp-echo"` |
| **detectserver**  string | Gateways ping server for this IP. |
| **gwdetect**  string | Enable/disable detect gateway alive for first.  **Choices:**   - `"disable"` - `"enable"` |
| **ha-priority**  integer | HA election priority for the PING server. |
| **id**  integer | ID. |
| **ip**  string | Secondary IP address of the interface. |
| **ping-serv-status**  integer | Ping-Serv-Status. |
| **secip-relay-ip**  string | DHCP relay IP address. |
| **seq**  integer | Seq. |
| **vlanid**  integer | Vlanid. |
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
| **interface**  dictionary | no description |
| **ac-name**  string | PPPoE server name. |
| **aggregate**  string | Aggregate. |
| **aggregate-type**  string | Type of aggregation.  **Choices:**   - `"physical"` - `"vxlan"` |
| **algorithm**  string | Frame distribution algorithm.  **Choices:**   - `"L2"` - `"L3"` - `"L4"` - `"LB"` - `"Source-MAC"` |
| **alias**  string | Alias will be displayed with the interface name to make it easier to distinguish. |
| **allowaccess**  list / elements=string | Permitted types of management access to this interface.  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"auto-ipsec"` - `"radius-acct"` - `"probe-response"` - `"capwap"` - `"dnp"` - `"ftm"` - `"fabric"` - `"speed-test"` |
| **ap-discover**  string | Enable/disable automatic registration of unknown FortiAP devices.  **Choices:**   - `"disable"` - `"enable"` |
| **arpforward**  string | Enable/disable ARP forwarding.  **Choices:**   - `"disable"` - `"enable"` |
| **atm-protocol**  string | ATM protocol.  **Choices:**   - `"none"` - `"ipoa"` |
| **auth-cert**  string | HTTPS server certificate. |
| **auth-portal-addr**  string | Address of captive portal. |
| **auth-type**  string | PPP authentication type to use.  **Choices:**   - `"auto"` - `"pap"` - `"chap"` - `"mschapv1"` - `"mschapv2"` |
| **auto-auth-extension-device**  string | Enable/disable automatic authorization of dedicated Fortinet extension device on this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **bandwidth-measure-time**  integer | Bandwidth measure time |
| **bfd**  string | Bidirectional Forwarding Detection  **Choices:**   - `"global"` - `"enable"` - `"disable"` |
| **bfd-desired-min-tx**  integer | BFD desired minimal transmit interval. |
| **bfd-detect-mult**  integer | BFD detection multiplier. |
| **bfd-required-min-rx**  integer | BFD required minimal receive interval. |
| **broadcast-forticlient-discovery**  string | Enable/disable broadcasting FortiClient discovery messages.  **Choices:**   - `"disable"` - `"enable"` |
| **broadcast-forward**  string | Enable/disable broadcast forwarding.  **Choices:**   - `"disable"` - `"enable"` |
| **captive-portal**  integer | Enable/disable captive portal. |
| **cli-conn-status**  integer | Cli-Conn-Status. |
| **color**  integer | Color of icon on the GUI. |
| **ddns**  string | Ddns.  **Choices:**   - `"disable"` - `"enable"` |
| **ddns-auth**  string | Ddns-Auth.  **Choices:**   - `"disable"` - `"tsig"` |
| **ddns-domain**  string | Ddns-Domain. |
| **ddns-key**  any | (list or str) Ddns-Key. |
| **ddns-keyname**  string | Ddns-Keyname. |
| **ddns-password**  any | (list) Ddns-Password. |
| **ddns-server**  string | Ddns-Server.  **Choices:**   - `"dhs.org"` - `"dyndns.org"` - `"dyns.net"` - `"tzo.com"` - `"ods.org"` - `"vavic.com"` - `"now.net.cn"` - `"dipdns.net"` - `"easydns.com"` - `"genericDDNS"` |
| **ddns-server-ip**  string | Ddns-Server-Ip. |
| **ddns-sn**  string | Ddns-Sn. |
| **ddns-ttl**  integer | Ddns-Ttl. |
| **ddns-username**  string | Ddns-Username. |
| **ddns-zone**  string | Ddns-Zone. |
| **dedicated-to**  string | Configure interface for single purpose.  **Choices:**   - `"none"` - `"management"` |
| **default-purdue-level**  string | default purdue level of device detected on this interface.  **Choices:**   - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` - `"1.5"` - `"2.5"` - `"3.5"` - `"5.5"` |
| **defaultgw**  string | Enable to get the gateway IP from the DHCP or PPPoE server.  **Choices:**   - `"disable"` - `"enable"` |
| **description**  string | Description. |
| **detected-peer-mtu**  integer | Detected-Peer-Mtu. |
| **detectprotocol**  list / elements=string | Protocols used to detect the server.  **Choices:**   - `"ping"` - `"tcp-echo"` - `"udp-echo"` |
| **detectserver**  string | Gateways ping server for this IP. |
| **device-access-list**  any | (list or str) Device access list. |
| **device-identification**  string | Enable/disable passively gathering of device identity information about the devices on the network connected to this in…  **Choices:**   - `"disable"` - `"enable"` |
| **device-identification-active-scan**  string | Enable/disable active gathering of device identity information about the devices on the network connected to this inter…  **Choices:**   - `"disable"` - `"enable"` |
| **device-netscan**  string | Enable/disable inclusion of devices detected on this interface in network vulnerability scans.  **Choices:**   - `"disable"` - `"enable"` |
| **device-user-identification**  string | Enable/disable passive gathering of user identity information about users on this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **devindex**  integer | Devindex. |
| **dhcp-broadcast-flag**  string | Enable/disable setting of the broadcast flag in messages sent by the DHCP client  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-classless-route-addition**  string | Enable/disable addition of classless static routes retrieved from DHCP server.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-client-identifier**  string | DHCP client identifier. |
| **dhcp-relay-agent-option**  string | Enable/disable DHCP relay agent option.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-relay-circuit-id**  string | DHCP relay circuit ID. |
| **dhcp-relay-interface**  string | Specify outgoing interface to reach server. |
| **dhcp-relay-interface-select-method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **dhcp-relay-ip**  any | (list) DHCP relay IP address. |
| **dhcp-relay-link-selection**  string | DHCP relay link selection. |
| **dhcp-relay-request-all-server**  string | Enable/disable sending of DHCP requests to all servers.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-relay-service**  string | Enable/disable allowing this interface to act as a DHCP relay.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-relay-source-ip**  string | IP address used by the DHCP relay as its source IP. |
| **dhcp-relay-type**  string | DHCP relay type  **Choices:**   - `"regular"` - `"ipsec"` |
| **dhcp-renew-time**  integer | DHCP renew time in seconds |
| **dhcp-smart-relay**  string | Enable/disable DHCP smart relay.  **Choices:**   - `"disable"` - `"enable"` |
| **disc-retry-timeout**  integer | Time in seconds to wait before retrying to start a PPPoE discovery, 0 means no timeout. |
| **disconnect-threshold**  integer | Time in milliseconds to wait before sending a notification that this interface is down or disconnected. |
| **distance**  integer | Distance for routes learned through PPPoE or DHCP, lower distance indicates preferred route. |
| **dns-query**  string | Dns-Query.  **Choices:**   - `"disable"` - `"recursive"` - `"non-recursive"` |
| **dns-server-override**  string | Enable/disable use DNS acquired by DHCP or PPPoE.  **Choices:**   - `"disable"` - `"enable"` |
| **dns-server-protocol**  list / elements=string | no description  **Choices:**   - `"cleartext"` - `"dot"` - `"doh"` |
| **drop-fragment**  string | Enable/disable drop fragment packets.  **Choices:**   - `"disable"` - `"enable"` |
| **drop-overlapped-fragment**  string | Enable/disable drop overlapped fragment packets.  **Choices:**   - `"disable"` - `"enable"` |
| **eap-ca-cert**  string | EAP CA certificate name. |
| **eap-identity**  string | EAP identity. |
| **eap-method**  string | EAP method.  **Choices:**   - `"tls"` - `"peap"` |
| **eap-password**  any | (list) no description |
| **eap-supplicant**  string | Enable/disable EAP-Supplicant.  **Choices:**   - `"disable"` - `"enable"` |
| **eap-user-cert**  string | EAP user certificate name. |
| **egress-cos**  string | Override outgoing CoS in user VLAN tag.  **Choices:**   - `"disable"` - `"cos0"` - `"cos1"` - `"cos2"` - `"cos3"` - `"cos4"` - `"cos5"` - `"cos6"` - `"cos7"` |
| **egress-shaping-profile**  string | Outgoing traffic shaping profile. |
| **eip**  string | Eip. |
| **endpoint-compliance**  string | Enable/disable endpoint compliance enforcement.  **Choices:**   - `"disable"` - `"enable"` |
| **estimated-downstream-bandwidth**  integer | Estimated maximum downstream bandwidth |
| **estimated-upstream-bandwidth**  integer | Estimated maximum upstream bandwidth |
| **explicit-ftp-proxy**  string | Enable/disable the explicit FTP proxy on this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **explicit-web-proxy**  string | Enable/disable the explicit web proxy on this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **external**  string | Enable/disable identifying the interface as an external interface  **Choices:**   - `"disable"` - `"enable"` |
| **fail-action-on-extender**  string | Action on extender when interface fail .  **Choices:**   - `"soft-restart"` - `"hard-restart"` - `"reboot"` |
| **fail-alert-interfaces**  any | (list or str) Names of the FortiGate interfaces to which the link failure alert is sent. |
| **fail-alert-method**  string | Select link-failed-signal or link-down method to alert about a failed link.  **Choices:**   - `"link-failed-signal"` - `"link-down"` |
| **fail-detect**  string | Enable/disable fail detection features for this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **fail-detect-option**  list / elements=string | Options for detecting that this interface has failed.  **Choices:**   - `"detectserver"` - `"link-down"` |
| **fdp**  string | Fdp.  **Choices:**   - `"disable"` - `"enable"` |
| **fortiheartbeat**  string | Enable/disable FortiHeartBeat  **Choices:**   - `"disable"` - `"enable"` |
| **fortilink**  string | Enable FortiLink to dedicate this interface to manage other Fortinet devices.  **Choices:**   - `"disable"` - `"enable"` |
| **fortilink-backup-link**  integer | Fortilink-Backup-Link. |
| **fortilink-neighbor-detect**  string | Protocol for FortiGate neighbor discovery.  **Choices:**   - `"lldp"` - `"fortilink"` |
| **fortilink-split-interface**  string | Enable/disable FortiLink split interface to connect member link to different FortiSwitch in stack for uplink redundancy.  **Choices:**   - `"disable"` - `"enable"` |
| **fortilink-stacking**  string | Enable/disable FortiLink switch-stacking on this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **forward-domain**  integer | Transparent mode forward domain. |
| **forward-error-correction**  string | Enable/disable forward error correction  **Choices:**   - `"disable"` - `"enable"` - `"rs-fec"` - `"base-r-fec"` - `"fec-cl91"` - `"fec-cl74"` - `"rs-544"` - `"none"` - `"cl91-rs-fec"` - `"cl74-fc-fec"` - `"auto"` |
| **fp-anomaly**  list / elements=string | Fp-Anomaly.  **Choices:**   - `"drop_tcp_fin_noack"` - `"pass_winnuke"` - `"pass_tcpland"` - `"pass_udpland"` - `"pass_icmpland"` - `"pass_ipland"` - `"pass_iprr"` - `"pass_ipssrr"` - `"pass_iplsrr"` - `"pass_ipstream"` - `"pass_ipsecurity"` - `"pass_iptimestamp"` - `"pass_ipunknown_option"` - `"pass_ipunknown_prot"` - `"pass_icmp_frag"` - `"pass_tcp_no_flag"` - `"pass_tcp_fin_noack"` - `"drop_winnuke"` - `"drop_tcpland"` - `"drop_udpland"` - `"drop_icmpland"` - `"drop_ipland"` - `"drop_iprr"` - `"drop_ipssrr"` - `"drop_iplsrr"` - `"drop_ipstream"` - `"drop_ipsecurity"` - `"drop_iptimestamp"` - `"drop_ipunknown_option"` - `"drop_ipunknown_prot"` - `"drop_icmp_frag"` - `"drop_tcp_no_flag"` |
| **fp-disable**  list / elements=string | Fp-Disable.  **Choices:**   - `"all"` - `"ipsec"` - `"none"` |
| **gateway-address**  string | Gateway address |
| **generic-receive-offload**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **gi-gk**  string | Enable/disable Gi Gatekeeper.  **Choices:**   - `"disable"` - `"enable"` |
| **gwaddr**  string | Gateway address |
| **gwdetect**  string | Enable/disable detect gateway alive for first.  **Choices:**   - `"disable"` - `"enable"` |
| **ha-priority**  integer | HA election priority for the PING server. |
| **icmp-accept-redirect**  string | Enable/disable ICMP accept redirect.  **Choices:**   - `"disable"` - `"enable"` |
| **icmp-redirect**  string | Enable/disable ICMP redirect.  **Choices:**   - `"disable"` - `"enable"` |
| **icmp-send-redirect**  string | Enable/disable sending of ICMP redirects.  **Choices:**   - `"disable"` - `"enable"` |
| **ident-accept**  string | Enable/disable authentication for this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **idle-timeout**  integer | PPPoE auto disconnect after idle timeout seconds, 0 means no timeout. |
| **if-mdix**  string | Interface MDIX mode  **Choices:**   - `"auto"` - `"normal"` - `"crossover"` |
| **if-media**  string | Select interface media type  **Choices:**   - `"auto"` - `"copper"` - `"fiber"` |
| **ike-saml-server**  string | Configure IKE authentication SAML server. |
| **in-force-vlan-cos**  integer | In-Force-Vlan-Cos. |
| **inbandwidth**  integer | Bandwidth limit for incoming traffic |
| **ingress-cos**  string | Override incoming CoS in user VLAN tag on VLAN interface or assign a priority VLAN tag on physical interface.  **Choices:**   - `"disable"` - `"cos0"` - `"cos1"` - `"cos2"` - `"cos3"` - `"cos4"` - `"cos5"` - `"cos6"` - `"cos7"` |
| **ingress-shaping-profile**  string | Incoming traffic shaping profile. |
| **ingress-spillover-threshold**  integer | Ingress Spillover threshold |
| **interconnect-profile**  string | Set interconnect profile.  **Choices:**   - `"default"` - `"profile1"` - `"profile2"` |
| **internal**  integer | Implicitly created. |
| **ip**  string | Interface IPv4 address and subnet mask, syntax |
| **ip-managed-by-fortiipam**  string | Enable/disable automatic IP address assignment of this interface by FortiIPAM.  **Choices:**   - `"disable"` - `"enable"` - `"inherit-global"` |
| **ipmac**  string | Enable/disable IP/MAC binding.  **Choices:**   - `"disable"` - `"enable"` |
| **ips-sniffer-mode**  string | Enable/disable the use of this interface as a one-armed sniffer.  **Choices:**   - `"disable"` - `"enable"` |
| **ipunnumbered**  string | Unnumbered IP used for PPPoE interfaces for which no unique local address is provided. |
| **ipv6**  dictionary | no description |
| **autoconf**  string | Enable/disable address auto config.  **Choices:**   - `"disable"` - `"enable"` |
| **cli-conn6-status**  integer | Cli-Conn6-Status. |
| **dhcp6-client-options**  list / elements=string | Dhcp6-Client-Options.  **Choices:**   - `"rapid"` - `"iapd"` - `"iana"` - `"dns"` - `"dnsname"` |
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
| **ip6-allowaccess**  list / elements=string | Allow management access to the interface.  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"capwap"` - `"fabric"` |
| **ip6-default-life**  integer | Default life |
| **ip6-delegated-prefix-iaid**  integer | IAID of obtained delegated-prefix from the upstream interface. |
| **ip6-delegated-prefix-list**  list / elements=dictionary | Ip6-Delegated-Prefix-List. |
| **autonomous-flag**  string | Enable/disable the autonomous flag.  **Choices:**   - `"disable"` - `"enable"` |
| **delegated-prefix-iaid**  integer | IAID of obtained delegated-prefix from the upstream interface. |
| **onlink-flag**  string | Enable/disable the onlink flag.  **Choices:**   - `"disable"` - `"enable"` |
| **prefix-id**  integer | Prefix ID. |
| **rdnss**  any | (list) Recursive DNS server option. |
| **rdnss-service**  string | Recursive DNS service option.  **Choices:**   - `"delegated"` - `"default"` - `"specify"` |
| **subnet**  string | Add subnet ID to routing prefix. |
| **upstream-interface**  string | Name of the interface that provides delegated information. |
| **ip6-dns-server-override**  string | Enable/disable using the DNS server acquired by DHCP.  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-extra-addr**  list / elements=dictionary | Ip6-Extra-Addr. |
| **prefix**  string | IPv6 address prefix. |
| **ip6-hop-limit**  integer | Hop limit |
| **ip6-link-mtu**  integer | IPv6 link MTU. |
| **ip6-manage-flag**  string | Enable/disable the managed flag.  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-max-interval**  integer | IPv6 maximum interval |
| **ip6-min-interval**  integer | IPv6 minimum interval |
| **ip6-mode**  string | Addressing mode  **Choices:**   - `"static"` - `"dhcp"` - `"pppoe"` - `"delegated"` |
| **ip6-other-flag**  string | Enable/disable the other IPv6 flag.  **Choices:**   - `"disable"` - `"enable"` |
| **ip6-prefix-list**  list / elements=dictionary | Ip6-Prefix-List. |
| **autonomous-flag**  string | Enable/disable the autonomous flag.  **Choices:**   - `"disable"` - `"enable"` |
| **dnssl**  any | (list) DNS search list option. |
| **onlink-flag**  string | Enable/disable the onlink flag.  **Choices:**   - `"disable"` - `"enable"` |
| **preferred-life-time**  integer | Preferred life time |
| **prefix**  string | IPv6 prefix. |
| **rdnss**  any | (list) Recursive DNS server option. |
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
| **vrrp6**  list / elements=dictionary | Vrrp6. |
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
| **l2forward**  string | Enable/disable l2 forwarding.  **Choices:**   - `"disable"` - `"enable"` |
| **l2tp-client**  string | Enable/disable this interface as a Layer 2 Tunnelling Protocol  **Choices:**   - `"disable"` - `"enable"` |
| **lacp-ha-secondary**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **lacp-ha-slave**  string | LACP HA slave.  **Choices:**   - `"disable"` - `"enable"` |
| **lacp-mode**  string | LACP mode.  **Choices:**   - `"static"` - `"passive"` - `"active"` |
| **lacp-speed**  string | How often the interface sends LACP messages.  **Choices:**   - `"slow"` - `"fast"` |
| **large-receive-offload**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **lcp-echo-interval**  integer | Time in seconds between PPPoE Link Control Protocol |
| **lcp-max-echo-fails**  integer | Maximum missed LCP echo messages before disconnect. |
| **link-up-delay**  integer | Number of milliseconds to wait before considering a link is up. |
| **listen-forticlient-connection**  string | Listen-Forticlient-Connection.  **Choices:**   - `"disable"` - `"enable"` |
| **lldp-network-policy**  string | LLDP-MED network policy profile. |
| **lldp-reception**  string | Enable/disable Link Layer Discovery Protocol  **Choices:**   - `"disable"` - `"enable"` - `"vdom"` |
| **lldp-transmission**  string | Enable/disable Link Layer Discovery Protocol  **Choices:**   - `"enable"` - `"disable"` - `"vdom"` |
| **log**  string | Log.  **Choices:**   - `"disable"` - `"enable"` |
| **macaddr**  string | Change the interfaces MAC address. |
| **managed-subnetwork-size**  string | Number of IP addresses to be allocated by FortiIPAM and used by this FortiGate units DHCP server settings.  **Choices:**   - `"256"` - `"512"` - `"1024"` - `"2048"` - `"4096"` - `"8192"` - `"16384"` - `"32768"` - `"65536"` - `"32"` - `"64"` - `"128"` |
| **management-ip**  string | High Availability in-band management IP address of this interface. |
| **max-egress-burst-rate**  integer | Max egress burst rate |
| **max-egress-rate**  integer | Max egress rate |
| **measured-downstream-bandwidth**  integer | Measured downstream bandwidth |
| **measured-upstream-bandwidth**  integer | Measured upstream bandwidth |
| **mediatype**  string | Select SFP media interface type  **Choices:**   - `"serdes-sfp"` - `"sgmii-sfp"` - `"cfp2-sr10"` - `"cfp2-lr4"` - `"serdes-copper-sfp"` - `"sr"` - `"cr"` - `"lr"` - `"qsfp28-sr4"` - `"qsfp28-lr4"` - `"qsfp28-cr4"` - `"sr4"` - `"cr4"` - `"lr4"` - `"none"` - `"gmii"` - `"sgmii"` - `"sr2"` - `"lr2"` - `"cr2"` - `"sr8"` - `"lr8"` - `"cr8"` |
| **member**  any | (list or str) Physical interfaces that belong to the aggregate or redundant interface. |
| **min-links**  integer | Minimum number of aggregated ports that must be up. |
| **min-links-down**  string | Action to take when less than the configured minimum number of links are active.  **Choices:**   - `"operational"` - `"administrative"` |
| **mode**  string | Addressing mode  **Choices:**   - `"static"` - `"dhcp"` - `"pppoe"` - `"pppoa"` - `"ipoa"` - `"eoa"` |
| **monitor-bandwidth**  string | Enable monitoring bandwidth on this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **mtu**  integer | MTU value for this interface. |
| **mtu-override**  string | Enable to set a custom MTU for this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **mux-type**  string | Multiplexer type  **Choices:**   - `"llc-encaps"` - `"vc-encaps"` |
| **name**  string | Name. |
| **ndiscforward**  string | Enable/disable NDISC forwarding.  **Choices:**   - `"disable"` - `"enable"` |
| **netbios-forward**  string | Enable/disable NETBIOS forwarding.  **Choices:**   - `"disable"` - `"enable"` |
| **netflow-sampler**  string | Enable/disable NetFlow on this interface and set the data that NetFlow collects  **Choices:**   - `"disable"` - `"tx"` - `"rx"` - `"both"` |
| **np-qos-profile**  integer | NP QoS profile ID. |
| **npu-fastpath**  string | Npu-Fastpath.  **Choices:**   - `"disable"` - `"enable"` |
| **nst**  string | Nst.  **Choices:**   - `"disable"` - `"enable"` |
| **out-force-vlan-cos**  integer | Out-Force-Vlan-Cos. |
| **outbandwidth**  integer | Bandwidth limit for outgoing traffic |
| **padt-retry-timeout**  integer | PPPoE Active Discovery Terminate |
| **password**  any | (list) PPPoE accounts password. |
| **peer-interface**  any | (list or str) Peer-Interface. |
| **phy-mode**  string | DSL physical mode.  **Choices:**   - `"auto"` - `"adsl"` - `"vdsl"` - `"adsl-auto"` - `"vdsl2"` - `"adsl2+"` - `"adsl2"` - `"g.dmt"` - `"t1.413"` - `"g.lite"` |
| **ping-serv-status**  integer | Ping-Serv-Status. |
| **poe**  string | Enable/disable PoE status.  **Choices:**   - `"disable"` - `"enable"` |
| **polling-interval**  integer | sFlow polling interval |
| **pppoe-unnumbered-negotiate**  string | Enable/disable PPPoE unnumbered negotiation.  **Choices:**   - `"disable"` - `"enable"` |
| **pptp-auth-type**  string | PPTP authentication type.  **Choices:**   - `"auto"` - `"pap"` - `"chap"` - `"mschapv1"` - `"mschapv2"` |
| **pptp-client**  string | Enable/disable PPTP client.  **Choices:**   - `"disable"` - `"enable"` |
| **pptp-password**  any | (list) PPTP password. |
| **pptp-server-ip**  string | PPTP server IP address. |
| **pptp-timeout**  integer | Idle timer in minutes |
| **pptp-user**  string | PPTP user name. |
| **preserve-session-route**  string | Enable/disable preservation of session route when dirty.  **Choices:**   - `"disable"` - `"enable"` |
| **priority**  integer | Priority of learned routes. |
| **priority-override**  string | Enable/disable fail back to higher priority port once recovered.  **Choices:**   - `"disable"` - `"enable"` |
| **proxy-captive-portal**  string | Enable/disable proxy captive portal on this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **pvc-atm-qos**  string | SFP-DSL ADSL Fallback PVC ATM QoS.  **Choices:**   - `"cbr"` - `"rt-vbr"` - `"nrt-vbr"` |
| **pvc-chan**  integer | SFP-DSL ADSL Fallback PVC Channel. |
| **pvc-crc**  integer | SFP-DSL ADSL Fallback PVC CRC Option |
| **pvc-pcr**  integer | SFP-DSL ADSL Fallback PVC Packet Cell Rate in cells |
| **pvc-scr**  integer | SFP-DSL ADSL Fallback PVC Sustainable Cell Rate in cells |
| **pvc-vlan-id**  integer | SFP-DSL ADSL Fallback PVC VLAN ID. |
| **pvc-vlan-rx-id**  integer | SFP-DSL ADSL Fallback PVC VLANID RX. |
| **pvc-vlan-rx-op**  string | SFP-DSL ADSL Fallback PVC VLAN RX op.  **Choices:**   - `"pass-through"` - `"replace"` - `"remove"` |
| **pvc-vlan-tx-id**  integer | SFP-DSL ADSL Fallback PVC VLAN ID TX. |
| **pvc-vlan-tx-op**  string | SFP-DSL ADSL Fallback PVC VLAN TX op.  **Choices:**   - `"pass-through"` - `"replace"` - `"remove"` |
| **reachable-time**  integer | IPv4 reachable time in milliseconds |
| **redundant-interface**  string | Redundant-Interface. |
| **remote-ip**  string | Remote IP address of tunnel. |
| **replacemsg-override-group**  string | Replacement message override group. |
| **retransmission**  string | Enable/disable DSL retransmission.  **Choices:**   - `"disable"` - `"enable"` |
| **ring-rx**  integer | RX ring size. |
| **ring-tx**  integer | TX ring size. |
| **role**  string | Interface role.  **Choices:**   - `"lan"` - `"wan"` - `"dmz"` - `"undefined"` |
| **sample-direction**  string | Data that NetFlow collects  **Choices:**   - `"rx"` - `"tx"` - `"both"` |
| **sample-rate**  integer | sFlow sample rate |
| **scan-botnet-connections**  string | Enable monitoring or blocking connections to Botnet servers through this interface.  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **secondary-IP**  string | Enable/disable adding a secondary IP to this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **secondaryip**  list / elements=dictionary | Secondaryip. |
| **allowaccess**  list / elements=string | Management access settings for the secondary IP address.  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"auto-ipsec"` - `"radius-acct"` - `"probe-response"` - `"capwap"` - `"dnp"` - `"ftm"` - `"fabric"` - `"speed-test"` |
| **detectprotocol**  list / elements=string | Protocols used to detect the server.  **Choices:**   - `"ping"` - `"tcp-echo"` - `"udp-echo"` |
| **detectserver**  string | Gateways ping server for this IP. |
| **gwdetect**  string | Enable/disable detect gateway alive for first.  **Choices:**   - `"disable"` - `"enable"` |
| **ha-priority**  integer | HA election priority for the PING server. |
| **id**  integer | ID. |
| **ip**  string | Secondary IP address of the interface. |
| **ping-serv-status**  integer | Ping-Serv-Status. |
| **secip-relay-ip**  string | DHCP relay IP address. |
| **seq**  integer | Seq. |
| **security-8021x-dynamic-vlan-id**  integer | VLAN ID for virtual switch. |
| **security-8021x-master**  string |  |
| **security-8021x-mode**  string | **Choices:**   - `"default"` - `"dynamic-vlan"` - `"fallback"` - `"slave"` |
| **security-exempt-list**  string | Name of security-exempt-list. |
| **security-external-logout**  string | URL of external authentication logout server. |
| **security-external-web**  string | URL of external authentication web server. |
| **security-groups**  any | (list or str) User groups that can authenticate with the captive portal. |
| **security-mac-auth-bypass**  string | Enable/disable MAC authentication bypass.  **Choices:**   - `"disable"` - `"enable"` - `"mac-auth-only"` |
| **security-mode**  string | Turn on captive portal authentication for this interface.  **Choices:**   - `"none"` - `"captive-portal"` - `"802.1X"` |
| **security-redirect-url**  string | URL redirection after disclaimer/authentication. |
| **select-profile-30a-35b**  string | Select VDSL Profile 30a or 35b.  **Choices:**   - `"30A"` - `"35B"` |
| **service-name**  string | PPPoE service name. |
| **sflow-sampler**  string | Enable/disable sFlow on this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **sfp-dsl**  string | Enable/disable SFP DSL.  **Choices:**   - `"disable"` - `"enable"` |
| **sfp-dsl-adsl-fallback**  string | Enable/disable SFP DSL ADSL fallback.  **Choices:**   - `"disable"` - `"enable"` |
| **sfp-dsl-autodetect**  string | Enable/disable SFP DSL MAC address autodetect.  **Choices:**   - `"disable"` - `"enable"` |
| **sfp-dsl-mac**  string | SFP DSL MAC address. |
| **speed**  string | Interface speed.  **Choices:**   - `"auto"` - `"10full"` - `"10half"` - `"100full"` - `"100half"` - `"1000full"` - `"1000half"` - `"10000full"` - `"1000auto"` - `"10000auto"` - `"40000full"` - `"100Gfull"` - `"25000full"` - `"40000auto"` - `"25000auto"` - `"100Gauto"` - `"400Gfull"` - `"400Gauto"` - `"50000full"` - `"2500auto"` - `"5000auto"` - `"50000auto"` - `"200Gfull"` - `"200Gauto"` - `"100auto"` |
| **spillover-threshold**  integer | Egress Spillover threshold |
| **src-check**  string | Enable/disable source IP check.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Bring the interface up or shut the interface down.  **Choices:**   - `"down"` - `"up"` |
| **stp**  string | Enable/disable STP.  **Choices:**   - `"disable"` - `"enable"` |
| **stp-ha-secondary**  string | Control STP behaviour on HA secondary.  **Choices:**   - `"disable"` - `"enable"` - `"priority-adjust"` |
| **stp-ha-slave**  string | Control STP behaviour on HA slave.  **Choices:**   - `"disable"` - `"enable"` - `"priority-adjust"` |
| **stpforward**  string | Enable/disable STP forwarding.  **Choices:**   - `"disable"` - `"enable"` |
| **stpforward-mode**  string | Configure STP forwarding mode.  **Choices:**   - `"rpl-all-ext-id"` - `"rpl-bridge-ext-id"` - `"rpl-nothing"` |
| **strip-priority-vlan-tag**  string | Strip-Priority-Vlan-Tag.  **Choices:**   - `"disable"` - `"enable"` |
| **subst**  string | Enable to always send packets from this interface to a destination MAC address.  **Choices:**   - `"disable"` - `"enable"` |
| **substitute-dst-mac**  string | Destination MAC address that all packets are sent to from this interface. |
| **sw-algorithm**  string | Frame distribution algorithm for switch.  **Choices:**   - `"l2"` - `"l3"` - `"eh"` |
| **swc-first-create**  integer | Initial create for switch-controller VLANs. |
| **swc-vlan**  integer | Swc-Vlan. |
| **switch**  string | Switch. |
| **switch-controller-access-vlan**  string | Block FortiSwitch port-to-port traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-arp-inspection**  string | Enable/disable FortiSwitch ARP inspection.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-auth**  string | Switch controller authentication.  **Choices:**   - `"radius"` - `"usergroup"` |
| **switch-controller-dhcp-snooping**  string | Switch controller DHCP snooping.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-dhcp-snooping-option82**  string | Switch controller DHCP snooping option82.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-dhcp-snooping-verify-mac**  string | Switch controller DHCP snooping verify MAC.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-dynamic**  string | Integrated FortiLink settings for managed FortiSwitch. |
| **switch-controller-feature**  string | Interfaces purpose when assigning traffic  **Choices:**   - `"none"` - `"default-vlan"` - `"quarantine"` - `"sniffer"` - `"voice"` - `"camera"` - `"rspan"` - `"video"` - `"nac"` - `"nac-segment"` |
| **switch-controller-igmp-snooping**  string | Switch controller IGMP snooping.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-igmp-snooping-fast-leave**  string | Switch controller IGMP snooping fast-leave.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-igmp-snooping-proxy**  string | Switch controller IGMP snooping proxy.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-iot-scanning**  string | Enable/disable managed FortiSwitch IoT scanning.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-learning-limit**  integer | Limit the number of dynamic MAC addresses on this VLAN |
| **switch-controller-mgmt-vlan**  integer | VLAN to use for FortiLink management purposes. |
| **switch-controller-nac**  string | Integrated NAC settings for managed FortiSwitch. |
| **switch-controller-netflow-collect**  string | NetFlow collection and processing.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-offload**  string | Enable/disable managed FortiSwitch routing offload.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-offload-gw**  string | Enable/disable managed FortiSwitch routing offload gateway.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-offload-ip**  string | IP for routing offload on FortiSwitch. |
| **switch-controller-offloading**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-offloading-gw**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-offloading-ip**  string | no description |
| **switch-controller-radius-server**  string | RADIUS server name for this FortiSwitch VLAN. |
| **switch-controller-rspan-mode**  string | Stop Layer2 MAC learning and interception of BPDUs and other packets on this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-source-ip**  string | Source IP address used in FortiLink over L3 connections.  **Choices:**   - `"outbound"` - `"fixed"` |
| **switch-controller-traffic-policy**  string | Switch controller traffic policy for the VLAN. |
| **system-id**  string | Define a system ID for the aggregate interface. |
| **system-id-type**  string | Method in which system ID is generated.  **Choices:**   - `"auto"` - `"user"` |
| **tc-mode**  string | DSL transfer mode.  **Choices:**   - `"ptm"` - `"atm"` |
| **tcp-mss**  integer | TCP maximum segment size. |
| **trunk**  string | Enable/disable VLAN trunk.  **Choices:**   - `"disable"` - `"enable"` |
| **trust-ip-1**  string | Trusted host for dedicated management traffic |
| **trust-ip-2**  string | Trusted host for dedicated management traffic |
| **trust-ip-3**  string | Trusted host for dedicated management traffic |
| **trust-ip6-1**  string | Trusted IPv6 host for dedicated management traffic |
| **trust-ip6-2**  string | Trusted IPv6 host for dedicated management traffic |
| **trust-ip6-3**  string | Trusted IPv6 host for dedicated management traffic |
| **type**  string | Interface type.  **Choices:**   - `"physical"` - `"vlan"` - `"aggregate"` - `"redundant"` - `"tunnel"` - `"wireless"` - `"vdom-link"` - `"loopback"` - `"switch"` - `"hard-switch"` - `"hdlc"` - `"vap-switch"` - `"wl-mesh"` - `"fortilink"` - `"switch-vlan"` - `"fctrl-trunk"` - `"tdm"` - `"fext-wan"` - `"vxlan"` - `"emac-vlan"` - `"geneve"` - `"ssl"` - `"lan-extension"` |
| **username**  string | Username of the PPPoE account, provided by your ISP. |
| **vci**  integer | Virtual Channel ID |
| **vectoring**  string | Enable/disable DSL vectoring.  **Choices:**   - `"disable"` - `"enable"` |
| **vindex**  integer | Vindex. |
| **vlan-id**  integer | Vlan ID |
| **vlan-op-mode**  string | Configure DSL 802.  **Choices:**   - `"tag"` - `"untag"` - `"passthrough"` |
| **vlan-protocol**  string | Ethernet protocol of VLAN.  **Choices:**   - `"8021q"` - `"8021ad"` |
| **vlanforward**  string | Enable/disable traffic forwarding between VLANs on this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **vlanid**  integer | VLAN ID |
| **vpi**  integer | Virtual Path ID |
| **vrf**  integer | Virtual Routing Forwarding ID. |
| **vrrp**  list / elements=dictionary | Vrrp. |
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
| **vrdst**  any | (list) Monitor the route to this destination. |
| **vrdst-priority**  integer | Priority of the virtual router when the virtual router destination becomes unreachable |
| **vrgrp**  integer | VRRP group ID |
| **vrid**  integer | Virtual router identifier |
| **vrip**  string | IP address of the virtual router. |
| **vrrp-virtual-mac**  string | Enable/disable use of virtual MAC for VRRP.  **Choices:**   - `"disable"` - `"enable"` |
| **wccp**  string | Enable/disable WCCP on this interface.  **Choices:**   - `"disable"` - `"enable"` |
| **weight**  integer | Default weight for static routes |
| **wifi-5g-threshold**  string | Minimal signal strength to be considered as a good 5G AP. |
| **wifi-acl**  string | Access control for MAC addresses in the MAC list.  **Choices:**   - `"deny"` - `"allow"` |
| **wifi-ap-band**  string | How to select the AP to connect.  **Choices:**   - `"any"` - `"5g-preferred"` - `"5g-only"` |
| **wifi-auth**  string | WiFi authentication.  **Choices:**   - `"PSK"` - `"RADIUS"` - `"radius"` - `"usergroup"` |
| **wifi-auto-connect**  string | Enable/disable WiFi network auto connect.  **Choices:**   - `"disable"` - `"enable"` |
| **wifi-auto-save**  string | Enable/disable WiFi network automatic save.  **Choices:**   - `"disable"` - `"enable"` |
| **wifi-broadcast-ssid**  string | Enable/disable SSID broadcast in the beacon.  **Choices:**   - `"disable"` - `"enable"` |
| **wifi-dns-server1**  string | DNS server 1. |
| **wifi-dns-server2**  string | DNS server 2. |
| **wifi-encrypt**  string | Data encryption.  **Choices:**   - `"TKIP"` - `"AES"` |
| **wifi-fragment-threshold**  integer | WiFi fragment threshold |
| **wifi-gateway**  string | IPv4 default gateway IP address. |
| **wifi-key**  any | (list) WiFi WEP Key. |
| **wifi-keyindex**  integer | WEP key index |
| **wifi-mac-filter**  string | Enable/disable MAC filter status.  **Choices:**   - `"disable"` - `"enable"` |
| **wifi-passphrase**  any | (list) WiFi pre-shared key for WPA. |
| **wifi-radius-server**  string | WiFi RADIUS server for WPA. |
| **wifi-rts-threshold**  integer | WiFi RTS threshold |
| **wifi-security**  string | Wireless access security of SSID.  **Choices:**   - `"None"` - `"WEP64"` - `"wep64"` - `"WEP128"` - `"wep128"` - `"WPA_PSK"` - `"WPA_RADIUS"` - `"WPA"` - `"WPA2"` - `"WPA2_AUTO"` - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` - `"wpa-only-personal"` - `"wpa-only-enterprise"` - `"wpa2-only-personal"` - `"wpa2-only-enterprise"` |
| **wifi-ssid**  string | IEEE 802. |
| **wifi-usergroup**  string | WiFi user group for WPA. |
| **wins-ip**  string | WINS server IP. |
| **name**  string / required | Name. |
| **portal-message-override-group**  string | no description |
| **radius-server**  string | no description |
| **security**  string | no description  **Choices:**   - `"open"` - `"captive-portal"` - `"8021x"` |
| **selected-usergroups**  string | no description |
| **usergroup**  string | no description |
| **vdom**  string | Vdom. |
| **vlanid**  integer | Vlanid. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_fsp_vlan_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_fsp_vlan_module.md#id4)

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
      fmgr_fsp_vlan:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        fsp_vlan:
          _dhcp-status: <value in [disable, enable]>
          auth: <value in [radius, usergroup]>
          color: <integer>
          comments: <string>
          dynamic_mapping:
            -
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
          name: <string>
          portal-message-override-group: <string>
          radius-server: <string>
          security: <value in [open, captive-portal, 8021x]>
          selected-usergroups: <string>
          usergroup: <string>
          vdom: <string>
          vlanid: <integer>
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
            ac-name: <string>
            aggregate: <string>
            algorithm: <value in [L2, L3, L4, ...]>
            alias: <string>
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
            ap-discover: <value in [disable, enable]>
            arpforward: <value in [disable, enable]>
            atm-protocol: <value in [none, ipoa]>
            auth-type: <value in [auto, pap, chap, ...]>
            auto-auth-extension-device: <value in [disable, enable]>
            bandwidth-measure-time: <integer>
            bfd: <value in [global, enable, disable]>
            bfd-desired-min-tx: <integer>
            bfd-detect-mult: <integer>
            bfd-required-min-rx: <integer>
            broadcast-forticlient-discovery: <value in [disable, enable]>
            broadcast-forward: <value in [disable, enable]>
            captive-portal: <integer>
            cli-conn-status: <integer>
            color: <integer>
            ddns: <value in [disable, enable]>
            ddns-auth: <value in [disable, tsig]>
            ddns-domain: <string>
            ddns-key: <list or string>
            ddns-keyname: <string>
            ddns-password: <list or string>
            ddns-server: <value in [dhs.org, dyndns.org, dyns.net, ...]>
            ddns-server-ip: <string>
            ddns-sn: <string>
            ddns-ttl: <integer>
            ddns-username: <string>
            ddns-zone: <string>
            dedicated-to: <value in [none, management]>
            defaultgw: <value in [disable, enable]>
            description: <string>
            detected-peer-mtu: <integer>
            detectprotocol:
              - ping
              - tcp-echo
              - udp-echo
            detectserver: <string>
            device-access-list: <list or string>
            device-identification: <value in [disable, enable]>
            device-identification-active-scan: <value in [disable, enable]>
            device-netscan: <value in [disable, enable]>
            device-user-identification: <value in [disable, enable]>
            devindex: <integer>
            dhcp-client-identifier: <string>
            dhcp-relay-agent-option: <value in [disable, enable]>
            dhcp-relay-interface: <string>
            dhcp-relay-interface-select-method: <value in [auto, sdwan, specify]>
            dhcp-relay-ip: <list or string>
            dhcp-relay-service: <value in [disable, enable]>
            dhcp-relay-type: <value in [regular, ipsec]>
            dhcp-renew-time: <integer>
            disc-retry-timeout: <integer>
            disconnect-threshold: <integer>
            distance: <integer>
            dns-query: <value in [disable, recursive, non-recursive]>
            dns-server-override: <value in [disable, enable]>
            drop-fragment: <value in [disable, enable]>
            drop-overlapped-fragment: <value in [disable, enable]>
            egress-cos: <value in [disable, cos0, cos1, ...]>
            egress-shaping-profile: <string>
            eip: <string>
            endpoint-compliance: <value in [disable, enable]>
            estimated-downstream-bandwidth: <integer>
            estimated-upstream-bandwidth: <integer>
            explicit-ftp-proxy: <value in [disable, enable]>
            explicit-web-proxy: <value in [disable, enable]>
            external: <value in [disable, enable]>
            fail-action-on-extender: <value in [soft-restart, hard-restart, reboot]>
            fail-alert-interfaces: <list or string>
            fail-alert-method: <value in [link-failed-signal, link-down]>
            fail-detect: <value in [disable, enable]>
            fail-detect-option:
              - detectserver
              - link-down
            fdp: <value in [disable, enable]>
            fortiheartbeat: <value in [disable, enable]>
            fortilink: <value in [disable, enable]>
            fortilink-backup-link: <integer>
            fortilink-neighbor-detect: <value in [lldp, fortilink]>
            fortilink-split-interface: <value in [disable, enable]>
            fortilink-stacking: <value in [disable, enable]>
            forward-domain: <integer>
            forward-error-correction: <value in [disable, enable, rs-fec, ...]>
            fp-anomaly:
              - drop_tcp_fin_noack
              - pass_winnuke
              - pass_tcpland
              - pass_udpland
              - pass_icmpland
              - pass_ipland
              - pass_iprr
              - pass_ipssrr
              - pass_iplsrr
              - pass_ipstream
              - pass_ipsecurity
              - pass_iptimestamp
              - pass_ipunknown_option
              - pass_ipunknown_prot
              - pass_icmp_frag
              - pass_tcp_no_flag
              - pass_tcp_fin_noack
              - drop_winnuke
              - drop_tcpland
              - drop_udpland
              - drop_icmpland
              - drop_ipland
              - drop_iprr
              - drop_ipssrr
              - drop_iplsrr
              - drop_ipstream
              - drop_ipsecurity
              - drop_iptimestamp
              - drop_ipunknown_option
              - drop_ipunknown_prot
              - drop_icmp_frag
              - drop_tcp_no_flag
            fp-disable:
              - all
              - ipsec
              - none
            gateway-address: <string>
            gi-gk: <value in [disable, enable]>
            gwaddr: <string>
            gwdetect: <value in [disable, enable]>
            ha-priority: <integer>
            icmp-accept-redirect: <value in [disable, enable]>
            icmp-redirect: <value in [disable, enable]>
            icmp-send-redirect: <value in [disable, enable]>
            ident-accept: <value in [disable, enable]>
            idle-timeout: <integer>
            if-mdix: <value in [auto, normal, crossover]>
            if-media: <value in [auto, copper, fiber]>
            in-force-vlan-cos: <integer>
            inbandwidth: <integer>
            ingress-cos: <value in [disable, cos0, cos1, ...]>
            ingress-shaping-profile: <string>
            ingress-spillover-threshold: <integer>
            internal: <integer>
            ip: <string>
            ip-managed-by-fortiipam: <value in [disable, enable, inherit-global]>
            ipmac: <value in [disable, enable]>
            ips-sniffer-mode: <value in [disable, enable]>
            ipunnumbered: <string>
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
            l2forward: <value in [disable, enable]>
            l2tp-client: <value in [disable, enable]>
            lacp-ha-slave: <value in [disable, enable]>
            lacp-mode: <value in [static, passive, active]>
            lacp-speed: <value in [slow, fast]>
            lcp-echo-interval: <integer>
            lcp-max-echo-fails: <integer>
            link-up-delay: <integer>
            listen-forticlient-connection: <value in [disable, enable]>
            lldp-network-policy: <string>
            lldp-reception: <value in [disable, enable, vdom]>
            lldp-transmission: <value in [enable, disable, vdom]>
            log: <value in [disable, enable]>
            macaddr: <string>
            managed-subnetwork-size: <value in [256, 512, 1024, ...]>
            management-ip: <string>
            max-egress-burst-rate: <integer>
            max-egress-rate: <integer>
            measured-downstream-bandwidth: <integer>
            measured-upstream-bandwidth: <integer>
            mediatype: <value in [serdes-sfp, sgmii-sfp, cfp2-sr10, ...]>
            member: <list or string>
            min-links: <integer>
            min-links-down: <value in [operational, administrative]>
            mode: <value in [static, dhcp, pppoe, ...]>
            monitor-bandwidth: <value in [disable, enable]>
            mtu: <integer>
            mtu-override: <value in [disable, enable]>
            mux-type: <value in [llc-encaps, vc-encaps]>
            name: <string>
            ndiscforward: <value in [disable, enable]>
            netbios-forward: <value in [disable, enable]>
            netflow-sampler: <value in [disable, tx, rx, ...]>
            np-qos-profile: <integer>
            npu-fastpath: <value in [disable, enable]>
            nst: <value in [disable, enable]>
            out-force-vlan-cos: <integer>
            outbandwidth: <integer>
            padt-retry-timeout: <integer>
            password: <list or string>
            peer-interface: <list or string>
            phy-mode: <value in [auto, adsl, vdsl, ...]>
            ping-serv-status: <integer>
            poe: <value in [disable, enable]>
            polling-interval: <integer>
            pppoe-unnumbered-negotiate: <value in [disable, enable]>
            pptp-auth-type: <value in [auto, pap, chap, ...]>
            pptp-client: <value in [disable, enable]>
            pptp-password: <list or string>
            pptp-server-ip: <string>
            pptp-timeout: <integer>
            pptp-user: <string>
            preserve-session-route: <value in [disable, enable]>
            priority: <integer>
            priority-override: <value in [disable, enable]>
            proxy-captive-portal: <value in [disable, enable]>
            redundant-interface: <string>
            remote-ip: <string>
            replacemsg-override-group: <string>
            retransmission: <value in [disable, enable]>
            ring-rx: <integer>
            ring-tx: <integer>
            role: <value in [lan, wan, dmz, ...]>
            sample-direction: <value in [rx, tx, both]>
            sample-rate: <integer>
            scan-botnet-connections: <value in [disable, block, monitor]>
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
            security-8021x-dynamic-vlan-id: <integer>
            security-8021x-master: <string>
            security-8021x-mode: <value in [default, dynamic-vlan, fallback, ...]>
            security-exempt-list: <string>
            security-external-logout: <string>
            security-external-web: <string>
            security-groups: <list or string>
            security-mac-auth-bypass: <value in [disable, enable, mac-auth-only]>
            security-mode: <value in [none, captive-portal, 802.1X]>
            security-redirect-url: <string>
            service-name: <string>
            sflow-sampler: <value in [disable, enable]>
            speed: <value in [auto, 10full, 10half, ...]>
            spillover-threshold: <integer>
            src-check: <value in [disable, enable]>
            status: <value in [down, up]>
            stp: <value in [disable, enable]>
            stp-ha-slave: <value in [disable, enable, priority-adjust]>
            stpforward: <value in [disable, enable]>
            stpforward-mode: <value in [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]>
            strip-priority-vlan-tag: <value in [disable, enable]>
            subst: <value in [disable, enable]>
            substitute-dst-mac: <string>
            swc-first-create: <integer>
            swc-vlan: <integer>
            switch: <string>
            switch-controller-access-vlan: <value in [disable, enable]>
            switch-controller-arp-inspection: <value in [disable, enable]>
            switch-controller-auth: <value in [radius, usergroup]>
            switch-controller-dhcp-snooping: <value in [disable, enable]>
            switch-controller-dhcp-snooping-option82: <value in [disable, enable]>
            switch-controller-dhcp-snooping-verify-mac: <value in [disable, enable]>
            switch-controller-feature: <value in [none, default-vlan, quarantine, ...]>
            switch-controller-igmp-snooping: <value in [disable, enable]>
            switch-controller-igmp-snooping-fast-leave: <value in [disable, enable]>
            switch-controller-igmp-snooping-proxy: <value in [disable, enable]>
            switch-controller-iot-scanning: <value in [disable, enable]>
            switch-controller-learning-limit: <integer>
            switch-controller-mgmt-vlan: <integer>
            switch-controller-nac: <string>
            switch-controller-radius-server: <string>
            switch-controller-rspan-mode: <value in [disable, enable]>
            switch-controller-source-ip: <value in [outbound, fixed]>
            switch-controller-traffic-policy: <string>
            tc-mode: <value in [ptm, atm]>
            tcp-mss: <integer>
            trunk: <value in [disable, enable]>
            trust-ip-1: <string>
            trust-ip-2: <string>
            trust-ip-3: <string>
            trust-ip6-1: <string>
            trust-ip6-2: <string>
            trust-ip6-3: <string>
            type: <value in [physical, vlan, aggregate, ...]>
            username: <string>
            vci: <integer>
            vectoring: <value in [disable, enable]>
            vindex: <integer>
            vlan-protocol: <value in [8021q, 8021ad]>
            vlanforward: <value in [disable, enable]>
            vlanid: <integer>
            vpi: <integer>
            vrf: <integer>
            vrrp:
              -
                accept-mode: <value in [disable, enable]>
                adv-interval: <integer>
                ignore-default-route: <value in [disable, enable]>
                preempt: <value in [disable, enable]>
                priority: <integer>
                start-time: <integer>
                status: <value in [disable, enable]>
                version: <value in [2, 3]>
                vrdst: <list or string>
                vrdst-priority: <integer>
                vrgrp: <integer>
                vrid: <integer>
                vrip: <string>
                proxy-arp:
                  -
                    id: <integer>
                    ip: <string>
            vrrp-virtual-mac: <value in [disable, enable]>
            wccp: <value in [disable, enable]>
            weight: <integer>
            wifi-5g-threshold: <string>
            wifi-acl: <value in [deny, allow]>
            wifi-ap-band: <value in [any, 5g-preferred, 5g-only]>
            wifi-auth: <value in [PSK, RADIUS, radius, ...]>
            wifi-auto-connect: <value in [disable, enable]>
            wifi-auto-save: <value in [disable, enable]>
            wifi-broadcast-ssid: <value in [disable, enable]>
            wifi-encrypt: <value in [TKIP, AES]>
            wifi-fragment-threshold: <integer>
            wifi-key: <list or string>
            wifi-keyindex: <integer>
            wifi-mac-filter: <value in [disable, enable]>
            wifi-passphrase: <list or string>
            wifi-radius-server: <string>
            wifi-rts-threshold: <integer>
            wifi-security: <value in [None, WEP64, wep64, ...]>
            wifi-ssid: <string>
            wifi-usergroup: <string>
            wins-ip: <string>
            dhcp-relay-request-all-server: <value in [disable, enable]>
            stp-ha-secondary: <value in [disable, enable, priority-adjust]>
            switch-controller-dynamic: <string>
            auth-cert: <string>
            auth-portal-addr: <string>
            dhcp-classless-route-addition: <value in [disable, enable]>
            dhcp-relay-link-selection: <string>
            dns-server-protocol:
              - cleartext
              - dot
              - doh
            eap-ca-cert: <string>
            eap-identity: <string>
            eap-method: <value in [tls, peap]>
            eap-password: <list or string>
            eap-supplicant: <value in [disable, enable]>
            eap-user-cert: <string>
            ike-saml-server: <string>
            lacp-ha-secondary: <value in [disable, enable]>
            pvc-atm-qos: <value in [cbr, rt-vbr, nrt-vbr]>
            pvc-chan: <integer>
            pvc-crc: <integer>
            pvc-pcr: <integer>
            pvc-scr: <integer>
            pvc-vlan-id: <integer>
            pvc-vlan-rx-id: <integer>
            pvc-vlan-rx-op: <value in [pass-through, replace, remove]>
            pvc-vlan-tx-id: <integer>
            pvc-vlan-tx-op: <value in [pass-through, replace, remove]>
            reachable-time: <integer>
            select-profile-30a-35b: <value in [30A, 35B]>
            sfp-dsl: <value in [disable, enable]>
            sfp-dsl-adsl-fallback: <value in [disable, enable]>
            sfp-dsl-autodetect: <value in [disable, enable]>
            sfp-dsl-mac: <string>
            sw-algorithm: <value in [l2, l3, eh]>
            system-id: <string>
            system-id-type: <value in [auto, user]>
            vlan-id: <integer>
            vlan-op-mode: <value in [tag, untag, passthrough]>
            generic-receive-offload: <value in [disable, enable]>
            interconnect-profile: <value in [default, profile1, profile2]>
            large-receive-offload: <value in [disable, enable]>
            aggregate-type: <value in [physical, vxlan]>
            switch-controller-netflow-collect: <value in [disable, enable]>
            wifi-dns-server1: <string>
            wifi-dns-server2: <string>
            wifi-gateway: <string>
            default-purdue-level: <value in [1, 2, 3, ...]>
            dhcp-broadcast-flag: <value in [disable, enable]>
            dhcp-smart-relay: <value in [disable, enable]>
            switch-controller-offloading: <value in [disable, enable]>
            switch-controller-offloading-gw: <value in [disable, enable]>
            switch-controller-offloading-ip: <string>
            dhcp-relay-circuit-id: <string>
            dhcp-relay-source-ip: <string>
            switch-controller-offload: <value in [disable, enable]>
            switch-controller-offload-gw: <value in [disable, enable]>
            switch-controller-offload-ip: <string>
```

## [Return Values](fmgr_fsp_vlan_module.md#id5)

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
