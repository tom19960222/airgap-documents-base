---
collection: kernel
version: "6.8"
title: "Family ethtool netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/ethtool.html
fetched_at: 2026-08-21T03:49:15+00:00
---
# [Family `ethtool` netlink specification](ethtool.md#id50)

Contents

- [Family `ethtool` netlink specification](ethtool.md#family-ethtool-netlink-specification)

  - [Summary](ethtool.md#summary)
  - [Operations](ethtool.md#operations)

    - [strset-get](ethtool.md#strset-get)
    - [linkinfo-get](ethtool.md#linkinfo-get)
    - [linkinfo-set](ethtool.md#linkinfo-set)
    - [linkinfo-ntf](ethtool.md#linkinfo-ntf)
    - [linkmodes-get](ethtool.md#linkmodes-get)
    - [linkmodes-set](ethtool.md#linkmodes-set)
    - [linkmodes-ntf](ethtool.md#linkmodes-ntf)
    - [linkstate-get](ethtool.md#linkstate-get)
    - [debug-get](ethtool.md#debug-get)
    - [debug-set](ethtool.md#debug-set)
    - [debug-ntf](ethtool.md#debug-ntf)
    - [wol-get](ethtool.md#wol-get)
    - [wol-set](ethtool.md#wol-set)
    - [wol-ntf](ethtool.md#wol-ntf)
    - [features-get](ethtool.md#features-get)
    - [features-set](ethtool.md#features-set)
    - [features-ntf](ethtool.md#features-ntf)
    - [privflags-get](ethtool.md#privflags-get)
    - [privflags-set](ethtool.md#privflags-set)
    - [privflags-ntf](ethtool.md#privflags-ntf)
    - [rings-get](ethtool.md#rings-get)
    - [rings-set](ethtool.md#rings-set)
    - [rings-ntf](ethtool.md#rings-ntf)
    - [channels-get](ethtool.md#channels-get)
    - [channels-set](ethtool.md#channels-set)
    - [channels-ntf](ethtool.md#channels-ntf)
    - [coalesce-get](ethtool.md#coalesce-get)
    - [coalesce-set](ethtool.md#coalesce-set)
    - [coalesce-ntf](ethtool.md#coalesce-ntf)
    - [pause-get](ethtool.md#pause-get)
    - [pause-set](ethtool.md#pause-set)
    - [pause-ntf](ethtool.md#pause-ntf)
    - [eee-get](ethtool.md#eee-get)
    - [eee-set](ethtool.md#eee-set)
    - [eee-ntf](ethtool.md#eee-ntf)
    - [tsinfo-get](ethtool.md#tsinfo-get)
    - [cable-test-act](ethtool.md#cable-test-act)
    - [cable-test-ntf](ethtool.md#cable-test-ntf)
    - [cable-test-tdr-act](ethtool.md#cable-test-tdr-act)
    - [cable-test-tdr-ntf](ethtool.md#cable-test-tdr-ntf)
    - [tunnel-info-get](ethtool.md#tunnel-info-get)
    - [fec-get](ethtool.md#fec-get)
    - [fec-set](ethtool.md#fec-set)
    - [fec-ntf](ethtool.md#fec-ntf)
    - [module-eeprom-get](ethtool.md#module-eeprom-get)
    - [stats-get](ethtool.md#stats-get)
    - [phc-vclocks-get](ethtool.md#phc-vclocks-get)
    - [module-get](ethtool.md#module-get)
    - [module-set](ethtool.md#module-set)
    - [module-ntf](ethtool.md#module-ntf)
    - [pse-get](ethtool.md#pse-get)
    - [pse-set](ethtool.md#pse-set)
    - [rss-get](ethtool.md#rss-get)
    - [plca-get-cfg](ethtool.md#plca-get-cfg)
    - [plca-set-cfg](ethtool.md#plca-set-cfg)
    - [plca-get-status](ethtool.md#plca-get-status)
    - [plca-ntf](ethtool.md#plca-ntf)
    - [mm-get](ethtool.md#mm-get)
    - [mm-set](ethtool.md#mm-set)
    - [mm-ntf](ethtool.md#mm-ntf)
  - [Definitions](ethtool.md#definitions)

    - [udp-tunnel-type](ethtool.md#udp-tunnel-type)
    - [stringset](ethtool.md#stringset)
  - [Attribute sets](ethtool.md#attribute-sets)

    - [header](ethtool.md#header)

      - [dev-index (`u32`)](ethtool.md#dev-index-u32)
      - [dev-name (`string`)](ethtool.md#dev-name-string)
      - [flags (`u32`)](ethtool.md#flags-u32)
    - [bitset-bit](ethtool.md#bitset-bit)

      - [index (`u32`)](ethtool.md#index-u32)
      - [name (`string`)](ethtool.md#name-string)
      - [value (`flag`)](ethtool.md#value-flag)
    - [bitset-bits](ethtool.md#bitset-bits)

      - [bit (`nest`)](ethtool.md#bit-nest)
    - [bitset](ethtool.md#bitset)

      - [nomask (`flag`)](ethtool.md#nomask-flag)
      - [size (`u32`)](ethtool.md#size-u32)
      - [bits (`nest`)](ethtool.md#bits-nest)
    - [string](ethtool.md#string)

      - [index (`u32`)](ethtool.md#id1)
      - [value (`string`)](ethtool.md#value-string)
    - [strings](ethtool.md#strings)

      - [string (`nest`)](ethtool.md#string-nest)
    - [stringset](ethtool.md#id2)

      - [id (`u32`)](ethtool.md#id-u32)
      - [count (`u32`)](ethtool.md#count-u32)
      - [strings (`nest`)](ethtool.md#strings-nest)
    - [stringsets](ethtool.md#stringsets)

      - [stringset (`nest`)](ethtool.md#stringset-nest)
    - [strset](ethtool.md#strset)

      - [header (`nest`)](ethtool.md#header-nest)
      - [stringsets (`nest`)](ethtool.md#stringsets-nest)
      - [counts-only (`flag`)](ethtool.md#counts-only-flag)
    - [privflags](ethtool.md#privflags)

      - [header (`nest`)](ethtool.md#id3)
      - [flags (`nest`)](ethtool.md#flags-nest)
    - [rings](ethtool.md#rings)

      - [header (`nest`)](ethtool.md#id4)
      - [rx-max (`u32`)](ethtool.md#rx-max-u32)
      - [rx-mini-max (`u32`)](ethtool.md#rx-mini-max-u32)
      - [rx-jumbo-max (`u32`)](ethtool.md#rx-jumbo-max-u32)
      - [tx-max (`u32`)](ethtool.md#tx-max-u32)
      - [rx (`u32`)](ethtool.md#rx-u32)
      - [rx-mini (`u32`)](ethtool.md#rx-mini-u32)
      - [rx-jumbo (`u32`)](ethtool.md#rx-jumbo-u32)
      - [tx (`u32`)](ethtool.md#tx-u32)
      - [rx-buf-len (`u32`)](ethtool.md#rx-buf-len-u32)
      - [tcp-data-split (`u8`)](ethtool.md#tcp-data-split-u8)
      - [cqe-size (`u32`)](ethtool.md#cqe-size-u32)
      - [tx-push (`u8`)](ethtool.md#tx-push-u8)
      - [rx-push (`u8`)](ethtool.md#rx-push-u8)
      - [tx-push-buf-len (`u32`)](ethtool.md#tx-push-buf-len-u32)
      - [tx-push-buf-len-max (`u32`)](ethtool.md#tx-push-buf-len-max-u32)
    - [mm-stat](ethtool.md#mm-stat)

      - [pad (`pad`)](ethtool.md#pad-pad)
      - [reassembly-errors (`u64`)](ethtool.md#reassembly-errors-u64)
      - [smd-errors (`u64`)](ethtool.md#smd-errors-u64)
      - [reassembly-ok (`u64`)](ethtool.md#reassembly-ok-u64)
      - [rx-frag-count (`u64`)](ethtool.md#rx-frag-count-u64)
      - [tx-frag-count (`u64`)](ethtool.md#tx-frag-count-u64)
      - [hold-count (`u64`)](ethtool.md#hold-count-u64)
    - [mm](ethtool.md#mm)

      - [header (`nest`)](ethtool.md#id5)
      - [pmac-enabled (`u8`)](ethtool.md#pmac-enabled-u8)
      - [tx-enabled (`u8`)](ethtool.md#tx-enabled-u8)
      - [tx-active (`u8`)](ethtool.md#tx-active-u8)
      - [tx-min-frag-size (`u32`)](ethtool.md#tx-min-frag-size-u32)
      - [rx-min-frag-size (`u32`)](ethtool.md#rx-min-frag-size-u32)
      - [verify-enabled (`u8`)](ethtool.md#verify-enabled-u8)
      - [verify-status (`u8`)](ethtool.md#verify-status-u8)
      - [verify-time (`u32`)](ethtool.md#verify-time-u32)
      - [max-verify-time (`u32`)](ethtool.md#max-verify-time-u32)
      - [stats (`nest`)](ethtool.md#stats-nest)
    - [linkinfo](ethtool.md#linkinfo)

      - [header (`nest`)](ethtool.md#id6)
      - [port (`u8`)](ethtool.md#port-u8)
      - [phyaddr (`u8`)](ethtool.md#phyaddr-u8)
      - [tp-mdix (`u8`)](ethtool.md#tp-mdix-u8)
      - [tp-mdix-ctrl (`u8`)](ethtool.md#tp-mdix-ctrl-u8)
      - [transceiver (`u8`)](ethtool.md#transceiver-u8)
    - [linkmodes](ethtool.md#linkmodes)

      - [header (`nest`)](ethtool.md#id7)
      - [autoneg (`u8`)](ethtool.md#autoneg-u8)
      - [ours (`nest`)](ethtool.md#ours-nest)
      - [peer (`nest`)](ethtool.md#peer-nest)
      - [speed (`u32`)](ethtool.md#speed-u32)
      - [duplex (`u8`)](ethtool.md#duplex-u8)
      - [master-slave-cfg (`u8`)](ethtool.md#master-slave-cfg-u8)
      - [master-slave-state (`u8`)](ethtool.md#master-slave-state-u8)
      - [lanes (`u32`)](ethtool.md#lanes-u32)
      - [rate-matching (`u8`)](ethtool.md#rate-matching-u8)
    - [linkstate](ethtool.md#linkstate)

      - [header (`nest`)](ethtool.md#id8)
      - [link (`u8`)](ethtool.md#link-u8)
      - [sqi (`u32`)](ethtool.md#sqi-u32)
      - [sqi-max (`u32`)](ethtool.md#sqi-max-u32)
      - [ext-state (`u8`)](ethtool.md#ext-state-u8)
      - [ext-substate (`u8`)](ethtool.md#ext-substate-u8)
      - [ext-down-cnt (`u32`)](ethtool.md#ext-down-cnt-u32)
    - [debug](ethtool.md#debug)

      - [header (`nest`)](ethtool.md#id9)
      - [msgmask (`nest`)](ethtool.md#msgmask-nest)
    - [wol](ethtool.md#wol)

      - [header (`nest`)](ethtool.md#id10)
      - [modes (`nest`)](ethtool.md#modes-nest)
      - [sopass (`binary`)](ethtool.md#sopass-binary)
    - [features](ethtool.md#features)

      - [header (`nest`)](ethtool.md#id11)
      - [hw (`nest`)](ethtool.md#hw-nest)
      - [wanted (`nest`)](ethtool.md#wanted-nest)
      - [active (`nest`)](ethtool.md#active-nest)
      - [nochange (`nest`)](ethtool.md#nochange-nest)
    - [channels](ethtool.md#channels)

      - [header (`nest`)](ethtool.md#id12)
      - [rx-max (`u32`)](ethtool.md#id13)
      - [tx-max (`u32`)](ethtool.md#id14)
      - [other-max (`u32`)](ethtool.md#other-max-u32)
      - [combined-max (`u32`)](ethtool.md#combined-max-u32)
      - [rx-count (`u32`)](ethtool.md#rx-count-u32)
      - [tx-count (`u32`)](ethtool.md#tx-count-u32)
      - [other-count (`u32`)](ethtool.md#other-count-u32)
      - [combined-count (`u32`)](ethtool.md#combined-count-u32)
    - [coalesce](ethtool.md#coalesce)

      - [header (`nest`)](ethtool.md#id15)
      - [rx-usecs (`u32`)](ethtool.md#rx-usecs-u32)
      - [rx-max-frames (`u32`)](ethtool.md#rx-max-frames-u32)
      - [rx-usecs-irq (`u32`)](ethtool.md#rx-usecs-irq-u32)
      - [rx-max-frames-irq (`u32`)](ethtool.md#rx-max-frames-irq-u32)
      - [tx-usecs (`u32`)](ethtool.md#tx-usecs-u32)
      - [tx-max-frames (`u32`)](ethtool.md#tx-max-frames-u32)
      - [tx-usecs-irq (`u32`)](ethtool.md#tx-usecs-irq-u32)
      - [tx-max-frames-irq (`u32`)](ethtool.md#tx-max-frames-irq-u32)
      - [stats-block-usecs (`u32`)](ethtool.md#stats-block-usecs-u32)
      - [use-adaptive-rx (`u8`)](ethtool.md#use-adaptive-rx-u8)
      - [use-adaptive-tx (`u8`)](ethtool.md#use-adaptive-tx-u8)
      - [pkt-rate-low (`u32`)](ethtool.md#pkt-rate-low-u32)
      - [rx-usecs-low (`u32`)](ethtool.md#rx-usecs-low-u32)
      - [rx-max-frames-low (`u32`)](ethtool.md#rx-max-frames-low-u32)
      - [tx-usecs-low (`u32`)](ethtool.md#tx-usecs-low-u32)
      - [tx-max-frames-low (`u32`)](ethtool.md#tx-max-frames-low-u32)
      - [pkt-rate-high (`u32`)](ethtool.md#pkt-rate-high-u32)
      - [rx-usecs-high (`u32`)](ethtool.md#rx-usecs-high-u32)
      - [rx-max-frames-high (`u32`)](ethtool.md#rx-max-frames-high-u32)
      - [tx-usecs-high (`u32`)](ethtool.md#tx-usecs-high-u32)
      - [tx-max-frames-high (`u32`)](ethtool.md#tx-max-frames-high-u32)
      - [rate-sample-interval (`u32`)](ethtool.md#rate-sample-interval-u32)
      - [use-cqe-mode-tx (`u8`)](ethtool.md#use-cqe-mode-tx-u8)
      - [use-cqe-mode-rx (`u8`)](ethtool.md#use-cqe-mode-rx-u8)
      - [tx-aggr-max-bytes (`u32`)](ethtool.md#tx-aggr-max-bytes-u32)
      - [tx-aggr-max-frames (`u32`)](ethtool.md#tx-aggr-max-frames-u32)
      - [tx-aggr-time-usecs (`u32`)](ethtool.md#tx-aggr-time-usecs-u32)
    - [pause-stat](ethtool.md#pause-stat)

      - [pad (`pad`)](ethtool.md#id16)
      - [tx-frames (`u64`)](ethtool.md#tx-frames-u64)
      - [rx-frames (`u64`)](ethtool.md#rx-frames-u64)
    - [pause](ethtool.md#pause)

      - [header (`nest`)](ethtool.md#id17)
      - [autoneg (`u8`)](ethtool.md#id18)
      - [rx (`u8`)](ethtool.md#rx-u8)
      - [tx (`u8`)](ethtool.md#tx-u8)
      - [stats (`nest`)](ethtool.md#id19)
      - [stats-src (`u32`)](ethtool.md#stats-src-u32)
    - [eee](ethtool.md#eee)

      - [header (`nest`)](ethtool.md#id20)
      - [modes-ours (`nest`)](ethtool.md#modes-ours-nest)
      - [modes-peer (`nest`)](ethtool.md#modes-peer-nest)
      - [active (`u8`)](ethtool.md#active-u8)
      - [enabled (`u8`)](ethtool.md#enabled-u8)
      - [tx-lpi-enabled (`u8`)](ethtool.md#tx-lpi-enabled-u8)
      - [tx-lpi-timer (`u32`)](ethtool.md#tx-lpi-timer-u32)
    - [tsinfo](ethtool.md#tsinfo)

      - [header (`nest`)](ethtool.md#id21)
      - [timestamping (`nest`)](ethtool.md#timestamping-nest)
      - [tx-types (`nest`)](ethtool.md#tx-types-nest)
      - [rx-filters (`nest`)](ethtool.md#rx-filters-nest)
      - [phc-index (`u32`)](ethtool.md#phc-index-u32)
    - [cable-result](ethtool.md#cable-result)

      - [pair (`u8`)](ethtool.md#pair-u8)
      - [code (`u8`)](ethtool.md#code-u8)
    - [cable-fault-length](ethtool.md#cable-fault-length)

      - [pair (`u8`)](ethtool.md#id22)
      - [cm (`u32`)](ethtool.md#cm-u32)
    - [cable-nest](ethtool.md#cable-nest)

      - [result (`nest`)](ethtool.md#result-nest)
      - [fault-length (`nest`)](ethtool.md#fault-length-nest)
    - [cable-test](ethtool.md#cable-test)

      - [header (`nest`)](ethtool.md#id23)
    - [cable-test-ntf](ethtool.md#id24)

      - [header (`nest`)](ethtool.md#id25)
      - [status (`u8`)](ethtool.md#status-u8)
      - [nest (`nest`)](ethtool.md#nest-nest)
    - [cable-test-tdr-cfg](ethtool.md#cable-test-tdr-cfg)

      - [first (`u32`)](ethtool.md#first-u32)
      - [last (`u32`)](ethtool.md#last-u32)
      - [step (`u32`)](ethtool.md#step-u32)
      - [pair (`u8`)](ethtool.md#id26)
    - [cable-test-tdr-ntf](ethtool.md#id27)

      - [header (`nest`)](ethtool.md#id28)
      - [status (`u8`)](ethtool.md#id29)
      - [nest (`nest`)](ethtool.md#id30)
    - [cable-test-tdr](ethtool.md#cable-test-tdr)

      - [header (`nest`)](ethtool.md#id31)
      - [cfg (`nest`)](ethtool.md#cfg-nest)
    - [tunnel-udp-entry](ethtool.md#tunnel-udp-entry)

      - [port (`u16`)](ethtool.md#port-u16)
      - [type (`u32`)](ethtool.md#type-u32)
    - [tunnel-udp-table](ethtool.md#tunnel-udp-table)

      - [size (`u32`)](ethtool.md#id32)
      - [types (`nest`)](ethtool.md#types-nest)
      - [entry (`nest`)](ethtool.md#entry-nest)
    - [tunnel-udp](ethtool.md#tunnel-udp)

      - [table (`nest`)](ethtool.md#table-nest)
    - [tunnel-info](ethtool.md#tunnel-info)

      - [header (`nest`)](ethtool.md#id33)
      - [udp-ports (`nest`)](ethtool.md#udp-ports-nest)
    - [fec-stat](ethtool.md#fec-stat)

      - [pad (`pad`)](ethtool.md#id34)
      - [corrected (`binary`)](ethtool.md#corrected-binary)
      - [uncorr (`binary`)](ethtool.md#uncorr-binary)
      - [corr-bits (`binary`)](ethtool.md#corr-bits-binary)
    - [fec](ethtool.md#fec)

      - [header (`nest`)](ethtool.md#id35)
      - [modes (`nest`)](ethtool.md#id36)
      - [auto (`u8`)](ethtool.md#auto-u8)
      - [active (`u32`)](ethtool.md#active-u32)
      - [stats (`nest`)](ethtool.md#id37)
    - [module-eeprom](ethtool.md#module-eeprom)

      - [header (`nest`)](ethtool.md#id38)
      - [offset (`u32`)](ethtool.md#offset-u32)
      - [length (`u32`)](ethtool.md#length-u32)
      - [page (`u8`)](ethtool.md#page-u8)
      - [bank (`u8`)](ethtool.md#bank-u8)
      - [i2c-address (`u8`)](ethtool.md#i2c-address-u8)
      - [data (`binary`)](ethtool.md#data-binary)
    - [stats-grp](ethtool.md#stats-grp)

      - [pad (`pad`)](ethtool.md#id39)
      - [id (`u32`)](ethtool.md#id40)
      - [ss-id (`u32`)](ethtool.md#ss-id-u32)
      - [stat (`u64`)](ethtool.md#stat-u64)
      - [hist-rx (`nest`)](ethtool.md#hist-rx-nest)
      - [hist-tx (`nest`)](ethtool.md#hist-tx-nest)
      - [hist-bkt-low (`u32`)](ethtool.md#hist-bkt-low-u32)
      - [hist-bkt-hi (`u32`)](ethtool.md#hist-bkt-hi-u32)
      - [hist-val (`u64`)](ethtool.md#hist-val-u64)
    - [stats-grp-hist](ethtool.md#stats-grp-hist)

      - [hist-bkt-low](ethtool.md#hist-bkt-low)
      - [hist-bkt-hi](ethtool.md#hist-bkt-hi)
      - [hist-val](ethtool.md#hist-val)
    - [stats](ethtool.md#stats)

      - [pad (`pad`)](ethtool.md#id41)
      - [header (`nest`)](ethtool.md#id42)
      - [groups (`nest`)](ethtool.md#groups-nest)
      - [grp (`nest`)](ethtool.md#grp-nest)
      - [src (`u32`)](ethtool.md#src-u32)
    - [phc-vclocks](ethtool.md#phc-vclocks)

      - [header (`nest`)](ethtool.md#id43)
      - [num (`u32`)](ethtool.md#num-u32)
      - [index (`binary`)](ethtool.md#index-binary)
    - [module](ethtool.md#module)

      - [header (`nest`)](ethtool.md#id44)
      - [power-mode-policy (`u8`)](ethtool.md#power-mode-policy-u8)
      - [power-mode (`u8`)](ethtool.md#power-mode-u8)
    - [pse](ethtool.md#pse)

      - [header (`nest`)](ethtool.md#id45)
      - [admin-state (`u32`)](ethtool.md#admin-state-u32)
      - [admin-control (`u32`)](ethtool.md#admin-control-u32)
      - [pw-d-status (`u32`)](ethtool.md#pw-d-status-u32)
    - [rss](ethtool.md#rss)

      - [header (`nest`)](ethtool.md#id46)
      - [context (`u32`)](ethtool.md#context-u32)
      - [hfunc (`u32`)](ethtool.md#hfunc-u32)
      - [indir (`binary`)](ethtool.md#indir-binary)
      - [hkey (`binary`)](ethtool.md#hkey-binary)
      - [input_xfrm (`u32`)](ethtool.md#input-xfrm-u32)
    - [plca](ethtool.md#plca)

      - [header (`nest`)](ethtool.md#id47)
      - [version (`u16`)](ethtool.md#version-u16)
      - [enabled (`u8`)](ethtool.md#id48)
      - [status (`u8`)](ethtool.md#id49)
      - [node-cnt (`u32`)](ethtool.md#node-cnt-u32)
      - [node-id (`u32`)](ethtool.md#node-id-u32)
      - [to-tmr (`u32`)](ethtool.md#to-tmr-u32)
      - [burst-cnt (`u32`)](ethtool.md#burst-cnt-u32)
      - [burst-tmr (`u32`)](ethtool.md#burst-tmr-u32)

## [Summary](ethtool.md#id51)

Partial family for Ethtool Netlink.

## [Operations](ethtool.md#id52)

### [strset-get](ethtool.md#id53)

Get string set from the kernel.

attribute-set
:   strset

do
:   **request**
    :   attributes
        :   [`header`, `stringsets`, `counts-only`]

    **reply**
    :   attributes
        :   [`header`, `stringsets`]

dump
:   **request**
    :   attributes
        :   [`header`, `stringsets`, `counts-only`]

    **reply**
    :   attributes
        :   [`header`, `stringsets`]

### [linkinfo-get](ethtool.md#id54)

Get link info.

attribute-set
:   linkinfo

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `port`, `phyaddr`, `tp-mdix`, `tp-mdix-ctrl`, `transceiver`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `port`, `phyaddr`, `tp-mdix`, `tp-mdix-ctrl`, `transceiver`]

### [linkinfo-set](ethtool.md#id55)

Set link info.

attribute-set
:   linkinfo

do
:   **request**
    :   attributes
        :   [`header`, `port`, `phyaddr`, `tp-mdix`, `tp-mdix-ctrl`, `transceiver`]

### [linkinfo-ntf](ethtool.md#id56)

Notification for change in link info.

notify
:   linkinfo-get

### [linkmodes-get](ethtool.md#id57)

Get link modes.

attribute-set
:   linkmodes

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `autoneg`, `ours`, `peer`, `speed`, `duplex`, `master-slave-cfg`, `master-slave-state`, `lanes`, `rate-matching`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `autoneg`, `ours`, `peer`, `speed`, `duplex`, `master-slave-cfg`, `master-slave-state`, `lanes`, `rate-matching`]

### [linkmodes-set](ethtool.md#id58)

Set link modes.

attribute-set
:   linkmodes

do
:   **request**
    :   attributes
        :   [`header`, `autoneg`, `ours`, `peer`, `speed`, `duplex`, `master-slave-cfg`, `master-slave-state`, `lanes`, `rate-matching`]

### [linkmodes-ntf](ethtool.md#id59)

Notification for change in link modes.

notify
:   linkmodes-get

### [linkstate-get](ethtool.md#id60)

Get link state.

attribute-set
:   linkstate

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `link`, `sqi`, `sqi-max`, `ext-state`, `ext-substate`, `ext-down-cnt`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `link`, `sqi`, `sqi-max`, `ext-state`, `ext-substate`, `ext-down-cnt`]

### [debug-get](ethtool.md#id61)

Get debug message mask.

attribute-set
:   debug

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `msgmask`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `msgmask`]

### [debug-set](ethtool.md#id62)

Set debug message mask.

attribute-set
:   debug

do
:   **request**
    :   attributes
        :   [`header`, `msgmask`]

### [debug-ntf](ethtool.md#id63)

Notification for change in debug message mask.

notify
:   debug-get

### [wol-get](ethtool.md#id64)

Get WOL params.

attribute-set
:   wol

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `modes`, `sopass`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `modes`, `sopass`]

### [wol-set](ethtool.md#id65)

Set WOL params.

attribute-set
:   wol

do
:   **request**
    :   attributes
        :   [`header`, `modes`, `sopass`]

### [wol-ntf](ethtool.md#id66)

Notification for change in WOL params.

notify
:   wol-get

### [features-get](ethtool.md#id67)

Get features.

attribute-set
:   features

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `hw`, `wanted`, `active`, `nochange`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `hw`, `wanted`, `active`, `nochange`]

### [features-set](ethtool.md#id68)

Set features.

attribute-set
:   features

do
:   **request**
    :   attributes
        :   [`header`, `hw`, `wanted`, `active`, `nochange`]

    **reply**
    :   attributes
        :   [`header`, `hw`, `wanted`, `active`, `nochange`]

### [features-ntf](ethtool.md#id69)

Notification for change in features.

notify
:   features-get

### [privflags-get](ethtool.md#id70)

Get device private flags.

attribute-set
:   privflags

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `flags`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `flags`]

### [privflags-set](ethtool.md#id71)

Set device private flags.

attribute-set
:   privflags

do
:   **request**
    :   attributes
        :   [`header`, `flags`]

### [privflags-ntf](ethtool.md#id72)

Notification for change in device private flags.

notify
:   privflags-get

### [rings-get](ethtool.md#id73)

Get ring params.

attribute-set
:   rings

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `rx-max`, `rx-mini-max`, `rx-jumbo-max`, `tx-max`, `rx`, `rx-mini`, `rx-jumbo`, `tx`, `rx-buf-len`, `tcp-data-split`, `cqe-size`, `tx-push`, `rx-push`, `tx-push-buf-len`, `tx-push-buf-len-max`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `rx-max`, `rx-mini-max`, `rx-jumbo-max`, `tx-max`, `rx`, `rx-mini`, `rx-jumbo`, `tx`, `rx-buf-len`, `tcp-data-split`, `cqe-size`, `tx-push`, `rx-push`, `tx-push-buf-len`, `tx-push-buf-len-max`]

### [rings-set](ethtool.md#id74)

Set ring params.

attribute-set
:   rings

do
:   **request**
    :   attributes
        :   [`header`, `rx-max`, `rx-mini-max`, `rx-jumbo-max`, `tx-max`, `rx`, `rx-mini`, `rx-jumbo`, `tx`, `rx-buf-len`, `tcp-data-split`, `cqe-size`, `tx-push`, `rx-push`, `tx-push-buf-len`, `tx-push-buf-len-max`]

### [rings-ntf](ethtool.md#id75)

Notification for change in ring params.

notify
:   rings-get

### [channels-get](ethtool.md#id76)

Get channel params.

attribute-set
:   channels

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `rx-max`, `tx-max`, `other-max`, `combined-max`, `rx-count`, `tx-count`, `other-count`, `combined-count`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `rx-max`, `tx-max`, `other-max`, `combined-max`, `rx-count`, `tx-count`, `other-count`, `combined-count`]

### [channels-set](ethtool.md#id77)

Set channel params.

attribute-set
:   channels

do
:   **request**
    :   attributes
        :   [`header`, `rx-max`, `tx-max`, `other-max`, `combined-max`, `rx-count`, `tx-count`, `other-count`, `combined-count`]

### [channels-ntf](ethtool.md#id78)

Notification for change in channel params.

notify
:   channels-get

### [coalesce-get](ethtool.md#id79)

Get coalesce params.

attribute-set
:   coalesce

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `rx-usecs`, `rx-max-frames`, `rx-usecs-irq`, `rx-max-frames-irq`, `tx-usecs`, `tx-max-frames`, `tx-usecs-irq`, `tx-max-frames-irq`, `stats-block-usecs`, `use-adaptive-rx`, `use-adaptive-tx`, `pkt-rate-low`, `rx-usecs-low`, `rx-max-frames-low`, `tx-usecs-low`, `tx-max-frames-low`, `pkt-rate-high`, `rx-usecs-high`, `rx-max-frames-high`, `tx-usecs-high`, `tx-max-frames-high`, `rate-sample-interval`, `use-cqe-mode-tx`, `use-cqe-mode-rx`, `tx-aggr-max-bytes`, `tx-aggr-max-frames`, `tx-aggr-time-usecs`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `rx-usecs`, `rx-max-frames`, `rx-usecs-irq`, `rx-max-frames-irq`, `tx-usecs`, `tx-max-frames`, `tx-usecs-irq`, `tx-max-frames-irq`, `stats-block-usecs`, `use-adaptive-rx`, `use-adaptive-tx`, `pkt-rate-low`, `rx-usecs-low`, `rx-max-frames-low`, `tx-usecs-low`, `tx-max-frames-low`, `pkt-rate-high`, `rx-usecs-high`, `rx-max-frames-high`, `tx-usecs-high`, `tx-max-frames-high`, `rate-sample-interval`, `use-cqe-mode-tx`, `use-cqe-mode-rx`, `tx-aggr-max-bytes`, `tx-aggr-max-frames`, `tx-aggr-time-usecs`]

### [coalesce-set](ethtool.md#id80)

Set coalesce params.

attribute-set
:   coalesce

do
:   **request**
    :   attributes
        :   [`header`, `rx-usecs`, `rx-max-frames`, `rx-usecs-irq`, `rx-max-frames-irq`, `tx-usecs`, `tx-max-frames`, `tx-usecs-irq`, `tx-max-frames-irq`, `stats-block-usecs`, `use-adaptive-rx`, `use-adaptive-tx`, `pkt-rate-low`, `rx-usecs-low`, `rx-max-frames-low`, `tx-usecs-low`, `tx-max-frames-low`, `pkt-rate-high`, `rx-usecs-high`, `rx-max-frames-high`, `tx-usecs-high`, `tx-max-frames-high`, `rate-sample-interval`, `use-cqe-mode-tx`, `use-cqe-mode-rx`, `tx-aggr-max-bytes`, `tx-aggr-max-frames`, `tx-aggr-time-usecs`]

### [coalesce-ntf](ethtool.md#id81)

Notification for change in coalesce params.

notify
:   coalesce-get

### [pause-get](ethtool.md#id82)

Get pause params.

attribute-set
:   pause

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `autoneg`, `rx`, `tx`, `stats`, `stats-src`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `autoneg`, `rx`, `tx`, `stats`, `stats-src`]

### [pause-set](ethtool.md#id83)

Set pause params.

attribute-set
:   pause

do
:   **request**
    :   attributes
        :   [`header`, `autoneg`, `rx`, `tx`, `stats`, `stats-src`]

### [pause-ntf](ethtool.md#id84)

Notification for change in pause params.

notify
:   pause-get

### [eee-get](ethtool.md#id85)

Get eee params.

attribute-set
:   eee

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `modes-ours`, `modes-peer`, `active`, `enabled`, `tx-lpi-enabled`, `tx-lpi-timer`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `modes-ours`, `modes-peer`, `active`, `enabled`, `tx-lpi-enabled`, `tx-lpi-timer`]

### [eee-set](ethtool.md#id86)

Set eee params.

attribute-set
:   eee

do
:   **request**
    :   attributes
        :   [`header`, `modes-ours`, `modes-peer`, `active`, `enabled`, `tx-lpi-enabled`, `tx-lpi-timer`]

### [eee-ntf](ethtool.md#id87)

Notification for change in eee params.

notify
:   eee-get

### [tsinfo-get](ethtool.md#id88)

Get tsinfo params.

attribute-set
:   tsinfo

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `timestamping`, `tx-types`, `rx-filters`, `phc-index`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `timestamping`, `tx-types`, `rx-filters`, `phc-index`]

### [cable-test-act](ethtool.md#id89)

Cable test.

attribute-set
:   cable-test

do
:   **request**
    :   attributes
        :   [`header`]

### [cable-test-ntf](ethtool.md#id90)

Cable test notification.

attribute-set
:   cable-test-ntf

event
:   {'attributes': ['header', 'status']}

### [cable-test-tdr-act](ethtool.md#id91)

Cable test TDR.

attribute-set
:   cable-test-tdr

do
:   **request**
    :   attributes
        :   [`header`]

### [cable-test-tdr-ntf](ethtool.md#id92)

Cable test TDR notification.

attribute-set
:   cable-test-tdr-ntf

event
:   {'attributes': ['header', 'status', 'nest']}

### [tunnel-info-get](ethtool.md#id93)

Get tsinfo params.

attribute-set
:   tunnel-info

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `udp-ports`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `udp-ports`]

### [fec-get](ethtool.md#id94)

Get FEC params.

attribute-set
:   fec

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `modes`, `auto`, `active`, `stats`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `modes`, `auto`, `active`, `stats`]

### [fec-set](ethtool.md#id95)

Set FEC params.

attribute-set
:   fec

do
:   **request**
    :   attributes
        :   [`header`, `modes`, `auto`, `active`, `stats`]

### [fec-ntf](ethtool.md#id96)

Notification for change in FEC params.

notify
:   fec-get

### [module-eeprom-get](ethtool.md#id97)

Get module EEPROM params.

attribute-set
:   module-eeprom

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `offset`, `length`, `page`, `bank`, `i2c-address`, `data`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `offset`, `length`, `page`, `bank`, `i2c-address`, `data`]

### [stats-get](ethtool.md#id98)

Get statistics.

attribute-set
:   stats

do
:   **request**
    :   attributes
        :   [`header`, `groups`]

    **reply**
    :   attributes
        :   [`header`, `groups`, `grp`, `src`]

dump
:   **request**
    :   attributes
        :   [`header`, `groups`]

    **reply**
    :   attributes
        :   [`header`, `groups`, `grp`, `src`]

### [phc-vclocks-get](ethtool.md#id99)

Get PHC VCLOCKs.

attribute-set
:   phc-vclocks

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `num`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `num`]

### [module-get](ethtool.md#id100)

Get module params.

attribute-set
:   module

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `power-mode-policy`, `power-mode`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `power-mode-policy`, `power-mode`]

### [module-set](ethtool.md#id101)

Set module params.

attribute-set
:   module

do
:   **request**
    :   attributes
        :   [`header`, `power-mode-policy`, `power-mode`]

### [module-ntf](ethtool.md#id102)

Notification for change in module params.

notify
:   module-get

### [pse-get](ethtool.md#id103)

Get Power Sourcing Equipment params.

attribute-set
:   pse

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `admin-state`, `admin-control`, `pw-d-status`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `admin-state`, `admin-control`, `pw-d-status`]

### [pse-set](ethtool.md#id104)

Set Power Sourcing Equipment params.

attribute-set
:   pse

do
:   **request**
    :   attributes
        :   [`header`, `admin-state`, `admin-control`, `pw-d-status`]

### [rss-get](ethtool.md#id105)

Get RSS params.

attribute-set
:   rss

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `context`, `hfunc`, `indir`, `hkey`, `input_xfrm`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `context`, `hfunc`, `indir`, `hkey`, `input_xfrm`]

### [plca-get-cfg](ethtool.md#id106)

Get PLCA params.

attribute-set
:   plca

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `version`, `enabled`, `status`, `node-cnt`, `node-id`, `to-tmr`, `burst-cnt`, `burst-tmr`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `version`, `enabled`, `status`, `node-cnt`, `node-id`, `to-tmr`, `burst-cnt`, `burst-tmr`]

### [plca-set-cfg](ethtool.md#id107)

Set PLCA params.

attribute-set
:   plca

do
:   **request**
    :   attributes
        :   [`header`, `version`, `enabled`, `status`, `node-cnt`, `node-id`, `to-tmr`, `burst-cnt`, `burst-tmr`]

### [plca-get-status](ethtool.md#id108)

Get PLCA status params.

attribute-set
:   plca

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `version`, `enabled`, `status`, `node-cnt`, `node-id`, `to-tmr`, `burst-cnt`, `burst-tmr`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `version`, `enabled`, `status`, `node-cnt`, `node-id`, `to-tmr`, `burst-cnt`, `burst-tmr`]

### [plca-ntf](ethtool.md#id109)

Notification for change in PLCA params.

notify
:   plca-get-cfg

### [mm-get](ethtool.md#id110)

Get MAC Merge configuration and state

attribute-set
:   mm

do
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `pmac-enabled`, `tx-enabled`, `tx-active`, `tx-min-frag-size`, `rx-min-frag-size`, `verify-enabled`, `verify-time`, `max-verify-time`, `stats`]

dump
:   **request**
    :   attributes
        :   [`header`]

    **reply**
    :   attributes
        :   [`header`, `pmac-enabled`, `tx-enabled`, `tx-active`, `tx-min-frag-size`, `rx-min-frag-size`, `verify-enabled`, `verify-time`, `max-verify-time`, `stats`]

### [mm-set](ethtool.md#id111)

Set MAC Merge configuration

attribute-set
:   mm

do
:   **request**
    :   attributes
        :   [`header`, `verify-enabled`, `verify-time`, `tx-enabled`, `pmac-enabled`, `tx-min-frag-size`]

### [mm-ntf](ethtool.md#id112)

Notification for change in MAC Merge configuration.

notify
:   mm-get

## [Definitions](ethtool.md#id113)

### [udp-tunnel-type](ethtool.md#id114)

enum-name
:   None

type
:   enum

entries
:   - `vxlan`
    - `geneve`
    - `vxlan-gpe`

### [stringset](ethtool.md#id115)

type
:   enum

entries

## [Attribute sets](ethtool.md#id116)

### [header](ethtool.md#id117)

#### [dev-index (`u32`)](ethtool.md#id118)

#### [dev-name (`string`)](ethtool.md#id119)

#### [flags (`u32`)](ethtool.md#id120)

### [bitset-bit](ethtool.md#id121)

#### [index (`u32`)](ethtool.md#id122)

#### [name (`string`)](ethtool.md#id123)

#### [value (`flag`)](ethtool.md#id124)

### [bitset-bits](ethtool.md#id125)

#### [bit (`nest`)](ethtool.md#id126)

multi-attr
:   True

nested-attributes
:   bitset-bit

### [bitset](ethtool.md#id127)

#### [nomask (`flag`)](ethtool.md#id128)

#### [size (`u32`)](ethtool.md#id129)

#### [bits (`nest`)](ethtool.md#id130)

nested-attributes
:   bitset-bits

### [string](ethtool.md#id131)

#### [index (`u32`)](ethtool.md#id132)

#### [value (`string`)](ethtool.md#id133)

### [strings](ethtool.md#id134)

#### [string (`nest`)](ethtool.md#id135)

multi-attr
:   True

nested-attributes
:   string

### [stringset](ethtool.md#id136)

#### [id (`u32`)](ethtool.md#id137)

#### [count (`u32`)](ethtool.md#id138)

#### [strings (`nest`)](ethtool.md#id139)

multi-attr
:   True

nested-attributes
:   strings

### [stringsets](ethtool.md#id140)

#### [stringset (`nest`)](ethtool.md#id141)

multi-attr
:   True

nested-attributes
:   stringset

### [strset](ethtool.md#id142)

#### [header (`nest`)](ethtool.md#id143)

nested-attributes
:   header

#### [stringsets (`nest`)](ethtool.md#id144)

nested-attributes
:   stringsets

#### [counts-only (`flag`)](ethtool.md#id145)

### [privflags](ethtool.md#id146)

#### [header (`nest`)](ethtool.md#id147)

nested-attributes
:   header

#### [flags (`nest`)](ethtool.md#id148)

nested-attributes
:   bitset

### [rings](ethtool.md#id149)

#### [header (`nest`)](ethtool.md#id150)

nested-attributes
:   header

#### [rx-max (`u32`)](ethtool.md#id151)

#### [rx-mini-max (`u32`)](ethtool.md#id152)

#### [rx-jumbo-max (`u32`)](ethtool.md#id153)

#### [tx-max (`u32`)](ethtool.md#id154)

#### [rx (`u32`)](ethtool.md#id155)

#### [rx-mini (`u32`)](ethtool.md#id156)

#### [rx-jumbo (`u32`)](ethtool.md#id157)

#### [tx (`u32`)](ethtool.md#id158)

#### [rx-buf-len (`u32`)](ethtool.md#id159)

#### [tcp-data-split (`u8`)](ethtool.md#id160)

#### [cqe-size (`u32`)](ethtool.md#id161)

#### [tx-push (`u8`)](ethtool.md#id162)

#### [rx-push (`u8`)](ethtool.md#id163)

#### [tx-push-buf-len (`u32`)](ethtool.md#id164)

#### [tx-push-buf-len-max (`u32`)](ethtool.md#id165)

### [mm-stat](ethtool.md#id166)

#### [pad (`pad`)](ethtool.md#id167)

#### [reassembly-errors (`u64`)](ethtool.md#id168)

#### [smd-errors (`u64`)](ethtool.md#id169)

#### [reassembly-ok (`u64`)](ethtool.md#id170)

#### [rx-frag-count (`u64`)](ethtool.md#id171)

#### [tx-frag-count (`u64`)](ethtool.md#id172)

#### [hold-count (`u64`)](ethtool.md#id173)

### [mm](ethtool.md#id174)

#### [header (`nest`)](ethtool.md#id175)

nested-attributes
:   header

#### [pmac-enabled (`u8`)](ethtool.md#id176)

#### [tx-enabled (`u8`)](ethtool.md#id177)

#### [tx-active (`u8`)](ethtool.md#id178)

#### [tx-min-frag-size (`u32`)](ethtool.md#id179)

#### [rx-min-frag-size (`u32`)](ethtool.md#id180)

#### [verify-enabled (`u8`)](ethtool.md#id181)

#### [verify-status (`u8`)](ethtool.md#id182)

#### [verify-time (`u32`)](ethtool.md#id183)

#### [max-verify-time (`u32`)](ethtool.md#id184)

#### [stats (`nest`)](ethtool.md#id185)

nested-attributes
:   mm-stat

### [linkinfo](ethtool.md#id186)

#### [header (`nest`)](ethtool.md#id187)

nested-attributes
:   header

#### [port (`u8`)](ethtool.md#id188)

#### [phyaddr (`u8`)](ethtool.md#id189)

#### [tp-mdix (`u8`)](ethtool.md#id190)

#### [tp-mdix-ctrl (`u8`)](ethtool.md#id191)

#### [transceiver (`u8`)](ethtool.md#id192)

### [linkmodes](ethtool.md#id193)

#### [header (`nest`)](ethtool.md#id194)

nested-attributes
:   header

#### [autoneg (`u8`)](ethtool.md#id195)

#### [ours (`nest`)](ethtool.md#id196)

nested-attributes
:   bitset

#### [peer (`nest`)](ethtool.md#id197)

nested-attributes
:   bitset

#### [speed (`u32`)](ethtool.md#id198)

#### [duplex (`u8`)](ethtool.md#id199)

#### [master-slave-cfg (`u8`)](ethtool.md#id200)

#### [master-slave-state (`u8`)](ethtool.md#id201)

#### [lanes (`u32`)](ethtool.md#id202)

#### [rate-matching (`u8`)](ethtool.md#id203)

### [linkstate](ethtool.md#id204)

#### [header (`nest`)](ethtool.md#id205)

nested-attributes
:   header

#### [link (`u8`)](ethtool.md#id206)

#### [sqi (`u32`)](ethtool.md#id207)

#### [sqi-max (`u32`)](ethtool.md#id208)

#### [ext-state (`u8`)](ethtool.md#id209)

#### [ext-substate (`u8`)](ethtool.md#id210)

#### [ext-down-cnt (`u32`)](ethtool.md#id211)

### [debug](ethtool.md#id212)

#### [header (`nest`)](ethtool.md#id213)

nested-attributes
:   header

#### [msgmask (`nest`)](ethtool.md#id214)

nested-attributes
:   bitset

### [wol](ethtool.md#id215)

#### [header (`nest`)](ethtool.md#id216)

nested-attributes
:   header

#### [modes (`nest`)](ethtool.md#id217)

nested-attributes
:   bitset

#### [sopass (`binary`)](ethtool.md#id218)

### [features](ethtool.md#id219)

#### [header (`nest`)](ethtool.md#id220)

nested-attributes
:   header

#### [hw (`nest`)](ethtool.md#id221)

nested-attributes
:   bitset

#### [wanted (`nest`)](ethtool.md#id222)

nested-attributes
:   bitset

#### [active (`nest`)](ethtool.md#id223)

nested-attributes
:   bitset

#### [nochange (`nest`)](ethtool.md#id224)

nested-attributes
:   bitset

### [channels](ethtool.md#id225)

#### [header (`nest`)](ethtool.md#id226)

nested-attributes
:   header

#### [rx-max (`u32`)](ethtool.md#id227)

#### [tx-max (`u32`)](ethtool.md#id228)

#### [other-max (`u32`)](ethtool.md#id229)

#### [combined-max (`u32`)](ethtool.md#id230)

#### [rx-count (`u32`)](ethtool.md#id231)

#### [tx-count (`u32`)](ethtool.md#id232)

#### [other-count (`u32`)](ethtool.md#id233)

#### [combined-count (`u32`)](ethtool.md#id234)

### [coalesce](ethtool.md#id235)

#### [header (`nest`)](ethtool.md#id236)

nested-attributes
:   header

#### [rx-usecs (`u32`)](ethtool.md#id237)

#### [rx-max-frames (`u32`)](ethtool.md#id238)

#### [rx-usecs-irq (`u32`)](ethtool.md#id239)

#### [rx-max-frames-irq (`u32`)](ethtool.md#id240)

#### [tx-usecs (`u32`)](ethtool.md#id241)

#### [tx-max-frames (`u32`)](ethtool.md#id242)

#### [tx-usecs-irq (`u32`)](ethtool.md#id243)

#### [tx-max-frames-irq (`u32`)](ethtool.md#id244)

#### [stats-block-usecs (`u32`)](ethtool.md#id245)

#### [use-adaptive-rx (`u8`)](ethtool.md#id246)

#### [use-adaptive-tx (`u8`)](ethtool.md#id247)

#### [pkt-rate-low (`u32`)](ethtool.md#id248)

#### [rx-usecs-low (`u32`)](ethtool.md#id249)

#### [rx-max-frames-low (`u32`)](ethtool.md#id250)

#### [tx-usecs-low (`u32`)](ethtool.md#id251)

#### [tx-max-frames-low (`u32`)](ethtool.md#id252)

#### [pkt-rate-high (`u32`)](ethtool.md#id253)

#### [rx-usecs-high (`u32`)](ethtool.md#id254)

#### [rx-max-frames-high (`u32`)](ethtool.md#id255)

#### [tx-usecs-high (`u32`)](ethtool.md#id256)

#### [tx-max-frames-high (`u32`)](ethtool.md#id257)

#### [rate-sample-interval (`u32`)](ethtool.md#id258)

#### [use-cqe-mode-tx (`u8`)](ethtool.md#id259)

#### [use-cqe-mode-rx (`u8`)](ethtool.md#id260)

#### [tx-aggr-max-bytes (`u32`)](ethtool.md#id261)

#### [tx-aggr-max-frames (`u32`)](ethtool.md#id262)

#### [tx-aggr-time-usecs (`u32`)](ethtool.md#id263)

### [pause-stat](ethtool.md#id264)

#### [pad (`pad`)](ethtool.md#id265)

#### [tx-frames (`u64`)](ethtool.md#id266)

#### [rx-frames (`u64`)](ethtool.md#id267)

### [pause](ethtool.md#id268)

#### [header (`nest`)](ethtool.md#id269)

nested-attributes
:   header

#### [autoneg (`u8`)](ethtool.md#id270)

#### [rx (`u8`)](ethtool.md#id271)

#### [tx (`u8`)](ethtool.md#id272)

#### [stats (`nest`)](ethtool.md#id273)

nested-attributes
:   pause-stat

#### [stats-src (`u32`)](ethtool.md#id274)

### [eee](ethtool.md#id275)

#### [header (`nest`)](ethtool.md#id276)

nested-attributes
:   header

#### [modes-ours (`nest`)](ethtool.md#id277)

nested-attributes
:   bitset

#### [modes-peer (`nest`)](ethtool.md#id278)

nested-attributes
:   bitset

#### [active (`u8`)](ethtool.md#id279)

#### [enabled (`u8`)](ethtool.md#id280)

#### [tx-lpi-enabled (`u8`)](ethtool.md#id281)

#### [tx-lpi-timer (`u32`)](ethtool.md#id282)

### [tsinfo](ethtool.md#id283)

#### [header (`nest`)](ethtool.md#id284)

nested-attributes
:   header

#### [timestamping (`nest`)](ethtool.md#id285)

nested-attributes
:   bitset

#### [tx-types (`nest`)](ethtool.md#id286)

nested-attributes
:   bitset

#### [rx-filters (`nest`)](ethtool.md#id287)

nested-attributes
:   bitset

#### [phc-index (`u32`)](ethtool.md#id288)

### [cable-result](ethtool.md#id289)

#### [pair (`u8`)](ethtool.md#id290)

#### [code (`u8`)](ethtool.md#id291)

### [cable-fault-length](ethtool.md#id292)

#### [pair (`u8`)](ethtool.md#id293)

#### [cm (`u32`)](ethtool.md#id294)

### [cable-nest](ethtool.md#id295)

#### [result (`nest`)](ethtool.md#id296)

nested-attributes
:   cable-result

#### [fault-length (`nest`)](ethtool.md#id297)

nested-attributes
:   cable-fault-length

### [cable-test](ethtool.md#id298)

#### [header (`nest`)](ethtool.md#id299)

nested-attributes
:   header

### [cable-test-ntf](ethtool.md#id300)

#### [header (`nest`)](ethtool.md#id301)

nested-attributes
:   header

#### [status (`u8`)](ethtool.md#id302)

#### [nest (`nest`)](ethtool.md#id303)

nested-attributes
:   cable-nest

### [cable-test-tdr-cfg](ethtool.md#id304)

#### [first (`u32`)](ethtool.md#id305)

#### [last (`u32`)](ethtool.md#id306)

#### [step (`u32`)](ethtool.md#id307)

#### [pair (`u8`)](ethtool.md#id308)

### [cable-test-tdr-ntf](ethtool.md#id309)

#### [header (`nest`)](ethtool.md#id310)

nested-attributes
:   header

#### [status (`u8`)](ethtool.md#id311)

#### [nest (`nest`)](ethtool.md#id312)

nested-attributes
:   cable-nest

### [cable-test-tdr](ethtool.md#id313)

#### [header (`nest`)](ethtool.md#id314)

nested-attributes
:   header

#### [cfg (`nest`)](ethtool.md#id315)

nested-attributes
:   cable-test-tdr-cfg

### [tunnel-udp-entry](ethtool.md#id316)

#### [port (`u16`)](ethtool.md#id317)

byte-order
:   big-endian

#### [type (`u32`)](ethtool.md#id318)

enum
:   udp-tunnel-type

### [tunnel-udp-table](ethtool.md#id319)

#### [size (`u32`)](ethtool.md#id320)

#### [types (`nest`)](ethtool.md#id321)

nested-attributes
:   bitset

#### [entry (`nest`)](ethtool.md#id322)

multi-attr
:   True

nested-attributes
:   tunnel-udp-entry

### [tunnel-udp](ethtool.md#id323)

#### [table (`nest`)](ethtool.md#id324)

nested-attributes
:   tunnel-udp-table

### [tunnel-info](ethtool.md#id325)

#### [header (`nest`)](ethtool.md#id326)

nested-attributes
:   header

#### [udp-ports (`nest`)](ethtool.md#id327)

nested-attributes
:   tunnel-udp

### [fec-stat](ethtool.md#id328)

#### [pad (`pad`)](ethtool.md#id329)

#### [corrected (`binary`)](ethtool.md#id330)

sub-type
:   u64

#### [uncorr (`binary`)](ethtool.md#id331)

sub-type
:   u64

#### [corr-bits (`binary`)](ethtool.md#id332)

sub-type
:   u64

### [fec](ethtool.md#id333)

#### [header (`nest`)](ethtool.md#id334)

nested-attributes
:   header

#### [modes (`nest`)](ethtool.md#id335)

nested-attributes
:   bitset

#### [auto (`u8`)](ethtool.md#id336)

#### [active (`u32`)](ethtool.md#id337)

#### [stats (`nest`)](ethtool.md#id338)

nested-attributes
:   fec-stat

### [module-eeprom](ethtool.md#id339)

#### [header (`nest`)](ethtool.md#id340)

nested-attributes
:   header

#### [offset (`u32`)](ethtool.md#id341)

#### [length (`u32`)](ethtool.md#id342)

#### [page (`u8`)](ethtool.md#id343)

#### [bank (`u8`)](ethtool.md#id344)

#### [i2c-address (`u8`)](ethtool.md#id345)

#### [data (`binary`)](ethtool.md#id346)

### [stats-grp](ethtool.md#id347)

#### [pad (`pad`)](ethtool.md#id348)

#### [id (`u32`)](ethtool.md#id349)

#### [ss-id (`u32`)](ethtool.md#id350)

#### [stat (`u64`)](ethtool.md#id351)

type-value
:   ['id']

#### [hist-rx (`nest`)](ethtool.md#id352)

nested-attributes
:   stats-grp-hist

#### [hist-tx (`nest`)](ethtool.md#id353)

nested-attributes
:   stats-grp-hist

#### [hist-bkt-low (`u32`)](ethtool.md#id354)

#### [hist-bkt-hi (`u32`)](ethtool.md#id355)

#### [hist-val (`u64`)](ethtool.md#id356)

### [stats-grp-hist](ethtool.md#id357)

#### [hist-bkt-low](ethtool.md#id358)

#### [hist-bkt-hi](ethtool.md#id359)

#### [hist-val](ethtool.md#id360)

### [stats](ethtool.md#id361)

#### [pad (`pad`)](ethtool.md#id362)

#### [header (`nest`)](ethtool.md#id363)

nested-attributes
:   header

#### [groups (`nest`)](ethtool.md#id364)

nested-attributes
:   bitset

#### [grp (`nest`)](ethtool.md#id365)

nested-attributes
:   stats-grp

#### [src (`u32`)](ethtool.md#id366)

### [phc-vclocks](ethtool.md#id367)

#### [header (`nest`)](ethtool.md#id368)

nested-attributes
:   header

#### [num (`u32`)](ethtool.md#id369)

#### [index (`binary`)](ethtool.md#id370)

sub-type
:   s32

### [module](ethtool.md#id371)

#### [header (`nest`)](ethtool.md#id372)

nested-attributes
:   header

#### [power-mode-policy (`u8`)](ethtool.md#id373)

#### [power-mode (`u8`)](ethtool.md#id374)

### [pse](ethtool.md#id375)

#### [header (`nest`)](ethtool.md#id376)

nested-attributes
:   header

#### [admin-state (`u32`)](ethtool.md#id377)

name-prefix
:   ethtool-a-podl-pse-

#### [admin-control (`u32`)](ethtool.md#id378)

name-prefix
:   ethtool-a-podl-pse-

#### [pw-d-status (`u32`)](ethtool.md#id379)

name-prefix
:   ethtool-a-podl-pse-

### [rss](ethtool.md#id380)

#### [header (`nest`)](ethtool.md#id381)

nested-attributes
:   header

#### [context (`u32`)](ethtool.md#id382)

#### [hfunc (`u32`)](ethtool.md#id383)

#### [indir (`binary`)](ethtool.md#id384)

#### [hkey (`binary`)](ethtool.md#id385)

#### [input_xfrm (`u32`)](ethtool.md#id386)

### [plca](ethtool.md#id387)

#### [header (`nest`)](ethtool.md#id388)

nested-attributes
:   header

#### [version (`u16`)](ethtool.md#id389)

#### [enabled (`u8`)](ethtool.md#id390)

#### [status (`u8`)](ethtool.md#id391)

#### [node-cnt (`u32`)](ethtool.md#id392)

#### [node-id (`u32`)](ethtool.md#id393)

#### [to-tmr (`u32`)](ethtool.md#id394)

#### [burst-cnt (`u32`)](ethtool.md#id395)

#### [burst-tmr (`u32`)](ethtool.md#id396)
