---
collection: kernel
version: "6.8"
title: "Family rt-link netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/rt_link.html
fetched_at: 2026-08-21T03:49:21+00:00
---
# [Family `rt-link` netlink specification](rt_link.md#id31)

Contents

- [Family `rt-link` netlink specification](rt_link.md#family-rt-link-netlink-specification)

  - [Summary](rt_link.md#summary)
  - [Operations](rt_link.md#operations)

    - [newlink](rt_link.md#newlink)
    - [dellink](rt_link.md#dellink)
    - [getlink](rt_link.md#getlink)
    - [setlink](rt_link.md#setlink)
    - [getstats](rt_link.md#getstats)
  - [Multicast groups](rt_link.md#multicast-groups)
  - [Definitions](rt_link.md#definitions)

    - [ifinfo-flags](rt_link.md#ifinfo-flags)
    - [rtgenmsg](rt_link.md#rtgenmsg)
    - [ifinfomsg](rt_link.md#ifinfomsg)
    - [ifla-bridge-id](rt_link.md#ifla-bridge-id)
    - [ifla-cacheinfo](rt_link.md#ifla-cacheinfo)
    - [rtnl-link-stats](rt_link.md#rtnl-link-stats)
    - [rtnl-link-stats64](rt_link.md#rtnl-link-stats64)
    - [rtnl-link-ifmap](rt_link.md#rtnl-link-ifmap)
    - [ipv4-devconf](rt_link.md#ipv4-devconf)
    - [ipv6-devconf](rt_link.md#ipv6-devconf)
    - [ifla-icmp6-stats](rt_link.md#ifla-icmp6-stats)
    - [ifla-inet6-stats](rt_link.md#ifla-inet6-stats)
    - [br-boolopt-multi](rt_link.md#br-boolopt-multi)
    - [if_stats_msg](rt_link.md#if-stats-msg)
  - [Attribute sets](rt_link.md#attribute-sets)

    - [link-attrs](rt_link.md#link-attrs)

      - [address (`binary`)](rt_link.md#address-binary)
      - [broadcast (`binary`)](rt_link.md#broadcast-binary)
      - [ifname (`string`)](rt_link.md#ifname-string)
      - [mtu (`u32`)](rt_link.md#mtu-u32)
      - [link (`u32`)](rt_link.md#link-u32)
      - [qdisc (`string`)](rt_link.md#qdisc-string)
      - [stats (`binary`)](rt_link.md#stats-binary)
      - [cost (`string`)](rt_link.md#cost-string)
      - [priority (`string`)](rt_link.md#priority-string)
      - [master (`u32`)](rt_link.md#master-u32)
      - [wireless (`string`)](rt_link.md#wireless-string)
      - [protinfo (`string`)](rt_link.md#protinfo-string)
      - [txqlen (`u32`)](rt_link.md#txqlen-u32)
      - [map (`binary`)](rt_link.md#map-binary)
      - [weight (`u32`)](rt_link.md#weight-u32)
      - [operstate (`u8`)](rt_link.md#operstate-u8)
      - [linkmode (`u8`)](rt_link.md#linkmode-u8)
      - [linkinfo (`nest`)](rt_link.md#linkinfo-nest)
      - [net-ns-pid (`u32`)](rt_link.md#net-ns-pid-u32)
      - [ifalias (`string`)](rt_link.md#ifalias-string)
      - [num-vf (`u32`)](rt_link.md#num-vf-u32)
      - [vfinfo-list (`nest`)](rt_link.md#vfinfo-list-nest)
      - [stats64 (`binary`)](rt_link.md#stats64-binary)
      - [vf-ports (`nest`)](rt_link.md#vf-ports-nest)
      - [port-self (`nest`)](rt_link.md#port-self-nest)
      - [af-spec (`nest`)](rt_link.md#af-spec-nest)
      - [group (`u32`)](rt_link.md#group-u32)
      - [net-ns-fd (`u32`)](rt_link.md#net-ns-fd-u32)
      - [ext-mask (`u32`)](rt_link.md#ext-mask-u32)
      - [promiscuity (`u32`)](rt_link.md#promiscuity-u32)
      - [num-tx-queues (`u32`)](rt_link.md#num-tx-queues-u32)
      - [num-rx-queues (`u32`)](rt_link.md#num-rx-queues-u32)
      - [carrier (`u8`)](rt_link.md#carrier-u8)
      - [phys-port-id (`binary`)](rt_link.md#phys-port-id-binary)
      - [carrier-changes (`u32`)](rt_link.md#carrier-changes-u32)
      - [phys-switch-id (`binary`)](rt_link.md#phys-switch-id-binary)
      - [link-netnsid (`s32`)](rt_link.md#link-netnsid-s32)
      - [phys-port-name (`string`)](rt_link.md#phys-port-name-string)
      - [proto-down (`u8`)](rt_link.md#proto-down-u8)
      - [gso-max-segs (`u32`)](rt_link.md#gso-max-segs-u32)
      - [gso-max-size (`u32`)](rt_link.md#gso-max-size-u32)
      - [pad (`pad`)](rt_link.md#pad-pad)
      - [xdp (`nest`)](rt_link.md#xdp-nest)
      - [event (`u32`)](rt_link.md#event-u32)
      - [new-netnsid (`s32`)](rt_link.md#new-netnsid-s32)
      - [target-netnsid (`s32`)](rt_link.md#target-netnsid-s32)
      - [carrier-up-count (`u32`)](rt_link.md#carrier-up-count-u32)
      - [carrier-down-count (`u32`)](rt_link.md#carrier-down-count-u32)
      - [new-ifindex (`s32`)](rt_link.md#new-ifindex-s32)
      - [min-mtu (`u32`)](rt_link.md#min-mtu-u32)
      - [max-mtu (`u32`)](rt_link.md#max-mtu-u32)
      - [prop-list (`nest`)](rt_link.md#prop-list-nest)
      - [alt-ifname (`string`)](rt_link.md#alt-ifname-string)
      - [perm-address (`binary`)](rt_link.md#perm-address-binary)
      - [proto-down-reason (`string`)](rt_link.md#proto-down-reason-string)
      - [parent-dev-name (`string`)](rt_link.md#parent-dev-name-string)
      - [parent-dev-bus-name (`string`)](rt_link.md#parent-dev-bus-name-string)
      - [gro-max-size (`u32`)](rt_link.md#gro-max-size-u32)
      - [tso-max-size (`u32`)](rt_link.md#tso-max-size-u32)
      - [tso-max-segs (`u32`)](rt_link.md#tso-max-segs-u32)
      - [allmulti (`u32`)](rt_link.md#allmulti-u32)
      - [devlink-port (`binary`)](rt_link.md#devlink-port-binary)
      - [gso-ipv4-max-size (`u32`)](rt_link.md#gso-ipv4-max-size-u32)
      - [gro-ipv4-max-size (`u32`)](rt_link.md#gro-ipv4-max-size-u32)
      - [dpll-pin (`nest`)](rt_link.md#dpll-pin-nest)
    - [af-spec-attrs](rt_link.md#af-spec-attrs)

      - [inet (`nest`)](rt_link.md#inet-nest)
      - [inet6 (`nest`)](rt_link.md#inet6-nest)
      - [mctp (`nest`)](rt_link.md#mctp-nest)
    - [vfinfo-attrs](rt_link.md#vfinfo-attrs)
    - [vf-ports-attrs](rt_link.md#vf-ports-attrs)
    - [port-self-attrs](rt_link.md#port-self-attrs)
    - [linkinfo-attrs](rt_link.md#linkinfo-attrs)

      - [kind (`string`)](rt_link.md#kind-string)
      - [data (`sub-message`)](rt_link.md#data-sub-message)
      - [xstats (`binary`)](rt_link.md#xstats-binary)
      - [slave-kind (`string`)](rt_link.md#slave-kind-string)
      - [slave-data (`sub-message`)](rt_link.md#slave-data-sub-message)
    - [linkinfo-bridge-attrs](rt_link.md#linkinfo-bridge-attrs)

      - [forward-delay (`u32`)](rt_link.md#forward-delay-u32)
      - [hello-time (`u32`)](rt_link.md#hello-time-u32)
      - [max-age (`u32`)](rt_link.md#max-age-u32)
      - [ageing-time (`u32`)](rt_link.md#ageing-time-u32)
      - [stp-state (`u32`)](rt_link.md#stp-state-u32)
      - [priority (`u16`)](rt_link.md#priority-u16)
      - [vlan-filtering (`u8`)](rt_link.md#vlan-filtering-u8)
      - [vlan-protocol (`u16`)](rt_link.md#vlan-protocol-u16)
      - [group-fwd-mask (`u16`)](rt_link.md#group-fwd-mask-u16)
      - [root-id (`binary`)](rt_link.md#root-id-binary)
      - [bridge-id (`binary`)](rt_link.md#bridge-id-binary)
      - [root-port (`u16`)](rt_link.md#root-port-u16)
      - [root-path-cost (`u32`)](rt_link.md#root-path-cost-u32)
      - [topology-change (`u8`)](rt_link.md#topology-change-u8)
      - [topology-change-detected (`u8`)](rt_link.md#topology-change-detected-u8)
      - [hello-timer (`u64`)](rt_link.md#hello-timer-u64)
      - [tcn-timer (`u64`)](rt_link.md#tcn-timer-u64)
      - [topology-change-timer (`u64`)](rt_link.md#topology-change-timer-u64)
      - [gc-timer (`u64`)](rt_link.md#gc-timer-u64)
      - [group-addr (`binary`)](rt_link.md#group-addr-binary)
      - [fdb-flush (`binary`)](rt_link.md#fdb-flush-binary)
      - [mcast-router (`u8`)](rt_link.md#mcast-router-u8)
      - [mcast-snooping (`u8`)](rt_link.md#mcast-snooping-u8)
      - [mcast-query-use-ifaddr (`u8`)](rt_link.md#mcast-query-use-ifaddr-u8)
      - [mcast-querier (`u8`)](rt_link.md#mcast-querier-u8)
      - [mcast-hash-elasticity (`u32`)](rt_link.md#mcast-hash-elasticity-u32)
      - [mcast-hash-max (`u32`)](rt_link.md#mcast-hash-max-u32)
      - [mcast-last-member-cnt (`u32`)](rt_link.md#mcast-last-member-cnt-u32)
      - [mcast-startup-query-cnt (`u32`)](rt_link.md#mcast-startup-query-cnt-u32)
      - [mcast-last-member-intvl (`u64`)](rt_link.md#mcast-last-member-intvl-u64)
      - [mcast-membership-intvl (`u64`)](rt_link.md#mcast-membership-intvl-u64)
      - [mcast-querier-intvl (`u64`)](rt_link.md#mcast-querier-intvl-u64)
      - [mcast-query-intvl (`u64`)](rt_link.md#mcast-query-intvl-u64)
      - [mcast-query-response-intvl (`u64`)](rt_link.md#mcast-query-response-intvl-u64)
      - [mcast-startup-query-intvl (`u64`)](rt_link.md#mcast-startup-query-intvl-u64)
      - [nf-call-iptables (`u8`)](rt_link.md#nf-call-iptables-u8)
      - [nf-call-ip6-tables (`u8`)](rt_link.md#nf-call-ip6-tables-u8)
      - [nf-call-arptables (`u8`)](rt_link.md#nf-call-arptables-u8)
      - [vlan-default-pvid (`u16`)](rt_link.md#vlan-default-pvid-u16)
      - [pad (`pad`)](rt_link.md#id1)
      - [vlan-stats-enabled (`u8`)](rt_link.md#vlan-stats-enabled-u8)
      - [mcast-stats-enabled (`u8`)](rt_link.md#mcast-stats-enabled-u8)
      - [mcast-igmp-version (`u8`)](rt_link.md#mcast-igmp-version-u8)
      - [mcast-mld-version (`u8`)](rt_link.md#mcast-mld-version-u8)
      - [vlan-stats-per-port (`u8`)](rt_link.md#vlan-stats-per-port-u8)
      - [multi-boolopt (`binary`)](rt_link.md#multi-boolopt-binary)
      - [mcast-querier-state (`binary`)](rt_link.md#mcast-querier-state-binary)
    - [linkinfo-brport-attrs](rt_link.md#linkinfo-brport-attrs)

      - [state (`u8`)](rt_link.md#state-u8)
      - [priority (`u16`)](rt_link.md#id2)
      - [cost (`u32`)](rt_link.md#cost-u32)
      - [mode (`flag`)](rt_link.md#mode-flag)
      - [guard (`flag`)](rt_link.md#guard-flag)
      - [protect (`flag`)](rt_link.md#protect-flag)
      - [fast-leave (`flag`)](rt_link.md#fast-leave-flag)
      - [learning (`flag`)](rt_link.md#learning-flag)
      - [unicast-flood (`flag`)](rt_link.md#unicast-flood-flag)
      - [proxyarp (`flag`)](rt_link.md#proxyarp-flag)
      - [learning-sync (`flag`)](rt_link.md#learning-sync-flag)
      - [proxyarp-wifi (`flag`)](rt_link.md#proxyarp-wifi-flag)
      - [root-id (`binary`)](rt_link.md#id3)
      - [bridge-id (`binary`)](rt_link.md#id4)
      - [designated-port (`u16`)](rt_link.md#designated-port-u16)
      - [designated-cost (`u16`)](rt_link.md#designated-cost-u16)
      - [id (`u16`)](rt_link.md#id-u16)
      - [no (`u16`)](rt_link.md#no-u16)
      - [topology-change-ack (`u8`)](rt_link.md#topology-change-ack-u8)
      - [config-pending (`u8`)](rt_link.md#config-pending-u8)
      - [message-age-timer (`u64`)](rt_link.md#message-age-timer-u64)
      - [forward-delay-timer (`u64`)](rt_link.md#forward-delay-timer-u64)
      - [hold-timer (`u64`)](rt_link.md#hold-timer-u64)
      - [flush (`flag`)](rt_link.md#flush-flag)
      - [multicast-router (`u8`)](rt_link.md#multicast-router-u8)
      - [pad (`pad`)](rt_link.md#id5)
      - [mcast-flood (`flag`)](rt_link.md#mcast-flood-flag)
      - [mcast-to-ucast (`flag`)](rt_link.md#mcast-to-ucast-flag)
      - [vlan-tunnel (`flag`)](rt_link.md#vlan-tunnel-flag)
      - [bcast-flood (`flag`)](rt_link.md#bcast-flood-flag)
      - [group-fwd-mask (`u16`)](rt_link.md#id6)
      - [neigh-suppress (`flag`)](rt_link.md#neigh-suppress-flag)
      - [isolated (`flag`)](rt_link.md#isolated-flag)
      - [backup-port (`u32`)](rt_link.md#backup-port-u32)
      - [mrp-ring-open (`flag`)](rt_link.md#mrp-ring-open-flag)
      - [mrp-in-open (`flag`)](rt_link.md#mrp-in-open-flag)
      - [mcast-eht-hosts-limit (`u32`)](rt_link.md#mcast-eht-hosts-limit-u32)
      - [mcast-eht-hosts-cnt (`u32`)](rt_link.md#mcast-eht-hosts-cnt-u32)
      - [locked (`flag`)](rt_link.md#locked-flag)
      - [mab (`flag`)](rt_link.md#mab-flag)
      - [mcast-n-groups (`u32`)](rt_link.md#mcast-n-groups-u32)
      - [mcast-max-groups (`u32`)](rt_link.md#mcast-max-groups-u32)
      - [neigh-vlan-suppress (`flag`)](rt_link.md#neigh-vlan-suppress-flag)
      - [backup-nhid (`u32`)](rt_link.md#backup-nhid-u32)
    - [linkinfo-gre-attrs](rt_link.md#linkinfo-gre-attrs)

      - [link (`u32`)](rt_link.md#id7)
      - [iflags (`u16`)](rt_link.md#iflags-u16)
      - [oflags (`u16`)](rt_link.md#oflags-u16)
      - [ikey (`u32`)](rt_link.md#ikey-u32)
      - [okey (`u32`)](rt_link.md#okey-u32)
      - [local (`binary`)](rt_link.md#local-binary)
      - [remote (`binary`)](rt_link.md#remote-binary)
      - [ttl (`u8`)](rt_link.md#ttl-u8)
      - [tos (`u8`)](rt_link.md#tos-u8)
      - [pmtudisc (`u8`)](rt_link.md#pmtudisc-u8)
      - [encap-limit (`u32`)](rt_link.md#encap-limit-u32)
      - [flowinfo (`u32`)](rt_link.md#flowinfo-u32)
      - [flags (`u32`)](rt_link.md#flags-u32)
      - [encap-type (`u16`)](rt_link.md#encap-type-u16)
      - [encap-flags (`u16`)](rt_link.md#encap-flags-u16)
      - [encap-sport (`u16`)](rt_link.md#encap-sport-u16)
      - [encap-dport (`u16`)](rt_link.md#encap-dport-u16)
      - [collect-metadata (`flag`)](rt_link.md#collect-metadata-flag)
      - [ignore-df (`u8`)](rt_link.md#ignore-df-u8)
      - [fwmark (`u32`)](rt_link.md#fwmark-u32)
      - [erspan-index (`u32`)](rt_link.md#erspan-index-u32)
      - [erspan-ver (`u8`)](rt_link.md#erspan-ver-u8)
      - [erspan-dir (`u8`)](rt_link.md#erspan-dir-u8)
      - [erspan-hwid (`u16`)](rt_link.md#erspan-hwid-u16)
    - [linkinfo-geneve-attrs](rt_link.md#linkinfo-geneve-attrs)

      - [id (`u32`)](rt_link.md#id-u32)
      - [remote (`binary`)](rt_link.md#id8)
      - [ttl (`u8`)](rt_link.md#id9)
      - [tos (`u8`)](rt_link.md#id10)
      - [port (`u16`)](rt_link.md#port-u16)
      - [collect-metadata (`flag`)](rt_link.md#id11)
      - [remote6 (`binary`)](rt_link.md#remote6-binary)
      - [udp-csum (`u8`)](rt_link.md#udp-csum-u8)
      - [udp-zero-csum6-tx (`u8`)](rt_link.md#udp-zero-csum6-tx-u8)
      - [udp-zero-csum6-rx (`u8`)](rt_link.md#udp-zero-csum6-rx-u8)
      - [label (`u32`)](rt_link.md#label-u32)
      - [ttl-inherit (`u8`)](rt_link.md#ttl-inherit-u8)
      - [df (`u8`)](rt_link.md#df-u8)
      - [inner-proto-inherit (`flag`)](rt_link.md#inner-proto-inherit-flag)
    - [linkinfo-iptun-attrs](rt_link.md#linkinfo-iptun-attrs)

      - [link (`u32`)](rt_link.md#id12)
      - [local (`binary`)](rt_link.md#id13)
      - [remote (`binary`)](rt_link.md#id14)
      - [ttl (`u8`)](rt_link.md#id15)
      - [tos (`u8`)](rt_link.md#id16)
      - [encap-limit (`u8`)](rt_link.md#encap-limit-u8)
      - [flowinfo (`u32`)](rt_link.md#id17)
      - [flags (`u16`)](rt_link.md#flags-u16)
      - [proto (`u8`)](rt_link.md#proto-u8)
      - [pmtudisc (`u8`)](rt_link.md#id18)
      - [6rd-prefix (`binary`)](rt_link.md#rd-prefix-binary)
      - [6rd-relay-prefix (`binary`)](rt_link.md#rd-relay-prefix-binary)
      - [6rd-prefixlen (`u16`)](rt_link.md#rd-prefixlen-u16)
      - [6rd-relay-prefixlen (`u16`)](rt_link.md#rd-relay-prefixlen-u16)
      - [encap-type (`u16`)](rt_link.md#id19)
      - [encap-flags (`u16`)](rt_link.md#id20)
      - [encap-sport (`u16`)](rt_link.md#id21)
      - [encap-dport (`u16`)](rt_link.md#id22)
      - [collect-metadata (`flag`)](rt_link.md#id23)
      - [fwmark (`u32`)](rt_link.md#id24)
    - [linkinfo-tun-attrs](rt_link.md#linkinfo-tun-attrs)

      - [owner (`u32`)](rt_link.md#owner-u32)
      - [group (`u32`)](rt_link.md#id25)
      - [type (`u8`)](rt_link.md#type-u8)
      - [pi (`u8`)](rt_link.md#pi-u8)
      - [vnet-hdr (`u8`)](rt_link.md#vnet-hdr-u8)
      - [persist (`u8`)](rt_link.md#persist-u8)
      - [multi-queue (`u8`)](rt_link.md#multi-queue-u8)
      - [num-queues (`u32`)](rt_link.md#num-queues-u32)
      - [num-disabled-queues (`u32`)](rt_link.md#num-disabled-queues-u32)
    - [linkinfo-vrf-attrs](rt_link.md#linkinfo-vrf-attrs)

      - [table (`u32`)](rt_link.md#table-u32)
    - [xdp-attrs](rt_link.md#xdp-attrs)

      - [fd (`s32`)](rt_link.md#fd-s32)
      - [attached (`u8`)](rt_link.md#attached-u8)
      - [flags (`u32`)](rt_link.md#id26)
      - [prog-id (`u32`)](rt_link.md#prog-id-u32)
      - [drv-prog-id (`u32`)](rt_link.md#drv-prog-id-u32)
      - [skb-prog-id (`u32`)](rt_link.md#skb-prog-id-u32)
      - [hw-prog-id (`u32`)](rt_link.md#hw-prog-id-u32)
      - [expected-fd (`s32`)](rt_link.md#expected-fd-s32)
    - [ifla-attrs](rt_link.md#ifla-attrs)

      - [conf (`binary`)](rt_link.md#conf-binary)
    - [ifla6-attrs](rt_link.md#ifla6-attrs)

      - [flags (`u32`)](rt_link.md#id27)
      - [conf (`binary`)](rt_link.md#id28)
      - [stats (`binary`)](rt_link.md#id29)
      - [mcast (`binary`)](rt_link.md#mcast-binary)
      - [cacheinfo (`binary`)](rt_link.md#cacheinfo-binary)
      - [icmp6-stats (`binary`)](rt_link.md#icmp6-stats-binary)
      - [token (`binary`)](rt_link.md#token-binary)
      - [addr-gen-mode (`u8`)](rt_link.md#addr-gen-mode-u8)
      - [ra-mtu (`u32`)](rt_link.md#ra-mtu-u32)
    - [mctp-attrs](rt_link.md#mctp-attrs)

      - [mctp-net (`u32`)](rt_link.md#mctp-net-u32)
    - [stats-attrs](rt_link.md#stats-attrs)

      - [link-64 (`binary`)](rt_link.md#link-64-binary)
      - [link-xstats (`binary`)](rt_link.md#link-xstats-binary)
      - [link-xstats-slave (`binary`)](rt_link.md#link-xstats-slave-binary)
      - [link-offload-xstats (`nest`)](rt_link.md#link-offload-xstats-nest)
      - [af-spec (`binary`)](rt_link.md#af-spec-binary)
    - [link-offload-xstats](rt_link.md#link-offload-xstats)

      - [cpu-hit (`binary`)](rt_link.md#cpu-hit-binary)
      - [hw-s-info (`array-nest`)](rt_link.md#hw-s-info-array-nest)
      - [l3-stats (`binary`)](rt_link.md#l3-stats-binary)
    - [hw-s-info-one](rt_link.md#hw-s-info-one)

      - [request (`u8`)](rt_link.md#request-u8)
      - [used (`u8`)](rt_link.md#used-u8)
    - [link-dpll-pin-attrs](rt_link.md#link-dpll-pin-attrs)

      - [id (`u32`)](rt_link.md#id30)
  - [Sub-messages](rt_link.md#sub-messages)

    - [linkinfo-data-msg](rt_link.md#linkinfo-data-msg)
    - [linkinfo-member-data-msg](rt_link.md#linkinfo-member-data-msg)

## [Summary](rt_link.md#id32)

Link configuration over rtnetlink.

## [Operations](rt_link.md#id33)

### [newlink](rt_link.md#id34)

Create a new link.

attribute-set
:   link-attrs

fixed-header
:   ifinfomsg

do
:   **request**
    :   attributes
        :   [`ifi-index`, `ifname`, `net-ns-pid`, `net-ns-fd`, `target-netnsid`, `link-netnsid`, `linkinfo`, `group`, `num-tx-queues`, `num-rx-queues`, `address`, `broadcast`, `mtu`, `txqlen`, `operstate`, `linkmode`, `group`, `gso-max-size`, `gso-max-segs`, `gro-max-size`, `gso-ipv4-max-size`, `gro-ipv4-max-size`, `af-spec`]

### [dellink](rt_link.md#id35)

Delete an existing link.

attribute-set
:   link-attrs

fixed-header
:   ifinfomsg

do
:   **request**
    :   attributes
        :   [`ifi-index`, `ifname`]

### [getlink](rt_link.md#id36)

Get / dump information about a link.

attribute-set
:   link-attrs

fixed-header
:   ifinfomsg

do
:   **request**
    :   attributes
        :   [`ifi-index`, `ifname`, `alt-ifname`, `ext-mask`, `target-netnsid`]

    **reply**
    :   attributes
        :   [`ifi-family`, `ifi-type`, `ifi-index`, `ifi-flags`, `ifi-change`, `address`, `broadcast`, `ifname`, `mtu`, `link`, `qdisc`, `stats`, `cost`, `priority`, `master`, `wireless`, `protinfo`, `txqlen`, `map`, `weight`, `operstate`, `linkmode`, `linkinfo`, `net-ns-pid`, `ifalias`, `num-vf`, `vfinfo-list`, `stats64`, `vf-ports`, `port-self`, `af-spec`, `group`, `net-ns-fd`, `ext-mask`, `promiscuity`, `num-tx-queues`, `num-rx-queues`, `carrier`, `phys-port-id`, `carrier-changes`, `phys-switch-id`, `link-netnsid`, `phys-port-name`, `proto-down`, `gso-max-segs`, `gso-max-size`, `pad`, `xdp`, `event`, `new-netnsid`, `if-netnsid`, `target-netnsid`, `carrier-up-count`, `carrier-down-count`, `new-ifindex`, `min-mtu`, `max-mtu`, `prop-list`, `alt-ifname`, `perm-address`, `proto-down-reason`, `parent-dev-name`, `parent-dev-bus-name`, `gro-max-size`, `tso-max-size`, `tso-max-segs`, `allmulti`, `devlink-port`, `gso-ipv4-max-size`, `gro-ipv4-max-size`]

dump
:   **request**
    :   attributes
        :   [`target-netnsid`, `ext-mask`, `master`, `linkinfo`]

    **reply**
    :   attributes
        :   [`ifi-family`, `ifi-type`, `ifi-index`, `ifi-flags`, `ifi-change`, `address`, `broadcast`, `ifname`, `mtu`, `link`, `qdisc`, `stats`, `cost`, `priority`, `master`, `wireless`, `protinfo`, `txqlen`, `map`, `weight`, `operstate`, `linkmode`, `linkinfo`, `net-ns-pid`, `ifalias`, `num-vf`, `vfinfo-list`, `stats64`, `vf-ports`, `port-self`, `af-spec`, `group`, `net-ns-fd`, `ext-mask`, `promiscuity`, `num-tx-queues`, `num-rx-queues`, `carrier`, `phys-port-id`, `carrier-changes`, `phys-switch-id`, `link-netnsid`, `phys-port-name`, `proto-down`, `gso-max-segs`, `gso-max-size`, `pad`, `xdp`, `event`, `new-netnsid`, `if-netnsid`, `target-netnsid`, `carrier-up-count`, `carrier-down-count`, `new-ifindex`, `min-mtu`, `max-mtu`, `prop-list`, `alt-ifname`, `perm-address`, `proto-down-reason`, `parent-dev-name`, `parent-dev-bus-name`, `gro-max-size`, `tso-max-size`, `tso-max-segs`, `allmulti`, `devlink-port`, `gso-ipv4-max-size`, `gro-ipv4-max-size`]

### [setlink](rt_link.md#id37)

Set information about a link.

attribute-set
:   link-attrs

fixed-header
:   ifinfomsg

do
:   **request**
    :   attributes
        :   [`ifi-family`, `ifi-type`, `ifi-index`, `ifi-flags`, `ifi-change`, `address`, `broadcast`, `ifname`, `mtu`, `link`, `qdisc`, `stats`, `cost`, `priority`, `master`, `wireless`, `protinfo`, `txqlen`, `map`, `weight`, `operstate`, `linkmode`, `linkinfo`, `net-ns-pid`, `ifalias`, `num-vf`, `vfinfo-list`, `stats64`, `vf-ports`, `port-self`, `af-spec`, `group`, `net-ns-fd`, `ext-mask`, `promiscuity`, `num-tx-queues`, `num-rx-queues`, `carrier`, `phys-port-id`, `carrier-changes`, `phys-switch-id`, `link-netnsid`, `phys-port-name`, `proto-down`, `gso-max-segs`, `gso-max-size`, `pad`, `xdp`, `event`, `new-netnsid`, `if-netnsid`, `target-netnsid`, `carrier-up-count`, `carrier-down-count`, `new-ifindex`, `min-mtu`, `max-mtu`, `prop-list`, `alt-ifname`, `perm-address`, `proto-down-reason`, `parent-dev-name`, `parent-dev-bus-name`, `gro-max-size`, `tso-max-size`, `tso-max-segs`, `allmulti`, `devlink-port`, `gso-ipv4-max-size`, `gro-ipv4-max-size`]

### [getstats](rt_link.md#id38)

Get / dump link stats.

attribute-set
:   stats-attrs

fixed-header
:   if_stats_msg

do
:   **request**
    :   attributes
        :   [`ifindex`]

    **reply**
    :   attributes
        :   [`family`, `ifindex`, `filter-mask`, `link-64`, `link-xstats`, `link-xstats-slave`, `link-offload-xstats`, `af-spec`]

dump
:   **request**

    **reply**
    :   attributes
        :   [`family`, `ifindex`, `filter-mask`, `link-64`, `link-xstats`, `link-xstats-slave`, `link-offload-xstats`, `af-spec`]

## [Multicast groups](rt_link.md#id39)

- rtnlgrp-link
- rtnlgrp-stats

## [Definitions](rt_link.md#id40)

### [ifinfo-flags](rt_link.md#id41)

type
:   flags

entries
:   up

    broadcast

    debug

    loopback

    point-to-point

    no-trailers

    running

    no-arp

    promisc

    all-multi

    master

    slave

    multicast

    portsel

    auto-media

    dynamic

    lower-up

    dormant

    echo

### [rtgenmsg](rt_link.md#id42)

type
:   struct

members
:   family

### [ifinfomsg](rt_link.md#id43)

type
:   struct

members
:   ifi-family

    pad

    ifi-type

    ifi-index

    ifi-flags

    ifi-change

### [ifla-bridge-id](rt_link.md#id44)

type
:   struct

members
:   prio

    addr

### [ifla-cacheinfo](rt_link.md#id45)

type
:   struct

members
:   max-reasm-len

    tstamp

    reachable-time

    retrans-time

### [rtnl-link-stats](rt_link.md#id46)

type
:   struct

members
:   rx-packets

    tx-packets

    rx-bytes

    tx-bytes

    rx-errors

    tx-errors

    rx-dropped

    tx-dropped

    multicast

    collisions

    rx-length-errors

    rx-over-errors

    rx-crc-errors

    rx-frame-errors

    rx-fifo-errors

    rx-missed-errors

    tx-aborted-errors

    tx-carrier-errors

    tx-fifo-errors

    tx-heartbeat-errors

    tx-window-errors

    rx-compressed

    tx-compressed

    rx-nohandler

### [rtnl-link-stats64](rt_link.md#id47)

type
:   struct

members
:   rx-packets

    tx-packets

    rx-bytes

    tx-bytes

    rx-errors

    tx-errors

    rx-dropped

    tx-dropped

    multicast

    collisions

    rx-length-errors

    rx-over-errors

    rx-crc-errors

    rx-frame-errors

    rx-fifo-errors

    rx-missed-errors

    tx-aborted-errors

    tx-carrier-errors

    tx-fifo-errors

    tx-heartbeat-errors

    tx-window-errors

    rx-compressed

    tx-compressed

    rx-nohandler

    rx-otherhost-dropped

### [rtnl-link-ifmap](rt_link.md#id48)

type
:   struct

members
:   mem-start

    mem-end

    base-addr

    irq

    dma

    port

### [ipv4-devconf](rt_link.md#id49)

type
:   struct

members
:   forwarding

    mc-forwarding

    proxy-arp

    accept-redirects

    secure-redirects

    send-redirects

    shared-media

    rp-filter

    accept-source-route

    bootp-relay

    log-martians

    tag

    arpfilter

    medium-id

    noxfrm

    nopolicy

    force-igmp-version

    arp-announce

    arp-ignore

    promote-secondaries

    arp-accept

    arp-notify

    accept-local

    src-vmark

    proxy-arp-pvlan

    route-localnet

    igmpv2-unsolicited-report-interval

    igmpv3-unsolicited-report-interval

    ignore-routes-with-linkdown

    drop-unicast-in-l2-multicast

    drop-gratuitous-arp

    bc-forwarding

    arp-evict-nocarrier

### [ipv6-devconf](rt_link.md#id50)

type
:   struct

members
:   forwarding

    hoplimit

    mtu6

    accept-ra

    accept-redirects

    autoconf

    dad-transmits

    rtr-solicits

    rtr-solicit-interval

    rtr-solicit-delay

    use-tempaddr

    temp-valid-lft

    temp-prefered-lft

    regen-max-retry

    max-desync-factor

    max-addresses

    force-mld-version

    accept-ra-defrtr

    accept-ra-pinfo

    accept-ra-rtr-pref

    rtr-probe-interval

    accept-ra-rt-info-max-plen

    proxy-ndp

    optimistic-dad

    accept-source-route

    mc-forwarding

    disable-ipv6

    accept-dad

    force-tllao

    ndisc-notify

    mldv1-unsolicited-report-interval

    mldv2-unsolicited-report-interval

    suppress-frag-ndisc

    accept-ra-from-local

    use-optimistic

    accept-ra-mtu

    stable-secret

    use-oif-addrs-only

    accept-ra-min-hop-limit

    ignore-routes-with-linkdown

    drop-unicast-in-l2-multicast

    drop-unsolicited-na

    keep-addr-on-down

    rtr-solicit-max-interval

    seg6-enabled

    seg6-require-hmac

    enhanced-dad

    addr-gen-mode

    disable-policy

    accept-ra-rt-info-min-plen

    ndisc-tclass

    rpl-seg-enabled

    ra-defrtr-metric

    ioam6-enabled

    ioam6-id

    ioam6-id-wide

    ndisc-evict-nocarrier

    accept-untracked-na

### [ifla-icmp6-stats](rt_link.md#id51)

type
:   struct

members
:   inmsgs

    inerrors

    outmsgs

    outerrors

    csumerrors

    ratelimithost

### [ifla-inet6-stats](rt_link.md#id52)

type
:   struct

members
:   inpkts

    inoctets

    indelivers

    outforwdatagrams

    outpkts

    outoctets

    inhdrerrors

    intoobigerrors

    innoroutes

    inaddrerrors

    inunknownprotos

    intruncatedpkts

    indiscards

    outdiscards

    outnoroutes

    reasmtimeout

    reasmreqds

    reasmoks

    reasmfails

    fragoks

    fragfails

    fragcreates

    inmcastpkts

    outmcastpkts

    inbcastpkts

    outbcastpkts

    inmcastoctets

    outmcastoctets

    inbcastoctets

    outbcastoctets

    csumerrors

    noectpkts

    ect1-pkts

    ect0-pkts

    cepkts

    reasm-overlaps

### [br-boolopt-multi](rt_link.md#id53)

type
:   struct

members
:   optval

    optmask

### [if_stats_msg](rt_link.md#id54)

type
:   struct

members
:   family

    pad

    ifindex

    filter-mask

## [Attribute sets](rt_link.md#id55)

### [link-attrs](rt_link.md#id56)

#### [address (`binary`)](rt_link.md#id57)

display-hint
:   mac

#### [broadcast (`binary`)](rt_link.md#id58)

display-hint
:   mac

#### [ifname (`string`)](rt_link.md#id59)

#### [mtu (`u32`)](rt_link.md#id60)

#### [link (`u32`)](rt_link.md#id61)

#### [qdisc (`string`)](rt_link.md#id62)

#### [stats (`binary`)](rt_link.md#id63)

struct
:   rtnl-link-stats

#### [cost (`string`)](rt_link.md#id64)

#### [priority (`string`)](rt_link.md#id65)

#### [master (`u32`)](rt_link.md#id66)

#### [wireless (`string`)](rt_link.md#id67)

#### [protinfo (`string`)](rt_link.md#id68)

#### [txqlen (`u32`)](rt_link.md#id69)

#### [map (`binary`)](rt_link.md#id70)

struct
:   rtnl-link-ifmap

#### [weight (`u32`)](rt_link.md#id71)

#### [operstate (`u8`)](rt_link.md#id72)

#### [linkmode (`u8`)](rt_link.md#id73)

#### [linkinfo (`nest`)](rt_link.md#id74)

nested-attributes
:   linkinfo-attrs

#### [net-ns-pid (`u32`)](rt_link.md#id75)

#### [ifalias (`string`)](rt_link.md#id76)

#### [num-vf (`u32`)](rt_link.md#id77)

#### [vfinfo-list (`nest`)](rt_link.md#id78)

nested-attributes
:   vfinfo-attrs

#### [stats64 (`binary`)](rt_link.md#id79)

struct
:   rtnl-link-stats64

#### [vf-ports (`nest`)](rt_link.md#id80)

nested-attributes
:   vf-ports-attrs

#### [port-self (`nest`)](rt_link.md#id81)

nested-attributes
:   port-self-attrs

#### [af-spec (`nest`)](rt_link.md#id82)

nested-attributes
:   af-spec-attrs

#### [group (`u32`)](rt_link.md#id83)

#### [net-ns-fd (`u32`)](rt_link.md#id84)

#### [ext-mask (`u32`)](rt_link.md#id85)

#### [promiscuity (`u32`)](rt_link.md#id86)

#### [num-tx-queues (`u32`)](rt_link.md#id87)

#### [num-rx-queues (`u32`)](rt_link.md#id88)

#### [carrier (`u8`)](rt_link.md#id89)

#### [phys-port-id (`binary`)](rt_link.md#id90)

#### [carrier-changes (`u32`)](rt_link.md#id91)

#### [phys-switch-id (`binary`)](rt_link.md#id92)

#### [link-netnsid (`s32`)](rt_link.md#id93)

#### [phys-port-name (`string`)](rt_link.md#id94)

#### [proto-down (`u8`)](rt_link.md#id95)

#### [gso-max-segs (`u32`)](rt_link.md#id96)

#### [gso-max-size (`u32`)](rt_link.md#id97)

#### [pad (`pad`)](rt_link.md#id98)

#### [xdp (`nest`)](rt_link.md#id99)

nested-attributes
:   xdp-attrs

#### [event (`u32`)](rt_link.md#id100)

#### [new-netnsid (`s32`)](rt_link.md#id101)

#### [target-netnsid (`s32`)](rt_link.md#id102)

#### [carrier-up-count (`u32`)](rt_link.md#id103)

#### [carrier-down-count (`u32`)](rt_link.md#id104)

#### [new-ifindex (`s32`)](rt_link.md#id105)

#### [min-mtu (`u32`)](rt_link.md#id106)

#### [max-mtu (`u32`)](rt_link.md#id107)

#### [prop-list (`nest`)](rt_link.md#id108)

nested-attributes
:   link-attrs

#### [alt-ifname (`string`)](rt_link.md#id109)

multi-attr
:   True

#### [perm-address (`binary`)](rt_link.md#id110)

display-hint
:   mac

#### [proto-down-reason (`string`)](rt_link.md#id111)

#### [parent-dev-name (`string`)](rt_link.md#id112)

#### [parent-dev-bus-name (`string`)](rt_link.md#id113)

#### [gro-max-size (`u32`)](rt_link.md#id114)

#### [tso-max-size (`u32`)](rt_link.md#id115)

#### [tso-max-segs (`u32`)](rt_link.md#id116)

#### [allmulti (`u32`)](rt_link.md#id117)

#### [devlink-port (`binary`)](rt_link.md#id118)

#### [gso-ipv4-max-size (`u32`)](rt_link.md#id119)

#### [gro-ipv4-max-size (`u32`)](rt_link.md#id120)

#### [dpll-pin (`nest`)](rt_link.md#id121)

nested-attributes
:   link-dpll-pin-attrs

### [af-spec-attrs](rt_link.md#id122)

#### [inet (`nest`)](rt_link.md#id123)

value
:   2

nested-attributes
:   ifla-attrs

#### [inet6 (`nest`)](rt_link.md#id124)

value
:   10

nested-attributes
:   ifla6-attrs

#### [mctp (`nest`)](rt_link.md#id125)

value
:   45

nested-attributes
:   mctp-attrs

### [vfinfo-attrs](rt_link.md#id126)

### [vf-ports-attrs](rt_link.md#id127)

### [port-self-attrs](rt_link.md#id128)

### [linkinfo-attrs](rt_link.md#id129)

#### [kind (`string`)](rt_link.md#id130)

#### [data (`sub-message`)](rt_link.md#id131)

sub-message
:   linkinfo-data-msg

selector
:   kind

#### [xstats (`binary`)](rt_link.md#id132)

#### [slave-kind (`string`)](rt_link.md#id133)

#### [slave-data (`sub-message`)](rt_link.md#id134)

sub-message
:   linkinfo-member-data-msg

selector
:   slave-kind

### [linkinfo-bridge-attrs](rt_link.md#id135)

#### [forward-delay (`u32`)](rt_link.md#id136)

#### [hello-time (`u32`)](rt_link.md#id137)

#### [max-age (`u32`)](rt_link.md#id138)

#### [ageing-time (`u32`)](rt_link.md#id139)

#### [stp-state (`u32`)](rt_link.md#id140)

#### [priority (`u16`)](rt_link.md#id141)

#### [vlan-filtering (`u8`)](rt_link.md#id142)

#### [vlan-protocol (`u16`)](rt_link.md#id143)

#### [group-fwd-mask (`u16`)](rt_link.md#id144)

#### [root-id (`binary`)](rt_link.md#id145)

struct
:   ifla-bridge-id

#### [bridge-id (`binary`)](rt_link.md#id146)

struct
:   ifla-bridge-id

#### [root-port (`u16`)](rt_link.md#id147)

#### [root-path-cost (`u32`)](rt_link.md#id148)

#### [topology-change (`u8`)](rt_link.md#id149)

#### [topology-change-detected (`u8`)](rt_link.md#id150)

#### [hello-timer (`u64`)](rt_link.md#id151)

#### [tcn-timer (`u64`)](rt_link.md#id152)

#### [topology-change-timer (`u64`)](rt_link.md#id153)

#### [gc-timer (`u64`)](rt_link.md#id154)

#### [group-addr (`binary`)](rt_link.md#id155)

display-hint
:   mac

#### [fdb-flush (`binary`)](rt_link.md#id156)

#### [mcast-router (`u8`)](rt_link.md#id157)

#### [mcast-snooping (`u8`)](rt_link.md#id158)

#### [mcast-query-use-ifaddr (`u8`)](rt_link.md#id159)

#### [mcast-querier (`u8`)](rt_link.md#id160)

#### [mcast-hash-elasticity (`u32`)](rt_link.md#id161)

#### [mcast-hash-max (`u32`)](rt_link.md#id162)

#### [mcast-last-member-cnt (`u32`)](rt_link.md#id163)

#### [mcast-startup-query-cnt (`u32`)](rt_link.md#id164)

#### [mcast-last-member-intvl (`u64`)](rt_link.md#id165)

#### [mcast-membership-intvl (`u64`)](rt_link.md#id166)

#### [mcast-querier-intvl (`u64`)](rt_link.md#id167)

#### [mcast-query-intvl (`u64`)](rt_link.md#id168)

#### [mcast-query-response-intvl (`u64`)](rt_link.md#id169)

#### [mcast-startup-query-intvl (`u64`)](rt_link.md#id170)

#### [nf-call-iptables (`u8`)](rt_link.md#id171)

#### [nf-call-ip6-tables (`u8`)](rt_link.md#id172)

#### [nf-call-arptables (`u8`)](rt_link.md#id173)

#### [vlan-default-pvid (`u16`)](rt_link.md#id174)

#### [pad (`pad`)](rt_link.md#id175)

#### [vlan-stats-enabled (`u8`)](rt_link.md#id176)

#### [mcast-stats-enabled (`u8`)](rt_link.md#id177)

#### [mcast-igmp-version (`u8`)](rt_link.md#id178)

#### [mcast-mld-version (`u8`)](rt_link.md#id179)

#### [vlan-stats-per-port (`u8`)](rt_link.md#id180)

#### [multi-boolopt (`binary`)](rt_link.md#id181)

struct
:   br-boolopt-multi

#### [mcast-querier-state (`binary`)](rt_link.md#id182)

### [linkinfo-brport-attrs](rt_link.md#id183)

#### [state (`u8`)](rt_link.md#id184)

#### [priority (`u16`)](rt_link.md#id185)

#### [cost (`u32`)](rt_link.md#id186)

#### [mode (`flag`)](rt_link.md#id187)

#### [guard (`flag`)](rt_link.md#id188)

#### [protect (`flag`)](rt_link.md#id189)

#### [fast-leave (`flag`)](rt_link.md#id190)

#### [learning (`flag`)](rt_link.md#id191)

#### [unicast-flood (`flag`)](rt_link.md#id192)

#### [proxyarp (`flag`)](rt_link.md#id193)

#### [learning-sync (`flag`)](rt_link.md#id194)

#### [proxyarp-wifi (`flag`)](rt_link.md#id195)

#### [root-id (`binary`)](rt_link.md#id196)

struct
:   ifla-bridge-id

#### [bridge-id (`binary`)](rt_link.md#id197)

struct
:   ifla-bridge-id

#### [designated-port (`u16`)](rt_link.md#id198)

#### [designated-cost (`u16`)](rt_link.md#id199)

#### [id (`u16`)](rt_link.md#id200)

#### [no (`u16`)](rt_link.md#id201)

#### [topology-change-ack (`u8`)](rt_link.md#id202)

#### [config-pending (`u8`)](rt_link.md#id203)

#### [message-age-timer (`u64`)](rt_link.md#id204)

#### [forward-delay-timer (`u64`)](rt_link.md#id205)

#### [hold-timer (`u64`)](rt_link.md#id206)

#### [flush (`flag`)](rt_link.md#id207)

#### [multicast-router (`u8`)](rt_link.md#id208)

#### [pad (`pad`)](rt_link.md#id209)

#### [mcast-flood (`flag`)](rt_link.md#id210)

#### [mcast-to-ucast (`flag`)](rt_link.md#id211)

#### [vlan-tunnel (`flag`)](rt_link.md#id212)

#### [bcast-flood (`flag`)](rt_link.md#id213)

#### [group-fwd-mask (`u16`)](rt_link.md#id214)

#### [neigh-suppress (`flag`)](rt_link.md#id215)

#### [isolated (`flag`)](rt_link.md#id216)

#### [backup-port (`u32`)](rt_link.md#id217)

#### [mrp-ring-open (`flag`)](rt_link.md#id218)

#### [mrp-in-open (`flag`)](rt_link.md#id219)

#### [mcast-eht-hosts-limit (`u32`)](rt_link.md#id220)

#### [mcast-eht-hosts-cnt (`u32`)](rt_link.md#id221)

#### [locked (`flag`)](rt_link.md#id222)

#### [mab (`flag`)](rt_link.md#id223)

#### [mcast-n-groups (`u32`)](rt_link.md#id224)

#### [mcast-max-groups (`u32`)](rt_link.md#id225)

#### [neigh-vlan-suppress (`flag`)](rt_link.md#id226)

#### [backup-nhid (`u32`)](rt_link.md#id227)

### [linkinfo-gre-attrs](rt_link.md#id228)

#### [link (`u32`)](rt_link.md#id229)

#### [iflags (`u16`)](rt_link.md#id230)

#### [oflags (`u16`)](rt_link.md#id231)

#### [ikey (`u32`)](rt_link.md#id232)

#### [okey (`u32`)](rt_link.md#id233)

#### [local (`binary`)](rt_link.md#id234)

display-hint
:   ipv4

#### [remote (`binary`)](rt_link.md#id235)

display-hint
:   ipv4

#### [ttl (`u8`)](rt_link.md#id236)

#### [tos (`u8`)](rt_link.md#id237)

#### [pmtudisc (`u8`)](rt_link.md#id238)

#### [encap-limit (`u32`)](rt_link.md#id239)

#### [flowinfo (`u32`)](rt_link.md#id240)

#### [flags (`u32`)](rt_link.md#id241)

#### [encap-type (`u16`)](rt_link.md#id242)

#### [encap-flags (`u16`)](rt_link.md#id243)

#### [encap-sport (`u16`)](rt_link.md#id244)

#### [encap-dport (`u16`)](rt_link.md#id245)

#### [collect-metadata (`flag`)](rt_link.md#id246)

#### [ignore-df (`u8`)](rt_link.md#id247)

#### [fwmark (`u32`)](rt_link.md#id248)

#### [erspan-index (`u32`)](rt_link.md#id249)

#### [erspan-ver (`u8`)](rt_link.md#id250)

#### [erspan-dir (`u8`)](rt_link.md#id251)

#### [erspan-hwid (`u16`)](rt_link.md#id252)

### [linkinfo-geneve-attrs](rt_link.md#id253)

#### [id (`u32`)](rt_link.md#id254)

#### [remote (`binary`)](rt_link.md#id255)

display-hint
:   ipv4

#### [ttl (`u8`)](rt_link.md#id256)

#### [tos (`u8`)](rt_link.md#id257)

#### [port (`u16`)](rt_link.md#id258)

#### [collect-metadata (`flag`)](rt_link.md#id259)

#### [remote6 (`binary`)](rt_link.md#id260)

display-hint
:   ipv6

#### [udp-csum (`u8`)](rt_link.md#id261)

#### [udp-zero-csum6-tx (`u8`)](rt_link.md#id262)

#### [udp-zero-csum6-rx (`u8`)](rt_link.md#id263)

#### [label (`u32`)](rt_link.md#id264)

#### [ttl-inherit (`u8`)](rt_link.md#id265)

#### [df (`u8`)](rt_link.md#id266)

#### [inner-proto-inherit (`flag`)](rt_link.md#id267)

### [linkinfo-iptun-attrs](rt_link.md#id268)

#### [link (`u32`)](rt_link.md#id269)

#### [local (`binary`)](rt_link.md#id270)

display-hint
:   ipv4

#### [remote (`binary`)](rt_link.md#id271)

display-hint
:   ipv4

#### [ttl (`u8`)](rt_link.md#id272)

#### [tos (`u8`)](rt_link.md#id273)

#### [encap-limit (`u8`)](rt_link.md#id274)

#### [flowinfo (`u32`)](rt_link.md#id275)

#### [flags (`u16`)](rt_link.md#id276)

#### [proto (`u8`)](rt_link.md#id277)

#### [pmtudisc (`u8`)](rt_link.md#id278)

#### [6rd-prefix (`binary`)](rt_link.md#id279)

display-hint
:   ipv6

#### [6rd-relay-prefix (`binary`)](rt_link.md#id280)

display-hint
:   ipv4

#### [6rd-prefixlen (`u16`)](rt_link.md#id281)

#### [6rd-relay-prefixlen (`u16`)](rt_link.md#id282)

#### [encap-type (`u16`)](rt_link.md#id283)

#### [encap-flags (`u16`)](rt_link.md#id284)

#### [encap-sport (`u16`)](rt_link.md#id285)

#### [encap-dport (`u16`)](rt_link.md#id286)

#### [collect-metadata (`flag`)](rt_link.md#id287)

#### [fwmark (`u32`)](rt_link.md#id288)

### [linkinfo-tun-attrs](rt_link.md#id289)

#### [owner (`u32`)](rt_link.md#id290)

#### [group (`u32`)](rt_link.md#id291)

#### [type (`u8`)](rt_link.md#id292)

#### [pi (`u8`)](rt_link.md#id293)

#### [vnet-hdr (`u8`)](rt_link.md#id294)

#### [persist (`u8`)](rt_link.md#id295)

#### [multi-queue (`u8`)](rt_link.md#id296)

#### [num-queues (`u32`)](rt_link.md#id297)

#### [num-disabled-queues (`u32`)](rt_link.md#id298)

### [linkinfo-vrf-attrs](rt_link.md#id299)

#### [table (`u32`)](rt_link.md#id300)

### [xdp-attrs](rt_link.md#id301)

#### [fd (`s32`)](rt_link.md#id302)

#### [attached (`u8`)](rt_link.md#id303)

#### [flags (`u32`)](rt_link.md#id304)

#### [prog-id (`u32`)](rt_link.md#id305)

#### [drv-prog-id (`u32`)](rt_link.md#id306)

#### [skb-prog-id (`u32`)](rt_link.md#id307)

#### [hw-prog-id (`u32`)](rt_link.md#id308)

#### [expected-fd (`s32`)](rt_link.md#id309)

### [ifla-attrs](rt_link.md#id310)

#### [conf (`binary`)](rt_link.md#id311)

struct
:   ipv4-devconf

### [ifla6-attrs](rt_link.md#id312)

#### [flags (`u32`)](rt_link.md#id313)

#### [conf (`binary`)](rt_link.md#id314)

struct
:   ipv6-devconf

#### [stats (`binary`)](rt_link.md#id315)

struct
:   ifla-inet6-stats

#### [mcast (`binary`)](rt_link.md#id316)

#### [cacheinfo (`binary`)](rt_link.md#id317)

struct
:   ifla-cacheinfo

#### [icmp6-stats (`binary`)](rt_link.md#id318)

struct
:   ifla-icmp6-stats

#### [token (`binary`)](rt_link.md#id319)

#### [addr-gen-mode (`u8`)](rt_link.md#id320)

#### [ra-mtu (`u32`)](rt_link.md#id321)

### [mctp-attrs](rt_link.md#id322)

#### [mctp-net (`u32`)](rt_link.md#id323)

### [stats-attrs](rt_link.md#id324)

#### [link-64 (`binary`)](rt_link.md#id325)

struct
:   rtnl-link-stats64

#### [link-xstats (`binary`)](rt_link.md#id326)

#### [link-xstats-slave (`binary`)](rt_link.md#id327)

#### [link-offload-xstats (`nest`)](rt_link.md#id328)

nested-attributes
:   link-offload-xstats

#### [af-spec (`binary`)](rt_link.md#id329)

### [link-offload-xstats](rt_link.md#id330)

#### [cpu-hit (`binary`)](rt_link.md#id331)

#### [hw-s-info (`array-nest`)](rt_link.md#id332)

nested-attributes
:   hw-s-info-one

#### [l3-stats (`binary`)](rt_link.md#id333)

### [hw-s-info-one](rt_link.md#id334)

#### [request (`u8`)](rt_link.md#id335)

#### [used (`u8`)](rt_link.md#id336)

### [link-dpll-pin-attrs](rt_link.md#id337)

#### [id (`u32`)](rt_link.md#id338)

## [Sub-messages](rt_link.md#id339)

### [linkinfo-data-msg](rt_link.md#id340)

- **bridge**
  :   attribute-set
      :   linkinfo-bridge-attrs
- **erspan**
  :   attribute-set
      :   linkinfo-gre-attrs
- **gre**
  :   attribute-set
      :   linkinfo-gre-attrs
- **gretap**
  :   attribute-set
      :   linkinfo-gre-attrs
- **geneve**
  :   attribute-set
      :   linkinfo-geneve-attrs
- **ipip**
  :   attribute-set
      :   linkinfo-iptun-attrs
- **sit**
  :   attribute-set
      :   linkinfo-iptun-attrs
- **tun**
  :   attribute-set
      :   linkinfo-tun-attrs
- **vrf**
  :   attribute-set
      :   linkinfo-vrf-attrs

### [linkinfo-member-data-msg](rt_link.md#id341)

- **bridge**
  :   attribute-set
      :   linkinfo-brport-attrs
- **bond**
