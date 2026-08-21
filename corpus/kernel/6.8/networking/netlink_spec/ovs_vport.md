---
collection: kernel
version: "6.8"
title: "Family ovs_vport netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/ovs_vport.html
fetched_at: 2026-08-21T03:49:20+00:00
---
# [Family `ovs_vport` netlink specification](ovs_vport.md#id1)

Contents

- [Family `ovs_vport` netlink specification](ovs_vport.md#family-ovs-vport-netlink-specification)

  - [Summary](ovs_vport.md#summary)
  - [Operations](ovs_vport.md#operations)

    - [new](ovs_vport.md#new)
    - [del](ovs_vport.md#del)
    - [get](ovs_vport.md#get)
  - [Multicast groups](ovs_vport.md#multicast-groups)
  - [Definitions](ovs_vport.md#definitions)

    - [ovs-header](ovs_vport.md#ovs-header)
    - [vport-type](ovs_vport.md#vport-type)
    - [vport-stats](ovs_vport.md#vport-stats)
  - [Attribute sets](ovs_vport.md#attribute-sets)

    - [vport-options](ovs_vport.md#vport-options)

      - [dst-port (`u32`)](ovs_vport.md#dst-port-u32)
      - [extension (`u32`)](ovs_vport.md#extension-u32)
    - [upcall-stats](ovs_vport.md#upcall-stats)

      - [success (`u64`)](ovs_vport.md#success-u64)
      - [fail (`u64`)](ovs_vport.md#fail-u64)
    - [vport](ovs_vport.md#vport)

      - [unspec (`unused`)](ovs_vport.md#unspec-unused)
      - [port-no (`u32`)](ovs_vport.md#port-no-u32)
      - [type (`u32`)](ovs_vport.md#type-u32)
      - [name (`string`)](ovs_vport.md#name-string)
      - [options (`nest`)](ovs_vport.md#options-nest)
      - [upcall-pid (`binary`)](ovs_vport.md#upcall-pid-binary)
      - [stats (`binary`)](ovs_vport.md#stats-binary)
      - [pad (`unused`)](ovs_vport.md#pad-unused)
      - [ifindex (`u32`)](ovs_vport.md#ifindex-u32)
      - [netnsid (`u32`)](ovs_vport.md#netnsid-u32)
      - [upcall-stats (`nest`)](ovs_vport.md#upcall-stats-nest)

## [Summary](ovs_vport.md#id2)

OVS vport configuration over generic netlink.

## [Operations](ovs_vport.md#id3)

### [new](ovs_vport.md#id4)

Create a new OVS vport

attribute-set
:   vport

fixed-header
:   ovs-header

do
:   **request**
    :   attributes
        :   [`name`, `type`, `upcall-pid`, `ifindex`, `options`]

### [del](ovs_vport.md#id5)

Delete existing OVS vport from a data path

attribute-set
:   vport

fixed-header
:   ovs-header

do
:   **request**
    :   attributes
        :   [`port-no`, `type`, `name`]

### [get](ovs_vport.md#id6)

Get / dump OVS vport configuration and state

attribute-set
:   vport

fixed-header
:   ovs-header

do
:   **request**
    :   attributes
        :   [`name`]

    **reply**
    :   attributes
        :   [`port-no`, `type`, `name`, `upcall-pid`, `stats`, `ifindex`, `netnsid`, `upcall-stats`]

dump
:   **request**
    :   attributes
        :   [`name`]

    **reply**
    :   attributes
        :   [`port-no`, `type`, `name`, `upcall-pid`, `stats`, `ifindex`, `netnsid`, `upcall-stats`]

## [Multicast groups](ovs_vport.md#id7)

- ovs_vport

## [Definitions](ovs_vport.md#id8)

### [ovs-header](ovs_vport.md#id9)

type
:   struct

members
:   dp-ifindex

### [vport-type](ovs_vport.md#id10)

type
:   enum

enum-name
:   ovs-vport-type

name-prefix
:   ovs-vport-type-

entries
:   - `unspec`
    - `netdev`
    - `internal`
    - `gre`
    - `vxlan`
    - `geneve`

### [vport-stats](ovs_vport.md#id11)

type
:   struct

enum-name
:   ovs-vport-stats

members
:   rx-packets

    tx-packets

    rx-bytes

    tx-bytes

    rx-errors

    tx-errors

    rx-dropped

    tx-dropped

## [Attribute sets](ovs_vport.md#id12)

### [vport-options](ovs_vport.md#id13)

#### [dst-port (`u32`)](ovs_vport.md#id14)

#### [extension (`u32`)](ovs_vport.md#id15)

### [upcall-stats](ovs_vport.md#id16)

#### [success (`u64`)](ovs_vport.md#id17)

value
:   0

#### [fail (`u64`)](ovs_vport.md#id18)

### [vport](ovs_vport.md#id19)

#### [unspec (`unused`)](ovs_vport.md#id20)

value
:   0

#### [port-no (`u32`)](ovs_vport.md#id21)

#### [type (`u32`)](ovs_vport.md#id22)

enum
:   vport-type

#### [name (`string`)](ovs_vport.md#id23)

#### [options (`nest`)](ovs_vport.md#id24)

nested-attributes
:   vport-options

#### [upcall-pid (`binary`)](ovs_vport.md#id25)

sub-type
:   u32

#### [stats (`binary`)](ovs_vport.md#id26)

struct
:   vport-stats

#### [pad (`unused`)](ovs_vport.md#id27)

#### [ifindex (`u32`)](ovs_vport.md#id28)

#### [netnsid (`u32`)](ovs_vport.md#id29)

#### [upcall-stats (`nest`)](ovs_vport.md#id30)

nested-attributes
:   upcall-stats
