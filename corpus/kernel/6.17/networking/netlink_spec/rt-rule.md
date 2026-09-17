---
collection: kernel
version: "6.17"
title: "Family rt-rule netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/rt-rule.html
fetched_at: 2026-09-16T16:40:59+00:00
---
# [Family `rt-rule` netlink specification](rt-rule.md#id1)

Contents

- [Family `rt-rule` netlink specification](rt-rule.md#family-rt-rule-netlink-specification)

  - [Summary](rt-rule.md#summary)
  - [Operations](rt-rule.md#operations)

    - [newrule](rt-rule.md#newrule)
    - [newrule-ntf](rt-rule.md#newrule-ntf)
    - [delrule](rt-rule.md#delrule)
    - [delrule-ntf](rt-rule.md#delrule-ntf)
    - [getrule](rt-rule.md#getrule)
  - [Multicast groups](rt-rule.md#multicast-groups)
  - [Definitions](rt-rule.md#definitions)

    - [rtgenmsg](rt-rule.md#rtgenmsg)
    - [fib-rule-hdr](rt-rule.md#fib-rule-hdr)
    - [fr-act](rt-rule.md#fr-act)
    - [fib-rule-port-range](rt-rule.md#fib-rule-port-range)
    - [fib-rule-uid-range](rt-rule.md#fib-rule-uid-range)
  - [Attribute sets](rt-rule.md#attribute-sets)

    - [fib-rule-attrs](rt-rule.md#fib-rule-attrs)

## [Summary](rt-rule.md#id2)

FIB rule management over rtnetlink.

## [Operations](rt-rule.md#id3)

### [newrule](rt-rule.md#id4)

Add new FIB rule

attribute-set:
:   [fib-rule-attrs](rt-rule.md#rt-rule-attribute-set-fib-rule-attrs)

do:
:   **request**
    :   attributes:
        :   [`iifname`, `oifname`, `priority`, `fwmark`, `flow`, `tun-id`, `fwmask`, `table`, `suppress-prefixlen`, `suppress-ifgroup`, `goto`, `l3mdev`, `uid-range`, `protocol`, `ip-proto`, `sport-range`, `dport-range`, `dscp`, `flowlabel`, `flowlabel-mask`, `sport-mask`, `dport-mask`, `dscp-mask`]

### [newrule-ntf](rt-rule.md#id5)

Notify a rule creation

value:
:   32

notify:
:   getrule

### [delrule](rt-rule.md#id6)

Remove an existing FIB rule

attribute-set:
:   [fib-rule-attrs](rt-rule.md#rt-rule-attribute-set-fib-rule-attrs)

do:
:   **request**
    :   attributes:
        :   [`iifname`, `oifname`, `priority`, `fwmark`, `flow`, `tun-id`, `fwmask`, `table`, `suppress-prefixlen`, `suppress-ifgroup`, `goto`, `l3mdev`, `uid-range`, `protocol`, `ip-proto`, `sport-range`, `dport-range`, `dscp`, `flowlabel`, `flowlabel-mask`, `sport-mask`, `dport-mask`, `dscp-mask`]

### [delrule-ntf](rt-rule.md#id7)

Notify a rule deletion

value:
:   33

notify:
:   getrule

### [getrule](rt-rule.md#id8)

Dump all FIB rules

attribute-set:
:   [fib-rule-attrs](rt-rule.md#rt-rule-attribute-set-fib-rule-attrs)

dump:
:   **request**

    **reply**
    :   attributes:
        :   [`iifname`, `oifname`, `priority`, `fwmark`, `flow`, `tun-id`, `fwmask`, `table`, `suppress-prefixlen`, `suppress-ifgroup`, `goto`, `l3mdev`, `uid-range`, `protocol`, `ip-proto`, `sport-range`, `dport-range`, `dscp`, `flowlabel`, `flowlabel-mask`, `sport-mask`, `dport-mask`, `dscp-mask`]

## [Multicast groups](rt-rule.md#id9)

- rtnlgrp-ipv4-rule
- rtnlgrp-ipv6-rule

## [Definitions](rt-rule.md#id10)

### [rtgenmsg](rt-rule.md#id11)

type:
:   struct

members:
:   family (`u8`):

### [fib-rule-hdr](rt-rule.md#id12)

type:
:   struct

members:
:   family (`u8`):

    dst-len (`u8`):

    src-len (`u8`):

    tos (`u8`):

    table (`u8`):

    res1 (`pad`):

    res2 (`pad`):

    action (`u8`):

    flags (`u32`):

### [fr-act](rt-rule.md#id13)

type:
:   enum

enum-name:
:   None

entries:
:   - `unspec`
    - `to-tbl`
    - `goto`
    - `nop`
    - `res3`
    - `res4`
    - `blackhole`
    - `unreachable`
    - `prohibit`

### [fib-rule-port-range](rt-rule.md#id14)

type:
:   struct

members:
:   start (`u16`):

    end (`u16`):

### [fib-rule-uid-range](rt-rule.md#id15)

type:
:   struct

members:
:   start (`u32`):

    end (`u32`):

## [Attribute sets](rt-rule.md#id16)

### [fib-rule-attrs](rt-rule.md#id17)

#### dst (`u32`)

#### src (`u32`)

#### iifname (`string`)

#### goto (`u32`)

#### unused2 (`pad`)

#### priority (`u32`)

#### unused3 (`pad`)

#### unused4 (`pad`)

#### unused5 (`pad`)

#### fwmark (`u32`)

display-hint:
:   hex

#### flow (`u32`)

#### tun-id (`u64`)

#### suppress-ifgroup (`u32`)

#### suppress-prefixlen (`u32`)

display-hint:
:   hex

#### table (`u32`)

#### fwmask (`u32`)

display-hint:
:   hex

#### oifname (`string`)

#### pad (`pad`)

#### l3mdev (`u8`)

#### uid-range (`binary`)

struct:
:   [fib-rule-uid-range](rt-rule.md#rt-rule-definition-fib-rule-uid-range)

#### protocol (`u8`)

#### ip-proto (`u8`)

#### sport-range (`binary`)

struct:
:   [fib-rule-port-range](rt-rule.md#rt-rule-definition-fib-rule-port-range)

#### dport-range (`binary`)

struct:
:   [fib-rule-port-range](rt-rule.md#rt-rule-definition-fib-rule-port-range)

#### dscp (`u8`)

#### flowlabel (`u32`)

byte-order:
:   big-endian

display-hint:
:   hex

#### flowlabel-mask (`u32`)

byte-order:
:   big-endian

display-hint:
:   hex

#### sport-mask (`u16`)

display-hint:
:   hex

#### dport-mask (`u16`)

display-hint:
:   hex

#### dscp-mask (`u8`)

display-hint:
:   hex
