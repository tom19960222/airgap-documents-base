---
collection: kernel
version: "6.8"
title: "Family tc netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/tc.html
fetched_at: 2026-08-21T03:49:23+00:00
---
# [Family `tc` netlink specification](tc.md#id61)

Contents

- [Family `tc` netlink specification](tc.md#family-tc-netlink-specification)

  - [Summary](tc.md#summary)
  - [Operations](tc.md#operations)

    - [newqdisc](tc.md#newqdisc)
    - [delqdisc](tc.md#delqdisc)
    - [getqdisc](tc.md#getqdisc)
    - [newtclass](tc.md#newtclass)
    - [deltclass](tc.md#deltclass)
    - [gettclass](tc.md#gettclass)
    - [newtfilter](tc.md#newtfilter)
    - [deltfilter](tc.md#deltfilter)
    - [gettfilter](tc.md#gettfilter)
    - [newchain](tc.md#newchain)
    - [delchain](tc.md#delchain)
    - [getchain](tc.md#getchain)
  - [Multicast groups](tc.md#multicast-groups)
  - [Definitions](tc.md#definitions)

    - [tcmsg](tc.md#tcmsg)
    - [tc-cls-flags](tc.md#tc-cls-flags)
    - [tc-stats](tc.md#tc-stats)
    - [tc-cbs-qopt](tc.md#tc-cbs-qopt)
    - [tc-etf-qopt](tc.md#tc-etf-qopt)
    - [tc-fifo-qopt](tc.md#tc-fifo-qopt)
    - [tc-htb-opt](tc.md#tc-htb-opt)
    - [tc-htb-glob](tc.md#tc-htb-glob)
    - [tc-gred-qopt](tc.md#tc-gred-qopt)
    - [tc-gred-sopt](tc.md#tc-gred-sopt)
    - [tc-hfsc-qopt](tc.md#tc-hfsc-qopt)
    - [tc-mqprio-qopt](tc.md#tc-mqprio-qopt)
    - [tc-multiq-qopt](tc.md#tc-multiq-qopt)
    - [tc-netem-qopt](tc.md#tc-netem-qopt)
    - [tc-plug-qopt](tc.md#tc-plug-qopt)
    - [tc-prio-qopt](tc.md#tc-prio-qopt)
    - [tc-red-qopt](tc.md#tc-red-qopt)
    - [tc-sfb-qopt](tc.md#tc-sfb-qopt)
    - [tc-sfq-qopt-v1](tc.md#tc-sfq-qopt-v1)
    - [tc-tbf-qopt](tc.md#tc-tbf-qopt)
    - [tc-sizespec](tc.md#tc-sizespec)
    - [gnet-estimator](tc.md#gnet-estimator)
  - [Attribute sets](tc.md#attribute-sets)

    - [tc-attrs](tc.md#tc-attrs)

      - [kind (`string`)](tc.md#kind-string)
      - [options (`sub-message`)](tc.md#options-sub-message)
      - [stats (`binary`)](tc.md#stats-binary)
      - [xstats (`binary`)](tc.md#xstats-binary)
      - [rate (`binary`)](tc.md#rate-binary)
      - [fcnt (`u32`)](tc.md#fcnt-u32)
      - [stats2 (`nest`)](tc.md#stats2-nest)
      - [stab (`nest`)](tc.md#stab-nest)
      - [pad (`pad`)](tc.md#pad-pad)
      - [dump-invisible (`flag`)](tc.md#dump-invisible-flag)
      - [chain (`u32`)](tc.md#chain-u32)
      - [hw-offload (`u8`)](tc.md#hw-offload-u8)
      - [ingress-block (`u32`)](tc.md#ingress-block-u32)
      - [egress-block (`u32`)](tc.md#egress-block-u32)
      - [dump-flags (`bitfield32`)](tc.md#dump-flags-bitfield32)
      - [ext-warn-msg (`string`)](tc.md#ext-warn-msg-string)
    - [tc-cake-attrs](tc.md#tc-cake-attrs)

      - [pad (`pad`)](tc.md#id1)
      - [base-rate64 (`u64`)](tc.md#base-rate64-u64)
      - [diffserv-mode (`u32`)](tc.md#diffserv-mode-u32)
      - [atm (`u32`)](tc.md#atm-u32)
      - [flow-mode (`u32`)](tc.md#flow-mode-u32)
      - [overhead (`u32`)](tc.md#overhead-u32)
      - [rtt (`u32`)](tc.md#rtt-u32)
      - [target (`u32`)](tc.md#target-u32)
      - [autorate (`u32`)](tc.md#autorate-u32)
      - [memory (`u32`)](tc.md#memory-u32)
      - [nat (`u32`)](tc.md#nat-u32)
      - [raw (`u32`)](tc.md#raw-u32)
      - [wash (`u32`)](tc.md#wash-u32)
      - [mpu (`u32`)](tc.md#mpu-u32)
      - [ingress (`u32`)](tc.md#ingress-u32)
      - [ack-filter (`u32`)](tc.md#ack-filter-u32)
      - [split-gso (`u32`)](tc.md#split-gso-u32)
      - [fwmark (`u32`)](tc.md#fwmark-u32)
    - [tc-cake-stats-attrs](tc.md#tc-cake-stats-attrs)

      - [pad (`pad`)](tc.md#id2)
      - [capacity-estimate64 (`u64`)](tc.md#capacity-estimate64-u64)
      - [memory-limit (`u32`)](tc.md#memory-limit-u32)
      - [memory-used (`u32`)](tc.md#memory-used-u32)
      - [avg-netoff (`u32`)](tc.md#avg-netoff-u32)
      - [min-netlen (`u32`)](tc.md#min-netlen-u32)
      - [max-netlen (`u32`)](tc.md#max-netlen-u32)
      - [min-adjlen (`u32`)](tc.md#min-adjlen-u32)
      - [max-adjlen (`u32`)](tc.md#max-adjlen-u32)
      - [tin-stats (`binary`)](tc.md#tin-stats-binary)
      - [deficit (`s32`)](tc.md#deficit-s32)
      - [cobalt-count (`u32`)](tc.md#cobalt-count-u32)
      - [dropping (`u32`)](tc.md#dropping-u32)
      - [drop-next-us (`s32`)](tc.md#drop-next-us-s32)
      - [p-drop (`u32`)](tc.md#p-drop-u32)
      - [blue-timer-us (`s32`)](tc.md#blue-timer-us-s32)
    - [tc-cbs-attrs](tc.md#tc-cbs-attrs)

      - [parms (`binary`)](tc.md#parms-binary)
    - [tc-choke-attrs](tc.md#tc-choke-attrs)

      - [parms (`binary`)](tc.md#id3)
      - [stab (`binary`)](tc.md#stab-binary)
      - [max-p (`u32`)](tc.md#max-p-u32)
    - [tc-codel-attrs](tc.md#tc-codel-attrs)

      - [target (`u32`)](tc.md#id4)
      - [limit (`u32`)](tc.md#limit-u32)
      - [interval (`u32`)](tc.md#interval-u32)
      - [ecn (`u32`)](tc.md#ecn-u32)
      - [ce-threshold (`u32`)](tc.md#ce-threshold-u32)
    - [tc-drr-attrs](tc.md#tc-drr-attrs)

      - [quantum (`u32`)](tc.md#quantum-u32)
    - [tc-flower-attrs](tc.md#tc-flower-attrs)

      - [classid (`u32`)](tc.md#classid-u32)
      - [indev (`string`)](tc.md#indev-string)
      - [act (`array-nest`)](tc.md#act-array-nest)
      - [key-eth-dst (`binary`)](tc.md#key-eth-dst-binary)
      - [key-eth-dst-mask (`binary`)](tc.md#key-eth-dst-mask-binary)
      - [key-eth-src (`binary`)](tc.md#key-eth-src-binary)
      - [key-eth-src-mask (`binary`)](tc.md#key-eth-src-mask-binary)
      - [key-eth-type (`u16`)](tc.md#key-eth-type-u16)
      - [key-ip-proto (`u8`)](tc.md#key-ip-proto-u8)
      - [key-ipv4-src (`u32`)](tc.md#key-ipv4-src-u32)
      - [key-ipv4-src-mask (`u32`)](tc.md#key-ipv4-src-mask-u32)
      - [key-ipv4-dst (`u32`)](tc.md#key-ipv4-dst-u32)
      - [key-ipv4-dst-mask (`u32`)](tc.md#key-ipv4-dst-mask-u32)
      - [key-ipv6-src (`binary`)](tc.md#key-ipv6-src-binary)
      - [key-ipv6-src-mask (`binary`)](tc.md#key-ipv6-src-mask-binary)
      - [key-ipv6-dst (`binary`)](tc.md#key-ipv6-dst-binary)
      - [key-ipv6-dst-mask (`binary`)](tc.md#key-ipv6-dst-mask-binary)
      - [key-tcp-src (`u16`)](tc.md#key-tcp-src-u16)
      - [key-tcp-dst (`u16`)](tc.md#key-tcp-dst-u16)
      - [key-udp-src (`u16`)](tc.md#key-udp-src-u16)
      - [key-udp-dst (`u16`)](tc.md#key-udp-dst-u16)
      - [flags (`u32`)](tc.md#flags-u32)
      - [key-vlan-id (`u16`)](tc.md#key-vlan-id-u16)
      - [key-vlan-prio (`u8`)](tc.md#key-vlan-prio-u8)
      - [key-vlan-eth-type (`u16`)](tc.md#key-vlan-eth-type-u16)
      - [key-enc-key-id (`u32`)](tc.md#key-enc-key-id-u32)
      - [key-enc-ipv4-src (`u32`)](tc.md#key-enc-ipv4-src-u32)
      - [key-enc-ipv4-src-mask (`u32`)](tc.md#key-enc-ipv4-src-mask-u32)
      - [key-enc-ipv4-dst (`u32`)](tc.md#key-enc-ipv4-dst-u32)
      - [key-enc-ipv4-dst-mask (`u32`)](tc.md#key-enc-ipv4-dst-mask-u32)
      - [key-enc-ipv6-src (`binary`)](tc.md#key-enc-ipv6-src-binary)
      - [key-enc-ipv6-src-mask (`binary`)](tc.md#key-enc-ipv6-src-mask-binary)
      - [key-enc-ipv6-dst (`binary`)](tc.md#key-enc-ipv6-dst-binary)
      - [key-enc-ipv6-dst-mask (`binary`)](tc.md#key-enc-ipv6-dst-mask-binary)
      - [key-tcp-src-mask (`u16`)](tc.md#key-tcp-src-mask-u16)
      - [key-tcp-dst-mask (`u16`)](tc.md#key-tcp-dst-mask-u16)
      - [key-udp-src-mask (`u16`)](tc.md#key-udp-src-mask-u16)
      - [key-udp-dst-mask (`u16`)](tc.md#key-udp-dst-mask-u16)
      - [key-sctp-src-mask (`u16`)](tc.md#key-sctp-src-mask-u16)
      - [key-sctp-dst-mask (`u16`)](tc.md#key-sctp-dst-mask-u16)
      - [key-sctp-src (`u16`)](tc.md#key-sctp-src-u16)
      - [key-sctp-dst (`u16`)](tc.md#key-sctp-dst-u16)
      - [key-enc-udp-src-port (`u16`)](tc.md#key-enc-udp-src-port-u16)
      - [key-enc-udp-src-port-mask (`u16`)](tc.md#key-enc-udp-src-port-mask-u16)
      - [key-enc-udp-dst-port (`u16`)](tc.md#key-enc-udp-dst-port-u16)
      - [key-enc-udp-dst-port-mask (`u16`)](tc.md#key-enc-udp-dst-port-mask-u16)
      - [key-flags (`u32`)](tc.md#key-flags-u32)
      - [key-flags-mask (`u32`)](tc.md#key-flags-mask-u32)
      - [key-icmpv4-code (`u8`)](tc.md#key-icmpv4-code-u8)
      - [key-icmpv4-code-mask (`u8`)](tc.md#key-icmpv4-code-mask-u8)
      - [key-icmpv4-type (`u8`)](tc.md#key-icmpv4-type-u8)
      - [key-icmpv4-type-mask (`u8`)](tc.md#key-icmpv4-type-mask-u8)
      - [key-icmpv6-code (`u8`)](tc.md#key-icmpv6-code-u8)
      - [key-icmpv6-code-mask (`u8`)](tc.md#key-icmpv6-code-mask-u8)
      - [key-icmpv6-type (`u8`)](tc.md#key-icmpv6-type-u8)
      - [key-icmpv6-type-mask (`u8`)](tc.md#key-icmpv6-type-mask-u8)
      - [key-arp-sip (`u32`)](tc.md#key-arp-sip-u32)
      - [key-arp-sip-mask (`u32`)](tc.md#key-arp-sip-mask-u32)
      - [key-arp-tip (`u32`)](tc.md#key-arp-tip-u32)
      - [key-arp-tip-mask (`u32`)](tc.md#key-arp-tip-mask-u32)
      - [key-arp-op (`u8`)](tc.md#key-arp-op-u8)
      - [key-arp-op-mask (`u8`)](tc.md#key-arp-op-mask-u8)
      - [key-arp-sha (`binary`)](tc.md#key-arp-sha-binary)
      - [key-arp-sha-mask (`binary`)](tc.md#key-arp-sha-mask-binary)
      - [key-arp-tha (`binary`)](tc.md#key-arp-tha-binary)
      - [key-arp-tha-mask (`binary`)](tc.md#key-arp-tha-mask-binary)
      - [key-mpls-ttl (`u8`)](tc.md#key-mpls-ttl-u8)
      - [key-mpls-bos (`u8`)](tc.md#key-mpls-bos-u8)
      - [key-mpls-tc (`u8`)](tc.md#key-mpls-tc-u8)
      - [key-mpls-label (`u32`)](tc.md#key-mpls-label-u32)
      - [key-tcp-flags (`u16`)](tc.md#key-tcp-flags-u16)
      - [key-tcp-flags-mask (`u16`)](tc.md#key-tcp-flags-mask-u16)
      - [key-ip-tos (`u8`)](tc.md#key-ip-tos-u8)
      - [key-ip-tos-mask (`u8`)](tc.md#key-ip-tos-mask-u8)
      - [key-ip-ttl (`u8`)](tc.md#key-ip-ttl-u8)
      - [key-ip-ttl-mask (`u8`)](tc.md#key-ip-ttl-mask-u8)
      - [key-cvlan-id (`u16`)](tc.md#key-cvlan-id-u16)
      - [key-cvlan-prio (`u8`)](tc.md#key-cvlan-prio-u8)
      - [key-cvlan-eth-type (`u16`)](tc.md#key-cvlan-eth-type-u16)
      - [key-enc-ip-tos (`u8`)](tc.md#key-enc-ip-tos-u8)
      - [key-enc-ip-tos-mask (`u8`)](tc.md#key-enc-ip-tos-mask-u8)
      - [key-enc-ip-ttl (`u8`)](tc.md#key-enc-ip-ttl-u8)
      - [key-enc-ip-ttl-mask (`u8`)](tc.md#key-enc-ip-ttl-mask-u8)
      - [key-enc-opts (`binary`)](tc.md#key-enc-opts-binary)
      - [key-enc-opts-mask (`binary`)](tc.md#key-enc-opts-mask-binary)
      - [in-hw-count (`u32`)](tc.md#in-hw-count-u32)
      - [key-port-src-min (`u16`)](tc.md#key-port-src-min-u16)
      - [key-port-src-max (`u16`)](tc.md#key-port-src-max-u16)
      - [key-port-dst-min (`u16`)](tc.md#key-port-dst-min-u16)
      - [key-port-dst-max (`u16`)](tc.md#key-port-dst-max-u16)
      - [key-ct-state (`u16`)](tc.md#key-ct-state-u16)
      - [key-ct-state-mask (`u16`)](tc.md#key-ct-state-mask-u16)
      - [key-ct-zone (`u16`)](tc.md#key-ct-zone-u16)
      - [key-ct-zone-mask (`u16`)](tc.md#key-ct-zone-mask-u16)
      - [key-ct-mark (`u32`)](tc.md#key-ct-mark-u32)
      - [key-ct-mark-mask (`u32`)](tc.md#key-ct-mark-mask-u32)
      - [key-ct-labels (`binary`)](tc.md#key-ct-labels-binary)
      - [key-ct-labels-mask (`binary`)](tc.md#key-ct-labels-mask-binary)
      - [key-mpls-opts (`binary`)](tc.md#key-mpls-opts-binary)
      - [key-hash (`u32`)](tc.md#key-hash-u32)
      - [key-hash-mask (`u32`)](tc.md#key-hash-mask-u32)
      - [key-num-of-vlans (`u8`)](tc.md#key-num-of-vlans-u8)
      - [key-pppoe-sid (`u16`)](tc.md#key-pppoe-sid-u16)
      - [key-ppp-proto (`u16`)](tc.md#key-ppp-proto-u16)
      - [key-l2-tpv3-sid (`u32`)](tc.md#key-l2-tpv3-sid-u32)
    - [tc-gred-attrs](tc.md#tc-gred-attrs)

      - [parms (`binary`)](tc.md#id5)
      - [stab (`binary`)](tc.md#id6)
      - [dps (`binary`)](tc.md#dps-binary)
      - [max-p (`binary`)](tc.md#max-p-binary)
      - [limit (`u32`)](tc.md#id7)
      - [vq-list (`nest`)](tc.md#vq-list-nest)
    - [tca-gred-vq-list-attrs](tc.md#tca-gred-vq-list-attrs)

      - [entry (`nest`)](tc.md#entry-nest)
    - [tca-gred-vq-entry-attrs](tc.md#tca-gred-vq-entry-attrs)

      - [pad (`pad`)](tc.md#id8)
      - [dp (`u32`)](tc.md#dp-u32)
      - [stat-bytes (`u32`)](tc.md#stat-bytes-u32)
      - [stat-packets (`u32`)](tc.md#stat-packets-u32)
      - [stat-backlog (`u32`)](tc.md#stat-backlog-u32)
      - [stat-prob-drop (`u32`)](tc.md#stat-prob-drop-u32)
      - [stat-prob-mark (`u32`)](tc.md#stat-prob-mark-u32)
      - [stat-forced-drop (`u32`)](tc.md#stat-forced-drop-u32)
      - [stat-forced-mark (`u32`)](tc.md#stat-forced-mark-u32)
      - [stat-pdrop (`u32`)](tc.md#stat-pdrop-u32)
      - [stat-other (`u32`)](tc.md#stat-other-u32)
      - [flags (`u32`)](tc.md#id9)
    - [tc-hfsc-attrs](tc.md#tc-hfsc-attrs)

      - [rsc (`binary`)](tc.md#rsc-binary)
      - [fsc (`binary`)](tc.md#fsc-binary)
      - [usc (`binary`)](tc.md#usc-binary)
    - [tc-hhf-attrs](tc.md#tc-hhf-attrs)

      - [backlog-limit (`u32`)](tc.md#backlog-limit-u32)
      - [quantum (`u32`)](tc.md#id10)
      - [hh-flows-limit (`u32`)](tc.md#hh-flows-limit-u32)
      - [reset-timeout (`u32`)](tc.md#reset-timeout-u32)
      - [admit-bytes (`u32`)](tc.md#admit-bytes-u32)
      - [evict-timeout (`u32`)](tc.md#evict-timeout-u32)
      - [non-hh-weight (`u32`)](tc.md#non-hh-weight-u32)
    - [tc-htb-attrs](tc.md#tc-htb-attrs)

      - [parms (`binary`)](tc.md#id11)
      - [init (`binary`)](tc.md#init-binary)
      - [ctab (`binary`)](tc.md#ctab-binary)
      - [rtab (`binary`)](tc.md#rtab-binary)
      - [direct-qlen (`u32`)](tc.md#direct-qlen-u32)
      - [rate64 (`u64`)](tc.md#rate64-u64)
      - [ceil64 (`u64`)](tc.md#ceil64-u64)
      - [pad (`pad`)](tc.md#id12)
      - [offload (`flag`)](tc.md#offload-flag)
    - [tc-act-attrs](tc.md#tc-act-attrs)

      - [kind (`string`)](tc.md#id13)
      - [options (`sub-message`)](tc.md#id14)
      - [index (`u32`)](tc.md#index-u32)
      - [stats (`binary`)](tc.md#id15)
      - [pad (`pad`)](tc.md#id16)
      - [cookie (`binary`)](tc.md#cookie-binary)
      - [flags (`bitfield32`)](tc.md#flags-bitfield32)
      - [hw-stats (`bitfield32`)](tc.md#hw-stats-bitfield32)
      - [used-hw-stats (`bitfield32`)](tc.md#used-hw-stats-bitfield32)
      - [in-hw-count (`u32`)](tc.md#id17)
    - [tc-etf-attrs](tc.md#tc-etf-attrs)

      - [parms (`binary`)](tc.md#id18)
    - [tc-ets-attrs](tc.md#tc-ets-attrs)

      - [nbands (`u8`)](tc.md#nbands-u8)
      - [nstrict (`u8`)](tc.md#nstrict-u8)
      - [quanta (`nest`)](tc.md#quanta-nest)
      - [quanta-band (`u32`)](tc.md#quanta-band-u32)
      - [priomap (`nest`)](tc.md#priomap-nest)
      - [priomap-band (`u8`)](tc.md#priomap-band-u8)
    - [tc-fq-attrs](tc.md#tc-fq-attrs)

      - [plimit (`u32`)](tc.md#plimit-u32)
      - [flow-plimit (`u32`)](tc.md#flow-plimit-u32)
      - [quantum (`u32`)](tc.md#id19)
      - [initial-quantum (`u32`)](tc.md#initial-quantum-u32)
      - [rate-enable (`u32`)](tc.md#rate-enable-u32)
      - [flow-default-rate (`u32`)](tc.md#flow-default-rate-u32)
      - [flow-max-rate (`u32`)](tc.md#flow-max-rate-u32)
      - [buckets-log (`u32`)](tc.md#buckets-log-u32)
      - [flow-refill-delay (`u32`)](tc.md#flow-refill-delay-u32)
      - [orphan-mask (`u32`)](tc.md#orphan-mask-u32)
      - [low-rate-threshold (`u32`)](tc.md#low-rate-threshold-u32)
      - [ce-threshold (`u32`)](tc.md#id20)
      - [timer-slack (`u32`)](tc.md#timer-slack-u32)
      - [horizon (`u32`)](tc.md#horizon-u32)
      - [horizon-drop (`u8`)](tc.md#horizon-drop-u8)
    - [tc-fq-codel-attrs](tc.md#tc-fq-codel-attrs)

      - [target (`u32`)](tc.md#id21)
      - [limit (`u32`)](tc.md#id22)
      - [interval (`u32`)](tc.md#id23)
      - [ecn (`u32`)](tc.md#id24)
      - [flows (`u32`)](tc.md#flows-u32)
      - [quantum (`u32`)](tc.md#id25)
      - [ce-threshold (`u32`)](tc.md#id26)
      - [drop-batch-size (`u32`)](tc.md#drop-batch-size-u32)
      - [memory-limit (`u32`)](tc.md#id27)
      - [ce-threshold-selector (`u8`)](tc.md#ce-threshold-selector-u8)
      - [ce-threshold-mask (`u8`)](tc.md#ce-threshold-mask-u8)
    - [tc-fq-pie-attrs](tc.md#tc-fq-pie-attrs)

      - [limit (`u32`)](tc.md#id28)
      - [flows (`u32`)](tc.md#id29)
      - [target (`u32`)](tc.md#id30)
      - [tupdate (`u32`)](tc.md#tupdate-u32)
      - [alpha (`u32`)](tc.md#alpha-u32)
      - [beta (`u32`)](tc.md#beta-u32)
      - [quantum (`u32`)](tc.md#id31)
      - [memory-limit (`u32`)](tc.md#id32)
      - [ecn-prob (`u32`)](tc.md#ecn-prob-u32)
      - [ecn (`u32`)](tc.md#id33)
      - [bytemode (`u32`)](tc.md#bytemode-u32)
      - [dq-rate-estimator (`u32`)](tc.md#dq-rate-estimator-u32)
    - [tc-netem-attrs](tc.md#tc-netem-attrs)

      - [corr (`binary`)](tc.md#corr-binary)
      - [delay-dist (`binary`)](tc.md#delay-dist-binary)
      - [reorder (`binary`)](tc.md#reorder-binary)
      - [corrupt (`binary`)](tc.md#corrupt-binary)
      - [loss (`binary`)](tc.md#loss-binary)
      - [rate (`binary`)](tc.md#id34)
      - [ecn (`u32`)](tc.md#id35)
      - [rate64 (`u64`)](tc.md#id36)
      - [pad (`u32`)](tc.md#pad-u32)
      - [latency64 (`s64`)](tc.md#latency64-s64)
      - [jitter64 (`s64`)](tc.md#jitter64-s64)
      - [slot (`binary`)](tc.md#slot-binary)
      - [slot-dist (`binary`)](tc.md#slot-dist-binary)
    - [tc-pie-attrs](tc.md#tc-pie-attrs)

      - [target (`u32`)](tc.md#id37)
      - [limit (`u32`)](tc.md#id38)
      - [tupdate (`u32`)](tc.md#id39)
      - [alpha (`u32`)](tc.md#id40)
      - [beta (`u32`)](tc.md#id41)
      - [ecn (`u32`)](tc.md#id42)
      - [bytemode (`u32`)](tc.md#id43)
      - [dq-rate-estimator (`u32`)](tc.md#id44)
    - [tc-qfq-attrs](tc.md#tc-qfq-attrs)

      - [weight (`u32`)](tc.md#weight-u32)
      - [lmax (`u32`)](tc.md#lmax-u32)
    - [tc-red-attrs](tc.md#tc-red-attrs)

      - [parms (`binary`)](tc.md#id45)
      - [stab (`binary`)](tc.md#id46)
      - [max-p (`u32`)](tc.md#id47)
      - [flags (`binary`)](tc.md#flags-binary)
      - [early-drop-block (`u32`)](tc.md#early-drop-block-u32)
      - [mark-block (`u32`)](tc.md#mark-block-u32)
    - [tc-taprio-attrs](tc.md#tc-taprio-attrs)

      - [priomap (`binary`)](tc.md#priomap-binary)
      - [sched-entry-list (`nest`)](tc.md#sched-entry-list-nest)
      - [sched-base-time (`s64`)](tc.md#sched-base-time-s64)
      - [sched-single-entry (`nest`)](tc.md#sched-single-entry-nest)
      - [sched-clockid (`s32`)](tc.md#sched-clockid-s32)
      - [pad (`pad`)](tc.md#id48)
      - [admin-sched (`binary`)](tc.md#admin-sched-binary)
      - [sched-cycle-time (`s64`)](tc.md#sched-cycle-time-s64)
      - [sched-cycle-time-extension (`s64`)](tc.md#sched-cycle-time-extension-s64)
      - [flags (`u32`)](tc.md#id49)
      - [txtime-delay (`u32`)](tc.md#txtime-delay-u32)
      - [tc-entry (`nest`)](tc.md#tc-entry-nest)
    - [tc-taprio-sched-entry-list](tc.md#tc-taprio-sched-entry-list)

      - [entry (`nest`)](tc.md#id50)
    - [tc-taprio-sched-entry](tc.md#tc-taprio-sched-entry)

      - [index (`u32`)](tc.md#id51)
      - [cmd (`u8`)](tc.md#cmd-u8)
      - [gate-mask (`u32`)](tc.md#gate-mask-u32)
      - [interval (`u32`)](tc.md#id52)
    - [tc-taprio-tc-entry-attrs](tc.md#tc-taprio-tc-entry-attrs)

      - [index (`u32`)](tc.md#id53)
      - [max-sdu (`u32`)](tc.md#max-sdu-u32)
      - [fp (`u32`)](tc.md#fp-u32)
    - [tc-tbf-attrs](tc.md#tc-tbf-attrs)

      - [parms (`binary`)](tc.md#id54)
      - [rtab (`binary`)](tc.md#id55)
      - [ptab (`binary`)](tc.md#ptab-binary)
      - [rate64 (`u64`)](tc.md#id56)
      - [prate4 (`u64`)](tc.md#prate4-u64)
      - [burst (`u32`)](tc.md#burst-u32)
      - [pburst (`u32`)](tc.md#pburst-u32)
      - [pad (`pad`)](tc.md#id57)
    - [tca-gact-attrs](tc.md#tca-gact-attrs)

      - [tm (`binary`)](tc.md#tm-binary)
      - [parms (`binary`)](tc.md#id58)
      - [prob (`binary`)](tc.md#prob-binary)
      - [pad (`pad`)](tc.md#id59)
    - [tca-stab-attrs](tc.md#tca-stab-attrs)

      - [base (`binary`)](tc.md#base-binary)
      - [data (`binary`)](tc.md#data-binary)
    - [tca-stats-attrs](tc.md#tca-stats-attrs)

      - [basic (`binary`)](tc.md#basic-binary)
      - [rate-est (`binary`)](tc.md#rate-est-binary)
      - [queue (`binary`)](tc.md#queue-binary)
      - [app (`binary`)](tc.md#app-binary)
      - [rate-est64 (`binary`)](tc.md#rate-est64-binary)
      - [pad (`pad`)](tc.md#id60)
      - [basic-hw (`binary`)](tc.md#basic-hw-binary)
      - [pkt64 (`binary`)](tc.md#pkt64-binary)
  - [Sub-messages](tc.md#sub-messages)

    - [tc-options-msg](tc.md#tc-options-msg)
    - [tc-act-options-msg](tc.md#tc-act-options-msg)
    - [tca-stats-app-msg](tc.md#tca-stats-app-msg)

## [Summary](tc.md#id62)

Netlink raw family for tc qdisc, chain, class and filter configuration over rtnetlink.

## [Operations](tc.md#id63)

### [newqdisc](tc.md#id64)

Create new tc qdisc.

attribute-set
:   tc-attrs

fixed-header
:   tcmsg

do
:   **request**
    :   attributes
        :   [`kind`, `options`, `rate`, `chain`, `ingress-block`, `egress-block`]

### [delqdisc](tc.md#id65)

Delete existing tc qdisc.

attribute-set
:   tc-attrs

fixed-header
:   tcmsg

do
:   **request**

### [getqdisc](tc.md#id66)

Get / dump tc qdisc information.

attribute-set
:   tc-attrs

fixed-header
:   tcmsg

do
:   **request**
    :   attributes
        :   [`dump-invisible`]

    **reply**
    :   attributes
        :   [`kind`, `options`, `stats`, `xstats`, `rate`, `fcnt`, `stats2`, `stab`, `chain`, `ingress-block`, `egress-block`]

### [newtclass](tc.md#id67)

Get / dump tc traffic class information.

attribute-set
:   tc-attrs

fixed-header
:   tcmsg

do
:   **request**
    :   attributes
        :   [`kind`, `options`, `rate`, `chain`, `ingress-block`, `egress-block`]

### [deltclass](tc.md#id68)

Get / dump tc traffic class information.

attribute-set
:   tc-attrs

fixed-header
:   tcmsg

do
:   **request**

### [gettclass](tc.md#id69)

Get / dump tc traffic class information.

attribute-set
:   tc-attrs

fixed-header
:   tcmsg

do
:   **request**

    **reply**
    :   attributes
        :   [`kind`, `options`, `stats`, `xstats`, `rate`, `fcnt`, `stats2`, `stab`, `chain`, `ingress-block`, `egress-block`]

### [newtfilter](tc.md#id70)

Get / dump tc filter information.

attribute-set
:   tc-attrs

fixed-header
:   tcmsg

do
:   **request**
    :   attributes
        :   [`kind`, `options`, `rate`, `chain`, `ingress-block`, `egress-block`]

### [deltfilter](tc.md#id71)

Get / dump tc filter information.

attribute-set
:   tc-attrs

fixed-header
:   tcmsg

do
:   **request**
    :   attributes
        :   [`chain`, `kind`]

### [gettfilter](tc.md#id72)

Get / dump tc filter information.

attribute-set
:   tc-attrs

fixed-header
:   tcmsg

do
:   **request**
    :   attributes
        :   [`chain`, `kind`]

    **reply**
    :   attributes
        :   [`kind`, `options`, `stats`, `xstats`, `rate`, `fcnt`, `stats2`, `stab`, `chain`, `ingress-block`, `egress-block`]

dump
:   **request**
    :   attributes
        :   [`chain`, `dump-flags`]

    **reply**
    :   attributes
        :   [`kind`, `options`, `stats`, `xstats`, `rate`, `fcnt`, `stats2`, `stab`, `chain`, `ingress-block`, `egress-block`]

### [newchain](tc.md#id73)

Get / dump tc chain information.

attribute-set
:   tc-attrs

fixed-header
:   tcmsg

do
:   **request**
    :   attributes
        :   [`kind`, `options`, `rate`, `chain`, `ingress-block`, `egress-block`]

### [delchain](tc.md#id74)

Get / dump tc chain information.

attribute-set
:   tc-attrs

fixed-header
:   tcmsg

do
:   **request**
    :   attributes
        :   [`chain`]

### [getchain](tc.md#id75)

Get / dump tc chain information.

attribute-set
:   tc-attrs

fixed-header
:   tcmsg

do
:   **request**
    :   attributes
        :   [`chain`]

    **reply**
    :   attributes
        :   [`kind`, `options`, `stats`, `xstats`, `rate`, `fcnt`, `stats2`, `stab`, `chain`, `ingress-block`, `egress-block`]

## [Multicast groups](tc.md#id76)

- rtnlgrp-tc

## [Definitions](tc.md#id77)

### [tcmsg](tc.md#id78)

type
:   struct

members
:   family

    pad

    ifindex

    handle

    parent

    info

### [tc-cls-flags](tc.md#id79)

type
:   flags

entries
:   - `skip-hw`
    - `skip-sw`
    - `in-hw`
    - `not-in-nw`
    - `verbose`

### [tc-stats](tc.md#id80)

type
:   struct

members
:   bytes

    packets

    drops

    overlimits

    bps

    pps

    qlen

    backlog

### [tc-cbs-qopt](tc.md#id81)

type
:   struct

members
:   offload

    pad

    hicredit

    locredit

    idleslope

    sendslope

### [tc-etf-qopt](tc.md#id82)

type
:   struct

members
:   delta

    clockid

    flags

### [tc-fifo-qopt](tc.md#id83)

type
:   struct

members
:   limit

### [tc-htb-opt](tc.md#id84)

type
:   struct

members
:   rate

    ceil

    buffer

    cbuffer

    quantum

    level

    prio

### [tc-htb-glob](tc.md#id85)

type
:   struct

members
:   version

    rate2quantum

    defcls

    debug

    direct-pkts

### [tc-gred-qopt](tc.md#id86)

type
:   struct

members
:   limit

    qth-min

    qth-max

    DP

    backlog

    qave

    forced

    early

    other

    pdrop

    Wlog

    Plog

    Scell_log

    prio

    packets

    bytesin

### [tc-gred-sopt](tc.md#id87)

type
:   struct

members
:   DPs

    def_DP

    grio

    flags

    pad

### [tc-hfsc-qopt](tc.md#id88)

type
:   struct

members
:   defcls

### [tc-mqprio-qopt](tc.md#id89)

type
:   struct

members
:   num-tc

    prio-tc-map

    hw

    count

    offset

### [tc-multiq-qopt](tc.md#id90)

type
:   struct

members
:   bands

    max-bands

### [tc-netem-qopt](tc.md#id91)

type
:   struct

members
:   latency

    limit

    loss

    gap

    duplicate

    jitter

### [tc-plug-qopt](tc.md#id92)

type
:   struct

members
:   action

    limit

### [tc-prio-qopt](tc.md#id93)

type
:   struct

members
:   bands

    priomap

### [tc-red-qopt](tc.md#id94)

type
:   struct

members
:   limit

    qth-min

    qth-max

    Wlog

    Plog

    Scell-log

    flags

### [tc-sfb-qopt](tc.md#id95)

type
:   struct

members
:   rehash-interval

    warmup-time

    max

    bin-size

    increment

    decrement

    limit

    penalty-rate

    penalty-burst

### [tc-sfq-qopt-v1](tc.md#id96)

type
:   struct

members
:   quantum

    perturb-period

    limit

    divisor

    flows

    depth

    headdrop

    limit

    qth-min

    qth-mac

    Wlog

    Plog

    Scell-log

    flags

    max-P

    prob-drop

    forced-drop

    prob-mark

    forced-mark

    prob-mark-head

    forced-mark-head

### [tc-tbf-qopt](tc.md#id97)

type
:   struct

members
:   rate

    peakrate

    limit

    buffer

    mtu

### [tc-sizespec](tc.md#id98)

type
:   struct

members
:   cell-log

    size-log

    cell-align

    overhead

    linklayer

    mpu

    mtu

    tsize

### [gnet-estimator](tc.md#id99)

type
:   struct

members
:   interval

    ewma-log

## [Attribute sets](tc.md#id100)

### [tc-attrs](tc.md#id101)

#### [kind (`string`)](tc.md#id102)

#### [options (`sub-message`)](tc.md#id103)

sub-message
:   tc-options-msg

selector
:   kind

#### [stats (`binary`)](tc.md#id104)

struct
:   tc-stats

#### [xstats (`binary`)](tc.md#id105)

#### [rate (`binary`)](tc.md#id106)

struct
:   gnet-estimator

#### [fcnt (`u32`)](tc.md#id107)

#### [stats2 (`nest`)](tc.md#id108)

nested-attributes
:   tca-stats-attrs

#### [stab (`nest`)](tc.md#id109)

nested-attributes
:   tca-stab-attrs

#### [pad (`pad`)](tc.md#id110)

#### [dump-invisible (`flag`)](tc.md#id111)

#### [chain (`u32`)](tc.md#id112)

#### [hw-offload (`u8`)](tc.md#id113)

#### [ingress-block (`u32`)](tc.md#id114)

#### [egress-block (`u32`)](tc.md#id115)

#### [dump-flags (`bitfield32`)](tc.md#id116)

#### [ext-warn-msg (`string`)](tc.md#id117)

### [tc-cake-attrs](tc.md#id118)

#### [pad (`pad`)](tc.md#id119)

#### [base-rate64 (`u64`)](tc.md#id120)

#### [diffserv-mode (`u32`)](tc.md#id121)

#### [atm (`u32`)](tc.md#id122)

#### [flow-mode (`u32`)](tc.md#id123)

#### [overhead (`u32`)](tc.md#id124)

#### [rtt (`u32`)](tc.md#id125)

#### [target (`u32`)](tc.md#id126)

#### [autorate (`u32`)](tc.md#id127)

#### [memory (`u32`)](tc.md#id128)

#### [nat (`u32`)](tc.md#id129)

#### [raw (`u32`)](tc.md#id130)

#### [wash (`u32`)](tc.md#id131)

#### [mpu (`u32`)](tc.md#id132)

#### [ingress (`u32`)](tc.md#id133)

#### [ack-filter (`u32`)](tc.md#id134)

#### [split-gso (`u32`)](tc.md#id135)

#### [fwmark (`u32`)](tc.md#id136)

### [tc-cake-stats-attrs](tc.md#id137)

#### [pad (`pad`)](tc.md#id138)

#### [capacity-estimate64 (`u64`)](tc.md#id139)

#### [memory-limit (`u32`)](tc.md#id140)

#### [memory-used (`u32`)](tc.md#id141)

#### [avg-netoff (`u32`)](tc.md#id142)

#### [min-netlen (`u32`)](tc.md#id143)

#### [max-netlen (`u32`)](tc.md#id144)

#### [min-adjlen (`u32`)](tc.md#id145)

#### [max-adjlen (`u32`)](tc.md#id146)

#### [tin-stats (`binary`)](tc.md#id147)

#### [deficit (`s32`)](tc.md#id148)

#### [cobalt-count (`u32`)](tc.md#id149)

#### [dropping (`u32`)](tc.md#id150)

#### [drop-next-us (`s32`)](tc.md#id151)

#### [p-drop (`u32`)](tc.md#id152)

#### [blue-timer-us (`s32`)](tc.md#id153)

### [tc-cbs-attrs](tc.md#id154)

#### [parms (`binary`)](tc.md#id155)

struct
:   tc-cbs-qopt

### [tc-choke-attrs](tc.md#id156)

#### [parms (`binary`)](tc.md#id157)

struct
:   tc-red-qopt

#### [stab (`binary`)](tc.md#id158)

#### [max-p (`u32`)](tc.md#id159)

### [tc-codel-attrs](tc.md#id160)

#### [target (`u32`)](tc.md#id161)

#### [limit (`u32`)](tc.md#id162)

#### [interval (`u32`)](tc.md#id163)

#### [ecn (`u32`)](tc.md#id164)

#### [ce-threshold (`u32`)](tc.md#id165)

### [tc-drr-attrs](tc.md#id166)

#### [quantum (`u32`)](tc.md#id167)

### [tc-flower-attrs](tc.md#id168)

#### [classid (`u32`)](tc.md#id169)

#### [indev (`string`)](tc.md#id170)

#### [act (`array-nest`)](tc.md#id171)

nested-attributes
:   tc-act-attrs

#### [key-eth-dst (`binary`)](tc.md#id172)

display-hint
:   mac

#### [key-eth-dst-mask (`binary`)](tc.md#id173)

display-hint
:   mac

#### [key-eth-src (`binary`)](tc.md#id174)

display-hint
:   mac

#### [key-eth-src-mask (`binary`)](tc.md#id175)

display-hint
:   mac

#### [key-eth-type (`u16`)](tc.md#id176)

byte-order
:   big-endian

#### [key-ip-proto (`u8`)](tc.md#id177)

#### [key-ipv4-src (`u32`)](tc.md#id178)

byte-order
:   big-endian

display-hint
:   ipv4

#### [key-ipv4-src-mask (`u32`)](tc.md#id179)

byte-order
:   big-endian

display-hint
:   ipv4

#### [key-ipv4-dst (`u32`)](tc.md#id180)

byte-order
:   big-endian

display-hint
:   ipv4

#### [key-ipv4-dst-mask (`u32`)](tc.md#id181)

byte-order
:   big-endian

display-hint
:   ipv4

#### [key-ipv6-src (`binary`)](tc.md#id182)

display-hint
:   ipv6

#### [key-ipv6-src-mask (`binary`)](tc.md#id183)

display-hint
:   ipv6

#### [key-ipv6-dst (`binary`)](tc.md#id184)

display-hint
:   ipv6

#### [key-ipv6-dst-mask (`binary`)](tc.md#id185)

display-hint
:   ipv6

#### [key-tcp-src (`u16`)](tc.md#id186)

byte-order
:   big-endian

#### [key-tcp-dst (`u16`)](tc.md#id187)

byte-order
:   big-endian

#### [key-udp-src (`u16`)](tc.md#id188)

byte-order
:   big-endian

#### [key-udp-dst (`u16`)](tc.md#id189)

byte-order
:   big-endian

#### [flags (`u32`)](tc.md#id190)

enum
:   tc-cls-flags

enum-as-flags
:   True

#### [key-vlan-id (`u16`)](tc.md#id191)

byte-order
:   big-endian

#### [key-vlan-prio (`u8`)](tc.md#id192)

#### [key-vlan-eth-type (`u16`)](tc.md#id193)

byte-order
:   big-endian

#### [key-enc-key-id (`u32`)](tc.md#id194)

byte-order
:   big-endian

#### [key-enc-ipv4-src (`u32`)](tc.md#id195)

byte-order
:   big-endian

display-hint
:   ipv4

#### [key-enc-ipv4-src-mask (`u32`)](tc.md#id196)

byte-order
:   big-endian

display-hint
:   ipv4

#### [key-enc-ipv4-dst (`u32`)](tc.md#id197)

byte-order
:   big-endian

display-hint
:   ipv4

#### [key-enc-ipv4-dst-mask (`u32`)](tc.md#id198)

byte-order
:   big-endian

display-hint
:   ipv4

#### [key-enc-ipv6-src (`binary`)](tc.md#id199)

display-hint
:   ipv6

#### [key-enc-ipv6-src-mask (`binary`)](tc.md#id200)

display-hint
:   ipv6

#### [key-enc-ipv6-dst (`binary`)](tc.md#id201)

display-hint
:   ipv6

#### [key-enc-ipv6-dst-mask (`binary`)](tc.md#id202)

display-hint
:   ipv6

#### [key-tcp-src-mask (`u16`)](tc.md#id203)

byte-order
:   big-endian

#### [key-tcp-dst-mask (`u16`)](tc.md#id204)

byte-order
:   big-endian

#### [key-udp-src-mask (`u16`)](tc.md#id205)

byte-order
:   big-endian

#### [key-udp-dst-mask (`u16`)](tc.md#id206)

byte-order
:   big-endian

#### [key-sctp-src-mask (`u16`)](tc.md#id207)

byte-order
:   big-endian

#### [key-sctp-dst-mask (`u16`)](tc.md#id208)

byte-order
:   big-endian

#### [key-sctp-src (`u16`)](tc.md#id209)

byte-order
:   big-endian

#### [key-sctp-dst (`u16`)](tc.md#id210)

byte-order
:   big-endian

#### [key-enc-udp-src-port (`u16`)](tc.md#id211)

byte-order
:   big-endian

#### [key-enc-udp-src-port-mask (`u16`)](tc.md#id212)

byte-order
:   big-endian

#### [key-enc-udp-dst-port (`u16`)](tc.md#id213)

byte-order
:   big-endian

#### [key-enc-udp-dst-port-mask (`u16`)](tc.md#id214)

byte-order
:   big-endian

#### [key-flags (`u32`)](tc.md#id215)

byte-order
:   big-endian

#### [key-flags-mask (`u32`)](tc.md#id216)

byte-order
:   big-endian

#### [key-icmpv4-code (`u8`)](tc.md#id217)

#### [key-icmpv4-code-mask (`u8`)](tc.md#id218)

#### [key-icmpv4-type (`u8`)](tc.md#id219)

#### [key-icmpv4-type-mask (`u8`)](tc.md#id220)

#### [key-icmpv6-code (`u8`)](tc.md#id221)

#### [key-icmpv6-code-mask (`u8`)](tc.md#id222)

#### [key-icmpv6-type (`u8`)](tc.md#id223)

#### [key-icmpv6-type-mask (`u8`)](tc.md#id224)

#### [key-arp-sip (`u32`)](tc.md#id225)

byte-order
:   big-endian

#### [key-arp-sip-mask (`u32`)](tc.md#id226)

byte-order
:   big-endian

#### [key-arp-tip (`u32`)](tc.md#id227)

byte-order
:   big-endian

#### [key-arp-tip-mask (`u32`)](tc.md#id228)

byte-order
:   big-endian

#### [key-arp-op (`u8`)](tc.md#id229)

#### [key-arp-op-mask (`u8`)](tc.md#id230)

#### [key-arp-sha (`binary`)](tc.md#id231)

#### [key-arp-sha-mask (`binary`)](tc.md#id232)

#### [key-arp-tha (`binary`)](tc.md#id233)

#### [key-arp-tha-mask (`binary`)](tc.md#id234)

#### [key-mpls-ttl (`u8`)](tc.md#id235)

#### [key-mpls-bos (`u8`)](tc.md#id236)

#### [key-mpls-tc (`u8`)](tc.md#id237)

#### [key-mpls-label (`u32`)](tc.md#id238)

byte-order
:   big-endian

#### [key-tcp-flags (`u16`)](tc.md#id239)

byte-order
:   big-endian

#### [key-tcp-flags-mask (`u16`)](tc.md#id240)

byte-order
:   big-endian

#### [key-ip-tos (`u8`)](tc.md#id241)

#### [key-ip-tos-mask (`u8`)](tc.md#id242)

#### [key-ip-ttl (`u8`)](tc.md#id243)

#### [key-ip-ttl-mask (`u8`)](tc.md#id244)

#### [key-cvlan-id (`u16`)](tc.md#id245)

byte-order
:   big-endian

#### [key-cvlan-prio (`u8`)](tc.md#id246)

#### [key-cvlan-eth-type (`u16`)](tc.md#id247)

byte-order
:   big-endian

#### [key-enc-ip-tos (`u8`)](tc.md#id248)

#### [key-enc-ip-tos-mask (`u8`)](tc.md#id249)

#### [key-enc-ip-ttl (`u8`)](tc.md#id250)

#### [key-enc-ip-ttl-mask (`u8`)](tc.md#id251)

#### [key-enc-opts (`binary`)](tc.md#id252)

#### [key-enc-opts-mask (`binary`)](tc.md#id253)

#### [in-hw-count (`u32`)](tc.md#id254)

#### [key-port-src-min (`u16`)](tc.md#id255)

byte-order
:   big-endian

#### [key-port-src-max (`u16`)](tc.md#id256)

byte-order
:   big-endian

#### [key-port-dst-min (`u16`)](tc.md#id257)

byte-order
:   big-endian

#### [key-port-dst-max (`u16`)](tc.md#id258)

byte-order
:   big-endian

#### [key-ct-state (`u16`)](tc.md#id259)

#### [key-ct-state-mask (`u16`)](tc.md#id260)

#### [key-ct-zone (`u16`)](tc.md#id261)

#### [key-ct-zone-mask (`u16`)](tc.md#id262)

#### [key-ct-mark (`u32`)](tc.md#id263)

#### [key-ct-mark-mask (`u32`)](tc.md#id264)

#### [key-ct-labels (`binary`)](tc.md#id265)

#### [key-ct-labels-mask (`binary`)](tc.md#id266)

#### [key-mpls-opts (`binary`)](tc.md#id267)

#### [key-hash (`u32`)](tc.md#id268)

#### [key-hash-mask (`u32`)](tc.md#id269)

#### [key-num-of-vlans (`u8`)](tc.md#id270)

#### [key-pppoe-sid (`u16`)](tc.md#id271)

byte-order
:   big-endian

#### [key-ppp-proto (`u16`)](tc.md#id272)

byte-order
:   big-endian

#### [key-l2-tpv3-sid (`u32`)](tc.md#id273)

byte-order
:   big-endian

### [tc-gred-attrs](tc.md#id274)

#### [parms (`binary`)](tc.md#id275)

#### [stab (`binary`)](tc.md#id276)

sub-type
:   u8

#### [dps (`binary`)](tc.md#id277)

struct
:   tc-gred-sopt

#### [max-p (`binary`)](tc.md#id278)

sub-type
:   u32

#### [limit (`u32`)](tc.md#id279)

#### [vq-list (`nest`)](tc.md#id280)

nested-attributes
:   tca-gred-vq-list-attrs

### [tca-gred-vq-list-attrs](tc.md#id281)

#### [entry (`nest`)](tc.md#id282)

nested-attributes
:   tca-gred-vq-entry-attrs

multi-attr
:   True

### [tca-gred-vq-entry-attrs](tc.md#id283)

#### [pad (`pad`)](tc.md#id284)

#### [dp (`u32`)](tc.md#id285)

#### [stat-bytes (`u32`)](tc.md#id286)

#### [stat-packets (`u32`)](tc.md#id287)

#### [stat-backlog (`u32`)](tc.md#id288)

#### [stat-prob-drop (`u32`)](tc.md#id289)

#### [stat-prob-mark (`u32`)](tc.md#id290)

#### [stat-forced-drop (`u32`)](tc.md#id291)

#### [stat-forced-mark (`u32`)](tc.md#id292)

#### [stat-pdrop (`u32`)](tc.md#id293)

#### [stat-other (`u32`)](tc.md#id294)

#### [flags (`u32`)](tc.md#id295)

### [tc-hfsc-attrs](tc.md#id296)

#### [rsc (`binary`)](tc.md#id297)

#### [fsc (`binary`)](tc.md#id298)

#### [usc (`binary`)](tc.md#id299)

### [tc-hhf-attrs](tc.md#id300)

#### [backlog-limit (`u32`)](tc.md#id301)

#### [quantum (`u32`)](tc.md#id302)

#### [hh-flows-limit (`u32`)](tc.md#id303)

#### [reset-timeout (`u32`)](tc.md#id304)

#### [admit-bytes (`u32`)](tc.md#id305)

#### [evict-timeout (`u32`)](tc.md#id306)

#### [non-hh-weight (`u32`)](tc.md#id307)

### [tc-htb-attrs](tc.md#id308)

#### [parms (`binary`)](tc.md#id309)

struct
:   tc-htb-opt

#### [init (`binary`)](tc.md#id310)

struct
:   tc-htb-glob

#### [ctab (`binary`)](tc.md#id311)

#### [rtab (`binary`)](tc.md#id312)

#### [direct-qlen (`u32`)](tc.md#id313)

#### [rate64 (`u64`)](tc.md#id314)

#### [ceil64 (`u64`)](tc.md#id315)

#### [pad (`pad`)](tc.md#id316)

#### [offload (`flag`)](tc.md#id317)

### [tc-act-attrs](tc.md#id318)

#### [kind (`string`)](tc.md#id319)

#### [options (`sub-message`)](tc.md#id320)

sub-message
:   tc-act-options-msg

selector
:   kind

#### [index (`u32`)](tc.md#id321)

#### [stats (`binary`)](tc.md#id322)

#### [pad (`pad`)](tc.md#id323)

#### [cookie (`binary`)](tc.md#id324)

#### [flags (`bitfield32`)](tc.md#id325)

#### [hw-stats (`bitfield32`)](tc.md#id326)

#### [used-hw-stats (`bitfield32`)](tc.md#id327)

#### [in-hw-count (`u32`)](tc.md#id328)

### [tc-etf-attrs](tc.md#id329)

#### [parms (`binary`)](tc.md#id330)

struct
:   tc-etf-qopt

### [tc-ets-attrs](tc.md#id331)

#### [nbands (`u8`)](tc.md#id332)

#### [nstrict (`u8`)](tc.md#id333)

#### [quanta (`nest`)](tc.md#id334)

nested-attributes
:   tc-ets-attrs

#### [quanta-band (`u32`)](tc.md#id335)

multi-attr
:   True

#### [priomap (`nest`)](tc.md#id336)

nested-attributes
:   tc-ets-attrs

#### [priomap-band (`u8`)](tc.md#id337)

multi-attr
:   True

### [tc-fq-attrs](tc.md#id338)

#### [plimit (`u32`)](tc.md#id339)

#### [flow-plimit (`u32`)](tc.md#id340)

#### [quantum (`u32`)](tc.md#id341)

#### [initial-quantum (`u32`)](tc.md#id342)

#### [rate-enable (`u32`)](tc.md#id343)

#### [flow-default-rate (`u32`)](tc.md#id344)

#### [flow-max-rate (`u32`)](tc.md#id345)

#### [buckets-log (`u32`)](tc.md#id346)

#### [flow-refill-delay (`u32`)](tc.md#id347)

#### [orphan-mask (`u32`)](tc.md#id348)

#### [low-rate-threshold (`u32`)](tc.md#id349)

#### [ce-threshold (`u32`)](tc.md#id350)

#### [timer-slack (`u32`)](tc.md#id351)

#### [horizon (`u32`)](tc.md#id352)

#### [horizon-drop (`u8`)](tc.md#id353)

### [tc-fq-codel-attrs](tc.md#id354)

#### [target (`u32`)](tc.md#id355)

#### [limit (`u32`)](tc.md#id356)

#### [interval (`u32`)](tc.md#id357)

#### [ecn (`u32`)](tc.md#id358)

#### [flows (`u32`)](tc.md#id359)

#### [quantum (`u32`)](tc.md#id360)

#### [ce-threshold (`u32`)](tc.md#id361)

#### [drop-batch-size (`u32`)](tc.md#id362)

#### [memory-limit (`u32`)](tc.md#id363)

#### [ce-threshold-selector (`u8`)](tc.md#id364)

#### [ce-threshold-mask (`u8`)](tc.md#id365)

### [tc-fq-pie-attrs](tc.md#id366)

#### [limit (`u32`)](tc.md#id367)

#### [flows (`u32`)](tc.md#id368)

#### [target (`u32`)](tc.md#id369)

#### [tupdate (`u32`)](tc.md#id370)

#### [alpha (`u32`)](tc.md#id371)

#### [beta (`u32`)](tc.md#id372)

#### [quantum (`u32`)](tc.md#id373)

#### [memory-limit (`u32`)](tc.md#id374)

#### [ecn-prob (`u32`)](tc.md#id375)

#### [ecn (`u32`)](tc.md#id376)

#### [bytemode (`u32`)](tc.md#id377)

#### [dq-rate-estimator (`u32`)](tc.md#id378)

### [tc-netem-attrs](tc.md#id379)

#### [corr (`binary`)](tc.md#id380)

#### [delay-dist (`binary`)](tc.md#id381)

sub-type
:   s16

#### [reorder (`binary`)](tc.md#id382)

#### [corrupt (`binary`)](tc.md#id383)

#### [loss (`binary`)](tc.md#id384)

#### [rate (`binary`)](tc.md#id385)

#### [ecn (`u32`)](tc.md#id386)

#### [rate64 (`u64`)](tc.md#id387)

#### [pad (`u32`)](tc.md#id388)

#### [latency64 (`s64`)](tc.md#id389)

#### [jitter64 (`s64`)](tc.md#id390)

#### [slot (`binary`)](tc.md#id391)

#### [slot-dist (`binary`)](tc.md#id392)

sub-type
:   s16

### [tc-pie-attrs](tc.md#id393)

#### [target (`u32`)](tc.md#id394)

#### [limit (`u32`)](tc.md#id395)

#### [tupdate (`u32`)](tc.md#id396)

#### [alpha (`u32`)](tc.md#id397)

#### [beta (`u32`)](tc.md#id398)

#### [ecn (`u32`)](tc.md#id399)

#### [bytemode (`u32`)](tc.md#id400)

#### [dq-rate-estimator (`u32`)](tc.md#id401)

### [tc-qfq-attrs](tc.md#id402)

#### [weight (`u32`)](tc.md#id403)

#### [lmax (`u32`)](tc.md#id404)

### [tc-red-attrs](tc.md#id405)

#### [parms (`binary`)](tc.md#id406)

struct
:   tc-red-qopt

#### [stab (`binary`)](tc.md#id407)

#### [max-p (`u32`)](tc.md#id408)

#### [flags (`binary`)](tc.md#id409)

#### [early-drop-block (`u32`)](tc.md#id410)

#### [mark-block (`u32`)](tc.md#id411)

### [tc-taprio-attrs](tc.md#id412)

#### [priomap (`binary`)](tc.md#id413)

struct
:   tc-mqprio-qopt

#### [sched-entry-list (`nest`)](tc.md#id414)

nested-attributes
:   tc-taprio-sched-entry-list

#### [sched-base-time (`s64`)](tc.md#id415)

#### [sched-single-entry (`nest`)](tc.md#id416)

nested-attributes
:   tc-taprio-sched-entry

#### [sched-clockid (`s32`)](tc.md#id417)

#### [pad (`pad`)](tc.md#id418)

#### [admin-sched (`binary`)](tc.md#id419)

#### [sched-cycle-time (`s64`)](tc.md#id420)

#### [sched-cycle-time-extension (`s64`)](tc.md#id421)

#### [flags (`u32`)](tc.md#id422)

#### [txtime-delay (`u32`)](tc.md#id423)

#### [tc-entry (`nest`)](tc.md#id424)

nested-attributes
:   tc-taprio-tc-entry-attrs

### [tc-taprio-sched-entry-list](tc.md#id425)

#### [entry (`nest`)](tc.md#id426)

nested-attributes
:   tc-taprio-sched-entry

### [tc-taprio-sched-entry](tc.md#id427)

#### [index (`u32`)](tc.md#id428)

#### [cmd (`u8`)](tc.md#id429)

#### [gate-mask (`u32`)](tc.md#id430)

#### [interval (`u32`)](tc.md#id431)

### [tc-taprio-tc-entry-attrs](tc.md#id432)

#### [index (`u32`)](tc.md#id433)

#### [max-sdu (`u32`)](tc.md#id434)

#### [fp (`u32`)](tc.md#id435)

### [tc-tbf-attrs](tc.md#id436)

#### [parms (`binary`)](tc.md#id437)

struct
:   tc-tbf-qopt

#### [rtab (`binary`)](tc.md#id438)

#### [ptab (`binary`)](tc.md#id439)

#### [rate64 (`u64`)](tc.md#id440)

#### [prate4 (`u64`)](tc.md#id441)

#### [burst (`u32`)](tc.md#id442)

#### [pburst (`u32`)](tc.md#id443)

#### [pad (`pad`)](tc.md#id444)

### [tca-gact-attrs](tc.md#id445)

#### [tm (`binary`)](tc.md#id446)

#### [parms (`binary`)](tc.md#id447)

#### [prob (`binary`)](tc.md#id448)

#### [pad (`pad`)](tc.md#id449)

### [tca-stab-attrs](tc.md#id450)

#### [base (`binary`)](tc.md#id451)

struct
:   tc-sizespec

#### [data (`binary`)](tc.md#id452)

### [tca-stats-attrs](tc.md#id453)

#### [basic (`binary`)](tc.md#id454)

#### [rate-est (`binary`)](tc.md#id455)

#### [queue (`binary`)](tc.md#id456)

#### [app (`binary`)](tc.md#id457)

sub-message
:   tca-stats-app-msg

selector
:   kind

#### [rate-est64 (`binary`)](tc.md#id458)

#### [pad (`pad`)](tc.md#id459)

#### [basic-hw (`binary`)](tc.md#id460)

#### [pkt64 (`binary`)](tc.md#id461)

## [Sub-messages](tc.md#id462)

### [tc-options-msg](tc.md#id463)

- **bfifo**
  :   fixed-header
      :   tc-fifo-qopt
- **cake**
  :   attribute-set
      :   tc-cake-attrs
- **cbs**
  :   attribute-set
      :   tc-cbs-attrs
- **choke**
  :   attribute-set
      :   tc-choke-attrs
- **clsact**
- **codel**
  :   attribute-set
      :   tc-codel-attrs
- **drr**
  :   attribute-set
      :   tc-drr-attrs
- **etf**
  :   attribute-set
      :   tc-etf-attrs
- **ets**
  :   attribute-set
      :   tc-ets-attrs
- **fq**
  :   attribute-set
      :   tc-fq-attrs
- **fq_codel**
  :   attribute-set
      :   tc-fq-codel-attrs
- **fq_pie**
  :   attribute-set
      :   tc-fq-pie-attrs
- **flower**
  :   attribute-set
      :   tc-flower-attrs
- **gred**
  :   attribute-set
      :   tc-gred-attrs
- **hfsc**
  :   fixed-header
      :   tc-hfsc-qopt
- **hhf**
  :   attribute-set
      :   tc-hhf-attrs
- **htb**
  :   attribute-set
      :   tc-htb-attrs
- **ingress**
- **mq**
- **mqprio**
  :   fixed-header
      :   tc-mqprio-qopt
- **multiq**
  :   fixed-header
      :   tc-multiq-qopt
- **netem**
  :   fixed-header
      :   tc-netem-qopt

      attribute-set
      :   tc-netem-attrs
- **pfifo**
  :   fixed-header
      :   tc-fifo-qopt
- **pfifo_fast**
  :   fixed-header
      :   tc-prio-qopt
- **pfifo_head_drop**
  :   fixed-header
      :   tc-fifo-qopt
- **pie**
  :   attribute-set
      :   tc-pie-attrs
- **plug**
  :   fixed-header
      :   tc-plug-qopt
- **prio**
  :   fixed-header
      :   tc-prio-qopt
- **qfq**
  :   attribute-set
      :   tc-qfq-attrs
- **red**
  :   attribute-set
      :   tc-red-attrs
- **sfb**
  :   fixed-header
      :   tc-sfb-qopt
- **sfq**
  :   fixed-header
      :   tc-sfq-qopt-v1
- **taprio**
  :   attribute-set
      :   tc-taprio-attrs
- **tbf**
  :   attribute-set
      :   tc-tbf-attrs

### [tc-act-options-msg](tc.md#id464)

- **gact**
  :   attribute-set
      :   tca-gact-attrs

### [tca-stats-app-msg](tc.md#id465)

- **bfifo**
- **blackhole**
- **cake**
  :   attribute-set
      :   tc-cake-stats-attrs
- **cbs**
- **choke**
- **clsact**
- **codel**
- **drr**
- **etf**
- **ets**
- **fq**
- **fq_codel**
- **fq_pie**
- **flower**
- **gred**
- **hfsc**
- **hhf**
- **htb**
- **ingress**
- **mq**
- **mqprio**
- **multiq**
- **netem**
- **noqueue**
- **pfifo**
- **pfifo_fast**
- **pfifo_head_drop**
- **pie**
- **plug**
- **prio**
- **qfq**
- **red**
- **sfb**
- **sfq**
- **taprio**
- **tbf**
