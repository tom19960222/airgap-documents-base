---
collection: kernel
version: "6.8"
title: "Family nfsd netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/nfsd.html
fetched_at: 2026-08-21T03:49:18+00:00
---
# [Family `nfsd` netlink specification](nfsd.md#id1)

Contents

- [Family `nfsd` netlink specification](nfsd.md#family-nfsd-netlink-specification)

  - [Summary](nfsd.md#summary)
  - [Operations](nfsd.md#operations)

    - [rpc-status-get](nfsd.md#rpc-status-get)
  - [Attribute sets](nfsd.md#attribute-sets)

    - [rpc-status](nfsd.md#rpc-status)

      - [xid (`u32`)](nfsd.md#xid-u32)
      - [flags (`u32`)](nfsd.md#flags-u32)
      - [prog (`u32`)](nfsd.md#prog-u32)
      - [version (`u8`)](nfsd.md#version-u8)
      - [proc (`u32`)](nfsd.md#proc-u32)
      - [service_time (`s64`)](nfsd.md#service-time-s64)
      - [pad (`pad`)](nfsd.md#pad-pad)
      - [saddr4 (`u32`)](nfsd.md#saddr4-u32)
      - [daddr4 (`u32`)](nfsd.md#daddr4-u32)
      - [saddr6 (`binary`)](nfsd.md#saddr6-binary)
      - [daddr6 (`binary`)](nfsd.md#daddr6-binary)
      - [sport (`u16`)](nfsd.md#sport-u16)
      - [dport (`u16`)](nfsd.md#dport-u16)
      - [compound-ops (`u32`)](nfsd.md#compound-ops-u32)

## [Summary](nfsd.md#id2)

NFSD configuration over generic netlink.

## [Operations](nfsd.md#id3)

### [rpc-status-get](nfsd.md#id4)

dump pending nfsd rpc

attribute-set
:   rpc-status

dump
:   **pre**

    **post**

    **reply**
    :   attributes
        :   [`xid`, `flags`, `prog`, `version`, `proc`, `service_time`, `saddr4`, `daddr4`, `saddr6`, `daddr6`, `sport`, `dport`, `compound-ops`]

## [Attribute sets](nfsd.md#id5)

### [rpc-status](nfsd.md#id6)

#### [xid (`u32`)](nfsd.md#id7)

byte-order
:   big-endian

#### [flags (`u32`)](nfsd.md#id8)

#### [prog (`u32`)](nfsd.md#id9)

#### [version (`u8`)](nfsd.md#id10)

#### [proc (`u32`)](nfsd.md#id11)

#### [service_time (`s64`)](nfsd.md#id12)

#### [pad (`pad`)](nfsd.md#id13)

#### [saddr4 (`u32`)](nfsd.md#id14)

byte-order
:   big-endian

display-hint
:   ipv4

#### [daddr4 (`u32`)](nfsd.md#id15)

byte-order
:   big-endian

display-hint
:   ipv4

#### [saddr6 (`binary`)](nfsd.md#id16)

display-hint
:   ipv6

#### [daddr6 (`binary`)](nfsd.md#id17)

display-hint
:   ipv6

#### [sport (`u16`)](nfsd.md#id18)

byte-order
:   big-endian

#### [dport (`u16`)](nfsd.md#id19)

byte-order
:   big-endian

#### [compound-ops (`u32`)](nfsd.md#id20)

multi-attr
:   True
