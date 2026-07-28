---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_npu module – Configure NPU attributes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_npu_module.html
fetched_at: 2026-07-28T02:19:17+00:00
---
# fortinet.fortimanager.fmgr_system_npu module – Configure NPU attributes.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_npu`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_system_npu_module.md#synopsis)
- [Parameters](fmgr_system_npu_module.md#parameters)
- [Notes](fmgr_system_npu_module.md#notes)
- [Examples](fmgr_system_npu_module.md#examples)
- [Return Values](fmgr_system_npu_module.md#return-values)

## [Synopsis](fmgr_system_npu_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_npu_module.md#id2)

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
| **system_npu**  dictionary | the top level parameters set |
| **background-sse-scan**  dictionary | no description |
| **scan**  string | Enable/disable background SSE scan by driver thread  **Choices:**   - `"disable"` - `"enable"` |
| **scan-stale**  integer | Configure scanning of active or stale sessions |
| **scan-vt**  integer | Select version/type to scan |
| **stats-qual-access**  integer | Statistics update access qualification in seconds |
| **stats-qual-duration**  integer | Statistics update duration qualification in seconds |
| **stats-update-interval**  integer | Stats update interval |
| **udp-keepalive-interval**  integer | UDP keepalive interval |
| **udp-qual-access**  integer | UDP keepalive access qualification in seconds |
| **udp-qual-duration**  integer | UDP keepalive duration qualification in seconds |
| **capwap-offload**  string | Enable/disable offloading managed FortiAP and FortiLink CAPWAP sessions.  **Choices:**   - `"disable"` - `"enable"` |
| **dedicated-management-affinity**  string | Affinity setting for management deamons |
| **dedicated-management-cpu**  string | Enable to dedicate one CPU for GUI and CLI connections when NPs are busy.  **Choices:**   - `"disable"` - `"enable"` |
| **dedicated-tx-npu**  string | Enable/disable dedication of 3rd NPU for slow path TX.  **Choices:**   - `"disable"` - `"enable"` |
| **default-qos-type**  string | Set default QoS type.  **Choices:**   - `"policing"` - `"shaping"` - `"policing-enhanced"` |
| **default-tcp-refresh-dir**  string | Default SSE timeout TCP refresh direction.  **Choices:**   - `"both"` - `"outgoing"` - `"incoming"` |
| **default-udp-refresh-dir**  string | Default SSE timeout UDP refresh direction.  **Choices:**   - `"both"` - `"outgoing"` - `"incoming"` |
| **dos-options**  dictionary | no description |
| **npu-dos-meter-mode**  string | Set DoS meter NPU offloading mode.  **Choices:**   - `"local"` - `"global"` |
| **npu-dos-synproxy-mode**  string | Set NPU DoS SYNPROXY mode.  **Choices:**   - `"synack2ack"` - `"pass-synack"` |
| **npu-dos-tpe-mode**  string | Enable/disable insertion of DoS meter ID to session table.  **Choices:**   - `"disable"` - `"enable"` |
| **double-level-mcast-offload**  string | Enable double level mcast offload.  **Choices:**   - `"disable"` - `"enable"` |
| **dse-timeout**  integer | DSE timeout in seconds |
| **dsw-dts-profile**  list / elements=dictionary | no description |
| **action**  string | Set NPU DSW DTS profile action.  **Choices:**   - `"wait"` - `"drop"` - `"drop_tmr_0"` - `"drop_tmr_1"` - `"enque"` - `"enque_0"` - `"enque_1"` |
| **min-limit**  integer | Set NPU DSW DTS profile min-limt. |
| **profile-id**  integer | Set NPU DSW DTS profile profile id. |
| **step**  integer | Set NPU DSW DTS profile step. |
| **dsw-queue-dts-profile**  list / elements=dictionary | no description |
| **iport**  string | Set NPU DSW DTS in port.  **Choices:**   - `"EIF0"` - `"eif0"` - `"EIF1"` - `"eif1"` - `"EIF2"` - `"eif2"` - `"EIF3"` - `"eif3"` - `"EIF4"` - `"eif4"` - `"EIF5"` - `"eif5"` - `"EIF6"` - `"eif6"` - `"EIF7"` - `"eif7"` - `"HTX0"` - `"htx0"` - `"HTX1"` - `"htx1"` - `"SSE0"` - `"sse0"` - `"SSE1"` - `"sse1"` - `"SSE2"` - `"sse2"` - `"SSE3"` - `"sse3"` - `"RLT"` - `"rlt"` - `"DFR"` - `"dfr"` - `"IPSECI"` - `"ipseci"` - `"IPSECO"` - `"ipseco"` - `"IPTI"` - `"ipti"` - `"IPTO"` - `"ipto"` - `"VEP0"` - `"vep0"` - `"VEP2"` - `"vep2"` - `"VEP4"` - `"vep4"` - `"VEP6"` - `"vep6"` - `"IVS"` - `"ivs"` - `"L2TI1"` - `"l2ti1"` - `"L2TO"` - `"l2to"` - `"L2TI0"` - `"l2ti0"` - `"PLE"` - `"ple"` - `"SPATH"` - `"spath"` - `"QTM"` - `"qtm"` |
| **name**  string | Name. |
| **oport**  string | Set NPU DSW DTS out port.  **Choices:**   - `"EIF0"` - `"eif0"` - `"EIF1"` - `"eif1"` - `"EIF2"` - `"eif2"` - `"EIF3"` - `"eif3"` - `"EIF4"` - `"eif4"` - `"EIF5"` - `"eif5"` - `"EIF6"` - `"eif6"` - `"EIF7"` - `"eif7"` - `"HRX"` - `"hrx"` - `"SSE0"` - `"sse0"` - `"SSE1"` - `"sse1"` - `"SSE2"` - `"sse2"` - `"SSE3"` - `"sse3"` - `"RLT"` - `"rlt"` - `"DFR"` - `"dfr"` - `"IPSECI"` - `"ipseci"` - `"IPSECO"` - `"ipseco"` - `"IPTI"` - `"ipti"` - `"IPTO"` - `"ipto"` - `"VEP0"` - `"vep0"` - `"VEP2"` - `"vep2"` - `"VEP4"` - `"vep4"` - `"VEP6"` - `"vep6"` - `"IVS"` - `"ivs"` - `"L2TI1"` - `"l2ti1"` - `"L2TO"` - `"l2to"` - `"L2TI0"` - `"l2ti0"` - `"PLE"` - `"ple"` - `"SYNK"` - `"sync"` - `"NSS"` - `"nss"` - `"TSK"` - `"tsk"` - `"QTM"` - `"qtm"` - `"l2tO"` |
| **profile-id**  integer | Set NPU DSW DTS profile ID. |
| **queue-select**  integer | Set NPU DSW DTS queue ID select |
| **fastpath**  string | Enable/disable NP6 offloading  **Choices:**   - `"disable"` - `"enable"` |
| **fp-anomaly**  dictionary | no description |
| **capwap-minlen-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **esp-minlen-err**  string | Invalid IPv4 ESP short packet anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **gre-csum-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **gtpu-plen-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **icmp-csum-err**  string | Invalid IPv4 ICMP packet checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **icmp-frag**  string | Layer 3 fragmented packets that could be part of layer 4 ICMP anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **icmp-land**  string | ICMP land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **icmp-minlen-err**  string | Invalid IPv4 ICMP short packet anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4-csum-err**  string | Invalid IPv4 packet checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4-ihl-err**  string | Invalid IPv4 header length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4-land**  string | Land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-len-err**  string | Invalid IPv4 packet length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4-opt-err**  string | Invalid IPv4 option parsing anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4-optlsrr**  string | Loose source record route option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-optrr**  string | Record route option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-optsecurity**  string | Security option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-optssrr**  string | Strict source record route option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-optstream**  string | Stream option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-opttimestamp**  string | Timestamp option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-proto-err**  string | Invalid layer 4 protocol anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-ttlzero-err**  string | Invalid IPv4 TTL field zero anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv4-unknopt**  string | Unknown option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv4-ver-err**  string | Invalid IPv4 header version anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv6-daddr-err**  string | Destination address as unspecified or loopback address anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-exthdr-len-err**  string | Invalid IPv6 packet chain extension header total length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv6-exthdr-order-err**  string | Invalid IPv6 packet extension header ordering anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv6-ihl-err**  string | Invalid IPv6 packet length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv6-land**  string | Land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-optendpid**  string | End point identification anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-opthomeaddr**  string | Home address option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-optinvld**  string | Invalid option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-optjumbo**  string | Jumbo options anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-optnsap**  string | Network service access point address option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-optralert**  string | Router alert option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-opttunnel**  string | Tunnel encapsulation limit option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-plen-zero**  string | Invalid IPv6 packet payload length zero anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **ipv6-proto-err**  string | Layer 4 invalid protocol anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-saddr-err**  string | Source address as multicast anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-unknopt**  string | Unknown option anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **ipv6-ver-err**  string | Invalid IPv6 packet version anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **nvgre-minlen-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **sctp-clen-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **sctp-crc-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **sctp-l4len-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **tcp-csum-err**  string | Invalid IPv4 TCP packet checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **tcp-fin-noack**  string | TCP SYN flood with FIN flag set without ACK setting anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp-fin-only**  string | TCP SYN flood with only FIN flag set anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp-hlen-err**  string | Invalid IPv4 TCP header length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **tcp-hlenvsl4len-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **tcp-land**  string | TCP land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp-no-flag**  string | TCP SYN flood with no flag set anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp-plen-err**  string | Invalid IPv4 TCP packet length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **tcp-syn-data**  string | TCP SYN flood packets with data anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp-syn-fin**  string | TCP SYN flood SYN/FIN flag set anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **tcp-winnuke**  string | TCP WinNuke anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **udp-csum-err**  string | Invalid IPv4 UDP packet checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **udp-hlen-err**  string | Invalid IPv4 UDP packet header length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **udp-land**  string | UDP land anomalies.  **Choices:**   - `"allow"` - `"drop"` - `"trap-to-host"` |
| **udp-len-err**  string | Invalid IPv4 UDP packet length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **udp-plen-err**  string | Invalid IPv4 UDP packet minimum length anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **udplite-cover-err**  string | Invalid IPv4 UDP-Lite packet coverage anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **udplite-csum-err**  string | Invalid IPv4 UDP-Lite packet checksum anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **uesp-minlen-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **unknproto-minlen-err**  string | Invalid IPv4 L4 unknown protocol short packet anomalies.  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **vxlan-minlen-err**  string | no description  **Choices:**   - `"drop"` - `"trap-to-host"` |
| **gtp-enhanced-cpu-range**  string | GTP enhanced CPU range option.  **Choices:**   - `"0"` - `"1"` - `"2"` |
| **gtp-enhanced-mode**  string | Enable/disable GTP enhanced mode.  **Choices:**   - `"disable"` - `"enable"` |
| **gtp-support**  string | Enable/Disable NP7 GTP support  **Choices:**   - `"disable"` - `"enable"` |
| **hash-config**  string | Configure NPU trunk hash.  **Choices:**   - `"5-tuple"` - `"src-ip"` - `"src-dst-ip"` |
| **hash-ipv6-sel**  integer | Select which 4bytes of the IPv6 address are used for traffic hash |
| **hash-tbl-spread**  string | Enable/disable hash table entry spread  **Choices:**   - `"disable"` - `"enable"` |
| **host-shortcut-mode**  string | Set np6 host shortcut mode.  **Choices:**   - `"bi-directional"` - `"host-shortcut"` |
| **hpe**  dictionary | no description |
| **all-protocol**  integer | Maximum packet rate of each host queue except high priority traffic |
| **arp-max**  integer | Maximum ARP packet rate |
| **enable-queue-shaper**  string | Enable/Disable NPU host protection engine  **Choices:**   - `"disable"` - `"enable"` |
| **enable-shaper**  string | Enable/Disable NPU Host Protection Engine  **Choices:**   - `"disable"` - `"enable"` |
| **esp-max**  integer | Maximum ESP packet rate |
| **exception-code**  integer | Maximum exception code rate of traffic |
| **fragment-with-sess**  integer | Maximum fragment with session rate of traffic |
| **fragment-without-session**  integer | Maximum fragment without session rate of traffic |
| **high-priority**  integer | Maximum packet rate for high priority traffic packets |
| **icmp-max**  integer | Maximum ICMP packet rate |
| **ip-frag-max**  integer | Maximum fragmented IP packet rate |
| **ip-others-max**  integer | Maximum IP packet rate for other packets |
| **l2-others-max**  integer | Maximum L2 packet rate for L2 packets that are not ARP packets |
| **pri-type-max**  integer | Maximum overflow rate of priority type traffic |
| **queue-shaper-max**  integer | Maximum per queue byte rate of traffic |
| **sctp-max**  integer | Maximum SCTP packet rate |
| **tcp-max**  integer | Maximum TCP packet rate |
| **tcpfin-rst-max**  integer | Maximum TCP carries FIN or RST flags packet rate |
| **tcpsyn-ack-max**  integer | Maximum TCP carries SYN and ACK flags packet rate |
| **tcpsyn-max**  integer | Maximum TCP SYN packet rate |
| **udp-max**  integer | Maximum UDP packet rate |
| **htab-dedi-queue-nr**  integer | Set the number of dedicate queue for hash table messages. |
| **htab-msg-queue**  string | Set hash table message queue mode.  **Choices:**   - `"idle"` - `"data"` - `"dedicated"` |
| **htx-gtse-quota**  string | Configure HTX GTSE quota.  **Choices:**   - `"100Mbps"` - `"200Mbps"` - `"300Mbps"` - `"400Mbps"` - `"500Mbps"` - `"600Mbps"` - `"700Mbps"` - `"800Mbps"` - `"900Mbps"` - `"1Gbps"` - `"2Gbps"` - `"4Gbps"` - `"8Gbps"` - `"10Gbps"` |
| **htx-icmp-csum-chk**  string | Set HTX icmp csum checking mode.  **Choices:**   - `"pass"` - `"drop"` |
| **hw-ha-scan-interval**  integer | HW HA periodical scan interval in seconds |
| **inbound-dscp-copy**  string | Enable/disable copying the DSCP field from outer IP header to inner IP Header.  **Choices:**   - `"disable"` - `"enable"` |
| **inbound-dscp-copy-port**  any | (list) no description |
| **intf-shaping-offload**  string | Enable/disable NPU offload when doing interface-based traffic shaping according to the egress-shaping-profile.  **Choices:**   - `"disable"` - `"enable"` |
| **ip-fragment-offload**  string | Enable/disable NP7 NPU IP fragment offload.  **Choices:**   - `"disable"` - `"enable"` |
| **ip-reassembly**  dictionary | no description |
| **max-timeout**  integer | Maximum timeout value for IP reassembly |
| **min-timeout**  integer | Minimum timeout value for IP reassembly |
| **status**  string | Set IP reassembly processing status.  **Choices:**   - `"disable"` - `"enable"` |
| **iph-rsvd-re-cksum**  string | Enable/disable IP checksum re-calculation for packets with iph.  **Choices:**   - `"disable"` - `"enable"` |
| **ippool-overload-high**  integer | High threshold for overload ippool port reuse |
| **ippool-overload-low**  integer | Low threshold for overload ippool port reuse |
| **ipsec-dec-subengine-mask**  string | IPsec decryption subengine mask |
| **ipsec-enc-subengine-mask**  string | IPsec encryption subengine mask |
| **ipsec-host-dfclr**  string | Enable/disable DF clearing of NP4lite host IPsec offload.  **Choices:**   - `"disable"` - `"enable"` |
| **ipsec-inbound-cache**  string | Enable/disable IPsec inbound cache for anti-replay.  **Choices:**   - `"disable"` - `"enable"` |
| **ipsec-local-uesp-port**  integer | no description |
| **ipsec-mtu-override**  string | Enable/disable NP6 IPsec MTU override.  **Choices:**   - `"disable"` - `"enable"` |
| **ipsec-ob-np-sel**  string | IPsec NP selection for OB SA offloading.  **Choices:**   - `"RR"` - `"rr"` - `"Packet"` - `"Hash"` |
| **ipsec-over-vlink**  string | Enable/disable IPSEC over vlink.  **Choices:**   - `"disable"` - `"enable"` |
| **ipsec-STS-timeout**  string | Set NP7Lite IPsec STS msg timeout.  **Choices:**   - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` - `"6"` - `"7"` - `"8"` - `"9"` - `"10"` |
| **ipsec-throughput-msg-frequency**  string | Set NP7Lite IPsec throughput msg frequency  **Choices:**   - `"disable"` - `"32KB"` - `"64KB"` - `"128KB"` - `"256KB"` - `"512KB"` - `"1MB"` - `"2MB"` - `"4MB"` - `"8MB"` - `"16MB"` - `"32MB"` - `"64MB"` - `"128MB"` - `"256MB"` - `"512MB"` - `"1GB"` |
| **ipt-STS-timeout**  string | Set NP7Lite IPT STS msg timeout.  **Choices:**   - `"1"` - `"2"` - `"3"` - `"4"` - `"5"` - `"6"` - `"7"` - `"8"` - `"9"` - `"10"` |
| **ipt-throughput-msg-frequency**  string | Set NP7Lite IPT throughput msg frequency  **Choices:**   - `"disable"` - `"32KB"` - `"64KB"` - `"128KB"` - `"256KB"` - `"512KB"` - `"1MB"` - `"2MB"` - `"4MB"` - `"8MB"` - `"16MB"` - `"32MB"` - `"64MB"` - `"128MB"` - `"256MB"` - `"512MB"` - `"1GB"` |
| **isf-np-queues**  dictionary | no description |
| **cos0**  string | CoS profile name for CoS 0. |
| **cos1**  string | CoS profile name for CoS 1. |
| **cos2**  string | CoS profile name for CoS 2. |
| **cos3**  string | CoS profile name for CoS 3. |
| **cos4**  string | CoS profile name for CoS 4. |
| **cos5**  string | CoS profile name for CoS 5. |
| **cos6**  string | CoS profile name for CoS 6. |
| **cos7**  string | CoS profile name for CoS 7. |
| **isf-np-rx-tr-distr**  string | Select ISF NP Rx trunk distribution  **Choices:**   - `"port-flow"` - `"round-robin"` - `"randomized"` |
| **lag-out-port-select**  string | Enable/disable LAG outgoing port selection based on incoming traffic port.  **Choices:**   - `"disable"` - `"enable"` |
| **max-session-timeout**  integer | Maximum time interval for refreshing NPU-offloaded sessions |
| **mcast-session-accounting**  string | Enable/disable traffic accounting for each multicast session through TAE counter.  **Choices:**   - `"disable"` - `"session-based"` - `"tpe-based"` |
| **mcast-session-counting**  string | no description  **Choices:**   - `"disable"` - `"enable"` - `"session-based"` - `"tpe-based"` |
| **mcast-session-counting6**  string | Enable/disable traffic accounting for each multicast session6 through TAE counter.  **Choices:**   - `"disable"` - `"enable"` - `"session-based"` - `"tpe-based"` |
| **napi-break-interval**  integer | NAPI break interval |
| **nat46-force-ipv4-packet-forwarding**  string | Enable/disable mandatory IPv4 packet forwarding in nat46.  **Choices:**   - `"disable"` - `"enable"` |
| **np-queues**  dictionary | no description |
| **ethernet-type**  list / elements=dictionary | no description |
| **name**  string | Ethernet Type Name. |
| **queue**  integer | Queue Number. |
| **type**  integer | Ethernet Type. |
| **weight**  integer | Class Weight. |
| **ip-protocol**  list / elements=dictionary | no description |
| **name**  string | IP Protocol Name. |
| **protocol**  integer | IP Protocol. |
| **queue**  integer | Queue Number. |
| **weight**  integer | Class Weight. |
| **ip-service**  list / elements=dictionary | no description |
| **dport**  integer | Destination port. |
| **name**  string | IP service name. |
| **protocol**  integer | IP protocol. |
| **queue**  integer | Queue number. |
| **sport**  integer | Source port. |
| **weight**  integer | Class weight. |
| **profile**  list / elements=dictionary | no description |
| **cos0**  string | Queue number of CoS 0.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos1**  string | Queue number of CoS 1.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos2**  string | Queue number of CoS 2.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos3**  string | Queue number of CoS 3.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos4**  string | Queue number of CoS 4.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos5**  string | Queue number of CoS 5.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos6**  string | Queue number of CoS 6.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **cos7**  string | Queue number of CoS 7.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp0**  string | Queue number of DSCP 0.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp1**  string | Queue number of DSCP 1.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp10**  string | Queue number of DSCP 10.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp11**  string | Queue number of DSCP 11.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp12**  string | Queue number of DSCP 12.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp13**  string | Queue number of DSCP 13.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp14**  string | Queue number of DSCP 14.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp15**  string | Queue number of DSCP 15.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp16**  string | Queue number of DSCP 16.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp17**  string | Queue number of DSCP 17.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp18**  string | Queue number of DSCP 18.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp19**  string | Queue number of DSCP 19.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp2**  string | Queue number of DSCP 2.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp20**  string | Queue number of DSCP 20.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp21**  string | Queue number of DSCP 21.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp22**  string | Queue number of DSCP 22.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp23**  string | Queue number of DSCP 23.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp24**  string | Queue number of DSCP 24.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp25**  string | Queue number of DSCP 25.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp26**  string | Queue number of DSCP 26.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp27**  string | Queue number of DSCP 27.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp28**  string | Queue number of DSCP 28.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp29**  string | Queue number of DSCP 29.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp3**  string | Queue number of DSCP 3.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp30**  string | Queue number of DSCP 30.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp31**  string | Queue number of DSCP 31.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp32**  string | Queue number of DSCP 32.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp33**  string | Queue number of DSCP 33.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp34**  string | Queue number of DSCP 34.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp35**  string | Queue number of DSCP 35.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp36**  string | Queue number of DSCP 36.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp37**  string | Queue number of DSCP 37.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp38**  string | Queue number of DSCP 38.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp39**  string | Queue number of DSCP 39.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp4**  string | Queue number of DSCP 4.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp40**  string | Queue number of DSCP 40.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp41**  string | Queue number of DSCP 41.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp42**  string | Queue number of DSCP 42.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp43**  string | Queue number of DSCP 43.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp44**  string | Queue number of DSCP 44.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp45**  string | Queue number of DSCP 45.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp46**  string | Queue number of DSCP 46.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp47**  string | Queue number of DSCP 47.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp48**  string | Queue number of DSCP 48.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp49**  string | Queue number of DSCP 49.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp5**  string | Queue number of DSCP 5.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp50**  string | Queue number of DSCP 50.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp51**  string | Queue number of DSCP 51.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp52**  string | Queue number of DSCP 52.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp53**  string | Queue number of DSCP 53.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp54**  string | Queue number of DSCP 54.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp55**  string | Queue number of DSCP 55.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp56**  string | Queue number of DSCP 56.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp57**  string | Queue number of DSCP 57.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp58**  string | Queue number of DSCP 58.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp59**  string | Queue number of DSCP 59.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp6**  string | Queue number of DSCP 6.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp60**  string | Queue number of DSCP 60.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp61**  string | Queue number of DSCP 61.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp62**  string | Queue number of DSCP 62.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp63**  string | Queue number of DSCP 63.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp7**  string | Queue number of DSCP 7.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp8**  string | Queue number of DSCP 8.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **dscp9**  string | Queue number of DSCP 9.  **Choices:**   - `"queue0"` - `"queue1"` - `"queue2"` - `"queue3"` - `"queue4"` - `"queue5"` - `"queue6"` - `"queue7"` |
| **id**  integer | Profile ID. |
| **type**  string | Profile type.  **Choices:**   - `"cos"` - `"dscp"` |
| **weight**  integer | Class weight. |
| **scheduler**  list / elements=dictionary | no description |
| **mode**  string | Scheduler mode.  **Choices:**   - `"none"` - `"priority"` - `"round-robin"` |
| **name**  string | Scheduler name. |
| **np6-cps-optimization-mode**  string | Enable/disable NP6 connection per second  **Choices:**   - `"disable"` - `"enable"` |
| **npu-group-effective-scope**  integer | npu-group-effective-scope defines under which npu-group cmds such as list/purge will be excecuted. |
| **pba-eim**  string | Configure option for PBA  **Choices:**   - `"disallow"` - `"allow"` |
| **per-policy-accounting**  string | Set per-policy accounting.  **Choices:**   - `"disable"` - `"enable"` |
| **per-session-accounting**  string | Enable/disable per-session accounting.  **Choices:**   - `"enable"` - `"disable"` - `"enable-by-log"` - `"all-enable"` - `"traffic-log-only"` |
| **ple-non-syn-tcp-action**  string | Configure action for the PLE to take on TCP packets that have the SYN field unset.  **Choices:**   - `"forward"` - `"drop"` |
| **policy-offload-level**  string | Configure firewall policy offload level  **Choices:**   - `"disable"` - `"dos-offload"` - `"full-offload"` |
| **port-cpu-map**  list / elements=dictionary | no description |
| **cpu-core**  string | The CPU core to map to an interface. |
| **interface**  string | The interface to map to a CPU core. |
| **port-npu-map**  list / elements=dictionary | no description |
| **interface**  string | Set npu interface port to NPU group map. |
| **npu-group-index**  integer | Mapping NPU group index. |
| **port-path-option**  dictionary | no description |
| **ports-using-npu**  any | (list) no description |
| **priority-protocol**  dictionary | no description |
| **bfd**  string | Enable/disable NPU BFD priority protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **bgp**  string | Enable/disable NPU BGP priority protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **slbc**  string | Enable/disable NPU SLBC priority protocol.  **Choices:**   - `"disable"` - `"enable"` |
| **process-icmp-by-host**  string | Enable/disable process ICMP by host when received from IPsec tunnel and payload size  **Choices:**   - `"disable"` - `"enable"` |
| **prp-port-in**  any | (list or str) no description |
| **prp-port-out**  any | (list or str) no description |
| **prp-session-clear-mode**  string | PRP session clear mode for excluded ip sessions.  **Choices:**   - `"blocking"` - `"non-blocking"` - `"do-not-clear"` |
| **qos-mode**  string | QoS mode on switch and NP.  **Choices:**   - `"disable"` - `"priority"` - `"round-robin"` |
| **qtm-buf-mode**  string | QTM channel configuration for packet buffer.  **Choices:**   - `"6ch"` - `"4ch"` |
| **rdp-offload**  string | Enable/disable rdp offload.  **Choices:**   - `"disable"` - `"enable"` |
| **recover-np6-link**  string | Enable/disable internal link failure check and recovery after boot up.  **Choices:**   - `"disable"` - `"enable"` |
| **rps-mode**  string | Enable/disable receive packet steering  **Choices:**   - `"disable"` - `"enable"` |
| **session-acct-interval**  integer | Session accounting update interval |
| **session-denied-offload**  string | Enable/disable offloading of denied sessions.  **Choices:**   - `"disable"` - `"enable"` |
| **shaping-stats**  string | Enable/disable NP7 traffic shaping statistics  **Choices:**   - `"disable"` - `"enable"` |
| **sse-backpressure**  string | Enable/disable sse backpressure.  **Choices:**   - `"disable"` - `"enable"` |
| **sse-ha-scan**  dictionary | no description |
| **gap**  integer | Scanning message gap |
| **max-session-cnt**  integer | If the session count |
| **min-duration**  integer | Scanning filter for minimum duration of the session. |
| **strip-clear-text-padding**  string | Enable/disable stripping clear text padding.  **Choices:**   - `"disable"` - `"enable"` |
| **strip-esp-padding**  string | Enable/disable stripping ESP padding.  **Choices:**   - `"disable"` - `"enable"` |
| **sw-eh-hash**  dictionary | no description |
| **computation**  string | Set hashing computation.  **Choices:**   - `"xor16"` - `"xor8"` - `"xor4"` - `"crc16"` |
| **destination-ip-lower-16**  string | Include/exclude destination IP address lower 16 bits.  **Choices:**   - `"include"` - `"exclude"` |
| **destination-ip-upper-16**  string | Include/exclude destination IP address upper 16 bits.  **Choices:**   - `"include"` - `"exclude"` |
| **destination-port**  string | Include/exclude destination port if TCP/UDP.  **Choices:**   - `"include"` - `"exclude"` |
| **ip-protocol**  string | Include/exclude IP protocol.  **Choices:**   - `"include"` - `"exclude"` |
| **netmask-length**  integer | Network mask length. |
| **source-ip-lower-16**  string | Include/exclude source IP address lower 16 bits.  **Choices:**   - `"include"` - `"exclude"` |
| **source-ip-upper-16**  string | Include/exclude source IP address upper 16 bits.  **Choices:**   - `"include"` - `"exclude"` |
| **source-port**  string | Include/exclude source port if TCP/UDP.  **Choices:**   - `"include"` - `"exclude"` |
| **sw-np-bandwidth**  string | Bandwidth from switch to NP.  **Choices:**   - `"0G"` - `"2G"` - `"4G"` - `"5G"` - `"6G"` - `"7G"` - `"8G"` - `"9G"` |
| **sw-tr-hash**  dictionary | no description |
| **draco15**  string | Enable/disable DRACO15 hashing.  **Choices:**   - `"disable"` - `"enable"` |
| **tcp-udp-port**  string | Include/exclude TCP/UDP source and destination port for unicast trunk traffic.  **Choices:**   - `"include"` - `"exclude"` |
| **switch-np-hash**  string | Switch-NP trunk port selection Criteria.  **Choices:**   - `"src-ip"` - `"dst-ip"` - `"src-dst-ip"` |
| **tcp-rst-timeout**  integer | TCP RST timeout in seconds |
| **tcp-timeout-profile**  list / elements=dictionary | no description |
| **close-wait**  integer | Set close-wait timeout |
| **fin-wait**  integer | Set fin-wait timeout |
| **id**  integer | Timeout profile ID |
| **syn-sent**  integer | Set syn-sent timeout |
| **syn-wait**  integer | Set syn-wait timeout |
| **tcp-idle**  integer | Set TCP establish timeout |
| **time-wait**  integer | Set time-wait timeout |
| **udp-timeout-profile**  list / elements=dictionary | no description |
| **id**  integer | Timeout profile ID |
| **udp-idle**  integer | Set UDP idle timeout |
| **uesp-offload**  string | Enable/disable UDP-encapsulated ESP offload  **Choices:**   - `"disable"` - `"enable"` |
| **ull-port-mode**  string | Set ULL ports speed to 10G/25G  **Choices:**   - `"10G"` - `"25G"` |
| **vlan-lookup-cache**  string | Enable/disable vlan lookup cache  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_npu_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_npu_module.md#id4)

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
    - name: Configure NPU attributes.
      fmgr_system_npu:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        system_npu:
          capwap-offload: <value in [disable, enable]>
          dedicated-management-affinity: <string>
          dedicated-management-cpu: <value in [disable, enable]>
          fastpath: <value in [disable, enable]>
          fp-anomaly:
            esp-minlen-err: <value in [drop, trap-to-host]>
            icmp-csum-err: <value in [drop, trap-to-host]>
            icmp-minlen-err: <value in [drop, trap-to-host]>
            ipv4-csum-err: <value in [drop, trap-to-host]>
            ipv4-ihl-err: <value in [drop, trap-to-host]>
            ipv4-len-err: <value in [drop, trap-to-host]>
            ipv4-opt-err: <value in [drop, trap-to-host]>
            ipv4-ttlzero-err: <value in [drop, trap-to-host]>
            ipv4-ver-err: <value in [drop, trap-to-host]>
            ipv6-exthdr-len-err: <value in [drop, trap-to-host]>
            ipv6-exthdr-order-err: <value in [drop, trap-to-host]>
            ipv6-ihl-err: <value in [drop, trap-to-host]>
            ipv6-plen-zero: <value in [drop, trap-to-host]>
            ipv6-ver-err: <value in [drop, trap-to-host]>
            tcp-csum-err: <value in [drop, trap-to-host]>
            tcp-hlen-err: <value in [drop, trap-to-host]>
            tcp-plen-err: <value in [drop, trap-to-host]>
            udp-csum-err: <value in [drop, trap-to-host]>
            udp-hlen-err: <value in [drop, trap-to-host]>
            udp-len-err: <value in [drop, trap-to-host]>
            udp-plen-err: <value in [drop, trap-to-host]>
            udplite-cover-err: <value in [drop, trap-to-host]>
            udplite-csum-err: <value in [drop, trap-to-host]>
            unknproto-minlen-err: <value in [drop, trap-to-host]>
            tcp-fin-only: <value in [allow, drop, trap-to-host]>
            ipv4-optsecurity: <value in [allow, drop, trap-to-host]>
            ipv6-optralert: <value in [allow, drop, trap-to-host]>
            tcp-syn-fin: <value in [allow, drop, trap-to-host]>
            ipv4-proto-err: <value in [allow, drop, trap-to-host]>
            ipv6-saddr-err: <value in [allow, drop, trap-to-host]>
            icmp-frag: <value in [allow, drop, trap-to-host]>
            ipv4-optssrr: <value in [allow, drop, trap-to-host]>
            ipv6-opthomeaddr: <value in [allow, drop, trap-to-host]>
            udp-land: <value in [allow, drop, trap-to-host]>
            ipv6-optinvld: <value in [allow, drop, trap-to-host]>
            tcp-fin-noack: <value in [allow, drop, trap-to-host]>
            ipv6-proto-err: <value in [allow, drop, trap-to-host]>
            tcp-land: <value in [allow, drop, trap-to-host]>
            ipv4-unknopt: <value in [allow, drop, trap-to-host]>
            ipv4-optstream: <value in [allow, drop, trap-to-host]>
            ipv6-optjumbo: <value in [allow, drop, trap-to-host]>
            icmp-land: <value in [allow, drop, trap-to-host]>
            tcp-winnuke: <value in [allow, drop, trap-to-host]>
            ipv6-daddr-err: <value in [allow, drop, trap-to-host]>
            ipv4-land: <value in [allow, drop, trap-to-host]>
            ipv6-opttunnel: <value in [allow, drop, trap-to-host]>
            tcp-no-flag: <value in [allow, drop, trap-to-host]>
            ipv6-land: <value in [allow, drop, trap-to-host]>
            ipv4-optlsrr: <value in [allow, drop, trap-to-host]>
            ipv4-opttimestamp: <value in [allow, drop, trap-to-host]>
            ipv4-optrr: <value in [allow, drop, trap-to-host]>
            ipv6-optnsap: <value in [allow, drop, trap-to-host]>
            ipv6-unknopt: <value in [allow, drop, trap-to-host]>
            tcp-syn-data: <value in [allow, drop, trap-to-host]>
            ipv6-optendpid: <value in [allow, drop, trap-to-host]>
            gtpu-plen-err: <value in [drop, trap-to-host]>
            vxlan-minlen-err: <value in [drop, trap-to-host]>
            capwap-minlen-err: <value in [drop, trap-to-host]>
            gre-csum-err: <value in [drop, trap-to-host]>
            nvgre-minlen-err: <value in [drop, trap-to-host]>
            sctp-l4len-err: <value in [drop, trap-to-host]>
            tcp-hlenvsl4len-err: <value in [drop, trap-to-host]>
            sctp-crc-err: <value in [drop, trap-to-host]>
            sctp-clen-err: <value in [drop, trap-to-host]>
            uesp-minlen-err: <value in [drop, trap-to-host]>
          gtp-enhanced-cpu-range: <value in [0, 1, 2]>
          gtp-enhanced-mode: <value in [disable, enable]>
          host-shortcut-mode: <value in [bi-directional, host-shortcut]>
          htx-gtse-quota: <value in [100Mbps, 200Mbps, 300Mbps, ...]>
          intf-shaping-offload: <value in [disable, enable]>
          iph-rsvd-re-cksum: <value in [disable, enable]>
          ipsec-dec-subengine-mask: <string>
          ipsec-enc-subengine-mask: <string>
          ipsec-inbound-cache: <value in [disable, enable]>
          ipsec-mtu-override: <value in [disable, enable]>
          ipsec-over-vlink: <value in [disable, enable]>
          isf-np-queues:
            cos0: <string>
            cos1: <string>
            cos2: <string>
            cos3: <string>
            cos4: <string>
            cos5: <string>
            cos6: <string>
            cos7: <string>
          lag-out-port-select: <value in [disable, enable]>
          mcast-session-accounting: <value in [disable, session-based, tpe-based]>
          np6-cps-optimization-mode: <value in [disable, enable]>
          per-session-accounting: <value in [enable, disable, enable-by-log, ...]>
          port-cpu-map:
            -
              cpu-core: <string>
              interface: <string>
          port-npu-map:
            -
              interface: <string>
              npu-group-index: <integer>
          priority-protocol:
            bfd: <value in [disable, enable]>
            bgp: <value in [disable, enable]>
            slbc: <value in [disable, enable]>
          qos-mode: <value in [disable, priority, round-robin]>
          rdp-offload: <value in [disable, enable]>
          recover-np6-link: <value in [disable, enable]>
          session-denied-offload: <value in [disable, enable]>
          sse-backpressure: <value in [disable, enable]>
          strip-clear-text-padding: <value in [disable, enable]>
          strip-esp-padding: <value in [disable, enable]>
          sw-eh-hash:
            computation: <value in [xor16, xor8, xor4, ...]>
            destination-ip-lower-16: <value in [include, exclude]>
            destination-ip-upper-16: <value in [include, exclude]>
            destination-port: <value in [include, exclude]>
            ip-protocol: <value in [include, exclude]>
            netmask-length: <integer>
            source-ip-lower-16: <value in [include, exclude]>
            source-ip-upper-16: <value in [include, exclude]>
            source-port: <value in [include, exclude]>
          sw-np-bandwidth: <value in [0G, 2G, 4G, ...]>
          switch-np-hash: <value in [src-ip, dst-ip, src-dst-ip]>
          uesp-offload: <value in [disable, enable]>
          np-queues:
            ethernet-type:
              -
                name: <string>
                queue: <integer>
                type: <integer>
                weight: <integer>
            ip-protocol:
              -
                name: <string>
                protocol: <integer>
                queue: <integer>
                weight: <integer>
            ip-service:
              -
                dport: <integer>
                name: <string>
                protocol: <integer>
                queue: <integer>
                sport: <integer>
                weight: <integer>
            profile:
              -
                cos0: <value in [queue0, queue1, queue2, ...]>
                cos1: <value in [queue0, queue1, queue2, ...]>
                cos2: <value in [queue0, queue1, queue2, ...]>
                cos3: <value in [queue0, queue1, queue2, ...]>
                cos4: <value in [queue0, queue1, queue2, ...]>
                cos5: <value in [queue0, queue1, queue2, ...]>
                cos6: <value in [queue0, queue1, queue2, ...]>
                cos7: <value in [queue0, queue1, queue2, ...]>
                dscp0: <value in [queue0, queue1, queue2, ...]>
                dscp1: <value in [queue0, queue1, queue2, ...]>
                dscp10: <value in [queue0, queue1, queue2, ...]>
                dscp11: <value in [queue0, queue1, queue2, ...]>
                dscp12: <value in [queue0, queue1, queue2, ...]>
                dscp13: <value in [queue0, queue1, queue2, ...]>
                dscp14: <value in [queue0, queue1, queue2, ...]>
                dscp15: <value in [queue0, queue1, queue2, ...]>
                dscp16: <value in [queue0, queue1, queue2, ...]>
                dscp17: <value in [queue0, queue1, queue2, ...]>
                dscp18: <value in [queue0, queue1, queue2, ...]>
                dscp19: <value in [queue0, queue1, queue2, ...]>
                dscp2: <value in [queue0, queue1, queue2, ...]>
                dscp20: <value in [queue0, queue1, queue2, ...]>
                dscp21: <value in [queue0, queue1, queue2, ...]>
                dscp22: <value in [queue0, queue1, queue2, ...]>
                dscp23: <value in [queue0, queue1, queue2, ...]>
                dscp24: <value in [queue0, queue1, queue2, ...]>
                dscp25: <value in [queue0, queue1, queue2, ...]>
                dscp26: <value in [queue0, queue1, queue2, ...]>
                dscp27: <value in [queue0, queue1, queue2, ...]>
                dscp28: <value in [queue0, queue1, queue2, ...]>
                dscp29: <value in [queue0, queue1, queue2, ...]>
                dscp3: <value in [queue0, queue1, queue2, ...]>
                dscp30: <value in [queue0, queue1, queue2, ...]>
                dscp31: <value in [queue0, queue1, queue2, ...]>
                dscp32: <value in [queue0, queue1, queue2, ...]>
                dscp33: <value in [queue0, queue1, queue2, ...]>
                dscp34: <value in [queue0, queue1, queue2, ...]>
                dscp35: <value in [queue0, queue1, queue2, ...]>
                dscp36: <value in [queue0, queue1, queue2, ...]>
                dscp37: <value in [queue0, queue1, queue2, ...]>
                dscp38: <value in [queue0, queue1, queue2, ...]>
                dscp39: <value in [queue0, queue1, queue2, ...]>
                dscp4: <value in [queue0, queue1, queue2, ...]>
                dscp40: <value in [queue0, queue1, queue2, ...]>
                dscp41: <value in [queue0, queue1, queue2, ...]>
                dscp42: <value in [queue0, queue1, queue2, ...]>
                dscp43: <value in [queue0, queue1, queue2, ...]>
                dscp44: <value in [queue0, queue1, queue2, ...]>
                dscp45: <value in [queue0, queue1, queue2, ...]>
                dscp46: <value in [queue0, queue1, queue2, ...]>
                dscp47: <value in [queue0, queue1, queue2, ...]>
                dscp48: <value in [queue0, queue1, queue2, ...]>
                dscp49: <value in [queue0, queue1, queue2, ...]>
                dscp5: <value in [queue0, queue1, queue2, ...]>
                dscp50: <value in [queue0, queue1, queue2, ...]>
                dscp51: <value in [queue0, queue1, queue2, ...]>
                dscp52: <value in [queue0, queue1, queue2, ...]>
                dscp53: <value in [queue0, queue1, queue2, ...]>
                dscp54: <value in [queue0, queue1, queue2, ...]>
                dscp55: <value in [queue0, queue1, queue2, ...]>
                dscp56: <value in [queue0, queue1, queue2, ...]>
                dscp57: <value in [queue0, queue1, queue2, ...]>
                dscp58: <value in [queue0, queue1, queue2, ...]>
                dscp59: <value in [queue0, queue1, queue2, ...]>
                dscp6: <value in [queue0, queue1, queue2, ...]>
                dscp60: <value in [queue0, queue1, queue2, ...]>
                dscp61: <value in [queue0, queue1, queue2, ...]>
                dscp62: <value in [queue0, queue1, queue2, ...]>
                dscp63: <value in [queue0, queue1, queue2, ...]>
                dscp7: <value in [queue0, queue1, queue2, ...]>
                dscp8: <value in [queue0, queue1, queue2, ...]>
                dscp9: <value in [queue0, queue1, queue2, ...]>
                id: <integer>
                type: <value in [cos, dscp]>
                weight: <integer>
            scheduler:
              -
                mode: <value in [none, priority, round-robin]>
                name: <string>
          udp-timeout-profile:
            -
              id: <integer>
              udp-idle: <integer>
          qtm-buf-mode: <value in [6ch, 4ch]>
          default-qos-type: <value in [policing, shaping, policing-enhanced]>
          tcp-rst-timeout: <integer>
          ipsec-local-uesp-port: <integer>
          htab-dedi-queue-nr: <integer>
          double-level-mcast-offload: <value in [disable, enable]>
          dse-timeout: <integer>
          ippool-overload-low: <integer>
          pba-eim: <value in [disallow, allow]>
          policy-offload-level: <value in [disable, dos-offload, full-offload]>
          max-session-timeout: <integer>
          port-path-option:
            ports-using-npu: <list or string>
          vlan-lookup-cache: <value in [disable, enable]>
          dos-options:
            npu-dos-meter-mode: <value in [local, global]>
            npu-dos-synproxy-mode: <value in [synack2ack, pass-synack]>
            npu-dos-tpe-mode: <value in [disable, enable]>
          hash-tbl-spread: <value in [disable, enable]>
          tcp-timeout-profile:
            -
              close-wait: <integer>
              fin-wait: <integer>
              id: <integer>
              syn-sent: <integer>
              syn-wait: <integer>
              tcp-idle: <integer>
              time-wait: <integer>
          ip-reassembly:
            max-timeout: <integer>
            min-timeout: <integer>
            status: <value in [disable, enable]>
          gtp-support: <value in [disable, enable]>
          htx-icmp-csum-chk: <value in [pass, drop]>
          hpe:
            all-protocol: <integer>
            arp-max: <integer>
            enable-shaper: <value in [disable, enable]>
            esp-max: <integer>
            high-priority: <integer>
            icmp-max: <integer>
            ip-frag-max: <integer>
            ip-others-max: <integer>
            l2-others-max: <integer>
            pri-type-max: <integer>
            sctp-max: <integer>
            tcp-max: <integer>
            tcpfin-rst-max: <integer>
            tcpsyn-ack-max: <integer>
            tcpsyn-max: <integer>
            udp-max: <integer>
            enable-queue-shaper: <value in [disable, enable]>
            exception-code: <integer>
            fragment-with-sess: <integer>
            fragment-without-session: <integer>
            queue-shaper-max: <integer>
          dsw-dts-profile:
            -
              action: <value in [wait, drop, drop_tmr_0, ...]>
              min-limit: <integer>
              profile-id: <integer>
              step: <integer>
          hash-config: <value in [5-tuple, src-ip, src-dst-ip]>
          ipsec-ob-np-sel: <value in [RR, rr, Packet, ...]>
          napi-break-interval: <integer>
          background-sse-scan:
            scan: <value in [disable, enable]>
            stats-update-interval: <integer>
            udp-keepalive-interval: <integer>
            scan-stale: <integer>
            scan-vt: <integer>
            stats-qual-access: <integer>
            stats-qual-duration: <integer>
            udp-qual-access: <integer>
            udp-qual-duration: <integer>
          inbound-dscp-copy-port: <list or string>
          session-acct-interval: <integer>
          htab-msg-queue: <value in [idle, data, dedicated]>
          dsw-queue-dts-profile:
            -
              iport: <value in [EIF0, eif0, EIF1, ...]>
              name: <string>
              oport: <value in [EIF0, eif0, EIF1, ...]>
              profile-id: <integer>
              queue-select: <integer>
          hw-ha-scan-interval: <integer>
          ippool-overload-high: <integer>
          nat46-force-ipv4-packet-forwarding: <value in [disable, enable]>
          prp-port-out: <list or string>
          isf-np-rx-tr-distr: <value in [port-flow, round-robin, randomized]>
          mcast-session-counting6: <value in [disable, enable, session-based, ...]>
          prp-port-in: <list or string>
          rps-mode: <value in [disable, enable]>
          per-policy-accounting: <value in [disable, enable]>
          mcast-session-counting: <value in [disable, enable, session-based, ...]>
          inbound-dscp-copy: <value in [disable, enable]>
          ipsec-host-dfclr: <value in [disable, enable]>
          process-icmp-by-host: <value in [disable, enable]>
          dedicated-tx-npu: <value in [disable, enable]>
          ull-port-mode: <value in [10G, 25G]>
          sse-ha-scan:
            gap: <integer>
            max-session-cnt: <integer>
            min-duration: <integer>
          hash-ipv6-sel: <integer>
          ip-fragment-offload: <value in [disable, enable]>
          ple-non-syn-tcp-action: <value in [forward, drop]>
          npu-group-effective-scope: <integer>
          ipsec-STS-timeout: <value in [1, 2, 3, ...]>
          ipsec-throughput-msg-frequency: <value in [disable, 32KB, 64KB, ...]>
          ipt-STS-timeout: <value in [1, 2, 3, ...]>
          ipt-throughput-msg-frequency: <value in [disable, 32KB, 64KB, ...]>
          prp-session-clear-mode: <value in [blocking, non-blocking, do-not-clear]>
          shaping-stats: <value in [disable, enable]>
          sw-tr-hash:
            draco15: <value in [disable, enable]>
            tcp-udp-port: <value in [include, exclude]>
          default-tcp-refresh-dir: <value in [both, outgoing, incoming]>
          default-udp-refresh-dir: <value in [both, outgoing, incoming]>
```

## [Return Values](fmgr_system_npu_module.md#id5)

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
