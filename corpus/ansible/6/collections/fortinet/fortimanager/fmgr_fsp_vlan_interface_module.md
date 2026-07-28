---
collection: ansible
version: "6"
title: "fortinet.fortimanager.fmgr_fsp_vlan_interface module – no description"
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortimanager/fmgr_fsp_vlan_interface_module.html
fetched_at: 2026-07-27T17:32:54+00:00
---
# fortinet.fortimanager.fmgr_fsp_vlan_interface module – no description

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_fsp_vlan_interface`.

New in fortinet.fortimanager 1.0.0

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
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | only set to True when module schema diffs with FortiManager API structure,  module continues to execute without validating parameters  Choices:   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task  Choices:   - `false` ← (default) - `true` |
| **fsp_vlan_interface**  dictionary | the top level parameters set |
| **ac-name**  string | no description |
| **aggregate**  string | no description |
| **algorithm**  string | no description  Choices:   - `"L2"` - `"L3"` - `"L4"` - `"LB"` |
| **alias**  string | no description |
| **allowaccess**  list / elements=string | description  Choices:   - `"https"` - `"ping"` - `"ssh"` - `"snmp"` - `"http"` - `"telnet"` - `"fgfm"` - `"auto-ipsec"` - `"radius-acct"` - `"probe-response"` - `"capwap"` - `"dnp"` - `"ftm"` - `"fabric"` - `"speed-test"` |
| **ap-discover**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **arpforward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **atm-protocol**  string | no description  Choices:   - `"none"` - `"ipoa"` |
| **auth-cert**  string | no description |
| **auth-portal-addr**  string | no description |
| **auth-type**  string | no description  Choices:   - `"auto"` - `"pap"` - `"chap"` - `"mschapv1"` - `"mschapv2"` |
| **auto-auth-extension-device**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **bandwidth-measure-time**  integer | no description |
| **bfd**  string | no description  Choices:   - `"global"` - `"enable"` - `"disable"` |
| **bfd-desired-min-tx**  integer | no description |
| **bfd-detect-mult**  integer | no description |
| **bfd-required-min-rx**  integer | no description |
| **broadcast-forticlient-discovery**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **broadcast-forward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **captive-portal**  integer | no description |
| **cli-conn-status**  integer | no description |
| **color**  integer | no description |
| **ddns**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ddns-auth**  string | no description  Choices:   - `"disable"` - `"tsig"` |
| **ddns-domain**  string | no description |
| **ddns-key**  string | no description |
| **ddns-keyname**  string | no description |
| **ddns-password**  string | description |
| **ddns-server**  string | no description  Choices:   - `"dhs.org"` - `"dyndns.org"` - `"dyns.net"` - `"tzo.com"` - `"ods.org"` - `"vavic.com"` - `"now.net.cn"` - `"dipdns.net"` - `"easydns.com"` - `"genericDDNS"` |
| **ddns-server-ip**  string | no description |
| **ddns-sn**  string | no description |
| **ddns-ttl**  integer | no description |
| **ddns-username**  string | no description |
| **ddns-zone**  string | no description |
| **dedicated-to**  string | no description  Choices:   - `"none"` - `"management"` |
| **defaultgw**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **description**  string | no description |
| **detected-peer-mtu**  integer | no description |
| **detectprotocol**  list / elements=string | description  Choices:   - `"ping"` - `"tcp-echo"` - `"udp-echo"` |
| **detectserver**  string | no description |
| **device-access-list**  string | no description |
| **device-identification**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **device-identification-active-scan**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **device-netscan**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **device-user-identification**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **devindex**  integer | no description |
| **dhcp-classless-route-addition**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dhcp-client-identifier**  string | no description |
| **dhcp-relay-agent-option**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dhcp-relay-interface**  string | no description |
| **dhcp-relay-interface-select-method**  string | no description  Choices:   - `"auto"` - `"sdwan"` - `"specify"` |
| **dhcp-relay-ip**  string | description |
| **dhcp-relay-link-selection**  string | no description |
| **dhcp-relay-request-all-server**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dhcp-relay-service**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dhcp-relay-type**  string | no description  Choices:   - `"regular"` - `"ipsec"` |
| **dhcp-renew-time**  integer | no description |
| **disc-retry-timeout**  integer | no description |
| **disconnect-threshold**  integer | no description |
| **distance**  integer | no description |
| **dns-query**  string | no description  Choices:   - `"disable"` - `"recursive"` - `"non-recursive"` |
| **dns-server-override**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **dns-server-protocol**  list / elements=string | description  Choices:   - `"cleartext"` - `"dot"` - `"doh"` |
| **drop-fragment**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **drop-overlapped-fragment**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **eap-ca-cert**  string | no description |
| **eap-identity**  string | no description |
| **eap-method**  string | no description  Choices:   - `"tls"` - `"peap"` |
| **eap-password**  string | description |
| **eap-supplicant**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **eap-user-cert**  string | no description |
| **egress-cos**  string | no description  Choices:   - `"disable"` - `"cos0"` - `"cos1"` - `"cos2"` - `"cos3"` - `"cos4"` - `"cos5"` - `"cos6"` - `"cos7"` |
| **egress-shaping-profile**  string | no description |
| **eip**  string | no description |
| **endpoint-compliance**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **estimated-downstream-bandwidth**  integer | no description |
| **estimated-upstream-bandwidth**  integer | no description |
| **explicit-ftp-proxy**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **explicit-web-proxy**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **external**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fail-action-on-extender**  string | no description  Choices:   - `"soft-restart"` - `"hard-restart"` - `"reboot"` |
| **fail-alert-interfaces**  string | no description |
| **fail-alert-method**  string | no description  Choices:   - `"link-failed-signal"` - `"link-down"` |
| **fail-detect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fail-detect-option**  list / elements=string | description  Choices:   - `"detectserver"` - `"link-down"` |
| **fdp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fortiheartbeat**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fortilink**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fortilink-backup-link**  integer | no description |
| **fortilink-neighbor-detect**  string | no description  Choices:   - `"lldp"` - `"fortilink"` |
| **fortilink-split-interface**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **fortilink-stacking**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **forward-domain**  integer | no description |
| **forward-error-correction**  string | no description  Choices:   - `"disable"` - `"enable"` - `"rs-fec"` - `"base-r-fec"` - `"fec-cl91"` - `"fec-cl74"` - `"rs-544"` - `"none"` - `"cl91-rs-fec"` - `"cl74-fc-fec"` |
| **fp-anomaly**  list / elements=string | description  Choices:   - `"drop_tcp_fin_noack"` - `"pass_winnuke"` - `"pass_tcpland"` - `"pass_udpland"` - `"pass_icmpland"` - `"pass_ipland"` - `"pass_iprr"` - `"pass_ipssrr"` - `"pass_iplsrr"` - `"pass_ipstream"` - `"pass_ipsecurity"` - `"pass_iptimestamp"` - `"pass_ipunknown_option"` - `"pass_ipunknown_prot"` - `"pass_icmp_frag"` - `"pass_tcp_no_flag"` - `"pass_tcp_fin_noack"` - `"drop_winnuke"` - `"drop_tcpland"` - `"drop_udpland"` - `"drop_icmpland"` - `"drop_ipland"` - `"drop_iprr"` - `"drop_ipssrr"` - `"drop_iplsrr"` - `"drop_ipstream"` - `"drop_ipsecurity"` - `"drop_iptimestamp"` - `"drop_ipunknown_option"` - `"drop_ipunknown_prot"` - `"drop_icmp_frag"` - `"drop_tcp_no_flag"` |
| **fp-disable**  list / elements=string | description  Choices:   - `"all"` - `"ipsec"` - `"none"` |
| **gateway-address**  string | no description |
| **gi-gk**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **gwaddr**  string | no description |
| **gwdetect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ha-priority**  integer | no description |
| **icmp-accept-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **icmp-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **icmp-send-redirect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ident-accept**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **idle-timeout**  integer | no description |
| **if-mdix**  string | no description  Choices:   - `"auto"` - `"normal"` - `"crossover"` |
| **if-media**  string | no description  Choices:   - `"auto"` - `"copper"` - `"fiber"` |
| **ike-saml-server**  string | no description |
| **in-force-vlan-cos**  integer | no description |
| **inbandwidth**  integer | no description |
| **ingress-cos**  string | no description  Choices:   - `"disable"` - `"cos0"` - `"cos1"` - `"cos2"` - `"cos3"` - `"cos4"` - `"cos5"` - `"cos6"` - `"cos7"` |
| **ingress-shaping-profile**  string | no description |
| **ingress-spillover-threshold**  integer | no description |
| **internal**  integer | no description |
| **ip**  string | no description |
| **ip-managed-by-fortiipam**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ipmac**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ips-sniffer-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ipunnumbered**  string | no description |
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
| **l2forward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **l2tp-client**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **lacp-ha-secondary**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **lacp-ha-slave**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **lacp-mode**  string | no description  Choices:   - `"static"` - `"passive"` - `"active"` |
| **lacp-speed**  string | no description  Choices:   - `"slow"` - `"fast"` |
| **lcp-echo-interval**  integer | no description |
| **lcp-max-echo-fails**  integer | no description |
| **link-up-delay**  integer | no description |
| **listen-forticlient-connection**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **lldp-network-policy**  string | no description |
| **lldp-reception**  string | no description  Choices:   - `"disable"` - `"enable"` - `"vdom"` |
| **lldp-transmission**  string | no description  Choices:   - `"enable"` - `"disable"` - `"vdom"` |
| **log**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **macaddr**  string | no description |
| **managed-subnetwork-size**  string | no description  Choices:   - `"256"` - `"512"` - `"1024"` - `"2048"` - `"4096"` - `"8192"` - `"16384"` - `"32768"` - `"65536"` - `"32"` - `"64"` - `"128"` |
| **management-ip**  string | no description |
| **max-egress-burst-rate**  integer | no description |
| **max-egress-rate**  integer | no description |
| **measured-downstream-bandwidth**  integer | no description |
| **measured-upstream-bandwidth**  integer | no description |
| **mediatype**  string | no description  Choices:   - `"serdes-sfp"` - `"sgmii-sfp"` - `"cfp2-sr10"` - `"cfp2-lr4"` - `"serdes-copper-sfp"` - `"sr"` - `"cr"` - `"lr"` - `"qsfp28-sr4"` - `"qsfp28-lr4"` - `"qsfp28-cr4"` - `"sr4"` - `"cr4"` - `"lr4"` - `"none"` - `"gmii"` - `"sgmii"` |
| **member**  string | no description |
| **min-links**  integer | no description |
| **min-links-down**  string | no description  Choices:   - `"operational"` - `"administrative"` |
| **mode**  string | no description  Choices:   - `"static"` - `"dhcp"` - `"pppoe"` - `"pppoa"` - `"ipoa"` - `"eoa"` |
| **monitor-bandwidth**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mtu**  integer | no description |
| **mtu-override**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **mux-type**  string | no description  Choices:   - `"llc-encaps"` - `"vc-encaps"` |
| **name**  string | no description |
| **ndiscforward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **netbios-forward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **netflow-sampler**  string | no description  Choices:   - `"disable"` - `"tx"` - `"rx"` - `"both"` |
| **np-qos-profile**  integer | no description |
| **npu-fastpath**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **nst**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **out-force-vlan-cos**  integer | no description |
| **outbandwidth**  integer | no description |
| **padt-retry-timeout**  integer | no description |
| **password**  string | description |
| **peer-interface**  string | no description |
| **phy-mode**  string | no description  Choices:   - `"auto"` - `"adsl"` - `"vdsl"` - `"adsl-auto"` - `"vdsl2"` - `"adsl2+"` - `"adsl2"` - `"g.dmt"` - `"t1.413"` - `"g.lite"` |
| **ping-serv-status**  integer | no description |
| **poe**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **polling-interval**  integer | no description |
| **pppoe-unnumbered-negotiate**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pptp-auth-type**  string | no description  Choices:   - `"auto"` - `"pap"` - `"chap"` - `"mschapv1"` - `"mschapv2"` |
| **pptp-client**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pptp-password**  string | description |
| **pptp-server-ip**  string | no description |
| **pptp-timeout**  integer | no description |
| **pptp-user**  string | no description |
| **preserve-session-route**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **priority**  integer | no description |
| **priority-override**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **proxy-captive-portal**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **pvc-atm-qos**  string | no description  Choices:   - `"cbr"` - `"rt-vbr"` - `"nrt-vbr"` |
| **pvc-chan**  integer | no description |
| **pvc-crc**  integer | no description |
| **pvc-pcr**  integer | no description |
| **pvc-scr**  integer | no description |
| **pvc-vlan-id**  integer | no description |
| **pvc-vlan-rx-id**  integer | no description |
| **pvc-vlan-rx-op**  string | no description  Choices:   - `"pass-through"` - `"replace"` - `"remove"` |
| **pvc-vlan-tx-id**  integer | no description |
| **pvc-vlan-tx-op**  string | no description  Choices:   - `"pass-through"` - `"replace"` - `"remove"` |
| **reachable-time**  integer | no description |
| **redundant-interface**  string | no description |
| **remote-ip**  string | no description |
| **replacemsg-override-group**  string | no description |
| **retransmission**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **ring-rx**  integer | no description |
| **ring-tx**  integer | no description |
| **role**  string | no description  Choices:   - `"lan"` - `"wan"` - `"dmz"` - `"undefined"` |
| **sample-direction**  string | no description  Choices:   - `"rx"` - `"tx"` - `"both"` |
| **sample-rate**  integer | no description |
| **scan-botnet-connections**  string | no description  Choices:   - `"disable"` - `"block"` - `"monitor"` |
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
| **security-8021x-dynamic-vlan-id**  integer | no description |
| **security-8021x-master**  string | no description |
| **security-8021x-mode**  string | no description  Choices:   - `"default"` - `"dynamic-vlan"` - `"fallback"` - `"slave"` |
| **security-exempt-list**  string | no description |
| **security-external-logout**  string | no description |
| **security-external-web**  string | no description |
| **security-groups**  string | no description |
| **security-mac-auth-bypass**  string | no description  Choices:   - `"disable"` - `"enable"` - `"mac-auth-only"` |
| **security-mode**  string | no description  Choices:   - `"none"` - `"captive-portal"` - `"802.1X"` |
| **security-redirect-url**  string | no description |
| **select-profile-30a-35b**  string | no description  Choices:   - `"30A"` - `"35B"` |
| **service-name**  string | no description |
| **sflow-sampler**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sfp-dsl**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sfp-dsl-adsl-fallback**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sfp-dsl-autodetect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **sfp-dsl-mac**  string | no description |
| **speed**  string | no description  Choices:   - `"auto"` - `"10full"` - `"10half"` - `"100full"` - `"100half"` - `"1000full"` - `"1000half"` - `"10000full"` - `"1000auto"` - `"10000auto"` - `"40000full"` - `"100Gfull"` - `"25000full"` - `"40000auto"` - `"25000auto"` - `"100Gauto"` - `"400Gfull"` - `"400Gauto"` |
| **spillover-threshold**  integer | no description |
| **src-check**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **status**  string | no description  Choices:   - `"down"` - `"up"` |
| **stp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **stp-ha-secondary**  string | no description  Choices:   - `"disable"` - `"enable"` - `"priority-adjust"` |
| **stp-ha-slave**  string | no description  Choices:   - `"disable"` - `"enable"` - `"priority-adjust"` |
| **stpforward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **stpforward-mode**  string | no description  Choices:   - `"rpl-all-ext-id"` - `"rpl-bridge-ext-id"` - `"rpl-nothing"` |
| **strip-priority-vlan-tag**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **subst**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **substitute-dst-mac**  string | no description |
| **sw-algorithm**  string | no description  Choices:   - `"l2"` - `"l3"` - `"eh"` |
| **swc-first-create**  integer | no description |
| **swc-vlan**  integer | no description |
| **switch**  string | no description |
| **switch-controller-access-vlan**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switch-controller-arp-inspection**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switch-controller-auth**  string | no description  Choices:   - `"radius"` - `"usergroup"` |
| **switch-controller-dhcp-snooping**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switch-controller-dhcp-snooping-option82**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switch-controller-dhcp-snooping-verify-mac**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switch-controller-dynamic**  string | no description |
| **switch-controller-feature**  string | no description  Choices:   - `"none"` - `"default-vlan"` - `"quarantine"` - `"sniffer"` - `"voice"` - `"camera"` - `"rspan"` - `"video"` - `"nac"` - `"nac-segment"` |
| **switch-controller-igmp-snooping**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switch-controller-igmp-snooping-fast-leave**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switch-controller-igmp-snooping-proxy**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switch-controller-iot-scanning**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switch-controller-learning-limit**  integer | no description |
| **switch-controller-mgmt-vlan**  integer | no description |
| **switch-controller-nac**  string | no description |
| **switch-controller-radius-server**  string | no description |
| **switch-controller-rspan-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **switch-controller-source-ip**  string | no description  Choices:   - `"outbound"` - `"fixed"` |
| **switch-controller-traffic-policy**  string | no description |
| **system-id**  string | no description |
| **system-id-type**  string | no description  Choices:   - `"auto"` - `"user"` |
| **tc-mode**  string | no description  Choices:   - `"ptm"` - `"atm"` |
| **tcp-mss**  integer | no description |
| **trunk**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **trust-ip-1**  string | no description |
| **trust-ip-2**  string | no description |
| **trust-ip-3**  string | no description |
| **trust-ip6-1**  string | no description |
| **trust-ip6-2**  string | no description |
| **trust-ip6-3**  string | no description |
| **type**  string | no description  Choices:   - `"physical"` - `"vlan"` - `"aggregate"` - `"redundant"` - `"tunnel"` - `"wireless"` - `"vdom-link"` - `"loopback"` - `"switch"` - `"hard-switch"` - `"hdlc"` - `"vap-switch"` - `"wl-mesh"` - `"fortilink"` - `"switch-vlan"` - `"fctrl-trunk"` - `"tdm"` - `"fext-wan"` - `"vxlan"` - `"emac-vlan"` - `"geneve"` - `"ssl"` - `"lan-extension"` |
| **username**  string | no description |
| **vci**  integer | no description |
| **vectoring**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **vindex**  integer | no description |
| **vlan-id**  integer | no description |
| **vlan-op-mode**  string | no description  Choices:   - `"tag"` - `"untag"` - `"passthrough"` |
| **vlan-protocol**  string | no description  Choices:   - `"8021q"` - `"8021ad"` |
| **vlanforward**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **vlanid**  integer | no description |
| **vpi**  integer | no description |
| **vrf**  integer | no description |
| **vrrp**  list / elements=string | description |
| **accept-mode**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **adv-interval**  integer | no description |
| **ignore-default-route**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **preempt**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **priority**  integer | no description |
| **start-time**  integer | no description |
| **status**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **version**  string | no description  Choices:   - `"2"` - `"3"` |
| **vrdst**  string | description |
| **vrdst-priority**  integer | no description |
| **vrgrp**  integer | no description |
| **vrid**  integer | no description |
| **vrip**  string | no description |
| **vrrp-virtual-mac**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **wccp**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **weight**  integer | no description |
| **wifi-5g-threshold**  string | no description |
| **wifi-acl**  string | no description  Choices:   - `"deny"` - `"allow"` |
| **wifi-ap-band**  string | no description  Choices:   - `"any"` - `"5g-preferred"` - `"5g-only"` |
| **wifi-auth**  string | no description  Choices:   - `"PSK"` - `"RADIUS"` - `"radius"` - `"usergroup"` |
| **wifi-auto-connect**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **wifi-auto-save**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **wifi-broadcast-ssid**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **wifi-encrypt**  string | no description  Choices:   - `"TKIP"` - `"AES"` |
| **wifi-fragment-threshold**  integer | no description |
| **wifi-key**  string | description |
| **wifi-keyindex**  integer | no description |
| **wifi-mac-filter**  string | no description  Choices:   - `"disable"` - `"enable"` |
| **wifi-passphrase**  string | description |
| **wifi-radius-server**  string | no description |
| **wifi-rts-threshold**  integer | no description |
| **wifi-security**  string | no description  Choices:   - `"None"` - `"WEP64"` - `"wep64"` - `"WEP128"` - `"wep128"` - `"WPA_PSK"` - `"WPA_RADIUS"` - `"WPA"` - `"WPA2"` - `"WPA2_AUTO"` - `"open"` - `"wpa-personal"` - `"wpa-enterprise"` - `"wpa-only-personal"` - `"wpa-only-enterprise"` - `"wpa2-only-personal"` - `"wpa2-only-enterprise"` |
| **wifi-ssid**  string | no description |
| **wifi-usergroup**  string | no description |
| **wins-ip**  string | no description |
| **proposed_method**  string | The overridden method for the underlying Json RPC request  Choices:   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=string | the rc codes list with which the conditions to fail will be overriden |
| **rc_succeeded**  list / elements=string | the rc codes list with which the conditions to succeed will be overriden |
| **state**  string / required | the directive to create, update or delete an object  Choices:   - `"present"` - `"absent"` |
| **vlan**  string / required | the parameter (vlan) in requested url |
| **workspace_locking_adom**  string | the adom to lock for FortiManager running in workspace mode, the value can be global and others including root |
| **workspace_locking_timeout**  integer | the maximum time in seconds to wait for other user to release the workspace lock  Default: `300` |

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
   - name: no description
     fmgr_fsp_vlan_interface:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        vlan: <your own value>
        fsp_vlan_interface:
           ac-name: <value of string>
           aggregate: <value of string>
           algorithm: <value in [L2, L3, L4, ...]>
           alias: <value of string>
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
           bfd-desired-min-tx: <value of integer>
           bfd-detect-mult: <value of integer>
           bfd-required-min-rx: <value of integer>
           broadcast-forticlient-discovery: <value in [disable, enable]>
           broadcast-forward: <value in [disable, enable]>
           captive-portal: <value of integer>
           cli-conn-status: <value of integer>
           color: <value of integer>
           ddns: <value in [disable, enable]>
           ddns-auth: <value in [disable, tsig]>
           ddns-domain: <value of string>
           ddns-key: <value of string>
           ddns-keyname: <value of string>
           ddns-password: <value of string>
           ddns-server: <value in [dhs.org, dyndns.org, dyns.net, ...]>
           ddns-server-ip: <value of string>
           ddns-sn: <value of string>
           ddns-ttl: <value of integer>
           ddns-username: <value of string>
           ddns-zone: <value of string>
           dedicated-to: <value in [none, management]>
           defaultgw: <value in [disable, enable]>
           description: <value of string>
           detected-peer-mtu: <value of integer>
           detectprotocol:
             - ping
             - tcp-echo
             - udp-echo
           detectserver: <value of string>
           device-access-list: <value of string>
           device-identification: <value in [disable, enable]>
           device-identification-active-scan: <value in [disable, enable]>
           device-netscan: <value in [disable, enable]>
           device-user-identification: <value in [disable, enable]>
           devindex: <value of integer>
           dhcp-client-identifier: <value of string>
           dhcp-relay-agent-option: <value in [disable, enable]>
           dhcp-relay-ip: <value of string>
           dhcp-relay-service: <value in [disable, enable]>
           dhcp-relay-type: <value in [regular, ipsec]>
           dhcp-renew-time: <value of integer>
           disc-retry-timeout: <value of integer>
           disconnect-threshold: <value of integer>
           distance: <value of integer>
           dns-query: <value in [disable, recursive, non-recursive]>
           dns-server-override: <value in [disable, enable]>
           drop-fragment: <value in [disable, enable]>
           drop-overlapped-fragment: <value in [disable, enable]>
           egress-cos: <value in [disable, cos0, cos1, ...]>
           egress-shaping-profile: <value of string>
           endpoint-compliance: <value in [disable, enable]>
           estimated-downstream-bandwidth: <value of integer>
           estimated-upstream-bandwidth: <value of integer>
           explicit-ftp-proxy: <value in [disable, enable]>
           explicit-web-proxy: <value in [disable, enable]>
           external: <value in [disable, enable]>
           fail-action-on-extender: <value in [soft-restart, hard-restart, reboot]>
           fail-alert-interfaces: <value of string>
           fail-alert-method: <value in [link-failed-signal, link-down]>
           fail-detect: <value in [disable, enable]>
           fail-detect-option:
             - detectserver
             - link-down
           fdp: <value in [disable, enable]>
           fortiheartbeat: <value in [disable, enable]>
           fortilink: <value in [disable, enable]>
           fortilink-backup-link: <value of integer>
           fortilink-split-interface: <value in [disable, enable]>
           fortilink-stacking: <value in [disable, enable]>
           forward-domain: <value of integer>
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
           gateway-address: <value of string>
           gi-gk: <value in [disable, enable]>
           gwaddr: <value of string>
           gwdetect: <value in [disable, enable]>
           ha-priority: <value of integer>
           icmp-accept-redirect: <value in [disable, enable]>
           icmp-redirect: <value in [disable, enable]>
           icmp-send-redirect: <value in [disable, enable]>
           ident-accept: <value in [disable, enable]>
           idle-timeout: <value of integer>
           if-mdix: <value in [auto, normal, crossover]>
           if-media: <value in [auto, copper, fiber]>
           in-force-vlan-cos: <value of integer>
           inbandwidth: <value of integer>
           ingress-cos: <value in [disable, cos0, cos1, ...]>
           ingress-spillover-threshold: <value of integer>
           internal: <value of integer>
           ip: <value of string>
           ipmac: <value in [disable, enable]>
           ips-sniffer-mode: <value in [disable, enable]>
           ipunnumbered: <value of string>
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
              ip6-dns-server-override: <value in [disable, enable]>
              ip6-hop-limit: <value of integer>
              ip6-link-mtu: <value of integer>
              ip6-manage-flag: <value in [disable, enable]>
              ip6-max-interval: <value of integer>
              ip6-min-interval: <value of integer>
              ip6-mode: <value in [static, dhcp, pppoe, ...]>
              ip6-other-flag: <value in [disable, enable]>
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
              ip6-extra-addr:
                -
                    prefix: <value of string>
              ip6-prefix-list:
                -
                    autonomous-flag: <value in [disable, enable]>
                    dnssl: <value of string>
                    onlink-flag: <value in [disable, enable]>
                    preferred-life-time: <value of integer>
                    prefix: <value of string>
                    rdnss: <value of string>
                    valid-life-time: <value of integer>
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
           l2forward: <value in [disable, enable]>
           l2tp-client: <value in [disable, enable]>
           lacp-ha-slave: <value in [disable, enable]>
           lacp-mode: <value in [static, passive, active]>
           lacp-speed: <value in [slow, fast]>
           lcp-echo-interval: <value of integer>
           lcp-max-echo-fails: <value of integer>
           link-up-delay: <value of integer>
           listen-forticlient-connection: <value in [disable, enable]>
           lldp-network-policy: <value of string>
           lldp-reception: <value in [disable, enable, vdom]>
           lldp-transmission: <value in [enable, disable, vdom]>
           log: <value in [disable, enable]>
           macaddr: <value of string>
           management-ip: <value of string>
           max-egress-burst-rate: <value of integer>
           max-egress-rate: <value of integer>
           mediatype: <value in [serdes-sfp, sgmii-sfp, cfp2-sr10, ...]>
           member: <value of string>
           min-links: <value of integer>
           min-links-down: <value in [operational, administrative]>
           mode: <value in [static, dhcp, pppoe, ...]>
           mtu: <value of integer>
           mtu-override: <value in [disable, enable]>
           mux-type: <value in [llc-encaps, vc-encaps]>
           name: <value of string>
           ndiscforward: <value in [disable, enable]>
           netbios-forward: <value in [disable, enable]>
           netflow-sampler: <value in [disable, tx, rx, ...]>
           npu-fastpath: <value in [disable, enable]>
           nst: <value in [disable, enable]>
           out-force-vlan-cos: <value of integer>
           outbandwidth: <value of integer>
           padt-retry-timeout: <value of integer>
           password: <value of string>
           peer-interface: <value of string>
           phy-mode: <value in [auto, adsl, vdsl, ...]>
           ping-serv-status: <value of integer>
           poe: <value in [disable, enable]>
           polling-interval: <value of integer>
           pppoe-unnumbered-negotiate: <value in [disable, enable]>
           pptp-auth-type: <value in [auto, pap, chap, ...]>
           pptp-client: <value in [disable, enable]>
           pptp-password: <value of string>
           pptp-server-ip: <value of string>
           pptp-timeout: <value of integer>
           pptp-user: <value of string>
           preserve-session-route: <value in [disable, enable]>
           priority: <value of integer>
           priority-override: <value in [disable, enable]>
           proxy-captive-portal: <value in [disable, enable]>
           redundant-interface: <value of string>
           remote-ip: <value of string>
           replacemsg-override-group: <value of string>
           retransmission: <value in [disable, enable]>
           role: <value in [lan, wan, dmz, ...]>
           sample-direction: <value in [rx, tx, both]>
           sample-rate: <value of integer>
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
                 detectserver: <value of string>
                 gwdetect: <value in [disable, enable]>
                 ha-priority: <value of integer>
                 id: <value of integer>
                 ip: <value of string>
                 ping-serv-status: <value of integer>
                 seq: <value of integer>
           security-8021x-dynamic-vlan-id: <value of integer>
           security-8021x-master: <value of string>
           security-8021x-mode: <value in [default, dynamic-vlan, fallback, ...]>
           security-exempt-list: <value of string>
           security-external-logout: <value of string>
           security-external-web: <value of string>
           security-groups: <value of string>
           security-mac-auth-bypass: <value in [disable, enable, mac-auth-only]>
           security-mode: <value in [none, captive-portal, 802.1X]>
           security-redirect-url: <value of string>
           service-name: <value of string>
           sflow-sampler: <value in [disable, enable]>
           speed: <value in [auto, 10full, 10half, ...]>
           spillover-threshold: <value of integer>
           src-check: <value in [disable, enable]>
           status: <value in [down, up]>
           stp: <value in [disable, enable]>
           stp-ha-slave: <value in [disable, enable, priority-adjust]>
           stpforward: <value in [disable, enable]>
           stpforward-mode: <value in [rpl-all-ext-id, rpl-bridge-ext-id, rpl-nothing]>
           strip-priority-vlan-tag: <value in [disable, enable]>
           subst: <value in [disable, enable]>
           substitute-dst-mac: <value of string>
           switch: <value of string>
           switch-controller-access-vlan: <value in [disable, enable]>
           switch-controller-arp-inspection: <value in [disable, enable]>
           switch-controller-auth: <value in [radius, usergroup]>
           switch-controller-dhcp-snooping: <value in [disable, enable]>
           switch-controller-dhcp-snooping-option82: <value in [disable, enable]>
           switch-controller-dhcp-snooping-verify-mac: <value in [disable, enable]>
           switch-controller-igmp-snooping: <value in [disable, enable]>
           switch-controller-learning-limit: <value of integer>
           switch-controller-radius-server: <value of string>
           switch-controller-traffic-policy: <value of string>
           tc-mode: <value in [ptm, atm]>
           tcp-mss: <value of integer>
           trunk: <value in [disable, enable]>
           trust-ip-1: <value of string>
           trust-ip-2: <value of string>
           trust-ip-3: <value of string>
           trust-ip6-1: <value of string>
           trust-ip6-2: <value of string>
           trust-ip6-3: <value of string>
           type: <value in [physical, vlan, aggregate, ...]>
           username: <value of string>
           vci: <value of integer>
           vectoring: <value in [disable, enable]>
           vindex: <value of integer>
           vlanforward: <value in [disable, enable]>
           vlanid: <value of integer>
           vpi: <value of integer>
           vrf: <value of integer>
           vrrp:
             -
                 accept-mode: <value in [disable, enable]>
                 adv-interval: <value of integer>
                 ignore-default-route: <value in [disable, enable]>
                 preempt: <value in [disable, enable]>
                 priority: <value of integer>
                 start-time: <value of integer>
                 status: <value in [disable, enable]>
                 version: <value in [2, 3]>
                 vrdst: <value of string>
                 vrdst-priority: <value of integer>
                 vrgrp: <value of integer>
                 vrid: <value of integer>
                 vrip: <value of string>
           vrrp-virtual-mac: <value in [disable, enable]>
           wccp: <value in [disable, enable]>
           weight: <value of integer>
           wifi-5g-threshold: <value of string>
           wifi-acl: <value in [deny, allow]>
           wifi-ap-band: <value in [any, 5g-preferred, 5g-only]>
           wifi-auth: <value in [PSK, RADIUS, radius, ...]>
           wifi-auto-connect: <value in [disable, enable]>
           wifi-auto-save: <value in [disable, enable]>
           wifi-broadcast-ssid: <value in [disable, enable]>
           wifi-encrypt: <value in [TKIP, AES]>
           wifi-fragment-threshold: <value of integer>
           wifi-key: <value of string>
           wifi-keyindex: <value of integer>
           wifi-mac-filter: <value in [disable, enable]>
           wifi-passphrase: <value of string>
           wifi-radius-server: <value of string>
           wifi-rts-threshold: <value of integer>
           wifi-security: <value in [None, WEP64, wep64, ...]>
           wifi-ssid: <value of string>
           wifi-usergroup: <value of string>
           wins-ip: <value of string>
           eip: <value of string>
           fortilink-neighbor-detect: <value in [lldp, fortilink]>
           ingress-shaping-profile: <value of string>
           ring-rx: <value of integer>
           ring-tx: <value of integer>
           switch-controller-igmp-snooping-fast-leave: <value in [disable, enable]>
           switch-controller-igmp-snooping-proxy: <value in [disable, enable]>
           switch-controller-rspan-mode: <value in [disable, enable]>
           bandwidth-measure-time: <value of integer>
           ip-managed-by-fortiipam: <value in [disable, enable]>
           managed-subnetwork-size: <value in [256, 512, 1024, ...]>
           measured-downstream-bandwidth: <value of integer>
           measured-upstream-bandwidth: <value of integer>
           monitor-bandwidth: <value in [disable, enable]>
           swc-vlan: <value of integer>
           switch-controller-feature: <value in [none, default-vlan, quarantine, ...]>
           switch-controller-mgmt-vlan: <value of integer>
           switch-controller-nac: <value of string>
           vlan-protocol: <value in [8021q, 8021ad]>
           dhcp-relay-interface: <value of string>
           dhcp-relay-interface-select-method: <value in [auto, sdwan, specify]>
           np-qos-profile: <value of integer>
           swc-first-create: <value of integer>
           switch-controller-iot-scanning: <value in [disable, enable]>
           switch-controller-source-ip: <value in [outbound, fixed]>
           dhcp-relay-request-all-server: <value in [disable, enable]>
           stp-ha-secondary: <value in [disable, enable, priority-adjust]>
           switch-controller-dynamic: <value of string>
           auth-cert: <value of string>
           auth-portal-addr: <value of string>
           dhcp-classless-route-addition: <value in [disable, enable]>
           dhcp-relay-link-selection: <value of string>
           dns-server-protocol:
             - cleartext
             - dot
             - doh
           eap-ca-cert: <value of string>
           eap-identity: <value of string>
           eap-method: <value in [tls, peap]>
           eap-password: <value of string>
           eap-supplicant: <value in [disable, enable]>
           eap-user-cert: <value of string>
           ike-saml-server: <value of string>
           lacp-ha-secondary: <value in [disable, enable]>
           pvc-atm-qos: <value in [cbr, rt-vbr, nrt-vbr]>
           pvc-chan: <value of integer>
           pvc-crc: <value of integer>
           pvc-pcr: <value of integer>
           pvc-scr: <value of integer>
           pvc-vlan-id: <value of integer>
           pvc-vlan-rx-id: <value of integer>
           pvc-vlan-rx-op: <value in [pass-through, replace, remove]>
           pvc-vlan-tx-id: <value of integer>
           pvc-vlan-tx-op: <value in [pass-through, replace, remove]>
           reachable-time: <value of integer>
           select-profile-30a-35b: <value in [30A, 35B]>
           sfp-dsl: <value in [disable, enable]>
           sfp-dsl-adsl-fallback: <value in [disable, enable]>
           sfp-dsl-autodetect: <value in [disable, enable]>
           sfp-dsl-mac: <value of string>
           sw-algorithm: <value in [l2, l3, eh]>
           system-id: <value of string>
           system-id-type: <value in [auto, user]>
           vlan-id: <value of integer>
           vlan-op-mode: <value in [tag, untag, passthrough]>
```

## [Return Values](fmgr_fsp_vlan_interface_module.md#id5)

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
