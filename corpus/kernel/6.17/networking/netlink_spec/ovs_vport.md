---
collection: kernel
version: "6.17"
title: "Family ovs_vport netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/ovs_vport.html
fetched_at: 2026-09-16T16:40:55+00:00
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
    - [ovs-vport-stats](ovs_vport.md#ovs-vport-stats)
  - [Attribute sets](ovs_vport.md#attribute-sets)

    - [vport-options](ovs_vport.md#vport-options)
    - [upcall-stats](ovs_vport.md#upcall-stats)
    - [vport](ovs_vport.md#vport)

## [Summary](ovs_vport.md#id2)

OVS vport configuration over generic netlink.

## [Operations](ovs_vport.md#id3)

### [new](ovs_vport.md#id4)

Create a new OVS vport

attribute-set:
:   [vport](ovs_vport.md#ovs-vport-attribute-set-vport)

do:
:   **request**
    :   attributes:
        :   [`name`, `type`, `upcall-pid`, `ifindex`, `options`]

### [del](ovs_vport.md#id5)

Delete existing OVS vport from a data path

attribute-set:
:   [vport](ovs_vport.md#ovs-vport-attribute-set-vport)

do:
:   **request**
    :   attributes:
        :   [`port-no`, `type`, `name`]

### [get](ovs_vport.md#id6)

Get / dump OVS vport configuration and state

attribute-set:
:   [vport](ovs_vport.md#ovs-vport-attribute-set-vport)

do:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`port-no`, `type`, `name`, `upcall-pid`, `stats`, `ifindex`, `netnsid`, `upcall-stats`]

dump:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`port-no`, `type`, `name`, `upcall-pid`, `stats`, `ifindex`, `netnsid`, `upcall-stats`]

## [Multicast groups](ovs_vport.md#id7)

- ovs_vport

## [Definitions](ovs_vport.md#id8)

### [ovs-header](ovs_vport.md#id9)

type:
:   struct

members:
:   dp-ifindex (`u32`):

### [vport-type](ovs_vport.md#id10)

type:
:   enum

enum-name:
:   ovs-vport-type

name-prefix:
:   ovs-vport-type-

entries:
:   - `unspec`
    - `netdev`
    - `internal`
    - `gre`
    - `vxlan`
    - `geneve`

### [ovs-vport-stats](ovs_vport.md#id11)

type:
:   struct

members:
:   rx-packets (`u64`):

    tx-packets (`u64`):

    rx-bytes (`u64`):

    tx-bytes (`u64`):

    rx-errors (`u64`):

    tx-errors (`u64`):

    rx-dropped (`u64`):

    tx-dropped (`u64`):

## [Attribute sets](ovs_vport.md#id12)

### [vport-options](ovs_vport.md#id13)

#### dst-port (`u32`)

#### extension (`u32`)

### [upcall-stats](ovs_vport.md#id14)

#### success (`u64`)

value:
:   0

#### fail (`u64`)

### [vport](ovs_vport.md#id15)

#### unspec (`unused`)

value:
:   0

#### port-no (`u32`)

#### type (`u32`)

enum:
:   [vport-type](ovs_vport.md#ovs-vport-definition-vport-type)

#### name (`string`)

#### options (`nest`)

nested-attributes:
:   [vport-options](ovs_vport.md#ovs-vport-attribute-set-vport-options)

#### upcall-pid (`binary`)

sub-type:
:   u32

#### stats (`binary`)

struct:
:   [ovs-vport-stats](ovs_vport.md#ovs-vport-definition-ovs-vport-stats)

#### pad (`unused`)

#### ifindex (`u32`)

#### netnsid (`u32`)

#### upcall-stats (`nest`)

nested-attributes:
:   [upcall-stats](ovs_vport.md#ovs-vport-attribute-set-upcall-stats)
