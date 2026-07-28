---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_fsp_vlan_interface module – Configure interfaces."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_fsp_vlan_interface_module.html
fetched_at: 2026-07-28T02:14:08+00:00
---
# fortinet.fortimanager.fmgr_fsp_vlan_interface module – Configure interfaces.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fsp_vlan_interface`.

New in fortinet.fortimanager 2.0.0

- [Synopsis](fmgr_fsp_vlan_interface_module.md#synopsis)
- [Parameters](fmgr_fsp_vlan_interface_module.md#parameters)
- [Notes](fmgr_fsp_vlan_interface_module.md#notes)
- [Examples](fmgr_fsp_vlan_interface_module.md#examples)
- [Return Values](fmgr_fsp_vlan_interface_module.md#return-values)

## [Synopsis](fmgr_fsp_vlan_interface_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_fsp_vlan_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **fsp_vlan_interface**  dictionary | the top level parameters set |
| **ac-name**  string | no description |
| **aggregate**  string | no description |
| **aggregate-type**  string | Type of aggregation.  **Choices:**   - `"physical"` - `"vxlan"` |
| **algorithm**  string | no description  **Choices:**   - `"L2"` - `"L3"` - `"L4"` - `"LB"` - `"Source-MAC"` |
| **alias**  string | no description |
| **allowaccess**  list / elements=string | no description  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"auto-ipsec"` - `"radius-acct"` - `"probe-response"` - `"capwap"` - `"dnp"` - `"ftm"` - `"fabric"` - `"speed-test"` |
| **ap-discover**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **arpforward**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **atm-protocol**  string | no description  **Choices:**   - `"none"` - `"ipoa"` |
| **auth-cert**  string | HTTPS server certificate. |
| **auth-portal-addr**  string | Address of captive portal. |
| **auth-type**  string | no description  **Choices:**   - `"auto"` - `"pap"` - `"chap"` - `"mschapv1"` - `"mschapv2"` |
| **auto-auth-extension-device**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **bandwidth-measure-time**  integer | no description |
| **bfd**  string | no description  **Choices:**   - `"global"` - `"enable"` - `"disable"` |
| **bfd-desired-min-tx**  integer | no description |
| **bfd-detect-mult**  integer | no description |
| **bfd-required-min-rx**  integer | no description |
| **broadcast-forticlient-discovery**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **broadcast-forward**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **captive-portal**  integer | no description |
| **cli-conn-status**  integer | no description |
| **color**  integer | no description |
| **ddns**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ddns-auth**  string | no description  **Choices:**   - `"disable"` - `"tsig"` |
| **ddns-domain**  string | no description |
| **ddns-key**  any | (list or str) no description |
| **ddns-keyname**  string | no description |
| **ddns-password**  any | (list) no description |
| **ddns-server**  string | no description  **Choices:**   - `"dhs.org"` - `"dyndns.org"` - `"dyns.net"` - `"tzo.com"` - `"ods.org"` - `"vavic.com"` - `"now.net.cn"` - `"dipdns.net"` - `"easydns.com"` - `"genericDDNS"` |
| **ddns-server-ip**  string | no description |
| **ddns-sn**  string | no description |
| **ddns-ttl**  integer | no description |
| **ddns-username**  string | no description |
| **ddns-zone**  string | no description |
| **dedicated-to**  string | no description  **Choices:**   - `"none"` - `"management"` |
| **default-purdue-level**  string | default purdue level of device detected on this interface.  **Choices:**   - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` - `"1.5"` - `"2.5"` - `"3.5"` - `"5.5"` |
| **defaultgw**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **description**  string | no description |
| **detected-peer-mtu**  integer | no description |
| **detectprotocol**  list / elements=string | no description  **Choices:**   - `"ping"` - `"tcp-echo"` - `"udp-echo"` |
| **detectserver**  string | no description |
| **device-access-list**  any | (list or str) no description |
| **device-identification**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **device-identification-active-scan**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **device-netscan**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **device-user-identification**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **devindex**  integer | no description |
| **dhcp-broadcast-flag**  string | Enable/disable setting of the broadcast flag in messages sent by the DHCP client  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-classless-route-addition**  string | Enable/disable addition of classless static routes retrieved from DHCP server.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-client-identifier**  string | no description |
| **dhcp-relay-agent-option**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-relay-circuit-id**  string | DHCP relay circuit ID. |
| **dhcp-relay-interface**  string | no description |
| **dhcp-relay-interface-select-method**  string | no description  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **dhcp-relay-ip**  any | (list) no description |
| **dhcp-relay-link-selection**  string | DHCP relay link selection. |
| **dhcp-relay-request-all-server**  string | Enable/disable sending of DHCP requests to all servers.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-relay-service**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp-relay-source-ip**  string | IP address used by the DHCP relay as its source IP. |
| **dhcp-relay-type**  string | no description  **Choices:**   - `"regular"` - `"ipsec"` |
| **dhcp-renew-time**  integer | no description |
| **dhcp-smart-relay**  string | Enable/disable DHCP smart relay.  **Choices:**   - `"disable"` - `"enable"` |
| **disc-retry-timeout**  integer | no description |
| **disconnect-threshold**  integer | no description |
| **distance**  integer | no description |
| **dns-query**  string | no description  **Choices:**   - `"disable"` - `"recursive"` - `"non-recursive"` |
| **dns-server-override**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dns-server-protocol**  list / elements=string | no description  **Choices:**   - `"cleartext"` - `"dot"` - `"doh"` |
| **drop-fragment**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **drop-overlapped-fragment**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **eap-ca-cert**  string | EAP CA certificate name. |
| **eap-identity**  string | EAP identity. |
| **eap-method**  string | EAP method.  **Choices:**   - `"tls"` - `"peap"` |
| **eap-password**  any | (list) no description |
| **eap-supplicant**  string | Enable/disable EAP-Supplicant.  **Choices:**   - `"disable"` - `"enable"` |
| **eap-user-cert**  string | EAP user certificate name. |
| **egress-cos**  string | no description  **Choices:**   - `"disable"` - `"cos0"` - `"cos1"` - `"cos2"` - `"cos3"` - `"cos4"` - `"cos5"` - `"cos6"` - `"cos7"` |
| **egress-shaping-profile**  string | no description |
| **eip**  string | no description |
| **endpoint-compliance**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **estimated-downstream-bandwidth**  integer | no description |
| **estimated-upstream-bandwidth**  integer | no description |
| **explicit-ftp-proxy**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **explicit-web-proxy**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **external**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **fail-action-on-extender**  string | no description  **Choices:**   - `"soft-restart"` - `"hard-restart"` - `"reboot"` |
| **fail-alert-interfaces**  any | (list or str) no description |
| **fail-alert-method**  string | no description  **Choices:**   - `"link-failed-signal"` - `"link-down"` |
| **fail-detect**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **fail-detect-option**  list / elements=string | no description  **Choices:**   - `"detectserver"` - `"link-down"` |
| **fdp**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **fortiheartbeat**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **fortilink**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **fortilink-backup-link**  integer | no description |
| **fortilink-neighbor-detect**  string | no description  **Choices:**   - `"lldp"` - `"fortilink"` |
| **fortilink-split-interface**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **fortilink-stacking**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **forward-domain**  integer | no description |
| **forward-error-correction**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"rs-fec"` - `"base-r-fec"` - `"fec-cl91"` - `"fec-cl74"` - `"rs-544"` - `"none"` - `"cl91-rs-fec"` - `"cl74-fc-fec"` - `"auto"` |
| **fp-anomaly**  list / elements=string | no description  **Choices:**   - `"drop_tcp_fin_noack"` - `"pass_winnuke"` - `"pass_tcpland"` - `"pass_udpland"` - `"pass_icmpland"` - `"pass_ipland"` - `"pass_iprr"` - `"pass_ipssrr"` - `"pass_iplsrr"` - `"pass_ipstream"` - `"pass_ipsecurity"` - `"pass_iptimestamp"` - `"pass_ipunknown_option"` - `"pass_ipunknown_prot"` - `"pass_icmp_frag"` - `"pass_tcp_no_flag"` - `"pass_tcp_fin_noack"` - `"drop_winnuke"` - `"drop_tcpland"` - `"drop_udpland"` - `"drop_icmpland"` - `"drop_ipland"` - `"drop_iprr"` - `"drop_ipssrr"` - `"drop_iplsrr"` - `"drop_ipstream"` - `"drop_ipsecurity"` - `"drop_iptimestamp"` - `"drop_ipunknown_option"` - `"drop_ipunknown_prot"` - `"drop_icmp_frag"` - `"drop_tcp_no_flag"` |
| **fp-disable**  list / elements=string | no description  **Choices:**   - `"all"` - `"ipsec"` - `"none"` |
| **gateway-address**  string | no description |
| **generic-receive-offload**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **gi-gk**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **gwaddr**  string | no description |
| **gwdetect**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ha-priority**  integer | no description |
| **icmp-accept-redirect**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **icmp-redirect**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **icmp-send-redirect**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ident-accept**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **idle-timeout**  integer | no description |
| **if-mdix**  string | no description  **Choices:**   - `"auto"` - `"normal"` - `"crossover"` |
| **if-media**  string | no description  **Choices:**   - `"auto"` - `"copper"` - `"fiber"` |
| **ike-saml-server**  string | Configure IKE authentication SAML server. |
| **in-force-vlan-cos**  integer | no description |
| **inbandwidth**  integer | no description |
| **ingress-cos**  string | no description  **Choices:**   - `"disable"` - `"cos0"` - `"cos1"` - `"cos2"` - `"cos3"` - `"cos4"` - `"cos5"` - `"cos6"` - `"cos7"` |
| **ingress-shaping-profile**  string | no description |
| **ingress-spillover-threshold**  integer | no description |
| **interconnect-profile**  string | Set interconnect profile.  **Choices:**   - `"default"` - `"profile1"` - `"profile2"` |
| **internal**  integer | no description |
| **ip**  string | no description |
| **ip-managed-by-fortiipam**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"inherit-global"` |
| **ipmac**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ips-sniffer-mode**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ipunnumbered**  string | no description |
| **ipv6**  dictionary | no description |
| **autoconf**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **cli-conn6-status**  integer | no description |
| **dhcp6-client-options**  list / elements=string | no description  **Choices:**   - `"rapid"` - `"iapd"` - `"iana"` - `"dns"` - `"dnsname"` |
| **dhcp6-information-request**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp6-prefix-delegation**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp6-prefix-hint**  string | no description |
| **dhcp6-prefix-hint-plt**  integer | no description |
| **dhcp6-prefix-hint-vlt**  integer | no description |
| **dhcp6-relay-interface-id**  string | DHCP6 relay interface ID. |
| **dhcp6-relay-ip**  string | no description |
| **dhcp6-relay-service**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp6-relay-source-interface**  string | Enable/disable use of address on this interface as the source address of the relay message.  **Choices:**   - `"disable"` - `"enable"` |
| **dhcp6-relay-source-ip**  string | IPv6 address used by the DHCP6 relay as its source IP. |
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
| **l2forward**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **l2tp-client**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **lacp-ha-secondary**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **lacp-ha-slave**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **lacp-mode**  string | no description  **Choices:**   - `"static"` - `"passive"` - `"active"` |
| **lacp-speed**  string | no description  **Choices:**   - `"slow"` - `"fast"` |
| **large-receive-offload**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **lcp-echo-interval**  integer | no description |
| **lcp-max-echo-fails**  integer | no description |
| **link-up-delay**  integer | no description |
| **listen-forticlient-connection**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **lldp-network-policy**  string | no description |
| **lldp-reception**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"vdom"` |
| **lldp-transmission**  string | no description  **Choices:**   - `"enable"` - `"disable"` - `"vdom"` |
| **log**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **macaddr**  string | no description |
| **managed-subnetwork-size**  string | no description  **Choices:**   - `"256"` - `"512"` - `"1024"` - `"2048"` - `"4096"` - `"8192"` - `"16384"` - `"32768"` - `"65536"` - `"32"` - `"64"` - `"128"` |
| **management-ip**  string | no description |
| **max-egress-burst-rate**  integer | no description |
| **max-egress-rate**  integer | no description |
| **measured-downstream-bandwidth**  integer | no description |
| **measured-upstream-bandwidth**  integer | no description |
| **mediatype**  string | no description  **Choices:**   - `"serdes-sfp"` - `"sgmii-sfp"` - `"cfp2-sr10"` - `"cfp2-lr4"` - `"serdes-copper-sfp"` - `"sr"` - `"cr"` - `"lr"` - `"qsfp28-sr4"` - `"qsfp28-lr4"` - `"qsfp28-cr4"` - `"sr4"` - `"cr4"` - `"lr4"` - `"none"` - `"gmii"` - `"sgmii"` - `"sr2"` - `"lr2"` - `"cr2"` - `"sr8"` - `"lr8"` - `"cr8"` |
| **member**  any | (list or str) no description |
| **min-links**  integer | no description |
| **min-links-down**  string | no description  **Choices:**   - `"operational"` - `"administrative"` |
| **mode**  string | no description  **Choices:**   - `"static"` - `"dhcp"` - `"pppoe"` - `"pppoa"` - `"ipoa"` - `"eoa"` |
| **monitor-bandwidth**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **mtu**  integer | no description |
| **mtu-override**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **mux-type**  string | no description  **Choices:**   - `"llc-encaps"` - `"vc-encaps"` |
| **name**  string | no description |
| **ndiscforward**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **netbios-forward**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **netflow-sampler**  string | no description  **Choices:**   - `"disable"` - `"tx"` - `"rx"` - `"both"` |
| **np-qos-profile**  integer | NP QoS profile ID. |
| **npu-fastpath**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **nst**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **out-force-vlan-cos**  integer | no description |
| **outbandwidth**  integer | no description |
| **padt-retry-timeout**  integer | no description |
| **password**  any | (list) no description |
| **peer-interface**  any | (list or str) no description |
| **phy-mode**  string | no description  **Choices:**   - `"auto"` - `"adsl"` - `"vdsl"` - `"adsl-auto"` - `"vdsl2"` - `"adsl2+"` - `"adsl2"` - `"g.dmt"` - `"t1.413"` - `"g.lite"` |
| **ping-serv-status**  integer | no description |
| **poe**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **polling-interval**  integer | no description |
| **pppoe-unnumbered-negotiate**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **pptp-auth-type**  string | no description  **Choices:**   - `"auto"` - `"pap"` - `"chap"` - `"mschapv1"` - `"mschapv2"` |
| **pptp-client**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **pptp-password**  any | (list) no description |
| **pptp-server-ip**  string | no description |
| **pptp-timeout**  integer | no description |
| **pptp-user**  string | no description |
| **preserve-session-route**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **priority**  integer | no description |
| **priority-override**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **proxy-captive-portal**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
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
| **redundant-interface**  string | no description |
| **remote-ip**  string | no description |
| **replacemsg-override-group**  string | no description |
| **retransmission**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ring-rx**  integer | no description |
| **ring-tx**  integer | no description |
| **role**  string | no description  **Choices:**   - `"lan"` - `"wan"` - `"dmz"` - `"undefined"` |
| **sample-direction**  string | no description  **Choices:**   - `"rx"` - `"tx"` - `"both"` |
| **sample-rate**  integer | no description |
| **scan-botnet-connections**  string | no description  **Choices:**   - `"disable"` - `"block"` - `"monitor"` |
| **secondary-IP**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **secondaryip**  list / elements=dictionary | no description |
| **allowaccess**  list / elements=string | no description  **Choices:**   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"auto-ipsec"` - `"radius-acct"` - `"probe-response"` - `"capwap"` - `"dnp"` - `"ftm"` - `"fabric"` - `"speed-test"` |
| **detectprotocol**  list / elements=string | no description  **Choices:**   - `"ping"` - `"tcp-echo"` - `"udp-echo"` |
| **detectserver**  string | no description |
| **gwdetect**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **ha-priority**  integer | no description |
| **id**  integer | no description |
| **ip**  string | no description |
| **ping-serv-status**  integer | no description |
| **secip-relay-ip**  string | DHCP relay IP address. |
| **seq**  integer | no description |
| **security-8021x-dynamic-vlan-id**  integer | no description |
| **security-8021x-master**  string | no description |
| **security-8021x-mode**  string | no description  **Choices:**   - `"default"` - `"dynamic-vlan"` - `"fallback"` - `"slave"` |
| **security-exempt-list**  string | no description |
| **security-external-logout**  string | no description |
| **security-external-web**  string | no description |
| **security-groups**  any | (list or str) no description |
| **security-mac-auth-bypass**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"mac-auth-only"` |
| **security-mode**  string | no description  **Choices:**   - `"none"` - `"captive-portal"` - `"802.1X"` |
| **security-redirect-url**  string | no description |
| **select-profile-30a-35b**  string | Select VDSL Profile 30a or 35b.  **Choices:**   - `"30A"` - `"35B"` |
| **service-name**  string | no description |
| **sflow-sampler**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **sfp-dsl**  string | Enable/disable SFP DSL.  **Choices:**   - `"disable"` - `"enable"` |
| **sfp-dsl-adsl-fallback**  string | Enable/disable SFP DSL ADSL fallback.  **Choices:**   - `"disable"` - `"enable"` |
| **sfp-dsl-autodetect**  string | Enable/disable SFP DSL MAC address autodetect.  **Choices:**   - `"disable"` - `"enable"` |
| **sfp-dsl-mac**  string | SFP DSL MAC address. |
| **speed**  string | no description  **Choices:**   - `"auto"` - `"10full"` - `"10half"` - `"100full"` - `"100half"` - `"1000full"` - `"1000half"` - `"10000full"` - `"1000auto"` - `"10000auto"` - `"40000full"` - `"100Gfull"` - `"25000full"` - `"40000auto"` - `"25000auto"` - `"100Gauto"` - `"400Gfull"` - `"400Gauto"` - `"50000full"` - `"2500auto"` - `"5000auto"` - `"50000auto"` - `"200Gfull"` - `"200Gauto"` - `"100auto"` |
| **spillover-threshold**  integer | no description |
| **src-check**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | no description  **Choices:**   - `"down"` - `"up"` |
| **stp**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **stp-ha-secondary**  string | Control STP behaviour on HA secondary.  **Choices:**   - `"disable"` - `"enable"` - `"priority-adjust"` |
| **stp-ha-slave**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"priority-adjust"` |
| **stpforward**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **stpforward-mode**  string | no description  **Choices:**   - `"rpl-all-ext-id"` - `"rpl-bridge-ext-id"` - `"rpl-nothing"` |
| **strip-priority-vlan-tag**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **subst**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **substitute-dst-mac**  string | no description |
| **sw-algorithm**  string | Frame distribution algorithm for switch.  **Choices:**   - `"l2"` - `"l3"` - `"eh"` |
| **swc-first-create**  integer | Initial create for switch-controller VLANs. |
| **swc-vlan**  integer | no description |
| **switch**  string | no description |
| **switch-controller-access-vlan**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-arp-inspection**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-auth**  string | no description  **Choices:**   - `"radius"` - `"usergroup"` |
| **switch-controller-dhcp-snooping**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-dhcp-snooping-option82**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-dhcp-snooping-verify-mac**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-dynamic**  string | Integrated FortiLink settings for managed FortiSwitch. |
| **switch-controller-feature**  string | no description  **Choices:**   - `"none"` - `"default-vlan"` - `"quarantine"` - `"sniffer"` - `"voice"` - `"camera"` - `"rspan"` - `"video"` - `"nac"` - `"nac-segment"` |
| **switch-controller-igmp-snooping**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-igmp-snooping-fast-leave**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-igmp-snooping-proxy**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-iot-scanning**  string | Enable/disable managed FortiSwitch IoT scanning.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-learning-limit**  integer | no description |
| **switch-controller-mgmt-vlan**  integer | no description |
| **switch-controller-nac**  string | no description |
| **switch-controller-netflow-collect**  string | NetFlow collection and processing.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-offload**  string | Enable/disable managed FortiSwitch routing offload.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-offload-gw**  string | Enable/disable managed FortiSwitch routing offload gateway.  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-offload-ip**  string | IP for routing offload on FortiSwitch. |
| **switch-controller-offloading**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-offloading-gw**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-offloading-ip**  string | no description |
| **switch-controller-radius-server**  string | no description |
| **switch-controller-rspan-mode**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **switch-controller-source-ip**  string | Source IP address used in FortiLink over L3 connections.  **Choices:**   - `"outbound"` - `"fixed"` |
| **switch-controller-traffic-policy**  string | no description |
| **system-id**  string | Define a system ID for the aggregate interface. |
| **system-id-type**  string | Method in which system ID is generated.  **Choices:**   - `"auto"` - `"user"` |
| **tc-mode**  string | no description  **Choices:**   - `"ptm"` - `"atm"` |
| **tcp-mss**  integer | no description |
| **trunk**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **trust-ip-1**  string | no description |
| **trust-ip-2**  string | no description |
| **trust-ip-3**  string | no description |
| **trust-ip6-1**  string | no description |
| **trust-ip6-2**  string | no description |
| **trust-ip6-3**  string | no description |
| **type**  string | no description  **Choices:**   - `"physical"` - `"vlan"` - `"aggregate"` - `"redundant"` - `"tunnel"` - `"wireless"` - `"vdom-link"` - `"loopback"` - `"switch"` - `"hard-switch"` - `"hdlc"` - `"vap-switch"` - `"wl-mesh"` - `"fortilink"` - `"switch-vlan"` - `"fctrl-trunk"` - `"tdm"` - `"fext-wan"` - `"vxlan"` - `"emac-vlan"` - `"geneve"` - `"ssl"` - `"lan-extension"` |
| **username**  string | no description |
| **vci**  integer | no description |
| **vectoring**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **vindex**  integer | no description |
| **vlan-id**  integer | Vlan ID |
| **vlan-op-mode**  string | Configure DSL 802.  **Choices:**   - `"tag"` - `"untag"` - `"passthrough"` |
| **vlan-protocol**  string | no description  **Choices:**   - `"8021q"` - `"8021ad"` |
| **vlanforward**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **vlanid**  integer | no description |
| **vpi**  integer | no description |
| **vrf**  integer | no description |
| **vrrp**  list / elements=dictionary | no description |
| **accept-mode**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **adv-interval**  integer | no description |
| **ignore-default-route**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **preempt**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **priority**  integer | no description |
| **proxy-arp**  list / elements=dictionary | no description |
| **id**  integer | ID. |
| **ip**  string | Set IP addresses of proxy ARP. |
| **start-time**  integer | no description |
| **status**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **version**  string | no description  **Choices:**   - `"2"` - `"3"` |
| **vrdst**  any | (list) no description |
| **vrdst-priority**  integer | no description |
| **vrgrp**  integer | no description |
| **vrid**  integer | no description |
| **vrip**  string | no description |
| **vrrp-virtual-mac**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **wccp**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **weight**  integer | no description |
| **wifi-5g-threshold**  string | no description |
| **wifi-acl**  string | no description  **Choices:**   - `"deny"` - `"allow"` |
| **wifi-ap-band**  string | no description  **Choices:**   - `"any"` - `"5g-preferred"` - `"5g-only"` |
| **wifi-auth**  string | no description  **Choices:**   - `"PSK"` - `"RADIUS"` - `"radius"` - `"usergroup"` |
| **wifi-auto-connect**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **wifi-auto-save**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **wifi-broadcast-ssid**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **wifi-dns-server1**  string | DNS server 1. |
| **wifi-dns-server2**  string | DNS server 2. |
| **wifi-encrypt**  string | no description  **Choices:**   - `"TKIP"` - `"AES"` |
| **wifi-fragment-threshold**  integer | no description |
| **wifi-gateway**  string | IPv4 default gateway IP address. |
| **wifi-key**  any | (list) no description |
| **wifi-keyindex**  integer | no description |
| **wifi-mac-filter**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **wifi-passphrase**  any | (list) no description |
| **wifi-radius-server**  string | no description |
| **wifi-rts-threshold**  integer | no description |
| **wifi-security**  string | no description  **Choices:**   - `"None"` - `"WEP64"` - `"wep64"` - `"WEP128"` - `"wep128"` - `"WPA_PSK"` - `"WPA_RADIUS"` - `"WPA"` - `"WPA2"` - `"WPA2_AUTO"` - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` - `"wpa-only-personal"` - `"wpa-only-enterprise"` - `"wpa2-only-personal"` - `"wpa2-only-enterprise"` |
| **wifi-ssid**  string | no description |
| **wifi-usergroup**  string | no description |
| **wins-ip**  string | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **vlan**  string / required | the parameter (vlan) in requested url |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_fsp_vlan_interface_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_fsp_vlan_interface_module.md#id4)

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
    - name: Configure interfaces.
      fmgr_fsp_vlan_interface:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        vlan: <your own value>
        fsp_vlan_interface:
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
          ingress-spillover-threshold: <integer>
          internal: <integer>
          ip: <string>
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
            ip6-dns-server-override: <value in [disable, enable]>
            ip6-hop-limit: <integer>
            ip6-link-mtu: <integer>
            ip6-manage-flag: <value in [disable, enable]>
            ip6-max-interval: <integer>
            ip6-min-interval: <integer>
            ip6-mode: <value in [static, dhcp, pppoe, ...]>
            ip6-other-flag: <value in [disable, enable]>
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
            ip6-extra-addr:
              -
                prefix: <string>
            ip6-prefix-list:
              -
                autonomous-flag: <value in [disable, enable]>
                dnssl: <list or string>
                onlink-flag: <value in [disable, enable]>
                preferred-life-time: <integer>
                prefix: <string>
                rdnss: <list or string>
                valid-life-time: <integer>
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
          management-ip: <string>
          max-egress-burst-rate: <integer>
          max-egress-rate: <integer>
          mediatype: <value in [serdes-sfp, sgmii-sfp, cfp2-sr10, ...]>
          member: <list or string>
          min-links: <integer>
          min-links-down: <value in [operational, administrative]>
          mode: <value in [static, dhcp, pppoe, ...]>
          mtu: <integer>
          mtu-override: <value in [disable, enable]>
          mux-type: <value in [llc-encaps, vc-encaps]>
          name: <string>
          ndiscforward: <value in [disable, enable]>
          netbios-forward: <value in [disable, enable]>
          netflow-sampler: <value in [disable, tx, rx, ...]>
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
          switch: <string>
          switch-controller-access-vlan: <value in [disable, enable]>
          switch-controller-arp-inspection: <value in [disable, enable]>
          switch-controller-auth: <value in [radius, usergroup]>
          switch-controller-dhcp-snooping: <value in [disable, enable]>
          switch-controller-dhcp-snooping-option82: <value in [disable, enable]>
          switch-controller-dhcp-snooping-verify-mac: <value in [disable, enable]>
          switch-controller-igmp-snooping: <value in [disable, enable]>
          switch-controller-learning-limit: <integer>
          switch-controller-radius-server: <string>
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
          eip: <string>
          fortilink-neighbor-detect: <value in [lldp, fortilink]>
          ingress-shaping-profile: <string>
          ring-rx: <integer>
          ring-tx: <integer>
          switch-controller-igmp-snooping-fast-leave: <value in [disable, enable]>
          switch-controller-igmp-snooping-proxy: <value in [disable, enable]>
          switch-controller-rspan-mode: <value in [disable, enable]>
          bandwidth-measure-time: <integer>
          ip-managed-by-fortiipam: <value in [disable, enable, inherit-global]>
          managed-subnetwork-size: <value in [256, 512, 1024, ...]>
          measured-downstream-bandwidth: <integer>
          measured-upstream-bandwidth: <integer>
          monitor-bandwidth: <value in [disable, enable]>
          swc-vlan: <integer>
          switch-controller-feature: <value in [none, default-vlan, quarantine, ...]>
          switch-controller-mgmt-vlan: <integer>
          switch-controller-nac: <string>
          vlan-protocol: <value in [8021q, 8021ad]>
          dhcp-relay-interface: <string>
          dhcp-relay-interface-select-method: <value in [auto, sdwan, specify]>
          np-qos-profile: <integer>
          swc-first-create: <integer>
          switch-controller-iot-scanning: <value in [disable, enable]>
          switch-controller-source-ip: <value in [outbound, fixed]>
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

## [Return Values](fmgr_fsp_vlan_interface_module.md#id5)

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
