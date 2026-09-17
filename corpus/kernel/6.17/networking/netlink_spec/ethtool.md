---
collection: kernel
version: "6.17"
title: "Family ethtool netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/ethtool.html
fetched_at: 2026-09-16T16:40:46+00:00
---
# [Family `ethtool` netlink specification](ethtool.md#id119)

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
    - [module-fw-flash-act](ethtool.md#module-fw-flash-act)
    - [module-fw-flash-ntf](ethtool.md#module-fw-flash-ntf)
    - [phy-get](ethtool.md#phy-get)
    - [phy-ntf](ethtool.md#phy-ntf)
    - [tsconfig-get](ethtool.md#tsconfig-get)
    - [tsconfig-set](ethtool.md#tsconfig-set)
    - [pse-ntf](ethtool.md#pse-ntf)
    - [rss-set](ethtool.md#rss-set)
    - [rss-ntf](ethtool.md#rss-ntf)
    - [rss-create-act](ethtool.md#rss-create-act)
    - [rss-create-ntf](ethtool.md#rss-create-ntf)
    - [rss-delete-act](ethtool.md#rss-delete-act)
    - [rss-delete-ntf](ethtool.md#rss-delete-ntf)
  - [Multicast groups](ethtool.md#multicast-groups)
  - [Definitions](ethtool.md#definitions)

    - [udp-tunnel-type](ethtool.md#udp-tunnel-type)
    - [stringset](ethtool.md#stringset)
    - [header-flags](ethtool.md#header-flags)
    - [module-fw-flash-status](ethtool.md#module-fw-flash-status)
    - [c33-pse-ext-state](ethtool.md#c33-pse-ext-state)
    - [phy-upstream-type](ethtool.md#phy-upstream-type)
    - [tcp-data-split](ethtool.md#tcp-data-split)
    - [hwtstamp-source](ethtool.md#hwtstamp-source)
    - [pse-event](ethtool.md#pse-event)
    - [input-xfrm](ethtool.md#input-xfrm)
    - [rxfh-fields](ethtool.md#rxfh-fields)
  - [Attribute sets](ethtool.md#attribute-sets)

    - [header](ethtool.md#header)
    - [bitset-bit](ethtool.md#bitset-bit)
    - [bitset-bits](ethtool.md#bitset-bits)
    - [bitset](ethtool.md#bitset)
    - [string](ethtool.md#string)
    - [strings](ethtool.md#strings)
    - [stringset](ethtool.md#ethtool-attribute-set-stringset)
    - [stringsets](ethtool.md#stringsets)
    - [strset](ethtool.md#strset)
    - [privflags](ethtool.md#privflags)
    - [rings](ethtool.md#rings)
    - [mm-stat](ethtool.md#mm-stat)
    - [mm](ethtool.md#mm)
    - [linkinfo](ethtool.md#linkinfo)
    - [linkmodes](ethtool.md#linkmodes)
    - [linkstate](ethtool.md#linkstate)
    - [debug](ethtool.md#debug)
    - [wol](ethtool.md#wol)
    - [features](ethtool.md#features)
    - [channels](ethtool.md#channels)
    - [irq-moderation](ethtool.md#irq-moderation)
    - [profile](ethtool.md#profile)
    - [coalesce](ethtool.md#coalesce)
    - [pause-stat](ethtool.md#pause-stat)
    - [pause](ethtool.md#pause)
    - [eee](ethtool.md#eee)
    - [ts-stat](ethtool.md#ts-stat)
    - [ts-hwtstamp-provider](ethtool.md#ts-hwtstamp-provider)
    - [tsinfo](ethtool.md#tsinfo)
    - [cable-result](ethtool.md#cable-result)
    - [cable-fault-length](ethtool.md#cable-fault-length)
    - [cable-nest](ethtool.md#cable-nest)
    - [cable-test](ethtool.md#cable-test)
    - [cable-test-ntf](ethtool.md#ethtool-attribute-set-cable-test-ntf)
    - [cable-test-tdr-cfg](ethtool.md#cable-test-tdr-cfg)
    - [cable-test-tdr-ntf](ethtool.md#ethtool-attribute-set-cable-test-tdr-ntf)
    - [cable-test-tdr](ethtool.md#cable-test-tdr)
    - [tunnel-udp-entry](ethtool.md#tunnel-udp-entry)
    - [tunnel-udp-table](ethtool.md#tunnel-udp-table)
    - [tunnel-udp](ethtool.md#tunnel-udp)
    - [tunnel-info](ethtool.md#tunnel-info)
    - [fec-stat](ethtool.md#fec-stat)
    - [fec](ethtool.md#fec)
    - [module-eeprom](ethtool.md#module-eeprom)
    - [stats-grp](ethtool.md#stats-grp)
    - [stats-grp-hist](ethtool.md#stats-grp-hist)
    - [stats](ethtool.md#stats)
    - [phc-vclocks](ethtool.md#phc-vclocks)
    - [module](ethtool.md#module)
    - [c33-pse-pw-limit](ethtool.md#c33-pse-pw-limit)
    - [pse](ethtool.md#pse)
    - [flow](ethtool.md#flow)
    - [rss](ethtool.md#rss)
    - [plca](ethtool.md#plca)
    - [module-fw-flash](ethtool.md#module-fw-flash)
    - [phy](ethtool.md#phy)
    - [tsconfig](ethtool.md#tsconfig)
    - [pse-ntf](ethtool.md#ethtool-attribute-set-pse-ntf)

## [Summary](ethtool.md#id120)

Partial family for Ethtool Netlink.

## [Operations](ethtool.md#id121)

### [strset-get](ethtool.md#id122)

Get string set from the kernel.

attribute-set:
:   [strset](ethtool.md#ethtool-attribute-set-strset)

do:
:   **request**
    :   attributes:
        :   [`header`, `stringsets`, `counts-only`]

    **reply**
    :   attributes:
        :   [`header`, `stringsets`]

dump:
:   **request**
    :   attributes:
        :   [`header`, `stringsets`, `counts-only`]

    **reply**
    :   attributes:
        :   [`header`, `stringsets`]

### [linkinfo-get](ethtool.md#id123)

Get link info.

attribute-set:
:   [linkinfo](ethtool.md#ethtool-attribute-set-linkinfo)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `port`, `phyaddr`, `tp-mdix`, `tp-mdix-ctrl`, `transceiver`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `port`, `phyaddr`, `tp-mdix`, `tp-mdix-ctrl`, `transceiver`]

### [linkinfo-set](ethtool.md#id124)

Set link info.

attribute-set:
:   [linkinfo](ethtool.md#ethtool-attribute-set-linkinfo)

do:
:   **request**
    :   attributes:
        :   [`header`, `port`, `phyaddr`, `tp-mdix`, `tp-mdix-ctrl`, `transceiver`]

### [linkinfo-ntf](ethtool.md#id125)

Notification for change in link info.

notify:
:   linkinfo-get

### [linkmodes-get](ethtool.md#id126)

Get link modes.

attribute-set:
:   [linkmodes](ethtool.md#ethtool-attribute-set-linkmodes)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `autoneg`, `ours`, `peer`, `speed`, `duplex`, `master-slave-cfg`, `master-slave-state`, `lanes`, `rate-matching`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `autoneg`, `ours`, `peer`, `speed`, `duplex`, `master-slave-cfg`, `master-slave-state`, `lanes`, `rate-matching`]

### [linkmodes-set](ethtool.md#id127)

Set link modes.

attribute-set:
:   [linkmodes](ethtool.md#ethtool-attribute-set-linkmodes)

do:
:   **request**
    :   attributes:
        :   [`header`, `autoneg`, `ours`, `peer`, `speed`, `duplex`, `master-slave-cfg`, `master-slave-state`, `lanes`, `rate-matching`]

### [linkmodes-ntf](ethtool.md#id128)

Notification for change in link modes.

notify:
:   linkmodes-get

### [linkstate-get](ethtool.md#id129)

Get link state.

attribute-set:
:   [linkstate](ethtool.md#ethtool-attribute-set-linkstate)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `link`, `sqi`, `sqi-max`, `ext-state`, `ext-substate`, `ext-down-cnt`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `link`, `sqi`, `sqi-max`, `ext-state`, `ext-substate`, `ext-down-cnt`]

### [debug-get](ethtool.md#id130)

Get debug message mask.

attribute-set:
:   [debug](ethtool.md#ethtool-attribute-set-debug)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `msgmask`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `msgmask`]

### [debug-set](ethtool.md#id131)

Set debug message mask.

attribute-set:
:   [debug](ethtool.md#ethtool-attribute-set-debug)

do:
:   **request**
    :   attributes:
        :   [`header`, `msgmask`]

### [debug-ntf](ethtool.md#id132)

Notification for change in debug message mask.

notify:
:   debug-get

### [wol-get](ethtool.md#id133)

Get WOL params.

attribute-set:
:   [wol](ethtool.md#ethtool-attribute-set-wol)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `modes`, `sopass`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `modes`, `sopass`]

### [wol-set](ethtool.md#id134)

Set WOL params.

attribute-set:
:   [wol](ethtool.md#ethtool-attribute-set-wol)

do:
:   **request**
    :   attributes:
        :   [`header`, `modes`, `sopass`]

### [wol-ntf](ethtool.md#id135)

Notification for change in WOL params.

notify:
:   wol-get

### [features-get](ethtool.md#id136)

Get features.

attribute-set:
:   [features](ethtool.md#ethtool-attribute-set-features)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `hw`, `wanted`, `active`, `nochange`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `hw`, `wanted`, `active`, `nochange`]

### [features-set](ethtool.md#id137)

Set features.

attribute-set:
:   [features](ethtool.md#ethtool-attribute-set-features)

do:
:   **request**
    :   attributes:
        :   [`header`, `hw`, `wanted`, `active`, `nochange`]

    **reply**
    :   attributes:
        :   [`header`, `hw`, `wanted`, `active`, `nochange`]

### [features-ntf](ethtool.md#id138)

Notification for change in features.

notify:
:   features-get

### [privflags-get](ethtool.md#id139)

Get device private flags.

attribute-set:
:   [privflags](ethtool.md#ethtool-attribute-set-privflags)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `flags`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `flags`]

### [privflags-set](ethtool.md#id140)

Set device private flags.

attribute-set:
:   [privflags](ethtool.md#ethtool-attribute-set-privflags)

do:
:   **request**
    :   attributes:
        :   [`header`, `flags`]

### [privflags-ntf](ethtool.md#id141)

Notification for change in device private flags.

notify:
:   privflags-get

### [rings-get](ethtool.md#id142)

Get ring params.

attribute-set:
:   [rings](ethtool.md#ethtool-attribute-set-rings)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `rx-max`, `rx-mini-max`, `rx-jumbo-max`, `tx-max`, `rx`, `rx-mini`, `rx-jumbo`, `tx`, `rx-buf-len`, `tcp-data-split`, `cqe-size`, `tx-push`, `rx-push`, `tx-push-buf-len`, `tx-push-buf-len-max`, `hds-thresh`, `hds-thresh-max`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `rx-max`, `rx-mini-max`, `rx-jumbo-max`, `tx-max`, `rx`, `rx-mini`, `rx-jumbo`, `tx`, `rx-buf-len`, `tcp-data-split`, `cqe-size`, `tx-push`, `rx-push`, `tx-push-buf-len`, `tx-push-buf-len-max`, `hds-thresh`, `hds-thresh-max`]

### [rings-set](ethtool.md#id143)

Set ring params.

attribute-set:
:   [rings](ethtool.md#ethtool-attribute-set-rings)

do:
:   **request**
    :   attributes:
        :   [`header`, `rx-max`, `rx-mini-max`, `rx-jumbo-max`, `tx-max`, `rx`, `rx-mini`, `rx-jumbo`, `tx`, `rx-buf-len`, `tcp-data-split`, `cqe-size`, `tx-push`, `rx-push`, `tx-push-buf-len`, `tx-push-buf-len-max`, `hds-thresh`, `hds-thresh-max`]

### [rings-ntf](ethtool.md#id144)

Notification for change in ring params.

notify:
:   rings-get

### [channels-get](ethtool.md#id145)

Get channel params.

attribute-set:
:   [channels](ethtool.md#ethtool-attribute-set-channels)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `rx-max`, `tx-max`, `other-max`, `combined-max`, `rx-count`, `tx-count`, `other-count`, `combined-count`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `rx-max`, `tx-max`, `other-max`, `combined-max`, `rx-count`, `tx-count`, `other-count`, `combined-count`]

### [channels-set](ethtool.md#id146)

Set channel params.

attribute-set:
:   [channels](ethtool.md#ethtool-attribute-set-channels)

do:
:   **request**
    :   attributes:
        :   [`header`, `rx-max`, `tx-max`, `other-max`, `combined-max`, `rx-count`, `tx-count`, `other-count`, `combined-count`]

### [channels-ntf](ethtool.md#id147)

Notification for change in channel params.

notify:
:   channels-get

### [coalesce-get](ethtool.md#id148)

Get coalesce params.

attribute-set:
:   [coalesce](ethtool.md#ethtool-attribute-set-coalesce)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `rx-usecs`, `rx-max-frames`, `rx-usecs-irq`, `rx-max-frames-irq`, `tx-usecs`, `tx-max-frames`, `tx-usecs-irq`, `tx-max-frames-irq`, `stats-block-usecs`, `use-adaptive-rx`, `use-adaptive-tx`, `pkt-rate-low`, `rx-usecs-low`, `rx-max-frames-low`, `tx-usecs-low`, `tx-max-frames-low`, `pkt-rate-high`, `rx-usecs-high`, `rx-max-frames-high`, `tx-usecs-high`, `tx-max-frames-high`, `rate-sample-interval`, `use-cqe-mode-tx`, `use-cqe-mode-rx`, `tx-aggr-max-bytes`, `tx-aggr-max-frames`, `tx-aggr-time-usecs`, `rx-profile`, `tx-profile`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `rx-usecs`, `rx-max-frames`, `rx-usecs-irq`, `rx-max-frames-irq`, `tx-usecs`, `tx-max-frames`, `tx-usecs-irq`, `tx-max-frames-irq`, `stats-block-usecs`, `use-adaptive-rx`, `use-adaptive-tx`, `pkt-rate-low`, `rx-usecs-low`, `rx-max-frames-low`, `tx-usecs-low`, `tx-max-frames-low`, `pkt-rate-high`, `rx-usecs-high`, `rx-max-frames-high`, `tx-usecs-high`, `tx-max-frames-high`, `rate-sample-interval`, `use-cqe-mode-tx`, `use-cqe-mode-rx`, `tx-aggr-max-bytes`, `tx-aggr-max-frames`, `tx-aggr-time-usecs`, `rx-profile`, `tx-profile`]

### [coalesce-set](ethtool.md#id149)

Set coalesce params.

attribute-set:
:   [coalesce](ethtool.md#ethtool-attribute-set-coalesce)

do:
:   **request**
    :   attributes:
        :   [`header`, `rx-usecs`, `rx-max-frames`, `rx-usecs-irq`, `rx-max-frames-irq`, `tx-usecs`, `tx-max-frames`, `tx-usecs-irq`, `tx-max-frames-irq`, `stats-block-usecs`, `use-adaptive-rx`, `use-adaptive-tx`, `pkt-rate-low`, `rx-usecs-low`, `rx-max-frames-low`, `tx-usecs-low`, `tx-max-frames-low`, `pkt-rate-high`, `rx-usecs-high`, `rx-max-frames-high`, `tx-usecs-high`, `tx-max-frames-high`, `rate-sample-interval`, `use-cqe-mode-tx`, `use-cqe-mode-rx`, `tx-aggr-max-bytes`, `tx-aggr-max-frames`, `tx-aggr-time-usecs`, `rx-profile`, `tx-profile`]

### [coalesce-ntf](ethtool.md#id150)

Notification for change in coalesce params.

notify:
:   coalesce-get

### [pause-get](ethtool.md#id151)

Get pause params.

attribute-set:
:   [pause](ethtool.md#ethtool-attribute-set-pause)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `autoneg`, `rx`, `tx`, `stats`, `stats-src`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `autoneg`, `rx`, `tx`, `stats`, `stats-src`]

### [pause-set](ethtool.md#id152)

Set pause params.

attribute-set:
:   [pause](ethtool.md#ethtool-attribute-set-pause)

do:
:   **request**
    :   attributes:
        :   [`header`, `autoneg`, `rx`, `tx`, `stats`, `stats-src`]

### [pause-ntf](ethtool.md#id153)

Notification for change in pause params.

notify:
:   pause-get

### [eee-get](ethtool.md#id154)

Get eee params.

attribute-set:
:   [eee](ethtool.md#ethtool-attribute-set-eee)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `modes-ours`, `modes-peer`, `active`, `enabled`, `tx-lpi-enabled`, `tx-lpi-timer`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `modes-ours`, `modes-peer`, `active`, `enabled`, `tx-lpi-enabled`, `tx-lpi-timer`]

### [eee-set](ethtool.md#id155)

Set eee params.

attribute-set:
:   [eee](ethtool.md#ethtool-attribute-set-eee)

do:
:   **request**
    :   attributes:
        :   [`header`, `modes-ours`, `modes-peer`, `active`, `enabled`, `tx-lpi-enabled`, `tx-lpi-timer`]

### [eee-ntf](ethtool.md#id156)

Notification for change in eee params.

notify:
:   eee-get

### [tsinfo-get](ethtool.md#id157)

Get tsinfo params.

attribute-set:
:   [tsinfo](ethtool.md#ethtool-attribute-set-tsinfo)

do:
:   **request**
    :   attributes:
        :   [`header`, `hwtstamp-provider`]

    **reply**
    :   attributes:
        :   [`header`, `timestamping`, `tx-types`, `rx-filters`, `phc-index`, `stats`, `hwtstamp-provider`, `hwtstamp-source`, `hwtstamp-phyindex`]

dump:
:   **request**
    :   attributes:
        :   [`header`, `hwtstamp-provider`]

    **reply**
    :   attributes:
        :   [`header`, `timestamping`, `tx-types`, `rx-filters`, `phc-index`, `stats`, `hwtstamp-provider`, `hwtstamp-source`, `hwtstamp-phyindex`]

### [cable-test-act](ethtool.md#id158)

Cable test.

attribute-set:
:   [cable-test](ethtool.md#ethtool-attribute-set-cable-test)

do:
:   **request**
    :   attributes:
        :   [`header`]

### [cable-test-ntf](ethtool.md#id159)

Cable test notification.

attribute-set:
:   [cable-test-ntf](ethtool.md#ethtool-attribute-set-cable-test-ntf)

event:
:   {‘attributes’: [‘header’, ‘status’]}

### [cable-test-tdr-act](ethtool.md#id160)

Cable test TDR.

attribute-set:
:   [cable-test-tdr](ethtool.md#ethtool-attribute-set-cable-test-tdr)

do:
:   **request**
    :   attributes:
        :   [`header`]

### [cable-test-tdr-ntf](ethtool.md#id161)

Cable test TDR notification.

attribute-set:
:   [cable-test-tdr-ntf](ethtool.md#ethtool-attribute-set-cable-test-tdr-ntf)

event:
:   {‘attributes’: [‘header’, ‘status’, ‘nest’]}

### [tunnel-info-get](ethtool.md#id162)

Get tsinfo params.

attribute-set:
:   [tunnel-info](ethtool.md#ethtool-attribute-set-tunnel-info)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `udp-ports`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `udp-ports`]

### [fec-get](ethtool.md#id163)

Get FEC params.

attribute-set:
:   [fec](ethtool.md#ethtool-attribute-set-fec)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `modes`, `auto`, `active`, `stats`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `modes`, `auto`, `active`, `stats`]

### [fec-set](ethtool.md#id164)

Set FEC params.

attribute-set:
:   [fec](ethtool.md#ethtool-attribute-set-fec)

do:
:   **request**
    :   attributes:
        :   [`header`, `modes`, `auto`, `active`, `stats`]

### [fec-ntf](ethtool.md#id165)

Notification for change in FEC params.

notify:
:   fec-get

### [module-eeprom-get](ethtool.md#id166)

Get module EEPROM params.

attribute-set:
:   [module-eeprom](ethtool.md#ethtool-attribute-set-module-eeprom)

do:
:   **request**
    :   attributes:
        :   [`header`, `offset`, `length`, `page`, `bank`, `i2c-address`]

    **reply**
    :   attributes:
        :   [`header`, `data`]

dump:
:   **request**
    :   attributes:
        :   [`header`, `offset`, `length`, `page`, `bank`, `i2c-address`]

    **reply**
    :   attributes:
        :   [`header`, `data`]

### [stats-get](ethtool.md#id167)

Get statistics.

attribute-set:
:   [stats](ethtool.md#ethtool-attribute-set-stats)

do:
:   **request**
    :   attributes:
        :   [`header`, `groups`]

    **reply**
    :   attributes:
        :   [`header`, `groups`, `grp`, `src`]

dump:
:   **request**
    :   attributes:
        :   [`header`, `groups`]

    **reply**
    :   attributes:
        :   [`header`, `groups`, `grp`, `src`]

### [phc-vclocks-get](ethtool.md#id168)

Get PHC VCLOCKs.

attribute-set:
:   [phc-vclocks](ethtool.md#ethtool-attribute-set-phc-vclocks)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `num`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `num`]

### [module-get](ethtool.md#id169)

Get module params.

attribute-set:
:   [module](ethtool.md#ethtool-attribute-set-module)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `power-mode-policy`, `power-mode`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `power-mode-policy`, `power-mode`]

### [module-set](ethtool.md#id170)

Set module params.

attribute-set:
:   [module](ethtool.md#ethtool-attribute-set-module)

do:
:   **request**
    :   attributes:
        :   [`header`, `power-mode-policy`, `power-mode`]

### [module-ntf](ethtool.md#id171)

Notification for change in module params.

notify:
:   module-get

### [pse-get](ethtool.md#id172)

Get Power Sourcing Equipment params.

attribute-set:
:   [pse](ethtool.md#ethtool-attribute-set-pse)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `podl-pse-admin-state`, `podl-pse-admin-control`, `podl-pse-pw-d-status`, `c33-pse-admin-state`, `c33-pse-admin-control`, `c33-pse-pw-d-status`, `c33-pse-pw-class`, `c33-pse-actual-pw`, `c33-pse-ext-state`, `c33-pse-ext-substate`, `c33-pse-avail-pw-limit`, `c33-pse-pw-limit-ranges`, `pse-pw-d-id`, `pse-prio-max`, `pse-prio`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `podl-pse-admin-state`, `podl-pse-admin-control`, `podl-pse-pw-d-status`, `c33-pse-admin-state`, `c33-pse-admin-control`, `c33-pse-pw-d-status`, `c33-pse-pw-class`, `c33-pse-actual-pw`, `c33-pse-ext-state`, `c33-pse-ext-substate`, `c33-pse-avail-pw-limit`, `c33-pse-pw-limit-ranges`, `pse-pw-d-id`, `pse-prio-max`, `pse-prio`]

### [pse-set](ethtool.md#id173)

Set Power Sourcing Equipment params.

attribute-set:
:   [pse](ethtool.md#ethtool-attribute-set-pse)

do:
:   **request**
    :   attributes:
        :   [`header`, `podl-pse-admin-control`, `c33-pse-admin-control`, `c33-pse-avail-pw-limit`, `pse-prio`]

### [rss-get](ethtool.md#id174)

Get RSS params.

attribute-set:
:   [rss](ethtool.md#ethtool-attribute-set-rss)

do:
:   **request**
    :   attributes:
        :   [`header`, `context`]

    **reply**
    :   attributes:
        :   [`header`, `context`, `hfunc`, `indir`, `hkey`, `input-xfrm`, `flow-hash`]

dump:
:   **request**
    :   attributes:
        :   [`header`, `start-context`]

    **reply**
    :   attributes:
        :   [`header`, `context`, `hfunc`, `indir`, `hkey`, `input-xfrm`, `flow-hash`]

### [plca-get-cfg](ethtool.md#id175)

Get PLCA params.

attribute-set:
:   [plca](ethtool.md#ethtool-attribute-set-plca)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `version`, `enabled`, `status`, `node-cnt`, `node-id`, `to-tmr`, `burst-cnt`, `burst-tmr`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `version`, `enabled`, `status`, `node-cnt`, `node-id`, `to-tmr`, `burst-cnt`, `burst-tmr`]

### [plca-set-cfg](ethtool.md#id176)

Set PLCA params.

attribute-set:
:   [plca](ethtool.md#ethtool-attribute-set-plca)

do:
:   **request**
    :   attributes:
        :   [`header`, `version`, `enabled`, `status`, `node-cnt`, `node-id`, `to-tmr`, `burst-cnt`, `burst-tmr`]

### [plca-get-status](ethtool.md#id177)

Get PLCA status params.

attribute-set:
:   [plca](ethtool.md#ethtool-attribute-set-plca)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `version`, `enabled`, `status`, `node-cnt`, `node-id`, `to-tmr`, `burst-cnt`, `burst-tmr`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `version`, `enabled`, `status`, `node-cnt`, `node-id`, `to-tmr`, `burst-cnt`, `burst-tmr`]

### [plca-ntf](ethtool.md#id178)

Notification for change in PLCA params.

notify:
:   plca-get-cfg

### [mm-get](ethtool.md#id179)

Get MAC Merge configuration and state

attribute-set:
:   [mm](ethtool.md#ethtool-attribute-set-mm)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `pmac-enabled`, `tx-enabled`, `tx-active`, `tx-min-frag-size`, `rx-min-frag-size`, `verify-enabled`, `verify-time`, `max-verify-time`, `stats`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `pmac-enabled`, `tx-enabled`, `tx-active`, `tx-min-frag-size`, `rx-min-frag-size`, `verify-enabled`, `verify-time`, `max-verify-time`, `stats`]

### [mm-set](ethtool.md#id180)

Set MAC Merge configuration

attribute-set:
:   [mm](ethtool.md#ethtool-attribute-set-mm)

do:
:   **request**
    :   attributes:
        :   [`header`, `verify-enabled`, `verify-time`, `tx-enabled`, `pmac-enabled`, `tx-min-frag-size`]

### [mm-ntf](ethtool.md#id181)

Notification for change in MAC Merge configuration.

notify:
:   mm-get

### [module-fw-flash-act](ethtool.md#id182)

Flash transceiver module firmware.

attribute-set:
:   [module-fw-flash](ethtool.md#ethtool-attribute-set-module-fw-flash)

do:
:   **request**
    :   attributes:
        :   [`header`, `file-name`, `password`]

### [module-fw-flash-ntf](ethtool.md#id183)

Notification for firmware flashing progress and status.

attribute-set:
:   [module-fw-flash](ethtool.md#ethtool-attribute-set-module-fw-flash)

event:
:   {‘attributes’: [‘header’, ‘status’, ‘status-msg’, ‘done’, ‘total’]}

### [phy-get](ethtool.md#id184)

Get PHY devices attached to an interface

attribute-set:
:   [phy](ethtool.md#ethtool-attribute-set-phy)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `index`, `drvname`, `name`, `upstream-type`, `upstream-index`, `upstream-sfp-name`, `downstream-sfp-name`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `index`, `drvname`, `name`, `upstream-type`, `upstream-index`, `upstream-sfp-name`, `downstream-sfp-name`]

### [phy-ntf](ethtool.md#id185)

Notification for change in PHY devices.

notify:
:   phy-get

### [tsconfig-get](ethtool.md#id186)

Get hwtstamp config.

attribute-set:
:   [tsconfig](ethtool.md#ethtool-attribute-set-tsconfig)

do:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `hwtstamp-provider`, `tx-types`, `rx-filters`, `hwtstamp-flags`]

dump:
:   **request**
    :   attributes:
        :   [`header`]

    **reply**
    :   attributes:
        :   [`header`, `hwtstamp-provider`, `tx-types`, `rx-filters`, `hwtstamp-flags`]

### [tsconfig-set](ethtool.md#id187)

Set hwtstamp config.

attribute-set:
:   [tsconfig](ethtool.md#ethtool-attribute-set-tsconfig)

do:
:   **request**
    :   attributes:
        :   [`header`, `hwtstamp-provider`, `tx-types`, `rx-filters`, `hwtstamp-flags`]

    **reply**
    :   attributes:
        :   [`header`, `hwtstamp-provider`, `tx-types`, `rx-filters`, `hwtstamp-flags`]

### [pse-ntf](ethtool.md#id188)

Notification for PSE events.

attribute-set:
:   [pse-ntf](ethtool.md#ethtool-attribute-set-pse-ntf)

event:
:   {‘attributes’: [‘header’, ‘events’]}

### [rss-set](ethtool.md#id189)

Set RSS params.

attribute-set:
:   [rss](ethtool.md#ethtool-attribute-set-rss)

do:
:   **request**
    :   attributes:
        :   [`header`, `context`, `hfunc`, `indir`, `hkey`, `input-xfrm`, `flow-hash`]

### [rss-ntf](ethtool.md#id190)

Notification for change in RSS configuration.
For additional contexts only modifications use this notification,
creation and deletion have dedicated messages.

notify:
:   rss-get

### [rss-create-act](ethtool.md#id191)

Create an RSS context.

attribute-set:
:   [rss](ethtool.md#ethtool-attribute-set-rss)

do:
:   **request**
    :   attributes:
        :   [`header`, `context`, `hfunc`, `indir`, `hkey`, `input-xfrm`]

    **reply**
    :   attributes:
        :   [`header`, `context`, `hfunc`, `indir`, `hkey`, `input-xfrm`]

### [rss-create-ntf](ethtool.md#id192)

Notification for creation of an additional RSS context.

notify:
:   rss-create-act

### [rss-delete-act](ethtool.md#id193)

Delete an RSS context.

attribute-set:
:   [rss](ethtool.md#ethtool-attribute-set-rss)

do:
:   **request**
    :   attributes:
        :   [`header`, `context`]

### [rss-delete-ntf](ethtool.md#id194)

Notification for deletion of an additional RSS context.

attribute-set:
:   [rss](ethtool.md#ethtool-attribute-set-rss)

event:
:   {‘attributes’: [‘header’, ‘context’]}

## [Multicast groups](ethtool.md#id195)

- monitor

## [Definitions](ethtool.md#id196)

### [udp-tunnel-type](ethtool.md#id197)

enum-name:
:   None

type:
:   enum

enum-cnt-name:
:   __ethtool-udp-tunnel-type-cnt

entries:
:   - `vxlan`
    - `geneve`
    - `vxlan-gpe`

### [stringset](ethtool.md#id198)

type:
:   enum

header:
:   linux/ethtool.h

entries:

### [header-flags](ethtool.md#id199)

type:
:   flags

name-prefix:
:   ethtool-flag-

doc:
:   common ethtool header flags

entries:
:   compact-bitsets:
    :   use compact bitsets in reply

    omit-reply:
    :   provide optional reply for SET or ACT requests

    stats:
    :   request statistics, if supported by the driver

### [module-fw-flash-status](ethtool.md#id200)

type:
:   enum

doc:
:   plug-in module firmware flashing status

header:
:   linux/ethtool.h

entries:
:   started:
    :   The firmware flashing process has started.

    in-progress:
    :   The firmware flashing process is in progress.

    completed:
    :   The firmware flashing process was completed successfully.

    error:
    :   The firmware flashing process was stopped due to an error.

### [c33-pse-ext-state](ethtool.md#id201)

doc:
:   “groups of PSE extended states functions. IEEE 802.3-2022 33.2.4.4 Variables”

type:
:   enum

name-prefix:
:   ethtool-c33-pse-ext-state-

header:
:   linux/ethtool.h

entries:
:   none:
    :   none

    error-condition:
    :   Group of error_condition states

    mr-mps-valid:
    :   Group of mr_mps_valid states

    mr-pse-enable:
    :   Group of mr_pse_enable states

    option-detect-ted:
    :   Group of option_detect_ted states

    option-vport-lim:
    :   Group of option_vport_lim states

    ovld-detected:
    :   Group of ovld_detected states

    power-not-available:
    :   Group of power_not_available states

    short-detected:
    :   Group of short_detected states

### [phy-upstream-type](ethtool.md#id202)

enum-name:
:   phy-upstream

header:
:   linux/ethtool.h

type:
:   enum

name-prefix:
:   phy-upstream

entries:
:   - `mac`
    - `phy`

### [tcp-data-split](ethtool.md#id203)

type:
:   enum

entries:
:   - `unknown`
    - `disabled`
    - `enabled`

### [hwtstamp-source](ethtool.md#id204)

doc:
:   Source of the hardware timestamp

enum-name:
:   hwtstamp-source

name-prefix:
:   hwtstamp-source-

type:
:   enum

entries:
:   netdev:
    :   Hardware timestamp comes from a MAC or a device which has MAC and PHY integrated

    phylib:
    :   Hardware timestamp comes from one PHY device of the network topology

### [pse-event](ethtool.md#id205)

doc:
:   PSE event list for the PSE controller

type:
:   flags

name-prefix:
:   ethtool-

entries:
:   pse-event-over-current:
    :   PSE output current is too high

    pse-event-over-temp:
    :   PSE in over temperature state

    c33-pse-event-detection:
    :   detection process occur on the PSE. IEEE 802.3-2022 33.2.5 and 145.2.6 PSE detection of PDs. IEEE 802.3-202 30.9.1.1.5 aPSEPowerDetectionStatus

    c33-pse-event-classification:
    :   classification process occur on the PSE. IEEE 802.3-2022 33.2.6 and 145.2.8 classification of PDs mutual identification. IEEE 802.3-2022 30.9.1.1.8 aPSEPowerClassification.

    c33-pse-event-disconnection:
    :   PD has been disconnected on the PSE. IEEE 802.3-2022 33.3.8 and 145.3.9 PD Maintain Power Signature. IEEE 802.3-2022 33.5.1.2.9 MPS Absent. IEEE 802.3-2022 30.9.1.1.20 aPSEMPSAbsentCounter.

    pse-event-over-budget:
    :   PSE turned off due to over budget situation

    pse-event-sw-pw-control-error:
    :   PSE faced an error managing the power control from software

### [input-xfrm](ethtool.md#id206)

doc:
:   RSS hash function transformations.

type:
:   flags

enum-name:
:   None

name-prefix:
:   rxh-xfrm-

header:
:   linux/ethtool.h

entries:
:   sym-xor:
    :   XOR the corresponding source and destination fields of each specified protocol. Both copies of the XOR’ed fields are fed into the RSS and RXHASH calculation. Note that this XORing reduces the input set entropy and could be exploited to reduce the RSS queue spread.

    sym-or-xor:
    :   Similar to SYM_XOR, except that one copy of the XOR’ed fields is replaced by an OR of the same fields.

### [rxfh-fields](ethtool.md#id207)

name-prefix:
:   rxh-

enum-name:
:   None

header:
:   linux/ethtool.h

type:
:   flags

entries:
:   l2da:

    vlan:

    l3-proto:

    ip-src:

    ip-dst:

    l4-b-0-1:
    :   src port in case of TCP/UDP/SCTP

    l4-b-2-3:
    :   dst port in case of TCP/UDP/SCTP

    gtp-teid:

    discard:

## [Attribute sets](ethtool.md#id208)

### [header](ethtool.md#id209)

#### unspec (`unused`)

value:
:   0

#### dev-index (`u32`)

#### dev-name (`string`)

#### flags (`u32`)

enum:
:   [header-flags](ethtool.md#ethtool-definition-header-flags)

#### phy-index (`u32`)

### [bitset-bit](ethtool.md#id210)

#### unspec (`unused`)

value:
:   0

#### index (`u32`)

#### name (`string`)

#### value (`flag`)

### [bitset-bits](ethtool.md#id211)

#### unspec (`unused`)

value:
:   0

#### bit (`nest`)

multi-attr:
:   True

nested-attributes:
:   [bitset-bit](ethtool.md#ethtool-attribute-set-bitset-bit)

### [bitset](ethtool.md#id212)

#### unspec (`unused`)

value:
:   0

#### nomask (`flag`)

#### size (`u32`)

#### bits (`nest`)

nested-attributes:
:   [bitset-bits](ethtool.md#ethtool-attribute-set-bitset-bits)

#### value (`binary`)

#### mask (`binary`)

### [string](ethtool.md#id213)

#### unspec (`unused`)

value:
:   0

#### index (`u32`)

#### value (`string`)

### [strings](ethtool.md#id214)

#### unspec (`unused`)

value:
:   0

#### unspec (`unused`)

value:
:   0

#### string (`nest`)

multi-attr:
:   True

nested-attributes:
:   [string](ethtool.md#ethtool-attribute-set-string)

### [stringset](ethtool.md#id215)

#### unspec (`unused`)

value:
:   0

#### id (`u32`)

#### count (`u32`)

#### strings (`nest`)

multi-attr:
:   True

nested-attributes:
:   [strings](ethtool.md#ethtool-attribute-set-strings)

### [stringsets](ethtool.md#id216)

#### unspec (`unused`)

value:
:   0

#### stringset (`nest`)

multi-attr:
:   True

nested-attributes:
:   [stringset](ethtool.md#ethtool-attribute-set-stringset)

### [strset](ethtool.md#id217)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### stringsets (`nest`)

nested-attributes:
:   [stringsets](ethtool.md#ethtool-attribute-set-stringsets)

#### counts-only (`flag`)

### [privflags](ethtool.md#id218)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### flags (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

### [rings](ethtool.md#id219)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### rx-max (`u32`)

#### rx-mini-max (`u32`)

#### rx-jumbo-max (`u32`)

#### tx-max (`u32`)

#### rx (`u32`)

#### rx-mini (`u32`)

#### rx-jumbo (`u32`)

#### tx (`u32`)

#### rx-buf-len (`u32`)

#### tcp-data-split (`u8`)

enum:
:   [tcp-data-split](ethtool.md#ethtool-definition-tcp-data-split)

#### cqe-size (`u32`)

#### tx-push (`u8`)

#### rx-push (`u8`)

#### tx-push-buf-len (`u32`)

#### tx-push-buf-len-max (`u32`)

#### hds-thresh (`u32`)

#### hds-thresh-max (`u32`)

### [mm-stat](ethtool.md#id220)

#### unspec (`unused`)

value:
:   0

#### pad (`pad`)

#### reassembly-errors (`u64`)

doc:
:   aMACMergeFrameAssErrorCount

#### smd-errors (`u64`)

doc:
:   aMACMergeFrameSmdErrorCount

#### reassembly-ok (`u64`)

doc:
:   aMACMergeFrameAssOkCount

#### rx-frag-count (`u64`)

doc:
:   aMACMergeFragCountRx

#### tx-frag-count (`u64`)

doc:
:   aMACMergeFragCountTx

#### hold-count (`u64`)

doc:
:   aMACMergeHoldCount

### [mm](ethtool.md#id221)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### pmac-enabled (`u8`)

#### tx-enabled (`u8`)

#### tx-active (`u8`)

#### tx-min-frag-size (`u32`)

#### rx-min-frag-size (`u32`)

#### verify-enabled (`u8`)

#### verify-status (`u8`)

#### verify-time (`u32`)

#### max-verify-time (`u32`)

#### stats (`nest`)

nested-attributes:
:   [mm-stat](ethtool.md#ethtool-attribute-set-mm-stat)

### [linkinfo](ethtool.md#id222)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### port (`u8`)

#### phyaddr (`u8`)

#### tp-mdix (`u8`)

#### tp-mdix-ctrl (`u8`)

#### transceiver (`u8`)

### [linkmodes](ethtool.md#id223)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### autoneg (`u8`)

#### ours (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### peer (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### speed (`u32`)

#### duplex (`u8`)

#### master-slave-cfg (`u8`)

#### master-slave-state (`u8`)

#### lanes (`u32`)

#### rate-matching (`u8`)

### [linkstate](ethtool.md#id224)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### link (`u8`)

#### sqi (`u32`)

#### sqi-max (`u32`)

#### ext-state (`u8`)

#### ext-substate (`u8`)

#### ext-down-cnt (`u32`)

### [debug](ethtool.md#id225)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### msgmask (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

### [wol](ethtool.md#id226)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### modes (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### sopass (`binary`)

### [features](ethtool.md#id227)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### hw (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### wanted (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### active (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### nochange (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

### [channels](ethtool.md#id228)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### rx-max (`u32`)

#### tx-max (`u32`)

#### other-max (`u32`)

#### combined-max (`u32`)

#### rx-count (`u32`)

#### tx-count (`u32`)

#### other-count (`u32`)

#### combined-count (`u32`)

### [irq-moderation](ethtool.md#id229)

#### unspec (`unused`)

value:
:   0

#### usec (`u32`)

#### pkts (`u32`)

#### comps (`u32`)

### [profile](ethtool.md#id230)

#### unspec (`unused`)

value:
:   0

#### irq-moderation (`nest`)

multi-attr:
:   True

nested-attributes:
:   [irq-moderation](ethtool.md#ethtool-attribute-set-irq-moderation)

### [coalesce](ethtool.md#id231)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### rx-usecs (`u32`)

#### rx-max-frames (`u32`)

#### rx-usecs-irq (`u32`)

#### rx-max-frames-irq (`u32`)

#### tx-usecs (`u32`)

#### tx-max-frames (`u32`)

#### tx-usecs-irq (`u32`)

#### tx-max-frames-irq (`u32`)

#### stats-block-usecs (`u32`)

#### use-adaptive-rx (`u8`)

#### use-adaptive-tx (`u8`)

#### pkt-rate-low (`u32`)

#### rx-usecs-low (`u32`)

#### rx-max-frames-low (`u32`)

#### tx-usecs-low (`u32`)

#### tx-max-frames-low (`u32`)

#### pkt-rate-high (`u32`)

#### rx-usecs-high (`u32`)

#### rx-max-frames-high (`u32`)

#### tx-usecs-high (`u32`)

#### tx-max-frames-high (`u32`)

#### rate-sample-interval (`u32`)

#### use-cqe-mode-tx (`u8`)

#### use-cqe-mode-rx (`u8`)

#### tx-aggr-max-bytes (`u32`)

#### tx-aggr-max-frames (`u32`)

#### tx-aggr-time-usecs (`u32`)

#### rx-profile (`nest`)

nested-attributes:
:   [profile](ethtool.md#ethtool-attribute-set-profile)

#### tx-profile (`nest`)

nested-attributes:
:   [profile](ethtool.md#ethtool-attribute-set-profile)

### [pause-stat](ethtool.md#id232)

#### unspec (`unused`)

value:
:   0

#### pad (`pad`)

#### tx-frames (`u64`)

#### rx-frames (`u64`)

### [pause](ethtool.md#id233)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### autoneg (`u8`)

#### rx (`u8`)

#### tx (`u8`)

#### stats (`nest`)

nested-attributes:
:   [pause-stat](ethtool.md#ethtool-attribute-set-pause-stat)

#### stats-src (`u32`)

### [eee](ethtool.md#id234)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### modes-ours (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### modes-peer (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### active (`u8`)

#### enabled (`u8`)

#### tx-lpi-enabled (`u8`)

#### tx-lpi-timer (`u32`)

### [ts-stat](ethtool.md#id235)

#### unspec (`unused`)

value:
:   0

#### tx-pkts (`uint`)

#### tx-lost (`uint`)

#### tx-err (`uint`)

#### tx-onestep-pkts-unconfirmed (`uint`)

### [ts-hwtstamp-provider](ethtool.md#id236)

#### unspec (`unused`)

value:
:   0

#### index (`u32`)

#### qualifier (`u32`)

### [tsinfo](ethtool.md#id237)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### timestamping (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### tx-types (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### rx-filters (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### phc-index (`u32`)

#### stats (`nest`)

nested-attributes:
:   [ts-stat](ethtool.md#ethtool-attribute-set-ts-stat)

#### hwtstamp-provider (`nest`)

nested-attributes:
:   [ts-hwtstamp-provider](ethtool.md#ethtool-attribute-set-ts-hwtstamp-provider)

#### hwtstamp-source (`u32`)

enum:
:   [hwtstamp-source](ethtool.md#ethtool-definition-hwtstamp-source)

#### hwtstamp-phyindex (`u32`)

### [cable-result](ethtool.md#id238)

#### unspec (`unused`)

value:
:   0

#### pair (`u8`)

doc:
:   ETHTOOL_A_CABLE_PAIR

#### code (`u8`)

doc:
:   ETHTOOL_A_CABLE_RESULT_CODE

#### src (`u32`)

doc:
:   ETHTOOL_A_CABLE_INF_SRC

### [cable-fault-length](ethtool.md#id239)

#### unspec (`unused`)

value:
:   0

#### pair (`u8`)

#### cm (`u32`)

#### src (`u32`)

### [cable-nest](ethtool.md#id240)

#### unspec (`unused`)

value:
:   0

#### result (`nest`)

nested-attributes:
:   [cable-result](ethtool.md#ethtool-attribute-set-cable-result)

#### fault-length (`nest`)

nested-attributes:
:   [cable-fault-length](ethtool.md#ethtool-attribute-set-cable-fault-length)

### [cable-test](ethtool.md#id241)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

### [cable-test-ntf](ethtool.md#id242)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### status (`u8`)

doc:
:   _STARTED/_COMPLETE

#### nest (`nest`)

nested-attributes:
:   [cable-nest](ethtool.md#ethtool-attribute-set-cable-nest)

### [cable-test-tdr-cfg](ethtool.md#id243)

#### unspec (`unused`)

value:
:   0

#### first (`u32`)

#### last (`u32`)

#### step (`u32`)

#### pair (`u8`)

### [cable-test-tdr-ntf](ethtool.md#id244)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### status (`u8`)

#### nest (`nest`)

nested-attributes:
:   [cable-nest](ethtool.md#ethtool-attribute-set-cable-nest)

### [cable-test-tdr](ethtool.md#id245)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### cfg (`nest`)

nested-attributes:
:   [cable-test-tdr-cfg](ethtool.md#ethtool-attribute-set-cable-test-tdr-cfg)

### [tunnel-udp-entry](ethtool.md#id246)

#### unspec (`unused`)

value:
:   0

#### port (`u16`)

byte-order:
:   big-endian

#### type (`u32`)

enum:
:   [udp-tunnel-type](ethtool.md#ethtool-definition-udp-tunnel-type)

### [tunnel-udp-table](ethtool.md#id247)

#### unspec (`unused`)

value:
:   0

#### size (`u32`)

#### types (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### entry (`nest`)

multi-attr:
:   True

nested-attributes:
:   [tunnel-udp-entry](ethtool.md#ethtool-attribute-set-tunnel-udp-entry)

### [tunnel-udp](ethtool.md#id248)

#### unspec (`unused`)

value:
:   0

#### table (`nest`)

nested-attributes:
:   [tunnel-udp-table](ethtool.md#ethtool-attribute-set-tunnel-udp-table)

### [tunnel-info](ethtool.md#id249)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### udp-ports (`nest`)

nested-attributes:
:   [tunnel-udp](ethtool.md#ethtool-attribute-set-tunnel-udp)

### [fec-stat](ethtool.md#id250)

#### unspec (`unused`)

value:
:   0

#### pad (`pad`)

#### corrected (`binary`)

sub-type:
:   u64

#### uncorr (`binary`)

sub-type:
:   u64

#### corr-bits (`binary`)

sub-type:
:   u64

### [fec](ethtool.md#id251)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### modes (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### auto (`u8`)

#### active (`u32`)

#### stats (`nest`)

nested-attributes:
:   [fec-stat](ethtool.md#ethtool-attribute-set-fec-stat)

### [module-eeprom](ethtool.md#id252)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### offset (`u32`)

#### length (`u32`)

#### page (`u8`)

#### bank (`u8`)

#### i2c-address (`u8`)

#### data (`binary`)

### [stats-grp](ethtool.md#id253)

#### unspec (`unused`)

value:
:   0

#### pad (`pad`)

#### id (`u32`)

#### ss-id (`u32`)

#### stat (`u64`)

type-value:
:   [‘id’]

#### hist-rx (`nest`)

nested-attributes:
:   [stats-grp-hist](ethtool.md#ethtool-attribute-set-stats-grp-hist)

#### hist-tx (`nest`)

nested-attributes:
:   [stats-grp-hist](ethtool.md#ethtool-attribute-set-stats-grp-hist)

#### hist-bkt-low (`u32`)

#### hist-bkt-hi (`u32`)

#### hist-val (`u64`)

### [stats-grp-hist](ethtool.md#id254)

#### hist-bkt-low

#### hist-bkt-hi

#### hist-val

### [stats](ethtool.md#id255)

#### unspec (`unused`)

value:
:   0

#### pad (`pad`)

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### groups (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### grp (`nest`)

nested-attributes:
:   [stats-grp](ethtool.md#ethtool-attribute-set-stats-grp)

#### src (`u32`)

### [phc-vclocks](ethtool.md#id256)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### num (`u32`)

#### index (`binary`)

sub-type:
:   s32

### [module](ethtool.md#id257)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### power-mode-policy (`u8`)

#### power-mode (`u8`)

### [c33-pse-pw-limit](ethtool.md#id258)

#### unspec (`unused`)

value:
:   0

#### min (`u32`)

#### max (`u32`)

### [pse](ethtool.md#id259)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### podl-pse-admin-state (`u32`)

name-prefix:
:   ethtool-a-

#### podl-pse-admin-control (`u32`)

name-prefix:
:   ethtool-a-

#### podl-pse-pw-d-status (`u32`)

name-prefix:
:   ethtool-a-

#### c33-pse-admin-state (`u32`)

name-prefix:
:   ethtool-a-

#### c33-pse-admin-control (`u32`)

name-prefix:
:   ethtool-a-

#### c33-pse-pw-d-status (`u32`)

name-prefix:
:   ethtool-a-

#### c33-pse-pw-class (`u32`)

name-prefix:
:   ethtool-a-

#### c33-pse-actual-pw (`u32`)

name-prefix:
:   ethtool-a-

#### c33-pse-ext-state (`u32`)

name-prefix:
:   ethtool-a-

enum:
:   [c33-pse-ext-state](ethtool.md#ethtool-definition-c33-pse-ext-state)

#### c33-pse-ext-substate (`u32`)

name-prefix:
:   ethtool-a-

#### c33-pse-avail-pw-limit (`u32`)

name-prefix:
:   ethtool-a-

#### c33-pse-pw-limit-ranges (`nest`)

name-prefix:
:   ethtool-a-

multi-attr:
:   True

nested-attributes:
:   [c33-pse-pw-limit](ethtool.md#ethtool-attribute-set-c33-pse-pw-limit)

#### pse-pw-d-id (`u32`)

name-prefix:
:   ethtool-a-

#### pse-prio-max (`u32`)

name-prefix:
:   ethtool-a-

#### pse-prio (`u32`)

name-prefix:
:   ethtool-a-

### [flow](ethtool.md#id260)

#### ether (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### ip4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### ip6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### tcp4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### tcp6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### udp4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### udp6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### sctp4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### sctp6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### ah4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### ah6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### esp4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### esp6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### ah-esp4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### ah-esp6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### gtpu4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### gtpu6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### gtpc4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### gtpc6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### gtpc-teid4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### gtpc-teid6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### gtpu-eh4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### gtpu-eh6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### gtpu-ul4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### gtpu-ul6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### gtpu-dl4 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

#### gtpu-dl6 (`uint`)

enum:
:   [rxfh-fields](ethtool.md#ethtool-definition-rxfh-fields)

### [rss](ethtool.md#id261)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### context (`u32`)

#### hfunc (`u32`)

#### indir (`binary`)

sub-type:
:   u32

#### hkey (`binary`)

#### input-xfrm (`u32`)

enum:
:   [input-xfrm](ethtool.md#ethtool-definition-input-xfrm)

#### start-context (`u32`)

#### flow-hash (`nest`)

nested-attributes:
:   [flow](ethtool.md#ethtool-attribute-set-flow)

### [plca](ethtool.md#id262)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### version (`u16`)

#### enabled (`u8`)

#### status (`u8`)

#### node-cnt (`u32`)

#### node-id (`u32`)

#### to-tmr (`u32`)

#### burst-cnt (`u32`)

#### burst-tmr (`u32`)

### [module-fw-flash](ethtool.md#id263)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### file-name (`string`)

#### password (`u32`)

#### status (`u32`)

enum:
:   [module-fw-flash-status](ethtool.md#ethtool-definition-module-fw-flash-status)

#### status-msg (`string`)

#### done (`uint`)

#### total (`uint`)

### [phy](ethtool.md#id264)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### index (`u32`)

#### drvname (`string`)

#### name (`string`)

#### upstream-type (`u32`)

enum:
:   [phy-upstream-type](ethtool.md#ethtool-definition-phy-upstream-type)

#### upstream-index (`u32`)

#### upstream-sfp-name (`string`)

#### downstream-sfp-name (`string`)

### [tsconfig](ethtool.md#id265)

#### unspec (`unused`)

value:
:   0

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### hwtstamp-provider (`nest`)

nested-attributes:
:   [ts-hwtstamp-provider](ethtool.md#ethtool-attribute-set-ts-hwtstamp-provider)

#### tx-types (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### rx-filters (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

#### hwtstamp-flags (`nest`)

nested-attributes:
:   [bitset](ethtool.md#ethtool-attribute-set-bitset)

### [pse-ntf](ethtool.md#id266)

#### header (`nest`)

nested-attributes:
:   [header](ethtool.md#ethtool-attribute-set-header)

#### events (`uint`)

enum:
:   [pse-event](ethtool.md#ethtool-definition-pse-event)

doc:
:   List of events reported by the PSE controller
